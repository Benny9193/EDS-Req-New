"""
Tests for authentication routes: login, session validation, logout, touch.
"""

import pytest
from unittest.mock import patch, MagicMock


# ============================================
# Login Tests
# ============================================

class TestLogin:
    """Test POST /api/auth/login endpoint."""

    @patch("api.routes.auth.get_db_cursor")
    def test_login_success(self, mock_cursor_ctx, test_client):
        """Successful login returns session and user info."""
        mock_cursor = MagicMock()
        mock_cursor_ctx.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_cursor_ctx.return_value.__exit__ = MagicMock(return_value=False)

        # First call: sp_FA_AttemptLogin returns SessionId
        login_row = MagicMock()
        login_row.__getitem__ = lambda self, i: 101 if i == 0 else None

        # Second call: session details query
        session_row = MagicMock()
        session_row.SessionId = 101
        session_row.UserId = 42
        session_row.UserName = "jdoe"
        session_row.FirstName = "Jane"
        session_row.LastName = "Doe"
        session_row.Email = "jdoe@school.edu"
        session_row.DistrictId = 1
        session_row.DistrictCode = "DIST"
        session_row.DistrictName = "Test District"
        session_row.SchoolId = 5
        session_row.ApprovalLevel = 0

        mock_cursor.fetchone.side_effect = [login_row, session_row]

        response = test_client.post("/api/auth/login", json={
            "district_code": "DIST",
            "user_number": "12345",
            "password": "secret"
        })
        assert response.status_code == 200
        data = response.json()
        assert data["session_id"] == 101
        assert data["user"]["user_id"] == 42
        assert data["user"]["first_name"] == "Jane"
        assert data["district"]["district_code"] == "DIST"

    @patch("api.routes.auth.get_db_cursor")
    def test_login_invalid_credentials(self, mock_cursor_ctx, test_client):
        """Invalid credentials return 401."""
        mock_cursor = MagicMock()
        mock_cursor_ctx.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_cursor_ctx.return_value.__exit__ = MagicMock(return_value=False)

        # sp_FA_AttemptLogin returns NULL (failed auth)
        null_row = MagicMock()
        null_row.__getitem__ = lambda self, i: None
        mock_cursor.fetchone.return_value = null_row

        response = test_client.post("/api/auth/login", json={
            "district_code": "DIST",
            "user_number": "99999",
            "password": "wrong"
        })
        assert response.status_code == 401
        assert "Invalid credentials" in response.json()["detail"]

    @patch("api.routes.auth.get_db_cursor")
    def test_login_no_result(self, mock_cursor_ctx, test_client):
        """No row from stored proc returns 401."""
        mock_cursor = MagicMock()
        mock_cursor_ctx.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_cursor_ctx.return_value.__exit__ = MagicMock(return_value=False)

        mock_cursor.fetchone.return_value = None

        response = test_client.post("/api/auth/login", json={
            "district_code": "DIST",
            "user_number": "12345",
            "password": "pass"
        })
        assert response.status_code == 401

    def test_login_missing_fields(self, test_client):
        """Missing required fields return 422."""
        response = test_client.post("/api/auth/login", json={
            "district_code": "DIST"
            # missing user_number and password
        })
        assert response.status_code == 422

    def test_login_district_code_too_long(self, test_client):
        """District code exceeding max_length returns 422."""
        response = test_client.post("/api/auth/login", json={
            "district_code": "TOOLONG",
            "user_number": "12345",
            "password": "pass"
        })
        assert response.status_code == 422


# ============================================
# Session Validation Tests
# ============================================

