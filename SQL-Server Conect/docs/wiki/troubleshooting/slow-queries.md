# Troubleshooting: Slow Queries

[Home](../index.md) > [Troubleshooting](index.md) > Slow Queries

---

## Overview

This guide helps diagnose and resolve slow query performance in EDS.

---

## Symptoms

- Users report slow page loads
- Specific operations take longer than expected
- Database CPU elevated
- High wait times in DPA

---

## Diagnostic Steps

### Step 1: Identify the Slow Query

#### Using DPA
1. Open DPA dashboard
2. Look at "Top SQL" by wait time
3. Click on query to see details
4. Note the SQL hash for tracking

#### Using DMVs
```sql
-- Top 10 queries by total elapsed time
SELECT TOP 10
    SUBSTRING(qt.text, (qs.statement_start_offset/2)+1,
        ((CASE qs.statement_end_offset
            WHEN -1 THEN DATALENGTH(qt.text)
            ELSE qs.statement_end_offset
        END - qs.statement_start_offset)/2)+1) as QueryText,
    qs.execution_count,
    qs.total_elapsed_time / 1000000.0 as TotalSeconds,
    qs.total_elapsed_time / qs.execution_count / 1000.0 as AvgMs,
    qs.total_logical_reads / qs.execution_count as AvgReads
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) qt
ORDER BY qs.total_elapsed_time DESC
```

### Step 2: Get Execution Plan

```sql
-- Get cached execution plan
SELECT qp.query_plan
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_query_plan(qs.plan_handle) qp
WHERE qs.sql_handle = @SqlHandle
```

Or use SSMS:
1. Enable "Include Actual Execution Plan"
2. Run the slow query
3. Review the plan tab

### Step 3: Analyze the Plan

Look for these red flags:

| Issue | Indicator | Solution |
|-------|-----------|----------|
| Table Scan | Scan operator on large table | Add index |
| Key Lookup | Excessive lookups | Covering index |
| Sort | Memory grant warning | Pre-sort with index |
| Hash Match | Large hash builds | Better join strategy |
| Parameter Sniffing | Plan recompile helps | OPTIMIZE FOR hint |
| Estimated vs Actual | Big difference | Update statistics |

---

## Common Slow Query Patterns

### 1. Missing Index

**Symptoms:**
- Table scan on large table
- High logical reads

**Solution:**
```sql
-- Check for missing indexes
SELECT
    migs.avg_total_user_cost * migs.avg_user_impact * (migs.user_seeks + migs.user_scans) as Impact,
    mid.statement as TableName,
    mid.equality_columns,
    mid.inequality_columns,
    mid.included_columns
FROM sys.dm_db_missing_index_group_stats migs
JOIN sys.dm_db_missing_index_groups mig ON migs.group_handle = mig.index_group_handle
JOIN sys.dm_db_missing_index_details mid ON mig.index_handle = mid.index_handle
ORDER BY Impact DESC
```

### 2. Parameter Sniffing

**Symptoms:**
- Query fast sometimes, slow other times
- Different execution plans for same query
- Like KI-001: usp_GetIndexData (19 execution plans!)

**Solution:**
```sql
-- Option 1: OPTIMIZE FOR UNKNOWN
EXEC sp_name @param WITH RECOMPILE

-- Option 2: Local variable
DECLARE @local = @param
SELECT ... WHERE col = @local

-- Option 3: Plan guide
```

### 3. Outdated Statistics

**Symptoms:**
- Estimated rows vastly different from actual
- Bad cardinality estimates

**Solution:**
```sql
-- Update statistics on table
UPDATE STATISTICS TableName

-- Update all statistics in database
EXEC sp_updatestats
```

### 4. Implicit Conversions

**Symptoms:**
- Index not used despite existing
- CONVERT_IMPLICIT in plan

**Solution:**
Fix data type mismatch:
```sql
-- Bad: nvarchar parameter vs varchar column
WHERE Column = @NVarcharParam

-- Good: Match types
WHERE Column = CAST(@NVarcharParam as VARCHAR(100))
```

---

## Known Slow Queries

### usp_GetIndexData (KI-001)
- **Impact:** 24+ hours execution
- **Cause:** Parameter sniffing, 19 execution plans
- **Solution:** See [KI-001](../performance/known-issues/usp-getindexdata.md)

### Vendor Sync Job (KI-002)
- **Impact:** 59+ hours wasted monthly
- **Cause:** Unnecessary hourly execution
- **Solution:** See [KI-002](../performance/known-issues/vendor-sync-job.md)

---

## Quick Fixes

### Kill Long-Running Query
```sql
-- Find the session
SELECT session_id, start_time, status, command, wait_type
FROM sys.dm_exec_requests
WHERE session_id > 50
  AND total_elapsed_time > 300000  -- > 5 minutes

-- Kill it (carefully!)
KILL @SessionId
```

### Force Recompile
```sql
-- Single execution
EXEC sp_name WITH RECOMPILE

-- Clear plan cache for query
DBCC FREEPROCCACHE(@plan_handle)
```

### Add NOLOCK (Read-Only Queries)
```sql
-- For display/report queries only
SELECT * FROM TableName WITH (NOLOCK)
WHERE ...
```
**Warning:** Can return dirty reads. Only use for non-critical display queries.

---

## Prevention

### Index Maintenance
```sql
-- Check fragmentation
SELECT object_name(ips.object_id) as TableName,
       i.name as IndexName,
       ips.avg_fragmentation_in_percent
FROM sys.dm_db_index_physical_stats(DB_ID(), NULL, NULL, NULL, 'LIMITED') ips
JOIN sys.indexes i ON ips.object_id = i.object_id AND ips.index_id = i.index_id
WHERE ips.avg_fragmentation_in_percent > 30
ORDER BY ips.avg_fragmentation_in_percent DESC
```

### Statistics Updates
```sql
-- Check stale statistics
SELECT object_name(s.object_id) as TableName,
       s.name as StatName,
       STATS_DATE(s.object_id, s.stats_id) as LastUpdated
FROM sys.stats s
WHERE STATS_DATE(s.object_id, s.stats_id) < DATEADD(day, -7, GETDATE())
ORDER BY LastUpdated
```

---

## Escalation

Escalate to DBA team if:
- Query still slow after basic optimization
- Requires schema changes
- Affects multiple users
- Running > 1 hour

---

## See Also

- [Blocking](blocking.md) - If slow due to blocking
- [Known Issues](../performance/known-issues/index.md) - Documented issues
- [Performance Overview](../performance/index.md)

