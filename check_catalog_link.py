import pyodbc

out = open(r'C:\EDS\catalog_link.txt', 'w')
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

    # 1. Where is CatalogId 2018104 linked via BidsCatalogList?
    p("=" * 80)
    p("1. BidsCatalogList FOR CatalogId=2018104 (United Sales catalog)")
    p("=" * 80)
    cursor.execute("""
        SELECT bcl.BidCatalogId, bcl.CatalogId, bcl.BidId, bcl.DiscountRate,
               b.BidHeaderId, b.VendorId, b.Active,
               v.Name AS VendorName
        FROM BidsCatalogList bcl
        JOIN Bids b ON b.BidId = bcl.BidId
        LEFT JOIN Vendors v ON v.VendorId = b.VendorId
        WHERE bcl.CatalogId = 2018104
        ORDER BY b.BidHeaderId
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))
    else:
        p("  No BidsCatalogList entries!")

    # 2. Check @BidsList - what bids does the requisition have?
    # The trigger builds @BidsList from the requisition's category bids
    # Let's check what the requisition's BidHeaderId is
    p("\n" + "=" * 80)
    p("2. REQUISITION 60076856 - BidHeaderId and Category")
    p("=" * 80)
    cursor.execute("""
        SELECT r.RequisitionId, r.BidHeaderId, r.CategoryId,
               c.CategoryId, c.Description AS CategoryDesc, c.Type
        FROM Requisitions r
        JOIN Category c ON c.CategoryId = r.CategoryId
        WHERE r.RequisitionId = 60076856
    """)
    row = cursor.fetchone()
    if row:
        p(f"  RequisitionId={row[0]}, BidHeaderId={row[1]}, CategoryId={row[2]}")
        p(f"  Category: {row[4]} (Type={row[5]})")

    # 3. What bids does @BidsList contain? (Replicate the trigger's BidsList logic)
    # Let's look at the trigger's early lines to see how @BidsList is built
    p("\n" + "=" * 80)
    p("3. TRIGGER - @BidsList POPULATION (first 130 lines)")
    p("=" * 80)
    cursor.execute("SELECT OBJECT_DEFINITION(OBJECT_ID('trig_DetailUpdate'))")
    trig = cursor.fetchone()[0]
    lines = trig.split('\n')
    for i in range(min(130, len(lines))):
        line = lines[i].rstrip()
        ll = line.lower()
        if any(kw in ll for kw in ['bidslist', '@bids', 'insert into @', 'declare @bids',
                                    'bidheaderid', 'requisition', 'category',
                                    'parentbid', 'vw_bidgrouper', 'bidgrouper']):
            p(f"  L{i}: {line}")

    # 4. The trigger's catalog pricing reassignment of BidHeaderId (Line 203)
    # BidHeaderId = case when BidHeaders.BidHeaderId != Requisitions.BidHeaderId
    #                    then BidHeaders.BidHeaderId else null end
    # So if catalog's bid (13576) != requisition's bid, it gets 13576
    # What IS the requisition's BidHeaderId?
    p("\n" + "=" * 80)
    p("4. CROSS-CHECK: Does Catalog 2018104 also exist under bid 13575?")
    p("=" * 80)
    cursor.execute("""
        SELECT bcl.BidCatalogId, bcl.CatalogId, bcl.BidId,
               b.BidHeaderId, b.VendorId, b.Active,
               v.Name AS VendorName
        FROM BidsCatalogList bcl
        JOIN Bids b ON b.BidId = bcl.BidId
        LEFT JOIN Vendors v ON v.VendorId = b.VendorId
        WHERE bcl.CatalogId = 2018104
          AND b.BidHeaderId = 13575
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))
    else:
        p("  Catalog 2018104 is NOT linked to bid 13575 via BidsCatalogList!")

    # 5. What about the Staples catalog 2018382?
    p("\n" + "=" * 80)
    p("5. BidsCatalogList FOR CatalogId=2018382 (Staples catalog)")
    p("=" * 80)
    cursor.execute("""
        SELECT bcl.BidCatalogId, bcl.CatalogId, bcl.BidId,
               b.BidHeaderId, b.VendorId, b.Active,
               v.Name AS VendorName
        FROM BidsCatalogList bcl
        JOIN Bids b ON b.BidId = bcl.BidId
        LEFT JOIN Vendors v ON v.VendorId = b.VendorId
        WHERE bcl.CatalogId = 2018382
        ORDER BY b.BidHeaderId
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))
    else:
        p("  No BidsCatalogList entries for Staples catalog!")

    # 6. Award 2417219 - what bid is it linked to?
    p("\n" + "=" * 80)
    p("6. AWARD 2417219 (United Sales catalog items)")
    p("=" * 80)
    cursor.execute("""
        SELECT a.AwardId, a.BidId, a.VendorId, a.BidHeaderId,
               v.Name AS VendorName
        FROM Awards a
        LEFT JOIN Vendors v ON v.VendorId = a.VendorId
        WHERE a.AwardId = 2417219
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))

    # 7. Also check Award 2418934 (the $2.72 item's award)
    p("\n" + "=" * 80)
    p("7. AWARD 2418934 ($2.72 item)")
    p("=" * 80)
    cursor.execute("""
        SELECT a.AwardId, a.BidId, a.VendorId, a.BidHeaderId,
               v.Name AS VendorName
        FROM Awards a
        LEFT JOIN Vendors v ON v.VendorId = a.VendorId
        WHERE a.AwardId = 2418934
    """)
    rows = cursor.fetchall()
    if rows:
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
