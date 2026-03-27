# Troubleshooting: Blocking

[Home](../index.md) > [Troubleshooting](index.md) > Blocking

---

## Overview

Blocking occurs when one session holds a lock that another session needs. This guide helps diagnose and resolve blocking issues.

---

## Symptoms

- Users report "hanging" or "frozen" applications
- Operations timeout
- DPA shows high wait times
- Queries waiting on LCK_* wait types

---

## Diagnostic Steps

### Step 1: Identify Current Blocking

```sql
-- Current blocking chains
SELECT
    blocking.session_id as BlockerSPID,
    blocked.session_id as BlockedSPID,
    blocked.wait_type,
    blocked.wait_time / 1000 as WaitSeconds,
    blocked.wait_resource,
    blocker_text.text as BlockerQuery,
    blocked_text.text as BlockedQuery
FROM sys.dm_exec_requests blocked
JOIN sys.dm_exec_requests blocking ON blocked.blocking_session_id = blocking.session_id
CROSS APPLY sys.dm_exec_sql_text(blocking.sql_handle) blocker_text
CROSS APPLY sys.dm_exec_sql_text(blocked.sql_handle) blocked_text
WHERE blocked.blocking_session_id > 0
ORDER BY blocked.wait_time DESC
```

### Step 2: Find the Head Blocker

```sql
-- Head of blocking chain
WITH BlockingChain AS (
    SELECT session_id,
           blocking_session_id,
           wait_type,
           wait_time,
           1 as Level
    FROM sys.dm_exec_requests
    WHERE blocking_session_id = 0
      AND session_id IN (SELECT blocking_session_id FROM sys.dm_exec_requests WHERE blocking_session_id > 0)

    UNION ALL

    SELECT r.session_id,
           r.blocking_session_id,
           r.wait_type,
           r.wait_time,
           bc.Level + 1
    FROM sys.dm_exec_requests r
    JOIN BlockingChain bc ON r.blocking_session_id = bc.session_id
)
SELECT * FROM BlockingChain
ORDER BY Level, session_id
```

### Step 3: Get Blocker Details

```sql
-- Detailed info on blocking session
SELECT
    s.session_id,
    s.login_name,
    s.host_name,
    s.program_name,
    r.start_time,
    r.status,
    r.command,
    r.wait_type,
    r.wait_time,
    t.text as CurrentQuery,
    qp.query_plan
FROM sys.dm_exec_sessions s
LEFT JOIN sys.dm_exec_requests r ON s.session_id = r.session_id
OUTER APPLY sys.dm_exec_sql_text(r.sql_handle) t
OUTER APPLY sys.dm_exec_query_plan(r.plan_handle) qp
WHERE s.session_id = @BlockerSPID
```

---

## Common Blocking Patterns

### 1. Long-Running Transaction

**Cause:** Transaction open but not committed

**Identify:**
```sql
SELECT s.session_id, s.login_name, s.host_name,
       t.transaction_begin_time,
       DATEDIFF(minute, t.transaction_begin_time, GETDATE()) as OpenMinutes
FROM sys.dm_tran_active_transactions t
JOIN sys.dm_tran_session_transactions st ON t.transaction_id = st.transaction_id
JOIN sys.dm_exec_sessions s ON st.session_id = s.session_id
WHERE t.transaction_begin_time < DATEADD(minute, -5, GETDATE())
```

**Resolution:** Commit, rollback, or kill session

### 2. Trigger Blocking (KI-003)

**Cause:** `trig_DetailUpdate` holds locks during bulk operations

**Pattern:**
```
Bulk INSERT to Detail table
    → trig_DetailUpdate fires
        → Holds locks on Detail, Items, CrossRefs
            → Blocks other queries
```

**Resolution:** See [KI-003](../performance/known-issues/trigger-blocking.md)

### 3. Lock Escalation

**Cause:** Row locks escalate to page/table locks

**Identify:**
```sql
-- Check for escalation events
SELECT *
FROM sys.dm_exec_query_stats qs
CROSS APPLY sys.dm_exec_sql_text(qs.sql_handle) qt
WHERE qt.text LIKE '%UPDATE%'  -- or your suspected query
ORDER BY qs.total_elapsed_time DESC
```

