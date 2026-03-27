# Daily Monitoring Checklist

[Home](../index.md) > [Operations](index.md) > Daily Monitoring

---

## Morning Health Check

**Time:** 8:00 AM daily
**Duration:** ~15 minutes
**Owner:** DBA On-Call

---

## Checklist

### 1. Health Dashboard (2 minutes)

- [ ] Open DPA dashboard for EDS database
- [ ] Check overall health score (target: >75)
- [ ] Note any CRITICAL or WARNING alerts
- [ ] Review response time trends

**DPA URL:** `https://dpa-server/iwc/db/1/`

---

### 2. Overnight Blocking Review (3 minutes)

```sql
-- Check blocking from overnight (last 12 hours)
SELECT
    DATEHOUR,
    SUM(BLEETIMESECS)/60.0 as BlockedMinutes,
    SUM(BLERTIMESECS)/60.0 as BlockerMinutes
FROM CON_BLOCKING_SUM_1
WHERE DATEHOUR > DATEADD(hour, -12, GETDATE())
GROUP BY DATEHOUR
HAVING SUM(BLEETIMESECS) > 300  -- More than 5 min
ORDER BY DATEHOUR DESC
```

**Action if blocking > 30 min:**
1. Identify blocking query
2. Check if recurring pattern
3. Create ticket if new issue

---

### 3. Deadlock Check (2 minutes)

```sql
-- Check for overnight deadlocks
SELECT ID, D as DeadlockTime, SESSION_COUNT, VICTIM_SUM_MS
FROM CON_DEADLOCK_1
WHERE D > DATEADD(hour, -24, GETDATE())
ORDER BY D DESC
```

**Action if deadlocks found:**
1. Review deadlock graph in DPA
2. Identify pattern (same queries?)
3. Check [SSO Deadlocks issue](../performance/known-issues/sso-deadlocks.md)

---

### 4. Slow Query Review (5 minutes)

```sql
-- Top slow queries from overnight
SELECT TOP 10
    SQLHASH,
    SUM(TIMESECS)/3600.0 as TotalHours,
    LEFT(t.ST, 100) as SQL_Snippet
FROM CON_SQL_SUM_1 s
JOIN CONST_1 t ON s.SQLHASH = t.H
WHERE s.DATEHOUR > DATEADD(hour, -12, GETDATE())
GROUP BY SQLHASH, LEFT(t.ST, 100)
ORDER BY SUM(TIMESECS) DESC
```

**Action if new slow query:**
1. Check if known issue
2. Review execution plan
3. Add to known issues if recurring

---

### 5. SQL Agent Jobs (3 minutes)

- [ ] Check SQL Server Agent Job Activity Monitor
- [ ] Verify overnight jobs completed successfully
- [ ] Note any failed jobs

**Key Jobs to Check:**
| Job | Expected | Notes |
|-----|----------|-------|
| Vendor Sync | Every hour | [Known issue](../performance/known-issues/vendor-sync-job.md) |
| Index Maintenance | Nightly | Should complete by 6 AM |
| Statistics Update | Nightly | Should complete by 6 AM |
| Backup Jobs | Per schedule | Check completion |

---

### 6. Disk Space (1 minute)

```sql
-- Check database file space
SELECT
    name,
    size * 8 / 1024 as SizeMB,
    FILEPROPERTY(name, 'SpaceUsed') * 8 / 1024 as UsedMB
FROM sys.database_files
```

**Thresholds:**
- **Warning:** < 20% free space
- **Critical:** < 10% free space

---

### 7. Document Findings (2 minutes)

- [ ] Log any issues in DBA daily log
- [ ] Create tickets for new issues
- [ ] Update team on critical items

---

## Escalation Criteria

| Condition | Action |
|-----------|--------|
| Blocking > 1 hour | Notify DBA Lead |
| Multiple deadlocks | Investigate immediately |
| Job failure (critical) | Notify DBA Lead |
| Disk < 10% | Immediate action |
| Health score < 50 | Investigate immediately |

---

## Contact Information

| Role | Contact |
|------|---------|
| DBA On-Call | Rotation schedule |
| DBA Lead | David Harrison |
| Manager | See alert contacts |

---

## Related Documentation

- [Alert Triage](alert-triage.md) - Handling alerts
- [Known Issues](../performance/known-issues/index.md) - Active issues
- [Troubleshooting](../troubleshooting/index.md) - Problem resolution
- [Blocking Runbook](../troubleshooting/runbooks/blocking-emergency.md) - Emergency response
