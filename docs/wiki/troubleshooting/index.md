# Troubleshooting Guide

[Home](../index.md) > Troubleshooting

---

## Overview

This section provides guidance for diagnosing and resolving common EDS database performance issues.

---

## Quick Links

| Issue Type | Guide | Urgency |
|------------|-------|---------|
| [Slow Queries](slow-queries.md) | Query performance issues | Medium |
| [Blocking](blocking.md) | Sessions waiting on locks | High |
| [Deadlocks](deadlocks.md) | Circular lock dependencies | High |
| [Runbooks](runbooks/) | Emergency procedures | Critical |

---

## Issue Triage

### Step 1: Identify the Problem Type

```
User reports "slow system"
         │
         ▼
    Check DPA Dashboard
         │
    ┌────┴────┬────────────┬────────────┐
    │         │            │            │
    ▼         ▼            ▼            ▼
Blocking?  Deadlocks?  Slow Query?   CPU High?
    │         │            │            │
    ▼         ▼            ▼            ▼
[blocking.md] [deadlocks.md] [slow-queries.md] [runbooks/high-cpu.md]
```

### Step 2: Check Current State

#### Active Sessions
```sql
SELECT session_id, status, command, blocking_session_id,
       wait_type, wait_time, cpu_time, logical_reads
FROM sys.dm_exec_requests
WHERE session_id > 50
ORDER BY cpu_time DESC
```

#### Current Blocking
```sql
SELECT blocking_session_id as Blocker,
       session_id as Blocked,
       wait_type, wait_time / 1000 as WaitSecs,
       wait_resource
FROM sys.dm_exec_requests
WHERE blocking_session_id > 0
ORDER BY wait_time DESC
```

#### Recent Deadlocks
```sql
SELECT TOP 5 ID, D as DeadlockTime, SESSION_COUNT, VICTIM_SUM_MS
FROM CON_DEADLOCK_1
ORDER BY D DESC
```

---

## Known Issues Reference

| ID | Issue | Priority | Status |
|----|-------|----------|--------|
| [KI-001](../performance/known-issues/usp-getindexdata.md) | usp_GetIndexData slow | P1 Critical | Active |
| [KI-002](../performance/known-issues/vendor-sync-job.md) | Vendor sync job | P2 High | Active |
| [KI-003](../performance/known-issues/trigger-blocking.md) | trig_DetailUpdate | P3 High | Active |
| [KI-004](../performance/known-issues/crossref-blocking.md) | CrossRef blocking | P4 Medium | Active |
| [KI-005](../performance/known-issues/sso-deadlocks.md) | SSO deadlocks | P5 Medium | Active |

---

## Emergency Contacts

| Role | Contact | Availability |
|------|---------|--------------|
| Primary DBA | DBA Team | Business hours |
| On-Call DBA | Pager/Phone | 24/7 |
| App Support | Dev Team | Business hours |
| Vendor Support | SolarWinds | Per contract |

---

## Diagnostic Tools

### DPA (SolarWinds Database Performance Analyzer)
- Real-time wait analysis
- Historical trending
- Blocking chain visualization
- Query plan analysis

### SQL Server DMVs
| DMV | Purpose |
|-----|---------|
| `sys.dm_exec_requests` | Active queries |
| `sys.dm_exec_sessions` | Session info |
| `sys.dm_exec_query_stats` | Query performance |
| `sys.dm_tran_locks` | Current locks |
| `sys.dm_os_wait_stats` | Wait statistics |

### DPA Tables Reference
| Table | Content |
|-------|---------|
| CON_SQL_SUM_1 | SQL execution statistics |
| CON_BLOCKING_SUM_1 | Blocking history |
| CON_DEADLOCK_1 | Deadlock events |
| CONU_1 | User activity |
| CONPR_1 | Program activity |

---

## Common Resolutions

### Quick Fixes

| Problem | Quick Fix |
|---------|-----------|
| Long-running query | Identify and kill if safe |
| Blocking chain | Kill head blocker (carefully) |
| High CPU | Find expensive query |
| Deadlock | Usually self-resolves |

### Requires Investigation

| Problem | Investigation Steps |
|---------|---------------------|
| Recurring slow query | Check execution plans |
| Frequent blocking | Analyze lock patterns |
| Periodic deadlocks | Review deadlock graph |
| Gradual degradation | Check index fragmentation |

---

## Escalation Matrix

| Severity | Response Time | Actions |
|----------|---------------|---------|
| Critical | Immediate | Page on-call, start incident |
| High | < 1 hour | Alert DBA team, investigate |
| Medium | < 4 hours | Queue for DBA review |
| Low | Next business day | Document and track |

### When to Escalate

- Blocking > 10 minutes
- Multiple users affected
- Deadlocks involving > 5 sessions
- Query running > 1 hour
- System-wide slowdown

---

## See Also

- [Performance Overview](../performance/index.md) - Performance metrics
- [Known Issues](../performance/known-issues/index.md) - Active issues
- [Daily Monitoring](../operations/daily-monitoring.md) - Monitoring procedures

