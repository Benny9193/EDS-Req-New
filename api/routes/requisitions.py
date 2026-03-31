"""
Requisition management endpoints for EDS Universal Requisition.
Handles cart checkout, order submission, listing, and approval workflow.
"""

from fastapi import APIRouter, HTTPException, status, Query
from fastapi.responses import JSONResponse
from typing import Optional, List
from datetime import datetime
import logging
import math

from api.database import get_db_cursor, execute_single, execute_query, transaction
from api.middleware import SESSION_TIMEOUT_HOURS
import re
from api.routes.reports import invalidate_reports_cache
from api.models import (
    RequisitionSubmission,
    RequisitionResponse,
    RequisitionStatus,
    RequisitionListResponse,
    RequisitionListItem,
    RequisitionDetail,
    RequisitionLineItem,
    RequisitionUpdate,
    RequisitionApproval,
    RequisitionRejection,
    APIError
)

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/requisitions", tags=["Requisitions"])

# StatusId values from StatusTable — these are the integers stored in Requisitions.StatusId
STATUS_ON_HOLD = 1          # H - On Hold
STATUS_PENDING_APPROVAL = 2 # P - Pending Approval
STATUS_APPROVED = 3         # A - Approved
STATUS_REJECTED = 4         # R - Rejected
STATUS_AT_EDS = 5           # I - At EDS

# Map StatusId → display name (for API responses)
STATUS_NAMES = {
    None: "Draft",
    1: "On Hold",
    2: "Pending Approval",
    3: "Approved",
    4: "Rejected",
    5: "At EDS",
    6: "PO Printed",
}

# Map display name → StatusId (for filtering)
STATUS_IDS = {v: k for k, v in STATUS_NAMES.items()}


# ===========================================
# HELPER FUNCTIONS
# ===========================================

def get_user_from_session(session_id: int) -> Optional[dict]:
    """
    Validate session and return user info.
    Returns None if session is invalid or expired.
    """
    result = execute_single("""
        SELECT
            s.UserId,
            s.SchoolId,
            s.DistrictId,
            s.ApprovalLevel,
            u.UserName
        FROM SessionTable s
        LEFT JOIN Users u ON s.UserId = u.UserId
        WHERE s.SessionId = ?
        AND s.SessionEnd IS NULL
        AND DATEDIFF(HOUR, s.SessionStart, GETDATE()) < ?
    """, (session_id, SESSION_TIMEOUT_HOURS))
    return result


def validate_item_exists(cursor, item_id: int) -> bool:
    """Check if an ItemId exists in the Items table."""
    cursor.execute("SELECT 1 FROM Items WHERE ItemId = ?", (item_id,))
    return cursor.fetchone() is not None


def raise_api_error(status_code: int, error_code: str, message: str, details: dict = None):
    """Raise HTTPException with standardized error format."""
    raise HTTPException(
        status_code=status_code,
        detail={
            "error_code": error_code,
            "message": message,
            "details": details or {}
        }
    )


# ===========================================
# SUBMIT REQUISITION
# ===========================================

