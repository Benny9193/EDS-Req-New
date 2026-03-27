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
        }
    };
}
