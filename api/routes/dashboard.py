"""
User-facing dashboard API endpoints.

Provides dashboard summary data for all authenticated users (not admin-only).
Includes budget/spending summaries, approver info, and pending approval counts.
"""

from fastapi import APIRouter, HTTPException, Header
from typing import Optional
from datetime import datetime
import logging

from api.database import execute_single, execute_query

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

# StatusId values from StatusTable
STATUS_ON_HOLD = 1
STATUS_PENDING_APPROVAL = 2
STATUS_APPROVED = 3
STATUS_REJECTED = 4

STATUS_NAMES = {
    1: "On Hold",
    2: "Pending Approval",
    3: "Approved",
    4: "Rejected",
    5: "At EDS",
    6: "PO Printed",
}


def _get_session_user(session_id: str, demo_approval_level: int = 1) -> dict:
    """Validate session and return user info."""
    if not session_id or session_id == 'demo':
        # Demo mode: approval level can be overridden via X-Demo-Approval-Level header
        return {
            "UserId": 0, "DistrictId": 0, "SchoolId": 0,
            "ApprovalLevel": demo_approval_level, "UserName": "Demo User",
            "Email": "",
        }
    try:
        sid = int(session_id)
    except (ValueError, TypeError):
        raise HTTPException(status_code=401, detail="Invalid session")

    user = execute_single("""
        SELECT
            s.UserId, s.DistrictId, s.SchoolId, s.ApprovalLevel,
            u.UserName, u.Email
        FROM SessionTable s
        LEFT JOIN Users u ON s.UserId = u.UserId
        WHERE s.SessionId = ?
        AND s.SessionEnd IS NULL
        AND DATEDIFF(HOUR, s.SessionStart, GETDATE()) < 8
    """, (sid,))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
    return user


