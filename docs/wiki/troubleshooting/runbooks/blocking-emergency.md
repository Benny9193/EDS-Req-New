# Emergency Runbook: Blocking

[Home](../../index.md) > [Troubleshooting](../index.md) > [Runbooks](./) > Blocking Emergency

---

## Purpose

This runbook provides step-by-step procedures for responding to critical blocking events affecting multiple users.

---

## Severity Criteria

| Severity | Criteria | Response |
|----------|----------|----------|
| **Critical** | > 10 users blocked, > 10 min | Immediate |
| **High** | > 5 users blocked, > 5 min | < 15 min |
| **Medium** | 2-5 users blocked, > 5 min | < 1 hour |

---

## Immediate Actions (First 5 Minutes)

### Step 1: Assess Impact

```sql
-- Count blocked sessions
SELECT COUNT(*) as BlockedCount,
       MAX(wait_time) / 1000 as MaxWaitSeconds
FROM sys.dm_exec_requests
WHERE blocking_session_id > 0
```

**Decision Point:**
- < 5 blocked, < 5 min wait → Monitor, likely self-resolving
- ≥ 5 blocked OR > 5 min wait → Continue to Step 2

### Step 2: Identify Head Blocker

```sql
-- Find root blocker
SELECT
    blocking.session_id as BlockerSPID,
    blocking.login_name,
    blocking.host_name,
    blocking.program_name,
    blocking.status,
    blocking.command,
    blocker_text.text as BlockerQuery,
    COUNT(blocked.session_id) as BlockedSessionCount
FROM sys.dm_exec_sessions blocking
LEFT JOIN sys.dm_exec_requests blocked ON blocking.session_id = blocked.blocking_session_id
LEFT JOIN sys.dm_exec_requests blocking_req ON blocking.session_id = blocking_req.session_id
CROSS APPLY sys.dm_exec_sql_text(blocking_req.sql_handle) blocker_text
WHERE blocking.session_id IN (
    SELECT DISTINCT blocking_session_id
    FROM sys.dm_exec_requests
    WHERE blocking_session_id > 0
)
GROUP BY blocking.session_id, blocking.login_name, blocking.host_name,
         blocking.program_name, blocking.status, blocking.command, blocker_text.text
ORDER BY BlockedSessionCount DESC
```

### Step 3: Document Current State

Copy output from above queries. Record:
- Time of issue
- Blocker SPID
- Query being run
- Number of blocked sessions
- Business impact

---

## Resolution Options

### Option A: Wait for Completion

**When to use:**
- Blocker is legitimate business operation
- Expected to complete soon
- Impact is acceptable

**Actions:**
1. Monitor progress
2. Communicate to affected users
3. Document for post-incident review

### Option B: Kill the Blocker

**When to use:**
- Blocker is stuck or runaway
- Business impact is severe
- Blocker can be safely terminated

**Pre-Kill Checklist:**
- [ ] Is this a critical system process?
- [ ] Will killing cause data inconsistency?
- [ ] Can the operation be restarted?
- [ ] Is rollback acceptable?

**Execute Kill:**

```sql
-- Check session status first
SELECT session_id, status, open_transaction_count, transaction_isolation_level
FROM sys.dm_exec_sessions
WHERE session_id = @BlockerSPID

-- If safe, kill the session
KILL @BlockerSPID
```

**Post-Kill:**
1. Verify blocking resolved
2. Check for transaction rollback
3. Notify application team if needed

### Option C: Query Optimization

**When to use:**
- Recurring blocking pattern
- Same query/trigger causing issues
- Time to implement fix

**Actions:**
1. Identify problematic query
2. Add index or hint
3. Test in non-prod first

---

## Communication Template

### To Affected Users
```
Subject: [RESOLVED/ONGOING] Database Performance Issue

Status: [Investigating/Resolving/Resolved]
Start Time: [HH:MM]
Impact: [Description]
Actions Taken: [Summary]
Expected Resolution: [Time/Status]
```

### To Management
```
Incident Summary:
- Time: [Start] - [End]
- Duration: [X minutes]
- Impact: [N users, X operations affected]
- Root Cause: [Brief description]
- Resolution: [What was done]
- Prevention: [Follow-up actions]
```

---

## Post-Incident

### Immediate (Within 1 Hour)

1. Verify system is stable
2. Document timeline and actions
3. Initial communication to stakeholders

### Short-Term (Within 24 Hours)

1. Root cause analysis
2. Review blocking patterns
3. Identify prevention measures

### Long-Term (Within 1 Week)

1. Post-mortem document
2. Implement preventive measures
3. Update monitoring/alerts

---

## Known Blocking Triggers

| Trigger | Pattern | Reference |
|---------|---------|-----------|
| trig_DetailUpdate | Bulk requisition imports | [KI-003](../../performance/known-issues/trigger-blocking.md) |
| CrossRef lookups | Blocked by Detail triggers | [KI-004](../../performance/known-issues/crossref-blocking.md) |
| 22:00 batch jobs | Overlapping schedules | [Jan 6 Incident](../../performance/incidents/2026-01-06-blocking.md) |

---

## Escalation

### When to Escalate

- Blocking persists > 30 minutes
- Unable to identify blocker
- Kill causes further issues
- Requires application changes

### Escalation Path

1. **DBA Team Lead** - For complex database issues
2. **Application Team** - For application-level changes
3. **Infrastructure** - For server/network issues
4. **Management** - For business decisions

---

## Quick Reference

```
┌─────────────────────────────────────────────────────────────┐
│                 BLOCKING EMERGENCY QUICK REFERENCE           │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  1. ASSESS: How many blocked? How long?                     │
│                                                             │
│  2. IDENTIFY: Find head blocker (SPID, query, user)         │
│                                                             │
│  3. DECIDE:                                                 │
│     - Wait: Legitimate operation, will complete             │
│     - Kill: Stuck/runaway, safe to terminate                │
│     - Optimize: Add index, hint, or fix query               │
│                                                             │
│  4. DOCUMENT: Time, actions, outcome                        │
│                                                             │
│  5. FOLLOW UP: Root cause, prevention                       │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## See Also

- [Blocking Troubleshooting](../blocking.md)
- [High CPU Runbook](high-cpu.md)
- [Performance Overview](../../performance/index.md)

