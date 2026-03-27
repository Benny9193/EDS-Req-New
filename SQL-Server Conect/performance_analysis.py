"""
Comprehensive SQL Server Performance Analysis for EDS Database
==============================================================
Covers: Server health, wait stats, CPU, memory, IO, query performance,
index analysis, blocking, deadlocks, storage, table stats, procedure/trigger
analysis, TempDB, and EDS-specific known issue checks.
"""
import pyodbc
import os
import sys
import json
import datetime
from dotenv import load_dotenv
from collections import defaultdict

# Fix Windows console encoding
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

SERVER = os.getenv('DB_SERVER')
DATABASE = os.getenv('DB_DATABASE_CATALOG', 'EDS')
USERNAME = os.getenv('DB_USERNAME')
PASSWORD = os.getenv('DB_PASSWORD')

CONN_STR = (
    f"DRIVER={{ODBC Driver 17 for SQL Server}};"
    f"SERVER={SERVER};DATABASE={DATABASE};"
    f"UID={USERNAME};PWD={PASSWORD};"
    f"TrustServerCertificate=yes;"
)

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), 'reports')
os.makedirs(OUTPUT_DIR, exist_ok=True)


def get_connection():
    return pyodbc.connect(CONN_STR, timeout=30)


def run_query(conn, sql, params=None):
    """Execute query and return list of dicts."""
    cursor = conn.cursor()
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        if cursor.description:
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]
        return []
    except pyodbc.Error as e:
        return [{"ERROR": str(e)}]
    finally:
        cursor.close()


def fmt_num(n):
    """Format number with commas."""
    if n is None:
        return "N/A"
    if isinstance(n, float):
        return f"{n:,.2f}"
    return f"{n:,}"


def fmt_mb(bytes_val):
    """Format bytes as MB."""
    if bytes_val is None:
        return "N/A"
    return f"{bytes_val / 1024 / 1024:,.1f} MB"


def fmt_pct(val):
    if val is None:
        return "N/A"
    return f"{val:.1f}%"


def section_header(title):
    line = "=" * 80
    return f"\n{line}\n  {title}\n{line}\n"


def sub_header(title):
    return f"\n--- {title} {'─' * max(1, 70 - len(title))}\n"


# ============================================================================
# SECTION 1: SERVER CONFIGURATION & HEALTH
# ============================================================================
def analyze_server_config(conn):
    report = section_header("1. SERVER CONFIGURATION & HEALTH")

    # Server properties
    props = run_query(conn, """
        SELECT
            SERVERPROPERTY('MachineName') AS MachineName,
            SERVERPROPERTY('ServerName') AS ServerName,
            SERVERPROPERTY('Edition') AS Edition,
            SERVERPROPERTY('ProductVersion') AS ProductVersion,
            SERVERPROPERTY('ProductLevel') AS ProductLevel,
            SERVERPROPERTY('Collation') AS Collation,
            SERVERPROPERTY('IsClustered') AS IsClustered,
            SERVERPROPERTY('IsHadrEnabled') AS IsHadrEnabled,
            @@VERSION AS FullVersion
    """)
    if props:
        p = props[0]
        report += sub_header("Server Properties")
        report += f"  Machine:        {p.get('MachineName')}\n"
        report += f"  Instance:       {p.get('ServerName')}\n"
        report += f"  Edition:        {p.get('Edition')}\n"
        report += f"  Version:        {p.get('ProductVersion')} ({p.get('ProductLevel')})\n"
        report += f"  Collation:      {p.get('Collation')}\n"
        report += f"  Clustered:      {p.get('IsClustered')}\n"
        report += f"  Always On:      {p.get('IsHadrEnabled')}\n"

    # Key configuration settings
    config = run_query(conn, """
        SELECT name, value_in_use, description
        FROM sys.configurations
        WHERE name IN (
            'max degree of parallelism', 'cost threshold for parallelism',
            'max server memory (MB)', 'min server memory (MB)',
            'optimize for ad hoc workloads', 'max worker threads',
            'backup compression default', 'remote query timeout (s)',
            'clr enabled', 'xp_cmdshell', 'show advanced options',
            'fill factor (%)', 'blocked process threshold (s)'
        )
        ORDER BY name
    """)
    report += sub_header("Key Configuration Settings")
    for c in config:
        cname = c.get('name', c.get('Name', ''))
        cval = c.get('value_in_use', c.get('Value', c.get('value', '')))
        report += f"  {str(cname):45s} = {cval}\n"

    # CPU info
    cpu = run_query(conn, """
        SELECT cpu_count, hyperthread_ratio,
               physical_memory_kb / 1024 AS physical_memory_mb,
               committed_kb / 1024 AS committed_mb,
               committed_target_kb / 1024 AS target_mb,
               sqlserver_start_time,
               DATEDIFF(day, sqlserver_start_time, GETDATE()) AS uptime_days
        FROM sys.dm_os_sys_info
    """)
    if cpu:
        c = cpu[0]
        report += sub_header("Hardware & Uptime")
        report += f"  CPU Count:         {c.get('cpu_count')} (HT ratio: {c.get('hyperthread_ratio')})\n"
        report += f"  Physical Memory:   {fmt_num(c.get('physical_memory_mb'))} MB\n"
        report += f"  Committed Memory:  {fmt_num(c.get('committed_mb'))} MB\n"
        report += f"  Target Memory:     {fmt_num(c.get('target_mb'))} MB\n"
        report += f"  SQL Start Time:    {c.get('sqlserver_start_time')}\n"
        report += f"  Uptime:            {c.get('uptime_days')} days\n"

    # SQL Server error log recent entries
    report += sub_header("Recent Error Log Entries (Errors/Warnings)")
    try:
        errors = run_query(conn, "EXEC sp_readerrorlog 0, 1, N'Error'")
        if errors and not any('ERROR' in str(e) for e in errors):
            for e in errors[-10:]:
                vals = list(e.values())
                date_val = vals[0] if len(vals) > 0 else ''
                text_val = vals[2] if len(vals) > 2 else (vals[1] if len(vals) > 1 else '')
                report += f"  [{date_val}] {str(text_val)[:120]}\n"
        else:
            report += "  (Could not read error log or no recent errors)\n"
    except Exception:
        report += "  (Error log not accessible)\n"

    return report


# ============================================================================
# SECTION 2: WAIT STATISTICS
# ============================================================================
def analyze_wait_stats(conn):
    report = section_header("2. WAIT STATISTICS ANALYSIS")

    waits = run_query(conn, """
        WITH WaitStats AS (
            SELECT
                wait_type,
                waiting_tasks_count,
                wait_time_ms,
                max_wait_time_ms,
                signal_wait_time_ms,
                wait_time_ms - signal_wait_time_ms AS resource_wait_ms
            FROM sys.dm_os_wait_stats
            WHERE wait_type NOT IN (
                'CLR_SEMAPHORE','LAZYWRITER_SLEEP','RESOURCE_QUEUE',
                'SLEEP_TASK','SLEEP_SYSTEMTASK','SQLTRACE_BUFFER_FLUSH',
                'WAITFOR','LOGMGR_QUEUE','CHECKPOINT_QUEUE',
                'REQUEST_FOR_DEADLOCK_SEARCH','XE_TIMER_EVENT',
                'BROKER_TO_FLUSH','BROKER_TASK_STOP','CLR_MANUAL_EVENT',
                'CLR_AUTO_EVENT','DISPATCHER_QUEUE_SEMAPHORE',
                'FT_IFTS_SCHEDULER_IDLE_WAIT','XE_DISPATCHER_WAIT',
                'XE_DISPATCHER_JOIN','SQLTRACE_INCREMENTAL_FLUSH_SLEEP',
                'ONDEMAND_TASK_QUEUE','BROKER_EVENTHANDLER',
                'SLEEP_BPOOL_FLUSH','SLEEP_DBSTARTUP',
                'DIRTY_PAGE_POLL','HADR_FILESTREAM_IOMGR_IOCOMPLETION',
                'SP_SERVER_DIAGNOSTICS_SLEEP','QDS_PERSIST_TASK_MAIN_LOOP_SLEEP',
                'QDS_ASYNC_QUEUE','QDS_CLEANUP_STALE_QUERIES_TASK_MAIN_LOOP_SLEEP',
                'WAIT_XTP_CKPT_CLOSE','PREEMPTIVE_OS_FLUSHFILEBUFFERS',
                'PREEMPTIVE_XE_GETTARGETSTATE'
            )
            AND waiting_tasks_count > 0
        )
        SELECT TOP 25
            wait_type,
            waiting_tasks_count,
            wait_time_ms / 1000.0 AS wait_time_sec,
            resource_wait_ms / 1000.0 AS resource_wait_sec,
            signal_wait_time_ms / 1000.0 AS signal_wait_sec,
            max_wait_time_ms / 1000.0 AS max_wait_sec,
            CAST(100.0 * wait_time_ms / SUM(wait_time_ms) OVER() AS DECIMAL(5,2)) AS pct
        FROM WaitStats
        ORDER BY wait_time_ms DESC
    """)
    report += sub_header("Top 25 Wait Types (since server restart)")
    report += f"  {'Wait Type':<40s} {'Count':>12s} {'Total(s)':>12s} {'Resource(s)':>12s} {'Signal(s)':>12s} {'Max(s)':>10s} {'%':>6s}\n"
    report += f"  {'─'*40} {'─'*12} {'─'*12} {'─'*12} {'─'*12} {'─'*10} {'─'*6}\n"
    for w in waits:
        report += (f"  {w['wait_type']:<40s} "
                   f"{fmt_num(w['waiting_tasks_count']):>12s} "
                   f"{fmt_num(w['wait_time_sec']):>12s} "
                   f"{fmt_num(w['resource_wait_sec']):>12s} "
                   f"{fmt_num(w['signal_wait_sec']):>12s} "
                   f"{fmt_num(w['max_wait_sec']):>10s} "
                   f"{fmt_pct(w['pct']):>6s}\n")

    # Signal wait ratio (CPU pressure indicator)
    signal = run_query(conn, """
        SELECT
            SUM(signal_wait_time_ms) AS total_signal,
            SUM(wait_time_ms) AS total_wait,
            CASE WHEN SUM(wait_time_ms) > 0
                THEN CAST(100.0 * SUM(signal_wait_time_ms) / SUM(wait_time_ms) AS DECIMAL(5,2))
                ELSE 0
            END AS signal_pct
        FROM sys.dm_os_wait_stats
        WHERE wait_type NOT LIKE '%SLEEP%'
          AND wait_type NOT LIKE '%QUEUE%'
          AND waiting_tasks_count > 0
    """)
    if signal:
        s = signal[0]
        pct = s.get('signal_pct', 0)
        report += f"\n  Signal Wait Ratio: {fmt_pct(pct)}"
        if pct and pct > 20:
            report += "  ⚠ HIGH - Indicates CPU pressure"
        elif pct and pct > 10:
            report += "  ⚡ MODERATE"
        else:
            report += "  ✓ Normal"
        report += "\n"

    return report


