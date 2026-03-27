import pyodbc

out = open(r'C:\EDS\bid_tables.txt', 'w')

def p(s=''):
    print(s)
    out.write(s + '\n')
    out.flush()

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
        'DATABASE=EDS;'
        'UID=EDSAdmin;'
        'PWD=Consultant~!;'
        'timeout=30'
    )
    conn.autocommit = True
    cursor = conn.cursor()

    p("=== TABLES/VIEWS with 'Bid' in name ===")
    cursor.execute("""
        SELECT TABLE_NAME, TABLE_TYPE
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_NAME LIKE '%Bid%'
        ORDER BY TABLE_TYPE, TABLE_NAME
    """)
    for r in cursor.fetchall():
        p(f"  {r[1]:12s}  {r[0]}")

    p("\n=== TABLES/VIEWS with 'bid' in name (sys.objects) ===")
    cursor.execute("""
        SELECT name, type_desc
        FROM sys.objects
        WHERE name LIKE '%bid%' OR name LIKE '%Bid%'
        ORDER BY type_desc, name
    """)
    for r in cursor.fetchall():
        p(f"  {r[1]:30s}  {r[0]}")

    p("\n=== Columns containing 'BidHeader' ===")
    cursor.execute("""
        SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE COLUMN_NAME LIKE '%BidHeader%'
        ORDER BY TABLE_NAME
    """)
    for r in cursor.fetchall():
        p(f"  {r[0]:30s}  {r[1]:30s}  {r[2]}")

    conn.close()
    p("\nDone.")
except Exception as e:
    p(f"ERROR: {e}")
finally:
    out.close()