@router.get("/summary")
async def get_dashboard_summary(
    x_session_id: Optional[str] = Header(None, alias="X-Session-ID"),
    x_demo_approval: Optional[int] = Header(None, alias="X-Demo-Approval-Level"),
):
    """
    Get user-specific dashboard summary.

    Returns budget info, spending, pending approvals count,
    and approver info. Works for all authenticated users (not admin-only).
    """
    demo_level = x_demo_approval if x_demo_approval is not None else 1
    user = _get_session_user(x_session_id, demo_approval_level=demo_level)
    user_id = user.get("UserId", 0)
    district_id = user.get("DistrictId", 0)
    approval_level = user.get("ApprovalLevel", 0)
    is_demo = user_id == 0

    # --- Budget & Spending ---
    budget_data = {"budget": 0, "spent": 0, "remaining": 0, "percent": 0}
    user_filter = "WHERE UserId = ?" if not is_demo else "WHERE 1=1"
    user_params = [user_id] if not is_demo else []
    actual_spend = execute_single(f"""
        SELECT ISNULL(SUM(TotalRequisitionCost), 0) AS spent
        FROM Requisitions
        {user_filter}
        AND StatusId NOT IN (?, ?)
        AND Active = 1
        AND DateEntered >= DATEADD(YEAR, -1, GETDATE())
    """, tuple(user_params + [STATUS_REJECTED, STATUS_ON_HOLD]))
    spent = float(actual_spend["spent"]) if actual_spend else 0
    # Use a default budget of 50000 if not set (Users table doesn't have Budget column)
    # For demo mode, estimate budget as 175% of actual spend (matches reports logic)
    user_budget = spent * 1.75 if is_demo and spent > 0 else 50000.0
    if user_budget > 0:
        budget_data = {
            "budget": round(user_budget, 2),
            "spent": spent,
            "remaining": round(user_budget - spent, 2),
            "percent": round(spent / user_budget * 100) if user_budget > 0 else 0,
        }

    # --- My Orders Status Counts ---
    order_counts = {"on_hold": 0, "pending_approval": 0, "approved": 0, "total_active": 0}
    try:
        orders_filter = "WHERE UserId = ?" if not is_demo else "WHERE 1=1"
        orders_params = [user_id] if not is_demo else []
        count_rows = execute_query(f"""
            SELECT StatusId, COUNT(*) AS cnt
            FROM Requisitions
            {orders_filter}
            AND Active = 1
            AND StatusId IN (?, ?, ?)
            GROUP BY StatusId
        """, tuple(orders_params + [STATUS_ON_HOLD, STATUS_PENDING_APPROVAL, STATUS_APPROVED]))
        total_active = 0
        for r in count_rows:
            sid = r["StatusId"]
            name = STATUS_NAMES.get(sid, "unknown").lower().replace(" ", "_")
            order_counts[name] = r["cnt"]
            total_active += r["cnt"]
        order_counts["total_active"] = total_active
    except Exception as e:
        logger.warning(f"Dashboard order counts query failed: {e}")

    # --- Pending Approvals (if user is an approver) ---
    pending_approvals = {"count": 0, "urgent": 0, "oldest_days": 0}
    if approval_level >= 1:
        try:
            district_filter = "AND sc.DistrictId = ?" if not is_demo else ""
            district_params = [district_id] if not is_demo else []
            pending = execute_single(f"""
                SELECT
                    COUNT(*) AS cnt,
                    SUM(CASE WHEN DATEDIFF(DAY, r.DateEntered, GETDATE()) > 3 THEN 1 ELSE 0 END) AS urgent,
                    ISNULL(MAX(DATEDIFF(DAY, r.DateEntered, GETDATE())), 0) AS oldest
                FROM Requisitions r
                JOIN School sc ON r.SchoolId = sc.SchoolId
                WHERE r.StatusId IN (?, ?)
                AND r.Active = 1
                {district_filter}
            """, tuple([STATUS_ON_HOLD, STATUS_PENDING_APPROVAL] + district_params))
            if pending:
                pending_approvals = {
                    "count": pending["cnt"] or 0,
                    "urgent": pending["urgent"] or 0,
                    "oldest_days": pending["oldest"] or 0,
                }
        except Exception as e:
            logger.warning(f"Dashboard pending approvals query failed: {e}")

    # --- Approver Info ---
    approver_info = None
    if approval_level >= 1:
        approver_info = {
            "is_approver": True,
            "level": approval_level,
            "district_id": district_id,
        }

    # --- Recent Activity (last 5 requisitions by update date) ---
    recent_activity = []
    try:
        activity_filter = "WHERE r.UserId = ?" if not is_demo else "WHERE 1=1"
        activity_params = [user_id] if not is_demo else []
        activity_rows = execute_query(f"""
            SELECT TOP 5
                r.RequisitionId,
                r.RequisitionNumber,
                r.StatusId,
                st.Name as StatusName,
                r.DateUpdated,
                DATEDIFF(MINUTE, r.DateUpdated, GETDATE()) AS minutes_ago
            FROM Requisitions r
            LEFT JOIN StatusTable st ON r.StatusId = st.StatusId
            {activity_filter}
            AND r.DateUpdated IS NOT NULL
            AND r.Active = 1
            ORDER BY r.DateUpdated DESC
        """, tuple(activity_params))
        for r in activity_rows:
            mins = r["minutes_ago"] or 0
            if mins < 60:
                time_label = f"{mins}m ago"
            elif mins < 1440:
                time_label = f"{mins // 60}h ago"
            else:
                time_label = f"{mins // 1440}d ago"
            recent_activity.append({
                "id": r["RequisitionId"],
                "name": r["RequisitionNumber"] or f"Req #{r['RequisitionId']}",
                "status": r["StatusName"] or STATUS_NAMES.get(r["StatusId"], "Unknown"),
                "time_label": time_label,
            })
    except Exception as e:
        logger.warning(f"Dashboard recent activity query failed: {e}")

    # --- Alerts ---
    alerts = []
    # Budget warning
    if budget_data["percent"] >= 90:
        alerts.append({
            "type": "danger",
            "icon": "fas fa-exclamation-triangle",
            "title": "Budget Nearly Exhausted",
            "message": f"You've used {budget_data['percent']}% of your annual budget. Only ${budget_data['remaining']:,.0f} remaining.",
        })
    elif budget_data["percent"] >= 75:
        alerts.append({
            "type": "warning",
            "icon": "fas fa-exclamation-circle",
            "title": "Budget Alert",
            "message": f"You've used {budget_data['percent']}% of your annual budget (${budget_data['spent']:,.0f} of ${budget_data['budget']:,.0f}).",
        })

    # Urgent approvals
    if pending_approvals["urgent"] > 0:
        alerts.append({
            "type": "danger",
            "icon": "fas fa-clock",
            "title": f"{pending_approvals['urgent']} Urgent Approval{'s' if pending_approvals['urgent'] != 1 else ''}",
            "message": f"Requisitions waiting {pending_approvals['oldest_days']}+ days for approval.",
        })

    return {
        "budget": budget_data,
        "department_budget": None,
        "order_counts": order_counts,
        "pending_approvals": pending_approvals,
        "approver_info": approver_info,
        "recent_activity": recent_activity,
        "alerts": alerts,
    }
