"""
Admin API routes for EDS Universal Requisition.

Provides backend endpoints for admin pages:
- Dashboard statistics
- User management
- Budget management
- Report data
- Search index management
"""

from fastapi import APIRouter, HTTPException, Query, BackgroundTasks
from typing import Optional
from datetime import datetime
import logging
import math

from api.database import execute_query, execute_single, get_db_cursor, transaction

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/admin", tags=["Admin"])


# ===========================================
# HELPER: Require admin session
# ===========================================

def require_admin_session(session_id: int) -> dict:
    """
    Validate session and require admin/approver privileges.
    Returns user info or raises HTTPException.
    """
    user = execute_single("""
        SELECT
            s.UserId,
            s.SchoolId,
            s.DistrictId,
            s.ApprovalLevel,
            u.FirstName,
            u.LastName,
            u.Email
        FROM SessionTable s
        LEFT JOIN Users u ON s.UserId = u.UserId
        WHERE s.SessionId = ?
        AND s.SessionEnd IS NULL
        AND DATEDIFF(HOUR, s.SessionStart, GETDATE()) < 8
    """, (session_id,))
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired session")
    if user.get("ApprovalLevel", 0) < 1:
        raise HTTPException(status_code=403, detail="Admin access required")
    return user


# ===========================================
# DASHBOARD ENDPOINTS
# ===========================================

@router.get("/dashboard/stats")
async def get_dashboard_stats(session_id: int = Query(...)):
    """Get high-level dashboard metrics."""
    require_admin_session(session_id)

    # Orders today
    orders_today = execute_single("""
        SELECT COUNT(*) AS count
        FROM Requisitions
        WHERE CAST(CreatedAt AS DATE) = CAST(GETDATE() AS DATE)
    """) or {"count": 0}

    # Orders yesterday (for change calculation)
    orders_yesterday = execute_single("""
        SELECT COUNT(*) AS count
        FROM Requisitions
        WHERE CAST(CreatedAt AS DATE) = CAST(DATEADD(DAY, -1, GETDATE()) AS DATE)
    """) or {"count": 0}

    # Pending approvals
    pending = execute_single("""
        SELECT COUNT(*) AS count
        FROM Requisitions
        WHERE Status IN ('Submitted', 'Pending Approval')
    """) or {"count": 0}

    # Urgent (pending > 3 days)
    urgent = execute_single("""
        SELECT COUNT(*) AS count
        FROM Requisitions
        WHERE Status IN ('Submitted', 'Pending Approval')
        AND DATEDIFF(DAY, CreatedAt, GETDATE()) > 3
    """) or {"count": 0}

    # Total spend this month
    spend = execute_single("""
        SELECT ISNULL(SUM(TotalAmount), 0) AS total
        FROM Requisitions
        WHERE Status NOT IN ('Cancelled', 'Rejected', 'Draft')
        AND MONTH(CreatedAt) = MONTH(GETDATE())
        AND YEAR(CreatedAt) = YEAR(GETDATE())
    """) or {"total": 0}

    # Active users (sessions in last 24h)
    active_users = execute_single("""
        SELECT COUNT(DISTINCT UserId) AS count
        FROM SessionTable
        WHERE SessionEnd IS NULL
        AND DATEDIFF(HOUR, SessionStart, GETDATE()) < 24
    """) or {"count": 0}

    # Online now (sessions in last 30 min)
    online_now = execute_single("""
        SELECT COUNT(DISTINCT UserId) AS count
        FROM SessionTable
        WHERE SessionEnd IS NULL
        AND DATEDIFF(MINUTE, ISNULL(LastActivity, SessionStart), GETDATE()) < 30
    """) or {"count": 0}

    # Sparkline: last 7 days of spending
    sparkline_rows = execute_query("""
        SELECT
            CAST(CreatedAt AS DATE) AS day,
            ISNULL(SUM(TotalAmount), 0) AS total
        FROM Requisitions
        WHERE Status NOT IN ('Cancelled', 'Rejected', 'Draft')
        AND CreatedAt >= DATEADD(DAY, -6, CAST(GETDATE() AS DATE))
        GROUP BY CAST(CreatedAt AS DATE)
        ORDER BY day
    """)
    sparkline = [float(r["total"]) for r in sparkline_rows]

    today_count = orders_today["count"]
    yesterday_count = orders_yesterday["count"]
    change = 0
    if yesterday_count > 0:
        change = round(((today_count - yesterday_count) / yesterday_count) * 100)

    return {
        "metrics": {
            "ordersToday": today_count,
            "ordersChange": change,
            "pendingApprovals": pending["count"],
            "urgentApprovals": urgent["count"],
            "totalSpend": float(spend["total"]),
            "spendSparkline": sparkline,
            "activeUsers": active_users["count"],
            "onlineNow": online_now["count"],
        }
    }


