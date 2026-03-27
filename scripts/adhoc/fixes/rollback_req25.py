import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;'
    'UID=EDSAdmin;'
    'PWD=Consultant~!'
)
cursor = conn.cursor()

print("=== Rolling back DetailId=1534395373 to original state ===")
print("Original: BidHeaderId=NULL, BidPrice=2.72, VendorId=3842")
print()

# Disable the trigger so it doesn't fire and recalculate again
cursor.execute("ALTER TABLE Detail DISABLE TRIGGER trig_DetailUpdate")
print("Trigger trig_DetailUpdate DISABLED")

# Restore to original state
cursor.execute("""
UPDATE Detail
SET BidHeaderId = NULL,
    BidPrice    = 2.72,
    VendorId    = 3842
WHERE DetailId = 1534395373
  AND RequisitionId = 60076856
""")
print(f"UPDATE applied: {cursor.rowcount} row(s)")

# Re-enable the trigger
cursor.execute("ALTER TABLE Detail ENABLE TRIGGER trig_DetailUpdate")
print("Trigger trig_DetailUpdate ENABLED")

conn.commit()

# Verify the rollback
cursor.execute("""
SELECT DetailId, BidHeaderId, BidPrice, Quantity,
       CAST(ISNULL(BidPrice,0)*ISNULL(Quantity,0) AS DECIMAL(10,2)) AS ExtendedPrice,
       VendorId
FROM Detail
WHERE DetailId = 1534395373
""")
row = cursor.fetchone()
cols = [c[0] for c in cursor.description]
print()
print("=== Restored state ===")
for col, val in zip(cols, row):
    print(f"  {col}: {val}")

# Show grouping again
print()
print("=== Current vendor grouping for req 60076856 ===")
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
print("\nRollback complete.")
