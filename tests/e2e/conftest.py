"""
E2E test fixtures and configuration for Playwright.

Usage:
    # Start the API server first:
    uvicorn api.main:app --port 8000

    # Then run tests:
    pytest tests/e2e/ --headed  # Run with browser visible
    pytest tests/e2e/           # Run headless (default)

    # Override base URL:
    pytest tests/e2e/ --base-url http://localhost:3000

    # Visual regression:
    pytest tests/e2e/test_visual_regression.py           # Compare against baselines
    pytest tests/e2e/test_visual_regression.py --update-snapshots  # Update baselines
"""

import pytest
import urllib.request
from pathlib import Path

# Check if playwright is available
try:
    from playwright.sync_api import sync_playwright, Page, Browser, BrowserContext
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    PLAYWRIGHT_AVAILABLE = False


# Frontend paths (for file:// fallback)
FRONTEND_DIR = Path(__file__).parent.parent.parent / "frontend"
ALPINE_HTML = FRONTEND_DIR / "alpine-requisition.html"

# Default API server URL
DEFAULT_BASE_URL = "http://localhost:8000"


def pytest_addoption(parser):
    """Add CLI options for E2E tests."""
    parser.addoption(
        "--base-url",
        action="store",
        default=DEFAULT_BASE_URL,
        help="Base URL of the running API server (default: http://localhost:8000)",
    )
    parser.addoption(
        "--update-snapshots",
        action="store_true",
        default=False,
        help="Update visual regression baseline screenshots instead of comparing",
    )


def pytest_configure(config):
    """Register custom markers."""
    config.addinivalue_line("markers", "e2e: marks tests as end-to-end tests")


def _server_is_running(url: str) -> bool:
    """Check if the API server is reachable."""
    try:
        urllib.request.urlopen(f"{url}/api/health", timeout=3)
        return True
    except Exception:
        return False


@pytest.fixture(scope="session")
def base_url(request):
    """Resolve the base URL - prefer running server, fall back to file://."""
    url = request.config.getoption("--base-url")
    if _server_is_running(url):
        return url
    # Fall back to file:// (limited: CDN scripts won't load)
    if ALPINE_HTML.exists():
        return ALPINE_HTML.resolve().as_uri()
    pytest.skip("No running server and frontend files not found")


@pytest.fixture(scope="session")
def server_available(base_url):
    """Whether we're testing against a real HTTP server."""
    return base_url.startswith("http")


@pytest.fixture(scope="session")
def browser():
    """Create a browser instance for the test session."""
    if not PLAYWRIGHT_AVAILABLE:
        pytest.skip("Playwright not installed. Run: pip install playwright && playwright install")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Create a new page for each test."""
    context = browser.new_context(
        viewport={"width": 1280, "height": 720}
    )
    page = context.new_page()
    yield page
    context.close()


@pytest.fixture
def frontend_url(base_url):
    """
    Get the frontend URL for the main app page.

    When server is running: http://localhost:8000/
    When file://: file:///path/to/frontend/alpine-requisition.html
    """
    if base_url.startswith("http"):
        return base_url + "/"
    return base_url


@pytest.fixture
def make_url(base_url):
    """
    Factory fixture: build a URL for any page.

    Usage:
        url = make_url("login")           -> http://localhost:8000/login
        url = make_url("admin/approvals") -> http://localhost:8000/admin/approvals
        url = make_url("checkout")        -> http://localhost:8000/checkout

    Falls back to file:// when server is unavailable.
    """
    def _make(page_name: str) -> str:
        if base_url.startswith("http"):
            return f"{base_url}/{page_name}"
        # file:// fallback: resolve relative to frontend dir
        html_file = (FRONTEND_DIR / f"{page_name}.html").resolve()
        if html_file.exists():
            return html_file.as_uri()
        # Try without .html suffix already present
        return (FRONTEND_DIR / page_name).resolve().as_uri()
    return _make


@pytest.fixture
def api_base_url(base_url):
    """Get the API base URL."""
    if base_url.startswith("http"):
        return base_url
    return "http://localhost:8000"


@pytest.fixture
def authed_page(browser, base_url):
    """
    Create a page with mock authentication that survives server-side validation.

    The auth store calls /api/auth/session/{id} on init. Without a real DB
    session, this returns 404, which triggers clearSession() and a redirect
    to /login. This fixture intercepts that API call to return is_valid=true,
    keeping the mock session alive.

    Usage in tests:
        def test_something(self, authed_page, make_url, server_available):
            page = authed_page          # already has route interception
            page.goto(make_url("admin/approvals"))
            ...
    """
    import json

    context = browser.new_context(viewport={"width": 1280, "height": 720})
    page = context.new_page()

    # Only intercept when testing against a live server
    if base_url.startswith("http"):
        def handle_session_validation(route):
            """Return a valid session response for any session ID."""
            route.fulfill(
                status=200,
                content_type="application/json",
                body=json.dumps({"is_valid": True}),
            )

        # Intercept session validation calls
        page.route("**/api/auth/session/*", handle_session_validation)

    yield page
    context.close()


# ── Visual Regression Fixtures ──────────────────────────────────────────


SNAPSHOT_DIR = Path(__file__).parent / "snapshots"


@pytest.fixture(scope="session")
def snapshot_dir():
    """Root directory for visual regression screenshots."""
    SNAPSHOT_DIR.mkdir(parents=True, exist_ok=True)
    return SNAPSHOT_DIR


@pytest.fixture(scope="session")
def update_snapshots(request):
    """Whether to update baselines instead of comparing."""
    return request.config.getoption("--update-snapshots")
