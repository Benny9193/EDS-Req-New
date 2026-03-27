"""Quick script to explore database schema"""
import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;'
    'UID=EDSAdmin;'
    'PWD=Consultant~!;'
    'TrustServerCertificate=yes'
)
cursor = conn.cursor()

print("=== Category table columns ===")
cursor.execute("""
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'Category'
""")
for row in cursor.fetchall():
    print(f"  {row[0]}: {row[1]}")

print("\n=== Category sample ===")
cursor.execute("SELECT TOP 10 * FROM Category")
cols = [col[0] for col in cursor.description]
print(f"  Columns: {cols}")
for row in cursor.fetchall():
    print(f"  {row}")

conn.close()
