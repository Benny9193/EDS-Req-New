"""Get status, category, school, user mappings for the export."""
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
)
conn.autocommit = True
cursor = conn.cursor()

DISTRICT_ID = 11478849
BUDGET_ID = 1685383  # 2025-2026

# 1. StatusTable
print("=== StatusTable ===")
cursor.execute("SELECT TOP 0 * FROM StatusTable")
cols = [c[0] for c in cursor.description]
print("  Cols:", cols)
cursor.execute("SELECT * FROM StatusTable ORDER BY StatusId")
for r in cursor.fetchall():
    print(f"  {list(r)}")

# 2. vw_RequisitionStatus - maybe simpler
print("\n=== vw_RequisitionStatus (TOP 0) ===")
try:
    cursor.execute("SELECT TOP 0 * FROM vw_RequisitionStatus")
    cols = [c[0] for c in cursor.description]
    print("  Cols:", cols)
except Exception as e:
    print(f"  ERROR: {e}")

# 3. Requisition table (not view) for OrderType
print("\n=== Requisition table columns ===")
cursor.execute("""
    SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Requisition' AND TABLE_TYPE IS NULL
    ORDER BY ORDINAL_POSITION
""")
# it might be in sys.columns
cursor.execute("""
    SELECT c.name, t.name as type
    FROM sys.columns c
    JOIN sys.types t ON t.user_type_id = c.user_type_id
    JOIN sys.objects o ON o.object_id = c.object_id
    WHERE o.name = 'Requisition' AND o.type = 'U'
    ORDER BY c.column_id
""")
for r in cursor.fetchall():
    print(f"  {r[0]:40s} {r[1]}")

# 4. Check for OrderType column in all tables
print("\n=== Tables with OrderType column ===")
cursor.execute("""
    SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE COLUMN_NAME LIKE '%OrderType%' OR COLUMN_NAME LIKE '%Order_Type%'
    ORDER BY TABLE_NAME
""")
for r in cursor.fetchall():
    print(f"  {r[0]:30s}  {r[1]:20s}  {r[2]}")

# 5. Category table
print("\n=== Category table ===")
cursor.execute("""
    SELECT CategoryId, Name FROM Category WHERE Active=1 ORDER BY Name
""")
for r in cursor.fetchall():
    print(f"  {r[0]:10d}  {r[1]}")

# 6. Schools for Scarsdale
print("\n=== Schools for Scarsdale ===")
cursor.execute("""
    SELECT SchoolId, Name FROM School WHERE DistrictId=? AND Active=1 ORDER BY Name
""", DISTRICT_ID)
for r in cursor.fetchall():
    print(f"  {r[0]:10d}  {r[1]}")

# 7. Users table - UserNumber column?
print("\n=== Users table columns ===")
cursor.execute("""
    SELECT c.name, t.name as type
    FROM sys.columns c
    JOIN sys.types t ON t.user_type_id = c.user_type_id
    JOIN sys.objects o ON o.object_id = c.object_id
    WHERE o.name = 'Users' AND o.type = 'U'
    ORDER BY c.column_id
""")
for r in cursor.fetchall():
    print(f"  {r[0]:40s} {r[1]}")

# 8. Sample user from Scarsdale
print("\n=== Sample Scarsdale Users ===")
cursor.execute("""
    SELECT TOP 5 u.UserId, u.UserNumber, u.FirstName, u.LastName
    FROM Users u
    WHERE u.DistrictId = ?
    ORDER BY u.UserId
""", DISTRICT_ID)
for r in cursor.fetchall():
    print(f"  {list(r)}")

# 9. NotesCount - look at Comments field in RequisitionsView
print("\n=== Sample RequisitionsView for 2025-2026 Scarsdale ===")
cursor.execute("""
    SELECT TOP 5 rv.RequisitionNumber, rv.StatusId, rv.Comments,
           rv.TotalRequisitionCost
    FROM RequisitionsView rv
    WHERE rv.BudgetId = ?
    ORDER BY rv.RequisitionNumber DESC
""", BUDGET_ID)
cols = [c[0] for c in cursor.description]
print("  " + " | ".join(cols))
for r in cursor.fetchall():
    print("  " + " | ".join(str(x) if x is not None else "NULL" for x in r))

conn.close()
print("\nDone.")
