"""Explore Scarsdale-specific data for the export."""
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
)
conn.autocommit = True
cursor = conn.cursor()

DISTRICT_ID = 11478849  # Scarsdale Public Schools

# Find table name for Budget
print("=== Budget-related tables ===")
cursor.execute("""
    SELECT TABLE_NAME, TABLE_TYPE FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME LIKE '%udget%' ORDER BY TABLE_NAME
""")
for r in cursor.fetchall():
    print(f"  {r[1]:10s}  {r[0]}")

# 1. Find Scarsdale budgets
print("\n=== Scarsdale Budgets ===")
cursor.execute("""
    SELECT BudgetId, Name, Active, StartDate, EndDate
    FROM Budgets
    WHERE DistrictId = ?
    ORDER BY StartDate DESC
""", DISTRICT_ID)
for r in cursor.fetchall():
    print(f"  BudgetId={r[0]}, Name={r[1]!r}, Active={r[2]}, Start={r[3]}, End={r[4]}")

# 2. Status table
print("\n=== Status / Statuses table ===")
for t in ['Status', 'Statuses', 'ReqStatus']:
    try:
        cursor.execute(f"SELECT * FROM [{t}]")
        cols = [c[0] for c in cursor.description]
        print(f"  [{t}] cols: {cols}")
        for r in cursor.fetchall():
            print(f"    {list(r)}")
        break
    except:
        pass

# 3. RequisitionsView for Scarsdale (using Budgets)
print("\n=== RequisitionsView for Scarsdale (TOP 5) ===")
cursor.execute("""
    SELECT TOP 5 rv.RequisitionId, rv.RequisitionNumber, rv.SchoolId,
           rv.BudgetId, rv.StatusId, rv.TotalRequisitionCost, rv.Attention,
           rv.CategoryId, rv.UserAccountId
    FROM RequisitionsView rv
    JOIN Budgets b ON b.BudgetId = rv.BudgetId
    WHERE b.DistrictId = ?
    ORDER BY rv.DateEntered DESC
""", DISTRICT_ID)
cols = [c[0] for c in cursor.description]
print("  " + " | ".join(cols))
for r in cursor.fetchall():
    print("  " + " | ".join(str(x) if x is not None else "NULL" for x in r))

# 4. vw_ApproveRequisitions definition
print("\n=== vw_ApproveRequisitions definition ===")
cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('vw_ApproveRequisitions'))")
defn = cursor.fetchone()
if defn and defn[0]:
    print(defn[0][:5000])

# 5. Try querying vw_ApproveRequisitions for Scarsdale
print("\n=== vw_ApproveRequisitions for Scarsdale (TOP 3) ===")
try:
    cursor.execute("""
        SELECT TOP 3 *
        FROM vw_ApproveRequisitions
        WHERE DistrictID = ?
        ORDER BY RequisitionNumber
    """, DISTRICT_ID)
    cols = [c[0] for c in cursor.description]
    print("  Cols: " + ", ".join(cols))
    for r in cursor.fetchall():
        row_dict = dict(zip(cols, r))
        for k, v in row_dict.items():
            print(f"    {k}: {v}")
        print()
except Exception as e:
    print(f"  ERROR: {e}")

conn.close()
print("\nDone.")
