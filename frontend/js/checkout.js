// Checkout page component
function checkout() {
    return {
        step: 1,
        stepNames: ['Review', 'Shipping', 'Notes', 'Confirm'],
        cart: [],
        session: null,
        isSubmitting: false,
        confirmationId: '',
        locations: [
            { id: 'main-office', name: 'Main Office / District HQ' },
            { id: 'elementary', name: 'Elementary School' },
            { id: 'middle', name: 'Middle School' },
            { id: 'high', name: 'High School' },
            { id: 'warehouse', name: 'Central Warehouse' }
        ],
        shipping: {
            location: '',
            attentionTo: '',
            preference: 'standard',
            notes: ''
        },
        notes: {
            purpose: '',
            accountCode: '',
            internalNotes: ''
        },

        async init() {
            this.session = await validateSession('/v7/login.html');
            if (!this.session) return;
            this.shipping.attentionTo = this.session.first_name
                ? `${this.session.first_name} ${this.session.last_name || ''}`.trim()
                : '';

            this.loadCart();
        },

        async loadCart() {
            this.cart = await edsCart.loadFromServer();
        },

        saveCart() {
            edsCart.save(this.cart);
        },

        get totalItems() {
            return this.cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
        },

        get cartTotal() {
            return edsCart.total(this.cart);
        },

        updateQty(item, delta) {
            item.quantity = Math.max(1, (item.quantity || 1) + delta);
            this.saveCart();
        },

        removeItem(item) {
            const key = edsProduct.getId(item);
            this.cart = this.cart.filter(c => edsProduct.getId(c) !== key);
            this.saveCart();
        },

        getLocationName(id) {
            const loc = this.locations.find(l => l.id === id);
            return loc ? loc.name : id;
        },

        formatPrice(val) {
            return formatPriceShared(val);
        },

        async submitOrder() {
            if (this.isSubmitting) return;
            this.isSubmitting = true;

            try {
                const sessionId = this.session?.session_id;
                if (!sessionId) throw new Error('No session');

                const payload = {
                    items: this.cart.map(item => ({
                        item_number: edsProduct.getId(item),
                        quantity: item.quantity || 1,
                        price: edsProduct.getPrice(item),
                        description: edsProduct.getName(item)
                    })),
                    shipping_location: this.shipping.location,
                    attention_to: this.shipping.attentionTo,
                    shipping_preference: this.shipping.preference,
                    shipping_notes: this.shipping.notes,
                    purpose: this.notes.purpose,
                    account_code: this.notes.accountCode,
                    internal_notes: this.notes.internalNotes
                };

                const response = await fetch(`${API_BASE}/api/requisitions`, {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'X-Session-ID': sessionId
                    },
                    body: JSON.stringify(payload)
                });

                if (!response.ok) {
                    let errMsg = 'Submission failed';
                    try { const err = await response.json(); errMsg = err.detail || errMsg; } catch {}
                    throw new Error(errMsg);
                }

                const data = await response.json();
                this.confirmationId = data.requisition_number || data.id || '';

                localStorage.removeItem('eds_cart');
                this.cart = [];

                this.step = 5;
            } catch (error) {
                alert('Error: ' + error.message);
            } finally {
                this.isSubmitting = false;
            }
        }
    };
}
