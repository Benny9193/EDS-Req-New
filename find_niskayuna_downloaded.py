"""Find the Niskayuna downloaded requisitions that need to be reverted to On Hold."""
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

# First find the Budget table columns
print("=== Budget table columns ===")
cursor.execute("""
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Budgets'
    ORDER BY ORDINAL_POSITION
""")
for r in cursor.fetchall():
    print(f"  {r.COLUMN_NAME} ({r.DATA_TYPE})")

# Find Niskayuna via SLYADNEVA (the Niskayuna purchasing person from the screenshot)
print()
print("=== Downloaded reqs by N. SLYADNEVA (Niskayuna Purchasing) ===")
cursor.execute("""
    SELECT
        R.RequisitionId,
        R.RequisitionNumber,
        R.BudgetId,
        ST.StatusCode,
        vwRS.StatusDesc,
        A.ApprovalById,
        A.ApprovalDate
    FROM Requisitions R
    JOIN Approvals A ON A.RequisitionId = R.RequisitionId
        AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
    JOIN StatusTable ST ON ST.StatusId = A.StatusId
    LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
    WHERE ST.StatusCode = 'D'
      AND vwRS.StatusDesc LIKE '%SLYADNEVA%'
    ORDER BY R.RequisitionNumber
""")
rows = cursor.fetchall()
if rows:
    for r in rows:
        print(f"  Req#{r.RequisitionNumber} | ID={r.RequisitionId} | BudgetId={r.BudgetId}")
        print(f"    {r.StatusDesc}")
        print(f"    ApprovalById={r.ApprovalById} | Date: {r.ApprovalDate}")
    print(f"\n  Total: {len(rows)} requisitions")
else:
    print("  No results for SLYADNEVA")

# Also check if there's a district table
print()
print("=== Budget details for one of those req BudgetIds ===")
if rows:
    bid = rows[0].BudgetId
    cursor.execute(f"SELECT TOP 1 * FROM Budgets WHERE BudgetId = {bid}")
    cols = [desc[0] for desc in cursor.description]
    row = cursor.fetchone()
    if row:
        for i, c in enumerate(cols):
            print(f"  {c}: {row[i]}")

cursor.close()
conn.close()