# ============================================================================
# SECTION 3: CPU ANALYSIS
# ============================================================================
def analyze_cpu(conn):
    report = section_header("3. CPU ANALYSIS")

    # CPU usage over time from ring buffer
    cpu_history = run_query(conn, """
        DECLARE @ts_now BIGINT = (SELECT cpu_ticks/(cpu_ticks/ms_ticks) FROM sys.dm_os_sys_info);
        SELECT TOP 30
            DATEADD(ms, -1 * (@ts_now - [timestamp]), GETDATE()) AS event_time,
            SQLProcessUtilization AS sql_cpu,
            SystemIdle AS idle_cpu,
            100 - SystemIdle - SQLProcessUtilization AS other_cpu
        FROM (
            SELECT record.value('(./Record/@id)[1]','int') AS record_id,
                   record.value('(./Record/SchedulerMonitorEvent/SystemHealth/SystemIdle)[1]','int') AS SystemIdle,
                   record.value('(./Record/SchedulerMonitorEvent/SystemHealth/ProcessUtilization)[1]','int') AS SQLProcessUtilization,
                   [timestamp]
            FROM (
                SELECT [timestamp], CONVERT(xml, record) AS record
                FROM sys.dm_os_ring_buffers
                WHERE ring_buffer_type = N'RING_BUFFER_SCHEDULER_MONITOR'
                  AND record LIKE N'%<SystemHealth>%'
            ) AS x
        ) AS y
        ORDER BY event_time DESC
    """)
    report += sub_header("CPU History (Last 30 Samples)")
    if cpu_history and not any('ERROR' in str(e) for e in cpu_history):
        report += f"  {'Time':<22s} {'SQL CPU%':>10s} {'Other CPU%':>10s} {'Idle%':>10s}\n"
        report += f"  {'─'*22} {'─'*10} {'─'*10} {'─'*10}\n"
        for c in cpu_history:
            flag = "  ⚠" if (c.get('sql_cpu') or 0) > 80 else ""
            report += (f"  {str(c.get('event_time', '')):<22s} "
                       f"{c.get('sql_cpu', 0):>10d} "
                       f"{c.get('other_cpu', 0):>10d} "
                       f"{c.get('idle_cpu', 0):>10d}{flag}\n")
    else:
        report += "  (Ring buffer data not available)\n"

    # Scheduler health
    schedulers = run_query(conn, """
        SELECT
            COUNT(*) AS total_schedulers,
            SUM(CASE WHEN is_online = 1 THEN 1 ELSE 0 END) AS online,
            SUM(current_tasks_count) AS total_tasks,
            SUM(runnable_tasks_count) AS runnable_tasks,
            SUM(active_workers_count) AS active_workers,
            SUM(work_queue_count) AS work_queue,
            AVG(load_factor) AS avg_load_factor
        FROM sys.dm_os_schedulers
        WHERE scheduler_id < 255
    """)
    if schedulers:
        s = schedulers[0]
        report += sub_header("Scheduler Health")
        report += f"  Online Schedulers:  {s.get('online')} / {s.get('total_schedulers')}\n"
        report += f"  Total Tasks:        {fmt_num(s.get('total_tasks'))}\n"
        report += f"  Runnable Tasks:     {fmt_num(s.get('runnable_tasks'))}"
        if (s.get('runnable_tasks') or 0) > 10:
            report += "  ⚠ CPU pressure (tasks waiting for CPU)"
        report += "\n"
        report += f"  Active Workers:     {fmt_num(s.get('active_workers'))}\n"
        report += f"  Work Queue:         {fmt_num(s.get('work_queue'))}\n"
        report += f"  Avg Load Factor:    {fmt_num(s.get('avg_load_factor'))}\n"

    return report


# ============================================================================
# SECTION 4: MEMORY ANALYSIS
# ============================================================================
def analyze_memory(conn):
    report = section_header("4. MEMORY ANALYSIS")

    # Buffer pool usage (use performance counters instead of scanning buffer descriptors - much faster)
    bp = run_query(conn, """
        SELECT
            instance_name AS db_name,
            cntr_value / 1024 AS buffer_mb,
            0 AS dirty_mb
        FROM sys.dm_os_performance_counters
        WHERE counter_name = 'Database pages'
          AND object_name LIKE '%Buffer Manager%'
        UNION ALL
        SELECT
            d.name AS db_name,
            (SUM(size) * 8) / 1024 AS buffer_mb,
            0 AS dirty_mb
        FROM sys.master_files mf
        JOIN sys.databases d ON mf.database_id = d.database_id
        WHERE d.name IN ('EDS', 'dpa_EDSAdmin', 'tempdb')
        GROUP BY d.name
        ORDER BY buffer_mb DESC
    """)
    report += sub_header("Buffer Pool by Database")
    report += f"  {'Database':<30s} {'Cached (MB)':>12s} {'Dirty (MB)':>12s}\n"
    report += f"  {'─'*30} {'─'*12} {'─'*12}\n"
    total_cached = 0
    for b in bp:
        total_cached += b.get('buffer_mb', 0)
        report += (f"  {str(b['db_name']):<30s} "
                   f"{fmt_num(b.get('buffer_mb', 0)):>12s} "
                   f"{fmt_num(b.get('dirty_mb', 0)):>12s}\n")
    report += f"\n  Total Buffer Pool: {fmt_num(total_cached)} MB\n"

    # Memory clerks
    clerks = run_query(conn, """
        SELECT TOP 15
            type AS clerk_type,
            SUM(pages_kb) / 1024 AS size_mb
        FROM sys.dm_os_memory_clerks
        GROUP BY type
        ORDER BY SUM(pages_kb) DESC
    """)
    report += sub_header("Top 15 Memory Clerks")
    for c in clerks:
        report += f"  {c['clerk_type']:<45s} {fmt_num(c.get('size_mb', 0)):>10s} MB\n"

    # Page Life Expectancy
    ple = run_query(conn, """
        SELECT
            object_name, counter_name, cntr_value
        FROM sys.dm_os_performance_counters
        WHERE counter_name IN ('Page life expectancy', 'Buffer cache hit ratio',
                               'Buffer cache hit ratio base', 'Page reads/sec',
                               'Page writes/sec', 'Lazy writes/sec',
                               'Free list stalls/sec', 'Memory Grants Pending',
                               'Target Server Memory (KB)', 'Total Server Memory (KB)')
        AND (object_name LIKE '%Buffer Manager%' OR object_name LIKE '%Memory Manager%')
    """)
    report += sub_header("Key Memory Counters")
    for p in ple:
        val = p.get('cntr_value', 0)
        name = p.get('counter_name', '').strip()
        flag = ""
        if name == 'Page life expectancy' and val < 300:
            flag = "  ⚠ LOW (should be >300)"
        elif name == 'Memory Grants Pending' and val > 0:
            flag = "  ⚠ QUERIES WAITING FOR MEMORY"
        report += f"  {name:<40s} {fmt_num(val):>15s}{flag}\n"

    # Memory grants
    grants = run_query(conn, """
        SELECT
            COUNT(*) AS total_grants,
            SUM(CASE WHEN grant_time IS NULL THEN 1 ELSE 0 END) AS pending_grants,
            SUM(granted_memory_kb) / 1024 AS total_granted_mb,
            MAX(granted_memory_kb) / 1024 AS max_single_grant_mb,
            SUM(used_memory_kb) / 1024 AS total_used_mb,
            SUM(ideal_memory_kb) / 1024 AS total_ideal_mb
        FROM sys.dm_exec_query_memory_grants
    """)
    if grants:
        g = grants[0]
        report += sub_header("Active Memory Grants")
        report += f"  Total Grants:       {fmt_num(g.get('total_grants'))}\n"
        report += f"  Pending Grants:     {fmt_num(g.get('pending_grants'))}"
        if (g.get('pending_grants') or 0) > 0:
            report += "  ⚠ MEMORY PRESSURE"
        report += "\n"
        report += f"  Total Granted:      {fmt_num(g.get('total_granted_mb'))} MB\n"
        report += f"  Max Single Grant:   {fmt_num(g.get('max_single_grant_mb'))} MB\n"
        report += f"  Total Used:         {fmt_num(g.get('total_used_mb'))} MB\n"
        report += f"  Total Ideal:        {fmt_num(g.get('total_ideal_mb'))} MB\n"

    return report


