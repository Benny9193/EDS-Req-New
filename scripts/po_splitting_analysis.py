"""
PO Splitting Impact Analysis & Prototype for East Brunswick
============================================================
Request: Limit PO line items to 25 per PO (from Lori Tagerty, East Brunswick)

Current state: MaxPODetailItems = 999999999 (no limit) in AccountingFormats
The sp_CreatePO stored procedure has a hardcoded check for MaxPODetailItems = 99
but does NOT support arbitrary limits. This script:

1. Models the impact of a 25-item cap on East Brunswick POs
2. Provides the SQL changes needed to implement configurable PO splitting
3. Shows the before/after comparison

Budget year: Dec 1, 2024 – Nov 30, 2025 (most recent completed)
"""

import pyodbc
import math
from collections import defaultdict
from datetime import datetime

CONN_STR = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;"
    "DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;"
    "TrustServerCertificate=yes;Connection Timeout=30;"
)

DISTRICT_ID = 28  # East Brunswick
BUDGET_START = "2024-12-01"
BUDGET_END = "2025-12-01"
MAX_ITEMS_PER_PO = 25


def run_analysis():
    conn = pyodbc.connect(CONN_STR)
    cursor = conn.cursor()

    print("=" * 80)
    print("  PO SPLITTING IMPACT ANALYSIS -- East Brunswick Public Schools")
    print(f"  Budget Year: Dec 2024 – Nov 2025 | Proposed Cap: {MAX_ITEMS_PER_PO} items/PO")
    print("=" * 80)

    # -- Summary Stats --
    cursor.execute("""
        SELECT
            COUNT(*) AS TotalPOs,
            SUM(ItemCount) AS TotalItems,
            SUM(Amount) AS TotalAmount,
            SUM(CASE WHEN ItemCount > ? THEN 1 ELSE 0 END) AS POsOverLimit,
            SUM(CASE WHEN ItemCount <= ? THEN 1 ELSE 0 END) AS POsUnderLimit
        FROM POHeader
        WHERE DistrictId = ?
          AND PODate >= ? AND PODate < ?
    """, MAX_ITEMS_PER_PO, MAX_ITEMS_PER_PO, DISTRICT_ID, BUDGET_START, BUDGET_END)
    row = cursor.fetchone()
    total_pos, total_items, total_amount = row.TotalPOs, row.TotalItems, float(row.TotalAmount or 0)
    over, under = row.POsOverLimit, row.POsUnderLimit

    print(f"\n  CURRENT STATE")
    print(f"  Total POs:           {total_pos:,}")
    print(f"  Total line items:    {total_items:,}")
    print(f"  Total amount:        ${total_amount:,.2f}")
    print(f"  POs <= {MAX_ITEMS_PER_PO} items:     {under:,} ({under/total_pos*100:.1f}%)")
    print(f"  POs >  {MAX_ITEMS_PER_PO} items:     {over:,} ({over/total_pos*100:.1f}%)")

    # -- Detailed PO-level analysis --
    cursor.execute("""
        SELECT POId, PONumber, ItemCount, Amount, VendorId, VendorName,
               SchoolId, SchoolName, PODate
        FROM POHeader
        WHERE DistrictId = ?
          AND PODate >= ? AND PODate < ?
          AND ItemCount > ?
        ORDER BY VendorName, SchoolName, ItemCount DESC
    """, DISTRICT_ID, BUDGET_START, BUDGET_END, MAX_ITEMS_PER_PO)
    affected_pos = cursor.fetchall()

    # Calculate extra POs needed
    total_extra = 0
    vendor_impact = defaultdict(lambda: {"pos": 0, "extra": 0, "items": [], "amount": 0})
    school_impact = defaultdict(lambda: {"pos": 0, "extra": 0, "items": [], "amount": 0})
    school_vendor = defaultdict(lambda: defaultdict(lambda: {"pos": 0, "extra": 0, "items": []}))

    for po in affected_pos:
        extra = math.ceil(po.ItemCount / MAX_ITEMS_PER_PO) - 1
        total_extra += extra
        amt = float(po.Amount or 0)

        vi = vendor_impact[po.VendorName]
        vi["pos"] += 1
        vi["extra"] += extra
        vi["items"].append(po.ItemCount)
        vi["amount"] += amt

        si = school_impact[po.SchoolName or "Unknown"]
        si["pos"] += 1
        si["extra"] += extra
        si["items"].append(po.ItemCount)
        si["amount"] += amt

        sv = school_vendor[po.SchoolName or "Unknown"][po.VendorName]
        sv["pos"] += 1
        sv["extra"] += extra
        sv["items"].append(po.ItemCount)

    new_total = total_pos + total_extra
    print(f"\n  AFTER {MAX_ITEMS_PER_PO}-ITEM CAP")
    print(f"  POs that would split: {len(affected_pos):,}")
    print(f"  Extra POs created:    +{total_extra:,}")
    print(f"  New total POs:        {new_total:,} (was {total_pos:,}, +{total_extra/total_pos*100:.1f}%)")
    print(f"  Dollar amounts:       UNCHANGED (same items, just split across more POs)")

    # -- Vendor Breakdown --
    print(f"\n{'-' * 80}")
    print(f"  IMPACT BY VENDOR")
    print(f"{'-' * 80}")
    print(f"  {'Vendor':<42} {'POs':>5} {'Extra':>6} {'Avg':>5} {'Max':>5} {'Amount':>14}")
    print(f"  {'-'*42} {'-'*5} {'-'*6} {'-'*5} {'-'*5} {'-'*14}")
    for vname in sorted(vendor_impact, key=lambda v: vendor_impact[v]["extra"], reverse=True):
        vi = vendor_impact[vname]
        avg_items = sum(vi["items"]) / len(vi["items"])
        max_items = max(vi["items"])
        print(f"  {vname[:41]:<42} {vi['pos']:>5} {'+' + str(vi['extra']):>6} {avg_items:>5.0f} {max_items:>5} ${vi['amount']:>12,.2f}")
    print(f"  {'-'*42} {'-'*5} {'-'*6} {'-'*5} {'-'*5} {'-'*14}")
    print(f"  {'TOTAL':<42} {len(affected_pos):>5} {'+' + str(total_extra):>6}")

    # -- School Breakdown --
    print(f"\n{'-' * 80}")
    print(f"  IMPACT BY SCHOOL")
    print(f"{'-' * 80}")
    print(f"  {'School':<42} {'POs':>5} {'Extra':>6} {'Avg':>5} {'Max':>5}")
    print(f"  {'-'*42} {'-'*5} {'-'*6} {'-'*5} {'-'*5}")
    for sname in sorted(school_impact, key=lambda s: school_impact[s]["extra"], reverse=True):
        si = school_impact[sname]
        avg_items = sum(si["items"]) / len(si["items"])
        max_items = max(si["items"])
        print(f"  {sname[:41]:<42} {si['pos']:>5} {'+' + str(si['extra']):>6} {avg_items:>5.0f} {max_items:>5}")

    # -- School x Vendor Detail --
    print(f"\n{'-' * 80}")
    print(f"  DETAILED SCHOOL x VENDOR BREAKDOWN")
    print(f"{'-' * 80}")
    for sname in sorted(school_vendor, key=lambda s: sum(
        d["extra"] for d in school_vendor[s].values()
    ), reverse=True):
        vendors = school_vendor[sname]
        total_school_extra = sum(d["extra"] for d in vendors.values())
        total_school_pos = sum(d["pos"] for d in vendors.values())
        print(f"\n  {sname} ({total_school_pos} affected POs -> +{total_school_extra} extra)")
        for vname in sorted(vendors, key=lambda v: vendors[v]["extra"], reverse=True):
            d = vendors[vname]
            items = d["items"]
            avg = sum(items) / len(items)
            # Show how each PO would split
            splits = [f"{ic}->{math.ceil(ic/MAX_ITEMS_PER_PO)}" for ic in sorted(items, reverse=True)[:5]]
            more = f" +{len(items)-5} more" if len(items) > 5 else ""
            print(f"    {vname[:38]:<40} {d['pos']:>2} POs, +{d['extra']:>2} extra  [{', '.join(splits)}{more}]")

    # -- Sample PO Split Visualization --
    print(f"\n{'-' * 80}")
    print(f"  SAMPLE: How a 71-item PO would split into {math.ceil(71/MAX_ITEMS_PER_PO)} POs")
    print(f"{'-' * 80}")
    biggest = max(affected_pos, key=lambda p: p.ItemCount)
    n_splits = math.ceil(biggest.ItemCount / MAX_ITEMS_PER_PO)
    print(f"  Original: PO #{biggest.PONumber} -- {biggest.VendorName}")
    print(f"            {biggest.ItemCount} items, ${float(biggest.Amount or 0):,.2f}")
    print(f"  After split:")
    remaining = biggest.ItemCount
    for i in range(n_splits):
        chunk = min(MAX_ITEMS_PER_PO, remaining)
        est_amount = float(biggest.Amount or 0) * chunk / biggest.ItemCount
        suffix = "A" if i == 0 else chr(65 + i)
        print(f"    PO #{biggest.PONumber}-{suffix}: {chunk:>3} items, ~${est_amount:,.2f}")
        remaining -= chunk

    conn.close()

    # -- Implementation Guide --
    print(f"\n{'=' * 80}")
    print(f"  IMPLEMENTATION GUIDE")
    print(f"{'=' * 80}")
    print("""
  OPTION A: Configuration-only change (RECOMMENDED)
  --------------------------------------------------
  The AccountingFormats table already has a MaxPODetailItems column.
  East Brunswick (DistrictId=28) uses AccountingFormatId=33.

  However, sp_CreatePO currently only checks for the hardcoded value 99:
    if @MaxPODetailItems = 99  -->  SELECT TOP 99 ...

  To support arbitrary limits like 25, the SP needs a one-line fix.

  STEP 1: Update the stored procedure (see po_split_sp_patch.sql)
  STEP 2: Set MaxPODetailItems = 25 for East Brunswick's accounting format

  SQL to configure (after SP is patched):
    UPDATE AccountingFormats
       SET MaxPODetailItems = 25
     WHERE AccountingFormatId = 33;  -- East Brunswick format

  NOTE: AccountingFormatId 33 is specific to East Brunswick
        ("East Brunswick (Eddata PO Format)"), so this change
        only affects them.

  OPTION B: District-level override
  ----------------------------------
  If multiple districts share the same AccountingFormat and you
  need per-district control, add a MaxPODetailItems column to the
  District table itself, with fallback to AccountingFormats.
  This is more work but more flexible.
""")


if __name__ == "__main__":
    run_analysis()
