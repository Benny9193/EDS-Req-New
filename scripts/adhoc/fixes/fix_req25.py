import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;'
    'UID=EDSAdmin;'
    'PWD=Consultant~!'
)
cursor = conn.cursor()

# Confirm the row before updating
cursor.execute("""
SELECT DetailId, BidHeaderId, BidPrice, Quantity,
       CAST(ISNULL(BidPrice,0)*ISNULL(Quantity,0) AS DECIMAL(10,2)) AS ExtendedPrice
FROM Detail
WHERE DetailId = 1534395373
""")
row = cursor.fetchone()
print(f"BEFORE: DetailId={row[0]}, BidHeaderId={row[1]}, BidPrice={row[2]}, Qty={row[3]}, Extended={row[4]}")

# Apply the fix
cursor.execute("""
UPDATE Detail
SET BidHeaderId = 13576
WHERE DetailId = 1534395373
  AND RequisitionId = 60076856
""")
affected = cursor.rowcount
conn.commit()
print(f"UPDATE applied: {affected} row(s) affected")

# Verify after
cursor.execute("""
SELECT DetailId, BidHeaderId, BidPrice, Quantity,
       CAST(ISNULL(BidPrice,0)*ISNULL(Quantity,0) AS DECIMAL(10,2)) AS ExtendedPrice
FROM Detail
WHERE DetailId = 1534395373
""")
row = cursor.fetchone()
print(f"AFTER:  DetailId={row[0]}, BidHeaderId={row[1]}, BidPrice={row[2]}, Qty={row[3]}, Extended={row[4]}")

# Show the new grouping (what the modal will now show)
print("\n=== New vendor grouping for req 60076856 ===")
cursor.execute("""
SELECT
    ISNULL(v.DisplayAs, v.Name) AS VendorName,
    d.BidHeaderId,
    COUNT(*) AS ItemCount,
    CAST(SUM(ISNULL(d.BidPrice,0) * ISNULL(d.Quantity,0)) AS DECIMAL(10,2)) AS SubTotal
FROM Detail d
LEFT JOIN Vendors v ON v.VendorId = d.VendorId
WHERE d.RequisitionId = 60076856
GROUP BY ISNULL(v.DisplayAs, v.Name), d.BidHeaderId
ORDER BY ISNULL(v.DisplayAs, v.Name), d.BidHeaderId
""")
rows = cursor.fetchall()
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in rows:
    print('\t'.join(str(x) for x in r))

conn.close()
print("\nDone.")