# ============================================================================
# SECTION 5: I/O ANALYSIS
# ============================================================================
def analyze_io(conn):
    report = section_header("5. I/O ANALYSIS")

    # File level I/O
    io_stats = run_query(conn, """
        SELECT
            DB_NAME(vfs.database_id) AS db_name,
            mf.name AS file_name,
            mf.physical_name,
            mf.type_desc,
            vfs.num_of_reads,
            vfs.num_of_writes,
            vfs.num_of_bytes_read / 1024 / 1024 AS read_mb,
            vfs.num_of_bytes_written / 1024 / 1024 AS write_mb,
            vfs.io_stall_read_ms,
            vfs.io_stall_write_ms,
            vfs.io_stall,
            CASE WHEN vfs.num_of_reads > 0
                THEN vfs.io_stall_read_ms / vfs.num_of_reads ELSE 0
            END AS avg_read_latency_ms,
            CASE WHEN vfs.num_of_writes > 0
                THEN vfs.io_stall_write_ms / vfs.num_of_writes ELSE 0
            END AS avg_write_latency_ms
        FROM sys.dm_io_virtual_file_stats(NULL, NULL) vfs
        JOIN sys.master_files mf ON vfs.database_id = mf.database_id
            AND vfs.file_id = mf.file_id
        WHERE DB_NAME(vfs.database_id) IN ('EDS', 'dpa_EDSAdmin', 'tempdb')
        ORDER BY vfs.io_stall DESC
    """)
    report += sub_header("File-Level I/O Statistics")
    report += f"  {'Database':<15s} {'File':<20s} {'Type':<6s} {'Reads':>10s} {'Writes':>10s} {'ReadMB':>10s} {'WriteMB':>10s} {'AvgR(ms)':>10s} {'AvgW(ms)':>10s}\n"
    report += f"  {'─'*15} {'─'*20} {'─'*6} {'─'*10} {'─'*10} {'─'*10} {'─'*10} {'─'*10} {'─'*10}\n"
    for i in io_stats:
        r_lat = i.get('avg_read_latency_ms', 0)
        w_lat = i.get('avg_write_latency_ms', 0)
        flag = ""
        if r_lat > 20 or w_lat > 20:
            flag = " ⚠"
        report += (f"  {str(i.get('db_name', '')):<15s} "
                   f"{str(i.get('file_name', '')):<20s} "
                   f"{str(i.get('type_desc', '')):<6s} "
                   f"{fmt_num(i.get('num_of_reads')):>10s} "
                   f"{fmt_num(i.get('num_of_writes')):>10s} "
                   f"{fmt_num(i.get('read_mb')):>10s} "
                   f"{fmt_num(i.get('write_mb')):>10s} "
                   f"{fmt_num(r_lat):>10s} "
                   f"{fmt_num(w_lat):>10s}{flag}\n")

    # Pending I/O
    pending = run_query(conn, """
        SELECT
            DB_NAME(vfs.database_id) AS db_name,
            mf.physical_name,
            vfs.io_stall_queued_read_ms,
            vfs.io_stall_queued_write_ms
        FROM sys.dm_io_virtual_file_stats(NULL, NULL) vfs
        JOIN sys.master_files mf ON vfs.database_id = mf.database_id
            AND vfs.file_id = mf.file_id
        WHERE (vfs.io_stall_queued_read_ms > 0 OR vfs.io_stall_queued_write_ms > 0)
        ORDER BY (vfs.io_stall_queued_read_ms + vfs.io_stall_queued_write_ms) DESC
    """)
    if pending:
        report += sub_header("Files with Queued I/O Stalls")
        for p in pending[:10]:
            report += f"  {p.get('db_name')}: {p.get('physical_name')} - Read Queue: {fmt_num(p.get('io_stall_queued_read_ms'))}ms, Write Queue: {fmt_num(p.get('io_stall_queued_write_ms'))}ms\n"

    return report


# ============================================================================
# SECTION 6: TOP QUERIES BY RESOURCE CONSUMPTION
# ============================================================================
def analyze_top_queries(conn):
    report = section_header("6. TOP QUERIES BY RESOURCE CONSUMPTION")

    # Top by CPU
    top_cpu = run_query(conn, """
        SELECT TOP 15
            qs.total_worker_time / 1000 AS total_cpu_ms,
            qs.execution_count,
            qs.total_worker_time / qs.execution_count / 1000 AS avg_cpu_ms,
            qs.total_elapsed_time / qs.execution_count / 1000 AS avg_elapsed_ms,
            qs.total_logical_reads / qs.execution_count AS avg_logical_reads,
            qs.total_logical_writes / qs.execution_count AS avg_logical_writes,
            qs.creation_time AS plan_created,
            qs.last_execution_time,
            SUBSTRING(st.text, (qs.statement_start_offset/2)+1,
                ((CASE qs.statement_end_offset
                    WHEN -1 THEN DATALENGTH(st.text)
                    ELSE qs.statement_end_offset
                END - qs.statement_start_offset)/2) + 1) AS query_text
        FROM sys.dm_exec_query_stats qs
        CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
        WHERE st.dbid = DB_ID('EDS') OR st.dbid IS NULL
        ORDER BY qs.total_worker_time DESC
    """)
    report += sub_header("Top 15 Queries by Total CPU")
    report += f"  {'#':>3s} {'TotalCPU(ms)':>14s} {'Execs':>10s} {'AvgCPU(ms)':>12s} {'AvgElapsed(ms)':>16s} {'AvgReads':>12s} {'Query (truncated)'}\n"
    report += f"  {'─'*3} {'─'*14} {'─'*10} {'─'*12} {'─'*16} {'─'*12} {'─'*60}\n"
    for idx, q in enumerate(top_cpu, 1):
        qtext = str(q.get('query_text', '')).replace('\n', ' ').replace('\r', '')[:80]
        report += (f"  {idx:3d} "
                   f"{fmt_num(q.get('total_cpu_ms')):>14s} "
                   f"{fmt_num(q.get('execution_count')):>10s} "
                   f"{fmt_num(q.get('avg_cpu_ms')):>12s} "
                   f"{fmt_num(q.get('avg_elapsed_ms')):>16s} "
                   f"{fmt_num(q.get('avg_logical_reads')):>12s} "
                   f"{qtext}\n")

    # Top by reads
    top_reads = run_query(conn, """
        SELECT TOP 15
            qs.total_logical_reads,
            qs.execution_count,
            qs.total_logical_reads / qs.execution_count AS avg_reads,
            qs.total_worker_time / qs.execution_count / 1000 AS avg_cpu_ms,
            qs.last_execution_time,
            SUBSTRING(st.text, (qs.statement_start_offset/2)+1,
                ((CASE qs.statement_end_offset
                    WHEN -1 THEN DATALENGTH(st.text)
                    ELSE qs.statement_end_offset
                END - qs.statement_start_offset)/2) + 1) AS query_text
        FROM sys.dm_exec_query_stats qs
        CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
        WHERE st.dbid = DB_ID('EDS') OR st.dbid IS NULL
        ORDER BY qs.total_logical_reads DESC
    """)
    report += sub_header("Top 15 Queries by Total Logical Reads")
    report += f"  {'#':>3s} {'TotalReads':>14s} {'Execs':>10s} {'AvgReads':>12s} {'AvgCPU(ms)':>12s} {'Query (truncated)'}\n"
    report += f"  {'─'*3} {'─'*14} {'─'*10} {'─'*12} {'─'*12} {'─'*60}\n"
    for idx, q in enumerate(top_reads, 1):
        qtext = str(q.get('query_text', '')).replace('\n', ' ').replace('\r', '')[:80]
        report += (f"  {idx:3d} "
                   f"{fmt_num(q.get('total_logical_reads')):>14s} "
                   f"{fmt_num(q.get('execution_count')):>10s} "
                   f"{fmt_num(q.get('avg_reads')):>12s} "
                   f"{fmt_num(q.get('avg_cpu_ms')):>12s} "
                   f"{qtext}\n")

    # Top by elapsed time (long running)
    top_elapsed = run_query(conn, """
        SELECT TOP 15
            qs.total_elapsed_time / 1000 AS total_elapsed_ms,
            qs.execution_count,
            qs.total_elapsed_time / qs.execution_count / 1000 AS avg_elapsed_ms,
            qs.total_worker_time / qs.execution_count / 1000 AS avg_cpu_ms,
            qs.max_elapsed_time / 1000 AS max_elapsed_ms,
            qs.last_execution_time,
            SUBSTRING(st.text, (qs.statement_start_offset/2)+1,
                ((CASE qs.statement_end_offset
                    WHEN -1 THEN DATALENGTH(st.text)
                    ELSE qs.statement_end_offset
                END - qs.statement_start_offset)/2) + 1) AS query_text
        FROM sys.dm_exec_query_stats qs
        CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) st
        WHERE st.dbid = DB_ID('EDS') OR st.dbid IS NULL
        ORDER BY qs.total_elapsed_time DESC
    """)
    report += sub_header("Top 15 Queries by Total Elapsed Time")
    report += f"  {'#':>3s} {'TotalElapsed(ms)':>16s} {'Execs':>10s} {'AvgElapsed(ms)':>16s} {'MaxElapsed(ms)':>16s} {'Query (truncated)'}\n"
    report += f"  {'─'*3} {'─'*16} {'─'*10} {'─'*16} {'─'*16} {'─'*60}\n"
    for idx, q in enumerate(top_elapsed, 1):
        qtext = str(q.get('query_text', '')).replace('\n', ' ').replace('\r', '')[:80]
        report += (f"  {idx:3d} "
                   f"{fmt_num(q.get('total_elapsed_ms')):>16s} "
                   f"{fmt_num(q.get('execution_count')):>10s} "
                   f"{fmt_num(q.get('avg_elapsed_ms')):>16s} "
                   f"{fmt_num(q.get('max_elapsed_ms')):>16s} "
                   f"{qtext}\n")

    return report


