import pyodbc

out = open(r'C:\EDS\bid_investigation2.txt', 'w')

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

    # 1. Get all items on bid 13576 in this req and check their Awards/Prices
    p("=" * 80)
    p("1. ITEMS ON BID 13576 IN REQ 60076856 + CROSS-CHECK ALL 3 BIDS")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemNumber,
               LEFT(i.Description, 50) AS Descr,
               d.BidHeaderId, d.BidPrice, d.VendorId, d.AwardId
        FROM Detail d
        JOIN Item i ON i.ItemId = d.ItemId
        WHERE d.RequisitionId = 60076856
          AND d.BidHeaderId = 13576
    """)
    items_on_13576 = cursor.fetchall()
    cols = [c[0] for c in cursor.description]
    p('\t'.join(cols))
    for r in items_on_13576:
        p('\t'.join(str(x) for x in r))

    p()
    for r in items_on_13576:
        item_id = r[1]
        item_num = r[2]
        p(f"  --- Item {item_num} (ItemId={item_id}) ---")
        # Check Awards table
        cursor.execute("""
            SELECT a.AwardId, a.BidHeaderId, bh.Description AS BidDesc,
                   a.VendorId, v.Name AS VendorName, a.Active,
                   bh.ParentBidHeaderId
            FROM Awards a
            JOIN BidHeaders bh ON bh.BidHeaderId = a.BidHeaderId
            LEFT JOIN Vendors v ON v.VendorId = a.VendorId
            WHERE a.BidId IN (
                SELECT bi.BidId FROM BidItems bi WHERE bi.ItemId = ?
            )
            AND a.BidHeaderId IN (13575, 13576, 13577)
            ORDER BY a.BidHeaderId
        """, item_id)
        aw = cursor.fetchall()
        if aw:
            p(f"    Awards: {len(aw)} record(s)")
            for ar in aw:
                p(f"      AwardId={ar[0]}, BidHeaderId={ar[1]}, Vendor={ar[4]}, Active={ar[5]}")
        else:
            # Try without BidItems join
            cursor.execute("""
                SELECT a.AwardId, a.BidHeaderId, a.VendorId, v.Name, a.Active
                FROM Awards a
                LEFT JOIN Vendors v ON v.VendorId = a.VendorId
                WHERE a.CatalogId IN (
                    SELECT CatalogId FROM Detail WHERE DetailId = ?
                )
                AND a.BidHeaderId IN (13575, 13576, 13577)
            """, r[0])
            aw2 = cursor.fetchall()
            if aw2:
                p(f"    Awards (via CatalogId): {len(aw2)} record(s)")
                for ar in aw2:
                    p(f"      AwardId={ar[0]}, BidHeaderId={ar[1]}, Vendor={ar[3]}, Active={ar[4]}")
            else:
                p("    No Awards found for this item in bids 13575-13577")

        # Check Prices table
        cursor.execute("""
            SELECT p.PriceId, p.BidHeaderId, p.ItemId, p.Price, p.VendorId,
                   v.Name AS VendorName
            FROM Prices p
            LEFT JOIN Vendors v ON v.VendorId = p.VendorId
            WHERE p.ItemId = ?
              AND p.BidHeaderId IN (13575, 13576, 13577)
            ORDER BY p.BidHeaderId
        """, item_id)
        pr = cursor.fetchall()
        if pr:
            p(f"    Prices: {len(pr)} record(s)")
            for pp in pr:
                p(f"      PriceId={pp[0]}, BidHeaderId={pp[1]}, Price={pp[3]}, Vendor={pp[5]}")
        else:
            p("    No Prices found in bids 13575-13577")

    # 2. Trigger definition (full)
    p("\n" + "=" * 80)
    p("2. trig_DetailUpdate - FULL DEFINITION")
    p("=" * 80)
    cursor.execute("""
        SELECT OBJECT_DEFINITION(OBJECT_ID('trig_DetailUpdate'))
    """)
    result = cursor.fetchone()
    if result and result[0]:
        for line in result[0].split('\n'):
            p(f"  {line.rstrip()}")

    # 3. Check vw_BidGrouper
    p("\n" + "=" * 80)
    p("3. vw_BidGrouper DEFINITION")
    p("=" * 80)
    cursor.execute("""
        SELECT OBJECT_DEFINITION(OBJECT_ID('vw_BidGrouper'))
    """)
    result = cursor.fetchone()
    if result and result[0]:
        for line in result[0].split('\n'):
            p(f"  {line.rstrip()}")

    # 4. What is BidData? Check all object types
    p("\n" + "=" * 80)
    p("4. SEARCHING FOR 'BidData' OBJECT")
    p("=" * 80)
    cursor.execute("""
        SELECT name, type_desc, schema_id
        FROM sys.objects
        WHERE name LIKE '%BidData%'
    """)
    for r in cursor.fetchall():
        p(f"  {r[0]} -> {r[1]}")

    # Also check synonyms
    cursor.execute("SELECT * FROM sys.synonyms WHERE name LIKE '%BidData%'")
    for r in cursor.fetchall():
        p(f"  SYNONYM: {r}")

    # 5. Check vw_RequisitionShippingCosts definition (references BidData?)
    p("\n" + "=" * 80)
    p("5. vw_RequisitionShippingCosts - CHECKING FOR BidData REFERENCE")
    p("=" * 80)
    cursor.execute("""
        SELECT OBJECT_DEFINITION(OBJECT_ID('vw_RequisitionShippingCosts'))
    """)
    result = cursor.fetchone()
    if result and result[0]:
        lines = result[0].split('\n')
        for i, line in enumerate(lines):
            if 'BidData' in line or 'biddata' in line.lower():
                start = max(0, i-3)
                end = min(len(lines), i+3)
                for j in range(start, end):
                    p(f"  L{j}: {lines[j].rstrip()}")
                p("  ---")
        # Also print the FROM/JOIN section
        p("\n  --- FROM/JOIN section ---")
        in_from = False
        for i, line in enumerate(lines):
            l = line.strip().upper()
            if 'FROM' in l or 'JOIN' in l or 'ON' in l or 'WHERE' in l or 'GROUP' in l:
                in_from = True
            if in_from:
                p(f"  L{i}: {line.rstrip()}")

    conn.close()
    p("\nDone.")

except Exception as e:
    p(f"ERROR: {e}")
    import traceback
    p(traceback.format_exc())
finally:
    out.close()
