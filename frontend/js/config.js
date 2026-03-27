// API base URL - uses current origin in dev, empty string in production
const API_BASE = (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1')
    ? window.location.origin : '';

// Shared price formatter used across all pages
function formatPriceShared(val) {
    const n = parseFloat(val);
    return isNaN(n) ? '$0.00' : '$' + n.toFixed(2);
}
