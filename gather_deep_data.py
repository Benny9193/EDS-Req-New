"""Gather deep data: stored proc source, trends, approval flows, PO workflows."""
import pyodbc
import json
import decimal
from datetime import datetime

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

# ============================================================
# 1. STORED PROCEDURE SOURCE CODE
# ============================================================
print("=== 1. Stored Procedure Source Code ===")
key_procs = [
    'sp_FA_AddUpdateAccountCode', 'sp_FA_AvailableAccounts', 'sp_FA_DeleteAccount',
    'sp_FA_SetBudgetAccount', 'sp_FA_SetUserAccount',
    'sp_FA_UpdateRequisitionStatus', 'sp_FA_DeleteRequisition',
    'sp_FA_RequisitionsForPurchaseOrderModal', 'sp_FA_RequisitionsTotals',
    'sp_FA_SaveRequisitionNote', 'sp_FA_SaveRequisitionNoteEmails',
    'sp_RefreshAccounts', 'sp_MergeAccounts',
    'sp_ResetDistrictAccountingYear', 'sp_SetBudgetYear', 'sp_SetDistrictAndBudgetYear',
    'sp_CopyBudgetAmounts', 'sp_MasterBudgetBook',
    'sp_CreateNewRequisition', 'sp_SubmitRequisition', 'sp_SubmitRequisitionNew',
    'sp_DeleteRequisition', 'sp_HoldRequisition',
    'sp_GetUserRequisitions', 'sp_CanDeleteRequisition',
    'sp_CCAccountMaint', 'sp_CCUpdateUserAccounts', 'sp_CCUserAccountMaint',
    'sp_PAAccounts', 'sp_PABudgets', 'sp_PARequisitions',
    'usp_BringAccountsForward', 'usp_UpdateBudgets', 'usp_POPrintExport',
    'sp_FA_AttemptLogin',
]

proc_sources = {}
for proc_name in key_procs:
    cursor.execute("""
        SELECT OBJECT_DEFINITION(OBJECT_ID(?))
    """, proc_name)
    row = cursor.fetchone()
    if row and row[0]:
        proc_sources[proc_name] = row[0]
        print(f"  {proc_name}: {len(row[0])} chars")
    else:
        print(f"  {proc_name}: NOT FOUND")
results['proc_sources'] = proc_sources

# Also get functions
key_functions = [
    'uf_ActiveAccountList', 'uf_FA_Requisitions', 'uf_IsRequisitionLocked',
    'uf_OrderOrBudgetBook', 'uf_POAccountList', 'uf_POAccountsUsed',
    'uf_RequisitionData', 'uf_RequisitionStatus', 'uf_RequisitionIsVisible',
    'uf_UserTreeBudget', 'uf_PackCodeExport',
]
func_sources = {}
for fn in key_functions:
    cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID(?))", fn)
    row = cursor.fetchone()
    if row and row[0]:
        func_sources[fn] = row[0]
        print(f"  {fn}: {len(row[0])} chars")
results['func_sources'] = func_sources

# ============================================================
# 2. YEARLY TRANSACTION TRENDS
# ============================================================
print("\n=== 2. Yearly Transaction Trends ===")
cursor.execute("""
    SELECT YEAR(r.DateEntered) AS Yr,
           af.Description AS SystemName,
           COUNT(r.RequisitionId) AS ReqCount,
           SUM(r.TotalRequisitionCost) AS TotalValue
    FROM dbo.Requisitions r
    JOIN dbo.School s ON r.SchoolId = s.SchoolId
    JOIN dbo.District d ON s.DistrictId = d.DistrictId
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE d.Active = 1 AND r.DateEntered IS NOT NULL
    GROUP BY YEAR(r.DateEntered), af.Description
    ORDER BY YEAR(r.DateEntered), af.Description
""")
cols = [d[0] for d in cursor.description]
yearly_reqs = []
for row in cursor.fetchall():
    d = dict(zip(cols, row))
    if isinstance(d.get('TotalValue'), decimal.Decimal):
        d['TotalValue'] = float(d['TotalValue'])
    yearly_reqs.append(d)
results['yearly_reqs'] = yearly_reqs
print(f"  {len(yearly_reqs)} year/system combinations")

# PO trends
cursor.execute("""
    SELECT YEAR(p.PODate) AS Yr,
           af.Description AS SystemName,
           COUNT(p.POId) AS POCount,
           SUM(p.Amount) AS TotalAmount
    FROM dbo.PO p
    JOIN dbo.Requisitions r ON p.RequisitionId = r.RequisitionId
    JOIN dbo.School s ON r.SchoolId = s.SchoolId
    JOIN dbo.District d ON s.DistrictId = d.DistrictId
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE d.Active = 1 AND p.PODate IS NOT NULL
    GROUP BY YEAR(p.PODate), af.Description
    ORDER BY YEAR(p.PODate), af.Description
""")
cols = [d[0] for d in cursor.description]
yearly_pos = []
for row in cursor.fetchall():
    d = dict(zip(cols, row))
    if isinstance(d.get('TotalAmount'), decimal.Decimal):
        d['TotalAmount'] = float(d['TotalAmount'])
    yearly_pos.append(d)
