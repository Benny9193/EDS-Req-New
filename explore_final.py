"""Final schema exploration before building the export query."""
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

# 1. Sample Scarsdale Users with CometId
print("=== Sample Scarsdale Users (CometId) ===")
cursor.execute("""
    SELECT TOP 5 UserId, CometId, FirstName, LastName
    FROM Users WHERE DistrictId=? ORDER BY CometId
""", DISTRICT_ID)
for r in cursor.fetchall():
    print(f"  UserId={r[0]}, CometId={r[1]}, Name={r[2]} {r[3]}")

# 2. Requisitions table columns (the actual table)
print("\n=== Requisitions table - all columns ===")
cursor.execute("""
    SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Requisitions' ORDER BY ORDINAL_POSITION
""")
for r in cursor.fetchall():
    print(f"  {r[0]:40s} {r[1]}")

# 3. Sample Requisitions for Scarsdale
print("\n=== Sample Scarsdale Requisitions (TOP 5) ===")
cursor.execute("""
    SELECT TOP 5 r.RequisitionId, r.RequisitionNumber, r.OrderType,
           r.StatusId, r.TotalRequisitionCost, r.CategoryId, r.SchoolId, r.UserId
    FROM Requisitions r
    WHERE r.BudgetId = ?
    ORDER BY r.RequisitionNumber DESC
""", BUDGET_ID)
cols = [c[0] for c in cursor.description]
print("  " + " | ".join(cols))
for r in cursor.fetchall():
    print("  " + " | ".join(str(x) if x is not None else "NULL" for x in r))

# 4. vw_ApproveRequisitions OrderTypeDisplay
print("\n=== vw_ApproveRequisitions definition (OrderType section) ===")
cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('vw_ApproveRequisitions'))")
defn = cursor.fetchone()
if defn and defn[0]:
    lines = defn[0].split('\n')
    for i, line in enumerate(lines):
        if any(kw in line.lower() for kw in ['ordertype', 'annual', 'incidental', 'notescount', 'comment']):
            print(f"  L{i}: {line.rstrip()}")

# 5. Accounts / AccountCode - where does it come from?
print("\n=== Accounts table columns ===")
cursor.execute("""
    SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Accounts' ORDER BY ORDINAL_POSITION
""")
for r in cursor.fetchall():
    print(f"  {r[0]:40s} {r[1]}")

# 6. Check if there's a Notes table
print("\n=== Tables with 'Note' in name ===")
cursor.execute("""
    SELECT TABLE_NAME, TABLE_TYPE FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME LIKE '%Note%' ORDER BY TABLE_NAME
""")
for r in cursor.fetchall():
    print(f"  {r[1]:10s}  {r[0]}")

# 7. Count of notes per req for Scarsdale 2025-26
print("\n=== Notes table structure ===")
for t in ['Notes', 'RequisitionNotes', 'ReqNotes']:
    cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?", t)
    if cursor.fetchone()[0] > 0:
        cursor.execute(f"SELECT TOP 0 * FROM [{t}]")
        cols = [c[0] for c in cursor.description]
        print(f"  [{t}]: {cols}")

# 8. Full query test combining Requisitions + joins
print("\n=== Full export query test (TOP 10) ===")
cursor.execute("""
    SELECT TOP 10
        r.RequisitionNumber AS Requisition,
        st.Name AS Status,
        cat.Name AS Category,
        sch.Name AS School,
        r.AccountCode,
        r.Attention AS [Attention To],
        u.CometId AS [User #],
        CASE r.OrderType WHEN 1 THEN 'Incidental' ELSE 'Annual' END AS [Order Type],
        CASE WHEN LEN(ISNULL(r.Comments,'')) > 0 THEN 1 ELSE 0 END AS Notes,
        r.TotalRequisitionCost AS Total
    FROM Requisitions r
    LEFT JOIN StatusTable st ON st.StatusId = r.StatusId
    LEFT JOIN Category cat ON cat.CategoryId = r.CategoryId
    LEFT JOIN School sch ON sch.SchoolId = r.SchoolId
    LEFT JOIN Users u ON u.UserId = r.UserId
    WHERE r.BudgetId = ?
    ORDER BY cat.Name, r.RequisitionNumber
""", BUDGET_ID)
cols = [c[0] for c in cursor.description]
print("  " + " | ".join(cols))
for r in cursor.fetchall():
    print("  " + " | ".join(str(x) if x is not None else "NULL" for x in r))

conn.close()
print("\nDone.")
