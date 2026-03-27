"""Live SQL Server schema analysis for EDS databases."""
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import pyodbc

load_dotenv(Path(__file__).parent / ".env")

SERVER = os.getenv("DB_SERVER", "localhost")
USERNAME = os.getenv("DB_USERNAME", "")
PASSWORD = os.getenv("DB_PASSWORD", "")
DATABASES = ["EDS", "dpa_EDSAdmin"]


def connect(database):
    return pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={SERVER};DATABASE={database};"
        f"UID={USERNAME};PWD={PASSWORD};"
        f"TrustServerCertificate=yes;Connection Timeout=30;"
    )


def query(conn, sql):
    cursor = conn.cursor()
    cursor.execute(sql)
    cols = [c[0] for c in cursor.description]
    return [dict(zip(cols, row)) for row in cursor.fetchall()]


def fmt_num(n):
    if n is None:
        return "N/A"
    return f"{n:,}"


def print_section(title):
    print(f"\n{'='*70}")
    print(f"  {title}")
    print(f"{'='*70}")


def analyze_server(conn):
    print_section("SERVER INFO")
    row = query(conn, "SELECT @@VERSION AS ver, @@SERVERNAME AS name, SERVERPROPERTY('Edition') AS edition, SERVERPROPERTY('Collation') AS collation")[0]
    ver_line = row['ver'].split('\n')[0]
    print(f"  Server:    {row['name']}")
    print(f"  Version:   {ver_line}")
    print(f"  Edition:   {row['edition']}")
    print(f"  Collation: {row['collation']}")

    print_section("ALL DATABASES ON SERVER")
    dbs = query(conn, """
        SELECT d.name, d.state_desc, d.recovery_model_desc,
               CAST(SUM(mf.size) * 8.0 / 1024 AS DECIMAL(10,1)) AS size_mb
        FROM sys.databases d
        JOIN sys.master_files mf ON d.database_id = mf.database_id
        GROUP BY d.name, d.state_desc, d.recovery_model_desc
        ORDER BY size_mb DESC
    """)
    print(f"  {'Database':<30} {'State':<12} {'Recovery':<12} {'Size MB':>10}")
    print(f"  {'-'*30} {'-'*12} {'-'*12} {'-'*10}")
    for db in dbs:
        print(f"  {db['name']:<30} {db['state_desc']:<12} {db['recovery_model_desc']:<12} {fmt_num(db['size_mb']):>10}")