@router.get("/dashboard/departments")
async def get_dashboard_departments(session_id: int = Query(...)):
    """Get department budget summary for dashboard."""
    require_admin_session(session_id)

    rows = execute_query("""
        SELECT
            d.DepartmentName AS name,
            ISNULL(d.Budget, 0) AS budget,
            ISNULL(SUM(r.TotalAmount), 0) AS spent
        FROM Departments d
        LEFT JOIN Users u ON u.DepartmentId = d.DepartmentId
        LEFT JOIN Requisitions r ON r.UserId = u.UserId
            AND r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
            AND YEAR(r.CreatedAt) = YEAR(GETDATE())
        GROUP BY d.DepartmentName, d.Budget
        ORDER BY d.DepartmentName
    """)

    colors = ['#3b82f6', '#10b981', '#f59e0b', '#8b5cf6', '#ef4444', '#06b6d4']
    departments = []
    for i, r in enumerate(rows):
        budget = float(r["budget"]) or 1
        spent = float(r["spent"])
        departments.append({
            "name": r["name"],
            "spent": spent,
            "budget": budget,
            "percent": round(spent / budget * 100) if budget > 0 else 0,
            "color": colors[i % len(colors)],
        })

    return {"departments": departments}


@router.get("/dashboard/recent-orders")
async def get_recent_orders(session_id: int = Query(...), limit: int = 10):
    """Get recent orders for dashboard activity feed."""
    require_admin_session(session_id)

    rows = execute_query("""
        SELECT TOP (?)
            r.RequisitionId AS id,
            r.RequisitionNumber AS requisition_number,
            u.FirstName + ' ' + u.LastName AS requester,
            r.TotalAmount AS total,
            r.Status AS status,
            r.CreatedAt AS date
        FROM Requisitions r
        LEFT JOIN Users u ON r.UserId = u.UserId
        ORDER BY r.CreatedAt DESC
    """, (limit,))

    orders = []
    for r in rows:
        orders.append({
            "id": r["requisition_number"] or f"REQ-{r['id']}",
            "requester": r["requester"] or "Unknown",
            "total": float(r["total"] or 0),
            "status": (r["status"] or "").lower().replace(" ", "_"),
            "date": r["date"].isoformat() if r["date"] else "",
        })

    return {"recentOrders": orders}


@router.get("/dashboard/pending-orders")
async def get_pending_orders(session_id: int = Query(...), limit: int = 10):
    """Get pending orders awaiting approval."""
    require_admin_session(session_id)

    rows = execute_query("""
        SELECT TOP (?)
            r.RequisitionId AS id,
            r.RequisitionNumber AS requisition_number,
            u.FirstName + ' ' + u.LastName AS requester,
            r.TotalAmount AS total,
            r.CreatedAt AS submitted
        FROM Requisitions r
        LEFT JOIN Users u ON r.UserId = u.UserId
        WHERE r.Status IN ('Submitted', 'Pending Approval')
        ORDER BY r.CreatedAt ASC
    """, (limit,))

    orders = []
    for r in rows:
        orders.append({
            "id": r["requisition_number"] or f"REQ-{r['id']}",
            "requester": r["requester"] or "Unknown",
            "total": float(r["total"] or 0),
            "submitted": r["submitted"].isoformat() if r["submitted"] else "",
        })

    return {"pendingOrders": orders}


