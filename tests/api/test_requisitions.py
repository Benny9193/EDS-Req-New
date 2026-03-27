"""
Tests for requisition management endpoints:
submit, list, get, items, update, cancel, approve, reject.
"""

import pytest
from unittest.mock import patch, MagicMock
from datetime import datetime


# ============================================
# Helpers
# ============================================

VALID_USER = {
    "UserId": 42,
    "SchoolId": 5,
    "DistrictId": 1,
    "ApprovalLevel": 0,
    "UserName": "Jane Doe",
}

APPROVER_USER = {
    "UserId": 10,
    "SchoolId": 5,
    "DistrictId": 1,
    "ApprovalLevel": 2,
    "UserName": "Admin User",
}

CROSS_DISTRICT_APPROVER = {
    "UserId": 20,
    "SchoolId": 8,
    "DistrictId": 99,
    "ApprovalLevel": 2,
    "UserName": "Other Admin",
}

SUBMIT_PAYLOAD = {
    "session_id": 101,
    "items": [
        {
            "item_id": "100",
            "quantity": 3,
            "unit_price": 9.99,
            "description": "Pencils #2",
            "vendor_item_code": "SSI-P12",
        },
        {
            "item_id": "200",
            "quantity": 1,
            "unit_price": 15.50,
            "description": "Notebook",
        },
    ],
    "notes": "Rush order",
    "shipping_location": "Room 101",
    "attention_to": "Ms. Smith",
}


def _mock_session(mock_func, user_info):
    """Configure get_user_from_session mock to return user_info."""
    mock_func.return_value = user_info


def _mock_session_invalid(mock_func):
    """Configure get_user_from_session mock to return None."""
    mock_func.return_value = None


# ============================================
# Submit Requisition Tests
# ============================================

class TestSubmitRequisition:
    """Test POST /api/requisitions/submit endpoint."""

    @patch("api.routes.requisitions.transaction")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_submit_success(self, mock_session, mock_txn, test_client):
        """Successful submission creates requisition and returns response."""
        _mock_session(mock_session, VALID_USER)

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_txn.return_value.__enter__ = MagicMock(return_value=(mock_conn, mock_cursor))
        mock_txn.return_value.__exit__ = MagicMock(return_value=False)

        # validate_item_exists returns True for all items
        mock_cursor.fetchone.side_effect = [
            (1,),  # item 100 exists
            (1,),  # item 200 exists
            MagicMock(**{"__getitem__": lambda s, i: "REQ-20250105-0001"}),  # req number
            (1000,),  # inserted requisition_id
        ]

        response = test_client.post("/api/requisitions/submit", json=SUBMIT_PAYLOAD)
        assert response.status_code == 200
        data = response.json()
        assert data["requisition_id"] == 1000
        assert data["item_count"] == 2
        assert data["status"] == "Pending Approval"
        # Total = (3 * 9.99) + (1 * 15.50) = 45.47
        assert abs(data["total_amount"] - 45.47) < 0.01

    @patch("api.routes.requisitions.get_user_from_session")
    def test_submit_invalid_session(self, mock_session, test_client):
        """Invalid session returns 401."""
        _mock_session_invalid(mock_session)

        response = test_client.post("/api/requisitions/submit", json=SUBMIT_PAYLOAD)
        assert response.status_code == 401

    @patch("api.routes.requisitions.transaction")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_submit_invalid_items(self, mock_session, mock_txn, test_client):
        """Non-existent item IDs return 400."""
        _mock_session(mock_session, VALID_USER)

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_txn.return_value.__enter__ = MagicMock(return_value=(mock_conn, mock_cursor))
        mock_txn.return_value.__exit__ = MagicMock(return_value=False)

        # First item exists, second doesn't
        mock_cursor.fetchone.side_effect = [
            (1,),   # item 100 exists
            None,   # item 200 does NOT exist
        ]

        response = test_client.post("/api/requisitions/submit", json=SUBMIT_PAYLOAD)
        assert response.status_code == 400
        detail = response.json()["detail"]
        assert detail["error_code"] == "INVALID_ITEMS"

    def test_submit_empty_items(self, test_client):
        """Empty items list returns 422 (Pydantic validation)."""
        response = test_client.post("/api/requisitions/submit", json={
            "session_id": 101,
            "items": [],
        })
        assert response.status_code == 422

    def test_submit_missing_session(self, test_client):
        """Missing session_id returns 422."""
        response = test_client.post("/api/requisitions/submit", json={
            "items": [{"item_id": "1", "quantity": 1, "unit_price": 5.0}],
        })
        assert response.status_code == 422


