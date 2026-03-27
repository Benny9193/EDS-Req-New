"""
Tests for Vendors API endpoints.
"""

import pytest
from unittest.mock import patch


class TestGetVendors:
    """Test suite for GET /api/vendors endpoint."""

    def test_get_vendors_success(self, test_client):
        """Test successful vendor listing."""
        with patch('api.routes.vendors.execute_query') as mock_query:
            mock_query.return_value = [
                {"id": 1, "name": "School Supplies Inc", "code": "SSI", "product_count": 450},
                {"id": 2, "name": "Paper Plus", "code": "PP", "product_count": 123},
                {"id": 3, "name": "Art World", "code": "AW", "product_count": 287},
            ]

            response = test_client.get("/api/vendors")
            assert response.status_code == 200
            data = response.json()

            assert isinstance(data, list)
            assert len(data) == 3
            assert data[0]["name"] == "School Supplies Inc"

    def test_get_vendors_empty(self, test_client):
        """Test empty vendor list."""
        with patch('api.routes.vendors.execute_query') as mock_query:
            mock_query.return_value = []

            response = test_client.get("/api/vendors")
            assert response.status_code == 200
            assert response.json() == []

    def test_get_vendors_database_error(self, test_client):
        """Test database error handling."""
        with patch('api.routes.vendors.execute_query') as mock_query:
            mock_query.side_effect = Exception("Database connection failed")

            response = test_client.get("/api/vendors")
            assert response.status_code == 500


class TestVendorModel:
    """Test vendor data validation."""

    def test_vendor_response_structure(self, test_client, sample_vendors):
        """Test vendor response has correct structure."""
        with patch('api.routes.vendors.execute_query') as mock_query:
            mock_query.return_value = sample_vendors

            response = test_client.get("/api/vendors")
            assert response.status_code == 200
            data = response.json()

            for vendor in data:
                assert "id" in vendor
                assert "name" in vendor
                # code and product_count may be optional
