"""
Tests for API middleware: rate limiting, auth dependency, and security headers.
"""

import time
import pytest
from unittest.mock import patch, MagicMock
from fastapi import FastAPI, Depends
from fastapi.testclient import TestClient
from starlette.responses import JSONResponse

from api.middleware import (
    RateLimitMiddleware,
    SecurityHeadersMiddleware,
    get_current_user,
    SESSION_TIMEOUT_HOURS,
    SESSION_INACTIVITY_HOURS,
)


# ============================================
# Security Headers Tests
# ============================================

class TestSecurityHeaders:
    """Test SecurityHeadersMiddleware adds all required headers."""

    def test_csp_header_present(self, test_client):
        """CSP header is set on all responses."""
        response = test_client.get("/api/health")
        csp = response.headers.get("content-security-policy", "")
        assert "default-src 'self'" in csp

    def test_csp_allows_alpine_js(self, test_client):
        """CSP allows Alpine.js from cdn.jsdelivr.net."""
        response = test_client.get("/api/health")
        csp = response.headers.get("content-security-policy", "")
        assert "cdn.jsdelivr.net" in csp

    def test_csp_allows_tailwind(self, test_client):
        """CSP allows Tailwind CSS from cdn.tailwindcss.com."""
        response = test_client.get("/api/health")
        csp = response.headers.get("content-security-policy", "")
        assert "cdn.tailwindcss.com" in csp

    def test_csp_allows_font_awesome(self, test_client):
        """CSP allows Font Awesome from cdnjs.cloudflare.com."""
        response = test_client.get("/api/health")
        csp = response.headers.get("content-security-policy", "")
        assert "cdnjs.cloudflare.com" in csp

    def test_x_frame_options(self, test_client):
        """X-Frame-Options is set to DENY."""
        response = test_client.get("/api/health")
        assert response.headers.get("x-frame-options") == "DENY"

    def test_x_content_type_options(self, test_client):
        """X-Content-Type-Options is set to nosniff."""
        response = test_client.get("/api/health")
        assert response.headers.get("x-content-type-options") == "nosniff"

    def test_referrer_policy(self, test_client):
        """Referrer-Policy is set to strict-origin-when-cross-origin."""
        response = test_client.get("/api/health")
        assert response.headers.get("referrer-policy") == "strict-origin-when-cross-origin"

    def test_permissions_policy(self, test_client):
        """Permissions-Policy disables camera, microphone, geolocation."""
        response = test_client.get("/api/health")
        policy = response.headers.get("permissions-policy", "")
        assert "camera=()" in policy
        assert "microphone=()" in policy
        assert "geolocation=()" in policy


# ============================================
# Rate Limiting Tests
# ============================================

class TestRateLimiting:
    """Test RateLimitMiddleware behavior."""

    def _make_app(self, requests_per_minute=5):
        """Create a minimal app with rate limiting for isolated testing."""
        app = FastAPI()
        app.add_middleware(RateLimitMiddleware, requests_per_minute=requests_per_minute)

        @app.get("/test")
        async def test_endpoint():
            return {"ok": True}

        @app.get("/api/health")
        async def health():
            return {"status": "ok"}

        @app.get("/js/app.js")
        async def static_js():
            return {"file": "app.js"}

        return TestClient(app)

    def test_allows_requests_under_limit(self):
        """Requests under the limit succeed."""
        client = self._make_app(requests_per_minute=10)
        for _ in range(5):
            response = client.get("/test")
            assert response.status_code == 200

    def test_blocks_over_limit(self):
        """Requests over the limit return 429."""
        client = self._make_app(requests_per_minute=3)
        # First 3 should succeed
        for _ in range(3):
            response = client.get("/test")
            assert response.status_code == 200
        # 4th should be rate limited
        response = client.get("/test")
        assert response.status_code == 429
        assert "Retry-After" in response.headers

    def test_rate_limit_response_body(self):
        """429 response includes helpful error message."""
        client = self._make_app(requests_per_minute=1)
        client.get("/test")
        response = client.get("/test")
        assert response.status_code == 429
        data = response.json()
        assert "Too many requests" in data["detail"]

    def test_health_exempt(self):
        """Health check endpoints are exempt from rate limiting."""
        client = self._make_app(requests_per_minute=2)
        # Exhaust the rate limit on /test
        for _ in range(2):
            client.get("/test")
        assert client.get("/test").status_code == 429
        # /api/health should still work
        response = client.get("/api/health")
        assert response.status_code == 200

    def test_static_files_exempt(self):
        """Static file paths are exempt from rate limiting."""
        client = self._make_app(requests_per_minute=2)
        # Exhaust limit on /test
        for _ in range(2):
            client.get("/test")
        assert client.get("/test").status_code == 429
        # Static files should still work
        response = client.get("/js/app.js")
        assert response.status_code == 200


