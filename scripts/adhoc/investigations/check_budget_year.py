import pyodbc

conn = pyodbc.connect(
    'DRIVER={ODBC Driver 17 for SQL Server};'
    'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
    'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!'
)
cursor = conn.cursor()

# Check Budgets table structure and what year fields look like
print("=== Budgets columns ===")
cursor.execute("SELECT TOP 0 * FROM Budgets")
for col in cursor.description:
    print(col[0])

# See what budget years exist for Berkeley Heights (DistrictId=252)
print("\n=== Budget years for Berkeley Heights ===")
cursor.execute("""
    SELECT DISTINCT b.BudgetId, b.Name, b.StartDate, b.EndDate, b.Active
    FROM Budgets b
    WHERE b.DistrictId = 252
    ORDER BY b.StartDate DESC
""")
for row in cursor.fetchall():
    print(row)

conn.close()
