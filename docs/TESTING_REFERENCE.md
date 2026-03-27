# EDS Testing Reference

Comprehensive technical reference for the EDS test suite. This document expands on [TESTING.md](TESTING.md) with deep coverage of test infrastructure, fixture hierarchies, mocking patterns, and guidelines for each test layer.

**Related documents:** [TESTING.md](TESTING.md) | [DEVELOPMENT.md](DEVELOPMENT.md) | [CI_CD.md](CI_CD.md) | [API_REFERENCE.md](API_REFERENCE.md)

---

## Table of Contents

1. [Test Suite Overview](#1-test-suite-overview)
2. [Test Infrastructure](#2-test-infrastructure)
3. [Fixture Hierarchy](#3-fixture-hierarchy)
4. [Mocking Patterns](#4-mocking-patterns)
5. [API Test Suite](#5-api-test-suite)
6. [E2E Test Suite](#6-e2e-test-suite)
7. [Root-Level Unit Tests](#7-root-level-unit-tests)
8. [Visual Regression Testing](#8-visual-regression-testing)
9. [Test Configuration Reference](#9-test-configuration-reference)
10. [Running Tests](#10-running-tests)
11. [Writing New Tests](#11-writing-new-tests)
12. [Debugging Guide](#12-debugging-guide)

---

## 1. Test Suite Overview

The EDS test suite is organized into three distinct layers, each with a clear scope and set of dependencies.

```
tests/
├── conftest.py                    # Root fixtures (scripts layer)
├── test_config.py                 # Config module unit tests (13 tests)
├── test_db_utils.py               # Database utility unit tests (14 tests)
├── test_investigate_blocking.py   # Blocking analysis script tests
├── test_deploy_indexes.py         # Index deployment script tests
├── test_recursive_procedures.py   # SP recursion analysis tests
│
├── api/                           # FastAPI endpoint tests (no real DB)
│   ├── conftest.py                # test_client, mock fixtures
│   ├── test_health.py             # Health/status/CORS (6 tests)
│   ├── test_middleware.py         # Security headers, rate limiting, auth (22 tests)
│   ├── test_auth.py               # Login, session, logout, touch (14 tests)
│   ├── test_products.py           # Products CRUD and search (24 tests)
│   ├── test_categories.py         # Category listing (4 tests)
│   ├── test_vendors.py            # Vendor listing (4 tests)
│   ├── test_requisitions.py       # Requisition lifecycle (32 tests)
│   ├── test_ai_search.py          # AI-powered product search (14 tests)
│   ├── test_ai_chat.py            # AI chat and streaming SSE (21 tests)
│   ├── test_dashboard.py          # Dashboard summary endpoint (12 tests)
│   └── test_reports.py            # Reports, exports, cache (34 tests)
│
└── e2e/                           # Playwright browser tests (require live server)
    ├── conftest.py                # Playwright fixtures, CLI options
    ├── screenshot_utils.py        # Visual comparison utilities
    ├── test_login_workflow.py     # Auth flows, form validation, accessibility
    ├── test_product_browsing.py   # Product grid, search, mobile view
    ├── test_cart_workflow.py      # Cart drawer, budget, persistence
    ├── test_checkout_workflow.py  # Checkout, form, cart items
    ├── test_requisition_listing.py # Requisitions page, filters, empty state
    ├── test_approval_workflow.py  # Approval dashboard, stats, auth
    ├── test_critical_flows.py     # End-to-end critical journeys (6 flows)
    └── test_visual_regression.py  # Screenshot comparison baselines
```

### Test Count Summary

| Layer | Files | Approximate Tests |
|-------|-------|-------------------|
| Root unit (scripts) | 5 files | ~60 tests |
| API tests | 11 files | ~187 tests |
| E2E tests | 8 files | ~107 tests |
| **Total** | **24 files** | **~353 tests** |

### Test Markers

Three custom pytest markers are registered:

| Marker | Purpose | Deselect With |
|--------|---------|---------------|
| `e2e` | Browser tests requiring a live server and Playwright | `-m "not e2e"` |
| `integration` | Tests requiring a real SQL Server connection | `-m "not integration"` |
| `slow` | Tests that take more than a few seconds | `-m "not slow"` |

In CI, only `not e2e and not integration` tests run by default. The E2E suite is intended for local pre-release verification.

---

## 2. Test Infrastructure

### Python Environment

The test suite requires the package installed in editable mode with at minimum the `dev` extra. For API tests, the `api` extra is also needed. For E2E tests, the `e2e` extra is additionally required.

```bash
# Minimum for unit + API tests
pip install -e ".[dev,api]"

# Full suite including E2E
pip install -e ".[dev,api,e2e]"
playwright install chromium
```

### Rate Limit Bypass

The root `conftest.py` sets `EDS_RATE_LIMIT=999999` **before any app imports**. This is critical — the rate limit middleware reads this environment variable at module load time. Setting it after import would have no effect.

```python
# tests/conftest.py (line 12)
os.environ["EDS_RATE_LIMIT"] = "999999"
```

Without this, tests that make multiple requests to the same endpoint within a short window would receive `429 Too Many Requests` responses, causing false failures.

### Path Configuration

The root `conftest.py` inserts both the project root and the `scripts/` directory onto `sys.path`. This allows test files to import scripts-layer modules (`config`, `db_utils`, etc.) directly without package prefixes.

```python
project_root = Path(__file__).parent.parent
scripts_dir = project_root / 'scripts'
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(scripts_dir))
```

The `tests/api/conftest.py` additionally ensures the `api/` parent is importable:

```python
api_dir = Path(__file__).parent.parent.parent / 'api'
sys.path.insert(0, str(api_dir.parent))
```

### Cache Isolation

Every API test runs with a cleared in-memory cache. The `clear_cache` fixture in `tests/api/conftest.py` is marked `autouse=True` so it applies to every test in the `tests/api/` package without requiring explicit fixture declarations.

```python
@pytest.fixture(autouse=True)
def clear_cache():
    from api.cache import get_cache
    cache = get_cache()
    cache._cache.clear()
    yield
    cache._cache.clear()
```

This ensures that TTL-cached responses from one test do not leak into subsequent tests.

---

## 3. Fixture Hierarchy

Fixtures are organized in a three-level hierarchy that mirrors the directory structure. Lower-level conftest files override or extend upper-level fixtures.

```
conftest.py (root)
├── sample_config          scope=function
├── mock_db_credentials    scope=function  (monkeypatches env vars)
└── temp_output_dir        scope=function  (tmp_path based)

tests/api/conftest.py
├── clear_cache            scope=function, autouse=True
├── test_client            scope=module    (FastAPI TestClient)
├── mock_db_connection     scope=function
├── sample_product_data    scope=function
├── sample_product_list    scope=function
├── sample_categories      scope=function
├── sample_vendors         scope=function
├── mock_db_products       scope=function  (uses mock_db_connection + sample_product_list)
├── mock_healthy_db        scope=function  (patches api.main.test_connection -> True)
└── mock_unhealthy_db      scope=function  (patches api.main.test_connection -> False)

tests/e2e/conftest.py
├── base_url               scope=session   (checks server availability)
├── server_available       scope=session   (True if http://, False if file://)
├── browser                scope=session   (Chromium instance)
├── page                   scope=function  (new context + page per test)
├── frontend_url           scope=function
├── make_url               scope=function  (factory: make_url("checkout") -> URL)
├── api_base_url           scope=function
├── authed_page            scope=function  (intercepts /api/auth/session/* -> valid)
├── snapshot_dir           scope=session   (tests/e2e/snapshots/)
└── update_snapshots       scope=session   (--update-snapshots CLI flag)
```

### Key Fixture Details

**`test_client` (module scope)**

The `test_client` fixture creates a single `TestClient` instance shared across all tests in a module. Module scope is used rather than session scope because each module may need slightly different app state. The `TestClient` uses `with` to ensure proper startup/shutdown lifecycle.

```python
@pytest.fixture(scope="module")
def test_client():
    from api.main import app
    with TestClient(app) as client:
        yield client
```

**`authed_page` (E2E)**

The `authed_page` fixture creates a Playwright browser page that intercepts all calls to `/api/auth/session/*` and returns `{"is_valid": True}`. This prevents the Alpine.js auth store from clearing the localStorage session and redirecting to the login page mid-test.

```python
def handle_session_validation(route):
    route.fulfill(
        status=200,
        content_type="application/json",
        body=json.dumps({"is_valid": True}),
    )
page.route("**/api/auth/session/*", handle_session_validation)
```

Without this intercept, any test that seeds a fake session in localStorage would see it invalidated on the next Alpine.js re-render cycle.

**`make_url` (E2E)**

A factory fixture that builds URLs for any page. When a live HTTP server is detected, it returns `http://localhost:8000/{page_name}`. When no server is running, it falls back to `file://` paths within the `frontend/` directory.

```python
url = make_url("checkout")         # http://localhost:8000/checkout
url = make_url("admin/approvals")  # http://localhost:8000/admin/approvals
url = make_url("login")            # http://localhost:8000/login
```

---

## 4. Mocking Patterns

### Pattern 1: Route-Level DB Function Mocking

The most common pattern in API tests. The database helper functions (`execute_query`, `execute_single`) are patched at the point where they are imported into the route module, not at the definition site.

```python
# CORRECT: patch where it's used
with patch('api.routes.products.execute_query') as mock_query, \
     patch('api.routes.products.execute_single') as mock_single:
    mock_single.return_value = {"total": 100}
    mock_query.return_value = [{"id": 1, "name": "Test Product", ...}]
    response = test_client.get("/api/products")
```

This is a critical distinction. Patching `api.database.execute_query` would not affect code that has already imported the name into `api.routes.products`.

### Pattern 2: Context Manager Mocking (`get_db_cursor`)

For routes that use the `get_db_cursor()` context manager directly (auth routes, requisitions), the mock must replicate the `__enter__`/`__exit__` protocol:

```python
@patch("api.routes.auth.get_db_cursor")
def test_login_success(self, mock_cursor_ctx, test_client):
    mock_cursor = MagicMock()
    mock_cursor_ctx.return_value.__enter__ = MagicMock(return_value=mock_cursor)
    mock_cursor_ctx.return_value.__exit__ = MagicMock(return_value=False)
    mock_cursor.fetchone.side_effect = [login_row, session_row]
```

The `side_effect` list is used when the cursor's `fetchone` is called multiple times with different expected results (e.g., first the stored procedure result, then the session details query).

### Pattern 3: Auth Dependency Mocking

Endpoints protected by `get_user_from_session` (a dependency injected through FastAPI's `Depends`) are tested by patching the function at the route module's namespace:

```python
@patch("api.routes.requisitions.get_user_from_session")
def test_submit_success(self, mock_session, mock_txn, test_client):
    mock_session.return_value = {
        "UserId": 42,
        "SchoolId": 5,
        "DistrictId": 1,
        "ApprovalLevel": 0,
        "UserName": "Jane Doe",
    }
```

To simulate an invalid or expired session, return `None`:

```python
mock_session.return_value = None
# -> endpoint should return 401
```

### Pattern 4: Transaction Context Manager

Routes that use `transaction()` require mocking both the context manager and the cursor it yields:

```python
@patch("api.routes.requisitions.transaction")
def test_submit_success(self, mock_session, mock_txn, test_client):
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_txn.return_value.__enter__ = MagicMock(return_value=(mock_conn, mock_cursor))
    mock_txn.return_value.__exit__ = MagicMock(return_value=False)
    # Configure fetchone side effects for multi-step transactions
    mock_cursor.fetchone.side_effect = [
        (1,),         # item exists check
        (1,),         # second item exists check
        MagicMock(**{"__getitem__": lambda s, i: "REQ-20250105-0001"}),
        (1000,),      # inserted requisition_id
    ]
```

### Pattern 5: Isolated Rate Limit Testing

The `TestRateLimiting` class creates minimal FastAPI apps with specific rate limits rather than using the shared `test_client`. This prevents the global `EDS_RATE_LIMIT=999999` override from masking rate limit behavior in dedicated tests.

```python
def _make_app(self, requests_per_minute=5):
    app = FastAPI()
    app.add_middleware(RateLimitMiddleware, requests_per_minute=requests_per_minute)

    @app.get("/test")
    async def test_endpoint():
        return {"ok": True}

    return TestClient(app)

def test_blocks_over_limit(self):
    client = self._make_app(requests_per_minute=3)
    for _ in range(3):
        response = client.get("/test")
        assert response.status_code == 200
    response = client.get("/test")
    assert response.status_code == 429
    assert "Retry-After" in response.headers
```

### Pattern 6: Feature Flag Mocking

AI features (chat, search) use module-level boolean flags that can be patched in tests without affecting other tests:

```python
@patch("api.routes.ai_search.AI_SEARCH_ENABLED", False)
def test_disabled_returns_503(self, test_client):
    response = test_client.post("/api/products/ai-search", json={"query": "pencils"})
    assert response.status_code == 503

@patch("api.routes.ai_chat.AI_CHAT_ENABLED", True)
@patch("api.routes.ai_chat._LLM_PROVIDER", "ollama")
def test_ollama_provider_used(self, mock_get_agent, test_client):
    ...
```

### Pattern 7: Module-Level State Restoration

For tests that need to temporarily modify module-level variables (like the provider configuration), save and restore the originals in a try/finally block:

```python
def test_feature_flag_auto_detect(self):
    import api.routes.ai_chat as mod
    orig_key = mod._API_KEY
    orig_provider = mod._LLM_PROVIDER
    orig_enabled = mod.AI_CHAT_ENABLED
    try:
        mod._API_KEY = ""
        mod._LLM_PROVIDER = "ollama"
        mod.AI_CHAT_ENABLED = bool(mod._API_KEY) or mod._LLM_PROVIDER == "ollama"
        assert mod.AI_CHAT_ENABLED is True
    finally:
        mod._API_KEY = orig_key
        mod._LLM_PROVIDER = orig_provider
        mod.AI_CHAT_ENABLED = orig_enabled
```

### Pattern 8: E2E localStorage Seeding

E2E tests authenticate by directly writing to the browser's `localStorage` from the login page (where no auth redirect is triggered), then navigating to the target page:

```python
def goto_approvals_authed(page, make_url):
    # 1. Visit login (no auth redirect here)
    page.goto(make_url("login"))
    page.wait_for_load_state("domcontentloaded")
    # 2. Write session data
    seed_approver_session(page)
    # 3. Navigate — Alpine.js auth store finds session immediately
    page.goto(make_url("admin/approvals"))
    page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
    page.wait_for_timeout(1000)
```

### Pattern 9: E2E API Route Interception

For consistent test states (e.g., empty requisition lists), E2E tests intercept API calls and return controlled responses:

```python
def handle_requisitions(route):
    route.fulfill(
        status=200,
        content_type="application/json",
        body=json.dumps({
            "items": [], "total": 0, "total_pages": 0,
            "page": 1, "page_size": 20, "status_counts": {},
        }),
    )
page.route("**/api/requisitions*", handle_requisitions)
```

---

## 5. API Test Suite

All API tests use FastAPI's `TestClient` from `tests/api/conftest.py`. No real database is involved — all DB calls are mocked.

### 5.1 test_health.py — Health and Status Endpoints

**6 tests | Classes: `TestHealthEndpoints`, `TestCORSHeaders`**

| Test | What It Verifies |
|------|-----------------|
| `test_root_endpoint` | `GET /` returns 200 with `text/html` (serves frontend) |
| `test_health_check` | `GET /api/health` returns `{"status": "ok"}` |
| `test_status_healthy_db` | `GET /api/status` shows `healthy` when DB connected |
| `test_status_unhealthy_db` | `GET /api/status` shows `degraded` when DB disconnected |
| `test_cors_headers_present` | OPTIONS preflight accepted |
| `test_cors_allows_local_origin` | `localhost:3000` origin is allowed in development mode |

The `mock_healthy_db` and `mock_unhealthy_db` fixtures patch `api.main.test_connection` (the call site), not `api.database.test_connection` (the definition). This distinction is important for mock targeting.

### 5.2 test_middleware.py — Security, Rate Limiting, Auth

**22 tests | Classes: `TestSecurityHeaders`, `TestRateLimiting`, `TestGetCurrentUser`, `TestSessionConstants`**

**Security Headers (8 tests)**

Each test verifies a specific HTTP security header is present on responses:

| Header | Expected Value |
|--------|---------------|
| `Content-Security-Policy` | Contains `default-src 'self'`, `cdn.jsdelivr.net`, `cdn.tailwindcss.com`, `cdnjs.cloudflare.com` |
| `X-Frame-Options` | `DENY` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | Disables `camera`, `microphone`, `geolocation` |

**Rate Limiting (5 tests)**

Rate limit tests use isolated minimal apps (see [Pattern 5](#pattern-5-isolated-rate-limit-testing)). Key behaviors verified:

- Requests under the limit succeed (200)
- The (limit+1)th request returns 429 with `Retry-After` header
- 429 response body contains `"Too many requests"` in the `detail` field
- `/api/health` is exempt from rate limiting
- Paths starting with `/js/`, `/css/`, `/images/` are exempt

**Auth Dependency (5 tests)**

Tests for the `get_current_user` FastAPI dependency in `api/middleware.py`:

| Scenario | Expected Behavior |
|----------|-----------------|
| Valid session within time limits | 200, returns user dict |
| Non-existent session (`execute_single` returns None) | 401 |
| Session age exceeds `SESSION_TIMEOUT_HOURS` (8h) | 401, `"expired"` in detail |
| Inactive for more than `SESSION_INACTIVITY_HOURS` (2h) | 401, `"inactivity"` in detail |
| Missing `session_id` query parameter | 422 |

**Session Constants (3 tests)**

Sanity checks that `SESSION_TIMEOUT_HOURS > 0`, `SESSION_INACTIVITY_HOURS > 0`, and `SESSION_INACTIVITY_HOURS < SESSION_TIMEOUT_HOURS`.

### 5.3 test_auth.py — Authentication Routes

**14 tests | Classes: `TestLogin`, `TestGetSession`, `TestLogout`, `TestTouchSession`**

**TestLogin — POST /api/auth/login**

Tests the `sp_FA_AttemptLogin` stored procedure integration:

| Test | Scenario |
|------|---------|
| `test_login_success` | Returns session_id, user info, district info on success |
| `test_login_invalid_credentials` | Stored proc returns NULL → 401 |
| `test_login_no_result` | `fetchone` returns None → 401 |
| `test_login_missing_fields` | Missing `user_number` or `password` → 422 |
| `test_login_district_code_too_long` | Code > 4 chars → 422 |

The success test configures `fetchone.side_effect` with two return values: the stored procedure result (SessionId), then the session details query result (full user record).

**TestGetSession — GET /api/auth/session/{session_id}**

Tests the session validation endpoint called by the frontend every 5 minutes:

| Test | Scenario |
|------|---------|
| `test_valid_session` | Active session → 200, `is_valid: true` |
| `test_session_not_found` | No row → 404 |
| `test_session_already_ended` | `SessionEnd` is not null → 401, `"expired"` |
| `test_session_expired_age` | `session_age_hours > 8` → 401 |
| `test_session_inactive_too_long` | `inactive_hours > 2` → 401, `"inactivity"` |

**TestLogout and TestTouchSession**

Verify that logout always returns 200 (even for already-ended sessions), and that touch returns 401 when `rowcount == 0` (session not found).

### 5.4 test_products.py — Products Endpoints

**24 tests | Classes: `TestGetProducts`, `TestAutocomplete`, `TestGetSingleProduct`, `TestInputSanitization`, `TestProductModel`**

**TestGetProducts — GET /api/products**

Covers the main paginated product listing:

| Parameter | Test Coverage |
|-----------|--------------|
| `page`, `page_size` | Valid pagination, invalid page (0 → 422), page_size > 100 → 422 |
| `query` | Free-text search passed through |
| `category` | Category filter |
| `vendor` | Vendor filter |
| `min_price`, `max_price` | Valid range, invalid range (min > max → 400) |
| `status` | Single status, comma-separated multiple statuses |

Response structure is verified to include: `products`, `total`, `page`, `page_size`, `total_pages`.

**TestInputSanitization**

Tests the `sanitize_search_input` function imported directly from the route module:

- SQL injection attempts (semicolons, DROP statements) are stripped
- XSS attempts (`<script>` tags) are removed
- Valid characters (alphanumeric, spaces, `#`) are preserved
- Maximum length (`MAX_QUERY_LENGTH`) is enforced
- `validate_status_filter` only passes known status values (`in-stock`, `low-stock`, etc.)

**TestProductModel**

Tests the `map_row_to_product` function that converts database rows to `Product` Pydantic models:

- `id` is always cast to string
- NULL database values for `name`, `vendor`, `category`, `unit_of_measure` use safe defaults (`"Unknown Product"`, `"Unknown Vendor"`, `"General"`, `"Each"`)
- NULL `unit_price` becomes `0.0`

### 5.5 test_categories.py and test_vendors.py

**4 tests each | Structure: success, empty list, database error, response structure**

These are symmetric tests. Both verify:
- Success returns a list with correct field structure
- Empty database returns `[]`
- An unexpected exception from the DB layer becomes a 500 response
- Response items contain expected keys (`id`, `name`, `product_count` / `id`, `name`)

### 5.6 test_requisitions.py — Requisition Lifecycle

**32 tests | Classes: `TestSubmitRequisition`, `TestListRequisitions`, `TestGetRequisition`, `TestGetRequisitionItems`, `TestUpdateRequisition`, `TestCancelRequisition`, `TestListPendingApprovals`, `TestApproveRequisition`, `TestRejectRequisition`**

This is the most complex test module, covering the complete requisition state machine.

**User Personas**

Three user dicts are defined as module-level constants:

| Name | ApprovalLevel | Purpose |
|------|--------------|---------|
| `VALID_USER` | 0 | Standard user, no approval rights |
| `APPROVER_USER` | 2, DistrictId=1 | District approver |
| `CROSS_DISTRICT_APPROVER` | 2, DistrictId=99 | Approver from a different district |

**Status Machine Coverage**

| Status Transition | What's Tested |
|------------------|--------------|
| Submit → Pending Approval | Success, invalid session, invalid item IDs, empty items |
| Pending Approval → Approved | Success, cross-district rejection, no rights, already approved, not found |
| Pending Approval → Rejected | Success, reason too short (< 10 chars), missing reason, no rights, cross-district |
| Approved/Rejected → Update | Blocked (INVALID_STATUS error code) |
| Approved/Rejected → Cancel | Blocked (INVALID_STATUS error code) |
| Pending Approval → Cancel | Allowed |

**Business Rule Tests**

- Total amount calculation is verified: `(3 * 9.99) + (1 * 15.50) = 45.47` (float comparison within 0.01)
- Pending approvals list returns 403 for non-approvers (error_code: `NO_APPROVAL_RIGHTS`)
- Item ownership check: `GET /api/requisitions/{id}/items` returns 404 if the requisition does not belong to the requesting user
- District isolation: approvers cannot act on requisitions from other districts (error_code: `CROSS_DISTRICT`)

### 5.7 test_ai_search.py — AI-Powered Product Search

**14 tests | Classes: `TestAISearchEndpoint`, `TestSQLValidation`, `TestGeneratorFailures`**

Tests the `POST /api/products/ai-search` endpoint. The `_generate_product_sql` internal function is always mocked so no real LLM calls are made.

**Safety Validation Tests**

The SQL validator in the route is tested exhaustively:

| SQL Pattern | Expected Result |
|-------------|----------------|
| Valid SELECT with Items table | 200 |
| `DROP TABLE Items;` prefix | 400 |
| `DELETE FROM Items` | 400 |
| `UPDATE Items SET ...` | 400 |
| SELECT from Vendors (not Items) | 400, message contains `"Items"` |
| Empty string SQL from generator | 500 |

**Feature Flag Tests**

When `AI_SEARCH_ENABLED = False` (no API key configured), the endpoint returns 503 with `"not available"` in the detail.

### 5.8 test_ai_chat.py — AI Chat and SSE Streaming

**21 tests | Classes: `TestChatEndpoint`, `TestEndSession`, `TestChatStream`, `TestWarmup`, `TestProviderConfig`**

Tests the `POST /api/chat` endpoint and its streaming variant `POST /api/chat/stream`.

**SSE Event Parsing**

The streaming tests parse Server-Sent Events from the response body:

```python
events = []
for line in response.text.strip().split("\n\n"):
    if line.startswith("data: "):
        events.append(json.loads(line[6:]))
```

**Event Types Verified**

| Type | When Emitted |
|------|-------------|
| `chunk` | Normal response token |
| `status` | `[STATUS:message]` marker from agent |
| `done` | End of stream, includes `session_id` |
| `error` | Agent exception (user-friendly message) |

**Error Handling**

- `RuntimeError` mid-stream produces an `error` event (not a 500)
- `ConnectionError` produces an error event with `"connecting"` or `"trouble"` in the message
- The 200 status is maintained even when the stream encounters an error (SSE protocol requirement)

### 5.9 test_dashboard.py — Dashboard Summary

**12 tests | Class: `TestDashboardSummary`**

Tests `GET /api/dashboard/summary` with `X-Session-ID` header.

**Session Modes**

| Session ID Value | Mode |
|-----------------|------|
| `"demo"` | Demo mode — queries all districts, estimates budget as 175% of spend |
| Integer string (e.g., `"999"`) | User-specific mode — queries by UserId/DistrictId |
| `"not-a-number"` | Invalid → 401 |
| None/missing | Falls through to demo mode |

**Alert Threshold Tests**

| Spend Percentage | Expected Alert Type |
|-----------------|-------------------|
| < 75% | No budget alert |
| 75–89% | `"warning"` type alert |
| 90%+ | `"danger"` type alert, title contains `"Nearly Exhausted"` |

**Response Structure**

Verified keys: `budget`, `department_budget`, `order_counts`, `pending_approvals`, `approver_info`, `recent_activity`, `alerts`. The `deadlines` key is explicitly verified to be absent (it was removed).

### 5.10 test_reports.py — Reports and Exports

**34 tests | Classes: `TestReportsSummary`, `TestCSVExport`, `TestPDFExport`, `TestCacheInvalidation`, `TestAuthGuards`, `TestDateRangeComputation`, `TestDrillDown`**

An `autouse` module-level fixture mocks all six query functions so no DB calls occur:

```python
@pytest.fixture(autouse=True)
def mock_reports_queries():
    with patch("api.routes.reports._get_spending_summary", return_value=_MOCK_SUMMARY.copy()) as m1, \
         patch("api.routes.reports._get_vendor_spend", return_value=list(_MOCK_VENDORS)) as m2, \
         ...
        yield {...}
```

**Key Tests**

- Demo mode calls `_get_spending_summary` with `district_id=0` (all districts)
- CSV export verifies `Content-Type: text/csv` and `Content-Disposition: attachment`
- Section-specific exports (`?section=vendors`) only contain the relevant section
- CSV filename contains the period name (e.g., `previous`)
- PDF export verifies `Content-Type: application/pdf`, `%PDF` magic bytes, and size > 2000 bytes
- Cache invalidation for a specific district does not affect other districts' caches
- Cache hit returns the same data without calling the query function again

**Date Range Logic**

`_compute_date_range` is tested for:
- `"current"` → ends with `-12-01` start, `-11-30` end (EDS budget year)
- `"previous"` → exactly one year before current
- `"ytd"` → end date equals today

---

## 6. E2E Test Suite

E2E tests require a live running server at `http://localhost:8000` and a Playwright Chromium installation. All test classes are marked with `pytestmark = pytest.mark.e2e`.

### 6.1 Playwright Setup

The E2E conftest manages the browser lifecycle:

```
session scope: browser (Chromium, headless)
  function scope: page (new BrowserContext per test, 1280x720 viewport)
  function scope: authed_page (with route intercept for session validation)
```

Browser context is closed after each test, ensuring complete isolation between tests (cookies, localStorage, IndexedDB all cleared).

**Custom CLI Options**

```bash
# Override server URL
pytest tests/e2e/ --base-url http://staging.eds.example.com

# Update visual regression baselines instead of comparing
pytest tests/e2e/test_visual_regression.py --update-snapshots
```

**Server Availability Detection**

The `base_url` fixture probes `{url}/api/health` with a 3-second timeout. If the server is unreachable, it falls back to `file://` URLs pointing to the `frontend/` directory. Most E2E tests skip when using `file://` since Alpine.js CDN scripts won't load.

### 6.2 test_login_workflow.py

**Classes: `TestLoginPageRender`, `TestLoginFormValidation`, `TestLoginSession`, `TestLoginAccessibility`**

**Page Render**

- Page title contains `"Login"` or `"Sign In"`
- All three form fields (`#districtCode`, `#userNumber`, `#password`) are visible
- Password show/hide toggle changes the input type between `password` and `text`

**Form Validation**

- Empty submit does not navigate away from login
- District code auto-converts to uppercase (Alpine.js `@input` handler)
- District code has `maxlength="4"` attribute

**Session Management**

- No `eds-session` in localStorage → stays on login page after reload
- Valid session in localStorage → `authed_page` keeps it valid (via route intercept)
- `localStorage.removeItem('eds-session')` removes the session cleanly

**Accessibility**

- `a.skip-link` element is present
- Each `<input>` has a `<label for="...">` association
- Password field has `aria-describedby` attribute
- An `[role="alert"]` region exists for error messages

### 6.3 test_product_browsing.py

**Classes: `TestProductBrowsing`, `TestSearch`, `TestMobileView`**

- Page title contains `"Requisition"`
- `.products-area` is visible after loading
- `#grid-view-btn` and `#list-view-btn` are visible and clickable
- `header.header` and `.logo` are present
- `.cart-btn` is present
- Mobile viewport (375×667): `button:has(i.fa-bars)` (hamburger) is visible
- Mobile: `.cart-btn` is still accessible

### 6.4 test_cart_workflow.py

**Classes: `TestCartDrawer`, `TestBudgetIndicator`, `TestQuickOrder`, `TestCartPersistence`**

- Cart drawer opens showing `"Order List"` heading when `.cart-btn` is clicked
- Cart can be closed via `Alpine.store('ui').closeCartDrawer()` JavaScript call
- Empty cart shows `"Your cart is empty"` message
- `.budget-indicator` and `.budget-amount` are visible on desktop (1280px)
- `.budget-bar` progress element is present
- Quick Order button opens a panel with `h2:has-text('Quick Order')` heading
- Cart data survives page reload when seeded into `localStorage`

### 6.5 test_checkout_workflow.py

**Classes: `TestCartWithItems`, `TestCheckoutPage`, `TestCartQuantityManagement`**

- Cart badge count reflects item quantities (`eds-cart` key in localStorage)
- Cart drawer shows `"Order List"` heading with seeded items
- Cart drawer shows `"$"` or `"Total"` text
- Empty cart shows `"Your cart is empty"` after clearing localStorage
- Checkout page body contains checkout-related text
- Checkout with empty cart (no items seeded) shows `cart_length == 0`
- Multiple items stored correctly (5-item array test)

### 6.6 test_requisition_listing.py

**Classes: `TestRequisitionPageRender`, `TestRequisitionStatusFilters`, `TestRequisitionSearchAndSort`, `TestRequisitionEmptyState`, `TestRequisitionAuth`, `TestRequisitionNavigation`**

- `h1.page-title` contains `"Requisition"` or `"Order"`
- `a:has-text('New Order')` is visible
- `a.skip-link` is present (accessibility)
- At least 4 `.status-card` elements visible (All, Submitted, Pending, Approved, Cancelled)
- `"All Orders"` status card exists
- `.search-filter input` and `.sort-filter select` are visible
- `.sort-filter select` has at least 3 options
- Two `input[type='date']` elements for date range filter
- Empty state when API returns `{"items": []}` (via route intercept)
- `a:has-text('Start Shopping')` is in the DOM
- Navigation: `a.nav-link:has-text('Shop')` visible, `a.nav-link.active` contains `"Orders"`
- `a.btn-primary:has-text('New Order')` has `href="/"`

### 6.7 test_approval_workflow.py

**Classes: `TestApprovalPageRender`, `TestApprovalStats`, `TestApprovalFilters`, `TestApprovalEmptyState`, `TestApprovalAuth`, `TestApprovalNavigation`**

All tests in this file skip unless a live server is running, because the approval page uses Alpine.js `x-data` on the `<body>` tag.

- Title contains `"Approval"`, `h1.page-title` contains `"Approval"`
- Exactly 4 `.stat-card` elements
- `.stat-label` text contains `"pending"`
- Each `.stat-value` contains at least one digit or `$`
- `.search-filter input` has a non-null placeholder
- `.filter-select` has at least 3 options
- `button:has-text('Refresh')` is visible
- Without session: cleared localStorage → redirect or null session
- Seeded approver session has `approval_level == 2`
- Navigation: `Shop` and `My Orders` links visible, `Approvals` nav link is active

### 6.8 test_critical_flows.py

**6 critical flow groups | Classes: `TestLoginToDashboard`, `TestBrowseAndAddToCart`, `TestCartToCheckout`, `TestSessionExpiry`, `TestProductNormalization`, `TestAdminAccess`**

This file tests the full end-to-end journeys that cross multiple pages.

**Flow 1: Login → Dashboard**

- Unauthenticated visit to main page redirects to `login` URL
- Authenticated user sees dashboard content (Dashboard/Welcome/Overview/Recent)
- User name (Jane/Doe/JD) appears on the page
- Navigation items are visible on desktop

**Flow 2: Browse → Add to Cart**

- Switching to browse view shows product-related content
- Seeded cart items (3 + 5 = 8 total) are reflected in `eds_cart` localStorage
- Adding via Alpine store's `addToCart()` method persists to localStorage

**Flow 3: Cart → Checkout**

- Cart drawer with mixed field-naming items shows `"$"` in text
- Checkout page loads with cart items
- Empty cart checkout shows `cart_length == 0`

**Flow 4: Session Expiry**

- Removing `eds-session` then navigating redirects to login
- Malformed session JSON in localStorage redirects to login

**Flow 5: Product Field Normalization**

Tests the `edsProduct.normalize()` JavaScript function that maps between snake_case API fields and PascalCase cart/legacy fields:

| Input Format | Verified Output Fields |
|-------------|----------------------|
| `{id, name, unit_price, vendor}` | `{ItemNumber, Description, Price, VendorName}` |
| `{ItemNumber, Description, Price, VendorName}` | Pass-through unchanged |

The `edsCart.total()` function is verified to handle four price field name variants: `Price`, `price`, `UnitPrice`, `unit_price`.

**Flow 6: Admin Access**

- `isAdmin` computed property is `false` for `approval_level: 0` users
- `isAdmin` is `true` for `approval_level: 2` users (via seeded admin session)

---

## 7. Root-Level Unit Tests

These tests cover the Python scripts layer (`scripts/` directory) and do not touch the API.

### 7.1 test_config.py — Configuration Module

**13 tests | Classes: `TestConfig`, `TestThresholds`**

Tests the `config.py` module that loads `config.yaml` with environment variable overrides.

| Test | What It Verifies |
|------|-----------------|
| `test_config_loads_defaults` | `database.name == 'dpa_EDSAdmin'`, `timeout == 30`, `critical == 95` |
| `test_validate_params_*` | `days` must be 1-365, `min_saving` 0-100, `hours` 1-8760, `latency_ms` 0-10000 |
| `test_get_threshold` | `get_threshold('missing_index', 'critical')` returns 95 |
| `test_get_threshold_invalid_*` | Unknown category/level raises `ValueError` |
| `test_env_override` | `DB_DATABASE` env var overrides YAML value |
| Threshold dataclasses | `MissingIndexThresholds`, `BlockingThresholds`, `IOLatencyThresholds` default values |

### 7.2 test_db_utils.py — Database Utilities

**14 tests | Classes: `TestDatabaseConnection`, `TestConvenienceFunctions`, `TestDatabaseErrors`**

Tests the `db_utils.py` module used by monitoring scripts (distinct from `api/database.py`).

**Connection Lifecycle**

- `DatabaseConnection` reads server/credentials from environment variables
- `is_connected` is `False` before `connect()`, `True` within `with` block
- `mock_conn.close()` is called after exiting the context manager

**Credential Validation**

- Missing `DB_SERVER` → `DatabaseConnectionError: "Missing database credentials"`
- Missing `DB_USERNAME` → same error

**Query Methods**

- `execute_query` → `cursor.fetchall()`, returns list of tuples
- `fetch_one` → `cursor.fetchone()`, closes cursor
- `fetch_scalar` → `fetchone()[0]`, returns `None` when no results

**Error Classes**

`DatabaseConnectionError` and `DatabaseQueryError` both extend `Exception` and preserve the error message string.

---

## 8. Visual Regression Testing

Visual regression tests use a custom pixel-level comparison engine built on Pillow. This is separate from Playwright's built-in screenshot comparison.

### Directory Structure

```
tests/e2e/snapshots/
├── baseline/         # Committed to git — golden reference images
│   ├── login-page.png
│   ├── product-grid.png
│   ├── cart-drawer-items.png
│   └── ...
├── actual/           # Generated at test time — gitignored
└── diff/             # Generated on mismatch — gitignored
```

### Comparison Algorithm

The `compare_screenshots` function in `screenshot_utils.py` performs pixel-level comparison:

1. Both images are converted to RGB and their sizes are compared
2. Size mismatch is recorded but comparison continues (expected is resized to match actual)
3. `ImageChops.difference()` computes the per-pixel delta
4. A pixel is considered "changed" if any RGB channel delta exceeds `pixel_threshold` (default: 25)
5. The mismatch ratio (changed pixels / total pixels) is compared to `threshold` (default: 10%)
6. If `mismatch_ratio > threshold`, the test fails

The per-channel threshold of 25 (out of 255) accommodates sub-pixel rendering differences across OS and font hinting variations.

### Diff Visualization

When a mismatch is detected, a three-panel diff image is saved to `snapshots/diff/`:

```
[ Expected | Actual | Diff Heatmap ]
```

The diff heatmap highlights changed pixels in red and dims unchanged pixels to 33% brightness.

### Masking Dynamic Content

Elements whose content changes between test runs (timestamps, user names, budget amounts, item counts) are hidden before screenshot capture using `mask_selectors`:

```python
HEADER_MASKS = [
    ".user-greeting",    # "Welcome, Jane"
    ".budget-amount",    # live dollar amounts
    ".cart-count",       # item count badge
]

TIMESTAMP_MASKS = [
    "time",
    "[x-text*='date']",
    ".stat-value",
]

assert_screenshot_match(
    page, "product-grid", snapshot_dir,
    mask_selectors=HEADER_MASKS,
    wait_ms=2000,
)
```

Hidden elements are set to `visibility: hidden` (not `display: none`) so layout is preserved.

### Baseline Management

```bash
# Generate all baselines for the first time
pytest tests/e2e/test_visual_regression.py \
  --base-url http://localhost:8000 \
  --update-snapshots

# Update a single snapshot after an intentional UI change
pytest tests/e2e/test_visual_regression.py \
  -k "login_page" \
  --update-snapshots

# Compare against existing baselines
pytest tests/e2e/test_visual_regression.py \
  --base-url http://localhost:8000
```

When `--update-snapshots` is passed, `assert_screenshot_match` copies the actual screenshot to the baseline directory and skips the comparison assertion. Old diff images are deleted.

### Visual Test Coverage

| Test Class | Snapshots | Threshold |
|-----------|-----------|-----------|
| `TestLoginPageVisual` | login-page, login-page-error | 5% |
| `TestProductPageVisual` | product-grid, product-list, product-header | 8–10% |
| `TestCartDrawerVisual` | cart-drawer-items, cart-drawer-empty | 8–10% |
| `TestCheckoutPageVisual` | checkout-with-items | 10% |
| `TestApprovalDashboardVisual` | approval-dashboard, approval-stats | 10% |
| `TestRequisitionListingVisual` | requisition-listing | 10% |
| `TestMobileVisual` | mobile-product-page, mobile-login-page | 5–10% |

Mobile tests create a 375×667 browser context to simulate iPhone SE dimensions.

---

## 9. Test Configuration Reference

### pyproject.toml Settings

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = [
    "-v",           # Verbose output (show each test name)
    "--tb=short",   # Short traceback on failure
    "--strict-markers",  # Fail on unknown markers
]
markers = [
    "slow: marks tests as slow (deselect with '-m \"not slow\"')",
    "integration: marks tests that require database connection",
    "e2e: marks end-to-end tests that require browser (deselect with '-m \"not e2e\"')",
]

[tool.coverage.run]
source = ["scripts", "api"]
omit = [
    "scripts/__init__.py",
    "api/__init__.py",
    "tests/*",
]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "def __repr__",
    "raise NotImplementedError",
    "if __name__ == .__main__.:",
]
```

### Environment Variables for Tests

| Variable | Default in Tests | Purpose |
|----------|-----------------|---------|
| `EDS_RATE_LIMIT` | `999999` (set by root conftest) | Prevents 429 errors in tests |
| `DB_SERVER` | `test-server.local` (via `mock_db_credentials`) | Prevents real DB connection |
| `DB_USERNAME` | `test_user` | Mock credential |
| `DB_PASSWORD` | `test_pass` | Mock credential |
| `DB_DATABASE` | `test_db` | Mock database name |

---

## 10. Running Tests

### Standard Commands

```bash
# All tests except E2E and integration (recommended for local dev)
pytest -m "not e2e and not integration"

# All non-E2E tests with coverage
pytest -m "not e2e and not integration" \
  --cov=api --cov=scripts --cov-report=html

# API tests only
pytest tests/api/

# Root unit tests only (scripts layer)
pytest tests/ --ignore=tests/api --ignore=tests/e2e

# E2E tests (requires: uvicorn api.main:app --port 8000 running)
pytest tests/e2e/ -m e2e

# Visual regression tests
pytest tests/e2e/test_visual_regression.py \
  --base-url http://localhost:8000

# Update visual regression baselines
pytest tests/e2e/test_visual_regression.py \
  --base-url http://localhost:8000 \
  --update-snapshots
```

### Targeted Runs

```bash
# Single file
pytest tests/api/test_requisitions.py

# Single class
pytest tests/api/test_requisitions.py::TestApproveRequisition

# Single test
pytest tests/api/test_requisitions.py::TestApproveRequisition::test_approve_success

# By keyword
pytest -k "approve or reject"

# By multiple keywords
pytest -k "approval and not cross_district"
```

### Coverage Reports

```bash
# HTML report (open htmlcov/index.html)
pytest --cov=api --cov=scripts --cov-report=html

# Terminal summary with missing lines
pytest --cov=api --cov-report=term-missing

# XML for CI upload
pytest --cov=api --cov-report=xml
```

### Parallel Execution

```bash
# Install pytest-xdist for parallel runs
pip install pytest-xdist

# Run with 4 workers (API tests are safe to parallelize)
pytest tests/api/ -n 4

# Note: E2E tests should NOT be run in parallel (shared browser resource)
```

---

## 11. Writing New Tests

### Choosing the Right Test Layer

| What You're Testing | Use |
|---------------------|-----|
| Business logic, data transformation | Root unit test |
| API response structure, status codes | API test (mocked DB) |
| Database query logic | Integration test (or unit test with mocked cursor) |
| User-facing behavior, navigation, forms | E2E test |
| Visual layout, CSS correctness | Visual regression test |

### Adding an API Test

1. Determine which route module the endpoint lives in (e.g., `api.routes.products`)
2. Create a test class in the appropriate file under `tests/api/`
3. Use `test_client` fixture from `tests/api/conftest.py`
4. Patch `execute_query` and/or `execute_single` at the route module's namespace
5. Follow the AAA (Arrange, Act, Assert) pattern

```python
class TestMyNewEndpoint:
    """Test GET /api/my-endpoint."""

    def test_success(self, test_client):
        """Happy path: returns expected data."""
        with patch('api.routes.my_module.execute_query') as mock_query:
            mock_query.return_value = [{"id": 1, "name": "Test"}]

            response = test_client.get("/api/my-endpoint")

            assert response.status_code == 200
            data = response.json()
            assert len(data) == 1
            assert data[0]["name"] == "Test"

    def test_empty_returns_empty_list(self, test_client):
        """Empty database returns empty list, not 404."""
        with patch('api.routes.my_module.execute_query') as mock_query:
            mock_query.return_value = []
            response = test_client.get("/api/my-endpoint")
            assert response.status_code == 200
            assert response.json() == []

    def test_database_error_returns_500(self, test_client):
        """Unexpected DB exception becomes 500."""
        with patch('api.routes.my_module.execute_query') as mock_query:
            mock_query.side_effect = Exception("Connection lost")
            response = test_client.get("/api/my-endpoint")
            assert response.status_code == 500
```

### Adding a Protected Endpoint Test

For endpoints that require authentication:

```python
VALID_USER = {
    "UserId": 42, "SchoolId": 5, "DistrictId": 1,
    "ApprovalLevel": 0, "UserName": "Test User",
}

class TestProtectedEndpoint:
    @patch("api.routes.my_module.execute_query")
    @patch("api.routes.my_module.get_user_from_session")
    def test_authenticated_success(self, mock_session, mock_query, test_client):
        mock_session.return_value = VALID_USER
        mock_query.return_value = [{"id": 1}]

        response = test_client.get("/api/protected?session_id=101")
        assert response.status_code == 200

    @patch("api.routes.my_module.get_user_from_session")
    def test_unauthenticated_401(self, mock_session, test_client):
        mock_session.return_value = None
        response = test_client.get("/api/protected?session_id=999")
        assert response.status_code == 401
```

### Adding an E2E Test

```python
import pytest

pytestmark = pytest.mark.e2e


class TestMyFeature:
    """Test my feature E2E flow."""

    def test_feature_works(self, authed_page, make_url, server_available):
        """Test that the feature displays correctly for authenticated users."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        # Seed session on login page first
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")
        page.evaluate("""
            () => localStorage.setItem('eds-session', JSON.stringify({
                session_id: 12345,
                user: { user_id: 1, first_name: 'Test', last_name: 'User' },
                district: { district_id: 1, district_code: 'TEST' },
                session: { session_id: 12345, school_id: 1, approval_level: 0 }
            }))
        """)

        # Navigate to target page
        page.goto(make_url("my-feature-page"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Assert
        assert page.locator(".my-feature-container").is_visible()
        assert "Expected Text" in page.locator("body").inner_text()
```

### Adding a Visual Regression Test

```python
from .screenshot_utils import assert_screenshot_match

class TestMyPageVisual:
    def test_my_page_layout(self, authed_page, make_url, snapshot_dir,
                             update_snapshots, server_available):
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        # Navigate with auth...

        assert_screenshot_match(
            page,
            "my-page-layout",          # Snapshot name (becomes baseline/my-page-layout.png)
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,             # Allow up to 10% pixel difference
            mask_selectors=[".timestamp", ".dynamic-count"],  # Hide changing elements
            wait_ms=1500,               # Wait for animations to settle
            full_page=False,            # Viewport only (default)
        )
```

### Test Naming Conventions

```
File:     test_{module_or_feature}.py
Class:    Test{Feature}                  (e.g., TestSubmitRequisition)
Method:   test_{behavior}_{condition}    (e.g., test_approve_cross_district)
```

Write the docstring as a one-sentence description of what the test verifies, in plain English:

```python
def test_approve_cross_district(self, mock_session, mock_single, test_client):
    """Cannot approve requisition from different district."""
```

---

## 12. Debugging Guide

### Common Failures and Solutions

**`ModuleNotFoundError: No module named 'api'`**

```bash
# Install in editable mode
pip install -e ".[dev,api]"
```

**`429 Too Many Requests` in API tests**

The rate limit environment variable must be set before app import. Verify `os.environ["EDS_RATE_LIMIT"] = "999999"` appears at the top of `tests/conftest.py` before any other imports.

**E2E test skips even though server is running**

The `base_url` fixture checks `{url}/api/health`. Ensure the server is running with `uvicorn api.main:app --port 8000`. If using a different port, pass `--base-url http://localhost:{port}`.

**`playwright._impl._errors.Error: Timeout ... waiting for function "typeof Alpine !== 'undefined'"`**

The Alpine.js CDN script failed to load. Ensure the server is running and the frontend HTML files reference the CDN correctly. In `file://` mode, CDN scripts will not load; tests that call `wait_for_function("typeof Alpine")` will skip.

**Visual regression failures after a legitimate UI change**

Run with `--update-snapshots` to accept the new baseline:

```bash
pytest tests/e2e/test_visual_regression.py -k "my_test" --update-snapshots
```

Commit the updated baseline files in `tests/e2e/snapshots/baseline/`.

**`AssertionError: assert 401 == 200` in requisition tests**

Usually means the `get_user_from_session` mock was not set up or returned `None`. Verify the patch target matches the route module: `api.routes.requisitions.get_user_from_session`.

**`side_effect` list exhausted in multi-call mock**

When `fetchone.side_effect` is a list, it yields one item per call. If the route makes more calls than items in the list, the mock raises `StopIteration`. Add an additional entry to the list.

### Verbose Debugging

```bash
# Full tracebacks with local variables
pytest tests/api/test_requisitions.py -v --tb=long -l

# Drop into pdb on failure
pytest --pdb

# Print all stdout/stderr
pytest -s

# E2E: run with browser visible (headed mode)
pytest tests/e2e/ --headed

# E2E: slow down all actions by 500ms
pytest tests/e2e/ --headed --slowmo=500
```

### Coverage Gaps

```bash
# Identify uncovered lines in the API
pytest tests/api/ --cov=api --cov-report=term-missing | grep "MISS"
```

Coverage is configured to include `scripts` and `api` modules, excluding `__init__.py` files, `__repr__` methods, `raise NotImplementedError` lines, and `if __name__ == "__main__":` guards.

---

*This reference covers the test suite as of March 2026. See [CI_CD.md](CI_CD.md) for how tests are executed in the automated pipeline.*
