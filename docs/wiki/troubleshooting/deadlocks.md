# Troubleshooting: Deadlocks

[Home](../index.md) > [Troubleshooting](index.md) > Deadlocks

---

## Overview

A deadlock occurs when two or more sessions are waiting for each other in a circular dependency. SQL Server automatically detects deadlocks and terminates one session (the "victim") to break the cycle.

---

## Symptoms

- Application receives error 1205: "Transaction was deadlocked"
- One transaction is rolled back unexpectedly
- DPA shows deadlock events

---

## Diagnostic Steps

### Step 1: Check Recent Deadlocks

```sql
-- From DPA tables
SELECT TOP 10
    ID,
    D as DeadlockTime,
    SESSION_COUNT,
    VICTIM_SUM_MS / 1000.0 as VictimTimeSeconds
FROM CON_DEADLOCK_1
ORDER BY D DESC
```

### Step 2: Get Deadlock Details

```sql
-- Detailed deadlock information
SELECT
    dd.DEADLOCK_ID,
    dd.PIECE,
    dd.DETAIL
FROM CON_DEADLOCK_DETAIL_1 dd
WHERE dd.DEADLOCK_ID = @DeadlockId
ORDER BY dd.PIECE
```

### Step 3: Analyze the Deadlock Graph

The deadlock graph shows:
- Sessions involved
- Resources each holds
- Resources each is waiting for
- Which session was chosen as victim

```
Session A                    Session B
    │                            │
    │ Holds: PAGE 178975         │ Holds: PAGE 999246
    │ Wants: PAGE 999246         │ Wants: PAGE 178975
    │                            │
    └────────────────────────────┘
              DEADLOCK!
```

---

## Common Deadlock Patterns

### 1. SSO User Updates (KI-005)

**Pattern:** Multiple parallel updates to Users table

**Cause:**
- Same Kubernetes pod fires parallel SSO updates
- Each updates different user by Email
- Page-level locking conflicts

**Solution:** Serialize updates or add unique index on Email

See [KI-005](../performance/known-issues/sso-deadlocks.md) for details.

### 2. Trigger Cascades

**Pattern:** Triggers updating multiple tables

**Cause:**
- Trigger A updates Table X and Y
- Trigger B updates Table Y and X
- Different lock acquisition order

**Solution:**
- Consistent lock ordering
- Minimize trigger scope
- Use ROWLOCK hints

### 3. Index Deadlocks

**Pattern:** Non-clustered index vs clustered index

**Cause:**
- Query 1: Reads via NC index, needs CI
- Query 2: Updates CI, needs NC index

**Solution:**
- Covering indexes to avoid lookups
- Index maintenance during low usage

---

## Deadlock Analysis

### From System Event Session

```sql
-- Enable deadlock collection (if not using DPA)
ALTER EVENT SESSION [system_health] ON SERVER
WITH (STARTUP_STATE = ON)

-- Query deadlock XML
SELECT XEvent.query('.') as DeadlockGraph
FROM (
    SELECT CAST(target_data as XML) as TargetData
    FROM sys.dm_xe_session_targets st
    JOIN sys.dm_xe_sessions s ON s.address = st.event_session_address
    WHERE s.name = 'system_health'
      AND st.target_name = 'ring_buffer'
) AS Data
CROSS APPLY TargetData.nodes('RingBufferTarget/event[@name="xml_deadlock_report"]') AS XEventData(XEvent)
```

### Key Elements in Deadlock Graph

| Element | Description |
|---------|-------------|
| process-list | Sessions involved |
| resource-list | Objects locked |
| owner-list | Who holds what |
| waiter-list | Who wants what |
| victim-process | Session that was killed |

---

## Resolution Strategies

### 1. Retry Logic (Application)

```java
// Java example
int maxRetries = 3;
for (int i = 0; i < maxRetries; i++) {
    try {
        executeTransaction();
        break;
    } catch (DeadlockException e) {
        if (i == maxRetries - 1) throw e;
        Thread.sleep(100 * (i + 1));  // Exponential backoff
    }
}
```

### 2. Serialize Operations

For operations that frequently deadlock:
```java
synchronized(lockObject) {
    executeOperation();
}
```

### 3. Consistent Lock Ordering

Always acquire locks in the same order:
```sql
-- Always update TableA before TableB
BEGIN TRANSACTION
UPDATE TableA SET ... WHERE ...
UPDATE TableB SET ... WHERE ...
COMMIT
```

### 4. Reduce Lock Scope

```sql
-- Use ROWLOCK hint
UPDATE Table WITH (ROWLOCK)
SET Column = Value
WHERE Id = @Id

-- Use appropriate index
-- (Row-level locking requires index seek, not scan)
```

### 5. Snapshot Isolation

For read operations:
```sql
-- Database setting
ALTER DATABASE EDS SET ALLOW_SNAPSHOT_ISOLATION ON
ALTER DATABASE EDS SET READ_COMMITTED_SNAPSHOT ON

-- Then reads don't block writes
```

---

## Known Deadlock Issues

### SSO Updates (KI-005)

| Metric | Value |
|--------|-------|
| Frequency | ~20/month |
| Sessions | 8-12 per deadlock |
| Victim Time | Up to 2.4M ms |
| Root Cause | Parallel updates, page locks |

**Recent Deadlocks (Jan 12, 2026):**
- ID 996: 8 sessions, 21 sec victim time
- ID 995: 12 sessions, 8 sec victim time
- ID 994: 12 sessions, 3 sec victim time

Three deadlocks within 7 seconds!

---

## Prevention

### 1. Index on Lookup Columns

```sql
-- Prevents page scans that cause page locks
CREATE UNIQUE INDEX IX_Users_Email_Active
ON Users (Email, Active)
WHERE Active = 1
```

### 2. Short Transactions

Keep transactions as short as possible:
```sql
-- Bad: Long transaction
BEGIN TRANSACTION
SELECT @data = ...  -- Read data
-- User interaction here
UPDATE ...          -- Update data
COMMIT

-- Good: Short transaction
SELECT @data = ...  -- Read outside transaction
-- User interaction
BEGIN TRANSACTION
UPDATE ...          -- Quick update
COMMIT
```

### 3. Appropriate Isolation Level

| Level | Behavior | Deadlock Risk |
|-------|----------|---------------|
| READ UNCOMMITTED | No locks | Lowest |
| READ COMMITTED | Locks released early | Low |
| READ COMMITTED SNAPSHOT | No read locks | Lowest |
| REPEATABLE READ | Holds locks | Medium |
| SERIALIZABLE | Range locks | Highest |

---

## Monitoring

### Alert Configuration

| Metric | Threshold | Action |
|--------|-----------|--------|
| Deadlocks/hour | > 5 | Investigate |
| Sessions in deadlock | > 5 | Alert |
| Victim time | > 60 sec | Investigate |

### DPA Deadlock Monitoring

```sql
-- Deadlock trend
SELECT CAST(D as DATE) as DeadlockDate,
       COUNT(*) as DeadlockCount,
       SUM(SESSION_COUNT) as TotalSessions,
       SUM(VICTIM_SUM_MS) / 1000.0 as TotalVictimSeconds
FROM CON_DEADLOCK_1
WHERE D > DATEADD(day, -30, GETDATE())
GROUP BY CAST(D as DATE)
ORDER BY DeadlockDate DESC
```

---

## See Also

- [SSO Deadlock Issue](../performance/known-issues/sso-deadlocks.md)
- [Blocking](blocking.md) - Blocking can lead to deadlocks
- [Performance Overview](../performance/index.md)

