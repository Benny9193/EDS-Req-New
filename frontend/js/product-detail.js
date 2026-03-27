// Product detail page component
function productDetail() {
    return {
        product: null,
        loading: true,
        quantity: 1,
        justAdded: false,
        toastMessage: '',

        _getSessionId() {
            return getSessionId();
        },

        async init() {
            const session = await validateSession('/v7/login.html');
            if (!session) return;

            const params = new URLSearchParams(window.location.search);
            const productId = params.get('id');
            if (!productId) {
                this.loading = false;
                return;
            }

            try {
                const resp = await fetch(`${API_BASE}/api/products/${encodeURIComponent(productId)}`);
                if (resp.ok) {
                    const p = await resp.json();
                    this.product = {
                        ...edsProduct.normalize(p),
                        CategoryName: p.CategoryName || p.category_name || p.category || '',
                        UnitOfMeasure: p.UnitOfMeasure || p.unit_of_measure || p.UOM || '',
                        CatalogNumber: p.CatalogNumber || p.catalog_number || '',
                    };
                }
            } catch (e) {
                console.error('Error fetching product:', e);
            } finally {
                this.loading = false;
            }
        },

        formatPrice(val) {
            return formatPriceShared(val);
        },

        addToCart() {
            if (!this.product || this.justAdded) return;

            let cart = edsCart.load();

            const key = edsProduct.getId(this.product);
            const existing = cart.find(c => edsProduct.getId(c) === key);
            if (existing) {
                existing.quantity = (existing.quantity || 1) + this.quantity;
            } else {
                cart.push({ ...this.product, quantity: this.quantity });
            }

            edsCart.save(cart);

            this.justAdded = true;
            this.toastMessage = 'Added to cart!';
            setTimeout(() => { this.justAdded = false; this.toastMessage = ''; }, 2000);

            this.trackRecentlyViewed();
        },

        goBack() {
            if (document.referrer && document.referrer.includes('/v7')) {
                history.back();
            } else {
                window.location.href = '/v7/';
            }
        },

        trackRecentlyViewed() {
            if (!this.product) return;
            try {
                let recent = JSON.parse(localStorage.getItem('eds_recently_viewed') || '[]');
                const key = this.product.ItemNumber || this.product.id;
                recent = recent.filter(r => (r.ItemNumber || r.id) !== key);
                recent.unshift(this.product);
                if (recent.length > 10) recent = recent.slice(0, 10);
                localStorage.setItem('eds_recently_viewed', JSON.stringify(recent));
            } catch (e) {}
        }
    };
}
