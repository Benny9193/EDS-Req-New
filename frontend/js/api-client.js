// Centralized API client with error handling, retry, and auth headers
// Usage: const data = await edsApi.get('/api/products?page_size=12');
//        const data = await edsApi.post('/api/cart/123', { cart: [...] });

const edsApi = (() => {
    const MAX_RETRIES = 2;
    const RETRY_DELAY_MS = 1000;

    function _getSessionId() {
        try { return JSON.parse(localStorage.getItem('eds-session')).session_id; } catch { return null; }
    }

    function _buildHeaders(extra) {
        const headers = { 'Content-Type': 'application/json' };
        const sid = _getSessionId();
        if (sid) headers['X-Session-ID'] = sid;
        // In demo mode, send the selected approval level so the backend respects it
        if (sid === 'demo') {
            try {
                const s = JSON.parse(localStorage.getItem('eds-session'));
                const level = (s.session && s.session.approval_level);
                if (level !== undefined && level !== null) {
                    headers['X-Demo-Approval-Level'] = String(level);
                }
            } catch { /* ignore */ }
        }
        return Object.assign(headers, extra || {});
    }

    function _shouldRetry(status) {
        // Retry on network errors and 5xx server errors, not on 4xx client errors
        return status >= 500;
    }

    async function _request(url, options, { retries = 0, silent = false } = {}) {
        try {
            const response = await fetch(url, options);

            if (!response.ok) {
                if (retries < MAX_RETRIES && _shouldRetry(response.status)) {
                    await new Promise(r => setTimeout(r, RETRY_DELAY_MS * (retries + 1)));
                    return _request(url, options, { retries: retries + 1, silent });
                }

                const err = await response.json().catch(() => ({}));
                const message = err.detail || err.message || `Request failed (${response.status})`;

                if (!silent && typeof showToast === 'function') {
                    showToast(message, 'fas fa-exclamation-circle', 'var(--color-accent-500)');
                }

                return { ok: false, status: response.status, error: message, data: null };
            }

            // Check content-type to determine how to parse response
            const contentType = response.headers.get('content-type') || '';
            if (contentType.includes('application/json')) {
                const data = await response.json();
                return { ok: true, status: response.status, error: null, data };
            }

            // For blob responses (CSV/PDF exports)
            return { ok: true, status: response.status, error: null, response };

        } catch (e) {
            if (e.name === 'AbortError') {
                return { ok: false, status: 0, error: 'Request cancelled', data: null };
            }

            if (retries < MAX_RETRIES) {
                await new Promise(r => setTimeout(r, RETRY_DELAY_MS * (retries + 1)));
                return _request(url, options, { retries: retries + 1, silent });
            }

            if (!silent && typeof showToast === 'function') {
                showToast('Network error — check your connection', 'fas fa-wifi', 'var(--color-accent-500)');
            }

            return { ok: false, status: 0, error: e.message, data: null };
        }
    }

    return {
        async get(url, { silent = false, signal } = {}) {
            return _request(url, {
                method: 'GET',
                headers: _buildHeaders(),
                signal,
            }, { silent });
        },

        async post(url, body, { silent = false } = {}) {
            return _request(url, {
                method: 'POST',
                headers: _buildHeaders(),
                body: JSON.stringify(body),
            }, { silent });
        },

        async put(url, body, { silent = false } = {}) {
            return _request(url, {
                method: 'PUT',
                headers: _buildHeaders(),
                body: JSON.stringify(body),
            }, { silent });
        },

        async del(url, { silent = false } = {}) {
            return _request(url, {
                method: 'DELETE',
                headers: _buildHeaders(),
            }, { silent });
        },

        // Download helper for blob responses (CSV, PDF)
        async download(url, defaultFilename) {
            const result = await _request(url, {
                method: 'GET',
                headers: _buildHeaders(),
            });

            if (!result.ok) return result;

            const blob = await result.response.blob();
            const blobUrl = URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.href = blobUrl;

            const cd = result.response.headers.get('Content-Disposition') || '';
            const match = cd.match(/filename="?([^"]+)"?/);
            a.download = match ? match[1] : defaultFilename;
            a.click();
            URL.revokeObjectURL(blobUrl);

            return { ok: true, status: result.status, error: null, data: null };
        },

        getSessionId: _getSessionId,
    };
})();

// Global toast bridge — modules call showToast() directly via Alpine's `this.showToast`.
// For non-Alpine contexts (standalone pages), this no-op prevents errors.
if (typeof showToast === 'undefined') {
    var showToast = function() {};
}
