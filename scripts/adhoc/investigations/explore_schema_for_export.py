"""
Schema exploration to map Scarsdale export columns to DB tables.
Columns needed: Requisition, Status, Category, School, Account Code,
                Attention To, User #, Order Type, Notes, Total
"""
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
)
conn.autocommit = True
cursor = conn.cursor()

def show_columns(table):
    cursor.execute("""
        SELECT COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = ?
        ORDER BY ORDINAL_POSITION
    """, table)
    rows = cursor.fetchall()
    if rows:
        for r in rows:
            print(f"    {r[0]:40s} {r[1]}")
    else:
        print("    (TABLE NOT FOUND)")

# 1. Requisition table
print("=== Requisition ===")
show_columns('Requisition')

# 2. District table
print("\n=== District ===")
show_columns('District')

# 3. School/Building table
for t in ['School', 'Building', 'Schools', 'Buildings']:
    cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?", t)
    if cursor.fetchone()[0] > 0:
        print(f"\n=== {t} ===")
        show_columns(t)

# 4. Category table
for t in ['Category', 'Categories']:
    cursor.execute("SELECT COUNT(*) FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_NAME=?", t)
    if cursor.fetchone()[0] > 0:
        print(f"\n=== {t} ===")
        show_columns(t)

# 5. User/Users table
print("\n=== Users ===")
show_columns('Users')

# 6. Budget table
print("\n=== Budget ===")
show_columns('Budget')
print("\n=== Budgets ===")
show_columns('Budgets')

# 7. All tables in EDS db
print("\n=== ALL TABLES ===")
cursor.execute("""
    SELECT TABLE_NAME, TABLE_TYPE
    FROM INFORMATION_SCHEMA.TABLES
    ORDER BY TABLE_TYPE, TABLE_NAME
""")
for r in cursor.fetchall():
    print(f"  {r[1]:12s}  {r[0]}")

# 8. Sample rows from Requisition to see what's there
print("\n=== Sample Requisition rows (TOP 3) ===")
cursor.execute("SELECT TOP 3 * FROM Requisition ORDER BY RequisitionId DESC")
cols = [c[0] for c in cursor.description]
print("  " + " | ".join(cols))
for r in cursor.fetchall():
    print("  " + " | ".join(str(x) if x is not None else "NULL" for x in r))

# 9. Find Scarsdale district
print("\n=== Scarsdale District ===")
cursor.execute("SELECT * FROM District WHERE Name LIKE '%Scarsdale%'")
cols = [c[0] for c in cursor.description] if cursor.description else []
rows = cursor.fetchall()
if cols:
    print("  " + " | ".join(cols))
for r in rows:
    print("  " + " | ".join(str(x) if x is not None else "NULL" for x in r))

conn.close()
print("\nDone.")
