"""Fast schema exploration - avoid slow session-based views."""
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
)
conn.autocommit = True
cursor = conn.cursor()

DISTRICT_ID = 11478849  # Scarsdale Public Schools

# 1. Scarsdale budgets
print("=== Scarsdale Budgets ===")
cursor.execute("""
    SELECT BudgetId, Name, Active, StartDate, EndDate
    FROM Budgets WHERE DistrictId = ? ORDER BY StartDate DESC
""", DISTRICT_ID)
for r in cursor.fetchall():
    print(f"  {r}")

# 2. Status table structure
print("\n=== ReqStatus / Status tables ===")
cursor.execute("""
    SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME LIKE '%tatus%' ORDER BY TABLE_NAME
""")
for r in cursor.fetchall():
    print(f"  {r[0]}")

# 3. Check RequisitionStatus table
for t in ['ReqStatus', 'RequisitionStatus', 'StatusCodes']:
    cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?", t)
    if cursor.fetchone()[0] > 0:
        cursor.execute(f"SELECT * FROM [{t}]")
        cols = [c[0] for c in cursor.description]
        print(f"\n  [{t}]: {cols}")
        for r in cursor.fetchall():
            print(f"    {list(r)}")

# 4. StatusId mapping from RequisitionsView - what are the distinct values?
print("\n=== Distinct StatusId in RequisitionsView for Scarsdale ===")
cursor.execute("""
    SELECT DISTINCT rv.StatusId, COUNT(*) as cnt
    FROM RequisitionsView rv
    JOIN Budgets b ON b.BudgetId = rv.BudgetId
    WHERE b.DistrictId = ?
    GROUP BY rv.StatusId
    ORDER BY rv.StatusId
""", DISTRICT_ID)
for r in cursor.fetchall():
    print(f"  StatusId={r[0]}, count={r[1]}")

# 5. ReqStatus or similar
print("\n=== UserAccount / BudgetAccount columns ===")
for t in ['UserAccount', 'BudgetAccount', 'UserAccounts', 'BudgetAccounts']:
    cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?", t)
    if cursor.fetchone()[0] > 0:
        cursor.execute(f"SELECT TOP 0 * FROM [{t}]")
        cols = [c[0] for c in cursor.description]
        print(f"  [{t}]: {cols}")

# 6. OrderType - is it in RequisitionsView?
print("\n=== RequisitionsView full column list ===")
cursor.execute("SELECT TOP 0 * FROM RequisitionsView")
cols = [c[0] for c in cursor.description]
print("  " + ", ".join(cols))

# 7. ReqDetail full column list
print("\n=== ReqDetail full column list ===")
cursor.execute("SELECT TOP 0 * FROM ReqDetail")
cols = [c[0] for c in cursor.description]
print("  " + ", ".join(cols))

# 8. Sample data from ReqDetail for Scarsdale
print("\n=== ReqDetail for Scarsdale - TOP 5 ===")
cursor.execute("""
    SELECT TOP 5 rd.RequisitionId, rd.RequisitionNumber, rd.StatusId,
           rd.TotalRequisitionCost, rd.Attention, rd.AccountCode
    FROM ReqDetail rd
    JOIN Budgets b ON b.BudgetId = rd.BudgetId
    WHERE b.DistrictId = ?
    ORDER BY rd.DateEntered DESC
""", DISTRICT_ID)
cols = [c[0] for c in cursor.description]
print("  " + " | ".join(cols))
for r in cursor.fetchall():
    print("  " + " | ".join(str(x) if x is not None else "NULL" for x in r))

conn.close()
print("\nDone.")
