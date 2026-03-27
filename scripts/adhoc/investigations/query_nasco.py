import pyodbc, pickle

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;"
    "DATABASE=EDS;"
    "UID=EDSAdmin;PWD=Consultant~!"
)
cursor = conn.cursor()

cursor.execute("""
SELECT
    c.Name AS CategoryName,
    c.Code AS CategoryCode,
    b.BidId,
    b.Name AS BidName,
    b.VendorBidNumber AS BidVendorNumber,
    b.EffectiveFrom,
    b.EffectiveUntil,
    bh.BidHeaderKey,
    bh.Description AS BidHeaderDescription,
    COUNT(DISTINCT p.POId) AS POCount,
    SUM(p.Amount) AS TotalAmount,
    MIN(p.PODate) AS FirstPODate,
    MAX(p.PODate) AS LastPODate
FROM PO p
JOIN Awards a ON p.AwardId = a.AwardId
JOIN Bids b ON a.BidId = b.BidId
JOIN Category c ON a.CategoryId = c.CategoryId
LEFT JOIN BidHeaders bh ON b.BidHeaderId = bh.BidHeaderId
WHERE p.VendorId = 541
  AND p.PODate >= '2024-12-01'
  AND p.PODate <  '2025-12-01'
GROUP BY
    c.Name, c.Code, b.BidId, b.Name, b.VendorBidNumber,
    b.EffectiveFrom, b.EffectiveUntil, bh.BidHeaderKey, bh.Description
ORDER BY c.Name, b.EffectiveFrom
""")
detail_rows = cursor.fetchall()
detail_cols = [c[0] for c in cursor.description]

cursor.execute("""
SELECT
    c.Name AS CategoryName,
    c.Code AS CategoryCode,
    COUNT(DISTINCT b.BidId) AS BidCount,
    COUNT(DISTINCT p.POId) AS POCount,
    SUM(p.Amount) AS TotalAmount,
    MIN(p.PODate) AS FirstPODate,
    MAX(p.PODate) AS LastPODate
FROM PO p
JOIN Awards a ON p.AwardId = a.AwardId
JOIN Bids b ON a.BidId = b.BidId
JOIN Category c ON a.CategoryId = c.CategoryId
WHERE p.VendorId = 541
  AND p.PODate >= '2024-12-01'
  AND p.PODate <  '2025-12-01'
GROUP BY c.Name, c.Code
ORDER BY SUM(p.Amount) DESC
""")
cat_rows = cursor.fetchall()
cat_cols = [c[0] for c in cursor.description]
conn.close()

print(f"Detail rows: {len(detail_rows)}, Category rows: {len(cat_rows)}")
for r in cat_rows:
    d = dict(zip(cat_cols, r))
    print(f"  {d['CategoryName']}: {d['POCount']} POs, ${float(d['TotalAmount']):,.2f}")

with open("nasco_data.pkl", "wb") as f:
    pickle.dump({"detail": (detail_rows, detail_cols), "cats": (cat_rows, cat_cols)}, f)
print("Saved")
