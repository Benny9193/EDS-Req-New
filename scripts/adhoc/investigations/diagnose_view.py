import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={os.getenv("DB_SERVER")};'
    f'DATABASE={os.getenv("DB_DATABASE_CATALOG", "EDS")};'
    f'UID={os.getenv("DB_USERNAME")};'
    f'PWD={os.getenv("DB_PASSWORD")};'
    f'timeout=30'
)
cursor = conn.cursor()

# 1. Get current view definition
print("=== CURRENT VIEW DEFINITION ===")
cursor.execute("""
SELECT definition
FROM sys.sql_modules
WHERE object_id = OBJECT_ID('vw_ReqTotalsByVendor')
""")
row = cursor.fetchone()
if row:
    print(row[0][:3000])
else:
    print("VIEW NOT FOUND")

# 2. Sample data - find a recent requisition with multiple vendors
print("\n=== SAMPLE: Recent req with multiple vendor rows ===")
cursor.execute("""
SELECT TOP 5 RequisitionId, COUNT(*) as rows, COUNT(DISTINCT VendorCode) as vendors
FROM vw_ReqTotalsByVendor
WHERE RequisitionId > 60000000
GROUP BY RequisitionId
HAVING COUNT(*) > 1
ORDER BY RequisitionId DESC
""")
rows = cursor.fetchall()
cols = [c[0] for c in cursor.description]
print('\t'.join(cols))
for r in rows:
    print('\t'.join(str(x) for x in r))

if rows:
    sample_req = rows[0][0]
    print(f"\n=== DETAIL for RequisitionId {sample_req} ===")
    cursor.execute(f"""
    SELECT VendorCode, VendorName, ItemsTotal, HandlingAmount, TotalShippingCost, VendorTotal, POBelowMinimum, MinimumPOAmount, UpdateRequired
    FROM vw_ReqTotalsByVendor
    WHERE RequisitionId = {sample_req}
    """)
    rows2 = cursor.fetchall()
    cols2 = [c[0] for c in cursor.description]
    print('\t'.join(cols2))
    for r in rows2:
        print('\t'.join(str(x) for x in r))

# 3. Check for cases where same vendor appears multiple times in same req
print("\n=== DUPLICATE VENDOR ROWS (same vendor, same req) ===")
cursor.execute("""
SELECT TOP 10 RequisitionId, VendorCode, VendorName, COUNT(*) as row_count
FROM vw_ReqTotalsByVendor
WHERE RequisitionId > 60000000
GROUP BY RequisitionId, VendorCode, VendorName
HAVING COUNT(*) > 1
ORDER BY RequisitionId DESC
""")
rows3 = cursor.fetchall()
cols3 = [c[0] for c in cursor.description]
print('\t'.join(cols3))
for r in rows3:
    print('\t'.join(str(x) for x in r))

# 4. Check POBelowMinimum - cases where it should be 1
print("\n=== RECENT REQS WHERE POBelowMinimum = 1 ===")
cursor.execute("""
SELECT TOP 10 RequisitionId, VendorCode, VendorName, ItemsTotal, VendorTotal, MinimumPOAmount, POBelowMinimum
FROM vw_ReqTotalsByVendor
WHERE POBelowMinimum = 1 AND RequisitionId > 59000000
ORDER BY RequisitionId DESC
""")
rows4 = cursor.fetchall()
cols4 = [c[0] for c in cursor.description]
print('\t'.join(cols4))
for r in rows4:
    print('\t'.join(str(x) for x in r))

# 5. Check POBelowMinimum accuracy: compare view vs upstream
print("\n=== POBelowMinimum: VIEW vs UPSTREAM (vw_RequisitionShippingCosts) ===")
cursor.execute("""
SELECT TOP 10
    v.RequisitionId, v.VendorCode, v.VendorName,
    v.POBelowMinimum AS view_POBelowMin,
    rsc.POBelowMinimum AS upstream_POBelowMin,
    v.VendorTotal AS view_VendorTotal,
    rsc.Extended AS upstream_Extended,
    v.MinimumPOAmount
FROM vw_ReqTotalsByVendor v
JOIN vw_RequisitionShippingCosts rsc
    ON rsc.RequisitionId = v.RequisitionId
    AND rsc.VendorId = (SELECT VendorId FROM Vendors WHERE Code = v.VendorCode)
WHERE v.RequisitionId > 60000000
    AND v.POBelowMinimum != rsc.POBelowMinimum
ORDER BY v.RequisitionId DESC
""")
rows5 = cursor.fetchall()
cols5 = [c[0] for c in cursor.description]
print('\t'.join(cols5))
for r in rows5:
    print('\t'.join(str(x) for x in r))

if not rows5:
    print("(no mismatches found)")

conn.close()
print("\nDone.")
