"""Extract trig_DetailUpdate code and top query #2 full text from SQL Server."""
import pyodbc
from dotenv import load_dotenv
import os
import sys

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

server = os.getenv('DB_SERVER')
database = os.getenv('DB_DATABASE_CATALOG', 'EDS')
username = os.getenv('DB_USERNAME')
password = os.getenv('DB_PASSWORD')

conn_str = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={server};"
    f"DATABASE={database};"
    f"UID={username};"
    f"PWD={password};"
    f"TrustServerCertificate=yes;"
)

conn = pyodbc.connect(conn_str, timeout=30)
cursor = conn.cursor()

# 1. Extract trig_DetailUpdate full definition
print("=" * 100)
print("  trig_DetailUpdate - FULL TRIGGER CODE")
print("=" * 100)

cursor.execute("""
    SELECT OBJECT_DEFINITION(OBJECT_ID('trig_DetailUpdate'))
""")
row = cursor.fetchone()
if row and row[0]:
    trigger_code = row[0]
    print(trigger_code)

    # Save to file
    os.makedirs('reports', exist_ok=True)
    with open('reports/trig_DetailUpdate_code.sql', 'w', encoding='utf-8') as f:
        f.write(trigger_code)
    print(f"\n[Saved to reports/trig_DetailUpdate_code.sql - {len(trigger_code)} chars, {trigger_code.count(chr(10))+1} lines]")
else:
    print("Trigger not found or no definition available")

# 2. Extract the full query text for query #2 (the ut.* District query)
print("\n" + "=" * 100)
print("  QUERY #2 ANALYSIS - Full Text and Execution Plan Details")
print("=" * 100)

cursor.execute("""
    SELECT TOP 5
        qs.total_elapsed_time / 1000 as total_elapsed_ms,
        qs.execution_count,
        qs.total_elapsed_time / NULLIF(qs.execution_count, 0) / 1000 as avg_elapsed_ms,
        qs.max_elapsed_time / 1000 as max_elapsed_ms,
        qs.total_logical_reads,
        qs.total_logical_writes,
        qs.total_physical_reads,
        qs.total_worker_time / 1000 as total_cpu_ms,
        qs.total_rows,
        qs.total_grant_kb,
        qs.max_grant_kb,
        qs.min_grant_kb,
        qs.total_used_grant_kb,
        qs.total_spills,
        SUBSTRING(st.text, (qs.statement_start_offset/2)+1,
            ((CASE qs.statement_end_offset
                WHEN -1 THEN DATALENGTH(st.text)
                ELSE qs.statement_end_offset
            END - qs.statement_start_offset)/2) + 1) as query_text,
        st.text as full_batch_text,
        qp.query_plan,
        DB_NAME(st.dbid) as database_name,
        OBJECT_NAME(st.objectid, st.dbid) as object_name
    FROM sys.dm_exec_query_stats qs
    CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
    CROSS APPLY sys.dm_exec_query_plan(qs.plan_handle) qp
    WHERE st.text LIKE '%select ut.%District.Name DistrictName%'
        AND st.text NOT LIKE '%dm_exec_query_stats%'
    ORDER BY qs.total_elapsed_time DESC
""")