# ============================================
# Auth Dependency Tests
# ============================================

class TestGetCurrentUser:
    """Test get_current_user dependency."""

    def _make_app_with_auth(self):
        """Create a minimal app using get_current_user dependency."""
        app = FastAPI()

        @app.get("/protected")
        async def protected(user: dict = Depends(get_current_user)):
            return {"user_id": user.get("UserId"), "first_name": user.get("FirstName")}

        return TestClient(app)

    @patch("api.middleware.execute_single")
    def test_valid_session(self, mock_exec):
        """Valid session returns user info."""
        mock_exec.return_value = {
            "SessionId": 100,
            "UserId": 42,
            "SchoolId": 5,
            "DistrictId": 1,
            "ApprovalLevel": 0,
            "FirstName": "Jane",
            "LastName": "Doe",
            "session_age_hours": 1,
            "inactive_hours": 0,
        }
        client = self._make_app_with_auth()
        response = client.get("/protected?session_id=100")
        assert response.status_code == 200
        data = response.json()
        assert data["user_id"] == 42
        assert data["first_name"] == "Jane"

    @patch("api.middleware.execute_single")
    def test_invalid_session(self, mock_exec):
        """Non-existent session returns 401."""
        mock_exec.return_value = None
        client = self._make_app_with_auth()
        response = client.get("/protected?session_id=999")
        assert response.status_code == 401

    @patch("api.middleware.execute_single")
    def test_expired_session_age(self, mock_exec):
        """Session exceeding max age returns 401."""
        mock_exec.return_value = {
            "SessionId": 100,
            "UserId": 42,
            "SchoolId": 5,
            "DistrictId": 1,
            "ApprovalLevel": 0,
            "FirstName": "Jane",
            "LastName": "Doe",
            "session_age_hours": SESSION_TIMEOUT_HOURS + 1,
            "inactive_hours": 0,
        }
        client = self._make_app_with_auth()
        response = client.get("/protected?session_id=100")
        assert response.status_code == 401
        assert "expired" in response.json()["detail"].lower()

    @patch("api.middleware.execute_single")
    def test_inactive_session(self, mock_exec):
        """Session exceeding inactivity limit returns 401."""
        mock_exec.return_value = {
            "SessionId": 100,
            "UserId": 42,
            "SchoolId": 5,
            "DistrictId": 1,
            "ApprovalLevel": 0,
            "FirstName": "Jane",
            "LastName": "Doe",
            "session_age_hours": 1,
            "inactive_hours": SESSION_INACTIVITY_HOURS + 1,
        }
        client = self._make_app_with_auth()
        response = client.get("/protected?session_id=100")
        assert response.status_code == 401
        assert "inactivity" in response.json()["detail"].lower()

    def test_missing_session_id_param(self):
        """Missing session_id query param returns 422."""
        client = self._make_app_with_auth()
        response = client.get("/protected")
        assert response.status_code == 422


# ============================================
# Session Constants Tests
# ============================================

class TestSessionConstants:
    """Ensure session timeout constants are reasonable."""

    def test_timeout_is_positive(self):
        assert SESSION_TIMEOUT_HOURS > 0

    def test_inactivity_is_positive(self):
        assert SESSION_INACTIVITY_HOURS > 0

    def test_inactivity_less_than_timeout(self):
        assert SESSION_INACTIVITY_HOURS < SESSION_TIMEOUT_HOURS
