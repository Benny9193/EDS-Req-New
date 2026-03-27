"""Explore requisition-related views to find the right one for the report."""
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
)
conn.autocommit = True
cursor = conn.cursor()

def show_view_cols(view_name):
    cursor.execute("SELECT TOP 0 * FROM [" + view_name + "]")
    if cursor.description:
        cols = [c[0] for c in cursor.description]
        print("  " + ", ".join(cols))
    else:
        print("  (no columns)")

# Check key views
for v in ['RequisitionsView', 'pa_ReqList', 'vw_ApproveRequisitions',
          'vw_ARStatuses', 'ReqDetail']:
    print(f"\n=== {v} ===")
    try:
        show_view_cols(v)
    except Exception as e:
        print(f"  ERROR: {e}")

# Sample from RequisitionsView
print("\n=== RequisitionsView - TOP 3 ===")
try:
    cursor.execute("SELECT TOP 3 * FROM RequisitionsView")
    cols = [c[0] for c in cursor.description]
    print("  " + " | ".join(cols[:15]))  # first 15 cols
    for r in cursor.fetchall():
        print("  " + " | ".join(str(x) if x is not None else "NULL" for x in list(r)[:15]))
except Exception as e:
    print(f"  ERROR: {e}")

# Find Scarsdale district
print("\n=== Scarsdale District ===")
cursor.execute("SELECT DistrictId, Name, DistrictCode FROM District WHERE Name LIKE '%Scarsdale%'")
for r in cursor.fetchall():
    print(f"  DistrictId={r[0]}, Name={r[1]}, Code={r[2]}")

# Check Budget/Budgets table
print("\n=== Budget columns ===")
cursor.execute("""
    SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME IN ('Budget','Budgets') ORDER BY TABLE_NAME, ORDINAL_POSITION
""")
for r in cursor.fetchall():
    print(f"  {r[0]:40s} {r[1]}")

# What budget years exist?
print("\n=== Budget years (recent) ===")
try:
    cursor.execute("""
        SELECT TOP 10 BudgetId, Name, BudgetYear, Active
        FROM Budget
        ORDER BY BudgetYear DESC
    """)
    for r in cursor.fetchall():
        print(f"  {r}")
except:
    try:
        cursor.execute("""
            SELECT TOP 10 BudgetId, Name, BudgetYear, Active
            FROM Budgets
            ORDER BY BudgetYear DESC
        """)
        for r in cursor.fetchall():
            print(f"  {r}")
    except Exception as e:
        print(f"  ERROR: {e}")

conn.close()
print("\nDone.")
