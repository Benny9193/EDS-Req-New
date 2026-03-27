#!/usr/bin/env python3
"""
Undo Downloaded Requisition - Revert status from "Downloaded" to "On Hold"

A reusable tool for changing requisition status from "Requisition Downloaded"
(StatusId=35, Code='D') back to "On Hold" (StatusId=1, Code='H').

The EDS requisition system determines current status by looking at the latest
(MAX ApprovalId) row in the Approvals table. This tool inserts a new row with
StatusId=1 to change the status back.

Usage:
    # Find downloaded reqs by district/budget name
    python undo_download.py find --district "Niskayuna"

    # Find downloaded reqs by budget ID
    python undo_download.py find --budget-id 1685509

    # Find downloaded reqs by specific req numbers in a budget
    python undo_download.py find --budget-id 1685509 --req-numbers 5,26,41,42

    # Preview what would be changed (dry run) using RequisitionIds
    python undo_download.py preview --req-ids 59928605,59944425,59966095

    # Apply the fix
    python undo_download.py apply --req-ids 59928605,59944425,59966095

    # Interactive mode - walks through find, preview, apply
    python undo_download.py interactive
"""
import argparse
import sys
import os
import pyodbc
from datetime import datetime

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass  # .env not required if env vars are already set


def get_connection():
    """Create database connection using environment variables."""
    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('DB_SERVER')};"
        f"DATABASE={os.getenv('DB_DATABASE_CATALOG')};"
        f"UID={os.getenv('DB_USERNAME')};"
        f"PWD={os.getenv('DB_PASSWORD')}"
    )
    return pyodbc.connect(conn_str, timeout=15)


def find_downloaded_reqs(cursor, budget_id=None, district_name=None, req_numbers=None):
    """Find downloaded requisitions matching criteria.

    Returns list of dicts with RequisitionId, RequisitionNumber, BudgetId,
    BudgetName, StatusDesc, ApprovalById, Level, ApprovalDate.
    """
    conditions = ["ST.StatusCode = 'D'"]
    params = []

    if budget_id:
        conditions.append("R.BudgetId = ?")
        params.append(budget_id)

    if district_name:
        conditions.append("""
            R.BudgetId IN (
                SELECT B.BudgetId FROM Budgets B
                WHERE B.DistrictId IN (
                    SELECT B2.DistrictId FROM Budgets B2
                    WHERE B2.Name LIKE ? OR B2.BudgetId IN (
                        SELECT BudgetId FROM Budgets WHERE Name LIKE ?
                    )
                )
                AND B.Active = 1
            )
        """)
        like_pattern = f"%{district_name}%"
        params.extend([like_pattern, like_pattern])
        # Also try via vw_RequisitionStatus display text
        # The district name might appear in the status description

    if req_numbers:
        placeholders = ",".join("?" * len(req_numbers))
        conditions.append(f"R.RequisitionNumber IN ({placeholders})")
        params.extend(req_numbers)

    where_clause = " AND ".join(conditions)

    cursor.execute(f"""
        SELECT
            R.RequisitionId,
            R.RequisitionNumber,
            R.BudgetId,
            B.Name AS BudgetName,
            ST.StatusCode,
            ST.Name AS StatusName,
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
        LEFT JOIN Budgets B ON B.BudgetId = R.BudgetId
        WHERE {where_clause}
        ORDER BY B.Name, R.RequisitionNumber
    """, params)

    results = []
    for r in cursor.fetchall():
        results.append({
            "RequisitionId": r.RequisitionId,
            "RequisitionNumber": r.RequisitionNumber,
            "BudgetId": r.BudgetId,
            "BudgetName": r.BudgetName,
            "StatusCode": r.StatusCode,
            "StatusName": r.StatusName,
            "StatusDesc": r.StatusDesc,
            "ApprovalById": r.ApprovalById,
            "ApproverId": r.ApproverId,
            "Level": r.Level,
            "ApprovalDate": r.ApprovalDate,
        })
    return results


def preview_reqs(cursor, req_ids):
    """Preview specific requisitions by RequisitionId. Returns list of dicts."""
    if not req_ids:
        return []

    placeholders = ",".join("?" * len(req_ids))
    cursor.execute(f"""
        SELECT
            R.RequisitionId,
            R.RequisitionNumber,
            R.BudgetId,
            B.Name AS BudgetName,
            ST.StatusId,
            ST.StatusCode,
            ST.Name AS StatusName,
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
        LEFT JOIN Budgets B ON B.BudgetId = R.BudgetId
        WHERE R.RequisitionId IN ({placeholders})
        ORDER BY R.RequisitionNumber
    """, req_ids)

    results = []
    for r in cursor.fetchall():
        results.append({
            "RequisitionId": r.RequisitionId,
            "RequisitionNumber": r.RequisitionNumber,
            "BudgetId": r.BudgetId,
            "BudgetName": r.BudgetName,
            "StatusId": r.StatusId,
            "StatusCode": r.StatusCode,
            "StatusName": r.StatusName,
            "StatusDesc": r.StatusDesc,
            "ApprovalById": r.ApprovalById,
            "ApproverId": r.ApproverId,
            "Level": r.Level,
            "ApprovalDate": r.ApprovalDate,
        })
    return results