# ============================================================================
# SECTION 7: PLAN CACHE ANALYSIS
# ============================================================================
def analyze_plan_cache(conn):
    report = section_header("7. PLAN CACHE ANALYSIS")

    # Plan cache summary
    cache_summary = run_query(conn, """
        SELECT
            objtype AS plan_type,
            COUNT(*) AS plan_count,
            SUM(usecounts) AS total_uses,
            SUM(size_in_bytes) / 1024 / 1024 AS size_mb,
            AVG(usecounts) AS avg_uses,
            SUM(CASE WHEN usecounts = 1 THEN 1 ELSE 0 END) AS single_use_count
        FROM sys.dm_exec_cached_plans
        GROUP BY objtype
        ORDER BY SUM(size_in_bytes) DESC
    """)
    report += sub_header("Plan Cache Summary by Type")
    report += f"  {'Type':<12s} {'Plans':>10s} {'Total Uses':>12s} {'Size(MB)':>10s} {'AvgUses':>10s} {'SingleUse':>12s}\n"
    report += f"  {'─'*12} {'─'*10} {'─'*12} {'─'*10} {'─'*10} {'─'*12}\n"
    total_plans = 0
    total_single = 0
    for c in cache_summary:
        total_plans += c.get('plan_count', 0)
        total_single += c.get('single_use_count', 0)
        report += (f"  {str(c.get('plan_type', '')):<12s} "
                   f"{fmt_num(c.get('plan_count')):>10s} "
                   f"{fmt_num(c.get('total_uses')):>12s} "
                   f"{fmt_num(c.get('size_mb')):>10s} "
                   f"{fmt_num(c.get('avg_uses')):>10s} "
                   f"{fmt_num(c.get('single_use_count')):>12s}\n")

    if total_plans > 0:
        bloat_pct = (total_single / total_plans) * 100
        report += f"\n  Plan Cache Bloat: {bloat_pct:.1f}% single-use plans ({total_single:,} of {total_plans:,})"
        if bloat_pct > 50:
            report += "  ⚠ HIGH - Consider 'optimize for ad hoc workloads'"
        report += "\n"

    # Frequently recompiled
    recompile = run_query(conn, """
        SELECT TOP 10
            plan_generation_num,
            execution_count,
            OBJECT_NAME(objectid, dbid) AS object_name,
            SUBSTRING(text, 1, 100) AS query_text
        FROM sys.dm_exec_query_stats qs
        CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle)
        WHERE plan_generation_num > 5
        ORDER BY plan_generation_num DESC
    """)
    if recompile:
        report += sub_header("Top Recompiled Queries (plan_generation_num > 5)")
        for r in recompile:
            report += f"  Recompiles: {r.get('plan_generation_num')}, Execs: {fmt_num(r.get('execution_count'))}, Object: {r.get('object_name')}\n"
            report += f"    SQL: {str(r.get('query_text', ''))[:100]}\n"

    return report


# ============================================================================
# SECTION 8: INDEX ANALYSIS
# ============================================================================
def analyze_indexes(conn):
    report = section_header("8. INDEX ANALYSIS")

    # Missing indexes
    missing = run_query(conn, """
        SELECT TOP 25
            OBJECT_NAME(mid.object_id) AS table_name,
            mid.equality_columns,
            mid.inequality_columns,
            mid.included_columns,
            migs.avg_user_impact,
            migs.user_seeks,
            migs.user_scans,
            migs.avg_total_user_cost,
            migs.avg_user_impact * (migs.user_seeks + migs.user_scans) *
                migs.avg_total_user_cost AS improvement_measure
        FROM sys.dm_db_missing_index_groups mig
        JOIN sys.dm_db_missing_index_group_stats migs ON mig.index_group_handle = migs.group_handle
        JOIN sys.dm_db_missing_index_details mid ON mig.index_handle = mid.index_handle
        WHERE mid.database_id = DB_ID('EDS')
        ORDER BY migs.avg_user_impact * (migs.user_seeks + migs.user_scans) *
                 migs.avg_total_user_cost DESC
    """)
    report += sub_header("Top 25 Missing Indexes (by improvement measure)")
    report += f"  {'Table':<35s} {'Impact%':>8s} {'Seeks':>10s} {'Scans':>10s} {'Score':>14s}\n"
    report += f"  {'─'*35} {'─'*8} {'─'*10} {'─'*10} {'─'*14}\n"
    for m in missing:
        report += (f"  {str(m.get('table_name', '')):<35s} "
                   f"{fmt_pct(m.get('avg_user_impact')):>8s} "
                   f"{fmt_num(m.get('user_seeks')):>10s} "
                   f"{fmt_num(m.get('user_scans')):>10s} "
                   f"{fmt_num(m.get('improvement_measure')):>14s}\n")
        if m.get('equality_columns'):
            report += f"    Equality:  {m['equality_columns']}\n"
        if m.get('inequality_columns'):
            report += f"    Inequality: {m['inequality_columns']}\n"
        if m.get('included_columns'):
            report += f"    Include:   {m['included_columns']}\n"
        report += "\n"

    # Unused indexes
    unused = run_query(conn, """
        SELECT
            OBJECT_NAME(i.object_id) AS table_name,
            i.name AS index_name,
            i.type_desc,
            ius.user_seeks, ius.user_scans, ius.user_lookups, ius.user_updates,
            (SELECT SUM(a.used_pages) * 8 / 1024
             FROM sys.partitions p
             JOIN sys.allocation_units a ON p.partition_id = a.container_id
             WHERE p.object_id = i.object_id AND p.index_id = i.index_id) AS size_mb
        FROM sys.indexes i
        LEFT JOIN sys.dm_db_index_usage_stats ius
            ON i.object_id = ius.object_id AND i.index_id = ius.index_id
            AND ius.database_id = DB_ID()
        WHERE OBJECTPROPERTY(i.object_id, 'IsUserTable') = 1
          AND i.type_desc <> 'HEAP'
          AND i.is_primary_key = 0
          AND i.is_unique = 0
          AND (ius.user_seeks + ius.user_scans + ius.user_lookups) = 0
          AND ius.user_updates > 100
        ORDER BY ius.user_updates DESC
    """)
    report += sub_header("Unused Indexes (0 reads, >100 writes)")
    report += f"  {'Table':<35s} {'Index':<35s} {'Updates':>10s} {'Size(MB)':>10s}\n"
    report += f"  {'─'*35} {'─'*35} {'─'*10} {'─'*10}\n"
    total_wasted = 0
    for u in unused[:25]:
        sz = u.get('size_mb') or 0
        total_wasted += sz
        report += (f"  {str(u.get('table_name', '')):<35s} "
                   f"{str(u.get('index_name', '')):<35s} "
                   f"{fmt_num(u.get('user_updates')):>10s} "
                   f"{fmt_num(sz):>10s}\n")
    report += f"\n  Total wasted space from unused indexes: {fmt_num(total_wasted)} MB\n"

    # Index fragmentation on key tables only (full scan too slow on 1.2TB DB)
    frag = run_query(conn, """
        SELECT TOP 20
            OBJECT_NAME(ips.object_id) AS table_name,
            i.name AS index_name,
            ips.index_type_desc,
            ips.avg_fragmentation_in_percent,
            ips.page_count,
            ips.page_count * 8 / 1024 AS size_mb,
            ips.avg_page_space_used_in_percent
        FROM (
            SELECT object_id FROM sys.tables
            WHERE name IN ('Detail','CrossRefs','BidResults','Items','Users',
                           'PricingConsolidated','BidMappedItems','VendorCategoryPP')
        ) key_tables
        CROSS APPLY sys.dm_db_index_physical_stats(DB_ID(), key_tables.object_id, NULL, NULL, 'LIMITED') ips
        JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id
        WHERE ips.page_count > 1000
          AND ips.avg_fragmentation_in_percent > 10
        ORDER BY ips.avg_fragmentation_in_percent DESC
    """)
    report += sub_header("Fragmented Indexes (>10%, >1000 pages)")
    report += f"  {'Table':<30s} {'Index':<30s} {'Frag%':>8s} {'Pages':>10s} {'Size(MB)':>10s} {'Action'}\n"
    report += f"  {'─'*30} {'─'*30} {'─'*8} {'─'*10} {'─'*10} {'─'*15}\n"
    for f in frag:
        pct = f.get('avg_fragmentation_in_percent', 0)
        action = "REBUILD" if pct > 30 else "REORGANIZE"
        report += (f"  {str(f.get('table_name', '')):<30s} "
                   f"{str(f.get('index_name', '')):<30s} "
                   f"{fmt_pct(pct):>8s} "
                   f"{fmt_num(f.get('page_count')):>10s} "
                   f"{fmt_num(f.get('size_mb')):>10s} "
                   f"{action}\n")

    return report


