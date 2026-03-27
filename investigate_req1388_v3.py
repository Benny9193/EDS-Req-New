"""
Investigation v3: Burnt Hills-Ballston Lake Requisition #1388
RequisitionId = 60159579, DistrictId = 728
Deep dive into audit trails, sessions, and user activity.
"""

import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("C:/EDS/.env")

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_DATABASE_CATALOG')};"
    f"UID={os.getenv('DB_USERNAME')};"
    f"PWD={os.getenv('DB_PASSWORD')};"
    f"TrustServerCertificate=yes;"
)

REQ_ID = 60159579
DISTRICT_ID = 728

def run_query(cursor, title, sql, params=None):
    print(f"\n{'='*120}")
    print(f"  {title}")
    print(f"{'='*120}")
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
        widths = [len(c) for c in columns]
        str_rows = []
        for row in rows:
            vals = []
            for idx, v in enumerate(row):
                if v is None:
                    s = "NULL"
                elif isinstance(v, datetime):
                    s = v.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    s = str(v)[:80]
                vals.append(s)
                if len(s) > widths[idx]:
                    widths[idx] = min(len(s), 80)
            str_rows.append(vals)
        header = " | ".join(c.ljust(widths[i]) for i, c in enumerate(columns))
        print(f"  {header}")
        print(f"  {'-+-'.join('-' * w for w in widths)}")
        for vals in str_rows:
            line = " | ".join(v.ljust(widths[i]) for i, v in enumerate(vals))
            print(f"  {line}")
        print(f"  ({len(rows)} row(s))")
        return rows
    except Exception as e:
        print(f"  ERROR: {e}")
        return []


