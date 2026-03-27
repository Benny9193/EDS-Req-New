"""
Verify the "Undo Downloaded Requisition" SQL script against the live EDS database.
Checks schema, data, and tests the logic without making changes.
"""
import pyodbc
import os
from dotenv import load_dotenv

load_dotenv()

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={os.getenv('DB_SERVER')};"
    f"DATABASE={os.getenv('DB_DATABASE_CATALOG')};"
    f"UID={os.getenv('DB_USERNAME')};"
    f"PWD={os.getenv('DB_PASSWORD')}"
)

def run():
    conn = pyodbc.connect(conn_str)
    cursor = conn.cursor()

    print("=" * 70)
    print("STEP 1: Verify StatusTable has 'H' (On Hold) status code")
    print("=" * 70)
    cursor.execute("SELECT StatusId, StatusCode, Name, RequiredLevel FROM StatusTable ORDER BY StatusId")
    rows = cursor.fetchall()
    found_h = False
    for r in rows:
        marker = " <-- ON HOLD" if r.StatusCode and r.StatusCode.strip() == 'H' else ""
        print(f"  StatusId={r.StatusId}, Code='{r.StatusCode}', Name='{r.Name}', RequiredLevel={r.RequiredLevel}{marker}")
        if r.StatusCode and r.StatusCode.strip() == 'H':
            found_h = True
    print(f"\n  'H' (On Hold) status exists: {found_h}")

    print("\n" + "=" * 70)
    print("STEP 2: Verify Approvals table structure")
    print("=" * 70)
    cursor.execute("""
        SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, CHARACTER_MAXIMUM_LENGTH
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'Approvals'
        ORDER BY ORDINAL_POSITION
    """)
    rows = cursor.fetchall()
    cols = [r.COLUMN_NAME for r in rows]
    for r in rows:
        print(f"  {r.COLUMN_NAME} ({r.DATA_TYPE}, nullable={r.IS_NULLABLE})")

    required = ['ApprovalId', 'RequisitionId', 'StatusId']
    missing = [c for c in required if c not in cols]
    print(f"\n  Required columns present: {len(missing) == 0}")
    if missing:
        print(f"  MISSING: {missing}")
    print(f"  All columns: {cols}")

    print("\n" + "=" * 70)
    print("STEP 3: Verify PO table has DateExported column")
    print("=" * 70)
    cursor.execute("""
        SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'PO'
        ORDER BY ORDINAL_POSITION
    """)
    rows = cursor.fetchall()
    po_cols = [r.COLUMN_NAME for r in rows]
    for r in rows:
        marker = " <-- TARGET" if r.COLUMN_NAME == 'DateExported' else ""
        print(f"  {r.COLUMN_NAME} ({r.DATA_TYPE}, nullable={r.IS_NULLABLE}){marker}")

    has_date_exported = 'DateExported' in po_cols
    print(f"\n  DateExported column exists: {has_date_exported}")

    print("\n" + "=" * 70)
    print("STEP 4: Find requisition #26 and check current status")
    print("=" * 70)
    cursor.execute("""
        SELECT TOP 1
            R.RequisitionId,
            R.RequisitionNumber,
            A.ApprovalId,
            A.StatusId,
            ST.StatusCode,
            ST.Name AS StatusName,
            A.ApprovalDate
        FROM Requisitions R
        JOIN Approvals A ON A.RequisitionId = R.RequisitionId
            AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        WHERE R.RequisitionNumber = 26
    """)
    row = cursor.fetchone()
    if row:
        print(f"  RequisitionId: {row.RequisitionId}")
        print(f"  RequisitionNumber: {row.RequisitionNumber}")
        print(f"  Current ApprovalId: {row.ApprovalId}")
        print(f"  Current StatusId: {row.StatusId}")
        print(f"  Current StatusCode: '{row.StatusCode}'")
        print(f"  Current StatusName: '{row.StatusName}'")
        print(f"  ApprovalDate: {row.ApprovalDate}")
    else:
        print("  Requisition #26 NOT FOUND - trying to find it differently...")
        cursor.execute("SELECT TOP 5 RequisitionId, RequisitionNumber FROM Requisitions WHERE RequisitionNumber = 26")
        for r in cursor.fetchall():
            print(f"    RequisitionId={r.RequisitionId}, RequisitionNumber={r.RequisitionNumber}")

    print("\n" + "=" * 70)
    print("STEP 5: Check PO records for requisition #26")
    print("=" * 70)
    cursor.execute("""
        SELECT PO.POID, PO.RequisitionId, PO.PONumber, PO.DateExported, PO.POStatusId,
               POST.StatusName AS POStatusName
        FROM PO
        LEFT JOIN POStatusTable POST ON POST.POStatusID = PO.POStatusId
        WHERE PO.RequisitionId = (
            SELECT TOP 1 RequisitionId FROM Requisitions WHERE RequisitionNumber = 26
        )
    """)
    rows = cursor.fetchall()
    if rows:
        for r in rows:
            print(f"  POID={r.POID}, PONumber={r.PONumber}, DateExported={r.DateExported}, POStatus={r.POStatusName}")
    else:
        print("  No PO records found for requisition #26")

    print("\n" + "=" * 70)
    print("STEP 6: Check vw_RequisitionStatus for requisition #26")
    print("=" * 70)
    try:
        cursor.execute("""
            SELECT *
            FROM vw_RequisitionStatus
            WHERE RequisitionId = (
                SELECT TOP 1 RequisitionId FROM Requisitions WHERE RequisitionNumber = 26
            )
        """)
        rows = cursor.fetchall()
        if rows:
            cols = [desc[0] for desc in cursor.description]
            for r in rows:
                for i, c in enumerate(cols):
                    print(f"  {c}: {r[i]}")
        else:
            print("  No rows in vw_RequisitionStatus for req #26")
    except Exception as e:
        print(f"  Error querying vw_RequisitionStatus: {e}")

    print("\n" + "=" * 70)
    print("STEP 7: Show some 'Downloaded' requisitions as examples")
    print("=" * 70)
    try:
        cursor.execute("""
            SELECT TOP 10
                R.RequisitionId,
                R.RequisitionNumber,
                ST.Name AS ApprovalStatus,
                ST.StatusCode,
                vwRS.StatusDesc
            FROM Requisitions R
            JOIN Approvals A ON A.RequisitionId = R.RequisitionId
                AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
            JOIN StatusTable ST ON ST.StatusId = A.StatusId
            LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
            WHERE vwRS.StatusDesc LIKE '%Downloaded%'
            ORDER BY R.RequisitionNumber DESC
        """)
        rows = cursor.fetchall()
        if rows:
            for r in rows:
                print(f"  Req#{r.RequisitionNumber} (ID={r.RequisitionId}): Approval='{r.ApprovalStatus}' ({r.StatusCode}), Display='{r.StatusDesc}'")
        else:
            print("  No requisitions with 'Downloaded' status desc found")
    except Exception as e:
        print(f"  Error: {e}")

    print("\n" + "=" * 70)
    print("STEP 8: Check Approvals table columns for INSERT statement")
    print("=" * 70)
    cursor.execute("""
        SELECT COLUMN_NAME, IS_NULLABLE, COLUMN_DEFAULT, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'Approvals'
          AND COLUMNPROPERTY(OBJECT_ID('Approvals'), COLUMN_NAME, 'IsIdentity') = 0
        ORDER BY ORDINAL_POSITION
    """)
    rows = cursor.fetchall()
    print("  Non-identity (insertable) columns:")
    for r in rows:
        print(f"    {r.COLUMN_NAME} ({r.DATA_TYPE}, nullable={r.IS_NULLABLE}, default={r.COLUMN_DEFAULT})")

    cursor.close()
    conn.close()
    print("\n" + "=" * 70)
    print("VERIFICATION COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    run()
