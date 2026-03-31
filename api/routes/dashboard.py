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
from api.middleware import SESSION_TIMEOUT_HOURS

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
        AND DATEDIFF(HOUR, s.SessionStart, GETDATE()) < ?
    """, (sid, SESSION_TIMEOUT_HOURS))
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
    budget_data = {"budget": 0, "spent": 0, "remaining": 0, "percent": 0, "breakdown": []}
    demo_district_id = None
    district_name = None
    demo_school_name = None
    if is_demo:
        # First, find the top-spending district for reference
        demo_budget = execute_single("""
            SELECT TOP 1
                d.DistrictId as district_id,
                d.Name as district_name,
                ISNULL(SUM(r.TotalRequisitionCost), 0) AS spent,
                COUNT(*) as order_count
            FROM Requisitions r
            JOIN School sc ON r.SchoolId = sc.SchoolId
            JOIN District d ON sc.DistrictId = d.DistrictId
            WHERE r.StatusId NOT IN (?, ?)
            AND r.Active = 1
            AND r.DateEntered >= DATEADD(YEAR, -1, GETDATE())
            GROUP BY d.DistrictId, d.Name
            HAVING SUM(r.TotalRequisitionCost) > 0
            ORDER BY SUM(r.TotalRequisitionCost) DESC
        """, (STATUS_REJECTED, STATUS_ON_HOLD))
        district_name = demo_budget["district_name"] if demo_budget else "Demo District"
        demo_district_id = demo_budget["district_id"] if demo_budget else None

        if approval_level >= 1:
            # Approver: show district-level budget
            spent = float(demo_budget["spent"]) if demo_budget else 0
            user_budget = spent * 1.35
            budget_label = district_name
        else:
            # Teacher: show a single school's budget within the district
            school_budget = execute_single("""
                SELECT TOP 1
                    sc.Name as school_name,
                    ISNULL(SUM(r.TotalRequisitionCost), 0) AS spent
                FROM Requisitions r
                JOIN School sc ON r.SchoolId = sc.SchoolId
                WHERE sc.DistrictId = ?
                AND r.StatusId NOT IN (?, ?)
                AND r.Active = 1
                AND r.DateEntered >= DATEADD(YEAR, -1, GETDATE())
                GROUP BY sc.SchoolId, sc.Name
                HAVING SUM(r.TotalRequisitionCost) > 0
                ORDER BY SUM(r.TotalRequisitionCost) DESC
            """, (demo_district_id, STATUS_REJECTED, STATUS_ON_HOLD))
            spent = float(school_budget["spent"]) if school_budget else 0
            demo_school_name = school_budget["school_name"] if school_budget else "My School"
            user_budget = spent * 1.25  # Tighter school budget
            budget_label = demo_school_name

        # Get top spending categories for breakdown
        scope_filter = "d.DistrictId = ?" if approval_level >= 1 else "sc.Name = ?"
        scope_param = demo_district_id if approval_level >= 1 else demo_school_name
        breakdown_rows = execute_query(f"""
            SELECT TOP 5 category, SUM(amount) as amount FROM (
                SELECT
                    ISNULL(c.Name, 'Other') as category,
                    r.TotalRequisitionCost as amount
                FROM Requisitions r
                JOIN School sc ON r.SchoolId = sc.SchoolId
                JOIN District d ON sc.DistrictId = d.DistrictId
                CROSS APPLY (
                    SELECT TOP 1 dt.ItemId FROM Detail dt WHERE dt.RequisitionId = r.RequisitionId
                ) top_item
                LEFT JOIN Items i ON top_item.ItemId = i.ItemId
                LEFT JOIN Category c ON i.CategoryId = c.CategoryId
                WHERE {scope_filter}
                AND r.StatusId NOT IN (?, ?)
                AND r.Active = 1
                AND r.TotalRequisitionCost > 0
                AND r.DateEntered >= DATEADD(YEAR, -1, GETDATE())
            ) sub
            GROUP BY category
            ORDER BY SUM(amount) DESC
        """, (scope_param, STATUS_REJECTED, STATUS_ON_HOLD))
        breakdown = [{"category": row["category"], "amount": round(float(row["amount"]), 2)} for row in breakdown_rows]
    else:
        user_filter = "WHERE UserId = ?"
        user_params = [user_id]
        actual_spend = execute_single(f"""
            SELECT ISNULL(SUM(TotalRequisitionCost), 0) AS spent
            FROM Requisitions
            {user_filter}
            AND StatusId NOT IN (?, ?)
            AND Active = 1
            AND DateEntered >= DATEADD(YEAR, -1, GETDATE())
        """, tuple(user_params + [STATUS_REJECTED, STATUS_ON_HOLD]))
        spent = float(actual_spend["spent"]) if actual_spend else 0
        user_budget = 50000.0  # Default budget
        breakdown = []

    # Monthly spending trend (last 12 months)
    monthly_spending = []
    try:
        if is_demo and demo_district_id:
            monthly_rows = execute_query("""
                SELECT
                    FORMAT(r.DateEntered, 'yyyy-MM') as month,
                    ISNULL(SUM(r.TotalRequisitionCost), 0) as amount,
                    COUNT(*) as order_count
                FROM Requisitions r
                JOIN School sc ON r.SchoolId = sc.SchoolId
                WHERE sc.DistrictId = ?
                AND r.StatusId NOT IN (?, ?)
                AND r.Active = 1
                AND r.DateEntered >= DATEADD(MONTH, -12, GETDATE())
                GROUP BY FORMAT(r.DateEntered, 'yyyy-MM')
                ORDER BY FORMAT(r.DateEntered, 'yyyy-MM')
            """, (demo_district_id, STATUS_REJECTED, STATUS_ON_HOLD))
        else:
            monthly_rows = execute_query("""
                SELECT
                    FORMAT(DateEntered, 'yyyy-MM') as month,
                    ISNULL(SUM(TotalRequisitionCost), 0) as amount,
                    COUNT(*) as order_count
                FROM Requisitions
                WHERE UserId = ?
                AND StatusId NOT IN (?, ?)
                AND Active = 1
                AND DateEntered >= DATEADD(MONTH, -12, GETDATE())
                GROUP BY FORMAT(DateEntered, 'yyyy-MM')
                ORDER BY FORMAT(DateEntered, 'yyyy-MM')
            """, (user_id, STATUS_REJECTED, STATUS_ON_HOLD))
        monthly_spending = [{"month": row["month"], "amount": round(float(row["amount"]), 2), "orders": row["order_count"]} for row in monthly_rows]
    except Exception as e:
        logger.warning("Dashboard monthly spending query failed: %s", e)

    if user_budget > 0:
        budget_data = {
            "budget": round(user_budget, 2),
            "spent": round(spent, 2),
            "remaining": round(user_budget - spent, 2),
            "percent": round(spent / user_budget * 100) if user_budget > 0 else 0,
            "breakdown": breakdown,
            "monthly_spending": monthly_spending,
            "district_name": district_name if is_demo else None,
            "school_name": demo_school_name if is_demo and approval_level < 1 else None,
            "scope": "school" if (is_demo and approval_level < 1) else "district",
        }

    # --- My Orders Status Counts ---
    order_counts = {"on_hold": 0, "pending_approval": 0, "approved": 0, "total_active": 0}
    try:
        if is_demo and demo_district_id:
            # Demo: scope to the same district as the budget
            count_rows = execute_query("""
                SELECT r.StatusId, COUNT(*) AS cnt
                FROM Requisitions r
                JOIN School sc ON r.SchoolId = sc.SchoolId
                WHERE sc.DistrictId = ?
                AND r.Active = 1
                AND r.StatusId IN (?, ?, ?)
                AND r.DateEntered >= DATEADD(YEAR, -2, GETDATE())
                GROUP BY r.StatusId
            """, (demo_district_id, STATUS_ON_HOLD, STATUS_PENDING_APPROVAL, STATUS_APPROVED))
        else:
            orders_filter = "WHERE UserId = ?"
            orders_params = [user_id]
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
        logger.warning("Dashboard order counts query failed: %s", e)

    # --- Pending Approvals (if user is an approver) ---
    pending_approvals = {"count": 0, "urgent": 0, "oldest_days": 0}
    if approval_level >= 1:
        try:
            if is_demo and demo_district_id:
                district_filter = "AND sc.DistrictId = ?"
                district_params = [demo_district_id]
            elif not is_demo:
                district_filter = "AND sc.DistrictId = ?"
                district_params = [district_id]
            else:
                district_filter = ""
                district_params = []
            date_filter = "AND r.DateEntered >= DATEADD(YEAR, -2, GETDATE())" if is_demo else ""
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
                {date_filter}
            """, tuple([STATUS_ON_HOLD, STATUS_PENDING_APPROVAL] + district_params))
            if pending:
                pending_approvals = {
                    "count": pending["cnt"] or 0,
                    "urgent": pending["urgent"] or 0,
                    "oldest_days": pending["oldest"] or 0,
                }
        except Exception as e:
            logger.warning("Dashboard pending approvals query failed: %s", e)

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
        if is_demo and demo_district_id:
            activity_rows = execute_query("""
                SELECT TOP 5
                    r.RequisitionId,
                    r.RequisitionNumber,
                    r.StatusId,
                    st.Name as StatusName,
                    r.TotalRequisitionCost,
                    sc.Name as SchoolName,
                    r.DateUpdated,
                    DATEDIFF(MINUTE, r.DateUpdated, GETDATE()) AS minutes_ago
                FROM Requisitions r
                JOIN School sc ON r.SchoolId = sc.SchoolId
                LEFT JOIN StatusTable st ON r.StatusId = st.StatusId
                WHERE sc.DistrictId = ?
                AND r.DateUpdated IS NOT NULL
                AND r.Active = 1
                AND r.StatusId IS NOT NULL
                ORDER BY r.DateUpdated DESC
            """, (demo_district_id,))
        else:
            activity_rows = execute_query("""
                SELECT TOP 5
                    r.RequisitionId,
                    r.RequisitionNumber,
                    r.StatusId,
                    st.Name as StatusName,
                    r.TotalRequisitionCost,
                    sc.Name as SchoolName,
                    r.DateUpdated,
                    DATEDIFF(MINUTE, r.DateUpdated, GETDATE()) AS minutes_ago
                FROM Requisitions r
                JOIN School sc ON r.SchoolId = sc.SchoolId
                LEFT JOIN StatusTable st ON r.StatusId = st.StatusId
                WHERE r.UserId = ?
                AND r.DateUpdated IS NOT NULL
                AND r.Active = 1
                ORDER BY r.DateUpdated DESC
            """, (user_id,))
        for r in activity_rows:
            mins = r["minutes_ago"] or 0
            if mins < 60:
                time_label = f"{mins}m ago"
            elif mins < 1440:
                time_label = f"{mins // 60}h ago"
            else:
                time_label = f"{mins // 1440}d ago"
            status = r["StatusName"] or STATUS_NAMES.get(r["StatusId"], "Draft")
            amount = float(r["TotalRequisitionCost"] or 0)
            recent_activity.append({
                "id": r["RequisitionId"],
                "name": r["RequisitionNumber"] or f"Req #{r['RequisitionId']}",
                "status": status,
                "amount": amount,
                "school_name": r.get("SchoolName") or None,
                "time_label": time_label,
            })
    except Exception as e:
        logger.warning("Dashboard recent activity query failed: %s", e)

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
