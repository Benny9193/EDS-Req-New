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

# 1. Time a typical query
print("=== TIMING: Single req lookup ===")
start = time.time()
cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60158736
""")
rows = cursor.fetchall()
elapsed = time.time() - start
print(f"Rows: {len(rows)}, Time: {elapsed:.3f}s")

# 2. Get execution plan (estimated)
print("\n=== EXECUTION PLAN (XML) ===")
cursor.execute("SET SHOWPLAN_TEXT ON")
cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60158736
""")
plan_rows = cursor.fetchall()
for r in plan_rows:
    print(r[0])
cursor.execute("SET SHOWPLAN_TEXT OFF")

# 3. Check IO stats for the query
print("\n=== IO STATISTICS ===")
cursor.execute("SET STATISTICS IO ON")
cursor.execute("SET STATISTICS TIME ON")
cursor.execute("""
SELECT VendorCode, VendorName, ItemsTotal, VendorTotal, POBelowMinimum
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60158736
""")
cursor.fetchall()
# Stats come as messages - try to get them
cursor.execute("SET STATISTICS IO OFF")
cursor.execute("SET STATISTICS TIME OFF")

# 4. Check indexes on key tables used by the views
print("\n=== INDEXES ON Detail TABLE ===")
cursor.execute("""
SELECT i.name AS IndexName, i.type_desc,
       STRING_AGG(c.name, ', ') WITHIN GROUP (ORDER BY ic.key_ordinal) AS Columns,
       i.is_unique
FROM sys.indexes i
JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
WHERE i.object_id = OBJECT_ID('Detail')
  AND ic.is_included_column = 0
GROUP BY i.name, i.type_desc, i.is_unique
ORDER BY i.type_desc, i.name
""")
rows = cursor.fetchall()
for r in rows:
    print(f"  {r[0]} ({r[1]}) - Columns: {r[2]} - Unique: {r[3]}")

print("\n=== INDEXES ON Requisitions TABLE ===")
cursor.execute("""
SELECT i.name AS IndexName, i.type_desc,
       STRING_AGG(c.name, ', ') WITHIN GROUP (ORDER BY ic.key_ordinal) AS Columns,
       i.is_unique
FROM sys.indexes i
JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
WHERE i.object_id = OBJECT_ID('Requisitions')
  AND ic.is_included_column = 0
GROUP BY i.name, i.type_desc, i.is_unique
ORDER BY i.type_desc, i.name
""")
rows = cursor.fetchall()
for r in rows:
    print(f"  {r[0]} ({r[1]}) - Columns: {r[2]} - Unique: {r[3]}")

print("\n=== INDEXES ON Vendors TABLE ===")
cursor.execute("""
SELECT i.name AS IndexName, i.type_desc,
       STRING_AGG(c.name, ', ') WITHIN GROUP (ORDER BY ic.key_ordinal) AS Columns,
       i.is_unique
FROM sys.indexes i
JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
WHERE i.object_id = OBJECT_ID('Vendors')
  AND ic.is_included_column = 0
GROUP BY i.name, i.type_desc, i.is_unique
ORDER BY i.type_desc, i.name
""")
rows = cursor.fetchall()
for r in rows:
    print(f"  {r[0]} ({r[1]}) - Columns: {r[2]} - Unique: {r[3]}")

# 5. Table sizes
print("\n=== TABLE ROW COUNTS ===")
cursor.execute("""
SELECT t.name, p.rows
FROM sys.tables t
JOIN sys.partitions p ON t.object_id = p.object_id AND p.index_id IN (0,1)
WHERE t.name IN ('Detail', 'Requisitions', 'Vendors', 'Bids', 'BidHeaders', 'BidItems', 'Budgets', 'District', 'Approvals', 'DistrictVendor')
ORDER BY p.rows DESC
""")
rows = cursor.fetchall()
for r in rows:
    print(f"  {r[0]}: {r[1]:,} rows")

# 6. Check the window function impact - compare with/without
print("\n=== TIMING: upstream vw_RequisitionShippingCosts directly ===")
start = time.time()
cursor.execute("""
SELECT RequisitionId, VendorId, VendorName, Extended, ShippingCost, TotalShippingCost, POBelowMinimum, MinimumPOAmount
FROM vw_RequisitionShippingCosts
WHERE RequisitionId = 60158736
""")
rows = cursor.fetchall()
elapsed = time.time() - start
print(f"Rows: {len(rows)}, Time: {elapsed:.3f}s")

# 7. Check if the window function SUM OVER is causing a spool/sort
print("\n=== EXECUTION PLAN: Window function view ===")
cursor.execute("SET SHOWPLAN_TEXT ON")
cursor.execute("""
SELECT *
FROM vw_ReqTotalsByVendor
WHERE RequisitionId = 60158736
""")
plan_rows = cursor.fetchall()
for r in plan_rows:
    print(r[0])
cursor.execute("SET SHOWPLAN_TEXT OFF")

conn.close()
print("\nDone.")