def apply_fix(cursor, conn, req_ids):
    """Apply the fix: Insert On Hold approval rows for the given RequisitionIds.

    Returns (success_count, skipped_count, errors).
    Only changes reqs that are currently in Downloaded status.
    """
    if not req_ids:
        return 0, 0, ["No RequisitionIds provided"]

    placeholders = ",".join("?" * len(req_ids))

    # Safety check: confirm all are currently Downloaded
    cursor.execute(f"""
        SELECT
            R.RequisitionId,
            R.RequisitionNumber,
            ST.StatusCode,
            ST.Name AS StatusName
        FROM Requisitions R
        JOIN Approvals A ON A.RequisitionId = R.RequisitionId
            AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        WHERE R.RequisitionId IN ({placeholders})
    """, req_ids)

    not_downloaded = []
    for r in cursor.fetchall():
        if r.StatusCode != 'D':
            not_downloaded.append(
                f"Req#{r.RequisitionNumber} (ID={r.RequisitionId}) is '{r.StatusName}' ({r.StatusCode}), not Downloaded"
            )

    if not_downloaded:
        return 0, len(not_downloaded), not_downloaded

    # Execute the fix
    cursor.execute(f"""
        INSERT INTO Approvals (RequisitionId, StatusId, ApprovalById, ApproverId, Level, ApprovalDate)
        SELECT
            A.RequisitionId,
            1,              -- StatusId=1 = "On Hold" (Code='H')
            A.ApprovalById,
            A.ApproverId,
            A.Level,
            GETDATE()
        FROM Approvals A
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        WHERE A.RequisitionId IN ({placeholders})
          AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = A.RequisitionId)
          AND ST.StatusCode = 'D'
    """, req_ids)

    rows_affected = cursor.rowcount

    if rows_affected != len(req_ids):
        conn.rollback()
        return 0, 0, [f"Expected {len(req_ids)} inserts but got {rows_affected}. Transaction rolled back."]

    conn.commit()
    return rows_affected, 0, []


def verify_fix(cursor, req_ids):
    """Verify requisitions are now On Hold. Returns list of result dicts."""
    if not req_ids:
        return []

    placeholders = ",".join("?" * len(req_ids))
    cursor.execute(f"""
        SELECT
            R.RequisitionId,
            R.RequisitionNumber,
            ST.StatusId,
            ST.StatusCode,
            ST.Name AS StatusName,
            vwRS.StatusDesc,
            A.ApprovalDate
        FROM Requisitions R
        JOIN Approvals A ON A.RequisitionId = R.RequisitionId
            AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
        WHERE R.RequisitionId IN ({placeholders})
        ORDER BY R.RequisitionNumber
    """, req_ids)

    results = []
    for r in cursor.fetchall():
        results.append({
            "RequisitionId": r.RequisitionId,
            "RequisitionNumber": r.RequisitionNumber,
            "StatusId": r.StatusId,
            "StatusCode": r.StatusCode,
            "StatusName": r.StatusName,
            "StatusDesc": r.StatusDesc,
            "ApprovalDate": r.ApprovalDate,
            "IsOnHold": r.StatusCode == 'H',
        })
    return results


def print_reqs(reqs, show_budget=True):
    """Pretty-print a list of requisition dicts."""
    for r in reqs:
        budget_info = f" | Budget: {r.get('BudgetName', r.get('BudgetId', '?'))}" if show_budget else ""
        print(f"  Req#{r['RequisitionNumber']} (ID={r['RequisitionId']}){budget_info}")
        if 'StatusDesc' in r and r['StatusDesc']:
            print(f"    Status: {r['StatusDesc']}")
        elif 'StatusName' in r:
            print(f"    Status: {r['StatusName']} ({r.get('StatusCode', '?')})")
        if 'ApprovalDate' in r:
            print(f"    Date: {r['ApprovalDate']}")
        print()


# ============================================
# CLI Commands
# ============================================

