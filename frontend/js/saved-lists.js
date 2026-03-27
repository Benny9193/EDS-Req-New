// Saved lists and template orders
function savedListsModule() {
    return {
        savedLists: [],

        _initSavedLists() {
            try { this.savedLists = JSON.parse(localStorage.getItem('eds_saved_lists') || '[]'); } catch { this.savedLists = []; }
        },

        saveCurrentList() {
            const name = this.newListName.trim();
            if (!name || this.cart.length === 0) return;
            const items = this.cart.map(p => ({
                ItemNumber: edsProduct.getId(p),
                Description: edsProduct.getName(p),
                Price: edsProduct.getPrice(p),
                VendorName: edsProduct.getVendor(p),
                quantity: p.quantity || 1
            }));
            const list = { name, items, count: items.length, savedAt: new Date().toLocaleDateString() };
            this.savedLists = this.savedLists.filter(l => l.name !== name);
            this.savedLists.unshift(list);
            localStorage.setItem('eds_saved_lists', JSON.stringify(this.savedLists));
            this.newListName = '';
            this.showSaveListDialog = false;
            this.showToast('List "' + name + '" saved with ' + items.length + ' items', 'fas fa-bookmark', 'var(--eds-primary)');
        },

        deleteSavedList(name) {
            this.savedLists = this.savedLists.filter(l => l.name !== name);
            localStorage.setItem('eds_saved_lists', JSON.stringify(this.savedLists));
        },

        addListToCart(list) {
            list.items.forEach(item => this.addToCart(item, true));
            this.showToast('Added ' + list.items.length + ' items from "' + list.name + '" to cart', 'fas fa-cart-plus');
        },

        addTemplateToCart(tpl) {
            let added = 0, merged = 0;
            tpl.items.forEach(item => {
                const itemCode = item.item_code || item.ItemNumber || '';
                const existing = itemCode ? this.cart.find(c =>
                    (c.ItemNumber || c.item_number || c.ItemCode || '') === itemCode
                ) : null;
                if (existing) {
                    existing.quantity = (existing.quantity || 1) + (item.qty || 1);
                    merged++;
                } else {
                    this.cart.push({
                        ItemId: item.item_id,
                        ItemNumber: item.item_code,
                        ItemCode: item.item_code,
                        Description: item.name,
                        name: item.name,
                        Price: item.price,
                        UnitPrice: item.price,
                        quantity: item.qty || 1,
                        VendorName: item.vendor,
                        vendor: item.vendor,
                        UnitOfMeasure: item.unit || 'Each'
                    });
                    added++;
                }
            });
            this.saveCart();
            let msg = 'Added ' + added + ' items from "' + tpl.name + '"';
            if (merged > 0) msg += ' (' + merged + ' merged with existing)';
            this.showToast(msg, 'fas fa-cart-plus');
        }
    };
}