@router.get("/dashboard/spending-chart")
async def get_spending_chart(session_id: int = Query(...), year: Optional[int] = None):
    """Get monthly spending data for chart."""
    require_admin_session(session_id)

    target_year = year or datetime.now().year

    rows = execute_query("""
        SELECT
            MONTH(CreatedAt) AS month_num,
            ISNULL(SUM(TotalAmount), 0) AS total
        FROM Requisitions
        WHERE Status NOT IN ('Cancelled', 'Rejected', 'Draft')
        AND YEAR(CreatedAt) = ?
        GROUP BY MONTH(CreatedAt)
        ORDER BY month_num
    """, (target_year,))

    month_labels = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    data = [0.0] * 12
    for r in rows:
        idx = int(r["month_num"]) - 1
        data[idx] = float(r["total"])

    return {
        "labels": month_labels,
        "data": data,
        "year": target_year,
    }


@router.get("/dashboard/top-products")
async def get_top_products(session_id: int = Query(...), limit: int = 5):
    """Get top ordered products."""
    require_admin_session(session_id)

    rows = execute_query("""
        SELECT TOP (?)
            i.ItemName AS name,
            COUNT(rd.DetailId) AS orders,
            ISNULL(SUM(rd.Quantity * rd.UnitPrice), 0) AS revenue
        FROM RequisitionDetails rd
        INNER JOIN Items i ON rd.ItemId = i.ItemId
        INNER JOIN Requisitions r ON rd.RequisitionId = r.RequisitionId
        WHERE r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
        AND r.CreatedAt >= DATEADD(MONTH, -3, GETDATE())
        GROUP BY i.ItemName
        ORDER BY orders DESC
    """, (limit,))

    return {
        "topProducts": [
            {"name": r["name"], "orders": r["orders"], "revenue": float(r["revenue"])}
            for r in rows
        ]
    }


# ===========================================
# USER MANAGEMENT ENDPOINTS
# ===========================================

@router.get("/users")
async def list_users(
    session_id: int = Query(...),
    search: str = Query(""),
    role: str = Query(""),
    status: str = Query(""),
    department: str = Query(""),
    page: int = Query(1, ge=1),
    page_size: int = Query(20, ge=1, le=100),
):
    """List users with filters and pagination."""
    require_admin_session(session_id)

    # Build WHERE conditions
    conditions = []
    params = []

    if search:
        conditions.append("""
            (u.FirstName + ' ' + u.LastName LIKE ?
             OR u.Email LIKE ?
             OR ISNULL(d.DepartmentName, '') LIKE ?)
        """)
        like = f"%{search}%"
        params.extend([like, like, like])

    if role:
        conditions.append("u.Role = ?")
        params.append(role)

    if status:
        conditions.append("u.Status = ?")
        params.append(status)

    if department:
        conditions.append("d.DepartmentName = ?")
        params.append(department)

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    # Get total count
    count_result = execute_single(f"""
        SELECT COUNT(*) AS total
        FROM Users u
        LEFT JOIN Departments d ON u.DepartmentId = d.DepartmentId
        {where}
    """, tuple(params) if params else None)
    total = count_result["total"] if count_result else 0
    total_pages = max(1, math.ceil(total / page_size))

    # Get page of users
    offset = (page - 1) * page_size
    rows = execute_query(f"""
        SELECT
            u.UserId AS id,
            u.FirstName + ' ' + u.LastName AS name,
            u.Email AS email,
            ISNULL(d.DepartmentName, '') AS department,
            ISNULL(u.Role, 'requester') AS role,
            ISNULL(u.Status, 'active') AS status,
            ISNULL(u.Budget, 0) AS budget,
            ISNULL(u.BudgetUsed, 0) AS budgetUsed,
            (SELECT MAX(s.SessionStart) FROM SessionTable s WHERE s.UserId = u.UserId) AS lastActive
        FROM Users u
        LEFT JOIN Departments d ON u.DepartmentId = d.DepartmentId
        {where}
        ORDER BY u.LastName, u.FirstName
        OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
    """, tuple(params + [offset, page_size]) if params else (offset, page_size))

    users = []
    for r in rows:
        budget = float(r["budget"]) or 0
        budget_used_val = float(r["budgetUsed"]) or 0
        budget_pct = round(budget_used_val / budget * 100) if budget > 0 else 0

        users.append({
            "id": r["id"],
            "name": r["name"] or "Unknown",
            "email": r["email"] or "",
            "department": r["department"],
            "role": r["role"],
            "status": r["status"],
            "budget": budget,
            "budgetUsed": budget_pct,
            "lastActive": r["lastActive"].isoformat() if r["lastActive"] else "Never",
        })

    # Stats
    stats = execute_single("""
        SELECT
            COUNT(*) AS total,
            SUM(CASE WHEN Status = 'active' THEN 1 ELSE 0 END) AS active,
            SUM(CASE WHEN Role = 'admin' THEN 1 ELSE 0 END) AS admins,
            SUM(CASE WHEN CreatedAt >= DATEADD(MONTH, -1, GETDATE()) THEN 1 ELSE 0 END) AS newThisMonth
        FROM Users
    """) or {"total": 0, "active": 0, "admins": 0, "newThisMonth": 0}

    # Departments list
    depts = execute_query("""
        SELECT DepartmentName AS name FROM Departments ORDER BY DepartmentName
    """)

    return {
        "users": users,
        "total": total,
        "page": page,
        "page_size": page_size,
        "total_pages": total_pages,
        "stats": {
            "total": stats["total"] or 0,
            "active": stats["active"] or 0,
            "admins": stats["admins"] or 0,
            "newThisMonth": stats["newThisMonth"] or 0,
        },
        "departments": [d["name"] for d in depts],
    }


