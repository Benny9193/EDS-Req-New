import pyodbc

out = open(r'C:\EDS\bid_final.txt', 'w')

def p(s=''):
    print(s)
    out.write(s + '\n')
    out.flush()

try:
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=eds-sqlserver.eastus2.cloudapp.azure.com;'
        'DATABASE=EDS;UID=EDSAdmin;PWD=Consultant~!;timeout=30'
    )
    conn.autocommit = True
    cursor = conn.cursor()
    p("Connected.\n")

    # 1. All Detail rows for req 60076856
    p("=" * 80)
    p("1. ALL DETAIL ROWS FOR REQ 60076856")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemCode,
               LEFT(i.Description, 60) AS Descr,
               d.BidHeaderId, d.BidPrice, d.Quantity, d.VendorId,
               v.Name AS VendorName, d.AwardId, d.CatalogId
        FROM Detail d
        JOIN Items i ON i.ItemId = d.ItemId
        LEFT JOIN Vendors v ON v.VendorId = d.VendorId
        WHERE d.RequisitionId = 60076856
        ORDER BY v.Name, d.BidHeaderId
    """)
    rows = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in rows:
        p('\t'.join(str(x) for x in r))

    # 2. For items on bid 13576, cross-check with Prices table in all 3 bids
    p("\n" + "=" * 80)
    p("2. ITEMS ON BID 13576 - PRICES IN ALL 3 BIDS")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemCode,
               pr.BidHeaderId AS PriceBid, pr.BidPrice, pr.VendorId AS PriceVendor,
               pr.VendorName AS PriceVendorName, pr.AwardId
        FROM Detail d
        JOIN Items i ON i.ItemId = d.ItemId
        JOIN Prices pr ON pr.ItemId = d.ItemId
            AND pr.BidHeaderId IN (13575, 13576, 13577)
        WHERE d.RequisitionId = 60076856
          AND d.BidHeaderId = 13576
        ORDER BY d.ItemId, pr.BidHeaderId
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))
    else:
        p("  No Prices found in 13575-13577 for these items.")

    # 3. For items on bid 13576, cross-check BidItems + Bids (what trigger uses)
    p("\n" + "=" * 80)
    p("3. ITEMS ON BID 13576 - BidItems + Bids LOOKUP (trigger path)")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemCode,
               bi.BidItemId, bi.BidId, b.BidHeaderId AS BidsBidHeader,
               b.VendorId AS BidsVendor, v.Name AS BidsVendorName,
               bi.Price AS BidItemPrice
        FROM Detail d
        JOIN Items i ON i.ItemId = d.ItemId
        JOIN BidItems bi ON bi.ItemId = d.ItemId
        JOIN Bids b ON b.BidId = bi.BidId
            AND b.BidHeaderId IN (13575, 13576, 13577)
        LEFT JOIN Vendors v ON v.VendorId = b.VendorId
        WHERE d.RequisitionId = 60076856
          AND d.BidHeaderId = 13576
        ORDER BY d.ItemId, b.BidHeaderId
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))
    else:
        p("  No BidItems/Bids found for these items in 13575-13577.")

    # 4. The trigger's BidData temp table logic - check what the trigger reads
    p("\n" + "=" * 80)
    p("4. TRIGGER - KEY SECTIONS")
    p("=" * 80)
    cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('trig_DetailUpdate'))")
    trig = cursor.fetchone()[0]
    lines = trig.split('\n')

    # Print lines 140-200 (the BidData / pricing section)
    p("  --- Lines 130-250 (bid data / pricing logic) ---")
    for i in range(min(130, len(lines)), min(250, len(lines))):
        p(f"  L{i}: {lines[i].rstrip()}")

    # 5. Also check: does vw_RequisitionShippingCosts GROUP BY BidHeaderId?
    p("\n" + "=" * 80)
    p("5. vw_RequisitionShippingCosts - GROUP BY / FROM section")
    p("=" * 80)
    cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('vw_RequisitionShippingCosts'))")
    vdef = cursor.fetchone()[0]
    vlines = vdef.split('\n')
    for i, line in enumerate(vlines):
        l = line.strip().upper()
        if any(kw in l for kw in ['FROM ', 'JOIN ', 'GROUP BY', 'ON ', 'WHERE ', 'BIDDATA', 'BIDHEA']):
            p(f"  L{i}: {line.rstrip()}")

    # 6. NULL-BidHeaderId item: where is it priced?
    p("\n" + "=" * 80)
    p("6. NULL-BID ITEM (DetailId=1534395373) - PRICING LOOKUP")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemCode, d.BidHeaderId,
               d.BidPrice, d.VendorId, d.AwardId, d.CatalogId
        FROM Detail d
        JOIN Items i ON i.ItemId = d.ItemId
        WHERE d.DetailId = 1534395373
    """)
    row = cursor.fetchone()
    if row:
        item_id = row[1]
        p(f"  DetailId={row[0]}, ItemId={item_id}, ItemCode={row[2]}")
        p(f"  BidHeaderId={row[3]}, BidPrice={row[4]}, VendorId={row[5]}")
        p(f"  AwardId={row[6]}, CatalogId={row[7]}")

        # Prices for this item in ANY bid
        cursor.execute("""
            SELECT TOP 10 p.BidHeaderId,
                   p.BidPrice, p.VendorId, p.VendorName, p.AwardId
            FROM Prices p
            WHERE p.ItemId = ?
            ORDER BY p.BidHeaderId DESC
        """, item_id)
        pr = cursor.fetchall()
        p(f"\n  Prices (top 10 most recent bids):")
        for pp in pr:
            p(f"    BidHeaderId={pp[0]}, BidPrice={pp[1]}, VendorId={pp[2]}, Vendor={pp[3]}, AwardId={pp[4]}")

    conn.close()
    p("\nDone.")

except Exception as e:
    p(f"ERROR: {e}")
    import traceback
    p(traceback.format_exc())
finally:
    out.close()
