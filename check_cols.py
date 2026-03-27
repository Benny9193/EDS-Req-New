import pyodbc
conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;'
    'UID=EDSAdmin;'
    'PWD=Consultant~!;'
    'TrustServerCertificate=yes;'
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

for table in ['POLayouts', 'POLayoutFields', 'StatusTable', 'POStatusTable', 'ChargeTypes', 'InvoiceTypes', 'PaymentTypes']:
    print(f"\n=== {table} ===")
    try:
        cursor.execute(f"""
            SELECT COLUMN_NAME, DATA_TYPE
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '{table}' AND TABLE_SCHEMA = 'dbo'
            ORDER BY ORDINAL_POSITION
        """)
        for row in cursor.fetchall():
            print(f"  {row.COLUMN_NAME}: {row.DATA_TYPE}")
        # Sample data
        cursor.execute(f"SELECT TOP 3 * FROM dbo.[{table}]")
        cols = [d[0] for d in cursor.description]
        for row in cursor.fetchall():
            print(f"  DATA: {dict(zip(cols, row))}")
    except Exception as e:
        print(f"  ERROR: {e}")

conn.close()