@router.put("/users/{user_id}")
async def update_user(user_id: int, session_id: int = Query(...)):
    """Update user details (stub - body parsing handled by frontend)."""
    require_admin_session(session_id)
    # In a full implementation, parse body and update User record
    return {"message": "User updated", "user_id": user_id}


# ===========================================
# BUDGET MANAGEMENT ENDPOINTS
# ===========================================

@router.get("/budgets/overview")
async def get_budget_overview(session_id: int = Query(...)):
    """Get high-level budget overview."""
    require_admin_session(session_id)

    result = execute_single("""
        SELECT
            ISNULL(SUM(d.Budget), 0) AS totalBudget,
            ISNULL((
                SELECT SUM(r.TotalAmount)
                FROM Requisitions r
                WHERE r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
                AND YEAR(r.CreatedAt) = YEAR(GETDATE())
            ), 0) AS spent
        FROM Departments d
    """) or {"totalBudget": 0, "spent": 0}

    total = float(result["totalBudget"]) or 1
    spent = float(result["spent"])
    available = total - spent

    # Count departments over budget
    over = execute_single("""
        SELECT COUNT(*) AS count
        FROM Departments d
        WHERE d.Budget > 0
        AND (
            SELECT ISNULL(SUM(r.TotalAmount), 0)
            FROM Requisitions r
            INNER JOIN Users u ON r.UserId = u.UserId
            WHERE u.DepartmentId = d.DepartmentId
            AND r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
            AND YEAR(r.CreatedAt) = YEAR(GETDATE())
        ) > d.Budget
    """) or {"count": 0}

    return {
        "overview": {
            "totalBudget": total,
            "available": available,
            "availablePercent": round(available / total * 100) if total > 0 else 0,
            "spent": spent,
            "spentPercent": round(spent / total * 100) if total > 0 else 0,
            "overBudgetDepts": over["count"],
        }
    }


