"""
Apply the fix: Revert Niskayuna downloaded requisitions back to On Hold.

Target: Current budget (2025-2026, BudgetId=1685509)
Requisitions from screenshot: Req#5, #26, #41, #42

Found RequisitionIds:
  Req#5  -> ID=59928605
  Req#26 -> ID=59944425
  Req#41 -> ID=59966095
  Req#42 -> ID=59966297
"""
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_DATABASE_CATALOG')};"
    f"UID={os.getenv('DB_USERNAME')};"
    f"PWD={os.getenv('DB_PASSWORD')}"
)

conn = pyodbc.connect(conn_str, timeout=15)
cursor = conn.cursor()

# The 4 RequisitionIds we found in the current Niskayuna budget (2025-2026)
req_ids = [59928605, 59944425, 59966095, 59966297]

# ============================================
# STEP 1: PREVIEW - Confirm all are currently Downloaded
# ============================================
print("=" * 70)
print("STEP 1: PREVIEW - Confirming all reqs are currently Downloaded")
print("=" * 70)

cursor.execute("""
    SELECT
        R.RequisitionId,
        R.RequisitionNumber,
        R.BudgetId,
        ST.StatusId,
        ST.StatusCode,
        ST.Name AS CurrentStatus,
        vwRS.StatusDesc AS DisplayStatus,
        A.ApprovalById,
        A.ApproverId,
        A.Level,
        A.ApprovalDate
    FROM Requisitions R
    JOIN Approvals A ON A.RequisitionId = R.RequisitionId
        AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
    JOIN StatusTable ST ON ST.StatusId = A.StatusId
    LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
    WHERE R.RequisitionId IN (59928605, 59944425, 59966095, 59966297)
    ORDER BY R.RequisitionNumber
""")

rows = cursor.fetchall()
all_downloaded = True
for r in rows:
    status_ok = "OK" if r.StatusCode == 'D' else "*** NOT DOWNLOADED ***"
    if r.StatusCode != 'D':
        all_downloaded = False
    print(f"  Req#{r.RequisitionNumber} (ID={r.RequisitionId})")
    print(f"    Budget={r.BudgetId}, Status={r.CurrentStatus} ({r.StatusCode}) [{status_ok}]")
    print(f"    Display: {r.DisplayStatus}")
    print(f"    ApprovalById={r.ApprovalById}, ApproverId={r.ApproverId}, Level={r.Level}")
    print(f"    Date: {r.ApprovalDate}")
    print()

if not all_downloaded:
    print("*** ERROR: Not all requisitions are in Downloaded status! Aborting. ***")
    cursor.close()
    conn.close()
    exit(1)

if len(rows) != 4:
    print(f"*** ERROR: Expected 4 rows, got {len(rows)}! Aborting. ***")
    cursor.close()
    conn.close()
    exit(1)

print(f"All {len(rows)} requisitions confirmed as Downloaded. Proceeding with fix...\n")

# ============================================
# STEP 2: EXECUTE - Insert new "On Hold" approval rows
# ============================================
print("=" * 70)
print("STEP 2: EXECUTE - Inserting On Hold approval rows")
print("=" * 70)

cursor.execute("""
    INSERT INTO Approvals (RequisitionId, StatusId, ApprovalById, ApproverId, Level, ApprovalDate)
    SELECT
        A.RequisitionId,
        1,              -- StatusId=1 = "On Hold" (Code='H')
        A.ApprovalById, -- Keep same user
        A.ApproverId,   -- Keep same approver (usually NULL)
        A.Level,        -- Keep same level
        GETDATE()       -- New timestamp
    FROM Approvals A
    JOIN StatusTable ST ON ST.StatusId = A.StatusId
    WHERE A.RequisitionId IN (59928605, 59944425, 59966095, 59966297)
      AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = A.RequisitionId)
      AND ST.StatusCode = 'D'
""")

rows_affected = cursor.rowcount
print(f"  Rows inserted: {rows_affected}")

if rows_affected != 4:
    print(f"  *** WARNING: Expected 4 inserts, got {rows_affected}! Rolling back. ***")
    conn.rollback()
    cursor.close()
    conn.close()
    exit(1)

# Commit the transaction
conn.commit()
print(f"  Transaction committed successfully!\n")

# ============================================
# STEP 3: VERIFY - Confirm status changed to On Hold
# ============================================
print("=" * 70)
print("STEP 3: VERIFY - Confirming status changed to On Hold")
print("=" * 70)

# Check Approvals table
cursor.execute("""
    SELECT
        R.RequisitionId,
        R.RequisitionNumber,
        ST.StatusId,
        ST.StatusCode,
        ST.Name AS NewStatus,
        A.ApprovalDate
    FROM Requisitions R
    JOIN Approvals A ON A.RequisitionId = R.RequisitionId
        AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
    JOIN StatusTable ST ON ST.StatusId = A.StatusId
    WHERE R.RequisitionId IN (59928605, 59944425, 59966095, 59966297)
    ORDER BY R.RequisitionNumber
""")

all_on_hold = True
for r in cursor.fetchall():
    status_ok = "OK" if r.StatusCode == 'H' else "*** STILL NOT ON HOLD ***"
    if r.StatusCode != 'H':
        all_on_hold = False
    print(f"  Req#{r.RequisitionNumber} (ID={r.RequisitionId})")
    print(f"    New Status: {r.NewStatus} (Code={r.StatusCode}, Id={r.StatusId}) [{status_ok}]")
    print(f"    Date: {r.ApprovalDate}")
    print()

# Check vw_RequisitionStatus
print("  --- vw_RequisitionStatus view ---")
cursor.execute("""
    SELECT RequisitionId, StatusDesc, BaseStatus
    FROM vw_RequisitionStatus
    WHERE RequisitionId IN (59928605, 59944425, 59966095, 59966297)
    ORDER BY RequisitionId
""")
for r in cursor.fetchall():
    print(f"  ID={r.RequisitionId}: {r.StatusDesc} (Base: {r.BaseStatus})")

print()
if all_on_hold:
    print("=" * 70)
    print("SUCCESS: All 4 requisitions changed from Downloaded to On Hold!")
    print("=" * 70)
else:
    print("=" * 70)
    print("*** ISSUE: Not all requisitions are On Hold. Check results above. ***")
    print("=" * 70)

cursor.close()
conn.close()