rows = cursor.fetchall()
if rows:
    for i, row in enumerate(rows):
        cols = [desc[0] for desc in cursor.description]
        r = dict(zip(cols, row))
        print(f"\n--- Match {i+1} ---")
        print(f"  Total Elapsed: {r['total_elapsed_ms']:,} ms")
        print(f"  Executions: {r['execution_count']:,}")
        print(f"  Avg Elapsed: {r['avg_elapsed_ms']:,} ms")
        print(f"  Max Elapsed: {r['max_elapsed_ms']:,} ms")
        print(f"  Total Logical Reads: {r['total_logical_reads']:,}")
        print(f"  Total Physical Reads: {r['total_physical_reads']:,}")
        print(f"  Total Logical Writes: {r['total_logical_writes']:,}")
        print(f"  Total CPU: {r['total_cpu_ms']:,} ms")
        print(f"  Total Rows Returned: {r['total_rows']:,}")
        print(f"  Memory Grant (avg/max): {(r['total_grant_kb'] or 0) // max(r['execution_count'],1):,} KB / {r['max_grant_kb'] or 0:,} KB")
        print(f"  Total Spills: {r['total_spills'] or 0:,}")
        print(f"  Database: {r['database_name']}")
        print(f"  Object: {r['object_name']}")

        print(f"\n  FULL QUERY TEXT:")
        print("-" * 80)
        print(r['query_text'])
        print("-" * 80)

        # Save query plan
        if r['query_plan']:
            plan_file = f'reports/query2_plan_{i+1}.xml'
            with open(plan_file, 'w', encoding='utf-8') as f:
                f.write(r['query_plan'])
            print(f"  [Query plan saved to {plan_file}]")

        # Parse key plan info
        if r['query_plan']:
            plan = r['query_plan']
            # Look for table scans, index scans, missing indexes
            import re

            # Missing index hints in plan
            missing = re.findall(r'MissingIndex.*?Database="([^"]*)".*?Table="([^"]*)"', plan, re.DOTALL)
            if missing:
                print(f"\n  MISSING INDEX HINTS IN PLAN:")
                for db, tbl in missing:
                    print(f"    - {db}.{tbl}")

            # Table/Index scans
            scans = re.findall(r'<(TableScan|IndexScan).*?Table="([^"]*)".*?Index="([^"]*)"', plan, re.DOTALL)
            if scans:
                print(f"\n  TABLE/INDEX SCANS:")
                for scan_type, tbl, idx in scans:
                    print(f"    - {scan_type}: {tbl} ({idx})")

            # Estimated rows vs actual (if available)
            costly = re.findall(r'EstimatedTotalSubtreeCost="([^"]*)".*?PhysicalOp="([^"]*)".*?EstimateRows="([^"]*)"', plan, re.DOTALL)
            if costly:
                print(f"\n  TOP COST OPERATORS:")
                seen = set()
                for cost, op, rows in sorted(costly, key=lambda x: float(x[0]), reverse=True)[:10]:
                    key = f"{op}_{rows}"
                    if key not in seen:
                        seen.add(key)
                        print(f"    - {op}: Cost={float(cost):.1f}, EstRows={float(rows):,.0f}")
else:
    print("  Query not found in plan cache. Trying broader search...")
    cursor.execute("""
        SELECT TOP 3
            qs.total_elapsed_time / 1000 as total_elapsed_ms,
            qs.execution_count,
            SUBSTRING(st.text, (qs.statement_start_offset/2)+1,
                ((CASE qs.statement_end_offset
                    WHEN -1 THEN DATALENGTH(st.text)
                    ELSE qs.statement_end_offset
                END - qs.statement_start_offset)/2) + 1) as query_text,
            OBJECT_NAME(st.objectid, st.dbid) as object_name
        FROM sys.dm_exec_query_stats qs
        CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
        WHERE st.text LIKE '%select ut.%DistrictName%'
            AND st.text NOT LIKE '%dm_exec_query_stats%'
        ORDER BY qs.total_elapsed_time DESC
    """)
    rows2 = cursor.fetchall()
    if rows2:
        for row in rows2:
            print(f"  Elapsed: {row[0]:,} ms, Execs: {row[1]}, Object: {row[3]}")
            print(f"  Query: {row[2][:2000]}")
    else:
        print("  Query has been evicted from plan cache (server was restarted today)")

# 3. Also check if trig_DetailUpdate has recent execution stats
print("\n" + "=" * 100)
print("  trig_DetailUpdate - EXECUTION STATISTICS")
print("=" * 100)

cursor.execute("""
    SELECT
        OBJECT_NAME(object_id) as trigger_name,
        type_desc,
        is_disabled,
        create_date,
        modify_date
    FROM sys.triggers
    WHERE name = 'trig_DetailUpdate'
""")
trig_info = cursor.fetchone()
if trig_info:
    cols = [desc[0] for desc in cursor.description]
    t = dict(zip(cols, trig_info))
    print(f"  Name: {t['trigger_name']}")
    print(f"  Type: {t['type_desc']}")
    print(f"  Disabled: {t['is_disabled']}")
    print(f"  Created: {t['create_date']}")
    print(f"  Modified: {t['modify_date']}")

