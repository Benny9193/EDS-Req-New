import pyodbc

out = open(r'C:\EDS\bid_investigation.txt', 'w')

def p(s=''):
    print(s)
    out.write(s + '\n')
    out.flush()

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
        'DATABASE=EDS;'
        'UID=EDSAdmin;'
        'PWD=Consultant~!;'
        'timeout=30'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    p("Connected.\n")

    # 1. Bid header relationships: 13575, 13576, 13577
    p("=" * 80)
    p("1. BID HEADER DETAILS (13575, 13576, 13577)")
    p("=" * 80)
    cursor.execute("""
        SELECT BidHeaderId, BidNumber, BidName, BidYear,
               AwardedCatalogBidHeaderId, StatusId, DistrictId
        FROM BidHeader
        WHERE BidHeaderId IN (13575, 13576, 13577)
        ORDER BY BidHeaderId
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    # 2. All Detail rows for req 60076856 with bid info
    p("\n" + "=" * 80)
    p("2. ALL DETAIL ROWS FOR REQ 60076856 WITH BID INFO")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber, i.Description,
               d.BidHeaderId, d.BidPrice, d.Quantity, d.VendorId,
               v.Name AS VendorName,
               bh.BidName, bh.AwardedCatalogBidHeaderId
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        LEFT JOIN Vendors v ON v.VendorId = d.VendorId
        LEFT JOIN BidHeader bh ON bh.BidHeaderId = d.BidHeaderId
        WHERE d.RequisitionId = 60076856
        ORDER BY d.VendorId, d.BidHeaderId
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    # 3. Items on bid 13576 - check if they also exist in bid 13575 award data
    p("\n" + "=" * 80)
    p("3. DO THE 13576 ITEMS EXIST IN BID 13575 AWARD DATA?")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber,
               d.BidHeaderId AS CurrentBid,
               bd_13576.BidDetailId AS InBid13576,
               bd_13576.AwardPrice AS Price13576,
               bd_13576.VendorId AS Vendor13576,
               bd_13575.BidDetailId AS InBid13575,
               bd_13575.AwardPrice AS Price13575,
               bd_13575.VendorId AS Vendor13575
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        LEFT JOIN BidDetail bd_13576 ON bd_13576.ItemId = d.ItemId
            AND bd_13576.BidHeaderId = 13576
        LEFT JOIN BidDetail bd_13575 ON bd_13575.ItemId = d.ItemId
            AND bd_13575.BidHeaderId = 13575
        WHERE d.RequisitionId = 60076856
          AND d.BidHeaderId = 13576
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    # 4. Check BidData view (what the trigger uses) for these items
    p("\n" + "=" * 80)
    p("4. BidData VIEW FOR THESE ITEMS (what trigger uses to recalculate)")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber,
               bd.BidHeaderId, bd.AwardPrice, bd.VendorId AS BidVendorId,
               v.Name AS BidVendorName
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        CROSS APPLY (
            SELECT TOP 10 BidHeaderId, AwardPrice, VendorId, BidDetailId
            FROM BidData
            WHERE ItemId = d.ItemId
              AND BidHeaderId IN (13575, 13576, 13577)
        ) bd
        LEFT JOIN Vendors v ON v.VendorId = bd.VendorId
        WHERE d.RequisitionId = 60076856
          AND d.BidHeaderId = 13576
        ORDER BY d.ItemId, bd.BidHeaderId
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    # 5. What does BidData look like? Is it a view or table?
    p("\n" + "=" * 80)
    p("5. IS BidData A VIEW OR TABLE?")
    p("=" * 80)
    cursor.execute("""
        SELECT TABLE_NAME, TABLE_TYPE
        FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_NAME = 'BidData'
    """)
    rows = cursor.fetchall()
    for r in rows:
        p(f"  {r[0]} -> {r[1]}")

    cursor.execute("""
        SELECT name, type_desc
        FROM sys.objects
        WHERE name = 'BidData'
    """)
    rows = cursor.fetchall()
    for r in rows:
        p(f"  {r[0]} -> {r[1]}")

    # 6. Check trigger logic - what bid does the trigger pick?
    p("\n" + "=" * 80)
    p("6. TRIGGER trig_DetailUpdate - KEY SECTION (bid selection logic)")
    p("=" * 80)
    cursor.execute("""
        SELECT OBJECT_DEFINITION(OBJECT_ID('trig_DetailUpdate'))
    """)
    trigger_def = cursor.fetchone()[0]
    # Find the section that selects the bid
    lines = trigger_def.split('\n')
    for i, line in enumerate(lines):
        if any(kw in line.lower() for kw in ['bidheaderid', 'biddata', 'awardprice', 'biddetail']):
            start = max(0, i-2)
            end = min(len(lines), i+3)
            for j in range(start, end):
                p(f"  L{j}: {lines[j].rstrip()}")
            p("  ---")

    # 7. The item with BidHeaderId=NULL (the $2.72 one)
    p("\n" + "=" * 80)
    p("7. THE NULL-BID ITEM - WHAT BIDS DOES IT APPEAR IN?")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber, i.Description,
               d.BidHeaderId, d.BidPrice, d.VendorId
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        WHERE d.RequisitionId = 60076856 AND d.BidHeaderId IS NULL
          AND d.VendorId = 3842
    """)
    null_items = cursor.fetchall()
    for r in null_items:
        p(f"  DetailId={r[0]}, ItemId={r[1]}, ItemNumber={r[2]}")
        p(f"  Description={r[3]}")
        p(f"  BidHeaderId={r[4]}, BidPrice={r[5]}, VendorId={r[6]}")
        # Check what bids this item is in
        cursor.execute("""
            SELECT bd.BidHeaderId, bh.BidName, bd.AwardPrice, bd.VendorId,
                   v.Name AS VendorName
            FROM BidDetail bd
            JOIN BidHeader bh ON bh.BidHeaderId = bd.BidHeaderId
            LEFT JOIN Vendors v ON v.VendorId = bd.VendorId
            WHERE bd.ItemId = ?
            ORDER BY bd.BidHeaderId
        """, r[1])
        bid_rows = cursor.fetchall()
        if bid_rows:
            p(f"  Found in {len(bid_rows)} bid(s):")
            for br in bid_rows:
                p(f"    BidHeaderId={br[0]}, BidName={br[1]}, Price={br[2]}, VendorId={br[3]}, Vendor={br[4]}")
        else:
            p("  NOT FOUND in any BidDetail records!")

    # 8. District info for this requisition
    p("\n" + "=" * 80)
    p("8. DISTRICT INFO (MinimumPOAmount)")
    p("=" * 80)
    cursor.execute("""
        SELECT r.RequisitionId, r.DistrictId, d.Name AS DistrictName,
               d.MinimumPOAmount
        FROM Requisition r
        JOIN District d ON d.DistrictId = r.DistrictId
        WHERE r.RequisitionId = 60076856
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    conn.close()
    p("\nDone.")

except Exception as e:
    p(f"ERROR: {e}")
    import traceback
    p(traceback.format_exc())
finally:
    out.close()
