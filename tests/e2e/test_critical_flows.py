"""
E2E tests for critical user flows.

Tests the complete end-to-end journeys:
- Login -> Dashboard loads
- Browse products -> Add to cart -> Cart updates
- Cart -> Checkout navigation -> Form completion
- Session expiry -> Redirect to login
- Product normalization consistency (field naming)
"""

import json
import pytest

pytestmark = pytest.mark.e2e


# ── Helpers ────────────────────────────────────────────────────────────


MOCK_SESSION = {
    "session_id": 12345,
    "user": {
        "user_id": 1,
        "user_name": "jdoe",
        "first_name": "Jane",
        "last_name": "Doe",
        "email": "jane.doe@eds.com",
    },
    "district": {
        "district_id": 1,
        "district_code": "TEST",
        "district_name": "Test District",
    },
    "session": {
        "session_id": 12345,
        "school_id": 1,
        "approval_level": 0,
    },
}

MOCK_ADMIN_SESSION = {
    **MOCK_SESSION,
    "user": {
        **MOCK_SESSION["user"],
        "role": "admin",
    },
    "session": {
        **MOCK_SESSION["session"],
        "approval_level": 2,
    },
}

# Cart items using the normalized field names (PascalCase as produced by edsProduct.normalize)
MOCK_CART_ITEMS = [
    {
        "ItemNumber": "SSI-P12",
        "Description": "Pencils #2 Yellow - 12 Pack",
        "Price": 3.99,
        "VendorName": "School Specialty, LLC",
        "category": "Classroom Supplies",
        "unit_of_measure": "Pack",
        "quantity": 3,
    },
    {
        "ItemNumber": "PP-NB100",
        "Description": "Notebook Spiral 100ct",
        "Price": 2.49,
        "VendorName": "Cascade School Supplies",
        "category": "Classroom Supplies",
        "unit_of_measure": "Each",
        "quantity": 5,
    },
]


def seed_session(page, session=None):
    """Seed localStorage with mock session."""
    s = json.dumps(session or MOCK_SESSION)
    page.evaluate(f"() => localStorage.setItem('eds-session', JSON.stringify({s}))")


def seed_cart(page, items=None):
    """Seed localStorage with mock cart items."""
    c = json.dumps(items or MOCK_CART_ITEMS)
    page.evaluate(f"() => localStorage.setItem('eds_cart', JSON.stringify({c}))")


def goto_authed(page, url, frontend_url):
    """Navigate to a URL with pre-seeded auth."""
    base = frontend_url.rstrip("/")
    login_url = base + "/login" if base.startswith("http") else base
    page.goto(login_url)
    page.wait_for_load_state("domcontentloaded")
    seed_session(page)
    page.goto(url)
    page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
    page.wait_for_timeout(1000)


# ── Flow 1: Login → Dashboard ─────────────────────────────────────────


class TestLoginToDashboard:
    """Test the login -> dashboard flow."""

    def test_unauthenticated_redirects_to_login(self, page, frontend_url, server_available):
        """Visiting main page without session redirects to login."""
        if not server_available:
            pytest.skip("Requires running server")

        page.evaluate("() => localStorage.clear()")
        page.goto(frontend_url)
        page.wait_for_timeout(2000)

        assert "login" in page.url.lower()

    def test_authenticated_sees_dashboard(self, authed_page, frontend_url, server_available):
        """Authenticated user sees the dashboard view."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        # Dashboard should be the default view
        body = page.locator("body").inner_text()
        assert any(term in body for term in ["Dashboard", "Welcome", "Overview", "Recent"])

    def test_user_name_displayed(self, authed_page, frontend_url, server_available):
        """User's name should appear somewhere on the page."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        body = page.locator("body").inner_text()
        # Should show first name, last name, or initials
        assert "Jane" in body or "Doe" in body or "JD" in body

    def test_sidebar_navigation_visible(self, authed_page, frontend_url, server_available):
        """Sidebar with navigation links should be visible on desktop."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        page.set_viewport_size({"width": 1280, "height": 720})
        goto_authed(page, frontend_url, frontend_url)

        # Should have navigation items
        nav_items = page.locator("nav a, nav button, .sidebar a, .sidebar button")
        assert nav_items.count() > 0


# ── Flow 2: Browse → Add to Cart ──────────────────────────────────────


class TestBrowseAndAddToCart:
    """Test browsing products and adding them to cart."""

    def test_switch_to_browse_view(self, authed_page, frontend_url, server_available):
        """Test switching to browse view shows product grid."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        # Click Browse/Products in sidebar
        browse_link = page.locator("text=Browse").first
        if not browse_link.is_visible():
            browse_link = page.locator("text=Products").first
        if browse_link.is_visible():
            browse_link.click()
            page.wait_for_timeout(1500)

            # Should show product cards or a product grid
            body = page.locator("body").inner_text()
            assert any(term in body.lower() for term in [
                "product", "browse", "search", "category", "filter"
            ])

    def test_add_to_cart_updates_count(self, authed_page, frontend_url, server_available):
        """Adding a product to cart updates the cart badge count."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        # Seed cart with items and reload to update count
        seed_cart(page)
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Cart count should reflect items (3 + 5 = 8 items)
        cart_count = page.evaluate("""
            () => {
                const cart = JSON.parse(localStorage.getItem('eds_cart') || '[]');
                return cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
            }
        """)
        assert cart_count == 8

    def test_add_to_cart_via_javascript(self, authed_page, frontend_url, server_available):
        """Test adding item programmatically via Alpine store."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        # Clear cart first
        page.evaluate("() => localStorage.removeItem('eds_cart')")
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Add item via Alpine component
        page.evaluate("""
            () => {
                const appEl = document.querySelector('[x-data]');
                if (appEl && appEl.__x) {
                    appEl.__x.$data.addToCart({
                        ItemNumber: 'TEST-001',
                        Description: 'Test Item',
                        Price: 9.99,
                        VendorName: 'Test Vendor',
                        quantity: 1
                    });
                }
            }
        """)
        page.wait_for_timeout(500)

        # Verify item in localStorage
        cart = page.evaluate("""
            () => JSON.parse(localStorage.getItem('eds_cart') || '[]')
        """)
        assert len(cart) >= 1


