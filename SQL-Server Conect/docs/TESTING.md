# EDS Testing Guide

Comprehensive guide for testing the EDS Universal Requisition application.

---

## Overview

The EDS test suite includes:
- **Unit Tests** - Test individual functions and modules
- **API Tests** - Test FastAPI endpoints with mocked database
- **E2E Tests** - Test full user workflows in browser (Playwright)
- **Integration Tests** - Test with real database connections

---

## Quick Start

```bash
# Ensure you're in the project root
cd /mnt/c/EDS

# Activate virtual environment
source .venv/bin/activate

# Install test dependencies
pip install -e ".[dev]"

# Run all tests
pytest

# Run with coverage report
pytest --cov=api --cov=scripts --cov-report=html
```

---

## Test Structure

```
tests/
├── __init__.py
├── conftest.py              # Global fixtures
├── test_config.py           # Configuration tests
├── test_db_utils.py         # Database utility tests
├── test_deploy_indexes.py   # Index deployment tests
├── test_investigate_blocking.py  # Blocking analysis tests
├── test_recursive_procedures.py  # SP recursion tests
│
├── api/                     # API endpoint tests
│   ├── __init__.py
│   ├── conftest.py          # API fixtures (test_client)
│   ├── test_health.py       # Health check endpoint
│   ├── test_products.py     # Products endpoints
│   ├── test_categories.py   # Categories endpoints
│   └── test_vendors.py      # Vendors endpoints
│
└── e2e/                     # End-to-end browser tests
    ├── __init__.py
    ├── conftest.py          # Playwright fixtures
    ├── test_product_browsing.py  # Product browsing flows
    └── test_cart_workflow.py     # Cart/checkout flows
```

---

## Running Tests

### Run All Tests

```bash
# Standard run
pytest

# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Show print statements
pytest -s
```

### Run Specific Tests

```bash
# Run single file
pytest tests/api/test_products.py

# Run single class
pytest tests/api/test_products.py::TestGetProducts

# Run single test
pytest tests/api/test_products.py::TestGetProducts::test_get_products_success

# Run by keyword
pytest -k "test_product"
```

### Run by Marker

```bash
# Skip slow tests
pytest -m "not slow"

# Skip integration tests (require database)
pytest -m "not integration"

# Skip E2E tests (require browser)
pytest -m "not e2e"

# Run only E2E tests
pytest -m e2e
```

### Coverage Reports

```bash
# Generate HTML coverage report
pytest --cov=api --cov=scripts --cov-report=html

# View report
open htmlcov/index.html  # macOS
xdg-open htmlcov/index.html  # Linux
start htmlcov/index.html  # Windows

# Terminal coverage summary
pytest --cov=api --cov-report=term-missing
```

---

## Test Categories

### API Tests

Test the FastAPI backend endpoints with mocked database connections.

**Location:** `tests/api/`

**Example:**
```python
def test_get_products_success(self, test_client):
    """Test successful product listing."""
    with patch('api.routes.products.execute_query') as mock_query:
        mock_query.return_value = [
            {"id": 1, "name": "Test Product", ...}
        ]

        response = test_client.get("/api/products")
        assert response.status_code == 200
        assert "products" in response.json()
```

**Key Tests:**
| File | Endpoint | Tests |
|------|----------|-------|
| `test_health.py` | `/api/health` | Health check, status response |
| `test_products.py` | `/api/products` | Listing, search, filtering, pagination |
| `test_categories.py` | `/api/categories` | Category listing |
| `test_vendors.py` | `/api/vendors` | Vendor listing, search |

### E2E Tests

Test full user workflows in a real browser using Playwright.

**Location:** `tests/e2e/`

**Requirements:**
```bash
# Install Playwright and E2E dependencies
pip install -e ".[e2e]"

# Install browsers
playwright install chromium
```

**Running E2E Tests:**
```bash
# Run all E2E tests
pytest tests/e2e/ -m e2e

# Run with visible browser (headed mode)
pytest tests/e2e/ --headed

# Run specific browser
pytest tests/e2e/ --browser firefox
```

**Example:**
```python
@pytest.mark.e2e
class TestCartDrawer:
    def test_cart_drawer_opens(self, page, frontend_url):
        """Test that cart drawer opens when clicked."""
        page.goto(frontend_url)

        cart_btn = page.locator(".cart-btn").first
        cart_btn.click()

        drawer_heading = page.locator("text=Order List")
        assert drawer_heading.is_visible()
```

### Integration Tests

Test with real database connections.

**Requirements:**
- Database credentials in `.env`
- Network access to SQL Server

**Running:**
```bash
# Run integration tests
pytest -m integration

# Or with specific database
DB_DATABASE=EDS_Test pytest -m integration
```

---

## Fixtures

### Global Fixtures (`tests/conftest.py`)

