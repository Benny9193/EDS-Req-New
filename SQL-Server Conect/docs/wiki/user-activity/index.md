# User Activity

[Home](../index.md) > User Activity

---

## Overview

This section documents database user activity patterns, application connections, and usage trends observed through DPA monitoring.

---

## Contents

| Document | Description |
|----------|-------------|
| [Application Users](application-users.md) | System accounts and their usage |
| [Usage Patterns](usage-patterns.md) | Peak times and access patterns |

---

## Activity Summary (Monthly)

### Top Database Users

| User | Monthly Hours | % of Total | Description |
|------|---------------|------------|-------------|
| EDSIQWebUser | 214+ | 56% | Primary web application |
| EDSAdmin | Variable | ~20% | Administrative tasks |
| DPA Monitor | Continuous | ~10% | Performance monitoring |
| Other | Variable | ~14% | Various |

### Activity by Application

| Application | Description | Connection Pool |
|-------------|-------------|-----------------|
| EDSIQ Web | Main web application | Yes |
| EDSIQ Jobs | Background job processor | Yes |
| Node.js | API services | Yes |
| Reporting | SSRS/Reports | No |
| Integration | External system sync | No |

---

## Connection Sources

### By Machine/Pod

Primary traffic sources identified from DPA:

| Source | Type | Description |
|--------|------|-------------|
| eds-edsiq-* | Kubernetes Pod | Web application pods |
| eds-jobs-* | Kubernetes Pod | Job processor pods |
| eds-api-* | Kubernetes Pod | API service pods |
| REPORTING01 | Server | Report server |
| INTEGRATION | Server | Integration server |

### By Program

| Program | Description |
|---------|-------------|
| Java JDBC | Primary application |
| Node.js | API layer |
| Python | Integration scripts |
| .NET SQLClient | Reporting |

---

## Database Time Distribution

```
EDSIQWebUser    ████████████████████████████████████████████████ 214 hrs
Admin/Jobs      █████████████████ 80 hrs
Monitoring      ████████ 40 hrs
Other           █████ 24 hrs
                ──────────────────────────────────────────────────
                Total: ~358 hrs/month database time
```

---

## Key Observations

### Peak Usage
- **Morning:** 8-10 AM (East Coast schools start)
- **Midday:** 11 AM - 1 PM (Lunch ordering)
- **Afternoon:** 2-4 PM (End of day processing)
- **Month-End:** Higher than average (Budget reconciliation)
- **Back-to-School:** August-September (Highest volume)

### Low Usage
- **Overnight:** 10 PM - 6 AM
- **Weekends:** Minimal activity
- **Holidays:** School closures

### Concerning Patterns
- 22:00 batch jobs causing blocking
- Hourly vendor sync consuming resources
- SSO updates causing deadlocks

---

## Monitoring Queries

### Current Connections by User
```sql
SELECT login_name, COUNT(*) as Connections,
       SUM(CASE WHEN status = 'running' THEN 1 ELSE 0 END) as Active
FROM sys.dm_exec_sessions
WHERE is_user_process = 1
GROUP BY login_name
ORDER BY Connections DESC
```

### Activity by Hour (from DPA)
```sql
SELECT DATEPART(hour, DATEHOUR) as Hour,
       SUM(EXECSECS) / 3600.0 as TotalHours
FROM CON_SQL_SUM_1
WHERE DATEHOUR > DATEADD(day, -7, GETDATE())
GROUP BY DATEPART(hour, DATEHOUR)
ORDER BY Hour
```

---

## See Also

- [Daily Monitoring](../operations/daily-monitoring.md) - Monitoring procedures
- [Performance Overview](../performance/index.md) - Performance metrics
- [Architecture](../architecture/index.md) - System architecture