class TestGetSession:
    """Test GET /api/auth/session/{session_id} endpoint."""

    @patch("api.routes.auth.execute_single")
    def test_valid_session(self, mock_exec, test_client):
        """Valid session returns session details with is_valid=True."""
        mock_exec.return_value = {
            "SessionId": 101,
            "UserId": 42,
            "DistrictId": 1,
            "SchoolId": 5,
            "SessionEnd": None,
            "SessionStart": "2025-01-01T09:00:00",
            "SessionLast": "2025-01-01T09:30:00",
            "session_age_hours": 1,
            "inactive_hours": 0,
        }
        response = test_client.get("/api/auth/session/101")
        assert response.status_code == 200
        data = response.json()
        assert data["session_id"] == 101
        assert data["user_id"] == 42
        assert data["is_valid"] is True

    @patch("api.routes.auth.execute_single")
    def test_session_not_found(self, mock_exec, test_client):
        """Non-existent session returns 404."""
        mock_exec.return_value = None
        response = test_client.get("/api/auth/session/999")
        assert response.status_code == 404

    @patch("api.routes.auth.execute_single")
    def test_session_already_ended(self, mock_exec, test_client):
        """Session with SessionEnd set returns 401."""
        mock_exec.return_value = {
            "SessionId": 101,
            "UserId": 42,
            "DistrictId": 1,
            "SchoolId": 5,
            "SessionEnd": "2025-01-01T17:00:00",
            "SessionStart": "2025-01-01T09:00:00",
            "SessionLast": "2025-01-01T16:00:00",
            "session_age_hours": 2,
            "inactive_hours": 1,
        }
        response = test_client.get("/api/auth/session/101")
        assert response.status_code == 401
        assert "expired" in response.json()["detail"].lower()

    @patch("api.routes.auth.execute_single")
    def test_session_expired_age(self, mock_exec, test_client):
        """Session exceeding max age returns 401."""
        mock_exec.return_value = {
            "SessionId": 101,
            "UserId": 42,
            "DistrictId": 1,
            "SchoolId": 5,
            "SessionEnd": None,
            "SessionStart": "2025-01-01T00:00:00",
            "SessionLast": "2025-01-01T08:00:00",
            "session_age_hours": 10,  # > SESSION_TIMEOUT_HOURS (8)
            "inactive_hours": 0,
        }
        response = test_client.get("/api/auth/session/101")
        assert response.status_code == 401

    @patch("api.routes.auth.execute_single")
    def test_session_inactive_too_long(self, mock_exec, test_client):
        """Session inactive too long returns 401."""
        mock_exec.return_value = {
            "SessionId": 101,
            "UserId": 42,
            "DistrictId": 1,
            "SchoolId": 5,
            "SessionEnd": None,
            "SessionStart": "2025-01-01T09:00:00",
            "SessionLast": "2025-01-01T09:00:00",
            "session_age_hours": 4,
            "inactive_hours": 3,  # > SESSION_INACTIVITY_HOURS (2)
        }
        response = test_client.get("/api/auth/session/101")
        assert response.status_code == 401
        assert "inactivity" in response.json()["detail"].lower()


# ============================================
# Logout Tests
# ============================================

class TestLogout:
    """Test POST /api/auth/logout endpoint."""

    @patch("api.routes.auth.get_db_cursor")
    def test_logout_success(self, mock_cursor_ctx, test_client):
        """Successful logout returns confirmation message."""
        mock_cursor = MagicMock()
        mock_cursor_ctx.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_cursor_ctx.return_value.__exit__ = MagicMock(return_value=False)
        mock_cursor.rowcount = 1

        response = test_client.post("/api/auth/logout?session_id=101")
        assert response.status_code == 200
        data = response.json()
        assert "Logged out" in data["message"]
        assert data["session_id"] == 101

    @patch("api.routes.auth.get_db_cursor")
    def test_logout_already_ended(self, mock_cursor_ctx, test_client):
        """Logout on already-ended session still returns 200."""
        mock_cursor = MagicMock()
        mock_cursor_ctx.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_cursor_ctx.return_value.__exit__ = MagicMock(return_value=False)
        mock_cursor.rowcount = 0

        response = test_client.post("/api/auth/logout?session_id=999")
        assert response.status_code == 200


# ============================================
# Touch Session Tests
# ============================================

class TestTouchSession:
    """Test POST /api/auth/session/{session_id}/touch endpoint."""

    @patch("api.routes.auth.get_db_cursor")
    def test_touch_success(self, mock_cursor_ctx, test_client):
        """Touch on active session returns success."""
        mock_cursor = MagicMock()
        mock_cursor_ctx.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_cursor_ctx.return_value.__exit__ = MagicMock(return_value=False)
        mock_cursor.rowcount = 1

        response = test_client.post("/api/auth/session/101/touch")
        assert response.status_code == 200
        data = response.json()
        assert data["session_id"] == 101

    @patch("api.routes.auth.get_db_cursor")
    def test_touch_expired_session(self, mock_cursor_ctx, test_client):
        """Touch on expired/non-existent session returns 401."""
        mock_cursor = MagicMock()
        mock_cursor_ctx.return_value.__enter__ = MagicMock(return_value=mock_cursor)
        mock_cursor_ctx.return_value.__exit__ = MagicMock(return_value=False)
        mock_cursor.rowcount = 0

        response = test_client.post("/api/auth/session/999/touch")
        assert response.status_code == 401
