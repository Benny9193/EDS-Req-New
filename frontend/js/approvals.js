// Approvals module — only used by users with approver/admin role
function approvalsModule() {
    return {
        approvalReqs: [],
        approvalsLoading: false,
        approvalsLoadingMore: false,
        approvalsError: '',
        approvalsTotal: 0,
        approvalsPage: 1,
        approvalsPageSize: 20,
        approvalsSearch: '',
        _approvalsScrollHandler: null,
        _approvalsSearchTimer: null,

        // Detail / action state
        selectedApproval: null,
        approvalDetailItems: [],
        approvalDetailLoading: false,
        showApprovalDetail: false,

        // Approve dialog
        showApproveDialog: false,
        approveTarget: null,
        approveComments: '',
        approveSubmitting: false,

        // Reject dialog
        showRejectDialog: false,
        rejectTarget: null,
        rejectReason: '',
        rejectSubmitting: false,

        async fetchPendingApprovals(reset = true) {
            const sid = this._getSessionId();
            if (!sid) return;
            if (reset) {
                this.approvalsPage = 1;
                this.approvalsLoading = true;
                this.approvalsError = '';
            } else {
                this.approvalsLoadingMore = true;
            }
            try {
                const params = new URLSearchParams({
                    session_id: sid,
                    page: this.approvalsPage,
                    page_size: this.approvalsPageSize
                });
                if (this.approvalsSearch.trim()) {
                    params.set('search', this.approvalsSearch.trim());
                }
                const result = await edsApi.get('/api/requisitions/pending/list?' + params.toString(), { silent: true });
                if (result.ok) {
                    const items = result.data.items || [];
                    if (reset) {
                        this.approvalReqs = items;
                    } else {
                        this.approvalReqs = [...this.approvalReqs, ...items];
                    }
                    this.approvalsTotal = result.data.total || 0;
                    this.pendingApprovalCount = this.approvalsTotal;
                    this._setupApprovalsScroll();
                } else if (result.status === 403) {
                    this.approvalsError = 'You do not have approval privileges.';
                    this.approvalReqs = [];
                } else {
                    this.approvalsError = 'Failed to load pending approvals.';
                }
            } catch (e) {
                console.error('Fetch pending approvals error:', e);
                this.approvalsError = 'Network error loading approvals.';
            } finally {
                this.approvalsLoading = false;
                this.approvalsLoadingMore = false;
            }
        },

        _setupApprovalsScroll() {
            if (this._approvalsScrollHandler) return;
            this._approvalsScrollHandler = () => {
                if (this.activeView !== 'approvals') return;
                if (this.approvalsLoadingMore || this.approvalsLoading) return;
                if (this.approvalReqs.length >= this.approvalsTotal) return;
                const scrollY = window.innerHeight + window.scrollY;
                const threshold = document.body.offsetHeight - 400;
                if (scrollY >= threshold) {
                    this.approvalsPage++;
                    this.fetchPendingApprovals(false);
                }
            };
            window.addEventListener('scroll', this._approvalsScrollHandler, { passive: true });
        },

        approvalsSearchInput() {
            clearTimeout(this._approvalsSearchTimer);
            this._approvalsSearchTimer = setTimeout(() => {
                this.fetchPendingApprovals(true);
            }, 400);
        },

        clearApprovalsSearch() {
            this.approvalsSearch = '';
            this.fetchPendingApprovals(true);
        },

        // NOTE: approvalsHasMore getter lives in app.js (getters can't survive spread)

        async openApprovalDetail(req) {
            this.selectedApproval = req;
            this.approvalDetailItems = [];
            this.approvalDetailLoading = true;
            this.showApprovalDetail = true;
            const sid = this._getSessionId();
            try {
                const result = await edsApi.get('/api/requisitions/' + encodeURIComponent(req.requisition_id) + '/items?session_id=' + encodeURIComponent(sid), { silent: true });
                if (result.ok) {
                    this.approvalDetailItems = result.data;
                }
            } catch (e) { console.error('Approval detail fetch error:', e); }
            finally { this.approvalDetailLoading = false; }
        },

        closeApprovalDetail() {
            this.showApprovalDetail = false;
            this.selectedApproval = null;
            this.approvalDetailItems = [];
        },

        // --- Approve flow ---
        promptApprove(req) {
            this.approveTarget = req;
            this.approveComments = '';
            this.showApproveDialog = true;
        },

        async confirmApprove() {
            if (!this.approveTarget || this.approveSubmitting) return;
            this.approveSubmitting = true;
            const sid = this._getSessionId();
            try {
                const r = await fetch('/api/requisitions/' + encodeURIComponent(this.approveTarget.requisition_id) + '/approve', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        session_id: isNaN(parseInt(sid)) ? sid : parseInt(sid),
                        comments: this.approveComments.trim() || null
                    })
                });
                if (r.ok) {
                    this.showToast('Requisition ' + (this.approveTarget.requisition_number || '') + ' approved', 'fas fa-check-circle', 'var(--color-success-500)');
                    this.showApproveDialog = false;
                    this.showApprovalDetail = false;
                    this.approveTarget = null;
                    await this.fetchPendingApprovals();
                } else {
                    const err = await r.json().catch(() => ({}));
                    this.showToast(err.detail || 'Failed to approve', 'fas fa-exclamation-circle', 'var(--color-accent-500)');
                }
            } catch (e) {
                console.error('Approve error:', e);
                this.showToast('Network error during approval', 'fas fa-exclamation-circle', 'var(--color-accent-500)');
            } finally {
                this.approveSubmitting = false;
            }
        },

        cancelApprove() {
            this.showApproveDialog = false;
            this.approveTarget = null;
            this.approveComments = '';
        },

        // --- Reject flow ---
        promptReject(req) {
            this.rejectTarget = req;
            this.rejectReason = '';
            this.showRejectDialog = true;
        },

        async confirmReject() {
            if (!this.rejectTarget || this.rejectSubmitting) return;
            if (this.rejectReason.trim().length < 10) {
                this.showToast('Rejection reason must be at least 10 characters', 'fas fa-exclamation-triangle', 'var(--color-warning-500)');
                return;
            }
            this.rejectSubmitting = true;
            const sid = this._getSessionId();
            try {
                const r = await fetch('/api/requisitions/' + encodeURIComponent(this.rejectTarget.requisition_id) + '/reject', {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        session_id: isNaN(parseInt(sid)) ? sid : parseInt(sid),
                        reason: this.rejectReason.trim()
                    })
                });
                if (r.ok) {
                    this.showToast('Requisition ' + (this.rejectTarget.requisition_number || '') + ' rejected', 'fas fa-times-circle', 'var(--color-accent-500)');
                    this.showRejectDialog = false;
                    this.showApprovalDetail = false;
                    this.rejectTarget = null;
                    await this.fetchPendingApprovals();
                } else {
                    const err = await r.json().catch(() => ({}));
                    this.showToast(err.detail || 'Failed to reject', 'fas fa-exclamation-circle', 'var(--color-accent-500)');
                }
            } catch (e) {
                console.error('Reject error:', e);
                this.showToast('Network error during rejection', 'fas fa-exclamation-circle', 'var(--color-accent-500)');
            } finally {
                this.rejectSubmitting = false;
            }
        },

        cancelReject() {
            this.showRejectDialog = false;
            this.rejectTarget = null;
            this.rejectReason = '';
        },

        // --- Helpers ---
        approvalTimeAgo(dateStr) {
            if (!dateStr) return '';
            const d = new Date(dateStr);
            const now = new Date();
            const diffMs = now - d;
            const days = Math.floor(diffMs / 86400000);
            if (days > 1) return days + ' days ago';
            if (days === 1) return 'Yesterday';
            const hours = Math.floor(diffMs / 3600000);
            if (hours > 0) return hours + 'h ago';
            const mins = Math.floor(diffMs / 60000);
            return mins > 0 ? mins + 'm ago' : 'Just now';
        }
    };
}
