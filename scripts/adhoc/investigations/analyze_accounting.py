import pyodbc

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

# Sample districts with their accounting system
print('=== Sample Active Districts with Accounting Systems ===')
cursor.execute("""
    SELECT TOP 30 d.DistrictId, d.Name, d.City, d.State,
           af.Description AS AccountingSystem, af.ShortName,
           d.RequireAccounts, d.AccountSeparator
    FROM dbo.District d
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE d.Active = 1
    ORDER BY af.Description, d.Name
""")
for row in cursor.fetchall():
    acct = row.AccountingSystem or "None"
    print(f'  {row.Name} ({row.City}, {row.State}) -> {acct} | ReqAccounts={row.RequireAccounts} | Sep={row.AccountSeparator}')

# Budget info
print('\n=== Budget Summary by District (top 15 active) ===')
cursor.execute("""
    SELECT TOP 15 d.Name, b.Name AS BudgetName, b.StartDate, b.EndDate, b.Active,
           COUNT(ba.BudgetAccountId) AS AccountCount,
           SUM(ba.BudgetAmount) AS TotalBudget
    FROM dbo.Budgets b
    JOIN dbo.District d ON b.DistrictId = d.DistrictId
    LEFT JOIN dbo.BudgetAccounts ba ON b.BudgetId = ba.BudgetId
    GROUP BY d.Name, b.Name, b.StartDate, b.EndDate, b.Active
    ORDER BY b.Active DESC, d.Name
""")
for row in cursor.fetchall():
    budget = f'${row.TotalBudget:,.2f}' if row.TotalBudget else 'N/A'
    active = 'ACTIVE' if row.Active else 'inactive'
    print(f'  {row.Name} | {row.BudgetName} | {row.StartDate} to {row.EndDate} | {active} | {row.AccountCount} accounts | {budget}')

# Accounting system groupings
print('\n=== Accounting System Families ===')
cursor.execute("""
    SELECT
        CASE
            WHEN af.Description LIKE '%CSI%' THEN 'CSI'
            WHEN af.Description LIKE '%System%3000%' THEN 'Systems 3000'
            WHEN af.Description LIKE '%Finance Manager%' THEN 'Finance Manager'
            WHEN af.Description LIKE '%Genesis%' THEN 'Genesis'
            WHEN af.Description LIKE '%Wincap%' THEN 'WinCap'
            WHEN af.Description LIKE '%CDK%' THEN 'CDK'
            WHEN af.Description LIKE '%Pentamation%' THEN 'Pentamation'
            WHEN af.Description LIKE '%Edu-Met%' OR af.Description LIKE '%EMapp%' THEN 'Edu-Met/EMapp'
            WHEN af.Description LIKE '%Edmunds%' THEN 'Edmunds'
            WHEN af.Description LIKE '%Asbury%' THEN 'Asbury Park'
            WHEN af.Description LIKE '%Infinite%' THEN 'Infinite Visions'
            WHEN af.Description LIKE '%Sage%' OR af.Description LIKE '%Alio%' THEN 'Sage/Alio'
            WHEN af.Description LIKE '%APECS%' THEN 'APECS'
            WHEN af.Description LIKE '%Keystone%' THEN 'Keystone'
            WHEN af.Description LIKE '%No Accounting%' THEN 'No Accounting Interface'
            ELSE af.Description
        END AS SystemFamily,
        COUNT(d.DistrictId) AS DistrictCount
    FROM dbo.District d
    JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE d.Active = 1
    GROUP BY
        CASE
            WHEN af.Description LIKE '%CSI%' THEN 'CSI'
            WHEN af.Description LIKE '%System%3000%' THEN 'Systems 3000'
            WHEN af.Description LIKE '%Finance Manager%' THEN 'Finance Manager'
            WHEN af.Description LIKE '%Genesis%' THEN 'Genesis'
            WHEN af.Description LIKE '%Wincap%' THEN 'WinCap'
            WHEN af.Description LIKE '%CDK%' THEN 'CDK'
            WHEN af.Description LIKE '%Pentamation%' THEN 'Pentamation'
            WHEN af.Description LIKE '%Edu-Met%' OR af.Description LIKE '%EMapp%' THEN 'Edu-Met/EMapp'
            WHEN af.Description LIKE '%Edmunds%' THEN 'Edmunds'
            WHEN af.Description LIKE '%Asbury%' THEN 'Asbury Park'
            WHEN af.Description LIKE '%Infinite%' THEN 'Infinite Visions'
            WHEN af.Description LIKE '%Sage%' OR af.Description LIKE '%Alio%' THEN 'Sage/Alio'
            WHEN af.Description LIKE '%APECS%' THEN 'APECS'
            WHEN af.Description LIKE '%Keystone%' THEN 'Keystone'
            WHEN af.Description LIKE '%No Accounting%' THEN 'No Accounting Interface'
            ELSE af.Description
        END
    ORDER BY COUNT(d.DistrictId) DESC
""")
for row in cursor.fetchall():
    print(f'  {row.SystemFamily}: {row.DistrictCount} districts')

# District types
print('\n=== District Types ===')
cursor.execute("""
    SELECT dt.DistrictTypeId, dt.Description, COUNT(d.DistrictId) AS Count
    FROM dbo.DistrictTypes dt
    LEFT JOIN dbo.District d ON d.DistrictTypeId = dt.DistrictTypeId AND d.Active = 1
    GROUP BY dt.DistrictTypeId, dt.Description
    ORDER BY COUNT(d.DistrictId) DESC
""")
for row in cursor.fetchall():
    print(f'  {row.Description}: {row.Count} districts')

# Account code formats - sample patterns
print('\n=== Account Code Format Patterns (samples) ===')
cursor.execute("""
    SELECT TOP 30 d.Name, a.Code, af.Description AS AcctSystem
    FROM dbo.Accounts a
    JOIN dbo.District d ON a.DistrictId = d.DistrictId
    JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE a.Active = 1 AND d.Active = 1
    ORDER BY NEWID()
""")
for row in cursor.fetchall():
    print(f'  {row.Name} ({row.AcctSystem}): {row.Code}')

# State distribution
print('\n=== Districts by State ===')
cursor.execute("""
    SELECT State, COUNT(*) AS Count
    FROM dbo.District
    WHERE Active = 1
    GROUP BY State
    ORDER BY COUNT(*) DESC
""")
for row in cursor.fetchall():
    print(f'  {row.State}: {row.Count}')

conn.close()