# Check parent table
cursor.execute("""
    SELECT OBJECT_NAME(parent_id) as parent_table
    FROM sys.triggers
    WHERE name = 'trig_DetailUpdate'
""")
parent = cursor.fetchone()
if parent:
    print(f"  Parent Table: {parent[0]}")

# Check trigger execution stats from dm_exec_trigger_stats
cursor.execute("""
    SELECT
        OBJECT_NAME(object_id) as trigger_name,
        execution_count,
        total_worker_time / 1000 as total_cpu_ms,
        total_elapsed_time / 1000 as total_elapsed_ms,
        total_logical_reads,
        total_logical_writes,
        total_physical_reads,
        max_elapsed_time / 1000 as max_elapsed_ms,
        last_execution_time
    FROM sys.dm_exec_trigger_stats
    WHERE OBJECT_NAME(object_id) = 'trig_DetailUpdate'
""")
tstats = cursor.fetchone()
if tstats:
    cols = [desc[0] for desc in cursor.description]
    ts = dict(zip(cols, tstats))
    print(f"\n  Execution Stats (since restart):")
    print(f"    Executions: {ts['execution_count']:,}")
    print(f"    Total CPU: {ts['total_cpu_ms']:,} ms")
    print(f"    Total Elapsed: {ts['total_elapsed_ms']:,} ms")
    print(f"    Avg Elapsed: {ts['total_elapsed_ms'] // max(ts['execution_count'],1):,} ms")
    print(f"    Max Elapsed: {ts['max_elapsed_ms']:,} ms")
    print(f"    Total Logical Reads: {ts['total_logical_reads']:,}")
    print(f"    Total Logical Writes: {ts['total_logical_writes']:,}")
    print(f"    Total Physical Reads: {ts['total_physical_reads']:,}")
    print(f"    Last Execution: {ts['last_execution_time']}")
else:
    print("  No execution stats available (trigger may not have fired since restart)")

# 4. Check Detail table size and index info
print("\n" + "=" * 100)
print("  Detail TABLE - SIZE AND INDEX INFO")
print("=" * 100)

cursor.execute("""
    SELECT
        t.name as table_name,
        p.rows as row_count,
        SUM(a.total_pages) * 8 / 1024 as total_size_mb,
        SUM(a.used_pages) * 8 / 1024 as used_size_mb
    FROM sys.tables t
    INNER JOIN sys.indexes i ON t.object_id = i.object_id
    INNER JOIN sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
    INNER JOIN sys.allocation_units a ON p.partition_id = a.container_id
    WHERE t.name = 'Detail'
    GROUP BY t.name, p.rows
""")
detail_info = cursor.fetchone()
if detail_info:
    print(f"  Rows: {detail_info[1]:,}")
    print(f"  Total Size: {detail_info[2]:,} MB")
    print(f"  Used Size: {detail_info[3]:,} MB")

cursor.execute("""
    SELECT
        i.name as index_name,
        i.type_desc,
        i.is_unique,
        us.user_seeks,
        us.user_scans,
        us.user_lookups,
        us.user_updates,
        us.last_user_seek,
        us.last_user_scan
    FROM sys.indexes i
    LEFT JOIN sys.dm_db_index_usage_stats us
        ON i.object_id = us.object_id AND i.index_id = us.index_id
        AND us.database_id = DB_ID()
    WHERE i.object_id = OBJECT_ID('Detail')
    ORDER BY i.index_id
""")
print(f"\n  Indexes:")
for idx in cursor.fetchall():
    cols = [desc[0] for desc in cursor.description]
    ix = dict(zip(cols, idx))
    print(f"    {ix['index_name'] or '(HEAP)'}: {ix['type_desc']}, Unique={ix['is_unique']}")
    print(f"      Seeks={ix['user_seeks'] or 0:,}, Scans={ix['user_scans'] or 0:,}, Lookups={ix['user_lookups'] or 0:,}, Updates={ix['user_updates'] or 0:,}")

cursor.close()
conn.close()
print("\nDone.")
