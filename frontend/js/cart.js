// Cart operations
function cartModule() {
    return {
        cart: [],
        cartCount: 0,
        cartOpen: false,
        showSaveListDialog: false,
        newListName: '',

        // NOTE: cartTotal getter lives in app.js (getters can't survive spread)

        async loadCart() {
            this.cart = await edsCart.loadFromServer();
            this.cartCount = edsCart.itemCount(this.cart);
        },

        saveCart() {
            this.cartCount = edsCart.itemCount(this.cart);
            edsCart.save(this.cart, {
                onSyncError: () => {
                    this.showToast('Cart sync failed — changes saved locally', 'fas fa-exclamation-triangle', 'var(--color-warning-500)');
                }
            });
        },

        addToCart(product, silent = false) {
            const id = edsProduct.getId(product);
            const existing = this.cart.find(i => edsProduct.getId(i) === id);
            if (existing) { existing.quantity = (existing.quantity || 1) + 1; }
            else { this.cart.push({ ...product, quantity: 1 }); }
            this.saveCart();
            this.trackRecentlyViewed(product);
            if (!silent) {
                const name = (edsProduct.getName(product) || 'Item').substring(0, 40);
                this.showToast(name + ' added to cart', 'fas fa-cart-plus');
                // Warn if cart now exceeds remaining budget
                const remaining = this.budgetRemaining();
                if (remaining !== null && edsCart.total(this.cart) > remaining) {
                    setTimeout(() => {
                        this.showToast('Cart total exceeds your remaining budget', 'fas fa-exclamation-triangle', 'var(--color-accent-500)');
                    }, 400);
                }
            }
        },

        updateCartQty(idx, delta) {
            const item = this.cart[idx];
            if (!item) return;
            const newQty = (item.quantity || 1) + delta;
            if (newQty <= 0) { this.removeFromCart(idx); return; }
            item.quantity = newQty;
            this.saveCart();
        },

        removeFromCart(idx) {
            this.cart.splice(idx, 1);
            this.saveCart();
        },

        showSaveListFromCart() {
            this.showSaveListDialog = true;
            this.newListName = '';
        },

        // --- Budget-aware cart helpers ---

        budgetRemaining() {
            if (!this.dashboardBudget?.remaining) return null;
            return this.dashboardBudget.remaining;
        },

        cartOverBudget() {
            const remaining = this.budgetRemaining();
            if (remaining === null) return false;
            return this.cartTotal > remaining;
        },

        cartBudgetPercent() {
            const remaining = this.budgetRemaining();
            if (remaining === null || remaining <= 0) return 0;
            return Math.round((this.cartTotal / remaining) * 100);
        },

        cartBudgetWarningLevel() {
            if (!this.dashboardBudget) return 'none';
            const remaining = this.budgetRemaining();
            if (remaining === null) return 'none';
            if (this.cartTotal > remaining) return 'over';
            if (this.cartTotal > remaining * 0.9) return 'critical';
            if (this.cartTotal > remaining * 0.75) return 'warning';
            return 'none';
        }
    };
}
