"""
Visual regression tests for key EDS pages and UI states.

Captures screenshots and compares against baseline images to detect
unintended CSS / layout changes.

Usage:
    # Compare against existing baselines:
    pytest tests/e2e/test_visual_regression.py --base-url http://localhost:8000

    # Generate or update baselines:
    pytest tests/e2e/test_visual_regression.py --base-url http://localhost:8000 --update-snapshots

    # Run a single snapshot:
    pytest tests/e2e/test_visual_regression.py -k "login_page" --update-snapshots

Baselines are stored in tests/e2e/snapshots/baseline/ and should be
committed to version control.  Actual captures and diff images are in
snapshots/actual/ and snapshots/diff/ (gitignored).
"""

import json

import pytest

from .screenshot_utils import assert_screenshot_match

pytestmark = pytest.mark.e2e

# ── Shared dynamic-content masks ────────────────────────────────────────
# Elements whose text changes between runs (timestamps, usernames, counts)
# are hidden before capture so they don't cause false-positive diffs.

HEADER_MASKS = [
    ".user-greeting",       # "Welcome, Jane"
    ".budget-amount",       # live budget number
    ".cart-count",          # item count badge
]

TIMESTAMP_MASKS = [
    "time",
    "[x-text*='date']",
    "[x-text*='Date']",
    ".stat-value",          # numeric counters that change
]


# ── Helper functions ────────────────────────────────────────────────────

def seed_session(page):
    """Seed a standard user session into localStorage."""
    page.evaluate("""
        () => {
            localStorage.setItem('eds-session', JSON.stringify({
                session_id: 12345,
                user: {
                    user_id: 1,
                    user_name: 'jdoe',
                    first_name: 'Jane',
                    last_name: 'Doe',
                    email: 'jane.doe@eds.com'
                },
                district: {
                    district_id: 1,
                    district_code: 'TEST',
                    district_name: 'Test District'
                },
                session: {
                    session_id: 12345,
                    school_id: 1,
                    approval_level: 0
                }
            }));
        }
    """)


def seed_approver_session(page):
    """Seed an approver session (approval_level > 0) into localStorage."""
    page.evaluate("""
        () => {
            localStorage.setItem('eds-session', JSON.stringify({
                session_id: 99999,
                user: {
                    user_id: 10,
                    user_name: 'approver1',
                    first_name: 'Alice',
                    last_name: 'Approver',
                    email: 'alice.approver@eds.com'
                },
                district: {
                    district_id: 1,
                    district_code: 'TEST',
                    district_name: 'Test District'
                },
                session: {
                    session_id: 99999,
                    school_id: 1,
                    approval_level: 2
                }
            }));
        }
    """)


def seed_cart(page):
    """Seed a cart with representative items."""
    items = [
        {
            "id": "PROD-001",
            "name": "Pencils #2 Yellow",
            "quantity": 3,
            "unitPrice": 3.99,
            "extendedPrice": 11.97,
            "vendor": "School Supplies Inc",
            "vendorItemCode": "SSI-P12",
            "unitOfMeasure": "Pack",
        },
        {
            "id": "PROD-002",
            "name": "Notebook Spiral 100ct",
            "quantity": 5,
            "unitPrice": 2.49,
            "extendedPrice": 12.45,
            "vendor": "Paper Plus",
            "vendorItemCode": "PP-NB100",
            "unitOfMeasure": "Each",
        },
    ]
    page.evaluate(
        f"() => localStorage.setItem('eds-cart', JSON.stringify({json.dumps(items)}))"
    )


def goto_authed(page, url):
    """Navigate to a page with an existing session (seed-before-navigate)."""
    # Derive login URL from target URL (same origin)
    base = url.rsplit("/", 1)[0] if "/" in url else url
    login_url = base.rstrip("/") + "/login"
    page.goto(login_url)
    page.wait_for_load_state("domcontentloaded")
    seed_session(page)
    page.goto(url)
    page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
    page.wait_for_timeout(1500)