**Resolution:**
- Process in smaller batches
- Use ROWLOCK hint
- Disable lock escalation (carefully)

### 4. Missing Index

**Cause:** Scan acquires more locks than seek

**Resolution:** Add appropriate index

---

## Historical Blocking Analysis

### Using DPA Tables

```sql
-- Blocking by hour (last 7 days)
SELECT DATEHOUR,
       SUM(BLERTIMESECS) / 60.0 as BlockerMinutes,
       SUM(BLEETIMESECS) / 60.0 as BlockedMinutes
FROM CON_BLOCKING_SUM_1
WHERE DATEHOUR > DATEADD(day, -7, GETDATE())
GROUP BY DATEHOUR
HAVING SUM(BLEETIMESECS) > 60
ORDER BY DATEHOUR DESC
```

### Top Blocking Queries

```sql
-- Top blockers
SELECT c.SQLTEXT,
       SUM(bs.BLERTIMESECS) / 60.0 as BlockerMinutes
FROM CON_BLOCKING_SUM_1 bs
JOIN CONST_1 c ON bs.DIMENSIONID = c.H
WHERE bs.DIMENSIONTYPE = 'S'
  AND bs.DATEHOUR > DATEADD(day, -7, GETDATE())
GROUP BY c.SQLTEXT
ORDER BY BlockerMinutes DESC
```

---

## Resolution Options

### Option 1: Wait It Out
If the blocker is legitimate and will finish soon, wait.

### Option 2: Kill the Blocker
```sql
-- Kill session (use carefully!)
KILL @SessionId

-- Kill with rollback
KILL @SessionId WITH STATUSONLY  -- Check status first
```

**Warning:** Killing may cause:
- Transaction rollback (could take time)
- Data inconsistency if mid-transaction
- Application errors

### Option 3: Optimize the Query
- Add indexes
- Use NOLOCK for reads
- Process in smaller batches

### Option 4: Reduce Lock Duration
- Shorter transactions
- Move non-critical operations outside transaction
- Use READ COMMITTED SNAPSHOT

---

## Prevention Strategies

### 1. Index Optimization
Proper indexes reduce lock duration:
```sql
-- Covering index for common queries
CREATE INDEX IX_Table_Covering
ON Table (FilterColumn)
INCLUDE (SelectColumns)
```

### 2. Query Hints
```sql
-- For read-only queries
SELECT * FROM Table WITH (NOLOCK)

-- Force row-level locking
UPDATE Table WITH (ROWLOCK)
SET Column = Value
WHERE Condition
```

### 3. Batch Processing
```sql
-- Instead of one large operation
WHILE EXISTS (SELECT 1 FROM Table WHERE Condition)
BEGIN
    UPDATE TOP (1000) Table
    SET ...
    WHERE Condition

    -- Brief pause to allow other queries
    WAITFOR DELAY '00:00:00.100'
END
```

### 4. Transaction Management
- Keep transactions short
- Don't hold transactions open during user interaction
- Use appropriate isolation level

---

## Known Blocking Issues

| Issue | Impact | Documentation |
|-------|--------|---------------|
| trig_DetailUpdate | 82+ min/incident | [KI-003](../performance/known-issues/trigger-blocking.md) |
| CrossRef lookups | 12+ hrs blocked | [KI-004](../performance/known-issues/crossref-blocking.md) |
| Jan 6 Incident | 767 min total | [Incident Report](../performance/incidents/2026-01-06-blocking.md) |

---

## Monitoring

### Alert Thresholds
| Metric | Warning | Critical |
|--------|---------|----------|
| Blocking Duration | > 5 min | > 10 min |
| Blocked Sessions | > 5 | > 10 |
| Block Chain Depth | > 3 | > 5 |

### DPA Dashboard
- Real-time blocking visualization
- Historical trends
- Alert configuration

---

## See Also

- [Blocking Emergency Runbook](runbooks/blocking-emergency.md)
- [Deadlocks](deadlocks.md) - When blocking becomes circular
- [Known Issues](../performance/known-issues/index.md)