@router.get("/budgets/departments")
async def get_department_budgets(session_id: int = Query(...)):
    """Get per-department budget details."""
    require_admin_session(session_id)

    rows = execute_query("""
        SELECT
            d.DepartmentId AS id,
            d.DepartmentName AS name,
            ISNULL(d.Budget, 0) AS budget,
            ISNULL((
                SELECT SUM(r.TotalAmount)
                FROM Requisitions r
                INNER JOIN Users u ON r.UserId = u.UserId
                WHERE u.DepartmentId = d.DepartmentId
                AND r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
                AND YEAR(r.CreatedAt) = YEAR(GETDATE())
            ), 0) AS spent,
            (SELECT COUNT(*) FROM Users u WHERE u.DepartmentId = d.DepartmentId) AS users
        FROM Departments d
        ORDER BY d.DepartmentName
    """)

    departments = []
    for r in rows:
        budget = float(r["budget"])
        spent = float(r["spent"])
        remaining = budget - spent
        departments.append({
            "id": r["id"],
            "name": r["name"],
            "budget": budget,
            "spent": spent,
            "remaining": remaining,
            "percent": round(spent / budget * 100) if budget > 0 else 0,
            "users": r["users"],
        })

    return {"departments": departments}


@router.get("/budgets/users")
async def get_user_budgets(
    session_id: int = Query(...),
    search: str = Query(""),
    department: str = Query(""),
):
    """Get per-user budget details."""
    require_admin_session(session_id)

    conditions = []
    params = []

    if search:
        conditions.append("(u.FirstName + ' ' + u.LastName LIKE ? OR u.Email LIKE ?)")
        like = f"%{search}%"
        params.extend([like, like])

    if department:
        conditions.append("d.DepartmentName = ?")
        params.append(department)

    where = "WHERE " + " AND ".join(conditions) if conditions else ""

    rows = execute_query(f"""
        SELECT
            u.UserId AS id,
            u.FirstName + ' ' + u.LastName AS name,
            u.Email AS email,
            ISNULL(d.DepartmentName, '') AS department,
            ISNULL(u.Budget, 0) AS budget,
            ISNULL((
                SELECT SUM(r.TotalAmount)
                FROM Requisitions r
                WHERE r.UserId = u.UserId
                AND r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
                AND YEAR(r.CreatedAt) = YEAR(GETDATE())
            ), 0) AS spent
        FROM Users u
        LEFT JOIN Departments d ON u.DepartmentId = d.DepartmentId
        {where}
        ORDER BY u.LastName, u.FirstName
    """, tuple(params) if params else None)

    user_budgets = []
    for r in rows:
        budget = float(r["budget"])
        spent = float(r["spent"])
        user_budgets.append({
            "id": r["id"],
            "name": r["name"] or "Unknown",
            "email": r["email"] or "",
            "department": r["department"],
            "budget": budget,
            "spent": spent,
            "remaining": budget - spent,
            "percent": round(spent / budget * 100) if budget > 0 else 0,
        })

    return {"userBudgets": user_budgets}


# ===========================================
# REPORTS ENDPOINTS
# ===========================================

