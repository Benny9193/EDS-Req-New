// Shared product normalization and cart persistence utilities
// Eliminates field-name chaos (Price vs price vs UnitPrice vs unit_price)

const edsProduct = {
    /**
     * Normalize a product object from any API response format into a consistent shape.
     * Call this on every product coming from the API before storing in state.
     */
    normalize(p) {
        return {
            ...p,
            ItemNumber: p.ItemNumber || p.item_number || p.vendor_item_code || p.id || '',
            Description: p.Description || p.description || p.name || '',
            Price: parseFloat(p.Price || p.price || p.unit_price || p.UnitPrice || 0),
            VendorName: (() => {
                const v = p.VendorName || p.vendor_name || p.vendor || '';
                return v === 'Unknown Vendor' ? '' : v;
            })(),
            category: p.category || p.Category || '',
            unit_of_measure: p.unit_of_measure || p.UnitOfMeasure || '',
        };
    },

    /**
     * Get price from a product/cart item regardless of field naming.
     */
    getPrice(item) {
        return parseFloat(item.Price || item.price || item.unit_price || item.UnitPrice || 0);
    },

    /**
     * Get item identifier regardless of field naming.
     */
    getId(item) {
        return item.ItemNumber || item.item_number || item.vendor_item_code || item.id || '';
    },

    /**
     * Get display name regardless of field naming.
     */
    getName(item) {
        return item.Description || item.description || item.name || '';
    },

    /**
     * Get vendor name regardless of field naming.
     */
    getVendor(item) {
        return item.VendorName || item.vendor_name || item.vendor || '';
    },
};


const edsCart = {
    STORAGE_KEY: 'eds_cart',

    /**
     * Load cart from localStorage.
     */
    load() {
        try { return JSON.parse(localStorage.getItem(this.STORAGE_KEY) || '[]'); }
        catch { return []; }
    },

    /**
     * Save cart to localStorage and sync to server.
     * Returns a promise that resolves when server sync completes (or fails).
     */
    save(cart, { onSyncError } = {}) {
        localStorage.setItem(this.STORAGE_KEY, JSON.stringify(cart));

        const sid = edsApi ? edsApi.getSessionId() : null;
        if (!sid) return Promise.resolve();

        return fetch('/api/cart/' + encodeURIComponent(sid), {
            method: 'PUT',
            headers: { 'Content-Type': 'application/json', 'X-Session-ID': sid },
            body: JSON.stringify({ session_id: sid, cart })
        }).catch((err) => {
            console.warn('Cart server sync failed:', err.message);
            if (typeof onSyncError === 'function') {
                onSyncError(err);
            }
        });
    },

    /**
     * Load cart from server, falling back to localStorage.
     */
    async loadFromServer() {
        const localCart = this.load();
        const sid = edsApi ? edsApi.getSessionId() : null;
        if (!sid) return localCart;

        try {
            const r = await fetch('/api/cart/' + encodeURIComponent(sid));
            if (r.ok) {
                const d = await r.json();
                if (d.cart && d.cart.length) {
                    localStorage.setItem(this.STORAGE_KEY, JSON.stringify(d.cart));
                    return d.cart;
                }
            }
        } catch {
            // Fall back to localStorage
        }
        return localCart;
    },

    /**
     * Count total items in cart.
     */
    itemCount(cart) {
        return cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
    },

    /**
     * Calculate cart total price.
     */
    total(cart) {
        return cart.reduce((sum, item) => {
            return sum + (edsProduct.getPrice(item) * (item.quantity || 1));
        }, 0);
    },

    /**
     * Clear cart from localStorage.
     */
    clear() {
        localStorage.removeItem(this.STORAGE_KEY);
    }
};
