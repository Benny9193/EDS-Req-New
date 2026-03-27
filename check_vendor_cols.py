import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!'
)
cursor = conn.cursor()

# Check Awards columns (vendor info may be here)
print("=== Awards columns ===")
cursor.execute("SELECT TOP 0 * FROM Awards")
for col in cursor.description:
    print(col[0])

print("\n=== Detail columns ===")
cursor.execute("SELECT TOP 0 * FROM Detail")
for col in cursor.description:
    print(col[0])

print("\n=== Vendors columns ===")
cursor.execute("SELECT TOP 0 * FROM Vendors")
for col in cursor.description:
    print(col[0])

# Check District table for name field
print("\n=== District columns ===")
cursor.execute("SELECT TOP 0 * FROM District")
for col in cursor.description:
    print(col[0])

# Look for Berkeley Heights district
print("\n=== Berkeley Heights district ===")
cursor.execute("SELECT DistrictId, Name, City, State FROM District WHERE Name LIKE '%Berkeley%'")
for row in cursor.fetchall():
    print(row)

conn.close()