def main():
    conn = pyodbc.connect(conn_str, timeout=30)
    cursor = conn.cursor()
    print(f"Connected. Investigating RequisitionId={REQ_ID}, DistrictId={DISTRICT_ID}\n")

    # =========================================================================
    # 1. Requisition header
    # =========================================================================
    run_query(cursor, "1. REQUISITION HEADER",
        """
        SELECT r.RequisitionId, r.RequisitionNumber, r.SchoolId, r.UserId,
               r.BudgetId, r.CategoryId, r.DateEntered, r.StatusId, r.OrderDate,
               r.TotalItemsCost, r.TotalRequisitionCost, r.Comments,
               r.LastAlteredSessionId, r.DateUpdated, r.BidHeaderId,
               r.ApprovalRequired, r.ApprovalLevel, r.HistoryCount,
               r.Active
        FROM Requisitions r
        WHERE r.RequisitionId = ?
        """, (REQ_ID,))

    # =========================================================================
    # 2. User who owns this requisition
    # =========================================================================
    run_query(cursor, "2. REQUISITION OWNER (UserId from Requisitions)",
        """
        SELECT u.UserId, u.UserName, u.FirstName, u.LastName, u.Email,
               u.DistrictId, u.SchoolId, u.Active, u.ApprovalLevel, u.SecurityRoleId
        FROM Users u
        WHERE u.UserId = (SELECT UserId FROM Requisitions WHERE RequisitionId = ?)
        """, (REQ_ID,))

    # =========================================================================
    # 3. ALL detail lines
    # =========================================================================
    run_query(cursor, "3. ALL DETAIL LINES for req 1388",
        """
        SELECT d.DetailId, d.RequisitionId, d.ItemCode, d.Quantity,
               LEFT(d.Description, 60) AS Description, d.BidPrice,
               d.VendorId, d.POId,
               d.Modified, d.ModifiedById, d.SessionId,
               d.LastAlteredSessionId, d.Active, d.AddendumItem
        FROM Detail d
        WHERE d.RequisitionId = ?
        ORDER BY d.DetailId
        """, (REQ_ID,))

    # =========================================================================
    # 4. DetailChangeLog - THE KEY AUDIT TABLE (has UserId!)
    # =========================================================================
    run_query(cursor, "4. DETAIL CHANGE LOG - Full audit trail",
        """
        SELECT dcl.DetailChangeId, dcl.DetailId, dcl.RequisitionId,
               dcl.ItemId, i.ItemCode,
               dcl.OrigQty, dcl.NewQty,
               dcl.OrigBidPrice, dcl.NewBidPrice,
               dcl.UserId, dcl.SessionId, dcl.ChangeDate,
               dcl.OrigVendorId, dcl.NewVendorId
        FROM DetailChangeLog dcl
        LEFT JOIN Items i ON dcl.ItemId = i.ItemId
        WHERE dcl.RequisitionId = ?
        ORDER BY dcl.ChangeDate
        """, (REQ_ID,))

    # =========================================================================
    # 5. DetailChanges - secondary change table
    # =========================================================================
    run_query(cursor, "5. DETAIL CHANGES - Secondary change tracking",
        """
        SELECT dc.DetailChangeId, dc.DetailId, dc.ChangeDate,
               dc.OrigQty, dc.NewQty, dc.RequisitionId,
               dc.ItemId, i.ItemCode, dc.BidPrice
        FROM DetailChanges dc
        LEFT JOIN Items i ON dc.ItemId = i.ItemId
        WHERE dc.RequisitionId = ?
        ORDER BY dc.ChangeDate
        """, (REQ_ID,))

    # =========================================================================
    # 6. RequisitionChangeLog - header-level changes
    # =========================================================================
    run_query(cursor, "6. REQUISITION CHANGE LOG",
        """
        SELECT rcl.*, u.UserName, u.FirstName, u.LastName
        FROM RequisitionChangeLog rcl
        LEFT JOIN Users u ON rcl.UserId = u.UserId
        WHERE rcl.RequisitionId = ?
        ORDER BY rcl.ChangeDate
        """, (REQ_ID,))

    # =========================================================================
    # 7. Resolve all UserIds seen in change logs
    # =========================================================================
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
    """, (REQ_ID, REQ_ID, REQ_ID, REQ_ID))
    user_ids = [r[0] for r in cursor.fetchall()]

    if user_ids:
        ph = ','.join(['?'] * len(user_ids))
        run_query(cursor, "7. ALL USERS involved",
            f"""
            SELECT u.UserId, u.UserName, u.FirstName, u.LastName, u.Email,
                   u.DistrictId, u.SchoolId, u.Active, u.SecurityRoleId
            FROM Users u
            WHERE u.UserId IN ({ph})
            """, tuple(user_ids))

    # =========================================================================
    # 8. Session details for all sessions touching this req
    # =========================================================================
    cursor.execute("""
        SELECT DISTINCT SessionId FROM (
            SELECT SessionId FROM DetailChangeLog WHERE RequisitionId = ? AND SessionId IS NOT NULL AND SessionId > 0
            UNION
            SELECT SessionId FROM Detail WHERE RequisitionId = ? AND SessionId IS NOT NULL AND SessionId > 0
            UNION
            SELECT LastAlteredSessionId FROM Detail WHERE RequisitionId = ? AND LastAlteredSessionId IS NOT NULL AND LastAlteredSessionId > 0
            UNION
            SELECT SessionId FROM RequisitionChangeLog WHERE RequisitionId = ? AND SessionId IS NOT NULL AND SessionId > 0
            UNION
            SELECT LastAlteredSessionId FROM Requisitions WHERE RequisitionId = ? AND LastAlteredSessionId IS NOT NULL AND LastAlteredSessionId > 0
        ) x
    """, (REQ_ID, REQ_ID, REQ_ID, REQ_ID, REQ_ID))
    session_ids = [r[0] for r in cursor.fetchall()]

    if session_ids:
        ph = ','.join(['?'] * len(session_ids))
        run_query(cursor, "8. SESSION DETAILS for sessions touching this req",
            f"""
            SELECT s.SessionId, s.DistrictId, s.SchoolId, s.UserId,
                   s.RequisitionId, s.SessionStart, s.SessionEnd, s.SessionLast,
                   s.CSRepId, s.RepUserId,
                   u.UserName, u.FirstName, u.LastName, u.Email
            FROM SessionTable s
            LEFT JOIN Users u ON s.UserId = u.UserId
            WHERE s.SessionId IN ({ph})
            ORDER BY s.SessionStart
            """, tuple(session_ids))

    # =========================================================================
    # 9. All sessions for this district around 3/3-3/6/2026
    # =========================================================================
    run_query(cursor, "9. ALL SESSIONS for District 728 on 3/3-3/6/2026",
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
        """, (DISTRICT_ID,))

    # =========================================================================
    # 10. Sessions WITH CSRep for this district (EDS staff impersonation?)
    # =========================================================================
    run_query(cursor, "10. SESSIONS WITH CSRep (EDS staff) for District 728, Feb-Mar 2026",
        """
        SELECT s.SessionId, s.UserId, s.SchoolId, s.RequisitionId,
               s.SessionStart, s.SessionLast,
               s.CSRepId, s.RepUserId,
               u.UserName AS SessionUser, u.FirstName, u.LastName, u.Email,
               rep.UserName AS RepUserName, rep.FirstName AS RepFirst, rep.LastName AS RepLast, rep.Email AS RepEmail
        FROM SessionTable s
        LEFT JOIN Users u ON s.UserId = u.UserId
        LEFT JOIN Users rep ON s.RepUserId = rep.UserId
        WHERE s.DistrictId = ?
          AND s.CSRepId IS NOT NULL
          AND s.SessionStart >= '2026-02-01'
          AND s.SessionStart < '2026-04-01'
        ORDER BY s.SessionStart
        """, (DISTRICT_ID,))

    # =========================================================================
    # 11. Check the specific session IDs from Detail.SessionId & LastAlteredSessionId
    # =========================================================================
    run_query(cursor, "11. DETAIL SESSION IDs breakdown",
        """
        SELECT d.DetailId, d.ItemCode, d.Quantity, d.Modified,
               d.SessionId AS DetailSessionId,
               d.LastAlteredSessionId AS DetailLastAltSessionId,
               s1.UserId AS SessionUserId, s1.SessionStart AS SessionStart,
               s1.CSRepId, s1.RepUserId,
               u1.UserName AS SessionUserName, u1.FirstName AS SessFirst, u1.LastName AS SessLast,
               s2.UserId AS LastAltUserId, s2.SessionStart AS LastAltStart,
               u2.UserName AS LastAltUserName, u2.FirstName AS LAFirst, u2.LastName AS LALast
        FROM Detail d
        LEFT JOIN SessionTable s1 ON d.SessionId = s1.SessionId AND d.SessionId > 0
        LEFT JOIN Users u1 ON s1.UserId = u1.UserId
        LEFT JOIN SessionTable s2 ON d.LastAlteredSessionId = s2.SessionId AND d.LastAlteredSessionId > 0
        LEFT JOIN Users u2 ON s2.UserId = u2.UserId
        WHERE d.RequisitionId = ?
        ORDER BY d.DetailId
        """, (REQ_ID,))

    # =========================================================================
    # 12. Find Lisa Johnson - broader search
    # =========================================================================
    run_query(cursor, "12a. Search Users for 'Lisa' in District 728",
        """
        SELECT u.UserId, u.UserName, u.FirstName, u.LastName, u.Email,
               u.Active, u.SchoolId
        FROM Users u
        WHERE u.DistrictId = ? AND u.FirstName LIKE '%Lisa%'
        """, (DISTRICT_ID,))

    run_query(cursor, "12b. Search Users for 'Johnson' in District 728",
        """
        SELECT u.UserId, u.UserName, u.FirstName, u.LastName, u.Email,
               u.Active, u.SchoolId
        FROM Users u
        WHERE u.DistrictId = ? AND u.LastName LIKE '%Johnson%'
        """, (DISTRICT_ID,))

    # =========================================================================
    # 13. Who is UserId 1610732 (the req owner)?
    # =========================================================================
    run_query(cursor, "13. UserId 1610732 (requisition owner) details",
        """
        SELECT u.UserId, u.UserName, u.FirstName, u.LastName, u.Email,
               u.DistrictId, u.SchoolId, u.Active, u.ApprovalLevel,
               u.SecurityRoleId, u.ApproverId
        FROM Users u
        WHERE u.UserId = 1610732
        """)

    # =========================================================================
    # 14. POs for this requisition
    # =========================================================================
    run_query(cursor, "14. POs for RequisitionId 60159579",
        """
        SELECT po.POId, po.PONumber, po.VendorId, po.PODate, po.Amount,
               po.ItemCount, po.DatePrinted, po.DateExported, po.DateOrdered,
               po.Cancelled, po.POStatusID,
               v.Name AS VendorName
        FROM PO po
        LEFT JOIN Vendors v ON po.VendorId = v.VendorId
        WHERE po.RequisitionId = ?
        ORDER BY po.PODate
        """, (REQ_ID,))

    # =========================================================================
    # 15. School info for this req's school
    # =========================================================================
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'School' AND DATA_TYPE IN ('varchar','nvarchar') ORDER BY ORDINAL_POSITION")
    school_text_cols = [r[0] for r in cursor.fetchall()]
    print(f"\n  School text columns: {school_text_cols}")

    cursor.execute("SELECT SchoolId FROM Requisitions WHERE RequisitionId = ?", (REQ_ID,))
    school_row = cursor.fetchone()
    if school_row:
        run_query(cursor, f"15. School info for SchoolId {school_row[0]}",
            f"SELECT * FROM School WHERE SchoolId = ?", (school_row[0],))

    # =========================================================================
    # 16. Check if the detail Modified dates are around 3/4 or 3/5
    # =========================================================================
    run_query(cursor, "16. Detail items with Modified dates 3/3-3/6/2026",
        """
        SELECT d.DetailId, d.ItemCode, d.Quantity, d.Description,
               d.Modified, d.ModifiedById, d.SessionId, d.LastAlteredSessionId
        FROM Detail d
        WHERE d.RequisitionId = ?
          AND d.Modified >= '2026-03-03'
          AND d.Modified < '2026-03-07'
        ORDER BY d.Modified
        """, (REQ_ID,))

    # =========================================================================
    # 17. RequisitionNotes - check column names first
    # =========================================================================
    cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'RequisitionNotes' ORDER BY ORDINAL_POSITION")
    rn_cols = [r[0] for r in cursor.fetchall()]
    print(f"\n  RequisitionNotes columns: {rn_cols}")

    run_query(cursor, "17. Requisition Notes for this req",
        f"SELECT * FROM RequisitionNotes WHERE RequisitionId = ?", (REQ_ID,))

    # =========================================================================
    # 18. Check sessions that directly reference this RequisitionId
    # =========================================================================
    run_query(cursor, "18. Sessions that directly reference RequisitionId 60159579",
        """
        SELECT s.SessionId, s.UserId, s.DistrictId, s.SchoolId,
               s.RequisitionId, s.SessionStart, s.SessionEnd, s.SessionLast,
               s.CSRepId, s.RepUserId,
               u.UserName, u.FirstName, u.LastName, u.Email
        FROM SessionTable s
        LEFT JOIN Users u ON s.UserId = u.UserId
        WHERE s.RequisitionId = ?
        ORDER BY s.SessionStart
        """, (REQ_ID,))

    # =========================================================================
    # 19. Deep dive: session 1786625388 (attached to the sky blue item)
    # =========================================================================
    run_query(cursor, "19. Session 1786625388 (sky blue item session)",
        """
        SELECT s.*, u.UserName, u.FirstName, u.LastName, u.Email
        FROM SessionTable s
        LEFT JOIN Users u ON s.UserId = u.UserId
        WHERE s.SessionId = 1786625388
        """)

    run_query(cursor, "19b. Session 1786620958 (DBC21315-2003 item session)",
        """
        SELECT s.*, u.UserName, u.FirstName, u.LastName, u.Email
        FROM SessionTable s
        LEFT JOIN Users u ON s.UserId = u.UserId
        WHERE s.SessionId = 1786620958
        """)

    # =========================================================================
    # 20. Timeline: all changes to items on this req, sorted by date
    # =========================================================================
    run_query(cursor, "20. COMPLETE TIMELINE of changes (DetailChangeLog + DetailChanges)",
        """
        SELECT 'DetailChangeLog' AS Source, dcl.ChangeDate,
               i.ItemCode, dcl.OrigQty, dcl.NewQty,
               dcl.OrigBidPrice, dcl.NewBidPrice,
               dcl.UserId, dcl.SessionId,
               u.UserName, u.FirstName, u.LastName
        FROM DetailChangeLog dcl
        LEFT JOIN Items i ON dcl.ItemId = i.ItemId
        LEFT JOIN Users u ON dcl.UserId = u.UserId
        WHERE dcl.RequisitionId = ?

        UNION ALL

        SELECT 'DetailChanges' AS Source, dc.ChangeDate,
               i.ItemCode, dc.OrigQty, dc.NewQty,
               dc.BidPrice, NULL,
               NULL, NULL,
               NULL, NULL, NULL
        FROM DetailChanges dc
        LEFT JOIN Items i ON dc.ItemId = i.ItemId
        WHERE dc.RequisitionId = ?

        ORDER BY ChangeDate
        """, (REQ_ID, REQ_ID))

    print("\n" + "="*120)
    print("  INVESTIGATION v3 COMPLETE")
    print("="*120)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