results['yearly_pos'] = yearly_pos
print(f"  {len(yearly_pos)} year/system PO combinations")

# ============================================================
# 3. APPROVAL WORKFLOW DATA
# ============================================================
print("\n=== 3. Approval Workflow ===")

# Approval levels
cursor.execute("SELECT * FROM dbo.ApprovalLevels ORDER BY ApprovalLevelId")
cols = [d[0] for d in cursor.description]
results['approval_levels'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  Approval levels: {len(results['approval_levels'])}")

# Status table
cursor.execute("SELECT * FROM dbo.StatusTable ORDER BY StatusId")
cols = [d[0] for d in cursor.description]
results['statuses'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  Statuses: {len(results['statuses'])}")
for s in results['statuses']:
    print(f"    [{s.get('StatusId')}] {s.get('Name', '')}")

# PO Status
cursor.execute("SELECT * FROM dbo.POStatusTable ORDER BY POStatusID")
cols = [d[0] for d in cursor.description]
results['po_statuses'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  PO Statuses: {len(results['po_statuses'])}")
for s in results['po_statuses']:
    print(f"    [{s.get('POStatusID')}] {s.get('StatusName', '')}")

# District approval requirements
cursor.execute("""
    SELECT af.Description AS SystemName,
           d.RequiredApprovalLevel,
           COUNT(*) AS DistrictCount
    FROM dbo.District d
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE d.Active = 1
    GROUP BY af.Description, d.RequiredApprovalLevel
    ORDER BY af.Description, d.RequiredApprovalLevel
""")
cols = [d[0] for d in cursor.description]
results['approval_by_system'] = [dict(zip(cols, row)) for row in cursor.fetchall()]

# ============================================================
# 4. ACCOUNT CODE PATTERN ANALYSIS
# ============================================================
print("\n=== 4. Account Code Pattern Analysis ===")
cursor.execute("""
    SELECT af.Description AS SystemName,
           d.AccountSeparator,
           LEN(a.Code) AS CodeLength,
           COUNT(*) AS CodeCount
    FROM dbo.Accounts a
    JOIN dbo.District d ON a.DistrictId = d.DistrictId
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    WHERE a.Active = 1 AND d.Active = 1
    GROUP BY af.Description, d.AccountSeparator, LEN(a.Code)
    ORDER BY af.Description, LEN(a.Code)
""")
cols = [d[0] for d in cursor.description]
results['code_patterns'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  {len(results['code_patterns'])} pattern combinations")

# ============================================================
# 5. PO EXPORT/PRINT WORKFLOW
# ============================================================
print("\n=== 5. PO Layout Details ===")
cursor.execute("""
    SELECT pl.POLayoutId, pl.Name AS LayoutName,
           pl.FormLength, pl.FormWidth, pl.ContinuousFeed, pl.Copies
    FROM dbo.POLayouts pl
    ORDER BY pl.POLayoutId
""")
cols = [d[0] for d in cursor.description]
results['po_layouts'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  PO Layouts: {len(results['po_layouts'])}")
for l in results['po_layouts']:
    print(f"    [{l['POLayoutId']}] {l['LayoutName']}")

# PO layout fields (standalone reference table, not linked to POLayouts by FK)
cursor.execute("""
    SELECT plf.POLayoutFieldId, plf.POLayoutField, plf.POLayoutSource,
           plf.POLayoutFieldType, plf.DetailField
    FROM dbo.POLayoutFields plf
    ORDER BY plf.POLayoutFieldId
""")
cols = [d[0] for d in cursor.description]
results['po_layout_fields'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  PO Layout Fields: {len(results['po_layout_fields'])}")

# District PO layout assignments
cursor.execute("""
    SELECT af.Description AS SystemName,
           pl.Name AS LayoutName,
           COUNT(d.DistrictId) AS DistrictCount
    FROM dbo.District d
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    LEFT JOIN dbo.POLayouts pl ON d.POLayoutId = pl.POLayoutId
    WHERE d.Active = 1
    GROUP BY af.Description, pl.Name
    ORDER BY af.Description, pl.Name
""")
cols = [d[0] for d in cursor.description]
results['po_layout_by_system'] = [dict(zip(cols, row)) for row in cursor.fetchall()]

# ============================================================
# 6. TRANSACTION TYPES & LEDGER
# ============================================================
print("\n=== 6. Transaction Types ===")
cursor.execute("SELECT * FROM dbo.TransactionTypes ORDER BY TransactionTypeId")
cols = [d[0] for d in cursor.description]
results['transaction_types'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
for t in results['transaction_types']:
    print(f"  [{t.get('TransactionTypeId')}] {t.get('Description', '')}")

# Ledger summary
cursor.execute("""
    SELECT tt.Description AS TransType, COUNT(*) AS EntryCount,
           SUM(l.Amount) AS TotalAmount, MIN(l.TransactionDate) AS Earliest,
           MAX(l.TransactionDate) AS Latest
    FROM dbo.Ledger l
    JOIN dbo.TransactionTypes tt ON l.TransactionTypeId = tt.TransactionTypeId
    GROUP BY tt.Description
    ORDER BY COUNT(*) DESC
""")
cols = [d[0] for d in cursor.description]
ledger_summary = []
for row in cursor.fetchall():
    d = dict(zip(cols, row))
    for k, v in d.items():
        if isinstance(v, decimal.Decimal):
            d[k] = float(v)
        if hasattr(v, 'isoformat'):
            d[k] = v.isoformat()
    ledger_summary.append(d)
results['ledger_summary'] = ledger_summary
print(f"  Ledger entries by type: {len(ledger_summary)}")

# ============================================================
# 7. DISTRICT CHARGES & SHIPPING
# ============================================================
print("\n=== 7. District Charges ===")
cursor.execute("""
    SELECT ct.Description AS ChargeType, COUNT(*) AS Count
    FROM dbo.DistrictCharges dc
    JOIN dbo.ChargeTypes ct ON dc.ChargeTypeId = ct.ChargeTypeId
    GROUP BY ct.Description
    ORDER BY COUNT(*) DESC
""")
cols = [d[0] for d in cursor.description]
results['charge_types'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
for c in results['charge_types']:
    print(f"  {c['ChargeType']}: {c['Count']}")

# ============================================================
# 8. INVOICE & PAYMENT DATA
# ============================================================
print("\n=== 8. Invoice & Payment Types ===")
cursor.execute("SELECT * FROM dbo.InvoiceTypes")
cols = [d[0] for d in cursor.description]
results['invoice_types'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
for i in results['invoice_types']:
    print(f"  Invoice: {i}")

cursor.execute("SELECT * FROM dbo.PaymentTypes")
cols = [d[0] for d in cursor.description]
results['payment_types'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
for p in results['payment_types']:
    print(f"  Payment: {p}")

# ============================================================
# 9. REQUISITION STATUS FLOW PER SYSTEM
# ============================================================
print("\n=== 9. Requisition Status Distribution by System ===")
cursor.execute("""
    SELECT af.Description AS SystemName,
           st.Name AS StatusDesc,
           r.StatusId,
           COUNT(*) AS ReqCount
    FROM dbo.Requisitions r
    JOIN dbo.School s ON r.SchoolId = s.SchoolId
    JOIN dbo.District d ON s.DistrictId = d.DistrictId
    LEFT JOIN dbo.AccountingFormats af ON d.AccountingFormatId = af.AccountingFormatId
    LEFT JOIN dbo.StatusTable st ON r.StatusId = st.StatusId
    WHERE d.Active = 1
    GROUP BY af.Description, st.Name, r.StatusId
    ORDER BY af.Description, COUNT(*) DESC
""")
cols = [d[0] for d in cursor.description]
results['status_by_system'] = [dict(zip(cols, row)) for row in cursor.fetchall()]
print(f"  {len(results['status_by_system'])} status/system combinations")

# ============================================================
# 10. VIEWS SOURCE CODE
# ============================================================
print("\n=== 10. View Definitions ===")
key_views = []
cursor.execute("""
    SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS
    WHERE TABLE_NAME LIKE '%Account%' OR TABLE_NAME LIKE '%Budget%'
       OR TABLE_NAME LIKE '%Req%' OR TABLE_NAME LIKE '%PO%'
""")
for row in cursor.fetchall():
    key_views.append(row[0])

view_sources = {}
for vname in key_views:
    cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID(?))", vname)
    row = cursor.fetchone()
    if row and row[0]:
        view_sources[vname] = row[0]
        print(f"  {vname}: {len(row[0])} chars")
results['view_sources'] = view_sources

conn.close()

class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        if hasattr(obj, 'isoformat'):
            return obj.isoformat()
        return super().default(obj)

with open('output/accounting_deep_data.json', 'w') as f:
    json.dump(results, f, cls=CustomEncoder, indent=2, default=str)
print(f"\nDeep data saved to output/accounting_deep_data.json")
print(f"Stored procs gathered: {len(proc_sources)}")
print(f"Functions gathered: {len(func_sources)}")
print(f"Views gathered: {len(view_sources)}")