# ============================================================================
# SECTION 9: BLOCKING & DEADLOCK ANALYSIS
# ============================================================================
def analyze_blocking(conn):
    report = section_header("9. BLOCKING & DEADLOCK ANALYSIS")

    # Current blocking
    blocking = run_query(conn, """
        SELECT
            r.session_id AS blocked_session,
            r.blocking_session_id AS blocker_session,
            r.wait_type,
            r.wait_time / 1000 AS wait_sec,
            r.wait_resource,
            DB_NAME(r.database_id) AS database_name,
            t.text AS blocked_query,
            (SELECT text FROM sys.dm_exec_sql_text(
                (SELECT most_recent_sql_handle FROM sys.dm_exec_connections
                 WHERE session_id = r.blocking_session_id)
            )) AS blocker_query
        FROM sys.dm_exec_requests r
        CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t
        WHERE r.blocking_session_id > 0
        ORDER BY r.wait_time DESC
    """)
    report += sub_header("Current Blocking Chains")
    if blocking:
        for b in blocking:
            report += f"  BLOCKED: Session {b.get('blocked_session')} (waiting {fmt_num(b.get('wait_sec'))}s)\n"
            report += f"  BLOCKER: Session {b.get('blocker_session')}\n"
            report += f"  Wait:    {b.get('wait_type')} on {b.get('wait_resource')}\n"
            report += f"  Victim:  {str(b.get('blocked_query', ''))[:100]}\n"
            report += f"  Blocker: {str(b.get('blocker_query', ''))[:100]}\n\n"
    else:
        report += "  No active blocking detected ✓\n"

    # Open transactions
    open_trans = run_query(conn, """
        SELECT
            s.session_id,
            s.login_name,
            s.host_name,
            s.program_name,
            t.transaction_begin_time,
            DATEDIFF(second, t.transaction_begin_time, GETDATE()) AS age_seconds,
            t.transaction_type,
            CASE t.transaction_state
                WHEN 0 THEN 'Not initialized'
                WHEN 1 THEN 'Initialized not started'
                WHEN 2 THEN 'Active'
                WHEN 3 THEN 'Ended (read-only)'
                WHEN 4 THEN 'Commit initiated'
                WHEN 6 THEN 'Committed'
                WHEN 7 THEN 'Rolling back'
                WHEN 8 THEN 'Rolled back'
            END AS transaction_state
        FROM sys.dm_tran_active_transactions t
        JOIN sys.dm_tran_session_transactions st ON t.transaction_id = st.transaction_id
        JOIN sys.dm_exec_sessions s ON st.session_id = s.session_id
        WHERE t.transaction_begin_time < DATEADD(minute, -5, GETDATE())
        ORDER BY t.transaction_begin_time
    """)
    report += sub_header("Long-Running Open Transactions (>5 min)")
    if open_trans:
        for o in open_trans:
            report += (f"  Session {o.get('session_id')}: {o.get('login_name')}@{o.get('host_name')} "
                       f"({o.get('program_name')})\n"
                       f"    Started: {o.get('transaction_begin_time')} ({fmt_num(o.get('age_seconds'))}s ago) "
                       f"State: {o.get('transaction_state')}\n")
    else:
        report += "  No long-running transactions ✓\n"

    # Deadlock info from system health
    deadlocks = run_query(conn, """
        SELECT COUNT(*) AS deadlock_count
        FROM sys.dm_os_ring_buffers
        WHERE ring_buffer_type = 'RING_BUFFER_DEADLOCK'
    """)
    if deadlocks:
        report += sub_header("Deadlock Count (from ring buffer)")
        report += f"  Deadlocks recorded: {deadlocks[0].get('deadlock_count', 0)}\n"

    # Lock waits summary
    lock_waits = run_query(conn, """
        SELECT
            request_mode,
            request_type,
            request_status,
            COUNT(*) AS cnt
        FROM sys.dm_tran_locks
        WHERE request_status = 'WAIT'
        GROUP BY request_mode, request_type, request_status
        ORDER BY COUNT(*) DESC
    """)
    if lock_waits:
        report += sub_header("Current Lock Waits")
        for l in lock_waits:
            report += f"  {l.get('request_mode')} {l.get('request_type')}: {l.get('cnt')} waiting\n"
    else:
        report += sub_header("Current Lock Waits")
        report += "  No lock waits ✓\n"

    return report


# ============================================================================
# SECTION 10: DATABASE FILE & STORAGE ANALYSIS
# ============================================================================
def analyze_storage(conn):
    report = section_header("10. DATABASE FILE & STORAGE ANALYSIS")

    # Database sizes
    db_sizes = run_query(conn, """
        SELECT
            DB_NAME(database_id) AS db_name,
            type_desc,
            name AS file_name,
            physical_name,
            size * 8 / 1024 AS size_mb,
            FILEPROPERTY(name, 'SpaceUsed') * 8 / 1024 AS used_mb,
            (size - FILEPROPERTY(name, 'SpaceUsed')) * 8 / 1024 AS free_mb,
            CASE max_size
                WHEN -1 THEN 'Unlimited'
                WHEN 0 THEN 'No Growth'
                ELSE CAST(max_size * 8 / 1024 AS VARCHAR) + ' MB'
            END AS max_size,
            CASE is_percent_growth
                WHEN 1 THEN CAST(growth AS VARCHAR) + '%'
                ELSE CAST(growth * 8 / 1024 AS VARCHAR) + ' MB'
            END AS growth
        FROM sys.database_files
        ORDER BY type_desc, size DESC
    """)
    report += sub_header("Database Files (Current Database: EDS)")
    report += f"  {'File':<25s} {'Type':<10s} {'Size(MB)':>10s} {'Used(MB)':>10s} {'Free(MB)':>10s} {'Used%':>8s} {'MaxSize':>12s} {'Growth':>10s}\n"
    report += f"  {'─'*25} {'─'*10} {'─'*10} {'─'*10} {'─'*10} {'─'*8} {'─'*12} {'─'*10}\n"
    for d in db_sizes:
        used = d.get('used_mb') or 0
        total = d.get('size_mb') or 1
        pct = (used / total * 100) if total > 0 else 0
        flag = " ⚠" if pct > 90 else ""
        report += (f"  {str(d.get('file_name', '')):<25s} "
                   f"{str(d.get('type_desc', '')):<10s} "
                   f"{fmt_num(d.get('size_mb')):>10s} "
                   f"{fmt_num(d.get('used_mb')):>10s} "
                   f"{fmt_num(d.get('free_mb')):>10s} "
                   f"{fmt_pct(pct):>8s} "
                   f"{str(d.get('max_size', '')):>12s} "
                   f"{str(d.get('growth', '')):>10s}{flag}\n")

    # Table sizes
    table_sizes = run_query(conn, """
        SELECT TOP 30
            s.name + '.' + t.name AS table_name,
            p.rows AS row_count,
            SUM(a.total_pages) * 8 / 1024 AS total_mb,
            SUM(a.used_pages) * 8 / 1024 AS used_mb,
            SUM(a.data_pages) * 8 / 1024 AS data_mb,
            (SUM(a.total_pages) - SUM(a.used_pages)) * 8 / 1024 AS unused_mb,
            COUNT(DISTINCT i.index_id) AS index_count
        FROM sys.tables t
        JOIN sys.schemas s ON t.schema_id = s.schema_id
        JOIN sys.indexes i ON t.object_id = i.object_id
        JOIN sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
        JOIN sys.allocation_units a ON p.partition_id = a.container_id
        GROUP BY s.name, t.name, p.rows
        ORDER BY SUM(a.total_pages) DESC
    """)
    report += sub_header("Top 30 Tables by Size")
    report += f"  {'Table':<45s} {'Rows':>14s} {'Total(MB)':>10s} {'Data(MB)':>10s} {'Unused(MB)':>10s} {'Indexes':>8s}\n"
    report += f"  {'─'*45} {'─'*14} {'─'*10} {'─'*10} {'─'*10} {'─'*8}\n"
    for t in table_sizes:
        report += (f"  {str(t.get('table_name', '')):<45s} "
                   f"{fmt_num(t.get('row_count')):>14s} "
                   f"{fmt_num(t.get('total_mb')):>10s} "
                   f"{fmt_num(t.get('data_mb')):>10s} "
                   f"{fmt_num(t.get('unused_mb')):>10s} "
                   f"{fmt_num(t.get('index_count')):>8s}\n")

    return report


