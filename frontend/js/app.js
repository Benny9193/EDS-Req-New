// Main app composition - merges all modules into a single Alpine.js component
function app() {
    return {
        // --- Core UI state ---
        ready: false,
        mobileMenuOpen: false,
        showProductModal: false,
        selectedProduct: null,
        activeView: 'dashboard',

        // --- Data ---
        dashboardLoading: true,
        products: [],
        totalProductCount: 0,
        vendors: [],
        categories: [],

        // --- Templates ---
        templateTab: 'all',
        expandedTemplate: null,
        templates: [],
        templatesLoading: false,
        showSaveTemplateDialog: false,
        newTemplateName: '',
        newTemplateCategory: 'Custom',
        newTemplateDescription: '',

        // --- Getters (must be defined here, not in modules — spread flattens getters to static values) ---

        get cartTotal() {
            return edsCart.total(this.cart);
        },

        get filteredVendorList() {
            return this.vendors;
        },

        get filteredOrders() {
            if (this.ordersTab === 'all') return this.orders;
            if (this.ordersTab === 'active') return this.orders.filter(o => ['Approved', 'At EDS', 'PO Printed'].includes(o.status));
            if (this.ordersTab === 'pending') return this.orders.filter(o => ['On Hold', 'Draft', 'Submitted', 'Pending Approval'].includes(o.status));
            if (this.ordersTab === 'completed') return this.orders.filter(o => ['Fulfilled', 'Cancelled', 'Rejected'].includes(o.status));
            return this.orders;
        },

        get browseActiveFilters() {
            const filters = [];
            if (this.browseCategory) filters.push({ key: 'category', label: 'Category: ' + this.browseCategory });
            if (this.browseVendor) filters.push({ key: 'vendor', label: 'Vendor: ' + this.browseVendor });
            if (this.browseBidId) {
                const bid = this.availableBids.find(b => String(b.bid_id) === String(this.browseBidId));
                filters.push({ key: 'bid', label: 'Contract: ' + (bid ? bid.bid_name : this.browseBidId) });
            }
            if (this.browseQuery.trim()) filters.push({ key: 'query', label: 'Search: ' + this.browseQuery.trim() });
            if (this.browseMinPrice !== '' || this.browseMaxPrice !== '') {
                const min = this.browseMinPrice !== '' ? '$' + this.browseMinPrice : '$0';
                const max = this.browseMaxPrice !== '' ? '$' + this.browseMaxPrice : '...';
                filters.push({ key: 'price', label: 'Price: ' + min + ' - ' + max });
            }
            return filters;
        },

        get browsePageNumbers() {
            const pages = [];
            const total = this.browseTotalPages;
            const current = this.browsePage;
            const delta = 2;
            for (let i = Math.max(1, current - delta); i <= Math.min(total, current + delta); i++) {
                pages.push(i);
            }
            if (pages.length > 0 && pages[0] > 1) pages.unshift(1);
            if (pages.length > 0 && pages[pages.length - 1] < total) pages.push(total);
            return [...new Set(pages)];
        },

        get filteredTemplates() {
            if (this.templateTab === 'all') return this.templates;
            const catMap = { classroom: 'Classroom', office: 'Office', art: 'Art & Music', sports: 'Athletics', tech: 'Technology' };
            return this.templates.filter(t => t.category === catMap[this.templateTab]);
        },

        // --- Merge all modules ---
        ...authModule(),
        ...cartModule(),
        ...browseModule(),
        ...autocompleteModule(),
        ...ordersModule(),
        ...savedListsModule(),
        ...uiModule(),
        ...dashboardModule(),
        ...approvalsModule(),
        ...reportsModule(),

        // --- Demo persona definitions ---
        _demoPersonas: {
            approver: {
                session_id: 'demo',
                user: { name: 'Demo Admin', role: 'admin' },
                session: { approval_level: 2 },
                district: { code: 'DEMO', name: 'Demo District' }
            },
            teacher: {
                session_id: 'demo',
                user: { name: 'Demo Teacher', role: 'teacher' },
                session: { approval_level: 0 },
                district: { code: 'DEMO', name: 'Demo District' }
            }
        },

        // --- Init (orchestrates module inits) ---
        async init() {
            const authed = await this._initAuth();
            if (!authed) return;

            this.loadCart();
            this.loadRecentlyViewed();
            this._initSavedLists();
            this.ready = true;
            this.setupSwipeGestures();
            this.fetchData();
            this.fetchTemplates();
            this._startSessionCheck();
            this.startDashboardRefresh();

            // Demo persona switcher
            this.$el.addEventListener('demo-switch', (e) => {
                const persona = this._demoPersonas[e.detail];
                if (!persona) return;
                localStorage.setItem('eds-session', JSON.stringify(persona));
                window.location.reload();
            });
        },

        // --- Data fetching ---
        async fetchData() {
            await Promise.all([
                this.fetchProducts(),
                this.fetchVendors(),
                this.fetchCategories(),
                this.fetchOrders(),
                this.fetchBids(),
                this.fetchDashboardSummary()
            ]);
        },

        async fetchProducts() {
            this.dashboardLoading = true;
            try {
                const r = await fetch('/api/products?page_size=12');
                if (r.ok) {
                    const d = await r.json();
                    this.products = (d.products || d.items || d || []).map(p => this.normalizeProduct(p));
                    if (d.total) this.totalProductCount = d.total;
                }
            } catch (e) { console.error('Products fetch error:', e); }
            finally { this.dashboardLoading = false; }
        },

        async fetchVendors() {
            try {
                const r = await fetch('/api/vendors?limit=500');
                if (r.ok) {
                    const d = await r.json();
                    this.vendors = d.vendors || d || [];
                }
            } catch (e) { console.error('Vendors fetch error:', e); }
        },

        async fetchCategories() {
            try {
                const r = await fetch('/api/categories');
                if (r.ok) {
                    const d = await r.json();
                    this.categories = d.categories || d || [];
                }
            } catch (e) { console.error('Categories fetch error:', e); }
        },

        // --- Templates ---
        async fetchTemplates() {
            this.templatesLoading = true;
            try {
                const sid = this.sessionId || '';
                const r = await fetch('/api/templates?session_id=' + encodeURIComponent(sid));
                if (r.ok) {
                    this.templates = await r.json();
                }
            } catch (e) { console.error('Templates fetch error:', e); }
            finally { this.templatesLoading = false; }
        },

        async saveCartAsTemplate() {
            const name = this.newTemplateName.trim();
            if (!name || this.cart.length === 0) return;
            try {
                const r = await fetch('/api/templates?session_id=' + encodeURIComponent(this.sessionId || ''), {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({
                        name: name,
                        category: this.newTemplateCategory || 'Custom',
                        description: this.newTemplateDescription.trim(),
                        items: this.cart.map(item => ({
                            item_id: item.ItemId || item.item_id || 0,
                            item_code: edsProduct.getId(item),
                            name: edsProduct.getName(item) || 'Unknown',
                            price: edsProduct.getPrice(item),
                            qty: item.quantity || 1,
                            vendor: edsProduct.getVendor(item),
                            unit: item.UnitOfMeasure || item.unit || 'Each'
                        }))
                    })
                });
                if (r.ok) {
                    const tpl = await r.json();
                    this.templates.push(tpl);
                    this.showSaveTemplateDialog = false;
                    this.newTemplateName = '';
                    this.newTemplateDescription = '';
                    this.newTemplateCategory = 'Custom';
                    this.showToast('Template "' + name + '" saved with ' + this.cart.length + ' items', 'fas fa-bookmark', 'var(--eds-primary)');
                }
            } catch (e) { console.error('Save template error:', e); }
        },

        // --- Navigation ---
        switchView(view) {
            this.activeView = view;
            this.mobileMenuOpen = false;
            if (view === 'browse' && this.browseProducts.length === 0) {
                this.fetchBrowseProducts();
            }
            if (view === 'approvals' && this.isAdmin) {
                this.fetchPendingApprovals();
            }
            if (view === 'reports' && this.canViewReports) {
                this.fetchReportsData();
            }
        }
    };
}