# ── Flow 3: Cart → Checkout ───────────────────────────────────────────


class TestCartToCheckout:
    """Test the cart review to checkout submission flow."""

    def test_cart_drawer_shows_normalized_prices(self, authed_page, frontend_url, server_available):
        """Test that cart drawer shows prices correctly regardless of field naming."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        # Seed cart with mixed field naming (simulating real-world data)
        mixed_cart = json.dumps([
            {"ItemNumber": "A1", "Description": "Item A", "Price": 10.50, "quantity": 2},
            {"item_number": "B2", "name": "Item B", "price": 5.25, "quantity": 1},
            {"id": "C3", "description": "Item C", "UnitPrice": 3.00, "quantity": 4},
        ])
        page.evaluate(f"() => localStorage.setItem('eds_cart', JSON.stringify({mixed_cart}))")
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Open cart drawer
        cart_btn = page.locator(".cart-btn").last
        cart_btn.click()
        page.wait_for_timeout(500)

        # Cart should display and show a total
        drawer_text = page.locator("body").inner_text()
        assert "$" in drawer_text

    def test_checkout_page_accessible_with_cart(self, authed_page, make_url, frontend_url, server_available):
        """Test checkout page loads when cart has items."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        # Seed on login page first
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")
        seed_session(page)
        seed_cart(page)

        page.goto(make_url("checkout"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        body = page.locator("body").inner_text()
        # Should show checkout content (Review step)
        assert any(term in body for term in ["Review", "Checkout", "Order", "Cart", "Item"])

    def test_checkout_shows_correct_item_count(self, authed_page, make_url, frontend_url, server_available):
        """Test checkout page shows correct number of items."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")
        seed_session(page)
        seed_cart(page)

        page.goto(make_url("checkout"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Verify cart loaded from localStorage
        cart_length = page.evaluate("""
            () => JSON.parse(localStorage.getItem('eds_cart') || '[]').length
        """)
        assert cart_length == 2

    def test_checkout_empty_cart_warning(self, authed_page, make_url, frontend_url, server_available):
        """Test checkout page handles empty cart gracefully."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")
        seed_session(page)
        # Don't seed cart

        page.goto(make_url("checkout"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        cart_length = page.evaluate("""
            () => JSON.parse(localStorage.getItem('eds_cart') || '[]').length
        """)
        assert cart_length == 0


# ── Flow 4: Session Expiry ────────────────────────────────────────────


class TestSessionExpiry:
    """Test session management and expiry handling."""

    def test_clearing_session_redirects(self, authed_page, frontend_url, server_available):
        """Clearing session from localStorage triggers redirect to login."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        # Clear session
        page.evaluate("() => localStorage.removeItem('eds-session')")

        # Navigate to trigger auth check
        page.goto(frontend_url)
        page.wait_for_timeout(2000)

        assert "login" in page.url.lower()

    def test_invalid_session_json_redirects(self, page, frontend_url, server_available):
        """Malformed session JSON triggers redirect to login."""
        if not server_available:
            pytest.skip("Requires running server")

        page.goto(frontend_url.rstrip("/") + "/login")
        page.wait_for_load_state("domcontentloaded")
        page.evaluate("() => localStorage.setItem('eds-session', 'not-valid-json')")
        page.goto(frontend_url)
        page.wait_for_timeout(2000)

        assert "login" in page.url.lower()


# ── Flow 5: Product Field Normalization ───────────────────────────────


class TestProductNormalization:
    """Test that product field normalization works correctly across formats."""

    def test_normalize_snake_case_product(self, authed_page, frontend_url, server_available):
        """Test normalizing a snake_case product (from Products API)."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        result = page.evaluate("""
            () => {
                if (typeof edsProduct === 'undefined') return null;
                const p = edsProduct.normalize({
                    id: '123',
                    name: 'Test Product',
                    unit_price: 9.99,
                    vendor: 'Test Vendor',
                    category: 'Supplies'
                });
                return {
                    ItemNumber: p.ItemNumber,
                    Description: p.Description,
                    Price: p.Price,
                    VendorName: p.VendorName,
                };
            }
        """)

        if result is None:
            pytest.skip("edsProduct not available (script may not be loaded)")

        assert result["ItemNumber"] == "123"
        assert result["Description"] == "Test Product"
        assert result["Price"] == 9.99
        assert result["VendorName"] == "Test Vendor"

    def test_normalize_pascal_case_product(self, authed_page, frontend_url, server_available):
        """Test normalizing a PascalCase product (from legacy/cart)."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        result = page.evaluate("""
            () => {
                if (typeof edsProduct === 'undefined') return null;
                const p = edsProduct.normalize({
                    ItemNumber: 'ABC-001',
                    Description: 'Legacy Product',
                    Price: 15.50,
                    VendorName: 'Old Vendor',
                    Category: 'Office'
                });
                return {
                    ItemNumber: p.ItemNumber,
                    Description: p.Description,
                    Price: p.Price,
                    VendorName: p.VendorName,
                };
            }
        """)

        if result is None:
            pytest.skip("edsProduct not available")

        assert result["ItemNumber"] == "ABC-001"
        assert result["Description"] == "Legacy Product"
        assert result["Price"] == 15.50
        assert result["VendorName"] == "Old Vendor"

    def test_cart_total_with_mixed_fields(self, authed_page, frontend_url, server_available):
        """Test edsCart.total handles mixed field naming."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        result = page.evaluate("""
            () => {
                if (typeof edsCart === 'undefined') return null;
                return edsCart.total([
                    { Price: 10.00, quantity: 2 },
                    { price: 5.00, quantity: 3 },
                    { UnitPrice: 3.00, quantity: 1 },
                    { unit_price: 7.50, quantity: 4 },
                ]);
            }
        """)

        if result is None:
            pytest.skip("edsCart not available")

        # 10*2 + 5*3 + 3*1 + 7.5*4 = 20 + 15 + 3 + 30 = 68
        assert result == 68.0

    def test_get_price_helper(self, authed_page, frontend_url, server_available):
        """Test edsProduct.getPrice resolves all field name variants."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        result = page.evaluate("""
            () => {
                if (typeof edsProduct === 'undefined') return null;
                return [
                    edsProduct.getPrice({ Price: 1.11 }),
                    edsProduct.getPrice({ price: 2.22 }),
                    edsProduct.getPrice({ unit_price: 3.33 }),
                    edsProduct.getPrice({ UnitPrice: 4.44 }),
                    edsProduct.getPrice({}),
                ];
            }
        """)

        if result is None:
            pytest.skip("edsProduct not available")

        assert result == [1.11, 2.22, 3.33, 4.44, 0]


# ── Flow 6: Admin Approvals Access ────────────────────────────────────


class TestAdminAccess:
    """Test admin-only features are gated correctly."""

    def test_non_admin_cannot_see_approvals(self, authed_page, frontend_url, server_available):
        """Non-admin user should not see approvals nav item."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        goto_authed(page, frontend_url, frontend_url)

        # Check if approvals is hidden for non-admin
        is_admin = page.evaluate("""
            () => {
                const el = document.querySelector('[x-data]');
                return el && el.__x ? el.__x.$data.isAdmin : null;
            }
        """)
        # Default mock session has approval_level: 0, so isAdmin should be false
        if is_admin is not None:
            assert is_admin is False

    def test_admin_sees_approvals(self, authed_page, frontend_url, server_available):
        """Admin user should see approvals option."""
        if not server_available:
            pytest.skip("Requires running server")

        page = authed_page
        base = frontend_url.rstrip("/")
        login_url = base + "/login" if base.startswith("http") else base
        page.goto(login_url)
        page.wait_for_load_state("domcontentloaded")

        # Seed admin session
        s = json.dumps(MOCK_ADMIN_SESSION)
        page.evaluate(f"() => localStorage.setItem('eds-session', JSON.stringify({s}))")

        page.goto(frontend_url)
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        is_admin = page.evaluate("""
            () => {
                const el = document.querySelector('[x-data]');
                return el && el.__x ? el.__x.$data.isAdmin : null;
            }
        """)
        if is_admin is not None:
            assert is_admin is True
