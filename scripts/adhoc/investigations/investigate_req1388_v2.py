"""
Investigation v2: Burnt Hills-Ballston Lake Requisition #1388 (PO 261949)
Fix column name issues and search more broadly.
"""

import pyodbc
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv("C:/EDS/.env")

SERVER = os.getenv("DB_SERVER")
DATABASE = os.getenv("DB_DATABASE_CATALOG")
USERNAME = os.getenv("DB_USERNAME")
PASSWORD = os.getenv("DB_PASSWORD")

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};"
    f"DATABASE={DATABASE};"
    f"UID={USERNAME};"
    f"PWD={PASSWORD};"
    f"TrustServerCertificate=yes;"
)

def run_query(cursor, title, sql, params=None):
    print(f"\n{'='*100}")
    print(f"  {title}")
    print(f"{'='*100}")
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        columns = [col[0] for col in cursor.description] if cursor.description else []
        rows = cursor.fetchall()
        if not rows:
            print("  (no results)")
            return rows
        # Calculate column widths
        widths = [len(c) for c in columns]
        str_rows = []
        for row in rows:
            vals = []
            for idx, v in enumerate(row):
                if v is None:
                    s = "NULL"
                elif isinstance(v, datetime):
                    s = v.strftime("%Y-%m-%d %H:%M:%S")
                else:
                    s = str(v)
                vals.append(s)
                if len(s) > widths[idx]:
                    widths[idx] = min(len(s), 60)
            str_rows.append(vals)
        # Print
        header = " | ".join(c.ljust(widths[i]) for i, c in enumerate(columns))
        print(f"  {header}")
        print(f"  {'-+-'.join('-' * w for w in widths)}")
        for vals in str_rows:
            line = " | ".join(v[:60].ljust(widths[i]) for i, v in enumerate(vals))
            print(f"  {line}")
        print(f"  ({len(rows)} row(s))")
        return rows
    except Exception as e:
        print(f"  ERROR: {e}")
        return []


