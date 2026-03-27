# Universal Requisition Screen

User and Developer Guide for the EDS Universal Requisition interface.

---

## Overview

The Universal Requisition Screen is a modern, responsive web interface for browsing and ordering products from the EDS catalog. It connects to the FastAPI backend to fetch real-time product data from the SQL Server database.

**File:** `/universal-requisition.html` (single-page application)

---

## Features

### Product Browsing
- **Product Grid** - Responsive grid/list view of products
- **Lazy Loading** - Products load on-demand with "Load More"
- **Quick View** - Modal with full product details
- **Product Images** - Lazy-loaded from API

### Filtering & Search
- **Category Filter** - Sidebar filter by product category
- **Vendor Filter** - Searchable vendor list filter
- **Price Range Slider** - Visual min/max price filter
- **In-Stock Toggle** - Show only available products
- **Sort Options** - Name (A-Z, Z-A), Price (Low-High, High-Low)
- **Search Within Results** - Client-side text filter
- **Filter Chips** - Visual indicators of active filters with quick remove

### Shopping Cart
- **Add to Cart** - With quantity selector
- **Cart Drawer** - Slide-out cart panel
- **Quantity Adjustment** - +/- buttons in cart
- **Running Total** - Real-time price calculation
- **Checkout** - Proceed to checkout flow

### Cart Management
- **Save Cart as Draft** - Save current cart with custom name
- **Load Saved Cart** - Browse and load previous carts
- **Export to CSV** - Download cart as spreadsheet
- **Budget Indicator** - Visual spending tracker

### Product Comparison
- **Compare Products** - Select up to 3 products
- **Comparison Tray** - Floating bar showing selected items
- **Side-by-Side Table** - Compare specs, price, vendor, status

### User Features
- **Favorites** - Heart icon to save favorite products
- **Recently Viewed** - Track last 5 viewed products
- **Frequently Ordered** - Shows your order history

---

## User Guide

### Searching for Products

1. **Main Search Bar** - Type product name, SKU, or vendor
2. **Category Dropdown** - Select category before searching
3. **Autocomplete** - Results appear as you type

### Filtering Products

1. **Categories** (left sidebar) - Click to filter by category
2. **Vendors** (left sidebar) - Search and click to filter
3. **Price Range** - Drag sliders or enter min/max values
4. **In Stock Only** - Toggle checkbox above product grid
5. **Sort By** - Select from dropdown (Name, Price)

### Active Filter Chips
- Shows all active filters below the toolbar
- Click "X" on any chip to remove that filter
- Click "Clear All" to reset all filters

### Adding Products to Cart

**From Grid View:**
1. Adjust quantity with +/- buttons
2. Click "Add" button

**From Quick View:**
1. Click product card or "Quick View" button
2. Review full details in modal
3. Adjust quantity and click "Add to Requisition"

### Managing Your Cart

1. Click cart icon (top right) to open cart drawer
2. Adjust quantities or remove items
3. View running subtotal
4. Options:
   - **Checkout** - Proceed with order
   - **Save** - Save cart as draft for later
   - **CSV** - Export to spreadsheet
   - **Load Saved Cart** - Retrieve a saved cart

### Comparing Products

1. Click the scale icon on product cards (max 3)
2. Comparison tray appears at bottom
3. Click "Compare Now" to see side-by-side table
4. Add items directly from comparison view

---

## Technical Architecture

### JavaScript Components

| Component | Purpose |
|-----------|---------|
| `API_CONFIG` | API endpoint configuration |
| `api` | API fetch wrapper with retry logic |
| `ProductGrid` | Product listing, pagination, rendering |
| `SearchComponent` | Main search bar with autocomplete |
| `QuickViewModal` | Product detail modal |
| `CartDrawer` | Shopping cart slide-out panel |
| `cart` | Cart state management (localStorage) |
| `VendorFilter` | Vendor sidebar filter |
| `CategoryFilter` | Category sidebar filter |
| `FilterChips` | Active filter display |
| `FilterDrawer` | Mobile filter panel |
| `PriceSlider` | Price range dual slider |
| `SearchWithinResults` | Client-side result filtering |
| `ProductComparison` | Product comparison feature |
| `SavedCarts` | Cart save/load functionality |
| `RecentlyViewed` | Recently viewed tracking |
| `Favorites` | Favorites management |

