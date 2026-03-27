import pyodbc
import os
import time
from dotenv import load_dotenv

load_dotenv()

conn = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};'
    f'SERVER={os.getenv("DB_SERVER")};'
    f'DATABASE={os.getenv("DB_DATABASE_CATALOG", "EDS")};'
    f'UID={os.getenv("DB_USERNAME")};'
    f'PWD={os.getenv("DB_PASSWORD")};'
    f'timeout=60'
)
cursor = conn.cursor()

# Get XML execution plan for the view query
print("=== XML EXECUTION PLAN: vw_ReqTotalsByVendor ===")
cursor.execute("SET SHOWPLAN_XML ON")
cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60158736
""")
plan = cursor.fetchone()
if plan:
    xml = plan[0]
    # Extract key operations - look for table scans, index scans, seeks
    import re
    # Find all physical ops
    ops = re.findall(r'PhysicalOp="([^"]+)"', xml)
    print("Physical operations in plan:")
    for op in ops:
        print(f"  - {op}")

    # Find table/index references with scan/seek type
    rel_ops = re.findall(r'<RelOp[^>]*PhysicalOp="([^"]+)"[^>]*EstimatedTotalSubtreeCost="([^"]+)"[^>]*>', xml)
    print("\nOperations with cost:")
    for op, cost in rel_ops:
        print(f"  {op}: cost={cost}")

    # Find table scan / index scan details
    scans = re.findall(r'<(IndexScan|TableScan)[^>]*>.*?<Object[^>]*Table="\[([^\]]+)\]"[^>]*Index="\[([^\]]*)\]"[^/]*/>', xml, re.DOTALL)
    seeks = re.findall(r'<(IndexScan)[^>]*Lookup="([^"]*)"[^>]*>.*?<Object[^>]*Table="\[([^\]]+)\]"[^>]*Index="\[([^\]]*)\]"[^/]*/>', xml, re.DOTALL)

    # Better: just find all Object references with table and index
    objects = re.findall(r'<Object[^>]*Table="\[([^\]]+)\]"(?:[^>]*Index="\[([^\]]*)\]")?[^/]*/>', xml)
    print("\nTables/Indexes referenced in plan:")
    for table, idx in objects:
        print(f"  Table: {table}, Index: {idx if idx else '(heap/scan)'}")

    # Look for Segment/Window Spool operations (from window function)
    if 'Window Spool' in xml or 'Segment' in xml or 'Sequence Project' in xml:
        print("\n** WINDOW FUNCTION detected in plan (Segment/Window Spool/Sequence Project) **")

    # Save full XML for inspection
    with open('C:/EDS/plan_output.xml', 'w') as f:
        f.write(xml)
    print("\nFull plan saved to plan_output.xml")

cursor.execute("SET SHOWPLAN_XML OFF")

# Now compare: what does the ORIGINAL view definition plan look like?
print("\n\n=== COMPARISON: Plan for direct pass-through (no window function) ===")
cursor.execute("SET SHOWPLAN_XML ON")
cursor.execute("""
SELECT rsc.RequisitionId,
    COALESCE(Vendors.Code, '') VendorCode,
    rsc.VendorName,
    rsc.Extended + rsc.ShippingCost + rsc.TotalShippingCost VendorTotal,
    rsc.Extended ItemsTotal,
    rsc.POBelowMinimum,
    rsc.MinimumPOAmount
FROM vw_RequisitionShippingCosts rsc
JOIN Vendors ON Vendors.VendorId = rsc.VendorId
WHERE rsc.RequisitionId = 60158736
""")
plan2 = cursor.fetchone()
if plan2:
    xml2 = plan2[0]
    ops2 = re.findall(r'PhysicalOp="([^"]+)"', xml2)
    print("Physical operations (without window function):")
    for op in ops2:
        print(f"  - {op}")

    objects2 = re.findall(r'<Object[^>]*Table="\[([^\]]+)\]"(?:[^>]*Index="\[([^\]]*)\]")?[^/]*/>', xml2)
    print("\nTables/Indexes referenced:")
    for table, idx in objects2:
        print(f"  Table: {table}, Index: {idx if idx else '(heap/scan)'}")

    if 'Window Spool' in xml2 or 'Segment' in xml2 or 'Sequence Project' in xml2:
        print("\n** WINDOW FUNCTION detected **")
    else:
        print("\n** No window function overhead **")

    with open('C:/EDS/plan_output_nowindow.xml', 'w') as f:
        f.write(xml2)
    print("Full plan saved to plan_output_nowindow.xml")

cursor.execute("SET SHOWPLAN_XML OFF")

# Timing comparison
print("\n\n=== TIMING COMPARISON ===")

# Current view (with window function)
times1 = []
for i in range(3):
    start = time.time()
    cursor.execute("SELECT * FROM vw_ReqTotalsByVendor WHERE RequisitionId = 60158736")
    cursor.fetchall()
    times1.append(time.time() - start)

# Direct query without window function
times2 = []
for i in range(3):
    start = time.time()
    cursor.execute("""
    SELECT rsc.RequisitionId, COALESCE(Vendors.Code, '') VendorCode, rsc.VendorName,
           rsc.AdditionalHandlingAmount, rsc.FreeHandlingAmount, rsc.FreeHandlingStart, rsc.FreeHandlingEnd,
           rsc.ShippingCost HandlingAmount,
           rsc.Extended + rsc.ShippingCost + rsc.TotalShippingCost VendorTotal,
           rsc.Extended ItemsTotal,
           rsc.POBelowMinimum,
           rsc.MinimumPOAmount, rsc.AdditionalShipping, rsc.TotalShippingCost, rsc.UpdateRequired
    FROM vw_RequisitionShippingCosts rsc
    JOIN Vendors ON Vendors.VendorId = rsc.VendorId
    WHERE rsc.RequisitionId = 60158736
    """)
    cursor.fetchall()
    times2.append(time.time() - start)

print(f"Current view (window func):   avg={sum(times1)/len(times1):.3f}s  [{', '.join(f'{t:.3f}' for t in times1)}]")
print(f"Without window function:      avg={sum(times2)/len(times2):.3f}s  [{', '.join(f'{t:.3f}' for t in times2)}]")

conn.close()
print("\nDone.")
