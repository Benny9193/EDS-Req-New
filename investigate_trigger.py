import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;'
    'UID=EDSAdmin;'
    'PWD=Consultant~!'
)
cursor = conn.cursor()

# Check current full state of the affected row
print("=== Current state of DetailId=1534395373 ===")
cursor.execute("""
SELECT * FROM Detail WHERE DetailId = 1534395373
""")
row = cursor.fetchone()
cols = [c[0] for c in cursor.description]
for col, val in zip(cols, row):
    print(f"  {col}: {val}")

print()

# Check triggers on Detail table
print("=== Triggers on Detail table ===")
cursor.execute("""
SELECT t.name AS TriggerName, t.type_desc, t.is_disabled,
       te.type_desc AS EventType
FROM sys.triggers t
JOIN sys.trigger_events te ON te.object_id = t.object_id
WHERE t.parent_id = OBJECT_ID('Detail')
ORDER BY t.name
""")
rows = cursor.fetchall()
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in rows:
    print('\t'.join(str(x) for x in r))

print()

# Get trigger definitions
print("=== Trigger definitions ===")
cursor.execute("""
SELECT t.name, m.definition
FROM sys.triggers t
JOIN sys.sql_modules m ON m.object_id = t.object_id
WHERE t.parent_id = OBJECT_ID('Detail')
""")
for row in cursor.fetchall():
    print(f"\n--- Trigger: {row[0]} ---")
    print(row[1][:2000] if row[1] else '(no definition)')

conn.close()
