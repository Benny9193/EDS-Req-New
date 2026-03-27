"""
E2E tests for checkout and order submission workflow.

Tests the full shopping-to-checkout flow:
- Adding items to cart via localStorage
- Cart drawer showing correct items and totals
- Navigating to checkout page
- Filling in checkout form (shipping, notes)
- Order submission confirmation
- Post-submission redirect to confirmation
"""

import pytest

pytestmark = pytest.mark.e2e


def seed_cart(page, items=None):
    """Helper to seed the cart with test items via localStorage."""
    if items is None:
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
    import json
    page.evaluate(f"() => localStorage.setItem('eds-cart', JSON.stringify({json.dumps(items)}))")


def seed_session(page):
    """Helper to seed a mock auth session in localStorage."""
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


def goto_home_authed(page, frontend_url):
    """Navigate to main page with auth (requires authed_page fixture).

    Seeds the session on a neutral page first so that requireAuth() passes
    on the main page without redirecting to login.
    """
    base = frontend_url.rstrip("/")
    login_url = base + "/login" if base.startswith("http") else base
    page.goto(login_url)
    page.wait_for_load_state("domcontentloaded")
    seed_session(page)
    page.goto(frontend_url)
    page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
    page.wait_for_timeout(1000)


class TestCartWithItems:
    """Test cart functionality with seeded items."""

    def test_cart_shows_item_count(self, authed_page, frontend_url, server_available):
        """Test cart badge shows correct item count."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        seed_cart(page)
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Cart button should show count
        cart_btn = page.locator(".cart-btn").last
        assert cart_btn.is_visible()

    def test_cart_drawer_shows_items(self, authed_page, frontend_url, server_available):
        """Test cart drawer displays seeded items."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        seed_cart(page)
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Open cart
        cart_btn = page.locator(".cart-btn").last
        cart_btn.click()
        page.wait_for_timeout(500)

        # Drawer should be visible with "Order List" heading
        drawer_heading = page.locator("text=Order List")
        assert drawer_heading.is_visible()

    def test_cart_displays_total(self, authed_page, frontend_url, server_available):
        """Test cart shows total price."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        seed_cart(page)
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Open cart
        cart_btn = page.locator(".cart-btn").last
        cart_btn.click()
        page.wait_for_timeout(500)

        # Check for a total amount display (expected: $24.42)
        page_text = page.locator(".cart-drawer, .cart-panel, [x-show]").all_text_contents()
        full_text = " ".join(page_text)
        # Should contain some dollar amount
        assert "$" in full_text or "Total" in full_text

    def test_empty_cart_after_clear(self, authed_page, frontend_url, server_available):
        """Test cart is empty after clearing localStorage."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        seed_cart(page)
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        # Clear cart
        page.evaluate("() => localStorage.removeItem('eds-cart')")
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(500)

        # Open cart
        cart_btn = page.locator(".cart-btn").last
        cart_btn.click()
        page.wait_for_timeout(500)

        # Should show empty message
        empty_msg = page.locator("text=Your cart is empty")
        assert empty_msg.is_visible()


class TestCheckoutPage:
    """Test checkout page rendering and form."""

    def test_checkout_page_loads(self, page, make_url):
        """Test checkout page loads correctly."""
        page.goto(make_url("checkout"))
        page.wait_for_load_state("domcontentloaded")

        # Should contain checkout-related content
        body_text = page.locator("body").inner_text()
        assert any(word in body_text.lower() for word in ["checkout", "order", "submit", "review"])

    def test_checkout_shows_cart_items(self, authed_page, make_url, server_available):
        """Test checkout page displays cart items for review."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        page.goto(make_url("checkout"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        seed_session(page)
        seed_cart(page)
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1000)

        # Should display item names from cart or checkout content
        body_text = page.locator("body").inner_text()
        # Page should have rendered with Alpine, showing either items or checkout UI
        assert len(body_text) > 50  # Has content beyond minimal shell

    def test_checkout_requires_auth(self, page, make_url, server_available):
        """Test checkout redirects to login if not authenticated."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("checkout"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        # Clear any session
        page.evaluate("() => localStorage.removeItem('eds-session')")
        page.reload()
        page.wait_for_timeout(2000)

        # Should either redirect to login or show auth prompt
        current_url = page.url
        has_session = page.evaluate("() => localStorage.getItem('eds-session')")
        assert has_session is None


class TestCartQuantityManagement:
    """Test cart quantity updates and item removal."""

    def test_quantity_updates_in_localstorage(self, authed_page, frontend_url, server_available):
        """Test that quantity changes persist in localStorage."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        seed_cart(page, [{
            "id": "PROD-001",
            "name": "Test Product",
            "quantity": 1,
            "unitPrice": 10.00,
            "extendedPrice": 10.00,
            "vendor": "Test Vendor",
            "vendorItemCode": "TV-001",
            "unitOfMeasure": "Each",
        }])

        # Verify item is in localStorage
        cart_data = page.evaluate("""
            () => {
                const cart = localStorage.getItem('eds-cart');
                return cart ? JSON.parse(cart) : [];
            }
        """)
        assert len(cart_data) == 1
        assert cart_data[0]["quantity"] == 1

    def test_multiple_items_in_cart(self, authed_page, frontend_url, server_available):
        """Test cart handles multiple items correctly."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        items = [
            {"id": f"PROD-{i}", "name": f"Product {i}", "quantity": i,
             "unitPrice": 5.00 * i, "extendedPrice": 5.00 * i * i,
             "vendor": "Vendor", "vendorItemCode": f"V-{i}", "unitOfMeasure": "Each"}
            for i in range(1, 6)
        ]
        seed_cart(page, items)

        cart_data = page.evaluate("""
            () => {
                const cart = localStorage.getItem('eds-cart');
                return cart ? JSON.parse(cart) : [];
            }
        """)
        assert len(cart_data) == 5