# ============================================================================
# SECTION 11: STORED PROCEDURE PERFORMANCE
# ============================================================================
def analyze_procedures(conn):
    report = section_header("11. STORED PROCEDURE PERFORMANCE")

    procs = run_query(conn, """
        SELECT TOP 25
            OBJECT_NAME(ps.object_id) AS proc_name,
            ps.execution_count,
            ps.total_worker_time / 1000 AS total_cpu_ms,
            ps.total_elapsed_time / 1000 AS total_elapsed_ms,
            ps.total_worker_time / ps.execution_count / 1000 AS avg_cpu_ms,
            ps.total_elapsed_time / ps.execution_count / 1000 AS avg_elapsed_ms,
            ps.total_logical_reads / ps.execution_count AS avg_reads,
            ps.total_logical_writes / ps.execution_count AS avg_writes,
            ps.max_elapsed_time / 1000 AS max_elapsed_ms,
            ps.cached_time,
            ps.last_execution_time
        FROM sys.dm_exec_procedure_stats ps
        WHERE ps.database_id = DB_ID('EDS')
        ORDER BY ps.total_worker_time DESC
    """)
    report += sub_header("Top 25 Procedures by Total CPU")
    report += (f"  {'Procedure':<40s} {'Execs':>10s} {'TotalCPU(ms)':>14s} {'AvgCPU(ms)':>12s} "
               f"{'AvgElapsed(ms)':>16s} {'AvgReads':>12s} {'MaxElapsed(ms)':>16s}\n")
    report += f"  {'─'*40} {'─'*10} {'─'*14} {'─'*12} {'─'*16} {'─'*12} {'─'*16}\n"
    for p in procs:
        flag = ""
        if (p.get('avg_elapsed_ms') or 0) > 10000:
            flag = " ⚠ SLOW"
        report += (f"  {str(p.get('proc_name', '')):<40s} "
                   f"{fmt_num(p.get('execution_count')):>10s} "
                   f"{fmt_num(p.get('total_cpu_ms')):>14s} "
                   f"{fmt_num(p.get('avg_cpu_ms')):>12s} "
                   f"{fmt_num(p.get('avg_elapsed_ms')):>16s} "
                   f"{fmt_num(p.get('avg_reads')):>12s} "
                   f"{fmt_num(p.get('max_elapsed_ms')):>16s}{flag}\n")

    # Most executed procedures
    most_exec = run_query(conn, """
        SELECT TOP 15
            OBJECT_NAME(ps.object_id) AS proc_name,
            ps.execution_count,
            ps.total_worker_time / ps.execution_count / 1000 AS avg_cpu_ms,
            ps.total_elapsed_time / ps.execution_count / 1000 AS avg_elapsed_ms,
            ps.last_execution_time
        FROM sys.dm_exec_procedure_stats ps
        WHERE ps.database_id = DB_ID('EDS')
        ORDER BY ps.execution_count DESC
    """)
    report += sub_header("Top 15 Most Frequently Executed Procedures")
    for p in most_exec:
        report += (f"  {str(p.get('proc_name', '')):<40s} "
                   f"Execs: {fmt_num(p.get('execution_count')):>12s}  "
                   f"AvgCPU: {fmt_num(p.get('avg_cpu_ms')):>8s}ms  "
                   f"AvgElapsed: {fmt_num(p.get('avg_elapsed_ms')):>8s}ms  "
                   f"Last: {p.get('last_execution_time')}\n")

    return report


# ============================================================================
# SECTION 12: TRIGGER ANALYSIS
# ============================================================================
def analyze_triggers(conn):
    report = section_header("12. TRIGGER ANALYSIS")

    triggers = run_query(conn, """
        SELECT
            OBJECT_NAME(parent_id) AS table_name,
            t.name AS trigger_name,
            t.type_desc,
            te.type_desc AS event_type,
            t.is_disabled,
            t.is_instead_of_trigger,
            OBJECT_DEFINITION(t.object_id) AS trigger_definition
        FROM sys.triggers t
        JOIN sys.trigger_events te ON t.object_id = te.object_id
        WHERE t.parent_class = 1
        ORDER BY OBJECT_NAME(parent_id), t.name
    """)
    report += sub_header(f"All Triggers ({len(triggers)} total)")
    current_table = ""
    for tr in triggers:
        tbl = tr.get('table_name', '')
        if tbl != current_table:
            current_table = tbl
            report += f"\n  Table: {tbl}\n"
        defn = str(tr.get('trigger_definition', ''))
        # Count lines as complexity indicator
        lines = len(defn.split('\n')) if defn else 0
        disabled = " [DISABLED]" if tr.get('is_disabled') else ""
        instead = " [INSTEAD OF]" if tr.get('is_instead_of_trigger') else ""
        report += f"    {tr.get('trigger_name'):<35s} {tr.get('event_type'):<10s} ~{lines} lines{disabled}{instead}\n"

    # Check for known problem trigger
    report += sub_header("Known Problem: trig_DetailUpdate Analysis")
    detail_trigger = run_query(conn, """
        SELECT LEN(OBJECT_DEFINITION(OBJECT_ID('trig_DetailUpdate'))) AS definition_length
    """)
    if detail_trigger and detail_trigger[0].get('definition_length'):
        report += f"  trig_DetailUpdate definition size: {fmt_num(detail_trigger[0]['definition_length'])} chars\n"
        report += "  ⚠ Known P3 issue: Causes up to 82 minutes blocking on Detail table\n"
        report += "  ⚠ Affects: CrossRefs, BidMappedItems, Items lookups\n"
    else:
        report += "  trig_DetailUpdate not found or not accessible\n"

    return report


# ============================================================================
# SECTION 13: TEMPDB ANALYSIS
# ============================================================================
def analyze_tempdb(conn):
    report = section_header("13. TEMPDB ANALYSIS")

    # TempDB configuration
    tempdb_files = run_query(conn, """
        SELECT
            name, physical_name,
            size * 8 / 1024 AS size_mb,
            CASE max_size
                WHEN -1 THEN 'Unlimited'
                ELSE CAST(max_size * 8 / 1024 AS VARCHAR) + ' MB'
            END AS max_size,
            type_desc
        FROM tempdb.sys.database_files
        ORDER BY type_desc, file_id
    """)
    report += sub_header("TempDB File Configuration")
    for t in tempdb_files:
        report += f"  {t.get('name'):<25s} {str(t.get('type_desc')):<8s} Size: {fmt_num(t.get('size_mb'))} MB, Max: {t.get('max_size')}\n"

    data_files = sum(1 for t in tempdb_files if t.get('type_desc') == 'ROWS')
    report += f"\n  Data Files: {data_files}"
    cpu = run_query(conn, "SELECT cpu_count FROM sys.dm_os_sys_info")
    if cpu:
        cpus = cpu[0].get('cpu_count', 0)
        if data_files < min(8, cpus):
            report += f"  ⚠ Recommend {min(8, cpus)} files (1 per CPU up to 8)"
    report += "\n"

    # TempDB space usage
    usage = run_query(conn, """
        SELECT
            SUM(user_object_reserved_page_count) * 8 / 1024 AS user_objects_mb,
            SUM(internal_object_reserved_page_count) * 8 / 1024 AS internal_objects_mb,
            SUM(version_store_reserved_page_count) * 8 / 1024 AS version_store_mb,
            SUM(unallocated_extent_page_count) * 8 / 1024 AS free_space_mb
        FROM tempdb.sys.dm_db_file_space_usage
    """)
    if usage:
        u = usage[0]
        report += sub_header("TempDB Space Usage")
        report += f"  User Objects:      {fmt_num(u.get('user_objects_mb'))} MB\n"
        report += f"  Internal Objects:  {fmt_num(u.get('internal_objects_mb'))} MB\n"
        report += f"  Version Store:     {fmt_num(u.get('version_store_mb'))} MB\n"
        report += f"  Free Space:        {fmt_num(u.get('free_space_mb'))} MB\n"

    # Top TempDB consumers
    tempdb_tasks = run_query(conn, """
        SELECT TOP 10
            t.session_id,
            t.request_id,
            SUM(t.user_objects_alloc_page_count - t.user_objects_dealloc_page_count) * 8 / 1024 AS user_mb,
            SUM(t.internal_objects_alloc_page_count - t.internal_objects_dealloc_page_count) * 8 / 1024 AS internal_mb,
            s.login_name,
            s.program_name,
            (SELECT text FROM sys.dm_exec_sql_text(
                (SELECT most_recent_sql_handle FROM sys.dm_exec_connections c WHERE c.session_id = t.session_id)
            )) AS query_text
        FROM sys.dm_db_task_space_usage t
        JOIN sys.dm_exec_sessions s ON t.session_id = s.session_id
        WHERE t.session_id > 50
        GROUP BY t.session_id, t.request_id, s.login_name, s.program_name
        HAVING SUM(t.user_objects_alloc_page_count + t.internal_objects_alloc_page_count) > 0
        ORDER BY SUM(t.user_objects_alloc_page_count + t.internal_objects_alloc_page_count) DESC
    """)
    if tempdb_tasks:
        report += sub_header("Top TempDB Consumers (Active Tasks)")
        for t in tempdb_tasks:
            report += (f"  Session {t.get('session_id')}: User: {fmt_num(t.get('user_mb'))} MB, "
                       f"Internal: {fmt_num(t.get('internal_mb'))} MB "
                       f"({t.get('login_name')}, {t.get('program_name')})\n")
            if t.get('query_text'):
                report += f"    SQL: {str(t['query_text'])[:100]}\n"

    return report


