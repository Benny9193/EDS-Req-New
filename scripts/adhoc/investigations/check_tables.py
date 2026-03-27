import pyodbc
conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
)
cursor = conn.cursor()
for tbl in ['Prices', 'BidItems', 'Bids']:
    print(f"\n=== {tbl} ===")
    cursor.execute("""
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = ? ORDER BY ORDINAL_POSITION
    """, tbl)
    rows = cursor.fetchall()
    if rows:
        for r in rows:
            print(f"  {r[0]}")
    else:
        print("  TABLE NOT FOUND")
conn.close()