@router.get("/reports/summary")
async def get_report_summary(
    session_id: int = Query(...),
    date_range: str = Query("this_month"),
    department: str = Query("all"),
):
    """Get report summary statistics."""
    require_admin_session(session_id)

    # Build date filter
    date_filter = ""
    if date_range == "this_week":
        date_filter = "AND r.CreatedAt >= DATEADD(WEEK, -1, GETDATE())"
    elif date_range == "this_month":
        date_filter = "AND r.CreatedAt >= DATEADD(MONTH, -1, GETDATE())"
    elif date_range == "this_quarter":
        date_filter = "AND r.CreatedAt >= DATEADD(QUARTER, -1, GETDATE())"
    elif date_range == "this_year":
        date_filter = "AND YEAR(r.CreatedAt) = YEAR(GETDATE())"

    dept_filter = ""
    params = []
    if department and department != "all":
        dept_filter = "AND d.DepartmentName = ?"
        params.append(department)

    result = execute_single(f"""
        SELECT
            ISNULL(SUM(r.TotalAmount), 0) AS totalSpend,
            COUNT(*) AS totalOrders,
            COUNT(DISTINCT r.UserId) AS activeUsers,
            ISNULL(SUM(rd_count.item_count), 0) AS totalItems
        FROM Requisitions r
        LEFT JOIN Users u ON r.UserId = u.UserId
        LEFT JOIN Departments d ON u.DepartmentId = d.DepartmentId
        LEFT JOIN (
            SELECT RequisitionId, SUM(Quantity) AS item_count
            FROM RequisitionDetails
            GROUP BY RequisitionId
        ) rd_count ON rd_count.RequisitionId = r.RequisitionId
        WHERE r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
        {date_filter}
        {dept_filter}
    """, tuple(params) if params else None) or {
        "totalSpend": 0, "totalOrders": 0, "activeUsers": 0, "totalItems": 0
    }

    total_orders = result["totalOrders"] or 1
    total_spend = float(result["totalSpend"])
    active_users = result["activeUsers"] or 1

    # Budget total
    budget_result = execute_single("SELECT ISNULL(SUM(Budget), 0) AS total FROM Departments")
    total_budget = float(budget_result["total"]) if budget_result else 0

    # Unique products
    unique_products = execute_single(f"""
        SELECT COUNT(DISTINCT rd.ItemId) AS count
        FROM RequisitionDetails rd
        INNER JOIN Requisitions r ON rd.RequisitionId = r.RequisitionId
        LEFT JOIN Users u ON r.UserId = u.UserId
        LEFT JOIN Departments d ON u.DepartmentId = d.DepartmentId
        WHERE r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
        {date_filter}
        {dept_filter}
    """, tuple(params) if params else None) or {"count": 0}

    return {
        "summary": {
            "totalSpend": total_spend,
            "totalOrders": result["totalOrders"] or 0,
            "avgOrderValue": round(total_spend / total_orders, 2) if total_orders > 0 else 0,
            "totalItems": result["totalItems"] or 0,
            "uniqueProducts": unique_products["count"] or 0,
            "activeUsers": result["activeUsers"] or 0,
            "ordersPerUser": round(total_orders / active_users, 1) if active_users > 0 else 0,
            "totalBudget": total_budget,
        }
    }


@router.get("/reports/by-department")
async def get_report_by_department(
    session_id: int = Query(...),
    date_range: str = Query("this_month"),
):
    """Get per-department report data."""
    require_admin_session(session_id)

    date_filter = ""
    if date_range == "this_week":
        date_filter = "AND r.CreatedAt >= DATEADD(WEEK, -1, GETDATE())"
    elif date_range == "this_month":
        date_filter = "AND r.CreatedAt >= DATEADD(MONTH, -1, GETDATE())"
    elif date_range == "this_quarter":
        date_filter = "AND r.CreatedAt >= DATEADD(QUARTER, -1, GETDATE())"
    elif date_range == "this_year":
        date_filter = "AND YEAR(r.CreatedAt) = YEAR(GETDATE())"

    rows = execute_query(f"""
        SELECT
            d.DepartmentName AS name,
            COUNT(r.RequisitionId) AS orders,
            ISNULL(SUM(rd_count.item_count), 0) AS items,
            ISNULL(SUM(r.TotalAmount), 0) AS spend,
            ISNULL(d.Budget, 0) AS budget
        FROM Departments d
        LEFT JOIN Users u ON u.DepartmentId = d.DepartmentId
        LEFT JOIN Requisitions r ON r.UserId = u.UserId
            AND r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
            {date_filter}
        LEFT JOIN (
            SELECT RequisitionId, SUM(Quantity) AS item_count
            FROM RequisitionDetails
            GROUP BY RequisitionId
        ) rd_count ON rd_count.RequisitionId = r.RequisitionId
        GROUP BY d.DepartmentName, d.Budget
        ORDER BY spend DESC
    """)

    colors = ['#6366f1', '#f59e0b', '#10b981', '#ec4899', '#8b5cf6', '#14b8a6',
              '#ef4444', '#3b82f6', '#f97316', '#06b6d4']
    departments = []
    for i, r in enumerate(rows):
        budget = float(r["budget"]) or 0
        spend = float(r["spend"])
        departments.append({
            "name": r["name"],
            "orders": r["orders"] or 0,
            "items": r["items"] or 0,
            "spend": spend,
            "budget": budget,
            "percentUsed": round(spend / budget * 100) if budget > 0 else 0,
            "color": colors[i % len(colors)],
        })

    return {"departments": departments}