def analyze_database(database):
    print_section(f"DATABASE: {database}")
    conn = connect(database)

    # Object counts
    counts = query(conn, """
        SELECT type_desc, COUNT(*) AS cnt
        FROM sys.objects
        WHERE is_ms_shipped = 0
        GROUP BY type_desc
        ORDER BY cnt DESC
    """)
    print(f"\n  Object Type Summary:")
    for c in counts:
        print(f"    {c['type_desc']:<40} {fmt_num(c['cnt']):>8}")

    # Total columns
    col_count = query(conn, """
        SELECT COUNT(*) AS cnt FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_SCHEMA NOT IN ('sys')
    """)[0]['cnt']
    print(f"\n  Total columns: {fmt_num(col_count)}")

    # Index summary
    idx = query(conn, """
        SELECT i.type_desc, COUNT(*) AS cnt
        FROM sys.indexes i
        JOIN sys.objects o ON i.object_id = o.object_id
        WHERE o.is_ms_shipped = 0 AND i.type > 0
        GROUP BY i.type_desc
        ORDER BY cnt DESC
    """)
    print(f"\n  Index Types:")
    for ix in idx:
        print(f"    {ix['type_desc']:<30} {fmt_num(ix['cnt']):>8}")

    # Schema distribution
    schemas = query(conn, """
        SELECT s.name AS schema_name, COUNT(*) AS cnt
        FROM sys.objects o
        JOIN sys.schemas s ON o.schema_id = s.schema_id
        WHERE o.is_ms_shipped = 0 AND o.type IN ('U','V','P','FN','IF','TF','TR')
        GROUP BY s.name
        ORDER BY cnt DESC
    """)
    print(f"\n  Schema Distribution:")
    for s in schemas:
        print(f"    {s['schema_name']:<30} {fmt_num(s['cnt']):>8} objects")

    # FK count
    fk = query(conn, "SELECT COUNT(*) AS cnt FROM sys.foreign_keys")[0]['cnt']
    print(f"\n  Foreign Keys: {fmt_num(fk)}")

    # Top 25 tables by row count
    print(f"\n  Top 25 Tables by Row Count:")
    tables = query(conn, """
        SELECT TOP 25
            s.name AS schema_name,
            t.name AS table_name,
            p.rows AS row_count,
            (SELECT COUNT(*) FROM INFORMATION_SCHEMA.COLUMNS c
             WHERE c.TABLE_NAME = t.name AND c.TABLE_SCHEMA = s.name) AS col_count,
            CAST(SUM(a.total_pages) * 8.0 / 1024 AS DECIMAL(10,1)) AS size_mb
        FROM sys.tables t
        JOIN sys.schemas s ON t.schema_id = s.schema_id
        JOIN sys.indexes i ON t.object_id = i.object_id
        JOIN sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
        JOIN sys.allocation_units a ON p.partition_id = a.container_id
        WHERE i.index_id <= 1
        GROUP BY s.name, t.name, p.rows
        ORDER BY p.rows DESC
    """)
    print(f"    {'Schema':<10} {'Table':<40} {'Rows':>15} {'Cols':>6} {'Size MB':>10}")
    print(f"    {'-'*10} {'-'*40} {'-'*15} {'-'*6} {'-'*10}")
    for t in tables:
        print(f"    {t['schema_name']:<10} {t['table_name']:<40} {fmt_num(t['row_count']):>15} {t['col_count']:>6} {fmt_num(t['size_mb']):>10}")

    # Recently modified objects (last 30 days)
    recent = query(conn, """
        SELECT TOP 20 name, type_desc, modify_date
        FROM sys.objects
        WHERE is_ms_shipped = 0
          AND modify_date >= DATEADD(DAY, -30, GETDATE())
        ORDER BY modify_date DESC
    """)
    if recent:
        print(f"\n  Recently Modified Objects (last 30 days):")
        print(f"    {'Name':<50} {'Type':<30} {'Modified'}")
        print(f"    {'-'*50} {'-'*30} {'-'*20}")
        for r in recent:
            print(f"    {r['name']:<50} {r['type_desc']:<30} {r['modify_date']}")
    else:
        print(f"\n  No objects modified in the last 30 days.")

    # Top stored procedures by parameter count
    procs = query(conn, """
        SELECT TOP 15 o.name, COUNT(p.parameter_id) AS param_count
        FROM sys.objects o
        LEFT JOIN sys.parameters p ON o.object_id = p.object_id
        WHERE o.type = 'P' AND o.is_ms_shipped = 0
        GROUP BY o.name
        ORDER BY param_count DESC
    """)
    print(f"\n  Top 15 Stored Procedures by Parameter Count:")
    for p in procs:
        print(f"    {p['name']:<50} {p['param_count']} params")

    conn.close()


def main():
    print("EDS SQL Server Schema Analysis")
    print(f"Server: {SERVER}")
    print(f"Date: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Server-level info using first database
    conn = connect(DATABASES[0])
    analyze_server(conn)
    conn.close()

    # Per-database analysis
    for db in DATABASES:
        try:
            analyze_database(db)
        except Exception as e:
            print(f"\n  ERROR analyzing {db}: {e}")

    print(f"\n{'='*70}")
    print("  Analysis complete.")
    print(f"{'='*70}")


if __name__ == "__main__":
    main()
