"""
Tests for Products API endpoints.
"""

import pytest
from unittest.mock import patch, MagicMock


class TestGetProducts:
    """Test suite for GET /api/products endpoint."""

    def test_get_products_success(self, test_client):
        """Test successful product listing."""
        with patch('api.routes.products.execute_query') as mock_query, \
             patch('api.routes.products.execute_single') as mock_single:
            # Mock count query
            mock_single.return_value = {"total": 100}
            # Mock products query
            mock_query.return_value = [
                {
                    "id": 1, "item_code": "P001", "name": "Test Product",
                    "description": "Test desc", "vendor": "Test Vendor",
                    "vendor_item_code": "TV001", "category": "Writing",
                    "image": None, "status": "in-stock",
                    "unit_of_measure": "Each", "unit_price": 9.99
                }
            ]

            response = test_client.get("/api/products")
            assert response.status_code == 200
            data = response.json()

            assert "products" in data
            assert "total" in data
            assert "page" in data
            assert "page_size" in data
            assert "total_pages" in data
            assert data["total"] == 100

    def test_get_products_with_pagination(self, test_client):
        """Test pagination parameters."""
        with patch('api.routes.products.execute_query') as mock_query, \
             patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = {"total": 50}
            mock_query.return_value = []

            response = test_client.get("/api/products?page=2&page_size=10")
            assert response.status_code == 200
            data = response.json()
            assert data["page"] == 2
            assert data["page_size"] == 10

    def test_get_products_with_search_query(self, test_client):
        """Test search query filter."""
        with patch('api.routes.products.execute_query') as mock_query, \
             patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = {"total": 5}
            mock_query.return_value = []

            response = test_client.get("/api/products?query=pencil")
            assert response.status_code == 200

    def test_get_products_with_category_filter(self, test_client):
        """Test category filter."""
        with patch('api.routes.products.execute_query') as mock_query, \
             patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = {"total": 10}
            mock_query.return_value = []

            response = test_client.get("/api/products?category=Writing%20Supplies")
            assert response.status_code == 200

    def test_get_products_with_vendor_filter(self, test_client):
        """Test vendor filter."""
        with patch('api.routes.products.execute_query') as mock_query, \
             patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = {"total": 25}
            mock_query.return_value = []

            response = test_client.get("/api/products?vendor=School%20Supplies")
            assert response.status_code == 200

    def test_get_products_with_price_range(self, test_client):
        """Test price range filter."""
        with patch('api.routes.products.execute_query') as mock_query, \
             patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = {"total": 15}
            mock_query.return_value = []

            response = test_client.get("/api/products?min_price=5.00&max_price=20.00")
            assert response.status_code == 200

    def test_get_products_invalid_price_range(self, test_client):
        """Test invalid price range (min > max)."""
        response = test_client.get("/api/products?min_price=100&max_price=10")
        assert response.status_code == 400
        assert "min_price" in response.json()["detail"].lower()

    def test_get_products_invalid_pagination_page(self, test_client):
        """Test invalid page number."""
        response = test_client.get("/api/products?page=0")
        assert response.status_code == 422  # FastAPI validation error

    def test_get_products_invalid_page_size(self, test_client):
        """Test invalid page size (over limit)."""
        response = test_client.get("/api/products?page_size=500")
        assert response.status_code == 422

    def test_get_products_with_status_filter(self, test_client):
        """Test status filter."""
        with patch('api.routes.products.execute_query') as mock_query, \
             patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = {"total": 30}
            mock_query.return_value = []

            response = test_client.get("/api/products?status=in-stock")
            assert response.status_code == 200

    def test_get_products_with_multiple_status(self, test_client):
        """Test multiple status filter (comma-separated)."""
        with patch('api.routes.products.execute_query') as mock_query, \
             patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = {"total": 50}
            mock_query.return_value = []

            response = test_client.get("/api/products?status=in-stock,low-stock")
            assert response.status_code == 200


class TestAutocomplete:
    """Test suite for autocomplete search endpoint."""

    def test_autocomplete_success(self, test_client):
        """Test successful autocomplete search."""
        with patch('api.routes.products.execute_query') as mock_query:
            mock_query.return_value = [
                {
                    "id": 1, "item_code": "P001", "name": "Pencil #2 Yellow",
                    "description": "Standard pencil", "vendor": "Test Vendor",
                    "vendor_item_code": "TV001", "category": "Writing",
                    "image": None, "status": "in-stock",
                    "unit_of_measure": "Pack", "unit_price": 3.99
                }
            ]

            response = test_client.get("/api/products/search/autocomplete?q=pencil")
            assert response.status_code == 200
            data = response.json()
            assert isinstance(data, list)

    def test_autocomplete_minimum_length(self, test_client):
        """Test autocomplete requires minimum query length."""
        response = test_client.get("/api/products/search/autocomplete?q=a")
        assert response.status_code == 422  # Validation error for min_length

    def test_autocomplete_with_limit(self, test_client):
        """Test autocomplete respects limit parameter."""
        with patch('api.routes.products.execute_query') as mock_query:
            mock_query.return_value = []

            response = test_client.get("/api/products/search/autocomplete?q=test&limit=5")
            assert response.status_code == 200

    def test_autocomplete_empty_results(self, test_client):
        """Test autocomplete with no matches."""
        with patch('api.routes.products.execute_query') as mock_query:
            mock_query.return_value = []

            response = test_client.get("/api/products/search/autocomplete?q=xyznonexistent")
            assert response.status_code == 200
            assert response.json() == []


