"""Find OrderType and UserNumber columns."""
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

# 1. Look for OrderType column in all tables/views
print("=== Tables/Views with OrderType column ===")
cursor.execute("""
    SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE COLUMN_NAME IN ('OrderType', 'OrderTypeId', 'IncidentalOrder', 'OrderTypeDisplay')
    ORDER BY TABLE_NAME, COLUMN_NAME
""")
for r in cursor.fetchall():
    print(f"  {r[0]:40s}  {r[1]:25s}  {r[2]}")

# 2. Look for UserNumber in Users table
print("\n=== Users table - all columns ===")
cursor.execute("""
    SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Users' ORDER BY ORDINAL_POSITION
""")
for r in cursor.fetchall():
    print(f"  {r[0]:40s} {r[1]}")

# 3. Sample Users for Scarsdale
print("\n=== Sample Scarsdale Users ===")
cursor.execute("""
    SELECT TOP 5 UserId, UserNumber, FirstName, LastName, Email
    FROM Users WHERE DistrictId=? ORDER BY UserNumber
""", DISTRICT_ID)
cols = [c[0] for c in cursor.description]
for r in cursor.fetchall():
    print(f"  {dict(zip(cols, r))}")

# 4. Check vw_ApproveRequisitions definition for OrderType source
print("\n=== vw_ApproveRequisitions definition ===")
cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('vw_ApproveRequisitions'))")
defn = cursor.fetchone()
if defn and defn[0]:
    # Find OrderType relevant section
    lines = defn[0].split('\n')
    for i, line in enumerate(lines):
        if 'ordertype' in line.lower() or 'incidental' in line.lower() or 'annual' in line.lower():
            print(f"  L{i}: {line.rstrip()}")

# 5. Check RequisitionsView definition for any OrderType
print("\n=== RequisitionsView definition ===")
cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('RequisitionsView'))")
defn = cursor.fetchone()
if defn and defn[0]:
    print(defn[0][:3000])

# 6. Check Notes count view definition
print("\n=== vw_ApproveRequisitions NotesCount ===")
cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('vw_ApproveRequisitions'))")
defn = cursor.fetchone()
if defn and defn[0]:
    lines = defn[0].split('\n')
    for i, line in enumerate(lines):
        if 'note' in line.lower() or 'comment' in line.lower():
            print(f"  L{i}: {line.rstrip()}")

conn.close()
print("\nDone.")
