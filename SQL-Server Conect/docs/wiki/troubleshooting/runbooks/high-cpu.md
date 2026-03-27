# Emergency Runbook: High CPU

[Home](../../index.md) > [Troubleshooting](../index.md) > [Runbooks](./) > High CPU

---

## Purpose

This runbook provides step-by-step procedures for responding to high CPU utilization on the database server.

---

## Severity Criteria

| Severity | CPU % | Duration | Response |
|----------|-------|----------|----------|
| **Critical** | > 95% | > 5 min | Immediate |
| **High** | > 80% | > 10 min | < 15 min |
| **Medium** | > 70% | > 30 min | < 1 hour |

---

## Immediate Actions (First 5 Minutes)

### Step 1: Confirm CPU Status

```sql
-- Current CPU utilization
SELECT
    record_id,
    DATEADD(ms, -1 * (sys.ms_ticks - record.timestamp), GETDATE()) AS EventTime,
    SQLProcessUtilization AS SQL_CPU,
    100 - SystemIdle - SQLProcessUtilization AS Other_CPU,
    SystemIdle AS Idle_CPU
FROM (
    SELECT record.value('(./Record/@id)[1]', 'int') AS record_id,
           record.value('(./Record/SchedulerMonitorEvent/SystemHealth/SystemIdle)[1]', 'int') AS SystemIdle,
           record.value('(./Record/SchedulerMonitorEvent/SystemHealth/ProcessUtilization)[1]', 'int') AS SQLProcessUtilization,
           timestamp
    FROM (
        SELECT timestamp, CONVERT(XML, record) AS record
        FROM sys.dm_os_ring_buffers
        WHERE ring_buffer_type = N'RING_BUFFER_SCHEDULER_MONITOR'
          AND record LIKE '%<SystemHealth>%'
    ) AS x
) AS y
CROSS JOIN sys.dm_os_sys_info sys
ORDER BY record_id DESC
```

### Step 2: Find CPU-Heavy Queries

```sql
-- Currently executing queries by CPU
SELECT TOP 10
    req.session_id,
    req.status,
    req.cpu_time,
    req.total_elapsed_time / 1000 as ElapsedSeconds,
    req.reads,
    req.writes,
    SUBSTRING(qt.text, (req.statement_start_offset/2)+1,
        ((CASE req.statement_end_offset
            WHEN -1 THEN DATALENGTH(qt.text)
            ELSE req.statement_end_offset
        END - req.statement_start_offset)/2)+1) as QueryText,
    sess.login_name,
    sess.host_name,
    sess.program_name
FROM sys.dm_exec_requests req
JOIN sys.dm_exec_sessions sess ON req.session_id = sess.session_id
CROSS APPLY sys.dm_exec_sql_text(req.sql_handle) qt
WHERE req.session_id > 50
ORDER BY req.cpu_time DESC
```

### Step 3: Check for Parallelism Issues

```sql
-- Queries with high parallelism
SELECT
    req.session_id,
    req.parallel_worker_count,
    req.dop,
    qt.text as QueryText
FROM sys.dm_exec_requests req
CROSS APPLY sys.dm_exec_sql_text(req.sql_handle) qt
WHERE req.parallel_worker_count > 4
ORDER BY req.parallel_worker_count DESC
```

---

## Root Cause Analysis

### Common CPU Causes

| Cause | Indicators | Solution |
|-------|------------|----------|
| Runaway Query | Single query high CPU | Kill or optimize |
| Missing Index | Table scans | Add index |
| Parameter Sniffing | Variable execution times | Recompile |
| Parallelism | Many workers | Adjust MAXDOP |
| Compilation | High compile waits | Plan caching |
| Hash/Sort | Memory spills | Memory grant |

### Check Historical CPU Usage

```sql
-- From DPA tables
SELECT DATEHOUR,
       SUM(CPUTIMESECS) / 60.0 as CPUMinutes,
       COUNT(DISTINCT DIMENSIONID) as UniqueQueries
FROM CON_SQL_SUM_1
WHERE DATEHOUR > DATEADD(hour, -24, GETDATE())
GROUP BY DATEHOUR
ORDER BY DATEHOUR DESC
```

---

## Resolution Options

### Option A: Kill High-CPU Query

**When to use:**
- Single query consuming most CPU
- Query is stuck or runaway
- Can be safely terminated