# ============================================
# List Requisitions Tests
# ============================================

class TestListRequisitions:
    """Test GET /api/requisitions endpoint."""

    @patch("api.routes.requisitions.execute_query")
    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_list_success(self, mock_session, mock_single, mock_query, test_client):
        """Returns paginated list of requisitions."""
        _mock_session(mock_session, VALID_USER)

        # First call: count query
        mock_single.return_value = {"total": 2}
        mock_query.side_effect = [
            # status counts
            [{"StatusId": 2, "cnt": 1}, {"StatusId": 3, "cnt": 1}],
            # paginated results
            [
                {
                    "RequisitionId": 1,
                    "RequisitionNumber": "REQ-20250101-0001",
                    "StatusId": 2,
                    "StatusName": "Pending Approval",
                    "TotalRequisitionCost": 45.47,
                    "DateEntered": datetime(2025, 1, 1, 9, 0),
                    "Comments": "Rush order",
                    "ItemCount": 2,
                },
                {
                    "RequisitionId": 2,
                    "RequisitionNumber": "REQ-20250102-0001",
                    "StatusId": 3,
                    "StatusName": "Approved",
                    "TotalRequisitionCost": 12.00,
                    "DateEntered": datetime(2025, 1, 2, 10, 0),
                    "Comments": None,
                    "ItemCount": 1,
                },
            ],
        ]

        response = test_client.get("/api/requisitions?session_id=101")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 2
        assert len(data["items"]) == 2
        assert data["items"][0]["requisition_number"] == "REQ-20250101-0001"
        assert data["status_counts"]["Pending Approval"] == 1

    @patch("api.routes.requisitions.get_user_from_session")
    def test_list_invalid_session(self, mock_session, test_client):
        """Invalid session returns 401."""
        _mock_session_invalid(mock_session)
        response = test_client.get("/api/requisitions?session_id=999")
        assert response.status_code == 401

    def test_list_missing_session(self, test_client):
        """Missing session_id returns 422."""
        response = test_client.get("/api/requisitions")
        assert response.status_code == 422


# ============================================
# Get Requisition Details Tests
# ============================================

class TestGetRequisition:
    """Test GET /api/requisitions/{id} endpoint."""

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_get_success(self, mock_session, mock_single, test_client):
        """Returns requisition header details."""
        _mock_session(mock_session, VALID_USER)
        mock_single.return_value = {
            "RequisitionId": 1,
            "RequisitionNumber": "REQ-20250101-0001",
            "UserId": 42,
            "StatusId": 2,
            "StatusName": "Pending Approval",
            "DateEntered": datetime(2025, 1, 1, 9, 0),
            "TotalRequisitionCost": 45.47,
            "Comments": "Rush order",
        }

        response = test_client.get("/api/requisitions/1?session_id=101")
        assert response.status_code == 200
        data = response.json()
        assert data["requisition_id"] == 1
        assert data["status"] == "Pending Approval"

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_get_not_found(self, mock_session, mock_single, test_client):
        """Non-existent requisition returns 404."""
        _mock_session(mock_session, VALID_USER)
        mock_single.return_value = None

        response = test_client.get("/api/requisitions/999?session_id=101")
        assert response.status_code == 404

    @patch("api.routes.requisitions.get_user_from_session")
    def test_get_invalid_session(self, mock_session, test_client):
        """Invalid session returns 401."""
        _mock_session_invalid(mock_session)
        response = test_client.get("/api/requisitions/1?session_id=999")
        assert response.status_code == 401


# ============================================
# Get Requisition Line Items Tests
# ============================================

