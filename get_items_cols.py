import pyodbc
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
)
cursor = conn.cursor()
cursor.execute("SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME='Items' ORDER BY ORDINAL_POSITION")
for r in cursor.fetchall():
    print(r[0])
conn.close()