def cmd_find(args):
    """Find downloaded requisitions."""
    conn = get_connection()
    cursor = conn.cursor()

    req_numbers = None
    if args.req_numbers:
        req_numbers = [int(n.strip()) for n in args.req_numbers.split(",")]

    reqs = find_downloaded_reqs(
        cursor,
        budget_id=args.budget_id,
        district_name=args.district,
        req_numbers=req_numbers,
    )

    if not reqs:
        print("No downloaded requisitions found matching criteria.")
    else:
        print(f"Found {len(reqs)} downloaded requisition(s):\n")
        print_reqs(reqs)
        print(f"\nRequisitionIds (for use with preview/apply):")
        ids_str = ",".join(str(r["RequisitionId"]) for r in reqs)
        print(f"  {ids_str}")

    cursor.close()
    conn.close()


def cmd_preview(args):
    """Preview requisitions that would be changed."""
    conn = get_connection()
    cursor = conn.cursor()

    req_ids = [int(n.strip()) for n in args.req_ids.split(",")]
    reqs = preview_reqs(cursor, req_ids)

    if not reqs:
        print("No requisitions found with the given IDs.")
    else:
        print(f"Preview of {len(reqs)} requisition(s) to change:\n")
        all_ok = True
        for r in reqs:
            status_ok = "DOWNLOADED - will be changed" if r["StatusCode"] == "D" else f"*** {r['StatusName']} - will be SKIPPED ***"
            if r["StatusCode"] != "D":
                all_ok = False
            print(f"  Req#{r['RequisitionNumber']} (ID={r['RequisitionId']}) | Budget: {r.get('BudgetName', r['BudgetId'])}")
            print(f"    Current: {r['StatusDesc']} [{status_ok}]")
            print(f"    Date: {r['ApprovalDate']}")
            print()

        if all_ok:
            print(f"All {len(reqs)} requisitions are Downloaded and ready to be changed to On Hold.")
            print(f"\nTo apply, run:")
            ids_str = ",".join(str(r["RequisitionId"]) for r in reqs)
            print(f"  python undo_download.py apply --req-ids {ids_str}")
        else:
            print("WARNING: Some requisitions are not in Downloaded status and will be skipped.")

    cursor.close()
    conn.close()


def cmd_apply(args):
    """Apply the fix."""
    conn = get_connection()
    cursor = conn.cursor()

    req_ids = [int(n.strip()) for n in args.req_ids.split(",")]

    # Preview first
    reqs = preview_reqs(cursor, req_ids)
    downloaded_reqs = [r for r in reqs if r["StatusCode"] == "D"]

    if not downloaded_reqs:
        print("No requisitions in Downloaded status found. Nothing to change.")
        cursor.close()
        conn.close()
        return

    print(f"About to change {len(downloaded_reqs)} requisition(s) from Downloaded to On Hold:\n")
    for r in downloaded_reqs:
        print(f"  Req#{r['RequisitionNumber']} (ID={r['RequisitionId']}) | {r['StatusDesc']}")
    print()

    if not args.yes:
        confirm = input("Proceed? (y/N): ").strip().lower()
        if confirm not in ("y", "yes"):
            print("Aborted.")
            cursor.close()
            conn.close()
            return

    downloaded_ids = [r["RequisitionId"] for r in downloaded_reqs]
    success, skipped, errors = apply_fix(cursor, conn, downloaded_ids)

    if errors:
        print(f"\nERRORS:")
        for e in errors:
            print(f"  {e}")
    else:
        print(f"\nSUCCESS: {success} requisition(s) changed to On Hold.")

        # Verify
        print(f"\nVerification:")
        results = verify_fix(cursor, downloaded_ids)
        all_ok = True
        for r in results:
            status = "OK" if r["IsOnHold"] else "*** FAILED ***"
            if not r["IsOnHold"]:
                all_ok = False
            print(f"  Req#{r['RequisitionNumber']} (ID={r['RequisitionId']}): {r['StatusDesc']} [{status}]")

        if all_ok:
            print(f"\nAll {len(results)} requisitions verified as On Hold.")
        else:
            print(f"\nWARNING: Some requisitions may not have changed. Check results above.")

    cursor.close()
    conn.close()


