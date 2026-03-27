"""
Investigation: Burnt Hills-Ballston Lake Requisition #1388 (PO 261949)
Allegation: Quantities changed and item added without requisitioner's knowledge
Date of alleged changes: around 3/4/2026
Items in question:
  - DBCC20508-5071 (allegedly added - sky blue, 36 qty)
  - DBC20508-8141 (qty changed)
  - DBC21315-2003 (qty changed)
  - EDS00563 (qty changed)
"""

import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("C:/EDS/.env")

SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_DATABASE_CATALOG")  # EDS database
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    f"TrustServerCertificate=yes;"
)

def run_query(cursor, title, sql, params=None):
    print(f"\n{'='*80}")
    print(f"  {title}")
    print(f"{'='*80}")
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        columns = [col[0] for col in cursor.description] if cursor.description else []
        rows = cursor.fetchall()
        if not rows:
            print("  (no results)")
            return rows
        # Print header
        print("  " + " | ".join(columns))
        print("  " + "-+-".join(["-" * max(len(c), 12) for c in columns]))
        for row in rows:
            vals = []
            for v in row:
                if v is None:
                    vals.append("NULL")
                elif isinstance(v, datetime):
                    vals.append(v.strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    vals.append(str(v))
            print("  " + " | ".join(vals))
        print(f"  ({len(rows)} row(s))")
        return rows
    except Exception as e:
        print(f"  ERROR: {e}")
        return []


def main():
    print("Connecting to EDS database...")
    conn = pyodbc.connect(conn_str, timeout=30)
    cursor = conn.cursor()
    print("Connected successfully.\n")

    # =========================================================================
    # 1. Find EntityId / DistrictId for Burnt Hills-Ballston Lake
    # =========================================================================
    run_query(cursor, "1. FIND DISTRICT: Burnt Hills-Ballston Lake",
        """
        SELECT TOP 10 DistrictId, DistrictName, DistrictCode, Active
        FROM District
        WHERE DistrictName LIKE '%Burnt Hills%'
           OR DistrictName LIKE '%Ballston%'
        """)

    # =========================================================================
    # 2. Find Requisition 1388 header info
    # =========================================================================
    run_query(cursor, "2. REQUISITION HEADER: Req# 1388 for Burnt Hills",
        """
        SELECT r.RequisitionId, r.RequisitionNumber, r.SchoolId, r.UserId,
               r.BudgetId, r.CategoryId, r.DateEntered, r.StatusId, r.OrderDate,
               r.TotalItemsCost, r.TotalRequisitionCost, r.Comments,
               r.LastAlteredSessionId, r.DateUpdated, r.BidHeaderId,
               r.ApprovalRequired, r.ApprovalLevel, r.HistoryCount
        FROM Requisitions r
        JOIN District d ON r.BudgetId IN (
            SELECT BudgetId FROM Budgets WHERE DistrictId = d.DistrictId
        )
        WHERE r.RequisitionNumber = '1388'
          AND d.DistrictName LIKE '%Burnt Hills%'
        """)

    # Let's try a broader approach - find the requisition via PO 261949
    run_query(cursor, "2b. FIND REQUISITION via PO# 261949",
        """
        SELECT TOP 5 po.POId, po.RequisitionId, po.VendorId, po.PONumber,
               po.PODate, po.Amount, po.ItemCount,
               r.RequisitionNumber, r.UserId, r.SchoolId, r.BudgetId,
               r.DateEntered, r.StatusId, r.LastAlteredSessionId, r.DateUpdated,
               r.BidHeaderId
        FROM PO po
        JOIN Requisitions r ON po.RequisitionId = r.RequisitionId
        WHERE po.PONumber = '261949'
        """)

    # =========================================================================
    # 3. Get the RequisitionId from PO 261949 for further queries
    # =========================================================================
    cursor.execute("SELECT TOP 1 RequisitionId FROM PO WHERE PONumber = '261949'")
    row = cursor.fetchone()
    if not row:
        print("\n*** Could not find PO 261949. Trying broader search...")
        # Try finding requisition 1388 directly
        cursor.execute("""
            SELECT TOP 20 r.RequisitionId, r.RequisitionNumber, r.BudgetId, r.UserId,
                   b.DistrictId, d.DistrictName
            FROM Requisitions r
            JOIN Budgets b ON r.BudgetId = b.BudgetId
            JOIN District d ON b.DistrictId = d.DistrictId
            WHERE r.RequisitionNumber = '1388'
              AND d.DistrictName LIKE '%Burnt Hills%'
        """)
        rows = cursor.fetchall()
        if rows:
            cols = [c[0] for c in cursor.description]
            print("  Found requisitions:")
            print("  " + " | ".join(cols))
            for r in rows:
                print("  " + " | ".join(str(v) for v in r))
            req_id = rows[0][0]
        else:
            print("  No matching requisition found. Exiting.")
            return
    else:
        req_id = row[0]

    print(f"\n>>> Using RequisitionId = {req_id}")

    # =========================================================================
    # 4. Detail lines for this requisition
    # =========================================================================
    run_query(cursor, "3. ALL DETAIL LINES for this requisition",
        """
        SELECT d.DetailId, d.RequisitionId, d.ItemCode, d.Quantity,
               d.Description, d.BidPrice, d.CatalogPrice,
               d.VendorId, d.VendorItemCode, d.POId,
               d.Modified, d.ModifiedById, d.SessionId,
               d.LastAlteredSessionId, d.Active, d.AddendumItem,
               i.ItemCode AS ItemTableCode
        FROM Detail d
        LEFT JOIN Items i ON d.ItemId = i.ItemId
        WHERE d.RequisitionId = ?
        ORDER BY d.DetailId
        """, (req_id,))

    # =========================================================================
    # 5. Focus on the specific items mentioned
    # =========================================================================
    run_query(cursor, "4. SPECIFIC ITEMS of interest",
        """
        SELECT d.DetailId, d.ItemCode, d.Quantity, d.Description,
               d.BidPrice, d.Modified, d.ModifiedById, d.SessionId,
               d.LastAlteredSessionId, d.Active, d.AddendumItem
        FROM Detail d
        WHERE d.RequisitionId = ?
          AND (d.ItemCode LIKE '%20508-5071%'
               OR d.ItemCode LIKE '%20508-8141%'
               OR d.ItemCode LIKE '%21315-2003%'
               OR d.ItemCode LIKE '%EDS00563%'
               OR d.ItemCode LIKE '%DBCC20508%'
               OR d.ItemCode LIKE '%DBC20508%'
               OR d.ItemCode LIKE '%DBC21315%')
        """, (req_id,))

    # =========================================================================
    # 6. DetailChangeLog - audit trail for this requisition
    # =========================================================================
    run_query(cursor, "5. DETAIL CHANGE LOG (audit trail with UserId)",
        """
        SELECT dcl.DetailChangeId, dcl.DetailId, dcl.RequisitionId,
               dcl.ItemId, dcl.OrigQty, dcl.NewQty,
               dcl.OrigBidPrice, dcl.NewBidPrice,
               dcl.UserId, dcl.SessionId, dcl.ChangeDate,
               dcl.OrigVendorId, dcl.NewVendorId,
               i.ItemCode
        FROM DetailChangeLog dcl
        LEFT JOIN Items i ON dcl.ItemId = i.ItemId
        WHERE dcl.RequisitionId = ?
        ORDER BY dcl.ChangeDate DESC
        """, (req_id,))

    # =========================================================================
    # 7. DetailChanges - another change tracking table (no UserId)
    # =========================================================================
    run_query(cursor, "6. DETAIL CHANGES (change history)",
        """
        SELECT dc.DetailChangeId, dc.DetailId, dc.ChangeDate,
               dc.OrigQty, dc.NewQty, dc.RequisitionId,
               dc.ItemId, dc.BidPrice, dc.BidItemId,
               i.ItemCode
        FROM DetailChanges dc
        LEFT JOIN Items i ON dc.ItemId = i.ItemId
        WHERE dc.RequisitionId = ?
        ORDER BY dc.ChangeDate DESC
        """, (req_id,))

    # =========================================================================
    # 8. RequisitionChangeLog - header-level changes
    # =========================================================================
    run_query(cursor, "7. REQUISITION CHANGE LOG (header-level changes)",
        """
        SELECT rcl.RequisitionChangeId, rcl.RequisitionId,
               rcl.OrigUserId, rcl.NewUserId,
               rcl.OrigSchoolId, rcl.NewSchoolId,
               rcl.OrigBudgetId, rcl.NewBudgetId,
               rcl.UserId, rcl.SessionId, rcl.ChangeDate
        FROM RequisitionChangeLog rcl
        WHERE rcl.RequisitionId = ?
        ORDER BY rcl.ChangeDate DESC
        """, (req_id,))

    # =========================================================================
    # 9. Resolve UserIds to names
    # =========================================================================
    # First get all UserIds we've seen
    cursor.execute("""
        SELECT DISTINCT UserId FROM (
            SELECT UserId FROM DetailChangeLog WHERE RequisitionId = ?
            UNION
            SELECT ModifiedById FROM Detail WHERE RequisitionId = ? AND ModifiedById IS NOT NULL
            UNION
            SELECT UserId FROM RequisitionChangeLog WHERE RequisitionId = ?
            UNION
            SELECT UserId FROM Requisitions WHERE RequisitionId = ?
        ) x WHERE UserId IS NOT NULL
    """, (req_id, req_id, req_id, req_id))
    user_ids = [r[0] for r in cursor.fetchall()]

    if user_ids:
        placeholders = ','.join(['?'] * len(user_ids))
        run_query(cursor, "8. USER DETAILS for all involved UserIds",
            f"""
            SELECT u.UserId, u.UserName, u.FirstName, u.LastName, u.Email,
                   u.Active, u.UserType
            FROM Users u
            WHERE u.UserId IN ({placeholders})
            """, tuple(user_ids))

    # =========================================================================
    # 10. Session details for sessions that touched this requisition
    # =========================================================================
    cursor.execute("""
        SELECT DISTINCT SessionId FROM (
            SELECT SessionId FROM DetailChangeLog WHERE RequisitionId = ? AND SessionId IS NOT NULL
            UNION
            SELECT SessionId FROM Detail WHERE RequisitionId = ? AND SessionId IS NOT NULL
            UNION
            SELECT LastAlteredSessionId FROM Detail WHERE RequisitionId = ? AND LastAlteredSessionId IS NOT NULL
            UNION
            SELECT SessionId FROM RequisitionChangeLog WHERE RequisitionId = ? AND SessionId IS NOT NULL
            UNION
            SELECT LastAlteredSessionId FROM Requisitions WHERE RequisitionId = ? AND LastAlteredSessionId IS NOT NULL
        ) x
    """, (req_id, req_id, req_id, req_id, req_id))
    session_ids = [r[0] for r in cursor.fetchall()]

    if session_ids:
        placeholders = ','.join(['?'] * len(session_ids))
        run_query(cursor, "9. SESSION DETAILS for all sessions touching this requisition",
            f"""
            SELECT s.SessionId, s.DistrictId, s.SchoolId, s.UserId,
                   s.RequisitionId, s.SessionStart, s.SessionEnd, s.SessionLast,
                   s.CSRepId, s.RepUserId,
                   u.UserName, u.FirstName, u.LastName
            FROM SessionTable s
            LEFT JOIN Users u ON s.UserId = u.UserId
            WHERE s.SessionId IN ({placeholders})
            ORDER BY s.SessionStart
            """, tuple(session_ids))

    # =========================================================================
    # 11. Look for sessions around 3/4/2026 for this district
    # =========================================================================
    # First get district ID
    cursor.execute("""
        SELECT TOP 1 b.DistrictId
        FROM Requisitions r
        JOIN Budgets b ON r.BudgetId = b.BudgetId
        WHERE r.RequisitionId = ?
    """, (req_id,))
    dist_row = cursor.fetchone()
    if dist_row:
        district_id = dist_row[0]
        run_query(cursor, f"10. ALL SESSIONS for District {district_id} on 3/3-3/5/2026",
            """
            SELECT s.SessionId, s.UserId, s.SchoolId, s.RequisitionId,
                   s.SessionStart, s.SessionEnd, s.SessionLast,
                   s.CSRepId, s.RepUserId,
                   u.UserName, u.FirstName, u.LastName, u.Email
            FROM SessionTable s
            LEFT JOIN Users u ON s.UserId = u.UserId
            WHERE s.DistrictId = ?
              AND s.SessionStart >= '2026-03-03'
              AND s.SessionStart < '2026-03-06'
            ORDER BY s.SessionStart
            """, (district_id,))

        # Also check if a CSRep was involved
        run_query(cursor, "11. SESSIONS WITH CSRep for this district around 3/4/2026",
            """
            SELECT s.SessionId, s.UserId, s.SchoolId, s.RequisitionId,
                   s.SessionStart, s.SessionLast,
                   s.CSRepId, s.RepUserId,
                   u.UserName AS SessionUser, u.FirstName, u.LastName,
                   rep.UserName AS RepUserName, rep.FirstName AS RepFirst, rep.LastName AS RepLast
            FROM SessionTable s
            LEFT JOIN Users u ON s.UserId = u.UserId
            LEFT JOIN Users rep ON s.RepUserId = rep.UserId
            WHERE s.DistrictId = ?
              AND s.CSRepId IS NOT NULL
              AND s.SessionStart >= '2026-03-01'
              AND s.SessionStart < '2026-03-10'
            ORDER BY s.SessionStart
            """, (district_id,))

    # =========================================================================
    # 12. Check RequisitionNotes for any notes around the change date
    # =========================================================================
    run_query(cursor, "12. REQUISITION NOTES",
        """
        SELECT rn.RequisitionNoteID, rn.RequisitionId, rn.UserId,
               rn.NoteDate, rn.Note, rn.NoteType,
               u.UserName, u.FirstName, u.LastName
        FROM RequisitionNotes rn
        LEFT JOIN Users u ON rn.UserId = u.UserId
        WHERE rn.RequisitionId = ?
        ORDER BY rn.NoteDate DESC
        """, (req_id,))

    # =========================================================================
    # 13. Check PO details for comparison
    # =========================================================================
    run_query(cursor, "13. PO 261949 DETAILS",
        """
        SELECT po.POId, po.PONumber, po.VendorId, po.PODate,
               po.Amount, po.ItemCount, po.DatePrinted, po.DateExported,
               po.DateOrdered, po.Cancelled,
               v.VendorName
        FROM PO po
        LEFT JOIN Vendors v ON po.VendorId = v.VendorId
        WHERE po.PONumber = '261949'
        """)

    # =========================================================================
    # 14. Changes specifically around 3/4/2026 with user details
    # =========================================================================
    run_query(cursor, "14. DETAIL CHANGES around 3/3-3/5/2026 with USER INFO",
        """
        SELECT dcl.DetailChangeId, dcl.DetailId,
               dcl.OrigQty, dcl.NewQty,
               dcl.OrigBidPrice, dcl.NewBidPrice,
               dcl.UserId, dcl.SessionId, dcl.ChangeDate,
               i.ItemCode,
               u.UserName, u.FirstName, u.LastName, u.Email,
               s.CSRepId, s.RepUserId,
               rep.UserName AS RepUserName, rep.FirstName AS RepFirst, rep.LastName AS RepLast
        FROM DetailChangeLog dcl
        LEFT JOIN Items i ON dcl.ItemId = i.ItemId
        LEFT JOIN Users u ON dcl.UserId = u.UserId
        LEFT JOIN SessionTable s ON dcl.SessionId = s.SessionId
        LEFT JOIN Users rep ON s.RepUserId = rep.UserId
        WHERE dcl.RequisitionId = ?
          AND dcl.ChangeDate >= '2026-03-03'
          AND dcl.ChangeDate < '2026-03-06'
        ORDER BY dcl.ChangeDate
        """, (req_id,))

    # =========================================================================
    # 15. Check if the "sky blue" item was added (look for items with OrigQty=0 or NULL)
    # =========================================================================
    run_query(cursor, "15. ITEMS POSSIBLY ADDED (OrigQty=0 or NULL in change log)",
        """
        SELECT dcl.DetailChangeId, dcl.DetailId,
               dcl.OrigQty, dcl.NewQty,
               dcl.UserId, dcl.SessionId, dcl.ChangeDate,
               i.ItemCode, i.Description,
               u.UserName, u.FirstName, u.LastName
        FROM DetailChangeLog dcl
        LEFT JOIN Items i ON dcl.ItemId = i.ItemId
        LEFT JOIN Users u ON dcl.UserId = u.UserId
        WHERE dcl.RequisitionId = ?
          AND (dcl.OrigQty = 0 OR dcl.OrigQty IS NULL)
          AND dcl.NewQty > 0
        ORDER BY dcl.ChangeDate DESC
        """, (req_id,))

    # =========================================================================
    # 16. Look at the specific detail line Modified/ModifiedBy for the items
    # =========================================================================
    run_query(cursor, "16. MODIFIED BY INFO on Detail lines",
        """
        SELECT d.DetailId, d.ItemCode, d.Quantity, d.Description,
               d.Modified, d.ModifiedById,
               d.SessionId, d.LastAlteredSessionId,
               u.UserName AS ModifiedByUser, u.FirstName AS ModByFirst, u.LastName AS ModByLast,
               s.UserId AS SessionUserId, s.CSRepId, s.RepUserId,
               su.UserName AS SessionUserName, su.FirstName AS SessFirst, su.LastName AS SessLast
        FROM Detail d
        LEFT JOIN Users u ON d.ModifiedById = u.UserId
        LEFT JOIN SessionTable s ON d.LastAlteredSessionId = s.SessionId
        LEFT JOIN Users su ON s.UserId = su.UserId
        WHERE d.RequisitionId = ?
          AND (d.ItemCode LIKE '%20508-5071%'
               OR d.ItemCode LIKE '%20508-8141%'
               OR d.ItemCode LIKE '%21315-2003%'
               OR d.ItemCode LIKE '%EDS00563%'
               OR d.ItemCode LIKE '%DBCC20508%'
               OR d.ItemCode LIKE '%DBC20508%'
               OR d.ItemCode LIKE '%DBC21315%')
        """, (req_id,))

    # =========================================================================
    # 17. Find Lisa Johnson's UserId
    # =========================================================================
    run_query(cursor, "17. FIND Lisa Johnson",
        """
        SELECT TOP 10 u.UserId, u.UserName, u.FirstName, u.LastName, u.Email,
               u.Active, u.UserType, u.DistrictId
        FROM Users u
        WHERE (u.FirstName LIKE '%Lisa%' AND u.LastName LIKE '%Johnson%')
        ORDER BY u.Active DESC, u.UserId
        """)

    print("\n" + "="*80)
    print("  INVESTIGATION COMPLETE")
    print("="*80)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