@router.get("/reports/top-products")
async def get_report_top_products(
    session_id: int = Query(...),
    date_range: str = Query("this_month"),
    limit: int = Query(10, ge=1, le=50),
):
    """Get top products for reports."""
    require_admin_session(session_id)

    date_filter = ""
    if date_range == "this_week":
        date_filter = "AND r.CreatedAt >= DATEADD(WEEK, -1, GETDATE())"
    elif date_range == "this_month":
        date_filter = "AND r.CreatedAt >= DATEADD(MONTH, -1, GETDATE())"
    elif date_range == "this_quarter":
        date_filter = "AND r.CreatedAt >= DATEADD(QUARTER, -1, GETDATE())"
    elif date_range == "this_year":
        date_filter = "AND YEAR(r.CreatedAt) = YEAR(GETDATE())"

    rows = execute_query(f"""
        SELECT TOP (?)
            i.ItemId AS id,
            i.ItemName AS name,
            ISNULL(cr.VendorItemCode, '') AS sku,
            ISNULL(c.CategoryName, 'General') AS category,
            SUM(rd.Quantity) AS quantity,
            AVG(rd.UnitPrice) AS unitPrice,
            SUM(rd.Quantity * rd.UnitPrice) AS totalSpend
        FROM RequisitionDetails rd
        INNER JOIN Items i ON rd.ItemId = i.ItemId
        INNER JOIN Requisitions r ON rd.RequisitionId = r.RequisitionId
        LEFT JOIN CrossRefs cr ON i.ItemId = cr.ItemId
        LEFT JOIN Category c ON i.CategoryId = c.CategoryId
        WHERE r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
        {date_filter}
        GROUP BY i.ItemId, i.ItemName, cr.VendorItemCode, c.CategoryName
        ORDER BY totalSpend DESC
    """, (limit,))

    return {
        "topProducts": [
            {
                "id": r["id"],
                "name": r["name"],
                "sku": r["sku"],
                "category": r["category"],
                "quantity": r["quantity"],
                "unitPrice": round(float(r["unitPrice"]), 2),
                "totalSpend": round(float(r["totalSpend"]), 2),
            }
            for r in rows
        ]
    }


@router.get("/reports/top-users")
async def get_report_top_users(
    session_id: int = Query(...),
    date_range: str = Query("this_month"),
    limit: int = Query(10, ge=1, le=50),
):
    """Get top users by spending for reports."""
    require_admin_session(session_id)

    date_filter = ""
    if date_range == "this_month":
        date_filter = "AND r.CreatedAt >= DATEADD(MONTH, -1, GETDATE())"
    elif date_range == "this_quarter":
        date_filter = "AND r.CreatedAt >= DATEADD(QUARTER, -1, GETDATE())"
    elif date_range == "this_year":
        date_filter = "AND YEAR(r.CreatedAt) = YEAR(GETDATE())"

    rows = execute_query(f"""
        SELECT TOP (?)
            u.UserId AS id,
            u.FirstName + ' ' + u.LastName AS name,
            u.Email AS email,
            ISNULL(d.DepartmentName, '') AS department,
            COUNT(r.RequisitionId) AS orders,
            ISNULL(SUM(rd_count.item_count), 0) AS items,
            ISNULL(SUM(r.TotalAmount), 0) AS totalSpend
        FROM Users u
        INNER JOIN Requisitions r ON r.UserId = u.UserId
        LEFT JOIN Departments d ON u.DepartmentId = d.DepartmentId
        LEFT JOIN (
            SELECT RequisitionId, SUM(Quantity) AS item_count
            FROM RequisitionDetails
            GROUP BY RequisitionId
        ) rd_count ON rd_count.RequisitionId = r.RequisitionId
        WHERE r.Status NOT IN ('Cancelled', 'Rejected', 'Draft')
        {date_filter}
        GROUP BY u.UserId, u.FirstName, u.LastName, u.Email, d.DepartmentName
        ORDER BY totalSpend DESC
    """, (limit,))

    return {
        "topUsers": [
            {
                "id": r["id"],
                "name": r["name"] or "Unknown",
                "email": r["email"] or "",
                "department": r["department"],
                "orders": r["orders"],
                "items": r["items"] or 0,
                "totalSpend": round(float(r["totalSpend"]), 2),
            }
            for r in rows
        ]
    }


