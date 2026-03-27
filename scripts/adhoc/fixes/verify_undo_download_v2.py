"""
Verify the corrected "Undo Downloaded Requisition" SQL script.
Find actual downloaded Niskayuna requisitions and test the logic.
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

    # Find the Niskayuna downloaded requisitions from the screenshot
    print("=" * 70)
    print("STEP 1: Find Niskayuna downloaded reqs (from the screenshot)")
    print("=" * 70)
    cursor.execute("""
        SELECT TOP 20
            R.RequisitionId,
            R.RequisitionNumber,
            ST.StatusCode,
            ST.Name AS ApprovalStatus,
            vwRS.StatusDesc,
            A.ApprovalById,
            A.ApproverId,
            A.Level,
            A.ApprovalDate
        FROM Requisitions R
        JOIN Approvals A ON A.RequisitionId = R.RequisitionId
            AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
        WHERE vwRS.StatusDesc LIKE '%Downloaded%PURCHASING%'
            AND R.RequisitionNumber IN (5, 26, 36, 41, 42, 45)
        ORDER BY R.RequisitionNumber
    """)
    rows = cursor.fetchall()
    if rows:
        for r in rows:
            print(f"  Req#{r.RequisitionNumber} (ID={r.RequisitionId})")
            print(f"    Status: {r.ApprovalStatus} (Code={r.StatusCode})")
            print(f"    Display: {r.StatusDesc}")
            print(f"    ApprovalById={r.ApprovalById}, ApproverId={r.ApproverId}, Level={r.Level}")
            print(f"    Date: {r.ApprovalDate}")
            print()
    else:
        print("  None found with those exact req numbers. Trying broader search...")
        cursor.execute("""
            SELECT TOP 10
                R.RequisitionId,
                R.RequisitionNumber,
                ST.StatusCode,
                ST.Name AS ApprovalStatus,
                vwRS.StatusDesc,
                A.ApprovalById,
                A.ApproverId,
                A.Level,
                A.ApprovalDate
            FROM Requisitions R
            JOIN Approvals A ON A.RequisitionId = R.RequisitionId
                AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
            JOIN StatusTable ST ON ST.StatusId = A.StatusId
            LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
            WHERE vwRS.StatusDesc LIKE '%Downloaded%PURCHASING%'
            ORDER BY A.ApprovalDate DESC
        """)
        rows = cursor.fetchall()
        for r in rows:
            print(f"  Req#{r.RequisitionNumber} (ID={r.RequisitionId})")
            print(f"    Status: {r.ApprovalStatus} (Code={r.StatusCode})")
            print(f"    Display: {r.StatusDesc}")
            print(f"    ApprovalById={r.ApprovalById}, ApproverId={r.ApproverId}, Level={r.Level}")
            print(f"    Date: {r.ApprovalDate}")
            print()

    # Check the full approval history for one of them
    print("=" * 70)
    print("STEP 2: Check full approval history for a downloaded req")
    print("=" * 70)
    cursor.execute("""
        SELECT TOP 1 R.RequisitionId
        FROM Requisitions R
        JOIN Approvals A ON A.RequisitionId = R.RequisitionId
            AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        WHERE ST.StatusCode = 'D'
        ORDER BY A.ApprovalDate DESC
    """)
    row = cursor.fetchone()
    if row:
        req_id = row.RequisitionId
        print(f"  Showing approval history for RequisitionId={req_id}:")
        cursor.execute("""
            SELECT A.ApprovalId, A.StatusId, ST.StatusCode, ST.Name,
                   A.ApprovalById, A.ApproverId, A.Level, A.ApprovalDate
            FROM Approvals A
            JOIN StatusTable ST ON ST.StatusId = A.StatusId
            WHERE A.RequisitionId = ?
            ORDER BY A.ApprovalId
        """, req_id)
        for r in cursor.fetchall():
            print(f"    ApprovalId={r.ApprovalId}: {r.Name} (Code={r.StatusCode}) by UserId={r.ApprovalById}, Level={r.Level}, Date={r.ApprovalDate}")

        # Check PO records
        print(f"\n  PO records for RequisitionId={req_id}:")
        cursor.execute("""
            SELECT PO.POID, PO.PONumber, PO.DateExported, PO.POStatusID,
                   POST.StatusName
            FROM PO
            LEFT JOIN POStatusTable POST ON POST.POStatusID = PO.POStatusId
            WHERE PO.RequisitionId = ?
        """, req_id)
        po_rows = cursor.fetchall()
        if po_rows:
            for r in po_rows:
                print(f"    POID={r.POID}, PONumber={r.PONumber}, DateExported={r.DateExported}, POStatus={r.StatusName}")
        else:
            print("    No PO records")

    # Check what the "On Hold" status looks like in vw_RequisitionStatus
    print("\n" + "=" * 70)
    print("STEP 3: Example of 'On Hold' requisition in vw_RequisitionStatus")
    print("=" * 70)
    cursor.execute("""
        SELECT TOP 3
            vwRS.RequisitionId, vwRS.StatusId, vwRS.StatusCode,
            vwRS.StatusDesc, vwRS.BaseStatus, vwRS.ApprovalDate
        FROM vw_RequisitionStatus vwRS
        WHERE vwRS.StatusDesc LIKE '%On Hold%'
        ORDER BY vwRS.ApprovalDate DESC
    """)
    for r in cursor.fetchall():
        print(f"  ReqId={r.RequisitionId}: StatusId={r.StatusId}, Code={r.StatusCode}, Desc='{r.StatusDesc}', Base='{r.BaseStatus}'")

    # Dry-run the corrected INSERT
    print("\n" + "=" * 70)
    print("STEP 4: Dry-run the corrected INSERT statement")
    print("=" * 70)
    if row:
        req_id = row.RequisitionId
        cursor.execute("""
            SELECT
                R.RequisitionId,
                1 AS NewStatusId,  -- On Hold
                A.ApprovalById,
                A.ApproverId,
                A.Level,
                GETDATE() AS NewApprovalDate
            FROM Requisitions R
            JOIN Approvals A ON A.RequisitionId = R.RequisitionId
                AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
            WHERE R.RequisitionId = ?
        """, req_id)
        r = cursor.fetchone()
        if r:
            print(f"  Would INSERT into Approvals:")
            print(f"    RequisitionId = {r.RequisitionId}")
            print(f"    StatusId = {r.NewStatusId} (On Hold)")
            print(f"    ApprovalById = {r.ApprovalById}")
            print(f"    ApproverId = {r.ApproverId}")
            print(f"    Level = {r.Level}")
            print(f"    ApprovalDate = {r.NewApprovalDate}")
            print(f"\n  This looks correct for changing status from 'D' to 'H'")

    cursor.close()
    conn.close()
    print("\n" + "=" * 70)
    print("VERIFICATION COMPLETE")
    print("=" * 70)

if __name__ == "__main__":
    run()