### Data Flow

```
User Action
    ↓
Component Handler (e.g., CategoryFilter.applyFilter)
    ↓
ProductGrid.currentFilters updated
    ↓
ProductGrid.loadProducts(1) called
    ↓
api.getProducts(params) → FastAPI → SQL Server
    ↓
Response mapped via mapApiProduct()
    ↓
ProductGrid.renderProducts() → DOM updated
    ↓
SearchWithinResults.setProducts() for client filtering
```

### State Management

| State | Storage | Purpose |
|-------|---------|---------|
| Cart items | `localStorage: eds-cart` | Persist cart across sessions |
| Favorites | `localStorage: eds-favorites` | Saved favorite products |
| Recently Viewed | `localStorage: eds-recently-viewed` | Last 5 viewed |
| Saved Carts | `localStorage: eds-saved-carts` | Up to 10 saved carts |

### API Integration

The frontend auto-detects the API URL:
- `file://` protocol → Uses WSL IP (`http://172.23.32.137:8000/api`)
- `localhost` → Uses `http://localhost:8000/api`
- Production → Uses relative `/api` or `window.EDS_API_URL`

**Fallback:** If API unavailable, falls back to static demo data.

---

## Configuration

### API Settings (in HTML)

```javascript
const API_CONFIG = {
    baseUrl: 'http://localhost:8000/api',
    enabled: true,      // Set false to use static data
    timeout: 15000,     // Request timeout (ms)
    retryAttempts: 2,   // Retry on failure
    retryDelay: 1000,   // Delay between retries (ms)
};
```

### Customization

| Setting | Location | Description |
|---------|----------|-------------|
| Budget Limit | `cart.budgetLimit` | Default spending limit |
| Page Size | `ProductGrid.pageSize` | Products per page (default: 20) |
| Max Saved Carts | `SavedCarts.maxCarts` | Max saved carts (default: 10) |
| Max Compare | `ProductComparison.maxItems` | Max comparison items (default: 3) |
| Recently Viewed | `RecentlyViewed.maxItems` | Max recent items (default: 5) |

---

## Styling

### CSS Framework
- **Tailwind CSS** - Utility-first CSS (via CDN)
- **Font Awesome** - Icons (via CDN)
- **Custom CSS** - EDS brand colors and components

### Brand Colors

```css
:root {
    --eds-primary: #1c1a83;    /* Navy blue */
    --eds-secondary: #1a365d;  /* Dark blue */
    --eds-accent: #b70c0d;     /* Red */
}
```

### Responsive Breakpoints
- Mobile: < 768px (single column, filter drawer)
- Tablet: 768px - 1024px (2-3 columns)
- Desktop: > 1024px (4-5 columns, sidebar visible)

---

## Troubleshooting

### Products Not Loading
1. Check API is running: `curl http://localhost:8000/api/status`
2. Check browser console for errors (F12)
3. Verify `API_CONFIG.enabled = true`

### Filters Not Working
1. Clear all filters and try again
2. Check console for JavaScript errors
3. Verify API supports filter parameters

### Cart Not Saving
1. Check localStorage is enabled in browser
2. Clear localStorage and retry: `localStorage.clear()`

### Images Not Loading
1. API images endpoint may be slow
2. Check network tab for failed requests
3. Images lazy-load after products render

---

## See Also

- [API Reference](API_REFERENCE.md) - Backend API documentation
- [Database Architecture](wiki/architecture/database-architecture.md) - Data source
- [Development Setup](DEVELOPMENT.md) - Local development guide
