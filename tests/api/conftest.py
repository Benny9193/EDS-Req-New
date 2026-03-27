"""
API test fixtures and configuration.

Provides FastAPI TestClient and mock database fixtures.
"""

import pytest
import asyncio
from unittest.mock import MagicMock, patch
from fastapi.testclient import TestClient

# Import the FastAPI app
import sys
from pathlib import Path

# Ensure api module is importable
api_dir = Path(__file__).parent.parent.parent / 'api'
sys.path.insert(0, str(api_dir.parent))


@pytest.fixture(autouse=True)
def clear_cache():
    """Clear the API cache before each test to ensure test isolation."""
    from api.cache import get_cache
    cache = get_cache()
    # Clear cache synchronously
    cache._cache.clear()
    yield
    # Clear again after test
    cache._cache.clear()


@pytest.fixture(scope="module")
def test_client():
    """Create a FastAPI test client."""
    from api.main import app
    with TestClient(app) as client:
        yield client


@pytest.fixture
def mock_db_connection():
    """Mock database connection for unit tests."""
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value = mock_cursor
    mock_cursor.fetchall.return_value = []
    mock_cursor.fetchone.return_value = None
    return mock_conn, mock_cursor


@pytest.fixture
def sample_product_data():
    """Sample product data for testing."""
    return {
        "id": "TEST-001",
        "name": "Test Product",
        "description": "A test product description",
        "vendor": "Test Vendor",
        "vendor_item_code": "TV-001",
        "category": "Test Category",
        "image": "https://example.com/image.jpg",
        "status": "in-stock",
        "unit_of_measure": "Each",
        "unit_price": 9.99,
        "tags": ["test", "sample"]
    }


@pytest.fixture
def sample_product_list():
    """Sample product list from database query."""
    return [
        {
            "id": "PROD-001",
            "name": "Pencils #2 Yellow",
            "description": "Standard #2 pencils, pack of 12",
            "vendor": "School Supplies Inc",
            "vendor_item_code": "SSI-P12",
            "category": "Writing Supplies",
            "image": None,
            "status": "in-stock",
            "unit_of_measure": "Pack",
            "unit_price": 3.99,
        },
        {
            "id": "PROD-002",
            "name": "Notebook Spiral 100ct",
            "description": "College ruled spiral notebook",
            "vendor": "Paper Plus",
            "vendor_item_code": "PP-NB100",
            "category": "Paper Products",
            "image": "https://example.com/notebook.jpg",
            "status": "in-stock",
            "unit_of_measure": "Each",
            "unit_price": 2.49,
        },
        {
            "id": "PROD-003",
            "name": "Markers Washable 8pk",
            "description": "Washable markers, assorted colors",
            "vendor": "Art World",
            "vendor_item_code": "AW-WM8",
            "category": "Art Supplies",
            "image": None,
            "status": "low-stock",
            "unit_of_measure": "Pack",
            "unit_price": 5.99,
        },
    ]


@pytest.fixture
def sample_categories():
    """Sample category data."""
    return [
        {"id": 1, "name": "Writing Supplies", "product_count": 150},
        {"id": 2, "name": "Paper Products", "product_count": 89},
        {"id": 3, "name": "Art Supplies", "product_count": 234},
        {"id": 4, "name": "Classroom Supplies", "product_count": 67},
    ]


@pytest.fixture
def sample_vendors():
    """Sample vendor data."""
    return [
        {"id": 1, "name": "School Supplies Inc", "code": "SSI", "product_count": 450},
        {"id": 2, "name": "Paper Plus", "code": "PP", "product_count": 123},
        {"id": 3, "name": "Art World", "code": "AW", "product_count": 287},
    ]


@pytest.fixture
def mock_db_products(mock_db_connection, sample_product_list):
    """Mock database returning product list."""
    mock_conn, mock_cursor = mock_db_connection

    # Convert sample products to tuple format (as returned by pyodbc)
    mock_cursor.fetchall.return_value = [
        (
            p["id"], p["name"], p["description"], p["vendor"],
            p["vendor_item_code"], p["category"], p["image"],
            p["status"], p["unit_of_measure"], p["unit_price"]
        )
        for p in sample_product_list
    ]
    mock_cursor.fetchone.return_value = (len(sample_product_list),)

    return mock_conn, mock_cursor


@pytest.fixture
def mock_healthy_db():
    """Mock a healthy database connection."""
    # Patch where it's used (main.py), not where it's defined (database.py)
    with patch('api.main.test_connection') as mock_test:
        mock_test.return_value = True
        yield mock_test


@pytest.fixture
def mock_unhealthy_db():
    """Mock an unhealthy database connection."""
    # Patch where it's used (main.py), not where it's defined (database.py)
    with patch('api.main.test_connection') as mock_test:
        mock_test.return_value = False
        yield mock_test
