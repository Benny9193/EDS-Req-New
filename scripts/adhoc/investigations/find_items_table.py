import pyodbc
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
)
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("""
    SELECT TABLE_NAME, TABLE_TYPE FROM INFORMATION_SCHEMA.TABLES
    WHERE TABLE_NAME LIKE 'Item%' AND TABLE_TYPE = 'BASE TABLE'
    ORDER BY TABLE_NAME
""")
for r in cursor.fetchall():
    print(f"  {r[0]:30s} {r[1]}")

print()
# Also check what view the trigger uses for item lookup
cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('trig_DetailUpdate'))")
trig = cursor.fetchone()[0]
# Find lines referencing items
for i, line in enumerate(trig.split('\n')):
    ll = line.lower()
    if 'item' in ll and ('from' in ll or 'join' in ll):
        print(f"  L{i}: {line.rstrip()}")
conn.close()
