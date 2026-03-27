"""
Tests for Categories API endpoints.
"""

import pytest
from unittest.mock import patch


class TestGetCategories:
    """Test suite for GET /api/categories endpoint."""

    def test_get_categories_success(self, test_client):
        """Test successful category listing."""
        with patch('api.routes.categories.execute_query') as mock_query:
            mock_query.return_value = [
                {"id": 1, "name": "Writing Supplies", "product_count": 150},
                {"id": 2, "name": "Art Supplies", "product_count": 200},
                {"id": 3, "name": "Paper Products", "product_count": 75},
            ]

            response = test_client.get("/api/categories")
            assert response.status_code == 200
            data = response.json()

            assert isinstance(data, list)
            assert len(data) == 3
            assert data[0]["name"] == "Writing Supplies"

    def test_get_categories_empty(self, test_client):
        """Test empty category list."""
        with patch('api.routes.categories.execute_query') as mock_query:
            mock_query.return_value = []

            response = test_client.get("/api/categories")
            assert response.status_code == 200
            assert response.json() == []

    def test_get_categories_database_error(self, test_client):
        """Test database error handling."""
        with patch('api.routes.categories.execute_query') as mock_query:
            mock_query.side_effect = Exception("Database connection failed")

            response = test_client.get("/api/categories")
            assert response.status_code == 500


class TestCategoryModel:
    """Test category data validation."""

    def test_category_response_structure(self, test_client, sample_categories):
        """Test category response has correct structure."""
        with patch('api.routes.categories.execute_query') as mock_query:
            mock_query.return_value = sample_categories

            response = test_client.get("/api/categories")
            assert response.status_code == 200
            data = response.json()

            for category in data:
                assert "id" in category
                assert "name" in category
                assert "product_count" in category
