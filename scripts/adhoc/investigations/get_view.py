import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!'
)
cursor = conn.cursor()

# Get view definition
cursor.execute("""
SELECT definition 
FROM sys.sql_modules m 
JOIN sys.objects o ON m.object_id = o.object_id 
WHERE o.name = 'vw_savingsdetail1'
""")
row = cursor.fetchone()
if row:
    print("=== VIEW DEFINITION ===")
    print(row[0])
else:
    print('View not found')

# Also get column names
print("\n=== COLUMNS ===")
cursor.execute("""
SELECT TOP 0 * FROM vw_savingsdetail1
""")
for col in cursor.description:
    print(col[0])

conn.close()
