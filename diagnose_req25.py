import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;'
    'UID=EDSAdmin;'
    'PWD=Consultant~!'
)
cursor = conn.cursor()

print("=== All Detail rows for RequisitionId=60076856 ===")
cursor.execute("""
SELECT
    d.DetailId,
    d.BidHeaderId,
    CAST(d.BidPrice AS DECIMAL(10,4)) AS BidPrice,
    d.Quantity,
    CAST(ISNULL(d.BidPrice,0) * ISNULL(d.Quantity,0) AS DECIMAL(10,2)) AS ExtendedPrice,
    ISNULL(v.DisplayAs, v.Name) AS VendorName,
    d.VendorId,
    bh.Description AS BidDescription
FROM Detail d
LEFT JOIN Vendors v ON v.VendorId = d.VendorId
LEFT JOIN BidHeaders bh ON bh.BidHeaderId = d.BidHeaderId
WHERE d.RequisitionId = 60076856
ORDER BY ISNULL(v.DisplayAs, v.Name), d.BidHeaderId
""")
rows = cursor.fetchall()
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in rows:
    print('\t'.join(str(x) for x in r))

print()
print("=== United Sales rows only ===")
cursor.execute("""
SELECT
    d.DetailId,
    d.BidHeaderId,
    CAST(d.BidPrice AS DECIMAL(10,4)) AS BidPrice,
    d.Quantity,
    CAST(ISNULL(d.BidPrice,0) * ISNULL(d.Quantity,0) AS DECIMAL(10,2)) AS ExtendedPrice,
    ISNULL(v.DisplayAs, v.Name) AS VendorName,
    d.VendorId,
    bh.Description AS BidDescription
FROM Detail d
LEFT JOIN Vendors v ON v.VendorId = d.VendorId
LEFT JOIN BidHeaders bh ON bh.BidHeaderId = d.BidHeaderId
WHERE d.RequisitionId = 60076856
  AND ISNULL(v.DisplayAs, v.Name) LIKE '%United Sales%'
ORDER BY d.BidHeaderId
""")
rows = cursor.fetchall()
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in rows:
    print('\t'.join(str(x) for x in r))

print()
print("=== BidHeaderId totals per vendor (mirrors vw_RequisitionShippingCosts grouping) ===")
cursor.execute("""
SELECT
    ISNULL(v.DisplayAs, v.Name) AS VendorName,
    d.BidHeaderId,
    bh.Description AS BidDescription,
    COUNT(*) AS ItemCount,
    CAST(SUM(ISNULL(d.BidPrice,0) * ISNULL(d.Quantity,0)) AS DECIMAL(10,2)) AS SubTotal
FROM Detail d
LEFT JOIN Vendors v ON v.VendorId = d.VendorId
LEFT JOIN BidHeaders bh ON bh.BidHeaderId = d.BidHeaderId
WHERE d.RequisitionId = 60076856
GROUP BY ISNULL(v.DisplayAs, v.Name), d.BidHeaderId, bh.Description
ORDER BY ISNULL(v.DisplayAs, v.Name), d.BidHeaderId
""")
rows = cursor.fetchall()
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in rows:
    print('\t'.join(str(x) for x in r))

conn.close()
print("\nDone.")