class TestGetSingleProduct:
    """Test suite for GET /api/products/{product_id} endpoint."""

    def test_get_product_success(self, test_client):
        """Test successful single product retrieval."""
        with patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = {
                "id": 12345, "item_code": "P001", "name": "Test Product",
                "description": "A test product", "vendor": "Test Vendor",
                "vendor_item_code": "TV001", "category": "Writing",
                "image": None, "status": "in-stock",
                "unit_of_measure": "Each", "unit_price": 9.99
            }

            response = test_client.get("/api/products/12345")
            assert response.status_code == 200
            data = response.json()
            assert data["id"] == "12345"
            assert data["name"] == "Test Product"

    def test_get_product_not_found(self, test_client):
        """Test product not found response."""
        with patch('api.routes.products.execute_single') as mock_single:
            mock_single.return_value = None

            response = test_client.get("/api/products/99999")
            assert response.status_code == 404
            assert "not found" in response.json()["detail"].lower()

    def test_get_product_invalid_id_format(self, test_client):
        """Test invalid product ID format."""
        response = test_client.get("/api/products/invalid-id")
        assert response.status_code == 400
        assert "invalid" in response.json()["detail"].lower()


class TestInputSanitization:
    """Test input sanitization functions."""

    def test_sanitize_removes_dangerous_chars(self):
        """Test that dangerous characters are removed."""
        from api.routes.products import sanitize_search_input

        # SQL injection attempt
        result = sanitize_search_input("test'; DROP TABLE Items;--")
        assert "DROP" not in result or ";" not in result

        # XSS attempt
        result = sanitize_search_input("<script>alert('xss')</script>")
        assert "<script>" not in result

    def test_sanitize_preserves_valid_chars(self):
        """Test that valid search characters are preserved."""
        from api.routes.products import sanitize_search_input

        # Normal search queries should work
        result = sanitize_search_input("Pencil #2 Yellow")
        assert "Pencil" in result
        assert "Yellow" in result

    def test_sanitize_max_length(self):
        """Test that sanitize enforces max length."""
        from api.routes.products import sanitize_search_input, MAX_QUERY_LENGTH

        long_string = "a" * 200
        result = sanitize_search_input(long_string)
        assert len(result) <= MAX_QUERY_LENGTH

    def test_validate_status_filter(self):
        """Test status filter validation."""
        from api.routes.products import validate_status_filter

        # Valid statuses
        result = validate_status_filter("in-stock")
        assert "in-stock" in result

        # Invalid status
        result = validate_status_filter("invalid-status")
        assert result == []

        # Mixed valid/invalid
        result = validate_status_filter("in-stock,invalid,low-stock")
        assert "in-stock" in result
        assert "low-stock" in result
        assert len(result) == 2


class TestProductModel:
    """Test product data mapping."""

    def test_map_row_to_product(self, sample_product_data):
        """Test mapping database row to Product model."""
        from api.routes.products import map_row_to_product

        row = {
            "id": 123,
            "item_code": "TEST-001",
            "name": "Test Product",
            "description": "Test description",
            "vendor": "Test Vendor",
            "vendor_item_code": "TV-001",
            "category": "Test Category",
            "image": "https://example.com/img.jpg",
            "status": "in-stock",
            "unit_of_measure": "Each",
            "unit_price": 9.99
        }

        product = map_row_to_product(row)

        assert product.id == "123"
        assert product.name == "Test Product"
        assert product.vendor == "Test Vendor"
        assert product.unit_price == 9.99

    def test_map_row_handles_null_values(self):
        """Test mapping handles NULL/None values gracefully."""
        from api.routes.products import map_row_to_product

        row = {
            "id": 123,
            "item_code": "TEST-001",
            "name": None,  # NULL name
            "description": None,
            "vendor": None,
            "vendor_item_code": None,
            "category": None,
            "image": None,
            "status": None,
            "unit_of_measure": None,
            "unit_price": None
        }

        product = map_row_to_product(row)

        assert product.name == "Unknown Product"
        assert product.vendor == "Unknown Vendor"
        assert product.category == "General"
        assert product.unit_of_measure == "Each"
        assert product.unit_price == 0.0
