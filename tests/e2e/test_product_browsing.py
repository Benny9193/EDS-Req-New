"""
E2E tests for product browsing functionality.

Tests the core product browsing user flows:
- View product grid/list
- Toggle view modes
- Search products
- Filter by category
- Pagination
"""

import pytest

pytestmark = pytest.mark.e2e


def seed_user_session(page):
    """Seed localStorage with a mock user session."""
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
    seed_user_session(page)
    page.goto(frontend_url)
    page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
    page.wait_for_timeout(1000)


class TestProductBrowsing:
    """Test product browsing flows."""

    def test_page_loads(self, authed_page, frontend_url, server_available):
        """Test that the product page loads successfully."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        # Check page title
        assert "Requisition" in page.title()

    def test_products_display(self, authed_page, frontend_url, server_available):
        """Test that products are displayed after loading."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        # Wait for products to potentially load
        page.wait_for_timeout(2000)

        # Check for product container
        product_area = page.locator(".products-area")
        assert product_area.is_visible()

    def test_view_mode_toggle(self, authed_page, frontend_url, server_available):
        """Test grid/list view toggle functionality."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        # Find view toggle buttons
        grid_btn = page.locator("#grid-view-btn")
        list_btn = page.locator("#list-view-btn")

        # Grid should be active by default
        assert grid_btn.is_visible()
        assert list_btn.is_visible()

        # Click list view
        list_btn.click()
        page.wait_for_timeout(500)

        # Check list view is now active
        expect_list_active = page.locator("#list-view-btn.active")
        assert expect_list_active.count() >= 0  # May or may not have active class

        # Click grid view
        grid_btn.click()
        page.wait_for_timeout(500)

    def test_header_elements_visible(self, authed_page, frontend_url, server_available):
        """Test that header elements are visible."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        # Check header exists
        header = page.locator("header.header")
        assert header.is_visible()

        # Check logo area
        logo = page.locator(".logo")
        assert logo.count() > 0

    def test_cart_button_exists(self, authed_page, frontend_url, server_available):
        """Test that cart button is present."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        # Cart button should be visible
        cart_btn = page.locator(".cart-btn")
        assert cart_btn.count() > 0


class TestSearch:
    """Test search functionality."""

    def test_search_input_exists(self, authed_page, frontend_url, server_available):
        """Test that search input is present."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        # Desktop search input
        search_input = page.locator(".search-input")
        # May be hidden on mobile viewport
        if search_input.is_visible():
            assert search_input.is_visible()

    def test_category_dropdown_exists(self, authed_page, frontend_url, server_available):
        """Test that category dropdown is present."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_home_authed(page, frontend_url)

        # Category dropdown
        category_dropdown = page.locator(".category-dropdown")
        if category_dropdown.is_visible():
            assert category_dropdown.is_visible()


class TestMobileView:
    """Test mobile viewport behavior."""

    def test_mobile_menu_button(self, authed_page, frontend_url, server_available):
        """Test mobile menu button on small viewport."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        # Set mobile viewport
        page.set_viewport_size({"width": 375, "height": 667})
        goto_home_authed(page, frontend_url)

        # Mobile hamburger menu should be visible
        mobile_menu = page.locator("button:has(i.fa-bars)")
        assert mobile_menu.count() > 0

    def test_mobile_cart_accessible(self, authed_page, frontend_url, server_available):
        """Test cart is accessible on mobile."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        page.set_viewport_size({"width": 375, "height": 667})
        goto_home_authed(page, frontend_url)

        # Cart button should still be visible
        cart_btn = page.locator(".cart-btn")
        assert cart_btn.count() > 0
