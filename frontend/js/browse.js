// Browse products - filtering, pagination, view modes
function browseModule() {
    return {
        browseViewMode: 'grid',
        browseProducts: [],
        browseTotal: 0,
        browsePage: 1,
        browsePageSize: 24,
        browseTotalPages: 0,
        browseLoading: false,
        browseLoadingMore: false,
        browseQuery: '',
        browseCategory: '',
        browseVendor: '',
        browseBidId: '',
        browseMinPrice: '',
        browseMaxPrice: '',
        browseSortBy: 'name',
        availableBids: [],
        bidsLoading: false,

        // NOTE: browseActiveFilters and browsePageNumbers getters live in app.js (getters can't survive spread)

        _buildBrowseParams(page) {
            const params = new URLSearchParams();
            params.set('page', page);
            params.set('page_size', this.browsePageSize);
            if (this.browseQuery.trim()) params.set('query', this.browseQuery.trim());
            if (this.browseCategory) params.set('category', this.browseCategory);
            if (this.browseVendor) params.set('vendor', this.browseVendor);
            if (this.browseBidId) params.set('bid_ids', this.browseBidId);
            if (this.browseMinPrice !== '') params.set('min_price', this.browseMinPrice);
            if (this.browseMaxPrice !== '') params.set('max_price', this.browseMaxPrice);
            if (this.browseSortBy) {
                if (this.browseSortBy.includes('_')) {
                    const [field, order] = this.browseSortBy.split('_');
                    params.set('sort_by', field);
                    params.set('sort_order', order);
                } else {
                    params.set('sort_by', this.browseSortBy);
                    params.set('sort_order', 'asc');
                }
            }
            return params;
        },

        _browseEndpoint() {
            // Use ES search endpoint when bid filter is active
            return this.browseBidId ? '/api/search' : '/api/products';
        },

        async fetchBids() {
            if (this.availableBids.length > 0) return;
            this.bidsLoading = true;
            try {
                const result = await edsApi.get('/api/bids?active_only=true', { silent: true });
                if (result.ok) {
                    this.availableBids = (result.data.bids || []).filter(b => b.product_count > 0);
                }
            } catch (e) { console.error('Bids fetch error:', e); }
            finally { this.bidsLoading = false; }
        },

        async fetchBrowseProducts(resetPage = true) {
            if (resetPage) this.browsePage = 1;
            this.browseLoading = true;
            try {
                const params = this._buildBrowseParams(this.browsePage);
                const result = await edsApi.get(this._browseEndpoint() + '?' + params.toString(), { silent: true });
                if (result.ok) {
                    const d = result.data;
                    this.browseProducts = (d.products || []).map(p => this.normalizeProduct(p));
                    this.browseTotal = d.total || 0;
                    this.browsePage = d.page || 1;
                    this.browseTotalPages = d.total_pages || 1;
                }
            } catch (e) {
                console.error('Browse fetch error:', e);
            } finally {
                this.browseLoading = false;
            }
        },

        async browseLoadMore() {
            if (this.browseLoadingMore || this.browsePage >= this.browseTotalPages) return;
            this.browseLoadingMore = true;
            try {
                const nextPage = this.browsePage + 1;
                const params = this._buildBrowseParams(nextPage);
                const result = await edsApi.get(this._browseEndpoint() + '?' + params.toString(), { silent: true });
                if (result.ok) {
                    const d = result.data;
                    const newProducts = (d.products || []).map(p => this.normalizeProduct(p));
                    this.browseProducts = [...this.browseProducts, ...newProducts];
                    this.browsePage = d.page || nextPage;
                    this.browseTotalPages = d.total_pages || 1;
                    this.browseTotal = d.total || 0;
                }
            } catch (e) { console.error('Load more error:', e); }
            finally { this.browseLoadingMore = false; }
        },

        browseGoToPage(page) {
            if (page < 1 || page > this.browseTotalPages) return;
            this.browsePage = page;
            this.fetchBrowseProducts(false);
            window.scrollTo({ top: 0, behavior: 'smooth' });
        },

        browseApplyFilters() {
            this.fetchBrowseProducts(true);
        },

        browseClearFilters() {
            this.browseQuery = '';
            this.browseCategory = '';
            this.browseVendor = '';
            this.browseBidId = '';
            this.browseMinPrice = '';
            this.browseMaxPrice = '';
            this.browseSortBy = 'name';
            this.fetchBrowseProducts(true);
        },

        browseRemoveFilter(key) {
            if (key === 'category') this.browseCategory = '';
            else if (key === 'vendor') this.browseVendor = '';
            else if (key === 'query') this.browseQuery = '';
            else if (key === 'bid') this.browseBidId = '';
            else if (key === 'price') { this.browseMinPrice = ''; this.browseMaxPrice = ''; }
            this.fetchBrowseProducts(true);
        }
    };
}
