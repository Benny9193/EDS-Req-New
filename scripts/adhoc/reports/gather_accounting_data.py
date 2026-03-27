"""Gather comprehensive data about each accounting system for documentation."""
import pyodbc
import json
import decimal

conn_str = (
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;'
    'UID=EDSAdmin;'
    'PWD=Consultant~!;'
    'TrustServerCertificate=yes;'
)

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

results = {}

# 1. All accounting format details
print("=== 1. Accounting Format Details ===")
cursor.execute("SELECT * FROM dbo.AccountingFormats ORDER BY AccountingFormatId")
cols = [d[0] for d in cursor.description]
results['formats'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  {len(results['formats'])} formats found")

# 2. Districts per format
print("\n=== 2. Districts Per Accounting System ===")
cursor.execute("""
    SELECT d.DistrictId, d.DistrictCode, d.Name, d.City, d.State, d.County,
           d.AccountingFormatId, d.RequireAccounts, d.CurrentBudgetOnly,
           d.AccountSeparator, d.AccountingDistrictCode, d.AccountingSystemOptions,
           d.DistrictTypeId, dt.Description AS DistrictType,
           af.Description AS AccountingSystem, af.ShortName,
           af.MaxPODetailItems, af.LocationCodeRequired, af.VendorBidNumberRequired,
           af.VendorBidCommentsRequired, af.UsersDistrictAccountingCodeRequired,
           af.IncidentalOrdersSupported, af.DetailedFormat, af.ScriptURL,
           (SELECT COUNT(*) FROM dbo.School s WHERE s.DistrictId = d.DistrictId) AS SchoolCount,
           (SELECT COUNT(*) FROM dbo.Accounts a WHERE a.DistrictId = d.DistrictId AND a.Active = 1) AS AccountCount
    FROM dbo.District d
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    LEFT JOIN dbo.DistrictTypes dt ON d.DistrictTypeId = dt.DistrictTypeId
    WHERE d.Active = 1
    ORDER BY af.Description, d.Name
""")
cols = [d[0] for d in cursor.description]
results['districts'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  {len(results['districts'])} active districts")

# 3. User fields per accounting format
print("\n=== 3. Accounting User Fields ===")
cursor.execute("""
    SELECT auf.AccountingFormatId, af.Description AS FormatName,
           auf.DistrictId, d.Name AS DistrictName,
           auf.FieldPos, auf.FieldName, auf.RequiredField
    FROM dbo.AccountingUserFields auf
    JOIN dbo.AccountingFormats af ON auf.AccountingFormatId = af.AccountingFormatId
    JOIN dbo.District d ON auf.DistrictId = d.DistrictId
    ORDER BY auf.AccountingFormatId, auf.DistrictId, auf.FieldPos
""")
cols = [d[0] for d in cursor.description]
results['user_fields'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  {len(results['user_fields'])} user field configs")

# 4. Sample account codes per system (limit per system)
print("\n=== 4. Account Code Samples ===")
cursor.execute("""
    SELECT af.Description AS SystemName, d.Name AS DistrictName, a.Code, a.Description AS AcctDesc
    FROM dbo.Accounts a
    JOIN dbo.District d ON a.DistrictId = d.DistrictId
    JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE a.Active = 1 AND d.Active = 1
    ORDER BY af.Description, d.Name, a.Code
""")
cols = [d[0] for d in cursor.description]
results['accounts'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  {len(results['accounts'])} active accounts")

# 5. Budget data summary
print("\n=== 5. Budget Data ===")
cursor.execute("""
    SELECT d.Name AS DistrictName, af.Description AS SystemName,
           b.Name AS BudgetName, b.Active, b.StartDate, b.EndDate,
           COUNT(ba.BudgetAccountId) AS AccountCount,
           SUM(ba.BudgetAmount) AS TotalBudget,
           SUM(ba.AmountAvailable) AS TotalAvailable
    FROM dbo.Budgets b
    JOIN dbo.District d ON b.DistrictId = d.DistrictId
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    LEFT JOIN dbo.BudgetAccounts ba ON b.BudgetId = ba.BudgetId
    WHERE d.Active = 1
    GROUP BY d.Name, af.Description, b.Name, b.Active, b.StartDate, b.EndDate
    ORDER BY d.Name, b.StartDate
""")
cols = [d[0] for d in cursor.description]
budgets = []
for row in cursor.fetchall():
    d = dict(zip(cols, row))
    for k, v in d.items():
        if hasattr(v, 'isoformat'):
            d[k] = v.isoformat()
        if isinstance(v, decimal.Decimal):
            d[k] = float(v)
    budgets.append(d)
results['budgets'] = budgets
print(f"  {len(budgets)} budget records")

# 6. Requisition counts by system
print("\n=== 6. Requisition Volume by System ===")
cursor.execute("""
    SELECT af.Description AS SystemName,
           COUNT(r.RequisitionId) AS ReqCount,
           MIN(r.DateEntered) AS EarliestReq,
           MAX(r.DateEntered) AS LatestReq
    FROM dbo.Requisitions r
    JOIN dbo.School s ON r.SchoolId = s.SchoolId
    JOIN dbo.District d ON s.DistrictId = d.DistrictId
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE d.Active = 1
    GROUP BY af.Description
    ORDER BY COUNT(r.RequisitionId) DESC
""")
cols = [d[0] for d in cursor.description]
req_volumes = []
for row in cursor.fetchall():
    d = dict(zip(cols, row))
    for k, v in d.items():
        if hasattr(v, 'isoformat'):
            d[k] = v.isoformat()
    req_volumes.append(d)
    print(f"  {d['SystemName']}: {d['ReqCount']:,}")
results['req_volumes'] = req_volumes

# 7. PO volume by system
print("\n=== 7. PO Volume by System ===")
cursor.execute("""
    SELECT af.Description AS SystemName, COUNT(p.POId) AS POCount
    FROM dbo.PO p
    JOIN dbo.Requisitions r ON p.RequisitionId = r.RequisitionId
    JOIN dbo.School s ON r.SchoolId = s.SchoolId
    JOIN dbo.District d ON s.DistrictId = d.DistrictId
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE d.Active = 1
    GROUP BY af.Description
    ORDER BY COUNT(p.POId) DESC
""")
cols = [d[0] for d in cursor.description]
po_volumes = []
for row in cursor.fetchall():
    d = dict(zip(cols, row))
    po_volumes.append(d)
    print(f"  {d['SystemName']}: {d['POCount']:,}")
results['po_volumes'] = po_volumes

# 8. Stored procedures related to accounting
print("\n=== 8. Accounting-Related Stored Procedures ===")
cursor.execute("""
    SELECT ROUTINE_NAME, ROUTINE_TYPE
    FROM INFORMATION_SCHEMA.ROUTINES
    WHERE ROUTINE_NAME LIKE '%Account%' OR ROUTINE_NAME LIKE '%Budget%'
       OR ROUTINE_NAME LIKE '%Ledger%' OR ROUTINE_NAME LIKE '%Requisition%'
       OR ROUTINE_NAME LIKE '%Finance%' OR ROUTINE_NAME LIKE '%Export%'
    ORDER BY ROUTINE_NAME
""")
procs = []
for row in cursor.fetchall():
    procs.append({'name': row.ROUTINE_NAME, 'type': row.ROUTINE_TYPE})
    print(f"  {row.ROUTINE_TYPE}: {row.ROUTINE_NAME}")
results['stored_procs'] = procs

# 9. Coops
print("\n=== 9. Cooperative Organizations ===")
cursor.execute("""
    SELECT c.CoopId, c.Description, COUNT(d.DistrictId) AS DistrictCount
    FROM dbo.Coops c
    LEFT JOIN dbo.District d ON d.CoopId = c.CoopId AND d.Active = 1
    GROUP BY c.CoopId, c.Description
    ORDER BY COUNT(d.DistrictId) DESC
""")
cols = [d[0] for d in cursor.description]
results['coops'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
for c in results['coops']:
    print(f"  {c['Description']}: {c['DistrictCount']}")

# 10. School table structure
print("\n=== 10. School Table Columns ===")
cursor.execute("""
    SELECT COLUMN_NAME, DATA_TYPE
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_NAME = 'School' AND TABLE_SCHEMA = 'dbo'
    ORDER BY ORDINAL_POSITION
""")
for row in cursor.fetchall():
    print(f"  {row.COLUMN_NAME}: {row.DATA_TYPE}")

conn.close()

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        return super().default(obj)

with open('output/accounting_data.json', 'w') as f:
    json.dump(results, f, cls=CustomEncoder, indent=2)
print("\nData saved to output/accounting_data.json")
