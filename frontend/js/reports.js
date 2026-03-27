// Reports module — spending analytics, vendor breakdowns, budget reports (admin only)
function reportsModule() {
    function _reportsHeaders(sid) {
        if (!sid) return {};
        const h = { 'X-Session-ID': sid };
        if (sid === 'demo') {
            try {
                const s = JSON.parse(localStorage.getItem('eds-session'));
                const lvl = s.session && s.session.approval_level;
                if (lvl !== undefined && lvl !== null) h['X-Demo-Approval-Level'] = String(lvl);
            } catch { /* ignore */ }
        }
        return h;
    }
    return {
        // --- Reports state ---
        reportsLoading: false,
        reportsLoaded: false,
        reportsTab: 'overview',    // overview | vendors | categories | orders
        reportsPeriod: 'current',  // current | previous | ytd | custom
        reportsPeriodLabel: 'Dec 2025 - Nov 2026',

        // --- Custom date range ---
        reportsCustomStart: '',
        reportsCustomEnd: '',
        showReportsDatePicker: false,

        // --- Drill-down ---
        reportsDrilldown: null,
        reportsDrilldownLoading: false,
        showReportsDrilldown: false,

        // --- Report data ---
        reportsSummary: null,
        reportsVendorSpend: [],
        reportsCategorySpend: [],
        reportsMonthlyTrend: [],
        reportsRecentOrders: [],
        reportsBudgetDepts: [],

        // --- Fetch reports data ---
        async fetchReportsData() {
            if (this.reportsLoaded && this.reportsPeriod === 'current') return;
            this.reportsLoading = true;
            try {
                // Call reports API with session and period
                const sid = this._getSessionId();
                const params = new URLSearchParams({ period: this.reportsPeriod });
                if (this.reportsPeriod === 'custom' && this.reportsCustomStart && this.reportsCustomEnd) {
                    params.set('date_start', this.reportsCustomStart);
                    params.set('date_end', this.reportsCustomEnd);
                }
                const r = await fetch('/api/reports/summary?' + params, {
                    headers: _reportsHeaders(sid)
                });
                if (r.ok) {
                    const d = await r.json();
                    this._applyReportsData(d);
                    // Update period label from server date range
                    if (d.date_range) {
                        const start = new Date(d.date_range.start);
                        const end = new Date(d.date_range.end);
                        const fmt = (dt) => dt.toLocaleDateString('en-US', { month: 'short', year: 'numeric' });
                        this.reportsPeriodLabel = fmt(start) + ' - ' + fmt(end);
                    }
                    this.reportsLoaded = true;
                    this.reportsLoading = false;
                    return;
                }
            } catch (e) {
                console.error('Reports API error:', e.message);
            }
            this.reportsLoading = false;
        },

        _applyReportsData(d) {
            this.reportsSummary = d.summary || null;
            this.reportsVendorSpend = d.vendor_spend || [];
            this.reportsCategorySpend = d.category_spend || [];
            this.reportsMonthlyTrend = d.monthly_trend || [];
            this.reportsRecentOrders = d.recent_orders || [];
            this.reportsBudgetDepts = d.budget_departments || [];
        },

        // --- Period switching ---
        setReportsPeriod(period) {
            if (this.reportsPeriod === period && this.reportsLoaded) return;
            this.reportsPeriod = period;
            // Temporary label until server responds with actual date range
            const labels = {
                current: 'Loading current year...',
                previous: 'Loading previous year...',
                ytd: 'Loading year to date...',
            };
            this.reportsPeriodLabel = labels[period] || 'Custom Range';
            this.reportsLoaded = false;
            this.fetchReportsData();
        },

        // --- Custom date range ---
        applyCustomDateRange() {
            if (!this.reportsCustomStart || !this.reportsCustomEnd) return;
            if (this.reportsCustomStart > this.reportsCustomEnd) {
                if (this.showToast) this.showToast('Start date must be before end date', 'fas fa-exclamation-triangle', 'var(--color-accent-500)');
                return;
            }
            this.reportsPeriod = 'custom';
            this.reportsPeriodLabel = 'Loading custom range...';
            this.showReportsDatePicker = false;
            this.reportsLoaded = false;
            this.fetchReportsData();
        },

        // --- Drill-down ---
        async reportsDrillVendor(vendor) {
            this.reportsDrilldownLoading = true;
            this.showReportsDrilldown = true;
            try {
                const sid = this._getSessionId();
                const params = new URLSearchParams({
                    vendor_code: vendor.code,
                    period: this.reportsPeriod,
                });
                if (this.reportsPeriod === 'custom' && this.reportsCustomStart && this.reportsCustomEnd) {
                    params.set('date_start', this.reportsCustomStart);
                    params.set('date_end', this.reportsCustomEnd);
                }
                const r = await fetch('/api/reports/drilldown/vendor?' + params, {
                    headers: _reportsHeaders(sid)
                });
                if (r.ok) {
                    this.reportsDrilldown = await r.json();
                    this.reportsDrilldown._type = 'vendor';
                }
            } catch (e) { console.error('Vendor drilldown error:', e); }
            finally { this.reportsDrilldownLoading = false; }
        },

        async reportsDrillCategory(category) {
            this.reportsDrilldownLoading = true;
            this.showReportsDrilldown = true;
            try {
                const sid = this._getSessionId();
                const params = new URLSearchParams({
                    category_name: category.name,
                    period: this.reportsPeriod,
                });
                if (this.reportsPeriod === 'custom' && this.reportsCustomStart && this.reportsCustomEnd) {
                    params.set('date_start', this.reportsCustomStart);
                    params.set('date_end', this.reportsCustomEnd);
                }
                const r = await fetch('/api/reports/drilldown/category?' + params, {
                    headers: _reportsHeaders(sid)
                });
                if (r.ok) {
                    this.reportsDrilldown = await r.json();
                    this.reportsDrilldown._type = 'category';
                }
            } catch (e) { console.error('Category drilldown error:', e); }
            finally { this.reportsDrilldownLoading = false; }
        },

        closeDrilldown() {
            this.showReportsDrilldown = false;
            this.reportsDrilldown = null;
        },

        // --- CSV Export ---
        reportsExporting: false,
        async reportsExportCSV(section) {
            this.reportsExporting = true;
            try {
                const sid = this._getSessionId();
                const params = new URLSearchParams({ period: this.reportsPeriod, section: section || 'all' });
                const r = await fetch('/api/reports/export?' + params, {
                    headers: _reportsHeaders(sid)
                });
                if (!r.ok) throw new Error('Export failed');
                const blob = await r.blob();
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                // Extract filename from Content-Disposition header or use default
                const cd = r.headers.get('Content-Disposition') || '';
                const match = cd.match(/filename="?([^"]+)"?/);
                a.download = match ? match[1] : 'eds-reports-' + (section || 'all') + '.csv';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                if (this.showToast) this.showToast('Report exported successfully', 'fas fa-download', 'var(--color-success-500)');
            } catch (e) {
                console.error('Export error:', e);
                if (this.showToast) this.showToast('Export failed — try again', 'fas fa-exclamation-triangle', 'var(--color-accent-500)');
            } finally {
                this.reportsExporting = false;
            }
        },

        // --- PDF Export ---
        async reportsExportPDF() {
            this.reportsExporting = true;
            try {
                const sid = this._getSessionId();
                const params = new URLSearchParams({ period: this.reportsPeriod });
                const r = await fetch('/api/reports/export/pdf?' + params, {
                    headers: _reportsHeaders(sid)
                });
                if (!r.ok) throw new Error('PDF export failed');
                const blob = await r.blob();
                const url = URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                const cd = r.headers.get('Content-Disposition') || '';
                const match = cd.match(/filename="?([^"]+)"?/);
                a.download = match ? match[1] : 'eds-reports.pdf';
                document.body.appendChild(a);
                a.click();
                document.body.removeChild(a);
                URL.revokeObjectURL(url);
                if (this.showToast) this.showToast('PDF report downloaded', 'fas fa-file-pdf', 'var(--color-success-500)');
            } catch (e) {
                console.error('PDF export error:', e);
                if (this.showToast) this.showToast('PDF export failed — try again', 'fas fa-exclamation-triangle', 'var(--color-accent-500)');
            } finally {
                this.reportsExporting = false;
            }
        },

        // --- Formatting helpers ---
        reportsFmtCurrency(val) {
            if (val == null) return '$0';
            if (val >= 1000000) return '$' + (val / 1000000).toFixed(1) + 'M';
            if (val >= 1000) return '$' + (val / 1000).toFixed(1) + 'K';
            return '$' + val.toLocaleString(undefined, { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        },

        reportsFmtNumber(val) {
            if (val == null) return '0';
            return val.toLocaleString();
        },

        reportsFmtPercent(val) {
            if (val == null) return '0%';
            return val.toFixed(1) + '%';
        },

        // --- Bar width for horizontal charts ---
        reportsBarWidth(val, max) {
            if (!max || !val) return '0%';
            return Math.max(2, (val / max) * 100).toFixed(1) + '%';
        },

        // --- Trend sparkline (CSS bar chart heights) ---
        reportsTrendHeight(val) {
            if (!this.reportsMonthlyTrend.length) return '0%';
            const max = Math.max(...this.reportsMonthlyTrend.map(m => m.amount));
            if (!max) return '0%';
            return Math.max(4, (val / max) * 100).toFixed(0) + '%';
        },

        reportsTrendColor(val) {
            if (!this.reportsMonthlyTrend.length) return 'var(--color-primary-300)';
            const max = Math.max(...this.reportsMonthlyTrend.map(m => m.amount));
            const pct = val / max;
            if (pct > 0.8) return 'var(--color-primary-500)';
            if (pct > 0.5) return 'var(--color-primary-400)';
            return 'var(--color-primary-300)';
        },

        // --- Status badge class ---
        reportsStatusClass(status) {
            const s = (status || '').toLowerCase();
            if (s === 'approved' || s === 'fulfilled') return 'badge-success';
            if (s === 'submitted' || s === 'pending approval') return 'badge-warning';
            if (s === 'draft') return 'badge-info';
            if (s === 'rejected' || s === 'cancelled') return 'badge-accent';
            return 'badge-neutral';
        },

        // --- Budget health color ---
        reportsBudgetColor(pct) {
            if (pct >= 90) return 'var(--color-accent-500)';
            if (pct >= 75) return 'var(--color-warning-500)';
            return 'var(--color-success-500)';
        },

        reportsBudgetStatus(pct) {
            if (pct >= 90) return 'Critical';
            if (pct >= 75) return 'Warning';
            if (pct >= 50) return 'On Track';
            return 'Healthy';
        },

    };
}
