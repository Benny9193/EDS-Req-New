# API Field Naming Inconsistencies

This document maps the field naming differences between backend API responses and frontend usage.
Use `edsProduct.normalize()` (from `js/product-helpers.js`) to standardize all product objects.

## Product Fields

| Canonical (frontend) | Products API | Search/ES API | Cart API | Notes |
|---------------------|-------------|---------------|----------|-------|
| `ItemNumber` | `id` (aliased from ItemId) | `id` (itemId/pricingConsolidatedId) | Whatever was POSTed | Primary identifier |
| `Description` | `name` (aliased from Description) | `name` (shortDescription[0]) | Whatever was POSTed | Display name |
| `Price` | `unit_price` (aliased from ListPrice) | `unit_price` (bidPrice/catalogPrice) | `Price`, `price`, or `UnitPrice` | **CRITICAL: 3+ field names** |
| `VendorName` | `vendor` (aliased from Vendors.Name) | `vendor` (vendorName) | `vendor` or `VendorName` | |
| `category` | `category` (aliased from Category.Name) | `category` (categoryId) | `category` | |
| `unit_of_measure` | `unit_of_measure` (Units.Code) | `unit_of_measure` (unitCode) | N/A | |

## Cart API (`/api/cart/{session_id}`)

**Root cause**: `CartPayload.cart` is `List[dict]` — no validation or normalization.
The backend stores whatever field names the frontend sends, then returns them as-is.

**CartItem model has duplicate fields**:
- `ItemNumber` (PascalCase) AND `item_number` (snake_case)
- `Price` (PascalCase) AND `price` (snake_case) AND `UnitPrice` (PascalCase)
- `VendorName` (PascalCase) AND `vendor` (snake_case)

**Fix**: The frontend now normalizes via `edsProduct.normalize()` before storing in state.
Backend fix (future): Normalize cart items on PUT to a consistent schema.

## Requisition Fields

| Frontend | List API | Detail API | Notes |
|----------|---------|------------|-------|
| `requisition_id` | `requisition_id` (mapped from RequisitionId) | `requisition_id` (raw dict) | Consistent |
| `requisition_number` | `requisition_number` (mapped) | `requisition_number` | Consistent |
| `status` | `status` (mapped from StatusName) | `status` | Consistent |
| `total_amount` | `total_amount` (mapped) | `total_amount` | Consistent |
| `created_at` | `created_at` (mapped from DateEntered) | `created_at` | Consistent |

## Recommendations

1. **Short-term (done)**: Frontend uses `edsProduct.normalize()` / `edsProduct.getPrice()` etc.
2. **Medium-term**: Backend cart route should normalize items on PUT (single schema)
3. **Long-term**: Products API, Search API, and Cart API should all return identical field names
