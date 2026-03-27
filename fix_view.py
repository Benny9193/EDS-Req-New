import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;'
    'UID=EDSAdmin;'
    'PWD=Consultant~!'
)
cursor = conn.cursor()

# First verify current behavior for req 60076856
print("=== BEFORE: vw_ReqTotalsByVendor for req 60076856 ===")
cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum, MinimumPOAmount
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60076856
""")
rows = cursor.fetchall()
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in rows:
    print('\t'.join(str(x) for x in r))

print()
print("Applying ALTER VIEW to fix POBelowMinimum at vendor level...")

# ALTER the view to use window function for POBelowMinimum
cursor.execute("""
ALTER VIEW [dbo].[vw_ReqTotalsByVendor] AS
SELECT
    rsc.RequisitionId,
    COALESCE(Vendors.Code, '') VendorCode,
    rsc.VendorName,
    rsc.AdditionalHandlingAmount,
    rsc.FreeHandlingAmount,
    rsc.FreeHandlingStart,
    rsc.FreeHandlingEnd,
    rsc.ShippingCost HandlingAmount,
    rsc.Extended + rsc.ShippingCost + rsc.TotalShippingCost VendorTotal,
    rsc.Extended ItemsTotal,
    CASE
        WHEN SUM(rsc.Extended + rsc.ShippingCost + rsc.TotalShippingCost)
                 OVER (PARTITION BY rsc.RequisitionId, rsc.VendorId) < rsc.MinimumPOAmount
        THEN 1
        ELSE 0
    END POBelowMinimum,
    rsc.MinimumPOAmount,
    rsc.AdditionalShipping,
    rsc.TotalShippingCost,
    rsc.UpdateRequired
FROM vw_RequisitionShippingCosts rsc
JOIN Vendors ON Vendors.VendorId = rsc.VendorId
""")
conn.commit()
print("ALTER VIEW applied successfully.")

print()
print("=== AFTER: vw_ReqTotalsByVendor for req 60076856 ===")
cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum, MinimumPOAmount
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60076856
""")
rows = cursor.fetchall()
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in rows:
    print('\t'.join(str(x) for x in r))

conn.close()
print("\nDone.")