def main():
    print("Connecting to EDS database...")
    conn = pyodbc.connect(conn_str, timeout=30)
    cursor = conn.cursor()
    print("Connected.\n")

    # =========================================================================
    # 0. Check District table columns
    # =========================================================================
    run_query(cursor, "0a. District table columns",
        """
        SELECT COLUMN_NAME, DATA_TYPE
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'District'
        ORDER BY ORDINAL_POSITION
        """)

    # =========================================================================
    # 1. Find Burnt Hills district
    # =========================================================================
    run_query(cursor, "1. FIND DISTRICT: Burnt Hills",
        """
        SELECT TOP 10 *
        FROM District
        WHERE DistrictCode LIKE '%Burnt%'
           OR DistrictCode LIKE '%Ballston%'
           OR DistrictId IN (
               SELECT DistrictId FROM District
               WHERE DistrictCode LIKE '%BH%'
           )
        """)

    # Search by looking at entity/organization name fields
    run_query(cursor, "1b. Search for Burnt Hills in all text columns of District",
        """
        SELECT TOP 20 d.DistrictId, d.DistrictCode, d.Active
        FROM District d
        WHERE CAST(d.DistrictId AS varchar) + ' ' + ISNULL(d.DistrictCode, '') LIKE '%Burnt%'
        """)

    # Let's look at what columns District actually has and search using them
    cursor.execute("SELECT TOP 1 * FROM District")
    cols = [c[0] for c in cursor.description]
    print(f"\n  District columns: {cols}")

    # Search all varchar columns in District for 'Burnt'
    varchar_cols = []
    cursor.execute("""
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'District' AND DATA_TYPE IN ('varchar', 'nvarchar', 'char')
    """)
    varchar_cols = [r[0] for r in cursor.fetchall()]
    print(f"  District varchar columns: {varchar_cols}")

    if varchar_cols:
        where_clauses = " OR ".join([f"[{c}] LIKE '%Burnt%'" for c in varchar_cols])
        run_query(cursor, "1c. Search District for 'Burnt Hills' across all text columns",
            f"SELECT TOP 10 * FROM District WHERE {where_clauses}")

        where_clauses2 = " OR ".join([f"[{c}] LIKE '%Ballston%'" for c in varchar_cols])
        run_query(cursor, "1d. Search District for 'Ballston' across all text columns",
            f"SELECT TOP 10 * FROM District WHERE {where_clauses2}")

    # =========================================================================
    # 2. Maybe the district name is in a related table. Check Entity table.
    # =========================================================================
    cursor.execute("""
        SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES
        WHERE TABLE_NAME LIKE '%Entity%' OR TABLE_NAME LIKE '%Organization%'
        ORDER BY TABLE_NAME
    """)
    entity_tables = [r[0] for r in cursor.fetchall()]
    print(f"\n  Entity/Org tables: {entity_tables}")

    # Check if there's a Name field we haven't seen
    for tbl in entity_tables[:5]:
        cursor.execute(f"""
            SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_NAME = '{tbl}' AND DATA_TYPE IN ('varchar', 'nvarchar')
        """)
        text_cols = [r[0] for r in cursor.fetchall()]
        if text_cols:
            where_parts = " OR ".join([f"[{c}] LIKE '%Burnt%'" for c in text_cols])
            run_query(cursor, f"2. Search {tbl} for 'Burnt Hills'",
                f"SELECT TOP 5 * FROM [{tbl}] WHERE {where_parts}")

    # =========================================================================
    # 3. Search School table for Burnt Hills
    # =========================================================================
    run_query(cursor, "3. Search School for 'Burnt Hills'",
        """
        SELECT TOP 10 s.SchoolId, s.DistrictId, s.SchoolName, s.Active
        FROM School s
        WHERE s.SchoolName LIKE '%Burnt Hills%'
           OR s.SchoolName LIKE '%Ballston%'
        """)

    # =========================================================================
    # 4. Check Users table columns and find Lisa Johnson
    # =========================================================================
    cursor.execute("""
        SELECT COLUMN_NAME, DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'Users'
        ORDER BY ORDINAL_POSITION
    """)
    user_cols = [(r[0], r[1]) for r in cursor.fetchall()]
    print(f"\n  Users table columns: {[c[0] for c in user_cols]}")

    run_query(cursor, "4. Find Lisa Johnson in Users",
        """
        SELECT TOP 10 u.UserId, u.UserName, u.FirstName, u.LastName, u.Email, u.Active
        FROM Users u
        WHERE u.FirstName LIKE '%Lisa%' AND u.LastName LIKE '%Johnson%'
        ORDER BY u.Active DESC
        """)

    # =========================================================================
    # 5. Search for the specific item codes in the Items table
    # =========================================================================
    run_query(cursor, "5. Find items by code",
        """
        SELECT TOP 20 i.ItemId, i.ItemCode, i.Description, i.VendorId, i.Active
        FROM Items i
        WHERE i.ItemCode LIKE '%DBC%20508%'
           OR i.ItemCode LIKE '%DBCC20508%'
           OR i.ItemCode LIKE '%DBC21315%'
           OR i.ItemCode LIKE '%EDS00563%'
        """)

    # =========================================================================
    # 6. Search Detail table directly for items with these codes
    # =========================================================================
    run_query(cursor, "6. Detail lines with the suspect item codes (any req)",
        """
        SELECT TOP 30 d.DetailId, d.RequisitionId, d.ItemCode, d.Quantity,
               d.Description, d.BidPrice, d.VendorId, d.POId,
               d.Modified, d.ModifiedById, d.SessionId, d.LastAlteredSessionId,
               r.RequisitionNumber, r.UserId, r.BudgetId
        FROM Detail d
        JOIN Requisitions r ON d.RequisitionId = r.RequisitionId
        WHERE (d.ItemCode LIKE '%20508-5071%'
               OR d.ItemCode LIKE '%20508-8141%'
               OR d.ItemCode LIKE '%21315-2003%'
               OR d.ItemCode LIKE '%EDS00563%')
          AND r.RequisitionNumber = '1388'
        ORDER BY d.DetailId DESC
        """)

    # =========================================================================
    # 7. Search for requisition 1388 broadly
    # =========================================================================
    run_query(cursor, "7. ALL requisitions numbered 1388 (showing district info)",
        """
        SELECT TOP 20 r.RequisitionId, r.RequisitionNumber, r.UserId, r.SchoolId,
               r.BudgetId, r.DateEntered, r.StatusId,
               r.LastAlteredSessionId, r.DateUpdated, r.BidHeaderId,
               b.DistrictId,
               s.SchoolName
        FROM Requisitions r
        JOIN Budgets b ON r.BudgetId = b.BudgetId
        LEFT JOIN School s ON r.SchoolId = s.SchoolId
        WHERE r.RequisitionNumber = '1388'
          AND (s.SchoolName LIKE '%Burnt%' OR s.SchoolName LIKE '%Ballston%'
               OR b.DistrictId IN (SELECT DistrictId FROM School WHERE SchoolName LIKE '%Burnt%'))
        """)

    # =========================================================================
    # 8. Find PO 261949 with vendor info
    # =========================================================================
    cursor.execute("""
        SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'Vendors' AND DATA_TYPE IN ('varchar', 'nvarchar')
    """)
    vendor_text_cols = [r[0] for r in cursor.fetchall()]
    print(f"\n  Vendors text columns: {vendor_text_cols}")

    # Use a known name column
    name_col = 'Name' if 'Name' in vendor_text_cols else vendor_text_cols[0] if vendor_text_cols else None
    if name_col:
        run_query(cursor, "8. PO 261949 with vendor name",
            f"""
            SELECT po.POId, po.PONumber, po.VendorId, po.RequisitionId,
                   po.PODate, po.Amount, po.ItemCount,
                   v.[{name_col}] AS VendorName
            FROM PO po
            LEFT JOIN Vendors v ON po.VendorId = v.VendorId
            WHERE po.PONumber = '261949'
            """)

    # =========================================================================
    # 9. Maybe req 1388 uses a different number format or is a DistrictRequisitionNumber
    # =========================================================================
    run_query(cursor, "9. Detail lines with DistrictRequisitionNumber = 1388",
        """
        SELECT TOP 20 d.DetailId, d.RequisitionId, d.ItemCode, d.Quantity,
               d.DistrictRequisitionNumber, d.Description,
               r.RequisitionNumber, r.UserId
        FROM Detail d
        JOIN Requisitions r ON d.RequisitionId = r.RequisitionId
        WHERE d.DistrictRequisitionNumber = '1388'
          AND (d.ItemCode LIKE '%DBC%' OR d.ItemCode LIKE '%EDS00563%')
        """)

    # =========================================================================
    # 10. Search more broadly - find requisition that has these specific items
    # =========================================================================
    run_query(cursor, "10. Find ANY requisition with DBC20508-8141 item",
        """
        SELECT TOP 10 d.DetailId, d.RequisitionId, d.ItemCode, d.Quantity,
               d.Description, d.POId,
               r.RequisitionNumber, r.SchoolId, r.UserId, r.BudgetId, r.DateEntered,
               s.SchoolName
        FROM Detail d
        JOIN Requisitions r ON d.RequisitionId = r.RequisitionId
        LEFT JOIN School s ON r.SchoolId = s.SchoolId
        WHERE d.ItemCode LIKE '%DBC20508-8141%'
        ORDER BY d.DetailId DESC
        """)

    run_query(cursor, "10b. Find ANY requisition with DBCC20508-5071 (sky blue)",
        """
        SELECT TOP 10 d.DetailId, d.RequisitionId, d.ItemCode, d.Quantity,
               d.Description, d.POId,
               r.RequisitionNumber, r.SchoolId, r.UserId, r.BudgetId, r.DateEntered,
               s.SchoolName
        FROM Detail d
        JOIN Requisitions r ON d.RequisitionId = r.RequisitionId
        LEFT JOIN School s ON r.SchoolId = s.SchoolId
        WHERE d.ItemCode LIKE '%DBCC20508-5071%'
        ORDER BY d.DetailId DESC
        """)

    run_query(cursor, "10c. Find ANY requisition with EDS00563",
        """
        SELECT TOP 10 d.DetailId, d.RequisitionId, d.ItemCode, d.Quantity,
               d.Description, d.POId,
               r.RequisitionNumber, r.SchoolId, r.UserId, r.BudgetId, r.DateEntered,
               s.SchoolName
        FROM Detail d
        JOIN Requisitions r ON d.RequisitionId = r.RequisitionId
        LEFT JOIN School s ON r.SchoolId = s.SchoolId
        WHERE d.ItemCode LIKE '%EDS00563%'
        ORDER BY d.DetailId DESC
        """)

    run_query(cursor, "10d. Find ANY requisition with DBC21315-2003",
        """
        SELECT TOP 10 d.DetailId, d.RequisitionId, d.ItemCode, d.Quantity,
               d.Description, d.POId,
               r.RequisitionNumber, r.SchoolId, r.UserId, r.BudgetId, r.DateEntered,
               s.SchoolName
        FROM Detail d
        JOIN Requisitions r ON d.RequisitionId = r.RequisitionId
        LEFT JOIN School s ON r.SchoolId = s.SchoolId
        WHERE d.ItemCode LIKE '%DBC21315-2003%'
        ORDER BY d.DetailId DESC
        """)

    print("\n" + "="*100)
    print("  INVESTIGATION v2 COMPLETE")
    print("="*100)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