def goto_approver_authed(page, url):
    """Navigate to a page with an approver session."""
    base = url.rsplit("/", 1)[0] if "/" in url else url
    # Walk up to the root to find /login
    parts = url.split("/")
    # Find the scheme + host portion
    root = "/".join(parts[:3])  # http://localhost:8000
    login_url = root + "/login"
    page.goto(login_url)
    page.wait_for_load_state("domcontentloaded")
    seed_approver_session(page)
    page.goto(url)
    page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
    page.wait_for_timeout(1500)


# ── Test Classes ────────────────────────────────────────────────────────


class TestLoginPageVisual:
    """Visual regression for the login page."""

    def test_login_page(self, authed_page, make_url, snapshot_dir, update_snapshots, server_available):
        """Full login page with empty form."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        page.goto(make_url("login"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        # Clear any session so the login form is shown
        page.evaluate("() => localStorage.removeItem('eds-session')")
        page.wait_for_timeout(500)

        assert_screenshot_match(
            page,
            "login-page",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.05,
            wait_ms=1000,
        )

    def test_login_page_with_error(self, authed_page, make_url, snapshot_dir, update_snapshots, server_available):
        """Login page after an empty-submit validation error."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        page.goto(make_url("login"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.evaluate("() => localStorage.removeItem('eds-session')")
        page.wait_for_timeout(500)

        # Trigger validation by submitting empty form
        submit_btn = page.locator("button[type='submit']")
        submit_btn.click()
        page.wait_for_timeout(500)

        assert_screenshot_match(
            page,
            "login-page-error",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.05,
            wait_ms=500,
        )