def cmd_interactive(args):
    """Interactive walkthrough: find → preview → apply."""
    conn = get_connection()
    cursor = conn.cursor()

    print("=" * 60)
    print("  Undo Downloaded Requisition - Interactive Mode")
    print("=" * 60)
    print()

    # Step 1: Find
    print("Step 1: Find downloaded requisitions")
    print("-" * 40)
    search_type = input("Search by (1) Budget ID, (2) District name, or (3) RequisitionId list? [1/2/3]: ").strip()

    reqs = []
    if search_type == "1":
        budget_id = input("Enter Budget ID: ").strip()
        req_nums_input = input("Filter by req numbers? (comma-separated, or Enter to skip): ").strip()
        req_numbers = [int(n.strip()) for n in req_nums_input.split(",")] if req_nums_input else None
        reqs = find_downloaded_reqs(cursor, budget_id=int(budget_id), req_numbers=req_numbers)
    elif search_type == "2":
        district = input("Enter district name (partial match): ").strip()
        req_nums_input = input("Filter by req numbers? (comma-separated, or Enter to skip): ").strip()
        req_numbers = [int(n.strip()) for n in req_nums_input.split(",")] if req_nums_input else None
        reqs = find_downloaded_reqs(cursor, district_name=district, req_numbers=req_numbers)
    elif search_type == "3":
        ids_input = input("Enter RequisitionId(s) (comma-separated): ").strip()
        req_ids = [int(n.strip()) for n in ids_input.split(",")]
        reqs = preview_reqs(cursor, req_ids)
        reqs = [r for r in reqs if r["StatusCode"] == "D"]
    else:
        print("Invalid choice.")
        cursor.close()
        conn.close()
        return

    if not reqs:
        print("\nNo downloaded requisitions found.")
        cursor.close()
        conn.close()
        return

    print(f"\nFound {len(reqs)} downloaded requisition(s):\n")
    print_reqs(reqs)

    # Step 2: Select which to fix
    print("Step 2: Select requisitions to fix")
    print("-" * 40)
    select = input("Fix all of them? (y/N, or enter comma-separated RequisitionIds to fix specific ones): ").strip()

    if select.lower() in ("y", "yes"):
        selected_ids = [r["RequisitionId"] for r in reqs]
    elif select.lower() in ("n", "no", ""):
        print("Aborted.")
        cursor.close()
        conn.close()
        return
    else:
        selected_ids = [int(n.strip()) for n in select.split(",")]

    # Step 3: Apply
    print(f"\nStep 3: Applying fix to {len(selected_ids)} requisition(s)...")
    print("-" * 40)

    confirm = input(f"Confirm changing {len(selected_ids)} req(s) from Downloaded to On Hold? (y/N): ").strip()
    if confirm.lower() not in ("y", "yes"):
        print("Aborted.")
        cursor.close()
        conn.close()
        return

    success, skipped, errors = apply_fix(cursor, conn, selected_ids)

    if errors:
        print(f"\nERRORS:")
        for e in errors:
            print(f"  {e}")
    else:
        print(f"\nSUCCESS: {success} requisition(s) changed to On Hold.\n")

        # Verify
        print("Step 4: Verification")
        print("-" * 40)
        results = verify_fix(cursor, selected_ids)
        for r in results:
            status = "OK" if r["IsOnHold"] else "*** FAILED ***"
            print(f"  Req#{r['RequisitionNumber']} (ID={r['RequisitionId']}): {r['StatusDesc']} [{status}]")
        print()

    cursor.close()
    conn.close()


def main():
    parser = argparse.ArgumentParser(
        description="Undo Downloaded Requisition - Revert to On Hold",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Find downloaded reqs in a budget
  python undo_download.py find --budget-id 1685509

  # Find by district name
  python undo_download.py find --district "Niskayuna"

  # Find specific req numbers in a budget
  python undo_download.py find --budget-id 1685509 --req-numbers 5,26,41,42

  # Preview what would be changed
  python undo_download.py preview --req-ids 59928605,59944425

  # Apply the fix (with confirmation prompt)
  python undo_download.py apply --req-ids 59928605,59944425

  # Apply without confirmation prompt
  python undo_download.py apply --req-ids 59928605,59944425 --yes

  # Interactive walkthrough
  python undo_download.py interactive
        """,
    )

    subparsers = parser.add_subparsers(dest="command", help="Command to run")

    # find
    find_parser = subparsers.add_parser("find", help="Find downloaded requisitions")
    find_parser.add_argument("--budget-id", type=int, help="Budget ID to search in")
    find_parser.add_argument("--district", type=str, help="District name (partial match)")
    find_parser.add_argument("--req-numbers", type=str, help="Comma-separated requisition numbers to filter")

    # preview
    preview_parser = subparsers.add_parser("preview", help="Preview requisitions to change")
    preview_parser.add_argument("--req-ids", required=True, type=str, help="Comma-separated RequisitionIds")

    # apply
    apply_parser = subparsers.add_parser("apply", help="Apply the fix")
    apply_parser.add_argument("--req-ids", required=True, type=str, help="Comma-separated RequisitionIds")
    apply_parser.add_argument("--yes", "-y", action="store_true", help="Skip confirmation prompt")

    # interactive
    subparsers.add_parser("interactive", help="Interactive walkthrough")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        "find": cmd_find,
        "preview": cmd_preview,
        "apply": cmd_apply,
        "interactive": cmd_interactive,
    }

    commands[args.command](args)


if __name__ == "__main__":
    main()