# ============================================================================
# SECTION 14: ACTIVE SESSIONS & CURRENTLY RUNNING QUERIES
# ============================================================================
def analyze_active_sessions(conn):
    report = section_header("14. ACTIVE SESSIONS & RUNNING QUERIES")

    sessions = run_query(conn, """
        SELECT
            s.session_id,
            s.login_name,
            s.host_name,
            s.program_name,
            s.status,
            s.cpu_time,
            s.memory_usage * 8 AS memory_kb,
            s.reads,
            s.writes,
            s.logical_reads,
            s.last_request_start_time,
            r.command,
            r.wait_type,
            r.wait_time,
            r.percent_complete,
            r.estimated_completion_time / 1000 AS est_completion_sec,
            SUBSTRING(st.text, (r.statement_start_offset/2)+1,
                ((CASE r.statement_end_offset
                    WHEN -1 THEN DATALENGTH(st.text)
                    ELSE r.statement_end_offset
                END - r.statement_start_offset)/2) + 1) AS current_query
        FROM sys.dm_exec_sessions s
        LEFT JOIN sys.dm_exec_requests r ON s.session_id = r.session_id
        OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) st
        WHERE s.session_id > 50
          AND s.status != 'sleeping'
        ORDER BY s.cpu_time DESC
    """)
    report += sub_header("Active (Non-Sleeping) Sessions")
    if sessions:
        for s in sessions:
            report += (f"  Session {s.get('session_id')}: {s.get('login_name')}@{s.get('host_name')} "
                       f"[{s.get('status')}] CPU: {fmt_num(s.get('cpu_time'))}ms  "
                       f"Reads: {fmt_num(s.get('logical_reads'))}\n")
            if s.get('command'):
                report += f"    Command: {s.get('command')}"
                if s.get('percent_complete') and s['percent_complete'] > 0:
                    report += f" ({s['percent_complete']:.1f}% complete, ~{fmt_num(s.get('est_completion_sec'))}s remaining)"
                report += "\n"
            if s.get('wait_type'):
                report += f"    Waiting: {s['wait_type']} ({fmt_num(s.get('wait_time'))}ms)\n"
            if s.get('current_query'):
                report += f"    Query: {str(s['current_query']).replace(chr(10), ' ')[:120]}\n"
            report += "\n"
    else:
        report += "  No active queries running ✓\n"

    # Session count summary
    session_summary = run_query(conn, """
        SELECT
            status,
            COUNT(*) AS cnt,
            SUM(cpu_time) AS total_cpu,
            SUM(logical_reads) AS total_reads
        FROM sys.dm_exec_sessions
        WHERE session_id > 50
        GROUP BY status
        ORDER BY COUNT(*) DESC
    """)
    report += sub_header("Session Summary")
    for s in session_summary:
        report += (f"  {str(s.get('status', '')):<15s}: {s.get('cnt'):>5d} sessions, "
                   f"CPU: {fmt_num(s.get('total_cpu'))}ms, "
                   f"Reads: {fmt_num(s.get('total_reads'))}\n")

    return report


# ============================================================================
# SECTION 15: DATABASE HEALTH CHECKS
# ============================================================================
def analyze_db_health(conn):
    report = section_header("15. DATABASE HEALTH CHECKS")

    # Last DBCC CHECKDB
    report += sub_header("Last Integrity Check (DBCC CHECKDB)")
    checkdb = run_query(conn, """
        DBCC DBINFO('EDS') WITH TABLERESULTS, NO_INFOMSGS
    """)
    if checkdb:
        for row in checkdb:
            if row.get('Field') == 'dbi_dbccLastKnownGood':
                val = row.get('Value', 'Unknown')
                report += f"  Last known good CHECKDB: {val}\n"

    # Auto-grow events
    autogrow = run_query(conn, """
        DECLARE @filename NVARCHAR(1000);
        SELECT @filename = CAST(value AS NVARCHAR(1000))
        FROM sys.fn_trace_getinfo(DEFAULT)
        WHERE traceid = 1 AND property = 2;

        IF @filename IS NOT NULL
        BEGIN
            SELECT TOP 20
                te.name AS event_name,
                t.DatabaseName,
                t.FileName,
                t.StartTime,
                t.Duration / 1000 AS duration_ms,
                t.IntegerData * 8 / 1024 AS growth_mb
            FROM sys.fn_trace_gettable(@filename, DEFAULT) t
            JOIN sys.trace_events te ON t.EventClass = te.trace_event_id
            WHERE te.name LIKE '%Auto%Grow%'
              AND t.DatabaseName = 'EDS'
            ORDER BY t.StartTime DESC;
        END
    """)
    report += sub_header("Recent Auto-Grow Events")
    if autogrow and not any('ERROR' in str(e) for e in autogrow):
        for a in autogrow:
            report += (f"  {a.get('StartTime')}: {a.get('event_name')} - "
                       f"{a.get('FileName')} grew {fmt_num(a.get('growth_mb'))} MB "
                       f"(took {fmt_num(a.get('duration_ms'))}ms)\n")
    else:
        report += "  (No auto-grow events found or trace not available)\n"

    # Statistics freshness
    stale_stats = run_query(conn, """
        SELECT TOP 20
            OBJECT_NAME(s.object_id) AS table_name,
            s.name AS stat_name,
            sp.last_updated,
            sp.rows,
            sp.rows_sampled,
            sp.modification_counter,
            CASE WHEN sp.rows > 0
                THEN CAST(100.0 * sp.modification_counter / sp.rows AS DECIMAL(10,2))
                ELSE 0
            END AS pct_modified
        FROM sys.stats s
        CROSS APPLY sys.dm_db_stats_properties(s.object_id, s.stats_id) sp
        WHERE sp.modification_counter > 1000
          AND OBJECTPROPERTY(s.object_id, 'IsUserTable') = 1
        ORDER BY sp.modification_counter DESC
    """)
    report += sub_header("Stale Statistics (>1000 modifications)")
    report += f"  {'Table':<35s} {'Stat Name':<30s} {'Rows':>12s} {'Modifications':>14s} {'%Modified':>10s} {'Last Updated'}\n"
    report += f"  {'─'*35} {'─'*30} {'─'*12} {'─'*14} {'─'*10} {'─'*22}\n"
    for s in stale_stats:
        flag = " ⚠" if (s.get('pct_modified') or 0) > 20 else ""
        report += (f"  {str(s.get('table_name', '')):<35s} "
                   f"{str(s.get('stat_name', '')):<30s} "
                   f"{fmt_num(s.get('rows')):>12s} "
                   f"{fmt_num(s.get('modification_counter')):>14s} "
                   f"{fmt_pct(s.get('pct_modified')):>10s} "
                   f"{s.get('last_updated')}{flag}\n")

    # VLF count
    vlf = run_query(conn, "DBCC LOGINFO WITH NO_INFOMSGS")
    if vlf:
        report += sub_header("Virtual Log Files (VLF)")
        report += f"  VLF Count: {len(vlf)}"
        if len(vlf) > 100:
            report += "  ⚠ HIGH - Consider shrinking and pre-sizing log file"
        report += "\n"

    return report


