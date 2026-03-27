"""Find the CURRENT YEAR Niskayuna downloaded requisitions to fix."""
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

# Get Niskayuna's current budget (BudgetId=1685509 appears to be the 2025-2026 one)
print("=== Niskayuna current budget info ===")
cursor.execute("""
    SELECT BudgetId, DistrictId, Name, StartDate, EndDate, Active
    FROM Budgets
    WHERE BudgetId = 1685509
""")
r = cursor.fetchone()
if r:
    print(f"  BudgetId={r.BudgetId}, DistrictId={r.DistrictId}, Name={r.Name}")
    print(f"  Start={r.StartDate}, End={r.EndDate}, Active={r.Active}")

# Get ALL budgets for this district that are active
print()
print("=== All active Niskayuna budgets ===")
cursor.execute("""
    SELECT BudgetId, Name, StartDate, EndDate, Active
    FROM Budgets
    WHERE DistrictId = (SELECT DistrictId FROM Budgets WHERE BudgetId = 1685509)
      AND Active = 1
    ORDER BY StartDate DESC
""")
for r in cursor.fetchall():
    print(f"  BudgetId={r.BudgetId}, Name={r.Name}, Start={r.StartDate}, End={r.EndDate}")

# Now find the downloaded reqs from the CURRENT budget (1685509) with req#s from the screenshot
print()
print("=== Downloaded reqs in current Niskayuna budget (1685509) with screenshot req numbers ===")
cursor.execute("""
    SELECT
        R.RequisitionId,
        R.RequisitionNumber,
        vwRS.StatusDesc,
        A.ApprovalDate
    FROM Requisitions R
    JOIN Approvals A ON A.RequisitionId = R.RequisitionId
        AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
    JOIN StatusTable ST ON ST.StatusId = A.StatusId
    LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
    WHERE ST.StatusCode = 'D'
      AND R.BudgetId = 1685509
      AND R.RequisitionNumber IN (5, 26, 36, 41, 42, 45)
    ORDER BY R.RequisitionNumber
""")
rows = cursor.fetchall()
if rows:
    for r in rows:
        print(f"  Req#{r.RequisitionNumber} | ID={r.RequisitionId}")
        print(f"    {r.StatusDesc} | Date: {r.ApprovalDate}")
else:
    print("  None found. Trying broader search on current budget...")
    cursor.execute("""
        SELECT
            R.RequisitionId,
            R.RequisitionNumber,
            vwRS.StatusDesc,
            A.ApprovalDate
        FROM Requisitions R
        JOIN Approvals A ON A.RequisitionId = R.RequisitionId
            AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
        WHERE ST.StatusCode = 'D'
          AND R.BudgetId = 1685509
        ORDER BY R.RequisitionNumber
    """)
    rows = cursor.fetchall()
    print(f"  Found {len(rows)} total downloaded reqs in budget 1685509")
    for r in rows[:20]:
        print(f"  Req#{r.RequisitionNumber} | ID={r.RequisitionId}")
        print(f"    {r.StatusDesc} | Date: {r.ApprovalDate}")
    if len(rows) > 20:
        print(f"  ... and {len(rows)-20} more")

cursor.close()
conn.close()
