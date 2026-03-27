"""
Fix vw_ReqTotalsByVendor: Remove window function, revert to pass-through of upstream POBelowMinimum.

The previous fix (fix_view2.py) added a SUM() OVER (PARTITION BY) window function
which adds Table Spool + Segment operators to every query execution plan.
The upstream vw_RequisitionShippingCosts already computes POBelowMinimum correctly
per vendor group, so the window function is redundant overhead.
"""
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
conn.autocommit = True
cursor = conn.cursor()

# Verify current definition has the window function
print("=== CURRENT DEFINITION ===")
cursor.execute("""
SELECT definition FROM sys.sql_modules
WHERE object_id = OBJECT_ID('vw_ReqTotalsByVendor')
""")
current_def = cursor.fetchone()[0]
has_window = 'OVER' in current_def and 'PARTITION BY' in current_def
print(f"Has window function: {has_window}")

if not has_window:
    print("View does NOT have a window function. No fix needed.")
    conn.close()
    exit()

# Sample before data
print("\n=== BEFORE FIX: Sample data (req 60158736) ===")
cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum, MinimumPOAmount
FROM vw_ReqTotalsByVendor WHERE RequisitionId = 60158736
""")
for r in cursor.fetchall():
    print(f"  {r[0]} {r[1]}: Items={r[2]}, Total={r[3]}, POBelowMin={r[4]}, MinPO={r[5]}")

# Time before
times_before = []
for _ in range(5):
    start = time.time()
    cursor.execute("SELECT * FROM vw_ReqTotalsByVendor WHERE RequisitionId = 60158736")
    cursor.fetchall()
    times_before.append(time.time() - start)
print(f"\nBefore timing (5 runs): {[f'{t:.3f}' for t in times_before]}  avg={sum(times_before)/len(times_before):.3f}s")

# Apply the fix - revert to simple pass-through
print("\n=== APPLYING FIX: Reverting to pass-through POBelowMinimum ===")
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
    rsc.POBelowMinimum,
    rsc.MinimumPOAmount,
    rsc.AdditionalShipping,
    rsc.TotalShippingCost,
    rsc.UpdateRequired
FROM vw_RequisitionShippingCosts rsc
JOIN Vendors ON Vendors.VendorId = rsc.VendorId
""")
print("ALTER VIEW applied successfully.")

# Sample after data
print("\n=== AFTER FIX: Sample data (req 60158736) ===")
cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum, MinimumPOAmount
FROM vw_ReqTotalsByVendor WHERE RequisitionId = 60158736
""")
for r in cursor.fetchall():
    print(f"  {r[0]} {r[1]}: Items={r[2]}, Total={r[3]}, POBelowMin={r[4]}, MinPO={r[5]}")

# Time after
times_after = []
for _ in range(5):
    start = time.time()
    cursor.execute("SELECT * FROM vw_ReqTotalsByVendor WHERE RequisitionId = 60158736")
    cursor.fetchall()
    times_after.append(time.time() - start)
print(f"\nAfter timing (5 runs): {[f'{t:.3f}' for t in times_after]}  avg={sum(times_after)/len(times_after):.3f}s")

# Verify the new definition
print("\n=== VERIFY: New definition ===")
cursor.execute("""
SELECT definition FROM sys.sql_modules
WHERE object_id = OBJECT_ID('vw_ReqTotalsByVendor')
""")
new_def = cursor.fetchone()[0]
has_window_after = 'OVER' in new_def and 'PARTITION BY' in new_def
print(f"Has window function: {has_window_after}")
print(new_def[:1000])

conn.close()
print("\nDone.")
