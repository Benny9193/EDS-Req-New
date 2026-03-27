import pyodbc
import sys

out = open(r'C:\EDS\fix_view_output.txt', 'w')

def p(s=''):
    print(s)
    out.write(s + '\n')
    out.flush()

try:
    p("Connecting...")
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
    p("Connected.")

    # BEFORE
    p()
    p("=== BEFORE: vw_ReqTotalsByVendor for req 60076856 ===")
    cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum, MinimumPOAmount
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60076856
""")
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    p()
    p("Applying ALTER VIEW...")

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
    p("ALTER VIEW applied successfully.")

    # AFTER
    p()
    p("=== AFTER: vw_ReqTotalsByVendor for req 60076856 ===")
    cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum, MinimumPOAmount
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60076856
""")
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    conn.close()
    p()
    p("Done.")

except Exception as e:
    p(f"ERROR: {e}")
    import traceback
    p(traceback.format_exc())
finally:
    out.close()
