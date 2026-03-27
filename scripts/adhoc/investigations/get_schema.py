import pyodbc

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

for tbl in ['BidHeaders', 'BidHeaderDetail', 'Awards', 'Detail']:
    print(f"\n=== {tbl} COLUMNS ===")
    cursor.execute("""
        SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = ?
        ORDER BY ORDINAL_POSITION
    """, tbl)
    for r in cursor.fetchall():
        print(f"  {r[0]:40s} {r[1]:15s} {r[2]}")

# Quick peek at BidHeaders for 13575-13577
print("\n=== BidHeaders rows 13575-13577 (SELECT *) ===")
cursor.execute("SELECT TOP 3 * FROM BidHeaders WHERE BidHeaderId IN (13575,13576,13577) ORDER BY BidHeaderId")
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in cursor.fetchall():
    print('\t'.join(str(x) for x in r))

conn.close()
