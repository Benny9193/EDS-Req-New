// Saved lists and template orders — server-backed with localStorage fallback
function savedListsModule() {
    return {
        savedLists: [],

        // --- Create List builder ---
        createListMode: false,
        createListItems: [],
        createListName: '',
        createListSearch: '',
        createListResults: [],
        createListLoading: false,
        createListVendorFilter: '',
        createListCategoryFilter: '',
        _createListAbort: null,
        _createListTimer: null,

        startCreateList() {
            this.createListMode = true;
            this.createListItems = [];
            this.createListName = '';
            this.createListSearch = '';
            this.createListResults = [];
        },

        cancelCreateList() {
            this.createListMode = false;
            this.createListItems = [];
            this.createListName = '';
            this.createListSearch = '';
            this.createListResults = [];
            this.createListVendorFilter = '';
            this.createListCategoryFilter = '';
        },

        createListAutocomplete() {
            clearTimeout(this._createListTimer);
            if (this._createListAbort) { this._createListAbort.abort(); this._createListAbort = null; }
            const q = this.createListSearch.trim();
            if (q.length < 2) { this.createListResults = []; this.createListLoading = false; return; }
            this.createListLoading = true;
            this._createListTimer = setTimeout(() => this._doCreateListSearch(q), 350);
        },

        async _doCreateListSearch(q) {
            try {
                this._createListAbort = new AbortController();
                let url = '/api/products/search/autocomplete?q=' + encodeURIComponent(q) + '&limit=10';
                if (this.createListVendorFilter) url += '&vendor=' + encodeURIComponent(this.createListVendorFilter);
                if (this.createListCategoryFilter) url += '&category=' + encodeURIComponent(this.createListCategoryFilter);
                const r = await fetch(url, { signal: this._createListAbort.signal });
                if (r.ok) {
                    const d = await r.json();
                    if (this.createListSearch.trim() === q) {
                        this.createListResults = (d || []).map(p => this.normalizeProduct(p));
                    }
                }
            } catch (e) { if (e.name !== 'AbortError') console.error('Create list search error:', e); }
            finally { this._createListAbort = null; this.createListLoading = false; }
        },

        createListAddItem(product) {
            const id = edsProduct.getId(product);
            const existing = this.createListItems.find(i => edsProduct.getId(i) === id);
            if (existing) {
                existing.quantity = (existing.quantity || 1) + 1;
                const name = (edsProduct.getName(product) || 'Item').substring(0, 40);
                this.showToast(name + ' already in list — quantity increased to ' + existing.quantity, 'fas fa-layer-group', 'var(--color-warning-500)');
            } else {
                this.createListItems.push({ ...product, quantity: 1 });
            }
        },

        createListRemoveItem(idx) {
            this.createListItems.splice(idx, 1);
        },

        createListUpdateQty(idx, delta) {
            const item = this.createListItems[idx];
            if (!item) return;
            const newQty = (item.quantity || 1) + delta;
            if (newQty <= 0) { this.createListRemoveItem(idx); return; }
            item.quantity = newQty;
        },

        // NOTE: createListTotal getter lives in app.js (getters can't survive spread)

        calcCreateListTotal() {
            return this.createListItems.reduce((sum, item) => {
                return sum + (edsProduct.getPrice(item) * (item.quantity || 1));
            }, 0);
        },

        editSavedList(list) {
            this.createListMode = true;
            this.createListName = list.name;
            this.createListSearch = '';
            this.createListResults = [];
            this.createListItems = (list.items || []).map(item => ({
                ...item,
                // Ensure normalized fields exist for edsProduct helpers
                ItemNumber: item.ItemNumber || edsProduct.getId(item),
                Description: item.Description || edsProduct.getName(item),
                Price: item.Price || edsProduct.getPrice(item),
                VendorName: item.VendorName || edsProduct.getVendor(item),
                quantity: item.quantity || 1
            }));
        },

        async saveCreatedList() {
            const name = this.createListName.trim();
            if (!name) { this.showToast('Please enter a list name', 'fas fa-exclamation-triangle', 'var(--color-warning-500)'); return; }
            if (this.createListItems.length === 0) { this.showToast('Add at least one item to the list', 'fas fa-exclamation-triangle', 'var(--color-warning-500)'); return; }

            const items = this.createListItems.map(p => ({
                ItemNumber: edsProduct.getId(p),
                Description: edsProduct.getName(p),
                Price: edsProduct.getPrice(p),
                VendorName: edsProduct.getVendor(p),
                quantity: p.quantity || 1
            }));
            const list = { name, items, count: items.length, savedAt: new Date().toLocaleDateString() };

            this.savedLists = this.savedLists.filter(l => l.name !== name);
            this.savedLists.unshift(list);

            const sid = this._getSessionId();
            if (sid) {
                try {
                    await fetch('/api/saved-lists/' + encodeURIComponent(sid), {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name, items })
                    });
                } catch {
                    localStorage.setItem('eds_saved_lists', JSON.stringify(this.savedLists));
                }
            } else {
                localStorage.setItem('eds_saved_lists', JSON.stringify(this.savedLists));
            }

            this.showToast('List "' + name + '" saved with ' + items.length + ' items', 'fas fa-bookmark', 'var(--eds-primary)');
            this.cancelCreateList();
        },

        _loadExpandedState() {
            try { return JSON.parse(localStorage.getItem('eds_saved_lists_expanded') || '{}'); } catch { return {}; }
        },

        _saveExpandedState() {
            const state = {};
            this.savedLists.forEach(l => { if (l._expanded) state[l.name] = true; });
            localStorage.setItem('eds_saved_lists_expanded', JSON.stringify(state));
        },

        _applyExpandedState() {
            const state = this._loadExpandedState();
            this.savedLists.forEach(l => { l._expanded = !!state[l.name]; });
        },

        toggleListExpanded(list) {
            list._expanded = !list._expanded;
            this._saveExpandedState();
        },

        async _initSavedLists() {
            // Try loading from server first, fall back to localStorage
            const sid = this._getSessionId();
            if (sid) {
                try {
                    const r = await fetch('/api/saved-lists/' + encodeURIComponent(sid));
                    if (r.ok) {
                        const d = await r.json();
                        if (d.lists && d.lists.length > 0) {
                            this.savedLists = d.lists;
                            this._applyExpandedState();
                            return;
                        }
                    }
                } catch { /* fall through to localStorage */ }
            }
            // Fallback: load from localStorage
            try { this.savedLists = JSON.parse(localStorage.getItem('eds_saved_lists') || '[]'); } catch { this.savedLists = []; }
            this._applyExpandedState();
            // Migrate any localStorage lists to server
            if (this.savedLists.length > 0 && sid) {
                this.savedLists.forEach(list => {
                    fetch('/api/saved-lists/' + encodeURIComponent(sid), {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name: list.name, items: list.items })
                    }).catch(() => {});
                });
            }
        },

        async saveCurrentList() {
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

            // Update local state
            this.savedLists = this.savedLists.filter(l => l.name !== name);
            this.savedLists.unshift(list);

            // Save to server (with localStorage fallback)
            const sid = this._getSessionId();
            if (sid) {
                try {
                    await fetch('/api/saved-lists/' + encodeURIComponent(sid), {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ name, items })
                    });
                } catch {
                    localStorage.setItem('eds_saved_lists', JSON.stringify(this.savedLists));
                }
            } else {
                localStorage.setItem('eds_saved_lists', JSON.stringify(this.savedLists));
            }

            this.newListName = '';
            this.showSaveListDialog = false;
            this.showToast('List "' + name + '" saved with ' + items.length + ' items', 'fas fa-bookmark', 'var(--eds-primary)');
        },

        async deleteSavedList(name) {
            this.savedLists = this.savedLists.filter(l => l.name !== name);
            const sid = this._getSessionId();
            if (sid) {
                try {
                    await fetch('/api/saved-lists/' + encodeURIComponent(sid) + '/' + encodeURIComponent(name), {
                        method: 'DELETE'
                    });
                } catch {
                    localStorage.setItem('eds_saved_lists', JSON.stringify(this.savedLists));
                }
            } else {
                localStorage.setItem('eds_saved_lists', JSON.stringify(this.savedLists));
            }
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
