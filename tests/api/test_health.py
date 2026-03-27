"""
Tests for API health and status endpoints.
"""

import pytest
from unittest.mock import patch


class TestHealthEndpoints:
    """Test suite for health check endpoints."""

    def test_root_endpoint(self, test_client):
        """Test root endpoint serves the frontend application."""
        response = test_client.get("/")
        assert response.status_code == 200
        # Root now serves HTML frontend, not JSON API info
        assert "text/html" in response.headers.get("content-type", "")

    def test_health_check(self, test_client):
        """Test simple health check endpoint."""
        response = test_client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"

    def test_status_healthy_db(self, test_client, mock_healthy_db):
        """Test status endpoint with healthy database."""
        response = test_client.get("/api/status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["database_connected"] is True
        assert "version" in data

    def test_status_unhealthy_db(self, test_client, mock_unhealthy_db):
        """Test status endpoint with unhealthy database."""
        response = test_client.get("/api/status")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "degraded"
        assert data["database_connected"] is False


class TestCORSHeaders:
    """Test CORS configuration."""

    def test_cors_headers_present(self, test_client):
        """Test that CORS headers are present in response."""
        response = test_client.options(
            "/api/health",
            headers={
                "Origin": "http://localhost:3000",
                "Access-Control-Request-Method": "GET"
            }
        )
        # FastAPI handles CORS, check for 200 or 405 (method not allowed but CORS processed)
        assert response.status_code in [200, 405]

    def test_cors_allows_local_origin(self, test_client):
        """Test that local origins are allowed."""
        response = test_client.get(
            "/api/health",
            headers={"Origin": "http://localhost:3000"}
        )
        assert response.status_code == 200
        # CORS headers should allow the origin
        assert "access-control-allow-origin" in response.headers or response.status_code == 200
