// Authentication and session management
function authModule() {
    return {
        user: null,
        isAdmin: false,
        canViewReports: false,
        showUserMenu: false,
        _sessionCheckInterval: null,

        _getSessionId() {
            // Delegate to shared getSessionId() from auth-guard.js (single source of truth)
            return typeof getSessionId === 'function' ? getSessionId() : null;
        },

        async _initAuth() {
            const session = localStorage.getItem('eds-session');
            if (!session) { window.location.href = 'login.html'; return false; }
            try {
                const s = JSON.parse(session);
                if (!s.session_id) { window.location.href = 'login.html'; return false; }
                if (s.session_id !== 'demo') {
                    const r = await fetch('/api/auth/session/' + encodeURIComponent(s.session_id));
                    const d = await r.json();
                    if (!r.ok || !d.valid) { localStorage.removeItem('eds-session'); window.location.href = 'login.html'; return false; }
                }
                this.user = s.user || s;
                if (s.district) window._edsDistrict = s.district;

                // Determine admin/approver status from approval_level (the real EDS indicator)
                // approval_level lives in s.session (from login API) or can be checked via role for demo
                const approvalLevel = (s.session && s.session.approval_level) || s.approval_level || 0;
                const role = (this.user.role || this.user.UserType || this.user.user_type || '').toLowerCase();
                this.isAdmin = approvalLevel >= 1 || ['admin', 'administrator', 'approver', 'manager'].includes(role);
                this.canViewReports = this.isAdmin || ['reports_viewer', 'department_head', 'principal'].includes(role);
                return true;
            } catch { window.location.href = 'login.html'; return false; }
        },

        _startSessionCheck() {
            this._sessionCheckInterval = setInterval(async () => {
                const sid = this._getSessionId();
                if (!sid || sid === 'demo') return;
                try {
                    // Touch first to reset inactivity timer
                    await fetch('/api/auth/session/' + encodeURIComponent(sid) + '/touch', { method: 'POST' });
                    // Then validate session is still good
                    const r = await fetch('/api/auth/session/' + encodeURIComponent(sid));
                    const d = await r.json();
                    if (!r.ok || !d.valid) {
                        clearInterval(this._sessionCheckInterval);
                        localStorage.removeItem('eds-session');
                        window.location.href = 'login.html';
                    }
                } catch {}
            }, 5 * 60 * 1000);
        },

        userInitials() {
            if (!this.user) return '?';
            const f = (this.user.first_name || this.user.FirstName || '')[0] || '';
            const l = (this.user.last_name || this.user.LastName || '')[0] || '';
            return (f + l).toUpperCase() || '?';
        },

        userName() {
            if (!this.user) return 'User';
            const f = this.user.first_name || this.user.FirstName || '';
            const l = this.user.last_name || this.user.LastName || '';
            return (f + ' ' + l).trim() || 'User';
        },

        getUserDisplayName() {
            if (!this.user) return '';
            const first = this.user.first_name || this.user.FirstName;
            const last = this.user.last_name || this.user.LastName;
            if (first && last) return first + ' ' + last;
            if (first) return first;
            const dist = this.user.district_name || (window._edsDistrict && window._edsDistrict.district_name) || '';
            if (dist) return dist.replace(/\s*\(.*\)\s*$/, '');
            return '';
        },

        async logout() {
            if (this._sessionCheckInterval) {
                clearInterval(this._sessionCheckInterval);
                this._sessionCheckInterval = null;
            }
            // Invalidate server session before clearing local state
            const sid = this._getSessionId();
            if (sid && sid !== 'demo') {
                try {
                    await fetch('/api/auth/logout?session_id=' + encodeURIComponent(sid), {
                        method: 'POST'
                    });
                } catch (e) { /* proceed with logout even if server call fails */ }
            }
            localStorage.removeItem('eds-session');
            localStorage.removeItem('eds_cart');
            window.location.href = 'login.html';
        }
    };
}