class TestGetRequisitionItems:
    """Test GET /api/requisitions/{id}/items endpoint."""

    @patch("api.routes.requisitions.execute_query")
    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_items_success(self, mock_session, mock_single, mock_query, test_client):
        """Returns line items with product details."""
        _mock_session(mock_session, VALID_USER)
        # Ownership check
        mock_single.return_value = {"1": 1}
        # Line items
        mock_query.return_value = [
            {
                "LineId": 1,
                "ItemId": 100,
                "ProductName": "Pencils #2",
                "SKU": "SSI-P12",
                "Vendor": "School Supplies Inc",
                "Quantity": 3,
                "UnitPrice": 9.99,
                "ExtendedPrice": 29.97,
            }
        ]

        response = test_client.get("/api/requisitions/1/items?session_id=101")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 1
        assert data[0]["product_name"] == "Pencils #2"
        assert data[0]["extended_price"] == 29.97

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_items_not_owned(self, mock_session, mock_single, test_client):
        """Requisition not owned by user returns 404."""
        _mock_session(mock_session, VALID_USER)
        mock_single.return_value = None  # ownership check fails

        response = test_client.get("/api/requisitions/999/items?session_id=101")
        assert response.status_code == 404


# ============================================
# Update Requisition Tests
# ============================================

class TestUpdateRequisition:
    """Test PUT /api/requisitions/{id} endpoint."""

    @patch("api.routes.requisitions.transaction")
    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_update_submitted(self, mock_session, mock_single, mock_txn, test_client):
        """Update notes on Pending Approval requisition succeeds."""
        _mock_session(mock_session, VALID_USER)
        mock_single.return_value = {"RequisitionId": 1, "StatusId": 2}  # Pending Approval

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_txn.return_value.__enter__ = MagicMock(return_value=(mock_conn, mock_cursor))
        mock_txn.return_value.__exit__ = MagicMock(return_value=False)

        response = test_client.put(
            "/api/requisitions/1?session_id=101",
            json={"notes": "Updated notes"}
        )
        assert response.status_code == 200
        assert "updated" in response.json()["message"].lower()

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_update_approved_fails(self, mock_session, mock_single, test_client):
        """Cannot update an Approved requisition."""
        _mock_session(mock_session, VALID_USER)
        mock_single.return_value = {"RequisitionId": 1, "StatusId": 3}  # Approved

        response = test_client.put(
            "/api/requisitions/1?session_id=101",
            json={"notes": "Try to update"}
        )
        assert response.status_code == 400
        assert response.json()["detail"]["error_code"] == "INVALID_STATUS"

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_update_not_found(self, mock_session, mock_single, test_client):
        """Update non-existent requisition returns 404."""
        _mock_session(mock_session, VALID_USER)
        mock_single.return_value = None

        response = test_client.put(
            "/api/requisitions/999?session_id=101",
            json={"notes": "Notes"}
        )
        assert response.status_code == 404


# ============================================
# Cancel Requisition Tests
# ============================================

class TestCancelRequisition:
    """Test DELETE /api/requisitions/{id} endpoint."""

    @patch("api.routes.requisitions.transaction")
    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_cancel_submitted(self, mock_session, mock_single, mock_txn, test_client):
        """Cancel a Pending Approval requisition succeeds."""
        _mock_session(mock_session, VALID_USER)
        mock_single.return_value = {
            "RequisitionId": 1,
            "RequisitionNumber": "REQ-20250101-0001",
            "StatusId": 2,  # Pending Approval
        }

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_txn.return_value.__enter__ = MagicMock(return_value=(mock_conn, mock_cursor))
        mock_txn.return_value.__exit__ = MagicMock(return_value=False)

        response = test_client.delete("/api/requisitions/1?session_id=101&reason=No+longer+needed")
        assert response.status_code == 200
        data = response.json()
        assert "cancelled" in data["message"].lower()

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_cancel_approved_fails(self, mock_session, mock_single, test_client):
        """Cannot cancel an Approved requisition."""
        _mock_session(mock_session, VALID_USER)
        mock_single.return_value = {
            "RequisitionId": 1,
            "RequisitionNumber": "REQ-20250101-0001",
            "StatusId": 3,  # Approved
        }

        response = test_client.delete("/api/requisitions/1?session_id=101")
        assert response.status_code == 400
        assert response.json()["detail"]["error_code"] == "INVALID_STATUS"

    @patch("api.routes.requisitions.get_user_from_session")
    def test_cancel_invalid_session(self, mock_session, test_client):
        """Invalid session returns 401."""
        _mock_session_invalid(mock_session)
        response = test_client.delete("/api/requisitions/1?session_id=999")
        assert response.status_code == 401