# ============================================================================
# SECTION 16: EDS-SPECIFIC KNOWN ISSUE CHECKS
# ============================================================================
def analyze_eds_known_issues(conn):
    report = section_header("16. EDS-SPECIFIC KNOWN ISSUE CHECKS")

    # KI-001: usp_GetIndexData
    report += sub_header("KI-001: usp_GetIndexData Performance")
    ki001 = run_query(conn, """
        SELECT
            execution_count,
            total_worker_time / 1000 AS total_cpu_ms,
            total_elapsed_time / 1000 AS total_elapsed_ms,
            total_elapsed_time / execution_count / 1000 AS avg_elapsed_ms,
            max_elapsed_time / 1000 AS max_elapsed_ms,
            total_logical_reads,
            total_logical_reads / execution_count AS avg_reads,
            last_execution_time,
            cached_time
        FROM sys.dm_exec_procedure_stats
        WHERE object_id = OBJECT_ID('usp_GetIndexData')
    """)
    if ki001:
        k = ki001[0]
        report += f"  Executions:     {fmt_num(k.get('execution_count'))}\n"
        report += f"  Total CPU:      {fmt_num(k.get('total_cpu_ms'))} ms\n"
        report += f"  Avg Elapsed:    {fmt_num(k.get('avg_elapsed_ms'))} ms"
        if (k.get('avg_elapsed_ms') or 0) > 60000:
            report += "  ⚠ EXCEEDS 1 MINUTE"
        report += f"\n  Max Elapsed:    {fmt_num(k.get('max_elapsed_ms'))} ms\n"
        report += f"  Avg Reads:      {fmt_num(k.get('avg_reads'))}\n"
        report += f"  Last Exec:      {k.get('last_execution_time')}\n"
    else:
        report += "  (Not in plan cache - may not have run recently)\n"

    # KI-002: Vendor sync frequency
    report += sub_header("KI-002: Vendor Sync Job Activity")
    ki002 = run_query(conn, """
        SELECT
            execution_count,
            total_elapsed_time / 1000 AS total_elapsed_ms,
            total_elapsed_time / execution_count / 1000 AS avg_elapsed_ms,
            last_execution_time
        FROM sys.dm_exec_procedure_stats
        WHERE OBJECT_NAME(object_id) LIKE '%Vendor%Sync%'
           OR OBJECT_NAME(object_id) LIKE '%VendorCategory%'
    """)
    if ki002:
        for v in ki002:
            report += f"  Executions: {fmt_num(v.get('execution_count'))}, Avg: {fmt_num(v.get('avg_elapsed_ms'))}ms, Last: {v.get('last_execution_time')}\n"
    else:
        report += "  (No vendor sync procedures found in cache)\n"

    # KI-003: trig_DetailUpdate blocking check
    report += sub_header("KI-003: Detail Table & Trigger Blocking")
    ki003 = run_query(conn, """
        SELECT
            OBJECT_NAME(object_id) AS table_name,
            index_id,
            row_lock_count, row_lock_wait_count,
            row_lock_wait_in_ms,
            page_lock_count, page_lock_wait_count,
            page_lock_wait_in_ms,
            page_lock_escalation_count
        FROM sys.dm_db_index_operational_stats(DB_ID(), OBJECT_ID('Detail'), NULL, NULL)
        WHERE row_lock_wait_count > 0 OR page_lock_wait_count > 0
    """)
    if ki003:
        for k in ki003:
            report += f"  Detail index {k.get('index_id')}:\n"
            report += f"    Row Locks:  {fmt_num(k.get('row_lock_count'))}, Waits: {fmt_num(k.get('row_lock_wait_count'))} ({fmt_num(k.get('row_lock_wait_in_ms'))}ms)\n"
            report += f"    Page Locks: {fmt_num(k.get('page_lock_count'))}, Waits: {fmt_num(k.get('page_lock_wait_count'))} ({fmt_num(k.get('page_lock_wait_in_ms'))}ms)\n"
            if (k.get('page_lock_escalation_count') or 0) > 0:
                report += f"    ⚠ Lock Escalations: {fmt_num(k.get('page_lock_escalation_count'))}\n"
    else:
        report += "  No lock contention data for Detail table\n"

    # KI-004: CrossRefs table stats
    report += sub_header("KI-004: CrossRefs Table Lock Contention")
    ki004 = run_query(conn, """
        SELECT
            index_id,
            row_lock_count, row_lock_wait_count, row_lock_wait_in_ms,
            page_lock_count, page_lock_wait_count, page_lock_wait_in_ms
        FROM sys.dm_db_index_operational_stats(DB_ID(), OBJECT_ID('CrossRefs'), NULL, NULL)
        WHERE row_lock_wait_count > 0 OR page_lock_wait_count > 0
    """)
    if ki004:
        for k in ki004:
            report += f"  CrossRefs index {k.get('index_id')}: Row waits: {fmt_num(k.get('row_lock_wait_count'))} ({fmt_num(k.get('row_lock_wait_in_ms'))}ms), Page waits: {fmt_num(k.get('page_lock_wait_count'))} ({fmt_num(k.get('page_lock_wait_in_ms'))}ms)\n"
    else:
        report += "  No lock contention data for CrossRefs\n"

    # KI-005: Users table - SSO deadlock potential
    report += sub_header("KI-005: Users Table Lock Contention (SSO Deadlocks)")
    ki005 = run_query(conn, """
        SELECT
            index_id,
            row_lock_count, row_lock_wait_count, row_lock_wait_in_ms,
            page_lock_count, page_lock_wait_count, page_lock_wait_in_ms
        FROM sys.dm_db_index_operational_stats(DB_ID(), OBJECT_ID('Users'), NULL, NULL)
        WHERE row_lock_wait_count > 0 OR page_lock_wait_count > 0
    """)
    if ki005:
        for k in ki005:
            report += f"  Users index {k.get('index_id')}: Row waits: {fmt_num(k.get('row_lock_wait_count'))} ({fmt_num(k.get('row_lock_wait_in_ms'))}ms), Page waits: {fmt_num(k.get('page_lock_wait_count'))} ({fmt_num(k.get('page_lock_wait_in_ms'))}ms)\n"
    else:
        report += "  No lock contention data for Users table\n"

    # Check for missing indexes on known problem tables
    report += sub_header("Missing Indexes on Known Problem Tables")
    eds_missing = run_query(conn, """
        SELECT
            OBJECT_NAME(mid.object_id) AS table_name,
            mid.equality_columns,
            mid.inequality_columns,
            mid.included_columns,
            migs.avg_user_impact,
            migs.user_seeks
        FROM sys.dm_db_missing_index_groups mig
        JOIN sys.dm_db_missing_index_group_stats migs ON mig.index_group_handle = migs.group_handle
        JOIN sys.dm_db_missing_index_details mid ON mig.index_handle = mid.index_handle
        WHERE mid.database_id = DB_ID('EDS')
          AND OBJECT_NAME(mid.object_id) IN ('BidResults','CrossRefs','Detail','Users','PricingConsolidated','Items','BidMappedItems')
        ORDER BY migs.avg_user_impact * migs.user_seeks DESC
    """)
    if eds_missing:
        for m in eds_missing:
            report += f"  {m.get('table_name')}: Impact {fmt_pct(m.get('avg_user_impact'))}, Seeks: {fmt_num(m.get('user_seeks'))}\n"
            if m.get('equality_columns'):
                report += f"    EQ: {m['equality_columns']}\n"
            if m.get('inequality_columns'):
                report += f"    INEQ: {m['inequality_columns']}\n"
            if m.get('included_columns'):
                report += f"    INCLUDE: {m['included_columns']}\n"
    else:
        report += "  No missing index suggestions for known problem tables\n"

    # Check key table row counts
    report += sub_header("Key Table Row Counts")
    key_tables = run_query(conn, """
        SELECT
            t.name AS table_name,
            SUM(p.rows) AS row_count
        FROM sys.tables t
        JOIN sys.partitions p ON t.object_id = p.object_id AND p.index_id IN (0,1)
        WHERE t.name IN ('CrossRefs','BidResults','Detail','Items','Users',
                         'BidHeaderDetail','TransactionLog_HISTORY',
                         'OrderBookDetailOld','PricingConsolidated',
                         'BidMappedItems','VendorCategoryPP','ReportSessionLinks')
        GROUP BY t.name
        ORDER BY SUM(p.rows) DESC
    """)
    for k in key_tables:
        report += f"  {str(k.get('table_name', '')):<35s} {fmt_num(k.get('row_count')):>15s} rows\n"

    return report


# ============================================================================
# MAIN
# ============================================================================
def main():
    print("=" * 80)
    print("  EDS SQL SERVER COMPREHENSIVE PERFORMANCE ANALYSIS")
    print(f"  Server: {SERVER}")
    print(f"  Database: {DATABASE}")
    print(f"  Started: {datetime.datetime.now()}")
    print("=" * 80)

    conn = get_connection()
    full_report = ""
    full_report += f"EDS SQL SERVER COMPREHENSIVE PERFORMANCE ANALYSIS\n"
    full_report += f"Server: {SERVER}\n"
    full_report += f"Database: {DATABASE}\n"
    full_report += f"Generated: {datetime.datetime.now()}\n"

    sections = [
        ("Server Configuration & Health", analyze_server_config),
        ("Wait Statistics", analyze_wait_stats),
        ("CPU Analysis", analyze_cpu),
        ("Memory Analysis", analyze_memory),
        ("I/O Analysis", analyze_io),
        ("Top Queries", analyze_top_queries),
        ("Plan Cache", analyze_plan_cache),
        ("Index Analysis", analyze_indexes),
        ("Blocking & Deadlocks", analyze_blocking),
        ("Storage Analysis", analyze_storage),
        ("Stored Procedures", analyze_procedures),
        ("Trigger Analysis", analyze_triggers),
        ("TempDB Analysis", analyze_tempdb),
        ("Active Sessions", analyze_active_sessions),
        ("Database Health", analyze_db_health),
        ("EDS Known Issues", analyze_eds_known_issues),
    ]

    for name, func in sections:
        print(f"\n  Analyzing: {name}...")
        try:
            result = func(conn)
            full_report += result
            print(f"  ✓ {name} complete")
        except Exception as e:
            error_msg = f"\n  ✗ ERROR in {name}: {e}\n"
            print(error_msg)
            full_report += section_header(f"{name} - ERROR")
            full_report += f"  Error: {e}\n"

    conn.close()

    # Save report
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = os.path.join(OUTPUT_DIR, f"performance_analysis_{timestamp}.txt")
    with open(report_file, 'w', encoding='utf-8') as f:
        f.write(full_report)

    print(f"\n{'='*80}")
    print(f"  ANALYSIS COMPLETE")
    print(f"  Report saved to: {report_file}")
    print(f"  Report size: {len(full_report):,} characters")
    print(f"{'='*80}")

    return report_file


if __name__ == '__main__':
    main()
