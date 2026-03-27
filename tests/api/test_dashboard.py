"""
Tests for dashboard routes: GET /api/dashboard/summary.
"""

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta


class TestDashboardSummary:
    """Test GET /api/dashboard/summary endpoint."""

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_demo_session_returns_live_data(self, mock_single, mock_query, test_client):
        """Demo session queries live DB data (all users/districts)."""
        mock_single.side_effect = [
            # Budget spend query (no user filter in demo)
            {"spent": 50000},
            # Pending approvals query
            {"cnt": 3, "urgent": 1, "oldest": 5},
        ]
        mock_query.side_effect = [
            # Order status counts (no user filter in demo)
            [
                {"StatusId": 1, "cnt": 2},
                {"StatusId": 2, "cnt": 5},
                {"StatusId": 3, "cnt": 10},
            ],
            # Recent activity
            [
                {"RequisitionId": 101, "RequisitionNumber": "REQ-001", "StatusId": 2, "StatusName": "Pending Approval", "DateUpdated": "2026-03-19", "minutes_ago": 120},
            ],
        ]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "demo"}
        )
        assert response.status_code == 200
        data = response.json()

        # Budget — demo estimates budget as 175% of spend
        assert data["budget"]["spent"] == 50000
        assert data["budget"]["budget"] == 50000 * 1.75

        # Order counts from live query
        assert data["order_counts"]["on_hold"] == 2
        assert data["order_counts"]["pending_approval"] == 5
        assert data["order_counts"]["approved"] == 10
        assert data["order_counts"]["total_active"] == 17

        # Pending approvals from live query
        assert data["pending_approvals"]["count"] == 3
        assert data["pending_approvals"]["urgent"] == 1

        # Approver info
        assert data["approver_info"]["is_approver"] is True
        assert data["approver_info"]["level"] == 1

        # Recent activity from live query
        assert len(data["recent_activity"]) == 1
        assert data["recent_activity"][0]["name"] == "REQ-001"

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_demo_session_generates_alerts(self, mock_single, mock_query, test_client):
        """Demo session generates appropriate alerts from data."""
        mock_single.side_effect = [
            {"spent": 50000},  # budget
            {"cnt": 3, "urgent": 2, "oldest": 5},  # pending approvals
        ]
        mock_query.side_effect = [
            [{"StatusId": 2, "cnt": 3}],  # order counts
            [],  # recent activity
        ]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "demo"}
        )
        data = response.json()

        # Should have urgent approval alert (2 urgent > 0)
        alert_titles = [a["title"] for a in data["alerts"]]
        assert any("Urgent" in t for t in alert_titles)

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_missing_session_header_falls_to_demo(self, mock_single, mock_query, test_client):
        """No session header triggers demo mode (queries all data)."""
        mock_single.side_effect = [
            {"spent": 1000},
            {"cnt": 0, "urgent": 0, "oldest": 0},
        ]
        mock_query.side_effect = [[], []]

        response = test_client.get("/api/dashboard/summary")
        # No header means _get_session_user gets None, which triggers demo mode
        assert response.status_code == 200

    @patch("api.routes.dashboard.execute_single")
    def test_invalid_session_returns_401(self, mock_exec, test_client):
        """Invalid (non-integer, non-demo) session returns 401."""
        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "not-a-number"}
        )
        assert response.status_code == 401

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_valid_session_returns_user_data(self, mock_single, mock_query, test_client):
        """Valid session returns user-specific dashboard data."""
        mock_single.side_effect = [
            # 1st call: session validation
            {
                "UserId": 42, "DistrictId": 1, "SchoolId": 5,
                "ApprovalLevel": 0, "FirstName": "Jane", "LastName": "Doe",
                "Email": "jdoe@school.edu", "DepartmentId": None,
                "Budget": 30000, "BudgetUsed": 10000,
                "DepartmentName": None, "DeptBudget": 0,
            },
            # 2nd call: actual spend from Requisitions
            {"spent": 12000},
        ]

        # Mock queries: order counts, then recent activity
        mock_query.side_effect = [
            # order status counts (StatusId: 1=On Hold, 2=Pending Approval, 3=Approved)
            [
                {"StatusId": 1, "cnt": 1},
                {"StatusId": 2, "cnt": 2},
            ],
            # recent activity
            [
                {"RequisitionId": 101, "RequisitionNumber": "Office Supplies", "StatusId": 1, "StatusName": "On Hold", "DateUpdated": "2026-03-19", "minutes_ago": 120},
            ],
        ]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "999"}
        )
        assert response.status_code == 200
        data = response.json()

        # Budget: $50K default budget, $12K actual spend
        assert data["budget"]["budget"] == 50000
        assert data["budget"]["spent"] == 12000
        assert data["budget"]["remaining"] == 38000
        assert data["budget"]["percent"] == 24

        # Order counts (StatusId 1=on_hold, 2=pending_approval)
        assert data["order_counts"]["on_hold"] == 1
        assert data["order_counts"]["pending_approval"] == 2
        assert data["order_counts"]["total_active"] == 3

        # Non-approver: no approval info
        assert data["approver_info"] is None
        assert data["pending_approvals"]["count"] == 0

        # No department budget
        assert data["department_budget"] is None

        # Recent activity
        assert len(data["recent_activity"]) == 1
        assert data["recent_activity"][0]["name"] == "Office Supplies"
        assert data["recent_activity"][0]["time_label"] == "2h ago"

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_approver_gets_pending_approvals(self, mock_single, mock_query, test_client):
        """User with ApprovalLevel >= 1 gets pending approval counts."""
        mock_single.side_effect = [
            # Session user (approver)
            {
                "UserId": 10, "DistrictId": 1, "SchoolId": 5,
                "ApprovalLevel": 2, "FirstName": "Admin", "LastName": "User",
                "Email": "admin@school.edu", "DepartmentId": None,
                "Budget": 0, "BudgetUsed": 0,
                "DepartmentName": None, "DeptBudget": 0,
            },
            # Actual spend
            {"spent": 0},
            # Pending approvals
            {"cnt": 5, "urgent": 1, "oldest": 10},
        ]

        mock_query.side_effect = [
            [],  # order counts
            [],  # recent activity
        ]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "888"}
        )
        data = response.json()

        assert data["approver_info"]["is_approver"] is True
        assert data["approver_info"]["level"] == 2
        assert data["pending_approvals"]["count"] == 5
        assert data["pending_approvals"]["urgent"] == 1
        assert data["pending_approvals"]["oldest_days"] == 10

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_department_budget_not_implemented(self, mock_single, mock_query, test_client):
        """Department budget is always None (not implemented in schema)."""
        mock_single.side_effect = [
            # Session user with department
            {
                "UserId": 42, "DistrictId": 1, "SchoolId": 5,
                "ApprovalLevel": 0, "UserName": "Jane Doe",
                "Email": "jdoe@school.edu",
            },
            # Actual user spend
            {"spent": 8000},
        ]

        mock_query.side_effect = [
            [],  # order counts
            [],  # recent activity
        ]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "777"}
        )
        data = response.json()

        # department_budget is always None — no Departments table in production schema
        assert data["department_budget"] is None

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_budget_alert_at_75_percent(self, mock_single, mock_query, test_client):
        """Budget at 75%+ triggers warning alert."""
        mock_single.side_effect = [
            {
                "UserId": 42, "DistrictId": 1, "SchoolId": 5,
                "ApprovalLevel": 0, "UserName": "Jane Doe",
                "Email": "jdoe@school.edu",
            },
            {"spent": 40000},  # 80% of 50000 default budget
        ]

        mock_query.side_effect = [[], []]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "666"}
        )
        data = response.json()

        assert data["budget"]["percent"] == 80
        alert_types = [a["type"] for a in data["alerts"]]
        assert "warning" in alert_types

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_budget_alert_at_90_percent(self, mock_single, mock_query, test_client):
        """Budget at 90%+ triggers danger alert."""
        mock_single.side_effect = [
            {
                "UserId": 42, "DistrictId": 1, "SchoolId": 5,
                "ApprovalLevel": 0, "UserName": "Jane Doe",
                "Email": "jdoe@school.edu",
            },
            {"spent": 47500},  # 95% of 50000 default budget
        ]

        mock_query.side_effect = [[], []]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "555"}
        )
        data = response.json()

        assert data["budget"]["percent"] == 95
        alert_types = [a["type"] for a in data["alerts"]]
        assert "danger" in alert_types
        alert_titles = [a["title"] for a in data["alerts"]]
        assert any("Nearly Exhausted" in t for t in alert_titles)

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_expired_session_returns_401(self, mock_single, mock_query, test_client):
        """Expired session returns 401."""
        mock_single.return_value = None  # No session found

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "444"}
        )
        assert response.status_code == 401

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_demo_response_structure(self, mock_single, mock_query, test_client):
        """Verify the full response structure for demo mode."""
        mock_single.side_effect = [
            {"spent": 5000},
            {"cnt": 1, "urgent": 0, "oldest": 2},
        ]
        mock_query.side_effect = [
            [{"StatusId": 2, "cnt": 3}],
            [{"RequisitionId": 1, "RequisitionNumber": "REQ-001", "StatusId": 2, "StatusName": "Pending", "DateUpdated": "2026-03-19", "minutes_ago": 60}],
        ]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "demo"}
        )
        data = response.json()

        # All top-level keys present
        assert "budget" in data
        assert "department_budget" in data
        assert "order_counts" in data
        assert "pending_approvals" in data
        assert "approver_info" in data
        assert "recent_activity" in data
        assert "alerts" in data

        # No deadlines key (removed)
        assert "deadlines" not in data

        # Recent activity structure
        for act in data["recent_activity"]:
            assert "id" in act
            assert "name" in act
            assert "status" in act
            assert "time_label" in act

        # Budget keys
        b = data["budget"]
        assert all(k in b for k in ["budget", "spent", "remaining", "percent"])

        # Pending approvals keys
        pa = data["pending_approvals"]
        assert all(k in pa for k in ["count", "urgent", "oldest_days"])

        # Alert structure
        for alert in data["alerts"]:
            assert "type" in alert
            assert "icon" in alert
            assert "title" in alert
            assert "message" in alert

    @patch("api.routes.dashboard.execute_query")
    @patch("api.routes.dashboard.execute_single")
    def test_demo_no_expiring_contract_alerts(self, mock_single, mock_query, test_client):
        """Demo session should not generate expiring contract alerts (deadlines removed)."""
        mock_single.side_effect = [{"spent": 1000}, {"cnt": 0, "urgent": 0, "oldest": 0}]
        mock_query.side_effect = [[], []]

        response = test_client.get(
            "/api/dashboard/summary",
            headers={"X-Session-ID": "demo"}
        )
        data = response.json()

        alert_titles = [a["title"] for a in data["alerts"]]
        assert not any("Expiring" in t for t in alert_titles)