# ============================================
# List Pending Approvals Tests
# ============================================

class TestListPendingApprovals:
    """Test GET /api/requisitions/pending/list endpoint."""

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.execute_query")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_pending_list_approver(self, mock_session, mock_query, mock_single, test_client):
        """Approver sees pending requisitions in their district."""
        _mock_session(mock_session, APPROVER_USER)
        mock_query.return_value = [
            {
                "RequisitionId": 1,
                "RequisitionNumber": "REQ-20250101-0001",
                "StatusId": 2,
                "StatusName": "Pending Approval",
                "TotalRequisitionCost": 45.47,
                "DateEntered": datetime(2025, 1, 1, 9, 0),
                "Comments": "Rush",
                "SubmittedBy": "Jane Doe",
                "ItemCount": 2,
            }
        ]
        mock_single.return_value = {"total": 1}

        response = test_client.get("/api/requisitions/pending/list?session_id=101")
        assert response.status_code == 200
        data = response.json()
        assert data["total"] == 1
        assert data["items"][0]["submitted_by"] == "Jane Doe"

    @patch("api.routes.requisitions.get_user_from_session")
    def test_pending_list_no_approval_rights(self, mock_session, test_client):
        """User without approval rights gets 403."""
        _mock_session(mock_session, VALID_USER)  # ApprovalLevel=0

        response = test_client.get("/api/requisitions/pending/list?session_id=101")
        assert response.status_code == 403
        assert response.json()["detail"]["error_code"] == "NO_APPROVAL_RIGHTS"

    @patch("api.routes.requisitions.get_user_from_session")
    def test_pending_list_invalid_session(self, mock_session, test_client):
        """Invalid session returns 401."""
        _mock_session_invalid(mock_session)
        response = test_client.get("/api/requisitions/pending/list?session_id=999")
        assert response.status_code == 401


# ============================================
# Approve Requisition Tests
# ============================================

class TestApproveRequisition:
    """Test POST /api/requisitions/{id}/approve endpoint."""

    @patch("api.routes.requisitions.transaction")
    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_approve_success(self, mock_session, mock_single, mock_txn, test_client):
        """Approver in same district can approve a Pending Approval requisition."""
        _mock_session(mock_session, APPROVER_USER)
        mock_single.return_value = {
            "RequisitionId": 1,
            "RequisitionNumber": "REQ-20250101-0001",
            "StatusId": 2,  # Pending Approval
            "DistrictId": 1,  # same as APPROVER_USER
            "TotalRequisitionCost": 45.47,
        }

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_txn.return_value.__enter__ = MagicMock(return_value=(mock_conn, mock_cursor))
        mock_txn.return_value.__exit__ = MagicMock(return_value=False)

        response = test_client.post("/api/requisitions/1/approve", json={
            "session_id": 101,
            "comments": "Looks good",
        })
        assert response.status_code == 200
        data = response.json()
        assert data["new_status"] == "Approved"

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_approve_cross_district(self, mock_session, mock_single, test_client):
        """Cannot approve requisition from different district."""
        _mock_session(mock_session, CROSS_DISTRICT_APPROVER)
        mock_single.return_value = {
            "RequisitionId": 1,
            "RequisitionNumber": "REQ-20250101-0001",
            "StatusId": 2,
            "DistrictId": 1,  # different from CROSS_DISTRICT_APPROVER (99)
            "TotalRequisitionCost": 45.47,
        }

        response = test_client.post("/api/requisitions/1/approve", json={
            "session_id": 101,
        })
        assert response.status_code == 403
        assert response.json()["detail"]["error_code"] == "CROSS_DISTRICT"

    @patch("api.routes.requisitions.get_user_from_session")
    def test_approve_no_rights(self, mock_session, test_client):
        """User without approval rights gets 403."""
        _mock_session(mock_session, VALID_USER)  # ApprovalLevel=0

        response = test_client.post("/api/requisitions/1/approve", json={
            "session_id": 101,
        })
        assert response.status_code == 403

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_approve_already_approved(self, mock_session, mock_single, test_client):
        """Cannot approve an already-Approved requisition."""
        _mock_session(mock_session, APPROVER_USER)
        mock_single.return_value = {
            "RequisitionId": 1,
            "RequisitionNumber": "REQ-20250101-0001",
            "StatusId": 3,  # Approved
            "DistrictId": 1,
            "TotalRequisitionCost": 45.47,
        }

        response = test_client.post("/api/requisitions/1/approve", json={
            "session_id": 101,
        })
        assert response.status_code == 400

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_approve_not_found(self, mock_session, mock_single, test_client):
        """Approve non-existent requisition returns 404."""
        _mock_session(mock_session, APPROVER_USER)
        mock_single.return_value = None

        response = test_client.post("/api/requisitions/1/approve", json={
            "session_id": 101,
        })
        assert response.status_code == 404


