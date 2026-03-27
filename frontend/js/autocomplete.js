// Autocomplete for global search and browse search
function autocompleteModule() {
    return {
        globalSearch: '',
        globalAutocompleteSuggestions: [],
        showGlobalAutocomplete: false,
        globalAutocompleteTimer: null,
        browseAutocompleteSuggestions: [],
        showBrowseAutocomplete: false,
        browseAutocompleteTimer: null,
        globalAutocompleteLoading: false,
        browseAutocompleteLoading: false,

        _browseAbort: null,

        browseAutocomplete() {
            clearTimeout(this.browseAutocompleteTimer);
            if (this._browseAbort) { this._browseAbort.abort(); this._browseAbort = null; }
            const q = this.browseQuery.trim();
            if (q.length < 2) { this.browseAutocompleteSuggestions = []; this.showBrowseAutocomplete = false; this.browseAutocompleteLoading = false; return; }
            this.browseAutocompleteLoading = true;
            this.showBrowseAutocomplete = true;
            this.browseAutocompleteTimer = setTimeout(() => {
                this._doBrowseAutocomplete(q);
            }, 350);
        },

        async _doBrowseAutocomplete(q) {
            try {
                this._browseAbort = new AbortController();
                const r = await fetch('/api/products/search/autocomplete?q=' + encodeURIComponent(q) + '&limit=8', { signal: this._browseAbort.signal });
                if (r.ok) {
                    const d = await r.json();
                    if (this.browseQuery.trim() === q) {
                        this.browseAutocompleteSuggestions = (d || []).map(p => this.normalizeProduct(p));
                        this.showBrowseAutocomplete = this.browseAutocompleteSuggestions.length > 0;
                    }
                }
            } catch (e) { if (e.name !== 'AbortError') console.error('Autocomplete error:', e); }
            finally { this._browseAbort = null; this.browseAutocompleteLoading = false; }
        },

        selectBrowseAutocomplete(s) {
            this.browseQuery = s.Description || s.name || '';
            this.showBrowseAutocomplete = false;
            this.browseAutocompleteSuggestions = [];
            this.fetchBrowseProducts(true);
        },

        browseSearchSubmit() {
            this.showBrowseAutocomplete = false;
            this.fetchBrowseProducts(true);
        },

        _globalAbort: null,

        globalAutocomplete() {
            clearTimeout(this.globalAutocompleteTimer);
            if (this._globalAbort) { this._globalAbort.abort(); this._globalAbort = null; }
            const q = this.globalSearch.trim();
            if (q.length < 2) { this.globalAutocompleteSuggestions = []; this.showGlobalAutocomplete = false; this.globalAutocompleteLoading = false; return; }
            this.globalAutocompleteLoading = true;
            this.showGlobalAutocomplete = true;
            this.globalAutocompleteTimer = setTimeout(() => {
                this._doGlobalAutocomplete(q);
            }, 350);
        },

        async _doGlobalAutocomplete(q) {
            try {
                this._globalAbort = new AbortController();
                const r = await fetch('/api/products/search/autocomplete?q=' + encodeURIComponent(q) + '&limit=6', { signal: this._globalAbort.signal });
                if (r.ok) {
                    const d = await r.json();
                    if (this.globalSearch.trim() === q) {
                        this.globalAutocompleteSuggestions = (d || []).map(p => this.normalizeProduct(p));
                        this.showGlobalAutocomplete = this.globalAutocompleteSuggestions.length > 0;
                    }
                } else {
                    this.showGlobalAutocomplete = false;
                }
            } catch (e) { if (e.name !== 'AbortError') console.error('Autocomplete error:', e); }
            finally { this._globalAbort = null; this.globalAutocompleteLoading = false; }
        },

        selectGlobalAutocomplete(s) {
            this.browseQuery = s.Description || s.name || '';
            this.showGlobalAutocomplete = false;
            this.globalAutocompleteSuggestions = [];
            this.globalSearch = '';
            this.switchView('browse');
            this.fetchBrowseProducts(true);
        },

        globalSearchSubmit() {
            if (this.globalSearch.trim()) {
                this.browseQuery = this.globalSearch.trim();
                this.showGlobalAutocomplete = false;
                this.globalAutocompleteSuggestions = [];
                this.globalSearch = '';
                this.switchView('browse');
                this.fetchBrowseProducts(true);
            }
        }
    };
}