# ===========================================
# SEARCH INDEX MANAGEMENT
# ===========================================

# Track background reindex state
_reindex_state = {
    "running": False,
    "last_run": None,
    "last_result": None,
    "error": None,
}


def _run_reindex(full: bool = False):
    """Run the Elasticsearch reindex in-process (for background task)."""
    import time
    from api.search import ES_ENABLED

    if not ES_ENABLED:
        _reindex_state["error"] = "Elasticsearch is not enabled (ES_ENABLED=false)"
        _reindex_state["running"] = False
        return

    _reindex_state["running"] = True
    _reindex_state["error"] = None
    start = time.time()

    try:
        from scripts.index_elasticsearch import (
            get_es_client, get_db_connection, recreate_index,
            index_products, count_products, ES_INDEX,
        )

        es = get_es_client()
        info = es.info()
        logger.info(f"Reindex: connected to ES {info['version']['number']}")

        conn = get_db_connection()
        total_eligible = count_products(conn)

        if full:
            recreate_index(es)

        indexed, errors = index_products(es, conn)

        doc_count = es.count(index=ES_INDEX)["count"]
        conn.close()
        es.close()

        elapsed = time.time() - start
        _reindex_state["last_result"] = {
            "indexed": indexed,
            "errors": errors,
            "eligible": total_eligible,
            "doc_count": doc_count,
            "full_reindex": full,
            "elapsed_seconds": round(elapsed, 1),
        }
        _reindex_state["last_run"] = datetime.utcnow().isoformat() + "Z"
        logger.info(f"Reindex complete: {indexed} indexed, {errors} errors, {elapsed:.1f}s")

    except Exception as e:
        _reindex_state["error"] = str(e)
        logger.error(f"Reindex failed: {e}")
    finally:
        _reindex_state["running"] = False


@router.post("/search/reindex")
async def trigger_reindex(
    background_tasks: BackgroundTasks,
    full: bool = Query(False, description="Full reindex (drop and recreate index)"),
):
    """
    Trigger an Elasticsearch reindex.

    - **full=false** (default): Append/update products into existing index
    - **full=true**: Drop and recreate the index, then reindex all products

    Runs in the background. Check status via GET /api/admin/search/status.
    """
    if _reindex_state["running"]:
        raise HTTPException(status_code=409, detail="Reindex already in progress")

    background_tasks.add_task(_run_reindex, full=full)
    return {
        "message": f"{'Full' if full else 'Incremental'} reindex started in background",
        "check_status": "/api/admin/search/status",
    }


@router.get("/search/status")
async def search_index_status():
    """
    Get Elasticsearch index status and last reindex result.
    """
    from api.search import get_es_client, ES_ENABLED, ES_INDEX

    status = {
        "enabled": ES_ENABLED,
        "reindex_running": _reindex_state["running"],
        "last_run": _reindex_state["last_run"],
        "last_result": _reindex_state["last_result"],
        "last_error": _reindex_state["error"],
    }

    # Get live index stats if ES is available
    client = get_es_client()
    if client is not None:
        try:
            exists = await client.indices.exists(index=ES_INDEX)
            if exists:
                count = await client.count(index=ES_INDEX)
                stats = await client.indices.stats(index=ES_INDEX)
                index_stats = stats.get("indices", {}).get(ES_INDEX, {}).get("total", {})
                status["index"] = {
                    "exists": True,
                    "doc_count": count.get("count", 0),
                    "size_bytes": index_stats.get("store", {}).get("size_in_bytes", 0),
                    "size_mb": round(index_stats.get("store", {}).get("size_in_bytes", 0) / 1024 / 1024, 1),
                }
            else:
                status["index"] = {"exists": False}
        except Exception as e:
            status["index"] = {"error": str(e)}
    else:
        status["index"] = {"unavailable": True}

    return status