@router.post("/submit", response_model=RequisitionResponse)
async def submit_requisition(request: RequisitionSubmission):
    """
    Submit a requisition from the shopping cart.

    Creates a requisition header and detail records in the database
    within a transaction. Validates all item IDs exist before insertion.
    Requires a valid, non-expired session.
    """
    # Validate session
    user_info = get_user_from_session(request.session_id)
    if not user_info:
        logger.warning("Invalid session for requisition: %s", request.session_id)
        raise_api_error(
            status.HTTP_401_UNAUTHORIZED,
            "SESSION_INVALID",
            "Invalid or expired session"
        )

    try:
        with transaction() as (conn, cursor):
            # Validate all item IDs exist
            invalid_items = []
            for item in request.items:
                item_id = int(item.item_id)
                if not validate_item_exists(cursor, item_id):
                    invalid_items.append(item.item_id)

            if invalid_items:
                raise_api_error(
                    status.HTTP_400_BAD_REQUEST,
                    "INVALID_ITEMS",
                    f"The following item IDs do not exist: {', '.join(invalid_items)}",
                    {"invalid_item_ids": invalid_items}
                )

            # Calculate total amount
            total_amount = sum(
                item.quantity * item.unit_price
                for item in request.items
            )

            # Generate requisition number
            # Format: REQ-YYYYMMDD-NNNN where NNNN is sequential
            cursor.execute("""
                SELECT 'REQ-' + FORMAT(GETDATE(), 'yyyyMMdd') + '-' +
                       RIGHT('0000' + CAST(
                           ISNULL(
                               (SELECT MAX(CAST(RIGHT(RequisitionNumber, 4) AS INT)) + 1
                                FROM Requisitions
                                WHERE RequisitionNumber LIKE 'REQ-' + FORMAT(GETDATE(), 'yyyyMMdd') + '-%'),
                               1
                           ) AS VARCHAR
                       ), 4) AS ReqNumber
            """)
            row = cursor.fetchone()
            req_number = row[0] if row else f"REQ-{datetime.now().strftime('%Y%m%d%H%M%S')}"

            # Build notes with shipping info
            full_notes = request.notes or ""
            if request.shipping_location:
                full_notes += f"\nShipping: {request.shipping_location}"
            if request.attention_to:
                full_notes += f"\nAttention: {request.attention_to}"
            if request.delivery_preference:
                full_notes += f"\nDelivery: {request.delivery_preference}"

            # Insert requisition header
            cursor.execute("""
                INSERT INTO Requisitions (
                    Active,
                    RequisitionNumber,
                    UserId,
                    SchoolId,
                    DateEntered,
                    StatusId,
                    TotalRequisitionCost,
                    TotalItemsCost,
                    Comments,
                    ApprovalRequired,
                    DateUpdated
                )
                OUTPUT INSERTED.RequisitionId
                VALUES (1, ?, ?, ?, GETDATE(), ?, ?, ?, ?, 1, GETDATE())
            """, (
                req_number,
                user_info['UserId'],
                user_info.get('SchoolId'),
                STATUS_PENDING_APPROVAL,
                total_amount,
                total_amount,
                full_notes.strip() if full_notes else None
            ))

            result = cursor.fetchone()
            if not result:
                raise Exception("Failed to create requisition header")

            requisition_id = result[0]

            # Insert detail lines
            for item in request.items:
                cursor.execute("""
                    INSERT INTO Detail (
                        RequisitionId,
                        ItemId,
                        Quantity,
                        CatalogPrice,
                        Description,
                        VendorItemCode,
                        ItemCode
                    )
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (
                    requisition_id,
                    int(item.item_id),
                    item.quantity,
                    item.unit_price,
                    item.description,
                    item.vendor_item_code,
                    item.item_id
                ))

            # Transaction commits automatically on context exit

            logger.info(
                "Requisition %s created: %d items, $%.2f, user=%s",
                req_number, len(request.items), total_amount, user_info['UserId'],
            )

            # Invalidate reports cache for this district
            invalidate_reports_cache(user_info.get('DistrictId'))

            return RequisitionResponse(
                requisition_id=requisition_id,
                requisition_number=req_number,
                status="Pending Approval",
                total_amount=total_amount,
                item_count=len(request.items),
                created_at=datetime.now().isoformat()
            )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Requisition submission error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "SUBMISSION_FAILED",
            "Failed to submit requisition. Please try again."
        )


# ===========================================
# LIST REQUISITIONS
# ===========================================

@router.get("", response_model=RequisitionListResponse)
async def list_requisitions(
    session_id: str = Query(..., description="User's session ID"),
    status_filter: Optional[str] = Query(None, alias="status", description="Filter by status"),
    search: Optional[str] = Query(None, description="Search in requisition number or notes"),
    date_from: Optional[str] = Query(None, description="Filter from date (YYYY-MM-DD)"),
    date_to: Optional[str] = Query(None, description="Filter to date (YYYY-MM-DD)"),
    sort_by: str = Query("created_at", description="Sort field: created_at, total_amount, status"),
    sort_order: str = Query("desc", description="Sort order: asc, desc"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page")
):
    """
    List requisitions for the authenticated user.

    Supports filtering by status, date range, and search query.
    Returns paginated results with status counts.
    """
    # Validate session (demo mode shows all data across users)
    is_demo = session_id == 'demo'
    if not is_demo:
        try:
            sid = int(session_id)
        except (ValueError, TypeError):
            raise_api_error(status.HTTP_401_UNAUTHORIZED, "SESSION_INVALID", "Invalid session")

        user_info = get_user_from_session(sid)
        if not user_info:
            raise_api_error(
                status.HTTP_401_UNAUTHORIZED,
                "SESSION_INVALID",
                "Invalid or expired session"
            )

    try:
        # Build WHERE clause
        where_clauses = ["r.Active = 1"]
        params = []
        if is_demo:
            # Demo mode: show orders with known statuses for a meaningful view
            where_clauses.append("r.StatusId IN (1,2,3,4,5,6)")
        else:
            where_clauses.append("r.UserId = ?")
            params.append(user_info['UserId'])

        if status_filter:
            # Convert display name to StatusId
            filter_id = STATUS_IDS.get(status_filter)
            if filter_id:
                where_clauses.append("r.StatusId = ?")
                params.append(filter_id)

        if search:
            where_clauses.append("(r.RequisitionNumber LIKE ? OR r.Comments LIKE ?)")
            search_pattern = f"%{search}%"
            params.extend([search_pattern, search_pattern])

        if date_from:
            where_clauses.append("r.DateEntered >= ?")
            params.append(date_from)

        if date_to:
            where_clauses.append("r.DateEntered <= ?")
            params.append(date_to + " 23:59:59")

        where_sql = " AND ".join(where_clauses)

        # Validate sort field
        valid_sort_fields = {
            "created_at": "r.DateEntered",
            "total_amount": "r.TotalRequisitionCost",
            "status": "r.StatusId",
            "requisition_number": "r.RequisitionNumber"
        }
        sort_field = valid_sort_fields.get(sort_by, "r.DateEntered")
        sort_dir = "DESC" if sort_order.lower() == "desc" else "ASC"

        # Get total count
        count_query = f"""
            SELECT COUNT(*) as total
            FROM Requisitions r
            WHERE {where_sql}
        """
        count_result = execute_single(count_query, tuple(params))
        total = count_result['total'] if count_result else 0
        total_pages = math.ceil(total / page_size) if total > 0 else 1

        # Get status counts
        if is_demo:
            status_query = """
                SELECT r.StatusId, COUNT(*) as cnt
                FROM Requisitions r
                WHERE r.Active = 1
                GROUP BY r.StatusId
            """
            status_results = execute_query(status_query)
        else:
            status_query = """
                SELECT r.StatusId, COUNT(*) as cnt
                FROM Requisitions r
                WHERE r.UserId = ? AND r.Active = 1
                GROUP BY r.StatusId
            """
            status_results = execute_query(status_query, (user_info['UserId'],))
        status_counts = {STATUS_NAMES.get(row['StatusId'], str(row['StatusId'])): row['cnt'] for row in status_results}

        # Get paginated results with item counts
        offset = (page - 1) * page_size
        list_query = f"""
            SELECT
                r.RequisitionId,
                r.RequisitionNumber,
                r.StatusId,
                st.Name as StatusName,
                r.TotalRequisitionCost,
                r.DateEntered,
                r.Comments,
                (SELECT COUNT(*) FROM Detail d WHERE d.RequisitionId = r.RequisitionId) as ItemCount
            FROM Requisitions r
            LEFT JOIN StatusTable st ON r.StatusId = st.StatusId
            WHERE {where_sql}
            ORDER BY {sort_field} {sort_dir}
            OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
        """
        params.extend([offset, page_size])
        results = execute_query(list_query, tuple(params))

        items = [
            RequisitionListItem(
                requisition_id=row['RequisitionId'],
                requisition_number=row['RequisitionNumber'],
                status=row['StatusName'] or STATUS_NAMES.get(row['StatusId'], 'Draft'),
                total_amount=float(row['TotalRequisitionCost'] or 0),
                item_count=row['ItemCount'] or 0,
                created_at=row['DateEntered'],
                notes_preview=row['Comments'][:100] if row.get('Comments') else None
            )
            for row in results
        ]

        return RequisitionListResponse(
            items=items,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
            status_counts=status_counts
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("List requisitions error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "LIST_FAILED",
            "Failed to retrieve requisitions"
        )


# ===========================================
# GET REQUISITION DETAILS
# ===========================================

@router.get("/{requisition_id}")
async def get_requisition(requisition_id: int, session_id: str = Query(...)):
    """
    Get requisition header details by ID.
    Requires session_id for authorization.
    """
    # Validate session (demo mode shows data without user filter)
    is_demo = session_id == 'demo'
    if not is_demo:
        try:
            sid = int(session_id)
        except (ValueError, TypeError):
            raise_api_error(status.HTTP_401_UNAUTHORIZED, "SESSION_INVALID", "Invalid session")

        user_info = get_user_from_session(sid)
        if not user_info:
            raise_api_error(
                status.HTTP_401_UNAUTHORIZED,
                "SESSION_INVALID",
                "Invalid or expired session"
            )

    try:
        # Get requisition header
        if is_demo:
            result = execute_single("""
                SELECT
                    r.RequisitionId,
                    r.RequisitionNumber,
                    r.UserId,
                    r.StatusId,
                    st.Name as StatusName,
                    r.DateEntered,
                    r.TotalRequisitionCost,
                    r.Comments
                FROM Requisitions r
                LEFT JOIN StatusTable st ON r.StatusId = st.StatusId
                WHERE r.RequisitionId = ?
            """, (requisition_id,))
        else:
            result = execute_single("""
                SELECT
                    r.RequisitionId,
                    r.RequisitionNumber,
                    r.UserId,
                    r.StatusId,
                    st.Name as StatusName,
                    r.DateEntered,
                    r.TotalRequisitionCost,
                    r.Comments
                FROM Requisitions r
                LEFT JOIN StatusTable st ON r.StatusId = st.StatusId
                WHERE r.RequisitionId = ?
                AND r.UserId = ?
            """, (requisition_id, user_info['UserId']))

        if not result:
            raise_api_error(
                status.HTTP_404_NOT_FOUND,
                "NOT_FOUND",
                "Requisition not found"
            )

        return {
            "requisition_id": result['RequisitionId'],
            "requisition_number": result['RequisitionNumber'],
            "status": result['StatusName'] or STATUS_NAMES.get(result['StatusId'], 'Draft'),
            "total_amount": float(result['TotalRequisitionCost'] or 0),
            "notes": result.get('Comments'),
            "created_at": result['DateEntered'].isoformat() if result.get('DateEntered') else None
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Get requisition error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "RETRIEVAL_FAILED",
            "Failed to get requisition"
        )


# ===========================================
# GET REQUISITION LINE ITEMS
# ===========================================

@router.get("/{requisition_id}/items", response_model=List[RequisitionLineItem])
async def get_requisition_items(requisition_id: int, session_id: str = Query(...)):
    """
    Get line items for a requisition.
    Includes product details joined from Items table.
    """
    # Validate session (demo mode skips ownership check)
    is_demo = session_id == 'demo'
    if not is_demo:
        try:
            sid = int(session_id)
        except (ValueError, TypeError):
            raise_api_error(status.HTTP_401_UNAUTHORIZED, "SESSION_INVALID", "Invalid session")

        user_info = get_user_from_session(sid)
        if not user_info:
            raise_api_error(
                status.HTTP_401_UNAUTHORIZED,
                "SESSION_INVALID",
                "Invalid or expired session"
            )

    try:
        if not is_demo:
            # Verify user owns this requisition OR user is an approver in the same district
            approval_level = user_info.get('ApprovalLevel', 0)
            if approval_level >= 1:
                ownership = execute_single("""
                    SELECT 1 FROM Requisitions r
                    JOIN School sc ON r.SchoolId = sc.SchoolId
                    WHERE r.RequisitionId = ?
                    AND sc.DistrictId = ?
                """, (requisition_id, user_info['DistrictId']))
            else:
                ownership = execute_single("""
                    SELECT 1 FROM Requisitions
                    WHERE RequisitionId = ? AND UserId = ?
                """, (requisition_id, user_info['UserId']))

            if not ownership:
                raise_api_error(
                    status.HTTP_404_NOT_FOUND,
                    "NOT_FOUND",
                    "Requisition not found"
                )
        else:
            # Demo mode — just verify the requisition exists
            ownership = execute_single("""
                SELECT 1 FROM Requisitions WHERE RequisitionId = ?
            """, (requisition_id,))
            if not ownership:
                raise_api_error(
                    status.HTTP_404_NOT_FOUND,
                    "NOT_FOUND",
                    "Requisition not found"
                )

        # Get line items with product info
        items = execute_query("""
            SELECT
                d.DetailId as LineId,
                d.ItemId,
                COALESCE(i.Description, d.Description, 'Unknown Item') as ProductName,
                COALESCE(d.VendorItemCode, i.VendorPartNumber, d.ItemCode, '') as SKU,
                COALESCE(v.Name, '') as Vendor,
                d.Quantity,
                COALESCE(d.BidPrice, d.CatalogPrice, d.GrossPrice, 0) as UnitPrice,
                d.Quantity * COALESCE(d.BidPrice, d.CatalogPrice, d.GrossPrice, 0) as ExtendedPrice
            FROM Detail d
            LEFT JOIN Items i ON d.ItemId = i.ItemId
            LEFT JOIN Vendors v ON d.VendorId = v.VendorId
            WHERE d.RequisitionId = ?
            ORDER BY d.DetailId
        """, (requisition_id,))

        return [
            RequisitionLineItem(
                line_id=item['LineId'],
                item_id=item['ItemId'],
                product_name=item['ProductName'],
                sku=item['SKU'],
                vendor=item['Vendor'],
                quantity=item['Quantity'] or 1,
                unit_price=float(item['UnitPrice'] or 0),
                extended_price=float(item['ExtendedPrice'] or 0)
            )
            for item in items
        ]

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Get requisition items error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "RETRIEVAL_FAILED",
            "Failed to get requisition items"
        )


# ===========================================
# UPDATE REQUISITION
# ===========================================

@router.put("/{requisition_id}")
async def update_requisition(
    requisition_id: int,
    session_id: str = Query(...),
    update: RequisitionUpdate = None
):
    """
    Update a requisition's notes or shipping info.
    Only allowed when status is On Hold or Pending Approval.
    """
    if session_id == 'demo':
        raise_api_error(status.HTTP_403_FORBIDDEN, "DEMO_READ_ONLY", "Demo mode is read-only. Log in to modify requisitions.")

    # Validate session
    try:
        sid = int(session_id)
    except (ValueError, TypeError):
        raise_api_error(status.HTTP_401_UNAUTHORIZED, "SESSION_INVALID", "Invalid session")

    user_info = get_user_from_session(sid)
    if not user_info:
        raise_api_error(
            status.HTTP_401_UNAUTHORIZED,
            "SESSION_INVALID",
            "Invalid or expired session"
        )

    try:
        # Get current requisition
        current = execute_single("""
            SELECT RequisitionId, StatusId
            FROM Requisitions
            WHERE RequisitionId = ? AND UserId = ?
        """, (requisition_id, user_info['UserId']))

        if not current:
            raise_api_error(
                status.HTTP_404_NOT_FOUND,
                "NOT_FOUND",
                "Requisition not found"
            )

        current_status_id = current['StatusId']
        # Allow updates when On Hold or Pending Approval
        if current_status_id not in (STATUS_ON_HOLD, STATUS_PENDING_APPROVAL):
            status_name = STATUS_NAMES.get(current_status_id, str(current_status_id))
            raise_api_error(
                status.HTTP_400_BAD_REQUEST,
                "INVALID_STATUS",
                f"Cannot update requisition with status '{status_name}'",
                {"current_status": status_name, "allowed_statuses": ["On Hold", "Pending Approval"]}
            )

        # Build update query
        update_fields = ["DateUpdated = GETDATE()"]
        params = []

        if update.notes is not None:
            update_fields.append("Comments = ?")
            params.append(update.notes)

        if not update_fields:
            raise_api_error(
                status.HTTP_400_BAD_REQUEST,
                "NO_UPDATES",
                "No fields to update"
            )

        params.append(requisition_id)

        with transaction() as (conn, cursor):
            cursor.execute(f"""
                UPDATE Requisitions
                SET {', '.join(update_fields)}
                WHERE RequisitionId = ?
            """, tuple(params))

        logger.info("Requisition %s updated by user %s", requisition_id, user_info['UserId'])

        return {"message": "Requisition updated successfully", "requisition_id": requisition_id}

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Update requisition error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "UPDATE_FAILED",
            "Failed to update requisition"
        )


# ===========================================
# CANCEL REQUISITION
# ===========================================

@router.delete("/{requisition_id}")
async def cancel_requisition(
    requisition_id: int,
    session_id: str = Query(...),
    reason: Optional[str] = Query(None, max_length=500, description="Cancellation reason")
):
    """
    Cancel a requisition.
    Only allowed when status is On Hold or Pending Approval.
    """
    if session_id == 'demo':
        raise_api_error(status.HTTP_403_FORBIDDEN, "DEMO_READ_ONLY", "Demo mode is read-only. Log in to modify requisitions.")

    # Validate session
    try:
        sid = int(session_id)
    except (ValueError, TypeError):
        raise_api_error(status.HTTP_401_UNAUTHORIZED, "SESSION_INVALID", "Invalid session")

    user_info = get_user_from_session(sid)
    if not user_info:
        raise_api_error(
            status.HTTP_401_UNAUTHORIZED,
            "SESSION_INVALID",
            "Invalid or expired session"
        )

    try:
        # Get current requisition
        current = execute_single("""
            SELECT RequisitionId, RequisitionNumber, StatusId
            FROM Requisitions
            WHERE RequisitionId = ? AND UserId = ?
        """, (requisition_id, user_info['UserId']))

        if not current:
            raise_api_error(
                status.HTTP_404_NOT_FOUND,
                "NOT_FOUND",
                "Requisition not found"
            )

        current_status_id = current['StatusId']
        # Allow cancel when On Hold or Pending Approval
        if current_status_id not in (STATUS_ON_HOLD, STATUS_PENDING_APPROVAL):
            status_name = STATUS_NAMES.get(current_status_id, str(current_status_id))
            raise_api_error(
                status.HTTP_400_BAD_REQUEST,
                "INVALID_STATUS",
                f"Cannot cancel requisition with status '{status_name}'",
                {"current_status": status_name, "allowed_statuses": ["On Hold", "Pending Approval"]}
            )

        # Deactivate the requisition (soft delete)
        with transaction() as (conn, cursor):
            cursor.execute("""
                UPDATE Requisitions
                SET Active = 0,
                    Comments = COALESCE(Comments, '') + ?,
                    DateUpdated = GETDATE()
                WHERE RequisitionId = ?
            """, (
                f"\n\n[Cancelled: {reason or 'No reason provided'}]",
                requisition_id
            ))

        logger.info("Requisition %s cancelled by user %s", current['RequisitionNumber'], user_info['UserId'])
        invalidate_reports_cache(user_info.get('DistrictId'))

        return {
            "message": "Requisition cancelled successfully",
            "requisition_id": requisition_id,
            "requisition_number": current['RequisitionNumber']
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Cancel requisition error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "CANCEL_FAILED",
            "Failed to cancel requisition"
        )


# ===========================================
# APPROVAL WORKFLOW
# ===========================================

@router.get("/pending/list")
async def list_pending_approvals(
    session_id: str = Query(...),
    search: Optional[str] = Query(None, description="Search by requisition number, school, district, or submitter"),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100)
):
    """
    List requisitions pending approval.
    Only returns requisitions the user has authority to approve.
    """
    # Validate session (demo mode shows all pending across districts)
    is_demo = session_id == 'demo'
    if not is_demo:
        try:
            sid = int(session_id)
        except (ValueError, TypeError):
            raise_api_error(status.HTTP_401_UNAUTHORIZED, "SESSION_INVALID", "Invalid session")

        user_info = get_user_from_session(sid)
        if not user_info:
            raise_api_error(
                status.HTTP_401_UNAUTHORIZED,
                "SESSION_INVALID",
                "Invalid or expired session"
            )

        approval_level = user_info.get('ApprovalLevel', 0)
        if approval_level < 1:
            raise_api_error(
                status.HTTP_403_FORBIDDEN,
                "NO_APPROVAL_RIGHTS",
                "You do not have approval privileges"
            )

    try:
        # Get pending requisitions (filtered by district for real users, all for demo)
        offset = (page - 1) * page_size
        district_filter = "AND sc.DistrictId = ?" if not is_demo else ""
        district_params = [user_info['DistrictId']] if not is_demo else []
        # Demo mode: limit to last 2 years for realistic data
        date_filter = "AND r.DateEntered >= DATEADD(YEAR, -2, GETDATE())" if is_demo else ""
        # Search filter across requisition number, school, district, submitter
        search_filter = ""
        search_params = []
        if search:
            safe_search = re.sub(r'[^\w\s\-.,\'\"()]', '', search).strip()[:100]
            if safe_search:
                search_filter = """AND (
                    CAST(r.RequisitionNumber AS VARCHAR) LIKE ?
                    OR sc.Name LIKE ?
                    OR d.Name LIKE ?
                    OR u.UserName LIKE ?
                    OR u.FirstName LIKE ?
                    OR u.LastName LIKE ?
                )"""
                pattern = f"%{safe_search}%"
                search_params = [pattern] * 6

        base_params = [STATUS_ON_HOLD, STATUS_PENDING_APPROVAL] + district_params + search_params
        results = execute_query(f"""
            SELECT
                r.RequisitionId,
                r.RequisitionNumber,
                r.StatusId,
                st.Name as StatusName,
                r.TotalRequisitionCost,
                r.DateEntered,
                r.Comments,
                ISNULL(NULLIF(RTRIM(u.FirstName + ' ' + u.LastName), ''), u.UserName) as SubmittedBy,
                sc.Name as SchoolName,
                d.Name as DistrictName,
                (SELECT COUNT(*) FROM Detail d WHERE d.RequisitionId = r.RequisitionId) as ItemCount
            FROM Requisitions r
            JOIN Users u ON r.UserId = u.UserId
            JOIN School sc ON r.SchoolId = sc.SchoolId
            JOIN District d ON sc.DistrictId = d.DistrictId
            LEFT JOIN StatusTable st ON r.StatusId = st.StatusId
            WHERE r.StatusId IN (?, ?)
            AND r.Active = 1
            {district_filter}
            {date_filter}
            {search_filter}
            ORDER BY r.DateEntered DESC
            OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
        """, tuple(base_params + [offset, page_size]))

        count_result = execute_single(f"""
            SELECT COUNT(*) as total
            FROM Requisitions r
            JOIN Users u ON r.UserId = u.UserId
            JOIN School sc ON r.SchoolId = sc.SchoolId
            JOIN District d ON sc.DistrictId = d.DistrictId
            WHERE r.StatusId IN (?, ?)
            AND r.Active = 1
            {district_filter}
            {date_filter}
            {search_filter}
        """, tuple(base_params))

        total = count_result['total'] if count_result else 0

        return {
            "items": [
                {
                    "requisition_id": row['RequisitionId'],
                    "requisition_number": row['RequisitionNumber'],
                    "status": row['StatusName'] or STATUS_NAMES.get(row['StatusId'], 'Draft'),
                    "total_amount": float(row['TotalRequisitionCost'] or 0),
                    "item_count": row['ItemCount'] or 0,
                    "submitted_by": row['SubmittedBy'] or 'Unknown',
                    "school_name": row.get('SchoolName') or None,
                    "district_name": row.get('DistrictName') or None,
                    "created_at": row['DateEntered'].isoformat() if row['DateEntered'] else None,
                    "notes_preview": row['Comments'][:100] if row.get('Comments') else None
                }
                for row in results
            ],
            "total": total,
            "page": page,
            "page_size": page_size
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error("List pending approvals error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "LIST_FAILED",
            "Failed to list pending approvals"
        )


@router.post("/{requisition_id}/approve")
async def approve_requisition(requisition_id: int, approval: RequisitionApproval):
    """
    Approve a requisition.
    Requires approval privileges.
    """
    # Demo mode — read-only
    if str(approval.session_id) == 'demo':
        raise_api_error(status.HTTP_403_FORBIDDEN, "DEMO_READ_ONLY", "Demo mode is read-only. Log in to approve requisitions.")

    # Validate session
    sid = approval.session_id if isinstance(approval.session_id, int) else int(approval.session_id)
    user_info = get_user_from_session(sid)
    if not user_info:
        raise_api_error(
            status.HTTP_401_UNAUTHORIZED,
            "SESSION_INVALID",
            "Invalid or expired session"
        )

    approval_level = user_info.get('ApprovalLevel', 0)
    if approval_level < 1:
        raise_api_error(
            status.HTTP_403_FORBIDDEN,
            "NO_APPROVAL_RIGHTS",
            "You do not have approval privileges"
        )

    try:
        # Get requisition with district via School join
        current = execute_single("""
            SELECT r.RequisitionId, r.RequisitionNumber, r.StatusId,
                   r.TotalRequisitionCost, sc.DistrictId
            FROM Requisitions r
            JOIN School sc ON r.SchoolId = sc.SchoolId
            WHERE r.RequisitionId = ?
        """, (requisition_id,))

        if not current:
            raise_api_error(
                status.HTTP_404_NOT_FOUND,
                "NOT_FOUND",
                "Requisition not found"
            )

        # Verify same district
        if current['DistrictId'] != user_info['DistrictId']:
            raise_api_error(
                status.HTTP_403_FORBIDDEN,
                "CROSS_DISTRICT",
                "Cannot approve requisitions from other districts"
            )

        current_status_id = current['StatusId']
        if current_status_id not in (STATUS_ON_HOLD, STATUS_PENDING_APPROVAL):
            status_name = STATUS_NAMES.get(current_status_id, str(current_status_id))
            raise_api_error(
                status.HTTP_400_BAD_REQUEST,
                "INVALID_STATUS",
                f"Cannot approve requisition with status '{status_name}'"
            )

        # Approve the requisition
        approver_name = user_info.get('UserName') or f"User {user_info['UserId']}"

        with transaction() as (conn, cursor):
            cursor.execute("""
                UPDATE Requisitions
                SET StatusId = ?,
                    ApprovalId = ?,
                    ApprovalLevel = ?,
                    Comments = COALESCE(Comments, '') + ?,
                    DateUpdated = GETDATE()
                WHERE RequisitionId = ?
            """, (
                STATUS_APPROVED,
                user_info['UserId'],
                user_info.get('ApprovalLevel', 1),
                f"\n\n[Approved by {approver_name} on {datetime.now().strftime('%Y-%m-%d %H:%M')}]" +
                (f"\nComments: {approval.comments}" if approval.comments else ""),
                requisition_id
            ))

        logger.info("Requisition %s approved by %s", current['RequisitionNumber'], approver_name)
        invalidate_reports_cache(user_info.get('DistrictId'))

        return {
            "message": "Requisition approved successfully",
            "requisition_id": requisition_id,
            "requisition_number": current['RequisitionNumber'],
            "new_status": "Approved"
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Approve requisition error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "APPROVAL_FAILED",
            "Failed to approve requisition"
        )


@router.post("/{requisition_id}/reject")
async def reject_requisition(requisition_id: int, rejection: RequisitionRejection):
    """
    Reject a requisition.
    Requires approval privileges and a rejection reason.
    """
    # Demo mode — read-only
    if str(rejection.session_id) == 'demo':
        raise_api_error(status.HTTP_403_FORBIDDEN, "DEMO_READ_ONLY", "Demo mode is read-only. Log in to reject requisitions.")

    # Validate session
    sid = rejection.session_id if isinstance(rejection.session_id, int) else int(rejection.session_id)
    user_info = get_user_from_session(sid)
    if not user_info:
        raise_api_error(
            status.HTTP_401_UNAUTHORIZED,
            "SESSION_INVALID",
            "Invalid or expired session"
        )

    approval_level = user_info.get('ApprovalLevel', 0)
    if approval_level < 1:
        raise_api_error(
            status.HTTP_403_FORBIDDEN,
            "NO_APPROVAL_RIGHTS",
            "You do not have approval privileges"
        )

    try:
        # Get requisition with district via School join
        current = execute_single("""
            SELECT r.RequisitionId, r.RequisitionNumber, r.StatusId, sc.DistrictId
            FROM Requisitions r
            JOIN School sc ON r.SchoolId = sc.SchoolId
            WHERE r.RequisitionId = ?
        """, (requisition_id,))

        if not current:
            raise_api_error(
                status.HTTP_404_NOT_FOUND,
                "NOT_FOUND",
                "Requisition not found"
            )

        # Verify same district
        if current['DistrictId'] != user_info['DistrictId']:
            raise_api_error(
                status.HTTP_403_FORBIDDEN,
                "CROSS_DISTRICT",
                "Cannot reject requisitions from other districts"
            )

        current_status_id = current['StatusId']
        if current_status_id not in (STATUS_ON_HOLD, STATUS_PENDING_APPROVAL):
            status_name = STATUS_NAMES.get(current_status_id, str(current_status_id))
            raise_api_error(
                status.HTTP_400_BAD_REQUEST,
                "INVALID_STATUS",
                f"Cannot reject requisition with status '{status_name}'"
            )

        # Reject the requisition
        rejector_name = user_info.get('UserName') or f"User {user_info['UserId']}"

        with transaction() as (conn, cursor):
            cursor.execute("""
                UPDATE Requisitions
                SET StatusId = ?,
                    Comments = COALESCE(Comments, '') + ?,
                    DateUpdated = GETDATE()
                WHERE RequisitionId = ?
            """, (
                STATUS_REJECTED,
                f"\n\n[Rejected by {rejector_name} on {datetime.now().strftime('%Y-%m-%d %H:%M')}]\nReason: {rejection.reason}",
                requisition_id
            ))

        logger.info("Requisition %s rejected by %s: %s", current['RequisitionNumber'], rejector_name, rejection.reason)
        invalidate_reports_cache(user_info.get('DistrictId'))

        return {
            "message": "Requisition rejected",
            "requisition_id": requisition_id,
            "requisition_number": current['RequisitionNumber'],
            "new_status": "Rejected"
        }

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Reject requisition error: %s", e)
        raise_api_error(
            status.HTTP_500_INTERNAL_SERVER_ERROR,
            "REJECTION_FAILED",
            "Failed to reject requisition"
        )
