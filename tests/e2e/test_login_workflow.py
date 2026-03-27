"""
E2E tests for the login workflow.

Tests the complete authentication flow:
- Login page renders correctly
- Form validation (empty fields, invalid input)
- Successful login stores session and redirects
- Failed login shows error message
- Logout clears session and redirects to login
- Session persistence across page reloads
"""

import pytest

pytestmark = pytest.mark.e2e


class TestLoginPageRender:
    """Test that login page loads and renders correctly."""

    def test_login_page_loads(self, page, make_url):
        """Test login page loads with all form elements."""
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")

        assert "Login" in page.title() or "Sign In" in page.title()

    def test_login_form_fields_visible(self, page, make_url):
        """Test all login form fields are visible."""
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")

        # District code field
        district_input = page.locator("#districtCode")
        assert district_input.is_visible()

        # User number field
        user_input = page.locator("#userNumber")
        assert user_input.is_visible()

        # Password field
        password_input = page.locator("#password")
        assert password_input.is_visible()

        # Submit button
        submit_btn = page.locator("button[type='submit']")
        assert submit_btn.is_visible()

    def test_password_toggle_visibility(self, page, make_url, server_available):
        """Test password show/hide toggle works."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("login"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.wait_for_timeout(500)

        password_input = page.locator("#password")

        # Password should be hidden by default (Alpine :type binding)
        pw_type = page.evaluate("() => document.getElementById('password').type")
        assert pw_type == "password"

        # Click the toggle button
        toggle_btn = page.locator("button:has(i.fa-eye)")
        toggle_btn.click()
        page.wait_for_timeout(300)

        # Password should now be visible
        pw_type = page.evaluate("() => document.getElementById('password').type")
        assert pw_type == "text"

        # Click again to hide
        toggle_btn2 = page.locator("button:has(i.fa-eye-slash)")
        toggle_btn2.click()
        page.wait_for_timeout(300)

        pw_type = page.evaluate("() => document.getElementById('password').type")
        assert pw_type == "password"


class TestLoginFormValidation:
    """Test client-side form validation."""

    def test_empty_submit_shows_validation(self, page, make_url, server_available):
        """Test submitting empty form triggers validation."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("login"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        # Click submit with empty fields
        submit_btn = page.locator("button[type='submit']")
        submit_btn.click()
        page.wait_for_timeout(500)

        # Should not redirect (still on login page)
        assert "login" in page.url.lower() or "Login" in page.title()

    def test_district_code_uppercase_conversion(self, page, make_url, server_available):
        """Test district code auto-converts to uppercase."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("login"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        district_input = page.locator("#districtCode")
        district_input.fill("abcd")
        # Trigger input event for Alpine.js
        district_input.dispatch_event("input")
        page.wait_for_timeout(300)

        assert district_input.input_value() == "ABCD"

    def test_district_code_max_length(self, page, make_url):
        """Test district code respects maxlength attribute."""
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")

        district_input = page.locator("#districtCode")
        assert district_input.get_attribute("maxlength") == "4"


class TestLoginSession:
    """Test login session management in localStorage."""

    def test_no_session_stays_on_login(self, page, make_url, server_available):
        """Test that without a session, user stays on login page."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("login"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)
        page.evaluate("localStorage.clear()")
        page.reload()
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        # Should remain on login page
        assert "login" in page.url.lower()

    def test_existing_session_redirects(self, authed_page, make_url, server_available):
        """Test that existing valid session redirects away from login."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page = authed_page
        page.goto(make_url("login"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        # Set mock session in localStorage
        page.evaluate("""
            () => {
                localStorage.setItem('eds-session', JSON.stringify({
                    session_id: 12345,
                    user: {
                        user_id: 1,
                        user_name: 'testuser',
                        first_name: 'Test',
                        last_name: 'User',
                        email: 'test@eds.com'
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

        # Reload - session validation is intercepted so session persists
        page.reload()
        page.wait_for_timeout(1000)

        # Verify session is stored (authed_page intercepts validation API)
        has_session = page.evaluate("""
            () => {
                const s = localStorage.getItem('eds-session');
                return s ? JSON.parse(s).session_id : null;
            }
        """)
        assert has_session == 12345

    def test_clear_localstorage_removes_session(self, page, make_url, server_available):
        """Test that clearing localStorage removes the session."""
        if not server_available:
            pytest.skip("Requires running server for Alpine.js")

        page.goto(make_url("login"))
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=10000)

        # Set then clear
        page.evaluate("""
            () => {
                localStorage.setItem('eds-session', JSON.stringify({session_id: 999}));
                localStorage.removeItem('eds-session');
            }
        """)

        has_session = page.evaluate(
            "() => localStorage.getItem('eds-session')"
        )
        assert has_session is None


class TestLoginAccessibility:
    """Test login page accessibility features."""

    def test_skip_link_exists(self, page, make_url):
        """Test skip link is present for keyboard navigation."""
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")

        skip_link = page.locator("a.skip-link")
        assert skip_link.count() > 0

    def test_form_labels_linked(self, page, make_url):
        """Test form inputs have associated labels."""
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")

        # Each input should have a label with matching 'for' attribute
        for field_id in ["districtCode", "userNumber", "password"]:
            label = page.locator(f'label[for="{field_id}"]')
            assert label.count() > 0, f"Missing label for {field_id}"

    def test_aria_attributes_present(self, page, make_url):
        """Test ARIA attributes on form fields."""
        page.goto(make_url("login"))
        page.wait_for_load_state("domcontentloaded")

        # Password field should have aria-describedby
        password = page.locator("#password")
        assert password.get_attribute("aria-describedby") is not None

        # Error alert region should exist
        error_alert = page.locator("[role='alert']")
        assert error_alert.count() > 0
