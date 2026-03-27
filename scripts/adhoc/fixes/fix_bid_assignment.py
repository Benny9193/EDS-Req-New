import pyodbc

out = open(r'C:\EDS\fix_bid_assignment_output.txt', 'w')
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

    detail_ids = [1535015262, 1535015557, 1535015581]

    # === BEFORE STATE ===
    p("=" * 80)
    p("BEFORE: Detail rows for req 60076856")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemCode,
               LEFT(i.Description, 50) AS Descr,
               d.BidHeaderId, d.BidPrice, d.VendorId,
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

    p("\n" + "=" * 80)
    p("BEFORE: vw_RequisitionShippingCosts for req 60076856")
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

    # === APPLY FIX ===
    p("\n" + "=" * 80)
    p("APPLYING FIX: Disable trigger, update BidHeaderId, re-enable trigger")
    p("=" * 80)

    # Step 1: Disable trigger
    p("  Step 1: Disabling trig_DetailUpdate...")
    cursor.execute("DISABLE TRIGGER trig_DetailUpdate ON Detail")
    p("  Trigger disabled.")

    # Step 2: Update BidHeaderId to NULL for the 3 items
    # NULL means "use requisition's bid" (13575) per the view's logic:
    #   case isnull(Detail.BidHeaderId,0) when 0 then Requisitions.BidHeaderId
    p(f"  Step 2: Updating BidHeaderId to NULL for DetailIds {detail_ids}...")
    cursor.execute("""
        UPDATE Detail
        SET BidHeaderId = NULL
        WHERE DetailId IN (?, ?, ?)
          AND RequisitionId = 60076856
    """, detail_ids[0], detail_ids[1], detail_ids[2])
    p(f"  Updated {cursor.rowcount} rows.")

    # Step 3: Re-enable trigger
    p("  Step 3: Re-enabling trig_DetailUpdate...")
    cursor.execute("ENABLE TRIGGER trig_DetailUpdate ON Detail")
    p("  Trigger re-enabled.")

    # === AFTER STATE ===
    p("\n" + "=" * 80)
    p("AFTER: Detail rows for req 60076856")
    p("=" * 80)
    cursor.execute("""
        SELECT d.DetailId, d.ItemId, i.ItemCode,
               LEFT(i.Description, 50) AS Descr,
               d.BidHeaderId, d.BidPrice, d.VendorId,
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

    p("\n" + "=" * 80)
    p("AFTER: vw_RequisitionShippingCosts for req 60076856")
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

    p("\n" + "=" * 80)
    p("AFTER: vw_ReqTotalsByVendor for req 60076856")
    p("=" * 80)
    cursor.execute("""
        SELECT VendorCode, VendorName, ItemsTotal, VendorTotal,
               POBelowMinimum, MinimumPOAmount
        FROM vw_ReqTotalsByVendor
        WHERE RequisitionId = 60076856
    """)
    rows = cursor.fetchall()
    if rows:
        cols = [c[0] for c in cursor.description]
        p('\t'.join(cols))
        for r in rows:
            p('\t'.join(str(x) for x in r))

    conn.close()
    p("\nDone. Fix applied successfully.")

except Exception as e:
    p(f"ERROR: {e}")
    import traceback
    p(traceback.format_exc())
    # Try to re-enable trigger if it was disabled
    try:
        cursor.execute("ENABLE TRIGGER trig_DetailUpdate ON Detail")
        p("  (Trigger re-enabled after error)")
    except:
        p("  WARNING: Could not re-enable trigger! Manual intervention needed.")
finally:
    out.close()
