"""Check what happened to Req#36 and Req#45 in the current Niskayuna budget."""
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

for req_num in [36, 45]:
    print(f"=== Req#{req_num} in current budget (1685509) ===")
    cursor.execute("""
        SELECT
            R.RequisitionId,
            R.RequisitionNumber,
            ST.StatusCode,
            ST.Name AS CurrentStatus,
            vwRS.StatusDesc,
            A.ApprovalDate
        FROM Requisitions R
        JOIN Approvals A ON A.RequisitionId = R.RequisitionId
            AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
        WHERE R.BudgetId = 1685509
          AND R.RequisitionNumber = ?
    """, req_num)
    rows = cursor.fetchall()
    if rows:
        for r in rows:
            print(f"  ID={r.RequisitionId}, Status={r.CurrentStatus} ({r.StatusCode})")
            print(f"  Display: {r.StatusDesc}")
            print(f"  Date: {r.ApprovalDate}")
    else:
        print(f"  NOT FOUND in budget 1685509")
    print()

# Also check ALL downloaded reqs remaining in the current budget
print("=== ALL remaining downloaded reqs in budget 1685509 ===")
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
print(f"  Total: {len(rows)} downloaded reqs remaining")
for r in rows:
    print(f"  Req#{r.RequisitionNumber} (ID={r.RequisitionId}): {r.StatusDesc} | {r.ApprovalDate}")

cursor.close()
conn.close()
