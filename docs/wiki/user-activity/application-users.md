# Application Users

[Home](../index.md) > [User Activity](index.md) > Application Users

---

## Overview

EDS uses several database accounts for application connectivity. Understanding these accounts helps with troubleshooting and security.

---

## Primary Application Accounts

### EDSIQWebUser

| Property | Value |
|----------|-------|
| **Purpose** | Primary web application account |
| **Monthly Usage** | 214+ database hours |
| **Connection Type** | JDBC connection pool |
| **Typical Queries** | Requisitions, POs, lookups |

**Characteristics:**
- Highest volume account
- Represents all web user activity
- Uses connection pooling
- Includes both read and write operations

**Sample Activity:**
```sql
-- Check EDSIQWebUser activity
SELECT DATEHOUR,
       SUM(EXECSECS) / 60.0 as ExecutionMinutes,
       SUM(EXECS) as ExecutionCount
FROM CONU_1 u
JOIN CON_SQL_SUM_1 s ON u.ID = s.DBUSERID
WHERE u.N = 'EDSIQWebUser'
  AND s.DATEHOUR > DATEADD(day, -1, GETDATE())
GROUP BY DATEHOUR
ORDER BY DATEHOUR
```

---

### EDSAdmin

| Property | Value |
|----------|-------|
| **Purpose** | Administrative and maintenance tasks |
| **Monthly Usage** | Variable |
| **Connection Type** | Direct connections |
| **Typical Queries** | Maintenance, reports, admin tasks |

**Characteristics:**
- Used for background jobs
- Schema changes and maintenance
- Report generation
- Data imports/exports

---

### DPA Monitor Account

| Property | Value |
|----------|-------|
| **Purpose** | Performance monitoring |
| **Monthly Usage** | Continuous (24/7) |
| **Connection Type** | Persistent connection |
| **Typical Queries** | DMV queries, statistics collection |

**Characteristics:**
- Minimal resource usage
- Read-only access
- Collects performance data
- Should not appear in blocking

---

## Job/Service Accounts

### EDSIQ Job Processor

| Property | Value |
|----------|-------|
| **Purpose** | Background job execution |
| **Common Jobs** | Vendor sync, notifications, reports |
| **Schedule** | Various (hourly, daily) |

**Known Issues:**
- Vendor sync job runs too frequently (See [KI-002](../performance/known-issues/vendor-sync-job.md))

---

### Integration Service Account

| Property | Value |
|----------|-------|
| **Purpose** | External system integration |
| **Connections** | Financial systems, HR, SSO |
| **Typical Operations** | Data sync, user updates |

**Known Issues:**
- SSO updates cause deadlocks (See [KI-005](../performance/known-issues/sso-deadlocks.md))

---

## Connection Patterns

### Web Application Pool

```
Application Server
    │
    └── Connection Pool (EDSIQWebUser)
            │
            ├── Min Connections: 10
            ├── Max Connections: 100
            ├── Timeout: 30 seconds
            │
            └── Database Server
```

### Job Processor Pool

```
Job Server (Kubernetes)
    │
    ├── Pod 1 ──► Connection Pool ──► Database
    ├── Pod 2 ──► Connection Pool ──► Database
    └── Pod 3 ──► Connection Pool ──► Database
```

---

## Security Considerations

### Principle of Least Privilege

| Account | db_datareader | db_datawriter | Execute SPs | DDL |
|---------|---------------|---------------|-------------|-----|
| EDSIQWebUser | ✓ | ✓ | ✓ | ✗ |
| EDSAdmin | ✓ | ✓ | ✓ | ✓ |
| DPA Monitor | ✓ | ✗ | Limited | ✗ |
| Job Processor | ✓ | ✓ | ✓ | ✗ |

### Connection String Security

- Credentials stored in Azure Key Vault
- Connection strings use encrypted config
- No passwords in source code
- Regular credential rotation

---

## Monitoring Account Activity

### Current Sessions by Account
```sql
SELECT login_name,
       COUNT(*) as SessionCount,
       SUM(CASE WHEN r.session_id IS NOT NULL THEN 1 ELSE 0 END) as ActiveRequests
FROM sys.dm_exec_sessions s
LEFT JOIN sys.dm_exec_requests r ON s.session_id = r.session_id
WHERE s.is_user_process = 1
GROUP BY login_name
ORDER BY SessionCount DESC
```

### Account Activity History (DPA)
```sql
SELECT u.N as UserName,
       SUM(s.EXECSECS) / 3600.0 as TotalHours,
       SUM(s.EXECS) as TotalExecutions,
       AVG(s.EXECSECS * 1000.0 / NULLIF(s.EXECS, 0)) as AvgMs
FROM CONU_1 u
JOIN CON_SQL_SUM_1 s ON u.ID = s.DBUSERID
WHERE s.DATEHOUR > DATEADD(day, -30, GETDATE())
GROUP BY u.N
ORDER BY TotalHours DESC
```

---

## Troubleshooting Account Issues

### High Activity from Account
1. Check current sessions
2. Identify heavy queries
3. Review recent deployments
4. Check for runaway jobs

### Connection Pool Exhaustion
1. Check max pool settings
2. Review connection leaks
3. Check for blocking holding connections
4. Review transaction management

### Account Lockout
1. Check failed login attempts
2. Review password policy
3. Check credential rotation
4. Verify application configuration

---

## See Also

- [Usage Patterns](usage-patterns.md) - When activity occurs
- [Architecture](../architecture/application-stack.md) - Application connectivity
- [Performance Overview](../performance/index.md) - Performance metrics

