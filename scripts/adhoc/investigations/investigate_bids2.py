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

    # 1. BidHeaders for 13575, 13576, 13577
    p("=" * 80)
    p("1. BID HEADERS (13575, 13576, 13577)")
    p("=" * 80)
    cursor.execute("""
        SELECT BidHeaderId, BidNumber, BidName, BidYear,
               ParentBidHeaderId, StatusId
        FROM BidHeaders
        WHERE BidHeaderId IN (13575, 13576, 13577)
        ORDER BY BidHeaderId
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    # 2. vw_BidGrouper for these bids
    p("\n" + "=" * 80)
    p("2. vw_BidGrouper (bid parent-child relationships)")
    p("=" * 80)
    cursor.execute("""
        SELECT *
        FROM vw_BidGrouper
        WHERE MainBidHeaderId IN (13575, 13576, 13577)
           OR AltBidHeaderId IN (13575, 13576, 13577)
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    # 3. All Detail rows for req 60076856
    p("\n" + "=" * 80)
    p("3. ALL DETAIL ROWS FOR REQ 60076856")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber,
               LEFT(i.Description, 60) AS Descr,
               d.BidHeaderId, d.BidPrice, d.Quantity, d.VendorId,
               v.Name AS VendorName
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        LEFT JOIN Vendors v ON v.VendorId = d.VendorId
        WHERE d.RequisitionId = 60076856
        ORDER BY v.Name, d.BidHeaderId
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    # 4. For items on bid 13576, check if they also exist in bid 13575
    p("\n" + "=" * 80)
    p("4. ITEMS ON BID 13576 - DO THEY EXIST IN BID 13575?")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber,
               d.BidHeaderId AS CurrentBidHeader,
               d.BidPrice AS CurrentPrice,
               bd75.BidHeaderId AS Bid13575,
               bd75.AwardPrice AS Price13575,
               bd75.VendorId AS Vendor13575
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        LEFT JOIN BidHeaderDetail bd75 ON bd75.ItemId = d.ItemId
            AND bd75.BidHeaderId = 13575
        WHERE d.RequisitionId = 60076856
          AND d.BidHeaderId = 13576
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))
    else:
        p("  No items on bid 13576 in this req.")

    # 5. Check Awards table for these items
    p("\n" + "=" * 80)
    p("5. AWARDS TABLE - ITEMS ON BID 13576 IN THIS REQ")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber,
               a.BidHeaderId, a.ItemId AS AwardItemId, a.VendorId AS AwardVendor,
               v.Name AS AwardVendorName
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        LEFT JOIN Awards a ON a.ItemId = d.ItemId
            AND a.BidHeaderId IN (13575, 13576, 13577)
        LEFT JOIN Vendors v ON v.VendorId = a.VendorId
        WHERE d.RequisitionId = 60076856
          AND d.BidHeaderId = 13576
        ORDER BY d.ItemId, a.BidHeaderId
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))
    else:
        p("  No award records found.")

    # 6. What is BidData? Check if it's a view
    p("\n" + "=" * 80)
    p("6. BidData - WHAT IS IT?")
    p("=" * 80)
    cursor.execute("""
        SELECT name, type_desc
        FROM sys.objects
        WHERE name = 'BidData'
    """)
    rows = cursor.fetchall()
    for r in rows:
        p(f"  {r[0]} -> {r[1]}")
    if not rows:
        p("  'BidData' not found in sys.objects")
        # Maybe it's a synonym?
        cursor.execute("""
            SELECT name, base_object_name
            FROM sys.synonyms WHERE name = 'BidData'
        """)
        rows = cursor.fetchall()
        for r in rows:
            p(f"  SYNONYM: {r[0]} -> {r[1]}")
        if not rows:
            p("  Not a synonym either. Checking trigger text...")

    # 7. Trigger text - just the bid-selection portion
    p("\n" + "=" * 80)
    p("7. trig_DetailUpdate - FULL TEXT (first 4000 chars)")
    p("=" * 80)
    cursor.execute("""
        SELECT OBJECT_DEFINITION(OBJECT_ID('trig_DetailUpdate'))
    """)
    result = cursor.fetchone()
    if result and result[0]:
        text = result[0][:4000]
        for line in text.split('\n'):
            p(f"  {line.rstrip()}")
    else:
        p("  Trigger not found or no definition.")

    # 8. The NULL-BidHeader item ($2.72) - what bids is it in?
    p("\n" + "=" * 80)
    p("8. NULL-BID ITEM (DetailId=1534395373) - AWARD LOOKUP")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber, d.BidHeaderId,
               d.BidPrice, d.VendorId
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        WHERE d.DetailId = 1534395373
    """)
    row = cursor.fetchone()
    if row:
        p(f"  Detail: ItemId={row[1]}, ItemNumber={row[2]}, BidHeaderId={row[3]}, Price={row[4]}, VendorId={row[5]}")
        item_id = row[1]

        # Check BidHeaderDetail for this item
        p(f"\n  BidHeaderDetail entries for ItemId={item_id}:")
        cursor.execute("""
            SELECT bhd.BidHeaderId, bh.BidName, bhd.AwardPrice, bhd.VendorId,
                   v.Name AS VendorName
            FROM BidHeaderDetail bhd
            JOIN BidHeaders bh ON bh.BidHeaderId = bhd.BidHeaderId
            LEFT JOIN Vendors v ON v.VendorId = bhd.VendorId
            WHERE bhd.ItemId = ?
            ORDER BY bhd.BidHeaderId
        """, item_id)
        bd_rows = cursor.fetchall()
        if bd_rows:
            for br in bd_rows:
                p(f"    BidHeaderId={br[0]}, BidName={br[1]}, Price={br[2]}, VendorId={br[3]}, Vendor={br[4]}")
        else:
            p("    NOT in BidHeaderDetail!")

        # Check Awards for this item
        p(f"\n  Awards entries for ItemId={item_id}:")
        cursor.execute("""
            SELECT a.BidHeaderId, bh.BidName, a.VendorId, v.Name AS VendorName
            FROM Awards a
            JOIN BidHeaders bh ON bh.BidHeaderId = a.BidHeaderId
            LEFT JOIN Vendors v ON v.VendorId = a.VendorId
            WHERE a.ItemId = ?
            ORDER BY a.BidHeaderId
        """, item_id)
        aw_rows = cursor.fetchall()
        if aw_rows:
            for ar in aw_rows:
                p(f"    BidHeaderId={ar[0]}, BidName={ar[1]}, VendorId={ar[2]}, Vendor={ar[3]}")
        else:
            p("    NOT in Awards!")

    # 9. vw_RequisitionShippingCosts for this req (to see the BidHeaderId grouping)
    p("\n" + "=" * 80)
    p("9. vw_RequisitionShippingCosts FOR REQ 60076856")
    p("=" * 80)
    cursor.execute("""
        SELECT RequisitionId, VendorId, VendorName, BidHeaderId,
               Extended, ShippingCost, TotalShippingCost,
               POBelowMinimum, MinimumPOAmount
        FROM vw_RequisitionShippingCosts
        WHERE RequisitionId = 60076856
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))
    else:
        p("  No rows returned.")

    conn.close()
    p("\nDone.")

except Exception as e:
    p(f"ERROR: {e}")
    import traceback
    p(traceback.format_exc())
finally:
    out.close()