# ============================================
# Reject Requisition Tests
# ============================================

class TestRejectRequisition:
    """Test POST /api/requisitions/{id}/reject endpoint."""

    @patch("api.routes.requisitions.transaction")
    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_reject_success(self, mock_session, mock_single, mock_txn, test_client):
        """Approver can reject a Pending Approval requisition with reason."""
        _mock_session(mock_session, APPROVER_USER)
        mock_single.return_value = {
            "RequisitionId": 1,
            "RequisitionNumber": "REQ-20250101-0001",
            "StatusId": 2,  # Pending Approval
            "DistrictId": 1,
        }

        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_txn.return_value.__enter__ = MagicMock(return_value=(mock_conn, mock_cursor))
        mock_txn.return_value.__exit__ = MagicMock(return_value=False)

        response = test_client.post("/api/requisitions/1/reject", json={
            "session_id": 101,
            "reason": "Budget exceeded for this quarter - please resubmit next month",
        })
        assert response.status_code == 200
        data = response.json()
        assert data["new_status"] == "Rejected"

    @patch("api.routes.requisitions.get_user_from_session")
    def test_reject_no_rights(self, mock_session, test_client):
        """User without approval rights gets 403."""
        _mock_session(mock_session, VALID_USER)

        response = test_client.post("/api/requisitions/1/reject", json={
            "session_id": 101,
            "reason": "Not needed anymore - at least 10 chars",
        })
        assert response.status_code == 403

    def test_reject_reason_too_short(self, test_client):
        """Rejection reason under 10 chars returns 422."""
        response = test_client.post("/api/requisitions/1/reject", json={
            "session_id": 101,
            "reason": "No",  # min_length=10
        })
        assert response.status_code == 422

    def test_reject_missing_reason(self, test_client):
        """Missing rejection reason returns 422."""
        response = test_client.post("/api/requisitions/1/reject", json={
            "session_id": 101,
        })
        assert response.status_code == 422

    @patch("api.routes.requisitions.execute_single")
    @patch("api.routes.requisitions.get_user_from_session")
    def test_reject_cross_district(self, mock_session, mock_single, test_client):
        """Cannot reject requisition from different district."""
        _mock_session(mock_session, CROSS_DISTRICT_APPROVER)
        mock_single.return_value = {
            "RequisitionId": 1,
            "RequisitionNumber": "REQ-20250101-0001",
            "StatusId": 2,  # Pending Approval
            "DistrictId": 1,  # different district
        }

        response = test_client.post("/api/requisitions/1/reject", json={
            "session_id": 101,
            "reason": "Budget exceeded for this period, please resubmit",
        })
        assert response.status_code == 403
        assert response.json()["detail"]["error_code"] == "CROSS_DISTRICT"
