// Shared auth validation for standalone pages (checkout, product-detail)
// Returns the parsed session object if valid, or null (and redirects to login).
async function validateSession(redirectUrl) {
    redirectUrl = redirectUrl || '/v7/login.html';
    const raw = localStorage.getItem('eds-session');
    if (!raw) { window.location.href = redirectUrl; return null; }
    try {
        const session = JSON.parse(raw);
        if (!session.session_id) { window.location.href = redirectUrl; return null; }
        if (session.session_id !== 'demo') {
            const r = await fetch(`${API_BASE}/api/auth/session/${encodeURIComponent(session.session_id)}`);
            const d = await r.json();
            if (!r.ok || !d.valid) {
                localStorage.removeItem('eds-session');
                window.location.href = redirectUrl;
                return null;
            }
        }
        return session;
    } catch {
        window.location.href = redirectUrl;
        return null;
    }
}

// Helper to get session ID from localStorage
function getSessionId() {
    try { return JSON.parse(localStorage.getItem('eds-session')).session_id; } catch { return null; }
}
