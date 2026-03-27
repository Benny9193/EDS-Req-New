# EDS API Routes Reference

## Table of Contents

1. [Overview](#overview)
2. [Global Conventions](#global-conventions)
   - [Base URL and Prefix](#base-url-and-prefix)
   - [Authentication Model](#authentication-model)
   - [Rate Limiting](#rate-limiting)
   - [Caching Architecture](#caching-architecture)
   - [Error Response Format](#error-response-format)
   - [Core Data Models](#core-data-models)
3. [Health & System](#health--system-endpoints)
4. [Authentication (`/api/auth`)](#authentication-apíauth)
5. [Products (`/api/products`)](#products-apiproducts)
6. [Categories (`/api/categories`)](#categories-apicategories)
7. [Vendors (`/api/vendors`)](#vendors-apivendors)
8. [Bids (`/api/bids`)](#bids-apibids)
9. [Search (`/api/search`)](#elasticsearch-search-apisearch)
10. [Cart (`/api/cart`)](#cart-apicart)
11. [Templates (`/api/templates`)](#templates-apitemplates)
12. [Requisitions (`/api/requisitions`)](#requisitions-apirequisitions)
13. [Dashboard (`/api/dashboard`)](#dashboard-apidashboard)
14. [Reports (`/api/reports`)](#reports-apireports)
15. [AI Search (`/api/products/ai-search`)](#ai-search-apiproductsai-search)
16. [AI Chat (`/api/chat`)](#ai-chat-apichat)
17. [Admin (`/api/admin`)](#admin-apiadmin)
18. [Appendix: Status Codes](#appendix-status-codes)
19. [Appendix: Environment Variables](#appendix-environment-variables)

---

## Overview

The EDS API is a FastAPI application serving the Universal Requisition front-end. It exposes endpoints for browsing the school supplies catalog, managing shopping carts, submitting and approving requisitions, and accessing analytics reports. All API routes are mounted under the `/api` prefix. Interactive API documentation is available at `/docs` (Swagger UI) and `/redoc`.

The backend connects to two SQL Server databases:
- **EDS** — production catalog (Items, Vendors, Categories, CrossRefs, Requisitions, Sessions)
- **dpa_EDSAdmin** — monitoring and performance data (used by scripts, not the API)

An Elasticsearch cluster at `20.122.81.233:9200` provides optional full-text search over the `pricing_consolidated_53` index. When ES is healthy, search endpoints use it automatically; they fall back to SQL on failure.

---

## Global Conventions

### Base URL and Prefix

All API endpoints use the prefix `/api`. The application root (`/`) and all non-`/api` paths serve frontend HTML files.

| Environment | Example Base URL |
|---|---|
| Local development | `http://localhost:8000/api` |
| Docker | `http://localhost:8000/api` |
| Production (Kubernetes) | `https://<cluster-dns>/api` |

### Authentication Model

The API does not use HTTP Bearer tokens or API keys. Authentication is session-based:

1. The client POSTs credentials to `POST /api/auth/login`.
2. On success, the response includes a numeric `session_id`.
3. Protected endpoints accept `session_id` as a query parameter.
4. The `get_current_user` FastAPI dependency (defined in `api/middleware.py`) validates the session on each request, checking both the 8-hour absolute timeout and the 2-hour inactivity timeout.

**Demo mode:** Several endpoints accept the literal string `"demo"` as a `session_id`. In demo mode, user-scoped filters are removed so all data is visible. Write operations (update, cancel, approve) reject the demo session with HTTP 403.

**Session timeouts** (from `api/middleware.py`):
- Maximum session age: **8 hours** (`SESSION_TIMEOUT_HOURS`)
- Inactivity timeout: **2 hours** (`SESSION_INACTIVITY_HOURS`)

**Admin sessions** require `ApprovalLevel >= 1` in the `SessionTable`. Routes in `/api/admin` and certain requisition approval operations enforce this.

### Rate Limiting

The `RateLimitMiddleware` uses a per-IP sliding window. The default limit is 120 requests/minute, configurable via the `EDS_RATE_LIMIT` environment variable.

- Health check paths (`/api/health`, `/api/status`) are exempt.
- Static file paths (`/js/`, `/css/`, `/images/`, `/assets/`) are exempt.
- When a limit is exceeded, the response is `HTTP 429` with a `Retry-After: 60` header.

### Caching Architecture

An in-memory `SimpleCache` (defined in `api/cache.py`) stores frequently-read, rarely-changing data. It is a single-process in-memory store — not shared across Kubernetes pods. Cache entries expire based on TTL.

| Constant | TTL | Typical Use |
|---|---|---|
| `CACHE_TTL_SHORT` | 5 minutes | Autocomplete results, product total count |
| `CACHE_TTL_MEDIUM` | 30 minutes | Vendor lists, reports data |
| `CACHE_TTL_LONG` | 1 hour | Category list, template item lookups |
| `CACHE_TTL_VERY_LONG` | 2 hours | (reserved) |

Reports cache keys are prefixed `reports:<district_id>:<date_start>:<date_end>:<section>`. The `invalidate_reports_cache()` function in `api/routes/reports.py` clears these keys whenever a requisition is submitted, approved, rejected, or cancelled.

### Error Response Format

Structured errors use the `APIError` model:

```json
{
  "error_code": "SESSION_INVALID",
  "message": "Invalid or expired session",
  "details": {}
}
```

Generic HTTP errors use FastAPI's default `{"detail": "..."}` format. The `raise_api_error()` helper in `api/routes/requisitions.py` produces structured errors for all requisition operations.

### Core Data Models

The following Pydantic models appear across multiple endpoints (defined in `api/models.py`):

**Product**

| Field | Type | Description |
|---|---|---|
| `id` | `str` | Item ID as a string (from `Items.ItemId`) |
| `name` | `str` | Product description |
| `description` | `str` | Short description (may be empty) |
| `vendor` | `str` | Vendor name |
| `vendor_item_code` | `str \| null` | Vendor's part number |
| `category` | `str` | Category name (or numeric ID from ES results) |
| `image` | `str \| null` | Image URL from CrossRefs |
| `status` | `str` | `in-stock` or `discontinued` |
| `unit_of_measure` | `str` | Unit code (e.g., `Each`, `Box`) |
| `unit_price` | `float` | List price or bid price |
| `tags` | `list[str]` | Search tags (empty in SQL-sourced results) |

**ProductListResponse**

| Field | Type |
|---|---|
| `products` | `list[Product]` |
| `total` | `int` |
| `page` | `int` |
| `page_size` | `int` |
| `total_pages` | `int` |

**RequisitionStatus enum** (maps to `StatusTable.StatusId`):

| Display Name | StatusId |
|---|---|
| `On Hold` | 1 |
| `Pending Approval` | 2 |
| `Approved` | 3 |
| `Rejected` | 4 |
| `At EDS` | 5 |
| `PO Printed` | 6 |

---

## Health & System Endpoints

These endpoints are registered directly on `app` in `api/main.py`, not under a router. They have no authentication requirement.

### `GET /api/health`

Lightweight health check for load balancers and Kubernetes liveness probes.

**Response**

```json
{ "status": "ok" }
```

---

### `GET /api/status`

Full system status including database and Elasticsearch connectivity.

**Response** (`APIStatus` model)

| Field | Type | Description |
|---|---|---|
| `status` | `str` | `"healthy"` or `"degraded"` |
| `database_connected` | `bool` | Whether SQL Server connection succeeded |
| `version` | `str` | Application version string |
| `ai_enabled` | `bool` | Whether AI chat/search is available |
| `ai_provider` | `str \| null` | `"claude"`, `"ollama"`, or `null` |
| `search_enabled` | `bool` | Whether ES integration is active |
| `search_connected` | `bool` | Whether ES ping succeeded |

---

### `GET /api/debug/connection`

Returns database connection configuration details. Only available when `EDS_DEBUG=true` is set in the environment. Returns HTTP 404 otherwise.

**Response**

```json
{
  "database_connected": true,
  "config": { "server": "...", "database": "EDS" },
  "tables": ["Category", "CrossRefs", "Items", "Vendors"]
}
```

---

## Authentication (`/api/auth`)

Router prefix: `/auth` — registered at `/api/auth`.
Source: `api/routes/auth.py`

### `POST /api/auth/login`

Authenticate a user using district code, user number, and password. Delegates to the `sp_FA_AttemptLogin` stored procedure, which validates credentials and creates a row in `SessionTable`.

**Request body** (`LoginRequest`)

| Field | Type | Constraints | Description |
|---|---|---|---|
| `district_code` | `str` | max 4 chars | 4-character district code |
| `user_number` | `str` | required | User number (CometId) |
| `password` | `str` | required | User password |

**Response** (`LoginResponse`)

```json
{
  "session_id": 12345,
  "user": {
    "user_id": 678,
    "user_name": "jsmith",
    "first_name": "Jane",
    "last_name": "Smith",
    "email": "jsmith@district.edu"
  },
  "district": {
    "district_id": 42,
    "district_code": "ABCD",
    "district_name": "Example School District"
  },
  "session": {
    "session_id": 12345,
    "school_id": 7,
    "approval_level": 0
  }
}
```

**Errors**

| Status | Condition |
|---|---|
| 401 | Invalid credentials (sp returns NULL) |
| 500 | Authentication service error |

---

### `GET /api/auth/session/{session_id}`

Validate a session and return its details. Called by the frontend every 5 minutes to keep the session alive and detect expiry.

**Path parameter:** `session_id` (integer)

**Response** (`SessionResponse`)

| Field | Type | Description |
|---|---|---|
| `session_id` | `int` | Session identifier |
| `user_id` | `int` | Authenticated user |
| `district_id` | `int` | User's district |
| `school_id` | `int \| null` | User's school |
| `is_valid` | `bool` | Always `true` when response is 200 |
| `valid` | `bool` | Alias for `is_valid` (frontend compatibility) |

**Errors**

| Status | Condition |
|---|---|
| 401 | Session ended, older than 8 hours, or inactive for more than 2 hours |
| 404 | Session ID not found |

---

### `POST /api/auth/logout`

Invalidate a session by setting `SessionEnd` in `SessionTable`. Accepts `session_id` as a query parameter.

**Query parameters**

| Parameter | Type | Required |
|---|---|---|
| `session_id` | `int` | Yes |

**Response**

```json
{ "message": "Logged out successfully", "session_id": 12345 }
```

---

### `POST /api/auth/session/{session_id}/touch`

Update the `SessionLast` timestamp to reset the inactivity timer. The frontend calls this periodically during active use.

**Path parameter:** `session_id` (integer)

**Response**

```json
{ "message": "Session updated", "session_id": 12345 }
```

**Errors**

| Status | Condition |
|---|---|
| 401 | Session not found or already ended |

---

## Products (`/api/products`)

Router prefix: `/products` — registered at `/api/products`.
Source: `api/routes/products.py`

The products module queries the `Items` table directly. When Elasticsearch is enabled and a search query is provided, it transparently routes through ES and falls back to SQL on failure. The `PRODUCT_BASE_QUERY` constant in the module omits the `CrossRefs` CTE that was previously scanning 150 million rows.

### `GET /api/products`

Get a paginated, filterable list of products.

**Query parameters**

| Parameter | Type | Default | Constraints | Description |
|---|---|---|---|---|
| `query` | `str` | — | max 100 chars | Full-text search in name, description, ItemCode |
| `category` | `str` | — | max 50 chars | Filter by category name (exact) or category ID (numeric) |
| `vendor` | `str` | — | max 100 chars | Filter by vendor name (partial match) |
| `status` | `str` | — | — | Comma-separated: `in-stock`, `low-stock`, `out-of-stock`, `discontinued` |
| `min_price` | `float` | — | 0 – 1,000,000 | Minimum list price |
| `max_price` | `float` | — | 0 – 1,000,000 | Maximum list price |
| `sort_by` | `str` | — | `price`, `name` | Sort field |
| `sort_order` | `str` | `asc` | `asc`, `desc` | Sort direction |
| `page` | `int` | `1` | 1 – 10,000 | Page number |
| `page_size` | `int` | `20` | 1 – 100 | Results per page |

**Behavior notes:**

- When `query` is provided and ES is enabled, the request is routed to Elasticsearch against the `pricing_consolidated_53` index using `multi_match` with fuzzy matching across `shortDescription`, `itemCode`, `vendorName`, and related fields.
- On ES failure or when ES is disabled, falls back to SQL with a prefix-first LIKE strategy (`description%`, `% description%`) to maximize index usage.
- The unfiltered product count is cached for 5 minutes under the key `product_total_count`.
- Only items with `Active = 1`, a non-empty description, and `ListPrice > 0` are returned.

**Response** (`ProductListResponse`)

```json
{
  "products": [ /* Product objects */ ],
  "total": 48291,
  "page": 1,
  "page_size": 20,
  "total_pages": 2415
}
```

---

### `GET /api/products/search/autocomplete`

Fast prefix autocomplete for the search bar. Returns up to 20 product suggestions.

**Query parameters**

| Parameter | Type | Constraints | Description |
|---|---|---|---|
| `q` | `str` | 2–100 chars | Search prefix (required) |
| `limit` | `int` | 1–20, default 10 | Maximum number of suggestions |

**Behavior notes:**

- Attempts ES autocomplete first using `combinedTypeAheads.suggestion` (search-as-you-type field), item code prefix boosting, and phrase match boosting.
- Falls back to SQL `LIKE '%{q}%'` on ES failure.
- SQL results are cached for 5 minutes keyed by `autocomplete_{q}_{limit}`.
- ES results are deduplicated by `(name.lower(), vendor.lower())` before returning.

**Response:** `list[Product]`

---

### `GET /api/products/{product_id}`

Get a single product by its numeric `ItemId`.

**Path parameter:** `product_id` (string, must be numeric)

**Behavior notes:**

- Returns HTTP 400 if `product_id` is not a valid integer string.
- For the vendor name, falls back through `CrossRefs → Catalog → Vendors` if `Items.VendorId` is null, excluding the EDS default catalog (VendorId 7853).
- Fetches the first available image URL from `CrossRefs` where `ImageURL` is non-null and `Active = 1`.

**Response:** `Product`

---

### `GET /api/products/{product_id}/related`

Get related products based on shared vendor or category. Useful for "You may also like" UI sections.

**Path parameter:** `product_id` (string, must be numeric)

**Query parameters**

| Parameter | Type | Default | Constraints |
|---|---|---|---|
| `limit` | `int` | `8` | 1–20 |

**Behavior notes:**

- Fetches the source product's `VendorId` and `CategoryId`.
- Returns products from the same vendor first (priority order), then same category.
- Excludes the source product itself and items with no price.
- Returns an empty list (not an error) if the product is not found.

**Response:** `list[Product]`

---

### `POST /api/products/images`

Batch-fetch image URLs for up to 50 products in a single request. Used to lazy-load images after fetching a product list.

**Request body:** `list[str]` — list of product ID strings

**Response**

```json
{
  "3904313": "https://example.com/images/product.jpg",
  "3812687": null
}
```

A product ID maps to `null` (absent from the result) if no image is found. Only the first active image per product is returned.

---

### `POST /api/products/ai-search`

AI-powered natural language product search. Converts the query to SQL using an LLM and executes it.

See the dedicated [AI Search](#ai-search-apiproductsai-search) section below.

---

## Categories (`/api/categories`)

Router prefix: `/categories` — registered at `/api/categories`.
Source: `api/routes/categories.py`

### `GET /api/categories`

Get all active product categories with product counts.

**Caching:** Cached for 1 hour under the key `categories_list`. Categories change infrequently.

**Response:** `list[Category]`

| Field | Type | Description |
|---|---|---|
| `id` | `int` | `Category.CategoryId` |
| `name` | `str` | Category name |
| `product_count` | `int` | Count of active, priced items in this category |

---

### `GET /api/categories/{category_id}`

Get a single category by numeric ID.

**Path parameter:** `category_id` (integer)

**Response:** `Category`

**Errors:** HTTP 404 if not found.

---

## Vendors (`/api/vendors`)

Router prefix: `/vendors` — registered at `/api/vendors`.
Source: `api/routes/vendors.py`

### `GET /api/vendors`

Get vendors with at least one active, priced product. Excludes junk entries (names matching `NO BID`, `DELETED`, `**`, etc.) and the EDS default catalog vendor (VendorId 7853).

**Query parameters**

| Parameter | Type | Default | Constraints | Description |
|---|---|---|---|---|
| `search` | `str` | — | — | Filter vendor name (partial match) |
| `limit` | `int` | `100` | 1–500 | Maximum results |

**Caching:** When `search` is not provided, results are cached for 30 minutes under the key `vendors_list_{limit}`. Search results are never cached.

**Response:** `list[Vendor]`

| Field | Type | Description |
|---|---|---|
| `id` | `int` | `Vendors.VendorId` |
| `name` | `str` | Vendor name (trimmed) |
| `code` | `str \| null` | Vendor code |
| `product_count` | `int` | Active, priced items for this vendor |

---

### `GET /api/vendors/{vendor_id}`

Get a single vendor by numeric ID.

**Path parameter:** `vendor_id` (integer)

**Response:** `Vendor`

**Errors:** HTTP 404 if not found.

---

## Bids (`/api/bids`)

Router prefix: `/bids` — registered at `/api/bids`.
Source: `api/routes/bids.py`

Bids represent purchasing contracts (catalog entries in the `Catalog` table). Products are associated with bids through the `CrossRefs` table. The bid listing deliberately omits per-bid product counts to avoid scanning all 150 million CrossRefs rows — counts appear only in the single-bid detail endpoint.

### `GET /api/bids`

List all purchasing bids/contracts.

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `active_only` | `bool` | `true` | Only return bids with `Catalog.Active = 1` |
| `search` | `str` | — | Filter by bid name (max 100 chars) |

**Caching:** Results cached for 10 minutes under `bids_list_{active_only}_{search}`.

**Behavior notes:**

- Excludes the EDS default catalog (VendorId 7853).
- `product_count` is set to `1` (non-zero) on all listing items — actual counts require fetching the individual bid.
- `due_date` maps to `Catalog.EffectiveFrom`; `expiration_date` maps to `Catalog.EffectiveUntil`.

**Response** (`BidListResponse`)

```json
{
  "bids": [
    {
      "bid_id": 101,
      "bid_name": "NASCO 2024 Contract",
      "bid_code": "NAC24",
      "description": "Annual supplies contract",
      "vendor_count": 1,
      "product_count": 1,
      "is_active": true,
      "due_date": "2024-12-01",
      "expiration_date": "2025-11-30"
    }
  ],
  "total": 47
}
```

---

### `GET /api/bids/{bid_id}`

Get full details for a specific bid including its approved vendors.

**Path parameter:** `bid_id` (integer)

**Response** (`BidDetail`)

```json
{
  "bid_id": 101,
  "bid_name": "NASCO 2024 Contract",
  "bid_code": "NAC24",
  "description": null,
  "vendors": [
    { "vendor_id": 541, "vendor_name": "School Specialty, LLC dba Nasco Education", "product_count": 5842 }
  ],
  "product_count": 5842,
  "is_active": true,
  "due_date": "2024-12-01",
  "expiration_date": "2025-11-30"
}
```

Product count is the distinct `CrossRefs.ItemId` count for this `CatalogId` where `CrossRefs.Active = 1`.

---

### `GET /api/bids/{bid_id}/products`

Get products available under a specific bid, filtered from the `CrossRefs` join.

**Path parameter:** `bid_id` (integer)

**Query parameters**

| Parameter | Type | Default | Constraints | Description |
|---|---|---|---|---|
| `query` | `str` | — | max 100 chars | Search in description or vendor part number |
| `category` | `str` | — | max 50 chars | Filter by category name (exact) |
| `vendor` | `str` | — | max 100 chars | Filter by vendor name (exact) |
| `min_price` | `float` | — | ≥ 0 | Minimum price |
| `max_price` | `float` | — | ≥ 0 | Maximum price |
| `sort_by` | `str` | `name` | `name`, `price`, `vendor` | Sort field |
| `sort_order` | `str` | `asc` | `asc`, `desc` | Sort direction |
| `page` | `int` | `1` | ≥ 1 | Page number |
| `page_size` | `int` | `20` | 1–100 | Results per page |

**Behavior notes:**

- Price uses `ISNULL(CrossRefs.CatalogPrice, Items.ListPrice)` — the bid-negotiated price takes precedence.
- Image is the first non-null `CrossRefs.ImageURL` for the item with `Active = 1`.

**Response:** `ProductListResponse`

**Errors:** HTTP 404 if the bid does not exist.

---

### `GET /api/bids/{bid_id}/vendors`

Get the list of approved vendors for a bid with their product counts.

**Path parameter:** `bid_id` (integer)

**Response**

```json
{
  "bid_id": 101,
  "vendors": [
    { "id": 541, "name": "School Specialty, LLC dba Nasco Education", "code": "0518", "product_count": 5842 }
  ],
  "total": 1
}
```

---

### `GET /api/bids/{bid_id}/categories`

Get product categories that have at least one item under the specified bid.

**Path parameter:** `bid_id` (integer)

**Response**

```json
{
  "bid_id": 101,
  "categories": [
    { "id": 12, "name": "Art Supplies", "product_count": 432 }
  ],
  "total": 18
}
```

---

## Elasticsearch Search (`/api/search`)

Router prefix: `/search` — registered at `/api/search`.
Source: `api/routes/search.py`

This module exposes dedicated Elasticsearch search endpoints with full facet support. The underlying index is the existing `pricing_consolidated_53` index produced by the EDSIQ Java indexer. It uses camelCase field names (e.g., `shortDescription`, `bidHeaderId`, `vendorName`) rather than the API's snake_case conventions. Field mapping is handled internally.

> **Note:** This module requires ES to be enabled (`ES_ENABLED=true`). Both endpoints return HTTP 503 if ES is unavailable.

### `GET /api/search`

Full-text product search with optional bid filtering and facets.

**Query parameters**

| Parameter | Type | Default | Constraints | Description |
|---|---|---|---|---|
| `q` | `str` | — | max 200 chars | Full-text search query |
| `query` | `str` | — | max 200 chars | Alias for `q` |
| `bid_ids` | `str` | — | — | Comma-separated `BidHeaderId` values to filter by |
| `category` | `str` | — | max 100 chars | Filter by numeric category ID |
| `vendor` | `str` | — | max 100 chars | Filter by vendor name |
| `min_price` | `float` | — | ≥ 0 | Minimum `bidPrice` |
| `max_price` | `float` | — | ≥ 0 | Maximum `bidPrice` |
| `sort_by` | `str` | `relevance` | `relevance`, `price`, `name` | Sort field |
| `sort_order` | `str` | `asc` | `asc`, `desc` | Sort direction |
| `page` | `int` | `1` | 1–10,000 | Page number |
| `page_size` | `int` | `20` | 1–100 | Results per page |
| `include_facets` | `bool` | `false` | — | Include category/vendor/price aggregations |

**Behavior notes:**

- Uses `multi_match` with `best_fields` type and `AUTO` fuzziness across `shortDescription`, `productNames`, `itemCode`, `vendorName`, `keywords`, and others.
- `bid_ids` maps to the `bidHeaderId` field in ES (a long integer). Use `BidHeaderId` values from the `Bids` table per the CLAUDE.md convention.
- Price sorting uses `bidPrice` with `missing: _last`.
- Relevance sorting falls back to `orderCounts` (order popularity signal in the index).
- When `include_facets=true`, aggregations return the top 50 categories, top 50 vendors by name, and price min/max/avg statistics.

**Response** (`SearchResponse`)

```json
{
  "products": [ /* Product objects */ ],
  "total": 12842,
  "page": 1,
  "page_size": 20,
  "total_pages": 643,
  "facets": {
    "categories": [ { "name": "18", "count": 542 } ],
    "vendors": [ { "name": "School Specialty, LLC", "count": 3201 } ],
    "price_range": { "min": 0.49, "max": 1299.00, "avg": 24.87 }
  },
  "source": "elasticsearch"
}
```

---

### `GET /api/search/autocomplete`

Fast typeahead suggestions from the ES index.

**Query parameters**

| Parameter | Type | Constraints | Description |
|---|---|---|---|
| `q` | `str` | 2–100 chars, required | Partial search string |
| `bid_ids` | `str` | — | Comma-separated bid header IDs to scope suggestions |
| `limit` | `int` | 1–20, default 10 | Maximum number of suggestions |

**Behavior notes:**

- Searches across `combinedTypeAheads.suggestion` (search-as-you-type), item code, and product name fields.
- `combinedTypeAheads.suggestion` has boosted 2-gram and 3-gram sub-fields from the EDSIQ indexer.
- When `bid_ids` is provided, results are filtered by `terms` on `bidHeaderId`.

**Response:** `list[AutocompleteItem]`

| Field | Type |
|---|---|
| `id` | `str` |
| `name` | `str` |
| `vendor` | `str` |
| `category` | `str` |
| `unit_price` | `float` |
| `image` | `str \| null` |

---

## Cart (`/api/cart`)

Router prefix: `/cart` — registered at `/api/cart`.
Source: `api/routes/cart.py`

The cart is stored in server-side memory (a dict keyed by `session_id`). This is intentionally simple — the cart is session-scoped and lost if the server restarts or the request reaches a different pod. The frontend also maintains cart state in `localStorage`.

Cart data is schema-flexible: the `CartItem` model accepts several naming conventions for fields (e.g., `ItemNumber`, `item_number`, `id` for the item identifier). This accommodates different frontend versions.

### `GET /api/cart/{session_id}`

Retrieve the cart for a session.

**Path parameter:** `session_id` (string)

**Response**

```json
{ "session_id": "12345", "cart": [ { "ItemNumber": "3904313", "name": "Pencil #2", "quantity": 4, "Price": 3.99 } ] }
```

An empty cart returns `"cart": []`.

---

### `PUT /api/cart/{session_id}`

Replace the entire cart for a session. This is a full replacement, not a patch.

**Path parameter:** `session_id` (string)

**Request body** (`CartPayload`)

| Field | Type | Description |
|---|---|---|
| `session_id` | `int \| str` | Must match the path parameter |
| `cart` | `list[dict]` | Full cart contents |

**Response**

```json
{ "session_id": "12345", "cart": [ /* items */ ], "item_count": 4 }
```

**Errors:** HTTP 400 if `payload.session_id` does not match the path `session_id`.

---

### `DELETE /api/cart/{session_id}`

Clear the cart for a session.

**Path parameter:** `session_id` (string)

**Response**

```json
{ "session_id": "12345", "cart": [], "message": "Cart cleared" }
```

---

## Templates (`/api/templates`)

Router prefix: `/templates` — registered at `/api/templates`.
Source: `api/routes/templates.py`

Pre-built order templates serve as starting points for common school supply orders. There are 8 built-in default templates (Elementary Classroom Basics, High School Starter Kit, Administrative Office, Art Room Essentials, PE Equipment Pack, Computer Lab Refresh, Music Room Supplies, Teacher Desk Setup). Users can also create their own session-scoped templates that are stored in memory.

Default template items are resolved by fetching real `Items` records from the database. Resolved item data is cached for 1 hour per unique combination of `ItemId` values.

User-created templates are stored in `_user_templates: dict` (in-memory, not persisted).

### `GET /api/templates`

Retrieve all templates (defaults with live product data plus any user-created templates for the session).

**Query parameters**

| Parameter | Type | Description |
|---|---|---|
| `session_id` | `str` | Optional. If provided, user-created templates for this session are appended. |

**Response:** `list[Template]`

| Field | Type | Description |
|---|---|---|
| `id` | `str` | Template identifier (e.g., `elem-classroom`, `user-a1b2c3d4`) |
| `name` | `str` | Display name |
| `category` | `str` | Category label |
| `icon` | `str` | Font Awesome class |
| `color` | `str` | CSS color string |
| `description` | `str` | Template description |
| `items` | `list[TemplateItem]` | Line items with live pricing |
| `is_default` | `bool` | `true` for built-in templates |

**TemplateItem fields:**

| Field | Type |
|---|---|
| `item_id` | `int` |
| `item_code` | `str` |
| `name` | `str` |
| `price` | `float` |
| `qty` | `int` |
| `vendor` | `str` |
| `unit` | `str` |

---

### `POST /api/templates`

Create a user-scoped template from a set of items (typically saved from the cart).

**Query parameters**

| Parameter | Type | Required |
|---|---|---|
| `session_id` | `str` | Yes |

**Request body** (`CreateTemplateRequest`)

| Field | Type | Default | Description |
|---|---|---|---|
| `name` | `str` | required | Template name |
| `category` | `str` | `"Custom"` | Category label |
| `description` | `str` | `""` | Description |
| `items` | `list[dict]` | required | Items (flexible field names accepted) |

**Response:** `Template`

The generated template ID uses the format `user-{8 hex chars}`.

**Errors:** HTTP 400 if `session_id` is missing, name is empty, or items list is empty.

---

### `DELETE /api/templates/{template_id}`

Delete a user-created template.

**Path parameter:** `template_id` (string, must start with `user-`)

**Query parameters**

| Parameter | Type | Required |
|---|---|---|
| `session_id` | `str` | Yes |

**Response**

```json
{ "deleted": true }
```

**Errors:** HTTP 404 if not found, HTTP 400 if `session_id` is missing. Default templates cannot be deleted.

---

## Requisitions (`/api/requisitions`)

Router prefix: `/requisitions` — registered at `/api/requisitions`.
Source: `api/routes/requisitions.py`

Requisitions are the core transaction objects. A submitted requisition creates a header record in the `Requisitions` table and detail records in the `Detail` table. All write operations run within transactions. The reports cache is invalidated on every status change.

### `POST /api/requisitions/submit`

Submit a shopping cart as a new requisition.

**Request body** (`RequisitionSubmission`)

| Field | Type | Constraints | Description |
|---|---|---|---|
| `session_id` | `int` | required | Authenticated user session |
| `items` | `list[RequisitionItem]` | 1–100 items | Line items to order |
| `notes` | `str` | max 2000 chars | Order notes |
| `shipping_location` | `str` | max 200 chars | Delivery location |
| `attention_to` | `str` | max 100 chars | Attention line |
| `delivery_preference` | `str` | default `"standard"` | Delivery preference |

**RequisitionItem fields:**

| Field | Type | Constraints | Description |
|---|---|---|---|
| `item_id` | `str` | positive integer string | Must exist in `Items` table |
| `quantity` | `int` | 1–9,999 | Quantity ordered |
| `unit_price` | `float` | 0–999,999.99 | Price at time of order |
| `description` | `str` | max 500 chars | Item description |
| `vendor_item_code` | `str` | max 50 chars | Vendor part number |

**Behavior notes:**

- Validates all `item_id` values against the `Items` table before inserting. Returns HTTP 400 with a list of invalid IDs if any are missing.
- Generates a requisition number in the format `REQ-YYYYMMDD-NNNN`.
- The new requisition starts with `StatusId = 2` (Pending Approval).
- `notes`, `shipping_location`, `attention_to`, and `delivery_preference` are concatenated into the `Comments` column.
- Runs entirely within a database transaction — a failure rolls back both the header and all detail rows.

**Response** (`RequisitionResponse`)

```json
{
  "requisition_id": 45890,
  "requisition_number": "REQ-20260327-0003",
  "status": "Pending Approval",
  "total_amount": 127.45,
  "item_count": 5,
  "created_at": "2026-03-27T09:15:00"
}
```

**Errors**

| Status | Error Code | Condition |
|---|---|---|
| 401 | `SESSION_INVALID` | Invalid or expired session |
| 400 | `INVALID_ITEMS` | One or more item IDs do not exist |
| 500 | `SUBMISSION_FAILED` | Database error during transaction |

---

### `GET /api/requisitions`

List requisitions for the authenticated user with filtering and pagination.

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `session_id` | `str` | required | User session (or `"demo"`) |
| `status` | `str` | — | Filter by status display name (e.g., `"Pending Approval"`) |
| `search` | `str` | — | Search in requisition number or comments |
| `date_from` | `str` | — | Filter from date (`YYYY-MM-DD`) |
| `date_to` | `str` | — | Filter to date (`YYYY-MM-DD`, time extended to 23:59:59) |
| `sort_by` | `str` | `created_at` | `created_at`, `total_amount`, `status`, `requisition_number` |
| `sort_order` | `str` | `desc` | `asc`, `desc` |
| `page` | `int` | `1` | Page number |
| `page_size` | `int` | `20` | 1–100 |

**Response** (`RequisitionListResponse`)

```json
{
  "items": [
    {
      "requisition_id": 45890,
      "requisition_number": "REQ-20260327-0003",
      "status": "Pending Approval",
      "total_amount": 127.45,
      "item_count": 5,
      "created_at": "2026-03-27T09:15:00",
      "notes_preview": "Please deliver to Room 204"
    }
  ],
  "total": 23,
  "page": 1,
  "page_size": 20,
  "total_pages": 2,
  "status_counts": {
    "Pending Approval": 8,
    "Approved": 12,
    "Rejected": 3
  }
}
```

---

### `GET /api/requisitions/{requisition_id}`

Get header details for a single requisition.

**Path parameter:** `requisition_id` (integer)

**Query parameters**

| Parameter | Type | Required |
|---|---|---|
| `session_id` | `str` | Yes |

**Behavior:** In non-demo mode, the query includes a `UserId` filter so users can only retrieve their own requisitions.

**Response**

```json
{
  "requisition_id": 45890,
  "requisition_number": "REQ-20260327-0003",
  "status": "Pending Approval",
  "total_amount": 127.45,
  "notes": "Please deliver to Room 204\nShipping: Building A",
  "created_at": "2026-03-27T09:15:00"
}
```

---

### `GET /api/requisitions/{requisition_id}/items`

Get the line items for a requisition with product details.

**Path parameter:** `requisition_id` (integer)

**Query parameters**

| Parameter | Type | Required |
|---|---|---|
| `session_id` | `str` | Yes |

**Authorization:** Regular users can only access their own requisitions. Users with `ApprovalLevel >= 1` can access any requisition in their district.

**Response:** `list[RequisitionLineItem]`

| Field | Type | Description |
|---|---|---|
| `line_id` | `int` | `Detail.DetailId` |
| `item_id` | `int` | `Items.ItemId` |
| `product_name` | `str` | From `Items.Description` or `Detail.Description` |
| `sku` | `str` | Vendor item code or item code |
| `vendor` | `str` | From `Vendors.Name` via `Detail.VendorId` |
| `quantity` | `int` | Ordered quantity |
| `unit_price` | `float` | From `Detail.BidPrice`, `CatalogPrice`, or `GrossPrice` |
| `extended_price` | `float` | `quantity * unit_price` |

---

### `PUT /api/requisitions/{requisition_id}`

Update notes or shipping information on a requisition. Only allowed when the requisition is in `On Hold` or `Pending Approval` status.

**Path parameter:** `requisition_id` (integer)

**Query parameters**

| Parameter | Type | Required |
|---|---|---|
| `session_id` | `str` | Yes (not `"demo"`) |

**Request body** (`RequisitionUpdate`)

| Field | Type | Constraints |
|---|---|---|
| `notes` | `str` | max 2000 chars |
| `shipping_location` | `str` | max 200 chars |
| `attention_to` | `str` | max 100 chars |

**Errors**

| Status | Error Code | Condition |
|---|---|---|
| 403 | `DEMO_READ_ONLY` | Demo session used |
| 401 | `SESSION_INVALID` | Invalid session |
| 404 | `NOT_FOUND` | Requisition not owned by user |
| 400 | `INVALID_STATUS` | Status is not On Hold or Pending Approval |
| 400 | `NO_UPDATES` | No fields provided |

---

### `DELETE /api/requisitions/{requisition_id}`

Cancel a requisition (soft delete by setting `Active = 0`). Only allowed when the requisition is in `On Hold` or `Pending Approval` status.

**Path parameter:** `requisition_id` (integer)

**Query parameters**

| Parameter | Type | Required |
|---|---|---|
| `session_id` | `str` | Yes (not `"demo"`) |
| `reason` | `str` | No, max 500 chars |

**Behavior:** Appends `[Cancelled: {reason}]` to the `Comments` field and invalidates the reports cache for the user's district.

---

### `GET /api/requisitions/pending/list`

List requisitions awaiting approval for users with approval authority. Returns requisitions in `On Hold` or `Pending Approval` status within the approver's district.

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `session_id` | `str` | required | Must have `ApprovalLevel >= 1` (or `"demo"`) |
| `page` | `int` | `1` | Page number |
| `page_size` | `int` | `20` | 1–100 |

**Errors:** HTTP 403 with `NO_APPROVAL_RIGHTS` if the user lacks approval privileges.

---

### `POST /api/requisitions/{requisition_id}/approve`

Approve a pending requisition. Sets `StatusId = 3` (Approved).

**Path parameter:** `requisition_id` (integer)

**Request body** (`RequisitionApproval`)

| Field | Type | Description |
|---|---|---|
| `session_id` | `int \| str` | Approver's session ID (must have `ApprovalLevel >= 1`) |
| `comments` | `str` | Optional approval comments (max 500 chars) |

**Errors:** HTTP 403 if user lacks approval level; HTTP 400 if status does not allow approval.

---

### `POST /api/requisitions/{requisition_id}/reject`

Reject a pending requisition. Sets `StatusId = 4` (Rejected).

**Path parameter:** `requisition_id` (integer)

**Request body** (`RequisitionRejection`)

| Field | Type | Constraints | Description |
|---|---|---|---|
| `session_id` | `int \| str` | required | Approver's session |
| `reason` | `str` | 10–500 chars, required | Rejection reason |

---

## Dashboard (`/api/dashboard`)

Router prefix: `/dashboard` — registered at `/api/dashboard`.
Source: `api/routes/dashboard.py`

The dashboard provides personalized budget and activity data for all authenticated users. Authentication uses a session ID passed in the `X-Session-ID` HTTP header rather than a query parameter.

### `GET /api/dashboard/summary`

Get a user-specific dashboard summary including budget, order counts, pending approvals, and recent activity.

**Request headers**

| Header | Type | Description |
|---|---|---|
| `X-Session-ID` | `str` | User session ID (or `"demo"`) |
| `X-Demo-Approval-Level` | `int` | Override approval level in demo mode (default 1) |

**Response**

```json
{
  "budget": {
    "budget": 50000.00,
    "spent": 12340.50,
    "remaining": 37659.50,
    "percent": 25
  },
  "department_budget": null,
  "order_counts": {
    "on_hold": 2,
    "pending_approval": 5,
    "approved": 18,
    "total_active": 25
  },
  "pending_approvals": {
    "count": 12,
    "urgent": 3,
    "oldest_days": 7
  },
  "approver_info": {
    "is_approver": true,
    "level": 1,
    "district_id": 42
  },
  "recent_activity": [
    { "id": 45890, "name": "REQ-20260327-0003", "status": "Pending Approval", "time_label": "2h ago" }
  ],
  "alerts": [
    { "type": "warning", "icon": "fas fa-exclamation-circle", "title": "Budget Alert", "message": "..." }
  ]
}
```

**Behavior notes:**

- `budget.budget` defaults to $50,000 for non-demo users (the `Users` table does not have a `Budget` column in the current schema). In demo mode, it is estimated as 175% of actual spend.
- `pending_approvals` is only populated for users with `ApprovalLevel >= 1`.
- `alerts` contains budget warnings (75% threshold → warning, 90% threshold → danger) and urgent approval alerts (requisitions older than 3 days).
- `recent_activity` returns the 5 most recently updated active requisitions for the user.

---

## Reports (`/api/reports`)

Router prefix: `/reports` — registered at `/api/reports`.
Source: `api/routes/reports.py`

The reports module provides spending analytics for administrators and authorized viewers. Access requires `ApprovalLevel >= 1` OR a `UserType` in the set `{reports_viewer, department_head, principal}`. Authentication uses the `X-Session-ID` header.

Budget year: December 1 – November 30 (aligns with the EDS fiscal calendar).

**Period values and their date ranges:**

| Period | Date Range |
|---|---|
| `current` | Dec 1 of previous year to Nov 30 of current year |
| `previous` | The budget year before `current` |
| `ytd` | Dec 1 of previous year to today |
| `custom` | Requires explicit `date_start` and `date_end` |

### `GET /api/reports/summary`

Comprehensive spending report with multiple sections. Requires admin or reports viewer role.

**Request headers**

| Header | Type | Description |
|---|---|---|
| `X-Session-ID` | `str` | Session ID (or `"demo"`) |
| `X-Demo-Approval-Level` | `int` | Override level for demo mode |

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `period` | `str` | `current` | `current`, `previous`, `ytd`, `custom` |
| `date_start` | `str` | — | Required when `period=custom` (`YYYY-MM-DD`) |
| `date_end` | `str` | — | Required when `period=custom` (`YYYY-MM-DD`) |

**Caching:** All sub-queries are cached for 30 minutes keyed by district ID, date range, and section name. Recent orders are never cached. Cache is invalidated when requisitions change.

**Response**

```json
{
  "summary": {
    "total_spend": 1248930.50,
    "total_orders": 342,
    "avg_order_value": 3652.71,
    "vs_last_period": 12.3,
    "orders_vs_last": -2.1
  },
  "vendor_spend": [
    { "name": "School Specialty, LLC", "code": "0009", "orders": 145, "spend": 623450.00, "pct": 49.9 }
  ],
  "category_spend": [
    { "name": "Art Supplies", "spend": 84320.00, "pct": 6.75 }
  ],
  "monthly_trend": [
    { "month": "2024-12", "amount": 48200.00 }
  ],
  "recent_orders": [
    { "id": "REQ-20260327-0003", "date": "2026-03-27", "requester": "Jane Smith", "dept": "Elem Science", "items": 5, "amount": 127.45, "status": "Pending Approval" }
  ],
  "budget_departments": [
    { "name": "Washington Elementary", "budget": 50000.00, "spent": 12340.00, "pct": 24.7 }
  ],
  "period": "current",
  "date_range": { "start": "2024-12-01", "end": "2025-11-30" }
}
```

---

### `GET /api/reports/export`

Export reports data as a CSV file for use in Excel or other spreadsheet tools.

**Request headers:** Same as `/api/reports/summary`.

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `period` | `str` | `current` | `current`, `previous`, `ytd` |
| `section` | `str` | `all` | `all`, `vendors`, `categories`, `orders`, `monthly`, `schools` |

**Response:** `text/csv` with `Content-Disposition: attachment` header. Filename format: `eds-reports-{section}-{period}-{YYYYMMDD}.csv`.

The `all` section produces a single CSV file containing all sections in sequence, separated by blank rows.

---

### `GET /api/reports/export/pdf`

Export a formatted PDF report containing spending summary, vendor breakdown, category analysis, monthly trend, recent orders, and school budget utilization. Generated using ReportLab.

**Request headers**

| Header | Type | Description |
|---|---|---|
| `X-Session-ID` | `str` | Session ID (or `"demo"`) |
| `X-Demo-Approval-Level` | `int` | Override level for demo mode |

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `period` | `str` | `current` | `current`, `previous`, `ytd` |

**Auth:** Requires admin/approver/reports_viewer access (`require_reports_access`).

**Response:** `application/pdf` with `Content-Disposition: attachment` header. Filename format: `eds-reports-{period}-{YYYYMMDD}.pdf`.

The PDF includes all report sections (summary, vendor spend, category spend, monthly trend, recent orders, school budgets) formatted as tables with EDS branding.

---

### `GET /api/reports/drilldown/vendor`

Get line-item detail for a specific vendor. Returns the top 50 requisition line items for the vendor in the given period, ordered by line total descending.

**Request headers**

| Header | Type | Description |
|---|---|---|
| `X-Session-ID` | `str` | Session ID (or `"demo"`) |
| `X-Demo-Approval-Level` | `int` | Override level for demo mode |

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `vendor_code` | `str` | — | **Required.** Vendor code to drill into (e.g. `"0009"`) |
| `period` | `str` | `current` | `current`, `previous`, `ytd`, `custom` |
| `date_start` | `str` | — | Required when `period=custom` (`YYYY-MM-DD`) |
| `date_end` | `str` | — | Required when `period=custom` (`YYYY-MM-DD`) |

**Auth:** Requires admin/approver/reports_viewer access (`require_reports_access`).

**Response**

```json
{
  "vendor": { "name": "School Specialty, LLC", "code": "0009" },
  "period": { "start": "2024-12-01", "end": "2025-11-30" },
  "items": [
    {
      "item_name": "Crayola Markers 12pk",
      "sku": "CRY-1234",
      "qty": 50,
      "unit_price": 4.99,
      "line_total": 249.50,
      "req_number": "REQ-20260101-0042",
      "date": "2026-01-01",
      "school": "Washington Elementary"
    }
  ],
  "total_items": 50
}
```

**Notable behavior:** Results are filtered to the user's district (via `DistrictId` from their session). Only active detail lines are included (`Active IS NULL OR Active = 1`). Cancelled requisitions (`StatusId = 1`) are excluded.

---

### `GET /api/reports/drilldown/category`

Get requisition-level detail for a specific category. Returns the top 50 requisitions in the given category and period, ordered by total cost descending.

**Request headers**

| Header | Type | Description |
|---|---|---|
| `X-Session-ID` | `str` | Session ID (or `"demo"`) |
| `X-Demo-Approval-Level` | `int` | Override level for demo mode |

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `category_name` | `str` | — | **Required.** Category name to drill into (e.g. `"Art Supplies"`) |
| `period` | `str` | `current` | `current`, `previous`, `ytd`, `custom` |
| `date_start` | `str` | — | Required when `period=custom` (`YYYY-MM-DD`) |
| `date_end` | `str` | — | Required when `period=custom` (`YYYY-MM-DD`) |

**Auth:** Requires admin/approver/reports_viewer access (`require_reports_access`).

**Response**

```json
{
  "category": "Art Supplies",
  "period": { "start": "2024-12-01", "end": "2025-11-30" },
  "items": [
    {
      "req_number": "REQ-20260115-0008",
      "date": "2026-01-15",
      "requester": "Jane Smith",
      "school": "Lincoln Middle School",
      "amount": 1245.00,
      "status": "Approved",
      "item_count": 12
    }
  ],
  "total_items": 50
}
```

**Notable behavior:** Results are filtered to the user's district. Cancelled requisitions (`StatusId = 1`) are excluded. The `item_count` field shows the number of active detail lines per requisition.

---

## AI Search (`/api/products/ai-search`)

Registered under the products router at `/api/products`.
Source: `api/routes/ai_search.py`

AI search converts natural language queries into SQL using the DBA Agent's `QueryGeneratorTool`. The generated SQL is validated for safety before execution.

**Feature flag:** `AI_SEARCH_ENABLED` is `true` when `ANTHROPIC_API_KEY` is set or `LLM_PROVIDER=ollama`.

**Security:** Generated SQL is validated:
1. Must be a `SELECT` statement.
2. Must not contain dangerous keywords (`DROP`, `DELETE`, `UPDATE`, `INSERT`, `ALTER`, `CREATE`, `TRUNCATE`, `EXEC`, `xp_`, etc.).
3. Must reference the `Items` table.

### `POST /api/products/ai-search`

**Request body** (`AISearchRequest`)

| Field | Type | Constraints | Description |
|---|---|---|---|
| `query` | `str` | 3–300 chars | Natural language search (e.g., `"red pencils under $5"`) |
| `page` | `int` | 1–1,000, default 1 | Page number |
| `page_size` | `int` | 1–100, default 20 | Results per page |

**Example queries:**
- `"paper products from Staples sorted by price"`
- `"cheapest notebooks in Writing Supplies category"`
- `"PE equipment under $50 with more than 100 in stock"`

**Response** (`AISearchResponse`)

```json
{
  "products": [ /* Product objects */ ],
  "total": 20,
  "page": 1,
  "page_size": 20,
  "total_pages": 2,
  "ai_explanation": "Searching for notebooks filtered to the Writing Supplies category, sorted by ascending price",
  "generated_sql": "SELECT TOP 20 i.ItemId as id, i.Description as name, ..."
}
```

**Notes on total:** When the result count equals `page_size`, the total is estimated as `page_size * (page + 1)` since the AI-generated SQL may not include a `COUNT`. This is intentionally approximate.

**Errors**

| Status | Condition |
|---|---|
| 503 | AI feature not enabled (configure `ANTHROPIC_API_KEY` or `LLM_PROVIDER=ollama`) |
| 400 | Generated SQL failed safety validation |
| 500 | LLM query generation failed |

---

## AI Chat (`/api/chat`)

Router prefix: `/chat` — registered at `/api/chat`.
Source: `api/routes/ai_chat.py`

The chat module wraps the `EDSAgent` with a customer-facing system prompt. It maintains per-session agent instances (up to 50 cached simultaneously; oldest evicted when full). Sessions are keyed by the `session_id` field in requests, distinct from authentication sessions.

**Feature flag:** `AI_CHAT_ENABLED` is `true` when `ANTHROPIC_API_KEY` is set or `LLM_PROVIDER=ollama`.

**Ollama keepalive:** When using Ollama, a background task sends a minimal generation request every 4 minutes to prevent the model from unloading due to inactivity.

### `POST /api/chat`

Send a message to the shopping assistant. Supports multi-turn conversation via `session_id`.

**Request body** (`ChatRequest`)

| Field | Type | Constraints | Description |
|---|---|---|---|
| `message` | `str` | 1–2,000 chars | User message |
| `session_id` | `str` | optional | Omit to start a new conversation |

**Response** (`ChatResponse`)

| Field | Type | Description |
|---|---|---|
| `response` | `str` | Assistant's reply text |
| `session_id` | `str` | Session ID for continuing the conversation |
| `sql_generated` | `str \| null` | SQL generated by the agent, if any |
| `docs_retrieved` | `list[str]` | RAG documentation snippets used |

**Errors:** HTTP 503 if AI chat is not enabled.

---

### `POST /api/chat/warmup`

Pre-load the Ollama model into memory to eliminate cold-start latency. Safe to call on any provider — it returns `{"status": "skipped"}` if not using Ollama.

**Response**

```json
{ "status": "ok", "model": "qwen2.5:14b", "message": "Model loaded and ready" }
```

---

### `POST /api/chat/stream`

Streaming chat endpoint using Server-Sent Events (SSE). Returns text chunks as the model generates them.

**Request body:** Same as `POST /api/chat` (`ChatRequest`)

**Response:** `text/event-stream`

Each SSE event is a JSON object with a `type` field:

| Event type | Fields | Description |
|---|---|---|
| `chunk` | `content: str` | Partial response text |
| `status` | `content: str` | Tool invocation status (e.g., searching database) |
| `done` | `session_id: str` | Stream complete |
| `error` | `message: str` | User-friendly error occurred |

**Example stream:**

```
data: {"type": "chunk", "content": "I found "}
data: {"type": "chunk", "content": "several notebooks "}
data: {"type": "done", "session_id": "abc-123"}
```

The response headers include `Cache-Control: no-cache` and `X-Accel-Buffering: no` to prevent nginx from buffering the stream.

---

### `DELETE /api/chat/{session_id}`

End a chat session and clean up agent state.

**Path parameter:** `session_id` (string)

**Response**

```json
{ "status": "ok", "message": "Session abc-123 ended" }
```

---

## Admin (`/api/admin`)

Router prefix: `/admin` — registered at `/api/admin`.
Source: `api/routes/admin.py`

All admin endpoints require `ApprovalLevel >= 1` in the authenticated session. The `session_id` is passed as a query parameter (integer). The admin module queries some table columns (`CreatedAt`, `TotalAmount`, `Status`) that use schema conventions from a legacy data model — some queries in this module may not match the actual production schema perfectly and may require adjustment.

### Dashboard Endpoints

#### `GET /api/admin/dashboard/stats`

High-level system metrics for the admin dashboard.

**Query parameters:** `session_id` (int, required)

**Response**

```json
{
  "metrics": {
    "ordersToday": 12,
    "ordersChange": 20,
    "pendingApprovals": 34,
    "urgentApprovals": 5,
    "totalSpend": 84320.00,
    "spendSparkline": [3200, 4100, 2800, 5200, 3900, 4800, 6100],
    "activeUsers": 47,
    "onlineNow": 8
  }
}
```

---

#### `GET /api/admin/dashboard/departments`

Department budget summaries for the dashboard.

**Query parameters:** `session_id` (int, required)

**Response:** `{ "departments": [ { "name": "...", "spent": 0.0, "budget": 0.0, "percent": 0, "color": "#3b82f6" } ] }`

---

#### `GET /api/admin/dashboard/recent-orders`

Recent orders for the dashboard activity feed.

**Query parameters**

| Parameter | Type | Default |
|---|---|---|
| `session_id` | `int` | required |
| `limit` | `int` | 10 |

**Response:** `{ "recentOrders": [ { "id": "REQ-...", "requester": "...", "total": 0.0, "status": "...", "date": "..." } ] }`

---

#### `GET /api/admin/dashboard/pending-orders`

Orders currently awaiting approval.

**Query parameters**

| Parameter | Type | Default |
|---|---|---|
| `session_id` | `int` | required |
| `limit` | `int` | 10 |

**Response:** `{ "pendingOrders": [ { "id": "REQ-...", "requester": "...", "total": 0.0, "submitted": "..." } ] }`

---

#### `GET /api/admin/dashboard/spending-chart`

Monthly spending totals for charting.

**Query parameters**

| Parameter | Type | Default |
|---|---|---|
| `session_id` | `int` | required |
| `year` | `int` | current year |

**Response:** `{ "labels": ["Jan", "Feb", ...], "data": [0.0, ...], "year": 2026 }`

---

#### `GET /api/admin/dashboard/top-products`

Top products by order count.

**Query parameters**

| Parameter | Type | Default |
|---|---|---|
| `session_id` | `int` | required |
| `limit` | `int` | 5 |

**Response:** `{ "topProducts": [ { "name": "...", "orders": 0, "revenue": 0.0 } ] }`

---

### User Management Endpoints

#### `GET /api/admin/users`

Paginated list of users with optional filters.

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `session_id` | `int` | required | Admin session |
| `search` | `str` | `""` | Search in name, email, department |
| `role` | `str` | `""` | Filter by role |
| `status` | `str` | `""` | Filter by user status |
| `department` | `str` | `""` | Filter by department name |
| `page` | `int` | `1` | Page number |
| `page_size` | `int` | `20` | 1–100 |

**Response**

```json
{
  "users": [
    {
      "id": 678,
      "name": "Jane Smith",
      "email": "jsmith@district.edu",
      "department": "Elementary Science",
      "role": "requester",
      "status": "active",
      "budget": 50000.0,
      "budgetUsed": 25,
      "lastActive": "2026-03-27T09:00:00"
    }
  ],
  "total": 142,
  "page": 1,
  "page_size": 20,
  "total_pages": 8,
  "stats": { "total": 142, "active": 138, "admins": 4, "newThisMonth": 2 },
  "departments": ["Art", "Elementary Science", "Physical Education"]
}
```

---

#### `PUT /api/admin/users/{user_id}`

Update a user record (stub — body parsing deferred to frontend implementation).

**Path parameter:** `user_id` (integer)
**Query parameters:** `session_id` (int, required)

**Response:** `{ "message": "User updated", "user_id": 678 }`

---

### Budget Management Endpoints

#### `GET /api/admin/budgets/overview`

High-level district budget summary.

**Query parameters:** `session_id` (int, required)

**Response**

```json
{
  "overview": {
    "totalBudget": 2500000.0,
    "available": 1875000.0,
    "availablePercent": 75,
    "spent": 625000.0,
    "spentPercent": 25,
    "overBudgetDepts": 1
  }
}
```

---

#### `GET /api/admin/budgets/departments`

Per-department budget details.

**Query parameters:** `session_id` (int, required)

**Response:** `{ "departments": [ { "id": 1, "name": "...", "budget": 0.0, "spent": 0.0, "remaining": 0.0, "percent": 0, "users": 0 } ] }`

---

#### `GET /api/admin/budgets/users`

Per-user budget details with optional filters.

**Query parameters**

| Parameter | Type | Default |
|---|---|---|
| `session_id` | `int` | required |
| `search` | `str` | `""` |
| `department` | `str` | `""` |

**Response:** `{ "userBudgets": [ { "id": 0, "name": "...", "email": "...", "department": "...", "budget": 0.0, "spent": 0.0, "remaining": 0.0, "percent": 0 } ] }`

---

### Admin Reports Endpoints

These are distinct from the user-facing `/api/reports` endpoints and operate on different schema column names.

#### `GET /api/admin/reports/summary`

Report summary statistics for a date range and optional department.

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `session_id` | `int` | required | Admin session |
| `date_range` | `str` | `this_month` | `this_week`, `this_month`, `this_quarter`, `this_year` |
| `department` | `str` | `all` | Filter by department name |

**Response:** `{ "summary": { "totalSpend": 0.0, "totalOrders": 0, "avgOrderValue": 0.0, "totalItems": 0, "uniqueProducts": 0, "activeUsers": 0, "ordersPerUser": 0.0, "totalBudget": 0.0 } }`

---

#### `GET /api/admin/reports/by-department`

Spending broken down by department.

**Query parameters**

| Parameter | Type | Default |
|---|---|---|
| `session_id` | `int` | required |
| `date_range` | `str` | `this_month` |

**Response:** `{ "departments": [ { "name": "...", "orders": 0, "items": 0, "spend": 0.0, "budget": 0.0, "percentUsed": 0, "color": "..." } ] }`

---

#### `GET /api/admin/reports/top-products`

Top products ranked by total spend.

**Query parameters**

| Parameter | Type | Default |
|---|---|---|
| `session_id` | `int` | required |
| `date_range` | `str` | `this_month` |
| `limit` | `int` | 10 (1–50) |

**Response:** `{ "topProducts": [ { "id": 0, "name": "...", "sku": "...", "category": "...", "quantity": 0, "unitPrice": 0.0, "totalSpend": 0.0 } ] }`

---

#### `GET /api/admin/reports/top-users`

Top spenders ranked by total order value.

**Query parameters**

| Parameter | Type | Default |
|---|---|---|
| `session_id` | `int` | required |
| `date_range` | `str` | `this_month` |
| `limit` | `int` | 10 (1–50) |

**Response**

```json
{
  "topUsers": [
    {
      "id": 1042,
      "name": "Jane Smith",
      "email": "jsmith@district.edu",
      "department": "Science",
      "orders": 28,
      "items": 145,
      "totalSpend": 8432.50
    }
  ]
}
```

| Field | Type | Description |
|---|---|---|
| `id` | `int` | User ID |
| `name` | `str` | Full name (`FirstName + LastName`), or `"Unknown"` if null |
| `email` | `str` | User email, or `""` if null |
| `department` | `str` | Department name, or `""` if unassigned |
| `orders` | `int` | Count of non-cancelled/rejected/draft requisitions |
| `items` | `int` | Total quantity of items across all requisitions |
| `totalSpend` | `float` | Sum of `TotalAmount` across requisitions |

---

### Search Index Management

These endpoints manage the Elasticsearch product index. They are located in `api/routes/admin.py` under the `/admin` router prefix but have **no authentication requirement** — any client can call them without a session.

#### `POST /api/admin/search/reindex`

Trigger an Elasticsearch reindex of all products. The reindex runs as a background task.

**Auth:** None. This endpoint has no authentication or session requirement.

**Query parameters**

| Parameter | Type | Default | Description |
|---|---|---|---|
| `full` | `bool` | `false` | `false` = incremental (append/update into existing index). `true` = drop and recreate the index, then reindex all products. |

**Response** (`200 OK`)

```json
{
  "message": "Incremental reindex started in background",
  "check_status": "/api/admin/search/status"
}
```

**Error:** Returns `409 Conflict` if a reindex is already in progress.

**Notable behavior:** The reindex runs in a FastAPI `BackgroundTasks` worker. Use `GET /api/admin/search/status` to poll for completion and results.

---

#### `GET /api/admin/search/status`

Get the current Elasticsearch index status and the result of the last reindex operation.

**Auth:** None. This endpoint has no authentication or session requirement.

**Query parameters:** None.

**Response** (`200 OK`)

```json
{
  "enabled": true,
  "reindex_running": false,
  "last_run": "2026-03-27T14:30:00Z",
  "last_result": {
    "indexed": 48200,
    "errors": 0,
    "doc_count": 48200,
    "full_reindex": false,
    "elapsed_seconds": 12.3
  },
  "last_error": null,
  "index": {
    "exists": true,
    "doc_count": 48200,
    "size_bytes": 52428800,
    "size_mb": 50.0
  }
}
```

| Field | Type | Description |
|---|---|---|
| `enabled` | `bool` | Whether Elasticsearch is enabled (`ES_ENABLED` env var) |
| `reindex_running` | `bool` | Whether a reindex background task is currently running |
| `last_run` | `str\|null` | ISO 8601 timestamp of last completed reindex |
| `last_result` | `object\|null` | Result of last reindex: `indexed`, `errors`, `doc_count`, `full_reindex`, `elapsed_seconds` |
| `last_error` | `str\|null` | Error message if last reindex failed |
| `index` | `object` | Live ES index stats: `exists`, `doc_count`, `size_bytes`, `size_mb`. May contain `error` or `unavailable` if ES is unreachable. |

---

## Appendix: Status Codes

### HTTP Status Codes Used

| Code | Meaning in This API |
|---|---|
| 200 | Successful response |
| 400 | Bad request (invalid parameters, constraint violation, unsafe AI SQL) |
| 401 | Session invalid, expired, or not found |
| 403 | Insufficient privileges (not an admin/approver, demo mode write attempt) |
| 404 | Resource not found |
| 429 | Rate limit exceeded |
| 500 | Internal server error or database failure |
| 503 | Optional feature not enabled (ES, AI chat, AI search) |

### Requisition Status Values

| StatusId | Name | Transitions Allowed From |
|---|---|---|
| 1 | On Hold | Submit, Update, Cancel |
| 2 | Pending Approval | Update, Cancel, Approve, Reject |
| 3 | Approved | (terminal for user actions) |
| 4 | Rejected | (terminal for user actions) |
| 5 | At EDS | (set by EDS staff) |
| 6 | PO Printed | (set by EDS staff) |

---

## Appendix: Environment Variables

| Variable | Default | Description |
|---|---|---|
| `EDS_ENV` | `development` | Set to `production` to restrict CORS |
| `EDS_CORS_ORIGINS` | — | Comma-separated allowed origins (required in production) |
| `EDS_RATE_LIMIT` | `120` | Requests per minute per IP |
| `EDS_BEHIND_PROXY` | `false` | Trust `X-Forwarded-For` for real client IP |
| `EDS_DEBUG` | `false` | Enable `/api/debug/connection` endpoint |
| `DB_SERVER` | — | SQL Server hostname |
| `DB_DATABASE_CATALOG` | `EDS` | Database name for API |
| `DB_USERNAME` | — | SQL Server username |
| `DB_PASSWORD` | — | SQL Server password |
| `ES_URL` | `http://20.122.81.233:9200` | Elasticsearch cluster URL |
| `ES_ENABLED` | `true` | Enable/disable Elasticsearch integration |
| `ES_INDEX` | `pricing_consolidated_53` | ES index name |
| `ANTHROPIC_API_KEY` | — | Claude API key (enables AI features) |
| `LLM_PROVIDER` | `claude` (with key) or `ollama` | LLM provider for AI endpoints |
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |
| `OLLAMA_MODEL` | `qwen2.5:14b` | Model name for Ollama |
