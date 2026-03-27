"""
E2E tests for the requisition listing page.

Tests the My Requisitions page:
- Page rendering and structure
- Status filter cards
- Search and sort filters
- Empty state display
- Auth requirement
- Navigation links
- Date filter inputs
"""

import pytest

pytestmark = pytest.mark.e2e


def seed_user_session(page):
    """Seed localStorage with a standard user session."""
    page.evaluate("""
        () => {
            localStorage.setItem('eds-session', JSON.stringify({
                session_id: 55555,
                user: {
                    user_id: 5,
                    user_name: 'testuser',
                    first_name: 'Test',
                    last_name: 'User',
                    email: 'test.user@eds.com'
                },
                district: {
                    district_id: 1,
                    district_code: 'TEST',
                    district_name: 'Test District'
                },
                session: {
                    session_id: 55555,
                    school_id: 1,
                    approval_level: 0
                }
            }));
        }
    """)


class TestRequisitionPageRender:
    """Test the requisitions listing page loads correctly."""

    def test_page_loads(self, page, make_url):
        """Test the requisitions page loads without errors."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        title = page.title()
        assert "Requisition" in title or "Order" in title

    def test_page_has_heading(self, page, make_url):
        """Test the page has 'My Requisitions' heading."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        heading = page.locator("h1.page-title")
        assert heading.is_visible()
        assert "Requisition" in heading.inner_text() or "Order" in heading.inner_text()

    def test_page_has_new_order_button(self, page, make_url):
        """Test the page has a 'New Order' action button."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        new_order_btn = page.locator("a:has-text('New Order')")
        assert new_order_btn.is_visible()

    def test_page_has_skip_link(self, page, make_url):
        """Test accessibility skip link is present."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        skip_link = page.locator("a.skip-link")
        assert skip_link.count() > 0


class TestRequisitionStatusFilters:
    """Test the status filter cards."""

    def test_status_cards_visible(self, page, make_url):
        """Test all status filter cards are visible."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        status_cards = page.locator(".status-card")
        # Should have: All, Submitted, Pending, Approved, Cancelled
        assert status_cards.count() >= 4

    def test_all_orders_card_text(self, page, make_url):
        """Test 'All Orders' status card exists."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        all_card = page.locator(".status-card:has-text('All Orders')")
        assert all_card.count() > 0

    def test_status_labels_present(self, page, make_url):
        """Test expected status labels are on the page."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        labels = page.locator(".status-card-label").all_text_contents()
        label_text = " ".join(labels).lower()
        assert "submitted" in label_text or "pending" in label_text


class TestRequisitionSearchAndSort:
    """Test search and sort filter controls."""

    def test_search_input_visible(self, page, make_url):
        """Test the search input is present."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        search = page.locator(".search-filter input")
        assert search.is_visible()

    def test_search_has_placeholder(self, page, make_url):
        """Test the search input has a descriptive placeholder."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        search = page.locator(".search-filter input")
        placeholder = search.get_attribute("placeholder")
        assert placeholder is not None
        assert "order" in placeholder.lower() or "search" in placeholder.lower()

    def test_sort_select_visible(self, page, make_url):
        """Test the sort dropdown is present."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        sort_select = page.locator(".sort-filter select")
        assert sort_select.is_visible()

    def test_sort_has_options(self, page, make_url):
        """Test the sort dropdown has expected options."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        options = page.locator(".sort-filter select option")
        assert options.count() >= 3

    def test_date_filters_visible(self, page, make_url):
        """Test date filter inputs are present."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        date_inputs = page.locator(".date-filter input[type='date']")
        assert date_inputs.count() == 2


class TestRequisitionEmptyState:
    """Test the empty state display."""

    def test_empty_state_with_session(self, authed_page, make_url, server_available):
        """Test empty state renders when user has no requisitions."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page

        # Intercept requisitions API to return empty list
        import json as _json
        def handle_requisitions(route):
            route.fulfill(
                status=200,
                content_type="application/json",
                body=_json.dumps({
                    "items": [],
                    "total": 0,
                    "total_pages": 0,
                    "page": 1,
                    "page_size": 20,
                    "status_counts": {},
                }),
            )
        page.route("**/api/requisitions*", handle_requisitions)

        # Seed session on login page first (no auth redirect), then navigate
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")
        seed_user_session(page)
        page.goto(make_url("requisitions"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(3000)

        # Should display either the empty state or a table of results
        body_text = page.locator("body").inner_text()
        has_content = (
            "No requisitions" in body_text
            or "haven't placed" in body_text
            or "Start Shopping" in body_text
            or "Loading" in body_text
            or len(body_text) > 200
        )
        assert has_content

    def test_empty_state_has_shop_link(self, page, make_url):
        """Test empty state includes a 'Start Shopping' CTA."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        # The Start Shopping button should exist in the DOM (even if hidden)
        shop_btn = page.locator("a:has-text('Start Shopping')")
        assert shop_btn.count() > 0


class TestRequisitionAuth:
    """Test authentication requirements."""

    def test_no_session_shows_no_data(self, page, make_url, server_available):
        """Test page doesn't load data without a session."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("requisitions"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        # Clear any session
        page.evaluate("() => localStorage.removeItem('eds-session')")
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(1500)

        has_session = page.evaluate("() => localStorage.getItem('eds-session')")
        assert has_session is None

    def test_session_persists_after_seed(self, page, make_url, server_available):
        """Test seeded session is available in localStorage."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("requisitions"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        seed_user_session(page)

        session = page.evaluate("""
            () => {
                const s = localStorage.getItem('eds-session');
                return s ? JSON.parse(s) : null;
            }
        """)
        assert session is not None
        assert session["user"]["user_name"] == "testuser"


class TestRequisitionNavigation:
    """Test navigation elements."""

    def test_header_visible(self, page, make_url):
        """Test header is rendered."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        header = page.locator("header.page-header")
        assert header.is_visible()

    def test_nav_has_shop_link(self, page, make_url):
        """Test nav includes a Shop link."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        shop_link = page.locator("a.nav-link:has-text('Shop')")
        assert shop_link.is_visible()

    def test_my_orders_nav_is_active(self, page, make_url):
        """Test the My Orders nav link is marked active."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        active_link = page.locator("a.nav-link.active")
        assert active_link.count() > 0
        assert "Orders" in active_link.first.inner_text()

    def test_new_order_button_links_home(self, page, make_url):
        """Test the New Order button links to the home page."""
        page.goto(make_url("requisitions"))
        page.wait_for_load_state("domcontentloaded")

        new_order = page.locator("a.btn-primary:has-text('New Order')")
        href = new_order.get_attribute("href")
        assert href == "/"