class TestProductPageVisual:
    """Visual regression for the product browsing page."""

    def test_product_grid_view(self, authed_page, frontend_url, snapshot_dir, update_snapshots, server_available):
        """Product page in default grid layout."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url)

        assert_screenshot_match(
            page,
            "product-grid",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,
            mask_selectors=HEADER_MASKS,
            wait_ms=2000,
        )

    def test_product_list_view(self, authed_page, frontend_url, snapshot_dir, update_snapshots, server_available):
        """Product page toggled to list layout."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url)

        # Toggle to list view
        list_btn = page.locator("#list-view-btn")
        if list_btn.is_visible():
            list_btn.click()
            page.wait_for_timeout(500)

        assert_screenshot_match(
            page,
            "product-list",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,
            mask_selectors=HEADER_MASKS,
            wait_ms=1000,
        )

    def test_product_page_header(self, authed_page, frontend_url, snapshot_dir, update_snapshots, server_available):
        """Header section only — logo, nav, search, cart button."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url)

        assert_screenshot_match(
            page,
            "product-header",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.08,
            selector="header.header",
            mask_selectors=HEADER_MASKS,
            wait_ms=1000,
        )


class TestCartDrawerVisual:
    """Visual regression for the cart drawer."""

    def test_cart_drawer_with_items(self, authed_page, frontend_url, snapshot_dir, update_snapshots, server_available):
        """Cart drawer open with two seeded items."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url)
        seed_cart(page)
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Open cart
        cart_btn = page.locator(".cart-btn").last
        cart_btn.click()
        page.wait_for_timeout(500)

        assert_screenshot_match(
            page,
            "cart-drawer-items",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,
            mask_selectors=HEADER_MASKS,
            wait_ms=500,
        )

    def test_cart_drawer_empty(self, authed_page, frontend_url, snapshot_dir, update_snapshots, server_available):
        """Cart drawer open with no items (empty state)."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url)
        page.evaluate("() => localStorage.removeItem('eds-cart')")
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Open cart
        cart_btn = page.locator(".cart-btn").last
        cart_btn.click()
        page.wait_for_timeout(500)

        assert_screenshot_match(
            page,
            "cart-drawer-empty",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.08,
            mask_selectors=HEADER_MASKS,
            wait_ms=500,
        )


class TestCheckoutPageVisual:
    """Visual regression for the checkout page."""

    def test_checkout_with_items(self, authed_page, make_url, snapshot_dir, update_snapshots, server_available):
        """Checkout page showing cart items for review."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        # Seed session and cart on login page, then navigate to checkout
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")
        seed_session(page)
        seed_cart(page)
        page.goto(make_url("checkout"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(2000)

        assert_screenshot_match(
            page,
            "checkout-with-items",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,
            mask_selectors=HEADER_MASKS + TIMESTAMP_MASKS,
            wait_ms=1000,
        )


class TestApprovalDashboardVisual:
    """Visual regression for the approval dashboard."""

    def test_approval_dashboard(self, authed_page, make_url, snapshot_dir, update_snapshots, server_available):
        """Full approval dashboard with stats, filters, and list."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_approver_authed(page, make_url("admin/approvals"))

        assert_screenshot_match(
            page,
            "approval-dashboard",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,
            mask_selectors=HEADER_MASKS + TIMESTAMP_MASKS,
            wait_ms=1500,
        )

    def test_approval_stats_section(self, authed_page, make_url, snapshot_dir, update_snapshots, server_available):
        """Stats cards section only — Pending, Approved, etc."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_approver_authed(page, make_url("admin/approvals"))

        assert_screenshot_match(
            page,
            "approval-stats",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,
            selector=".approval-stats",
            mask_selectors=TIMESTAMP_MASKS,
            wait_ms=1000,
        )


class TestRequisitionListingVisual:
    """Visual regression for the requisitions listing page."""

    def test_requisition_listing(self, authed_page, make_url, snapshot_dir, update_snapshots, server_available):
        """Full requisition listing page with filters and status cards."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page

        # Intercept requisitions API to return empty list (consistent state)
        def handle_requisitions(route):
            route.fulfill(
                status=200,
                content_type="application/json",
                body=json.dumps({
                    "items": [],
                    "total": 0,
                    "total_pages": 0,
                    "page": 1,
                    "page_size": 20,
                    "status_counts": {},
                }),
            )
        page.route("**/api/requisitions*", handle_requisitions)

        # Seed on login, then navigate
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")
        seed_session(page)
        page.goto(make_url("requisitions"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(2000)

        assert_screenshot_match(
            page,
            "requisition-listing",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,
            mask_selectors=HEADER_MASKS + TIMESTAMP_MASKS,
            wait_ms=1000,
        )


class TestMobileVisual:
    """Visual regression for mobile viewport (375×667)."""

    def test_mobile_product_page(self, browser, base_url, snapshot_dir, update_snapshots, server_available):
        """Product page at mobile viewport size."""
        if not server_available:
            pytest.skip("Requires running server")

        context = browser.new_context(viewport={"width": 375, "height": 667})
        page = context.new_page()

        # Intercept session validation
        def handle_session(route):
            route.fulfill(
                status=200,
                content_type="application/json",
                body=json.dumps({"is_valid": True}),
            )
        page.route("**/api/auth/session/*", handle_session)

        # Seed and navigate
        login_url = base_url.rstrip("/") + "/login"
        page.goto(login_url)
        page.wait_for_load_state("domcontentloaded")
        seed_session(page)
        page.goto(base_url + "/")
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(2000)

        assert_screenshot_match(
            page,
            "mobile-product-page",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.10,
            mask_selectors=HEADER_MASKS,
            wait_ms=1000,
        )
        context.close()

    def test_mobile_login_page(self, browser, base_url, snapshot_dir, update_snapshots, server_available):
        """Login page at mobile viewport size."""
        if not server_available:
            pytest.skip("Requires running server")

        context = browser.new_context(viewport={"width": 375, "height": 667})
        page = context.new_page()

        page.goto(base_url.rstrip("/") + "/login")
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.evaluate("() => localStorage.removeItem('eds-session')")
        page.wait_for_timeout(500)

        assert_screenshot_match(
            page,
            "mobile-login-page",
            snapshot_dir,
            update=update_snapshots,
            threshold=0.05,
            wait_ms=1000,
        )
        context.close()