```sql
-- Verify the session
SELECT session_id, status, cpu_time, start_time
FROM sys.dm_exec_requests
WHERE session_id = @SessionId

-- Kill if appropriate
KILL @SessionId
```

### Option B: Force Query Recompile

**When to use:**
- Bad execution plan (parameter sniffing)
- Query has multiple plans

```sql
-- Clear plan for specific query
DBCC FREEPROCCACHE(@plan_handle)

-- Clear all plans (last resort)
DBCC FREEPROCCACHE
```

### Option C: Limit Parallelism

**When to use:**
- Excessive parallel workers
- Contention on CXPACKET waits

```sql
-- Check current setting
SELECT name, value_in_use
FROM sys.configurations
WHERE name = 'max degree of parallelism'

-- Temporarily reduce (requires sysadmin)
EXEC sp_configure 'max degree of parallelism', 4
RECONFIGURE
```

### Option D: Add Missing Index

**When to use:**
- Table scans visible in plan
- Missing index recommendation

```sql
-- Quick index creation
CREATE INDEX IX_Table_Column
ON Table (Column)
WITH (ONLINE = ON)  -- Minimize blocking
```

---

## Preventive Measures

### 1. Resource Governor

Limit CPU for specific workloads:
```sql
-- Create resource pool with CPU limit
CREATE RESOURCE POOL PoolName WITH (
    MIN_CPU_PERCENT = 0,
    MAX_CPU_PERCENT = 50
)
```

### 2. Query Store

Force good plans:
```sql
-- Enable Query Store
ALTER DATABASE EDS SET QUERY_STORE = ON

-- Force a specific plan
EXEC sp_query_store_force_plan @query_id, @plan_id
```

### 3. Index Maintenance

Prevent CPU spikes from bad plans:
```sql
-- Update statistics
UPDATE STATISTICS TableName

-- Rebuild fragmented indexes
ALTER INDEX IndexName ON TableName REBUILD
```

---

## Monitoring

### Alert Thresholds

| Metric | Warning | Critical |
|--------|---------|----------|
| CPU % | > 70% sustained | > 90% sustained |
| Batch requests/sec | > 5000 | > 10000 |
| Compilations/sec | > 100 | > 500 |

### Key DMVs

| DMV | Purpose |
|-----|---------|
| sys.dm_os_schedulers | Scheduler status |
| sys.dm_exec_query_stats | Query CPU usage |
| sys.dm_os_wait_stats | Wait statistics |

---

## Communication Template

### To Affected Users
```
Subject: [STATUS] Database Performance Issue - High CPU

Current Status: [Investigating/Resolving/Resolved]
Start Time: [HH:MM]
Impact: Slower than normal response times
Actions: [Brief description]
ETA: [Expected resolution time]
```

---

## Known High-CPU Patterns

### usp_GetIndexData (KI-001)

- **Impact:** Can run for 24+ hours
- **Pattern:** Multiple execution plans (19 variants)
- **Solution:** Force good plan, add OPTIMIZE FOR hint

See [KI-001](../../performance/known-issues/usp-getindexdata.md)

### Vendor Sync Job (KI-002)

- **Impact:** Runs hourly, unnecessary CPU usage
- **Pattern:** Full table scans for sync check
- **Solution:** Reduce frequency, add delta logic

See [KI-002](../../performance/known-issues/vendor-sync-job.md)

---

## Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│                 HIGH CPU QUICK REFERENCE                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. CONFIRM: Is CPU actually high? (> 80% sustained)        │
│                                                             │
│  2. IDENTIFY: Which query is using CPU?                     │
│     SELECT TOP 5 session_id, cpu_time, text                 │
│     FROM sys.dm_exec_requests                               │
│     CROSS APPLY sys.dm_exec_sql_text(sql_handle)            │
│     ORDER BY cpu_time DESC                                  │
│                                                             │
│  3. DECIDE:                                                 │
│     - Kill: Runaway query                                   │
│     - Recompile: Bad plan                                   │
│     - Index: Missing index causing scan                     │
│     - Wait: Legitimate operation                            │
│                                                             │
│  4. DOCUMENT: Time, actions, outcome                        │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## See Also

- [Slow Queries](../slow-queries.md)
- [Blocking Emergency](blocking-emergency.md)
- [Performance Overview](../../performance/index.md)

