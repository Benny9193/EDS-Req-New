# Usage Patterns

[Home](../index.md) > [User Activity](index.md) > Usage Patterns

---

## Overview

Understanding usage patterns helps with capacity planning, maintenance scheduling, and incident response.

---

## Daily Patterns

### Typical Weekday

```
Hour    Activity Level
────────────────────────────────────────────────
06:00   ░░░░░░░░░░ Low (East Coast waking up)
07:00   ░░░░░░░░░░░░░░░░ Moderate (Schools opening)
08:00   ░░░░░░░░░░░░░░░░░░░░░░░░ High (Peak start)
09:00   ░░░░░░░░░░░░░░░░░░░░░░░░░░░░ Peak
10:00   ░░░░░░░░░░░░░░░░░░░░░░░░░░ High
11:00   ░░░░░░░░░░░░░░░░░░░░░░ Moderate-High
12:00   ░░░░░░░░░░░░░░░░░░ Moderate (Lunch)
13:00   ░░░░░░░░░░░░░░░░░░░░░░ High
14:00   ░░░░░░░░░░░░░░░░░░░░░░░░ High
15:00   ░░░░░░░░░░░░░░░░░░░░ Moderate-High
16:00   ░░░░░░░░░░░░░░░░ Moderate
17:00   ░░░░░░░░░░░░ Low-Moderate
18:00   ░░░░░░░░░░ Low
19:00   ░░░░░░░░ Low
20:00   ░░░░░░░░ Low
21:00   ░░░░░░░░░░░░░░ Low (Batch jobs starting)
22:00   ░░░░░░░░░░░░░░░░ Moderate (Batch jobs)
23:00   ░░░░░░░░░░ Low
00:00   ░░░░░░ Very Low
```

### Peak Hours
- **Morning Rush:** 8:00 AM - 10:00 AM (Local time)
- **Afternoon:** 1:00 PM - 3:00 PM
- **Evening Batch:** 9:00 PM - 11:00 PM

### Low Usage Windows
- **Overnight:** 12:00 AM - 6:00 AM (Best for maintenance)
- **Weekends:** Minimal activity
- **Holidays:** School closures

---

## Weekly Patterns

| Day | Relative Activity | Notes |
|-----|-------------------|-------|
| Monday | High | Week start, catch-up |
| Tuesday | Moderate-High | Normal operations |
| Wednesday | Moderate | Mid-week |
| Thursday | Moderate | Normal operations |
| Friday | Moderate-High | Week-end processing |
| Saturday | Low | Minimal |
| Sunday | Very Low | Minimal |

---

## Monthly Patterns

### High Activity Periods

| Period | Activity | Reason |
|--------|----------|--------|
| Month Start | Moderate | New period begins |
| Mid-Month | Normal | Regular operations |
| Month End | High | Budget reconciliation, reports |
| Last Day | Very High | Closing activities |

### Budget Cycle Impact
```
Week 1:  ░░░░░░░░░░░░ Normal
Week 2:  ░░░░░░░░░░░░ Normal
Week 3:  ░░░░░░░░░░░░░░ Slightly Higher
Week 4:  ░░░░░░░░░░░░░░░░░░░░ Month-End Rush
```

---

## Annual Patterns

### School Year Calendar

| Period | Activity Level | Notes |
|--------|----------------|-------|
| **August** | Very High | Back-to-school ordering |
| **September** | High | Continued school start |
| **October-November** | Normal | Regular operations |
| **December** | Low-Moderate | Holiday break |
| **January** | Moderate | New semester |
| **February-April** | Normal | Regular operations |
| **May** | Moderate-High | Year-end prep |
| **June** | High | Fiscal year end |
| **July** | Low | Summer break |

### Fiscal Year End (June)
- Budget reconciliation
- Year-end reports
- Encumbrance rollover
- Audit preparation

---

## Query Patterns by Time

### Morning (8-10 AM)
- User authentication
- Requisition creation
- Item lookups
- Dashboard queries

### Midday (11 AM - 1 PM)
- Order processing
- PO generation
- Approval workflows
- Report generation

### Afternoon (2-4 PM)
- Receiving entries
- Invoice processing
- Budget queries
- End-of-day reporting

### Evening (9-11 PM)
- Batch jobs
- Data synchronization
- Report generation
- Maintenance tasks

---

## Batch Job Schedule

### Hourly Jobs

| Job | Time | Impact |
|-----|------|--------|
| Vendor Sync | :00 | Medium ([KI-002](../performance/known-issues/vendor-sync-job.md)) |

### Daily Jobs

| Job | Time | Impact |
|-----|------|--------|
| Statistics Update | 2:00 AM | Low |
| Index Maintenance | 3:00 AM | Medium |
| Backup | 4:00 AM | Low |

### Critical Window: 22:00

The 22:00 hour has historically been problematic:
- Multiple batch jobs scheduled
- [Jan 6 Incident](../performance/incidents/2026-01-06-blocking.md) occurred at this time
- 737 minutes of blocking accumulated

**Recommendation:** Stagger batch jobs, avoid overlapping schedules.

---

## Capacity Planning

### Current Utilization

| Metric | Peak | Average | Notes |
|--------|------|---------|-------|
| CPU | 80% | 45% | Peak during back-to-school |
| Memory | 75% | 60% | Stable |
| Connections | 150 | 80 | Pool max: 200 |
| Disk I/O | High | Moderate | SSD storage |

### Growth Projections

Based on historical trends:
- User growth: ~5% annually
- Data growth: ~20% annually
- Transaction growth: ~10% annually

---

## Monitoring Queries

### Activity by Hour of Day
```sql
SELECT DATEPART(hour, DATEHOUR) as Hour,
       AVG(EXECS) as AvgExecutions,
       AVG(EXECSECS) as AvgSeconds
FROM CON_SQL_SUM_1
WHERE DATEHOUR > DATEADD(day, -30, GETDATE())
GROUP BY DATEPART(hour, DATEHOUR)
ORDER BY Hour
```

### Activity by Day of Week
```sql
SELECT DATENAME(weekday, DATEHOUR) as DayOfWeek,
       DATEPART(weekday, DATEHOUR) as DayNum,
       SUM(EXECS) as TotalExecutions
FROM CON_SQL_SUM_1
WHERE DATEHOUR > DATEADD(day, -30, GETDATE())
GROUP BY DATENAME(weekday, DATEHOUR), DATEPART(weekday, DATEHOUR)
ORDER BY DayNum
```

---

## Maintenance Windows

### Recommended Maintenance Times

| Activity | Best Window | Duration |
|----------|-------------|----------|
| Index Rebuild | Sunday 2-6 AM | 4 hours |
| Statistics Update | Daily 2 AM | 30 min |
| Backup | Daily 4 AM | 1 hour |
| Major Updates | Sunday 12-6 AM | 6 hours |

### Avoid These Times

| Time | Reason |
|------|--------|
| 8-10 AM weekdays | Peak usage |
| Month-end | Budget processing |
| August-September | Back-to-school |
| 22:00 | Batch job conflicts |

---

## See Also

- [Application Users](application-users.md) - Account details
- [Daily Monitoring](../operations/daily-monitoring.md) - Monitoring procedures
- [Performance Overview](../performance/index.md) - Performance metrics

