// Dashboard module: budget, alerts, approver info, pending approvals
function dashboardModule() {
    return {
        // --- Dashboard data ---
        dashboardSummary: null,
        dashboardAlerts: [],
        dashboardBudget: null,
        dashboardDeptBudget: null,
        dashboardPendingApprovals: { count: 0, urgent: 0, oldest_days: 0 },
        dashboardOrderCounts: {},
        dashboardApproverInfo: null,
        dashboardRecentActivity: [],
        _dashboardRefreshInterval: null,

        async fetchDashboardSummary() {
            const sid = this._getSessionId();
            if (!sid) return;
            try {
                const hdrs = { 'X-Session-ID': sid };
                if (sid === 'demo') {
                    try {
                        const s = JSON.parse(localStorage.getItem('eds-session'));
                        const lvl = s.session && s.session.approval_level;
                        if (lvl !== undefined && lvl !== null) hdrs['X-Demo-Approval-Level'] = String(lvl);
                    } catch { /* ignore */ }
                }
                const r = await fetch('/api/dashboard/summary', { headers: hdrs });
                if (!r.ok) return;
                const d = await r.json();
                this.dashboardSummary = d;
                this.dashboardAlerts = d.alerts || [];
                this.dashboardBudget = d.budget || null;
                this.dashboardDeptBudget = d.department_budget || null;
                this.dashboardPendingApprovals = d.pending_approvals || { count: 0, urgent: 0, oldest_days: 0 };
                this.dashboardOrderCounts = d.order_counts || {};
                this.dashboardApproverInfo = d.approver_info || null;
                this.dashboardRecentActivity = d.recent_activity || [];
                // Update the global pending count used by sidebar badge
                if (d.pending_approvals) {
                    this.pendingApprovalCount = d.pending_approvals.count;
                }
            } catch (e) {
                console.error('Dashboard summary fetch error:', e);
            }
        },

        // --- Auto-refresh: poll every 5 minutes ---
        startDashboardRefresh() {
            this.stopDashboardRefresh();
            this._dashboardRefreshInterval = setInterval(() => {
                if (this.activeView === 'dashboard') {
                    this.fetchDashboardSummary();
                }
            }, 5 * 60 * 1000);
        },

        stopDashboardRefresh() {
            if (this._dashboardRefreshInterval) {
                clearInterval(this._dashboardRefreshInterval);
                this._dashboardRefreshInterval = null;
            }
        },

        // --- Budget display helpers ---
        budgetBarColor() {
            if (!this.dashboardBudget) return 'var(--color-primary-500)';
            const pct = this.dashboardBudget.percent;
            if (pct >= 90) return 'var(--color-accent-500)';
            if (pct >= 75) return 'var(--color-warning-500)';
            return 'var(--color-primary-500)';
        },

        budgetStatusLabel() {
            if (!this.dashboardBudget) return '';
            const pct = this.dashboardBudget.percent;
            if (pct >= 90) return 'Critical';
            if (pct >= 75) return 'Warning';
            if (pct >= 50) return 'On Track';
            return 'Healthy';
        },

        deptBudgetBarColor() {
            if (!this.dashboardDeptBudget) return 'var(--color-primary-400)';
            const pct = this.dashboardDeptBudget.percent;
            if (pct >= 90) return 'var(--color-accent-500)';
            if (pct >= 75) return 'var(--color-warning-500)';
            return 'var(--color-primary-400)';
        },

        deptBudgetStatusLabel() {
            if (!this.dashboardDeptBudget) return '';
            const pct = this.dashboardDeptBudget.percent;
            if (pct >= 90) return 'Critical';
            if (pct >= 75) return 'Warning';
            if (pct >= 50) return 'On Track';
            return 'Healthy';
        },

        // --- Recent Activity helpers ---
        activityStatusIcon(status) {
            const s = (status || '').toLowerCase();
            if (s === 'approved') return 'fas fa-check-circle';
            if (s === 'submitted') return 'fas fa-paper-plane';
            if (s.includes('pending')) return 'fas fa-hourglass-half';
            if (s === 'draft') return 'fas fa-pencil-alt';
            if (s === 'rejected' || s === 'cancelled') return 'fas fa-times-circle';
            return 'fas fa-circle';
        },

        activityStatusColor(status) {
            const s = (status || '').toLowerCase();
            if (s === 'approved') return 'var(--color-success-600)';
            if (s === 'submitted') return 'var(--color-primary-500)';
            if (s.includes('pending')) return 'var(--color-warning-600)';
            if (s === 'draft') return 'var(--text-muted)';
            if (s === 'rejected' || s === 'cancelled') return 'var(--color-accent-500)';
            return 'var(--text-muted)';
        },

        // --- Alert dismiss ---
        dismissedAlerts: [],

        dismissAlert(index) {
            this.dismissedAlerts.push(index);
        },

        visibleAlerts() {
            return this.dashboardAlerts.filter((alert, i) => {
                if (this.dismissedAlerts.includes(i)) return false;
                // Hide approval-related alerts for non-approvers
                if (!this.isAdmin && alert.title && alert.title.toLowerCase().includes('approval')) return false;
                return true;
            });
        },
    };
}
