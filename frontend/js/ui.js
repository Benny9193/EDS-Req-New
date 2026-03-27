// UI utilities: toast, swipe gestures, recently viewed, formatting, product helpers
function uiModule() {
    return {
        // --- Toast ---
        toasts: [],
        toastIdCounter: 0,

        showToast(msg, icon, color) {
            const id = ++this.toastIdCounter;
            this.toasts.push({ id, message: msg, icon: icon || 'fas fa-check-circle', color: color || 'var(--color-success-500)', visible: true });
            setTimeout(() => this.dismissToast(id), 3000);
            if (this.toasts.length > 5) this.toasts.shift();
        },

        dismissToast(id) {
            const t = this.toasts.find(t => t.id === id);
            if (t) t.visible = false;
            setTimeout(() => { this.toasts = this.toasts.filter(t => t.id !== id); }, 300);
        },

        // --- Swipe gestures ---
        setupSwipeGestures() {
            let touchStartX = 0;
            let touchStartY = 0;
            let touchEndX = 0;
            const SWIPE_THRESHOLD = 60;
            const EDGE_ZONE = 30;

            document.addEventListener('touchstart', (e) => {
                touchStartX = e.changedTouches[0].screenX;
                touchStartY = e.changedTouches[0].screenY;
            }, { passive: true });

            document.addEventListener('touchend', (e) => {
                touchEndX = e.changedTouches[0].screenX;
                const diffX = touchEndX - touchStartX;
                const diffY = Math.abs(e.changedTouches[0].screenY - touchStartY);
                if (diffY > Math.abs(diffX)) return;
                if (diffX > SWIPE_THRESHOLD && touchStartX < EDGE_ZONE && !this.mobileMenuOpen) {
                    this.mobileMenuOpen = true;
                }
                if (diffX < -SWIPE_THRESHOLD && this.mobileMenuOpen) {
                    this.mobileMenuOpen = false;
                }
            }, { passive: true });
        },

        // --- Recently viewed ---
        recentlyViewed: [],

        trackRecentlyViewed(product) {
            const id = edsProduct.getId(product);
            this.recentlyViewed = this.recentlyViewed.filter(p => edsProduct.getId(p) !== id);
            this.recentlyViewed.unshift(product);
            if (this.recentlyViewed.length > 10) this.recentlyViewed = this.recentlyViewed.slice(0, 10);
            try { localStorage.setItem('eds_recently_viewed', JSON.stringify(this.recentlyViewed)); } catch {}
        },

        loadRecentlyViewed() {
            try { this.recentlyViewed = JSON.parse(localStorage.getItem('eds_recently_viewed') || '[]'); } catch { this.recentlyViewed = []; }
        },

        // --- Formatting ---
        formatPrice(p) {
            return formatPriceShared(p);
        },

        vendorInitials(name) {
            if (!name) return '?';
            return name.split(/\s+/).map(w => w[0]).join('').substring(0, 2).toUpperCase();
        },

        // --- Product helpers ---
        normalizeProduct(p) {
            return edsProduct.normalize(p);
        },

        getCategoryIcon(product) {
            const cat = (product.category || product.Category || '').toLowerCase();
            const desc = (product.Description || product.description || '').toLowerCase();
            if (cat.includes('athletic') || cat.includes('sport') || desc.includes('ball') || desc.includes('athletic')) return 'fa-running';
            if (cat.includes('custodial') || cat.includes('cleaning') || desc.includes('clean')) return 'fa-broom';
            if (cat.includes('cafeteria') || cat.includes('food') || desc.includes('food')) return 'fa-utensils';
            if (cat.includes('technology') || cat.includes('computer') || cat.includes('audio visual') || desc.includes('laptop') || desc.includes('computer')) return 'fa-laptop';
            if (cat.includes('furniture') || cat.includes('classroom') || desc.includes('chair') || desc.includes('desk')) return 'fa-chair';
            if (cat.includes('science') || desc.includes('microscope') || desc.includes('lab')) return 'fa-flask';
            if (cat.includes('art') || desc.includes('paint') || desc.includes('canvas')) return 'fa-palette';
            if (cat.includes('paper') || cat.includes('office') || desc.includes('paper') || desc.includes('pen') || desc.includes('pencil')) return 'fa-pen';
            if (cat.includes('auto') || desc.includes('auto') || desc.includes('vehicle')) return 'fa-car';
            if (cat.includes('carpentry') || desc.includes('drill') || desc.includes('saw')) return 'fa-hammer';
            if (cat.includes('medical') || cat.includes('health') || desc.includes('first aid')) return 'fa-medkit';
            if (cat.includes('music') || desc.includes('instrument') || desc.includes('guitar')) return 'fa-music';
            if (cat.includes('book') || cat.includes('library') || desc.includes('book') || desc.includes('textbook')) return 'fa-book';
            if (cat.includes('apparel') || desc.includes('shirt') || desc.includes('uniform')) return 'fa-tshirt';
            if (cat.includes('cosmetology') || desc.includes('beauty') || desc.includes('hair')) return 'fa-cut';
            if (cat.includes('copier') || desc.includes('printer') || desc.includes('toner')) return 'fa-print';
            return 'fa-box';
        },

        getCategoryColor(product) {
            const cat = (product.category || product.Category || '').toLowerCase();
            if (cat.includes('athletic') || cat.includes('sport')) return '#e74c3c';
            if (cat.includes('custodial') || cat.includes('cleaning')) return '#27ae60';
            if (cat.includes('cafeteria') || cat.includes('food')) return '#f39c12';
            if (cat.includes('technology') || cat.includes('computer') || cat.includes('audio visual')) return '#3498db';
            if (cat.includes('furniture') || cat.includes('classroom')) return '#8e44ad';
            if (cat.includes('science')) return '#1abc9c';
            if (cat.includes('art')) return '#e91e63';
            if (cat.includes('paper') || cat.includes('office')) return '#607d8b';
            if (cat.includes('carpentry')) return '#795548';
            if (cat.includes('medical') || cat.includes('health')) return '#f44336';
            if (cat.includes('music')) return '#9c27b0';
            if (cat.includes('apparel')) return '#ff5722';
            return '#9e9e9e';
        },

        getProductUrl(product) {
            const id = product.id || product.Id || edsProduct.getId(product);
            return '/v7/product-detail.html?id=' + encodeURIComponent(id);
        },

        openProductModal(product) {
            this.selectedProduct = product;
            this.showProductModal = true;
            this.trackRecentlyViewed(product);
        },

        viewProduct(product) {
            this.openProductModal(product);
        }
    };
}
