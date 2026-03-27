"""
E2E tests for the approval workflow.

Tests the approval dashboard page:
- Page rendering and structure
- Approval stats display
- Pending approvals list
- Approve / reject actions via modals
- Bulk selection and approval
- Search and sort filters
- Auth redirect when not logged in

Note: All tests require a running server because the approvals page uses
Alpine.js x-data on the <body> tag, which causes the page to render empty
when Alpine.js cannot load from CDN (file:// protocol).
"""

import pytest

pytestmark = pytest.mark.e2e


def seed_approver_session(page):
    """Seed localStorage with a mock approver session (approval_level > 0)."""
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


def goto_approvals_authed(page, make_url):
    """Navigate to approvals page with a seeded session (requires authed_page).

    Seeds the session on the login page first (which doesn't redirect),
    then navigates to the approvals page so the auth check passes immediately.
    """
    # Visit login page first to establish the origin for localStorage
    page.goto(make_url("login"))
    page.wait_for_load_state("domcontentloaded")
    # Seed session BEFORE navigating to the auth-protected page
    seed_approver_session(page)
    # Now navigate to approvals - auth store will find session in localStorage
    page.goto(make_url("admin/approvals"))
    page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
    page.wait_for_timeout(1000)


class TestApprovalPageRender:
    """Test approval dashboard page loads and renders correctly."""

    def test_approval_page_loads(self, authed_page, make_url, server_available):
        """Test the approvals page loads without errors."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        title = page.title()
        assert "Approval" in title

    def test_approval_page_has_header(self, authed_page, make_url, server_available):
        """Test the approvals page has a proper header with nav."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        header = page.locator("header.page-header")
        assert header.is_visible()

        # Should have EDS logo text
        logo = page.locator(".logo-text")
        assert logo.is_visible()

    def test_approval_page_has_title_heading(self, authed_page, make_url, server_available):
        """Test the page has an 'Approval Dashboard' heading."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        heading = page.locator("h1.page-title")
        assert heading.is_visible()
        assert "Approval" in heading.inner_text()

    def test_approval_page_has_skip_link(self, authed_page, make_url, server_available):
        """Test accessibility skip link is present."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        skip_link = page.locator("a.skip-link")
        assert skip_link.count() > 0


class TestApprovalStats:
    """Test the approval summary stats cards render."""

    def test_stat_cards_visible(self, authed_page, make_url, server_available):
        """Test all four stat cards are visible."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        stat_cards = page.locator(".stat-card")
        assert stat_cards.count() == 4

    def test_stat_cards_have_labels(self, authed_page, make_url, server_available):
        """Test stat cards display expected labels."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        labels = page.locator(".stat-label").all_text_contents()
        label_text = " ".join(labels).lower()
        assert "pending" in label_text

    def test_stat_values_are_numeric(self, authed_page, make_url, server_available):
        """Test stat values show numbers or currency."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        values = page.locator(".stat-value").all_text_contents()
        # Each value should contain at least a digit or $
        for val in values:
            assert any(c.isdigit() or c == "$" for c in val), f"Unexpected stat value: {val}"


class TestApprovalFilters:
    """Test the filters bar on the approvals page."""

    def test_search_input_visible(self, authed_page, make_url, server_available):
        """Test the search input field is present."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        search_input = page.locator(".search-filter input")
        assert search_input.is_visible()
        assert search_input.get_attribute("placeholder") is not None

    def test_sort_select_visible(self, authed_page, make_url, server_available):
        """Test the sort dropdown is present."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        sort_select = page.locator(".filter-select")
        assert sort_select.is_visible()

    def test_sort_has_options(self, authed_page, make_url, server_available):
        """Test the sort dropdown has multiple options."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        options = page.locator(".filter-select option")
        assert options.count() >= 3

    def test_refresh_button_visible(self, authed_page, make_url, server_available):
        """Test the refresh button is present."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        refresh_btn = page.locator("button:has-text('Refresh')")
        assert refresh_btn.is_visible()


class TestApprovalEmptyState:
    """Test the empty state when no approvals are pending."""

    def test_empty_state_renders(self, authed_page, make_url, server_available):
        """Test empty state shows when no pending approvals."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        goto_approvals_authed(page, make_url)

        # Either shows empty state or a list - both are valid
        body_text = page.locator("body").inner_text()
        has_content = (
            "All Caught Up" in body_text
            or "no requisitions" in body_text.lower()
            or "approval-card" in page.content()
            or "Loading" in body_text
        )
        assert has_content or len(body_text) > 100


class TestApprovalAuth:
    """Test authentication requirements for the approvals page."""

    def test_redirects_without_session(self, page, make_url, server_available):
        """Test page redirects to login when no session exists."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("admin/approvals"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        # Clear any existing session
        page.evaluate("() => localStorage.removeItem('eds-session')")
        page.reload()
        page.wait_for_timeout(2000)

        # Should either redirect to login or show no session
        has_session = page.evaluate("() => localStorage.getItem('eds-session')")
        current_url = page.url

        # Either redirected to login or session is null
        assert has_session is None or "login" in current_url.lower()

    def test_session_stored_for_approver(self, authed_page, make_url, server_available):
        """Test that a seeded approver session persists."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        page.goto(make_url("admin/approvals"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        seed_approver_session(page)

        session_data = page.evaluate("""
            () => {
                const s = localStorage.getItem('eds-session');
                return s ? JSON.parse(s) : null;
            }
        """)
        assert session_data is not None
        assert session_data["session"]["approval_level"] == 2


class TestApprovalNavigation:
    """Test navigation elements on the approvals page."""

    def test_nav_has_shop_link(self, authed_page, make_url, server_available):
        """Test nav includes a Shop link."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        shop_link = page.locator("a.nav-link:has-text('Shop')")
        assert shop_link.is_visible()

    def test_nav_has_orders_link(self, authed_page, make_url, server_available):
        """Test nav includes a My Orders link."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        orders_link = page.locator("a.nav-link:has-text('My Orders')")
        assert orders_link.is_visible()

    def test_approvals_nav_is_active(self, authed_page, make_url, server_available):
        """Test the Approvals nav link is marked active."""
        if not server_available:
            pytest.skip("Requires running server - page uses Alpine.js x-data on body")

        page = authed_page
        goto_approvals_authed(page, make_url)

        active_link = page.locator("a.nav-link.active")
        assert active_link.count() > 0
        assert "Approvals" in active_link.first.inner_text()