| Fixture | Purpose |
|---------|---------|
| `sample_config` | Sample configuration dictionary |
| `mock_db_credentials` | Mock environment variables for DB |
| `temp_output_dir` | Temporary directory for test outputs |

### API Fixtures (`tests/api/conftest.py`)

| Fixture | Purpose |
|---------|---------|
| `test_client` | FastAPI TestClient instance |
| `sample_product_data` | Sample product response data |
| `sample_category_data` | Sample category data |

### E2E Fixtures (`tests/e2e/conftest.py`)

| Fixture | Purpose |
|---------|---------|
| `page` | Playwright page object |
| `frontend_url` | URL to frontend (file:// or http://) |
| `api_url` | URL to API server |

---

## Test Configuration

### pytest.ini Options (in `pyproject.toml`)

```toml
[tool.pytest.ini_options]
testpaths = ["tests"]
python_files = "test_*.py"
python_classes = "Test*"
python_functions = "test_*"
addopts = [
    "-v",
    "--tb=short",
    "--strict-markers",
]
markers = [
    "slow: marks tests as slow",
    "integration: marks tests requiring database",
    "e2e: marks end-to-end browser tests",
]
```

### Coverage Configuration

```toml
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

---

## Writing Tests

### Test Naming Conventions

```python
# Files: test_<module>.py
test_products.py
test_cart_workflow.py

# Classes: Test<Feature>
class TestGetProducts:
class TestCartDrawer:

# Functions: test_<behavior>
def test_get_products_success():
def test_get_products_with_pagination():
def test_invalid_price_range():
```

### Test Structure (AAA Pattern)

```python
def test_example():
    # Arrange - Set up test data and mocks
    with patch('module.function') as mock:
        mock.return_value = expected_data

    # Act - Execute the code being tested
    result = function_under_test()

    # Assert - Verify the results
    assert result.status_code == 200
    assert result.data == expected_data
```

### Mocking Database Calls

```python
from unittest.mock import patch, MagicMock

def test_with_mocked_db(test_client):
    with patch('api.routes.products.execute_query') as mock_query, \
         patch('api.routes.products.execute_single') as mock_single:

        mock_single.return_value = {"total": 100}
        mock_query.return_value = [
            {"id": 1, "name": "Product 1"},
            {"id": 2, "name": "Product 2"},
        ]

        response = test_client.get("/api/products")
        assert response.status_code == 200
```

### E2E Test Best Practices

```python
@pytest.mark.e2e
class TestFeature:
    def test_user_flow(self, page, frontend_url):
        # Navigate to page
        page.goto(frontend_url)

        # Wait for app to load
        page.wait_for_function("typeof Alpine !== 'undefined'", timeout=5000)

        # Use stable selectors
        button = page.locator("button[data-testid='submit']")
        # or
        button = page.locator("text=Submit Order")

        # Interact
        button.click()

        # Wait for result (avoid arbitrary timeouts)
        page.wait_for_selector(".success-message")

        # Assert
        assert page.locator(".success-message").is_visible()
```

---

## Debugging Tests

### Verbose Output

```bash
# Show full assertion details
pytest -v --tb=long

# Show local variables on failure
pytest --tb=long -l
```

### Interactive Debugging

```python
def test_example():
    # Add breakpoint
    import pdb; pdb.set_trace()

    # Or use pytest's built-in
    # pytest --pdb (drops into debugger on failure)
```

### E2E Debugging

```bash
# Run with visible browser
pytest tests/e2e/ --headed

# Slow down actions
pytest tests/e2e/ --slowmo=500

# Pause on failure
pytest tests/e2e/ --headed --pause-on-failure
```

---

## CI/CD Integration

### GitHub Actions Example

```yaml
# .github/workflows/test.yml
name: Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.12'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -e ".[dev]"

      - name: Run tests
        run: pytest --cov=api --cov-report=xml

      - name: Upload coverage
        uses: codecov/codecov-action@v3
        with:
          file: ./coverage.xml
```

---

## Troubleshooting

### Common Issues

**"ModuleNotFoundError: No module named 'api'"**
```bash
# Ensure package is installed in editable mode
pip install -e ".[dev]"
```

**"Database connection failed"**
```bash
# Run without integration tests
pytest -m "not integration"

# Or set test database
export DB_DATABASE=EDS_Test
```

**"Playwright browser not installed"**
```bash
playwright install chromium
```

**Tests hang or timeout**
```bash
# Increase timeout
pytest --timeout=60

# Skip slow tests
pytest -m "not slow"
```

---

## See Also

- [Development Guide](DEVELOPMENT.md) - Local development setup
- [API Reference](API_REFERENCE.md) - API endpoint documentation
- [pytest Documentation](https://docs.pytest.org/)
- [Playwright Python](https://playwright.dev/python/)
