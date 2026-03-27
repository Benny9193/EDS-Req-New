# KI-005: SSO User Update Deadlocks

[Home](../../index.md) > [Performance](../index.md) > [Known Issues](index.md) > SSO Deadlocks

---

## Summary

| Field | Value |
|-------|-------|
| **Issue ID** | KI-005 |
| **Priority** | P5 Medium |
| **Status** | Active |
| **First Detected** | 2026-01-12 |
| **Impact** | 20 deadlocks/month, 8-12 sessions involved |
| **Affected Area** | User authentication, SSO sync |

---

## Symptoms

- Deadlocks involving 8-12 sessions simultaneously
- All sessions attempting to UPDATE Users table
- Same Kubernetes pod (`eds-edsiq-2-*`) as source
- Page-level locking conflicts
- Deadlock victim chosen, transaction rolled back

---

## Root Cause Analysis

### 1. Parallel SSO Updates
The application performs bulk SSO user updates in parallel from the same pod.

**Pattern:**
- Multiple threads/requests fire simultaneously
- Each updates a different user by Email
- All try to update same pages in Users table
- Page-level locking causes deadlock

### 2. No Unique Index on Email
The WHERE clause uses `Email = @P2 AND Active = 1` but there's no unique index on this combination, causing table/page scans.

### 3. Same-Pod Contention
All deadlocking sessions originate from same pod: `eds-edsiq-2-868b8bf5f-t74zq`

---

## Deadlock Analysis

### Recent Deadlocks (Jan 12, 2026)
| ID | Time | Sessions | Victim Time (ms) |
|----|------|----------|------------------|
| 996 | 18:18:59 | 8 | 21,086 |
| 995 | 18:18:57 | 12 | 8,043 |
| 994 | 18:18:52 | 12 | 3,040 |

**Note:** Three deadlocks within 7 seconds!

### Affected Query
```sql
UPDATE dbo.Users
SET SSOID = @P0, SSOProvider = @P1
WHERE Email = @P2
  AND Active = 1
```

### Lock Resources
All deadlocks involve **PAGE locks** on the Users table:
- `PAGE: 5:1:178975` (Users)
- `PAGE: 5:1:999246` (Users)
- `PAGE: 5:1:132534783` (Users)

---

## Deadlock Graph Pattern

```
Session A (SPID 207)          Session B (SPID 99)
     │                              │
     │ Holds: PAGE 178975           │ Holds: PAGE 1037655
     │ Wants: PAGE 999246           │ Wants: PAGE 178975
     │                              │
     └──────────────────────────────┘
              DEADLOCK!

One session becomes victim → Transaction rolled back
```

---

## Business Impact

| Impact | Description |
|--------|-------------|
| Authentication | SSO updates may fail/retry |
| User Experience | Delayed profile updates |
| Error Logs | Deadlock exceptions in app logs |
| Retries | Failed transactions retry, adding load |

---

## Mitigation Options

### Immediate (Quick Win)

1. **Serialize SSO Updates**
   Process users one at a time instead of in parallel:
   ```java
   // Instead of parallel processing
   synchronized(ssoUpdateLock) {
       updateUserSSO(userId, ssoId, provider);
   }
   ```

2. **Add Retry Logic**
   ```java
   for (int i = 0; i < 3; i++) {
       try {
           updateUserSSO(...);
           break;
       } catch (DeadlockException e) {
           Thread.sleep(100 * (i + 1));  // Backoff
       }
   }
   ```

### Short-Term

1. **Add Index on Email**
   ```sql
   CREATE UNIQUE INDEX IX_Users_Email_Active
   ON Users (Email, Active)
   WHERE Active = 1
   ```
   This enables row-level locking instead of page scans.

2. **Use Row-Level Locking Hints**
   ```sql
   UPDATE dbo.Users WITH (ROWLOCK)
   SET SSOID = @P0, SSOProvider = @P1
   WHERE Email = @P2 AND Active = 1
   ```

### Long-Term

1. **Queue-Based Processing**
   - Queue SSO updates to message broker
   - Single consumer processes sequentially
   - Eliminates concurrent update conflicts

2. **Batch Updates**
   - Collect SSO updates over time window
   - Apply as single batch transaction
   - Use MERGE statement for efficiency

---

## Monitoring

### Check Recent Deadlocks
```sql
SELECT ID, D as DeadlockTime, SESSION_COUNT, VICTIM_SUM_MS
FROM CON_DEADLOCK_1
WHERE D > DATEADD(day, -7, GETDATE())
ORDER BY D DESC
```

### Check Deadlock Details
```sql
SELECT DEADLOCK_ID, PIECE, DETAIL
FROM CON_DEADLOCK_DETAIL_1
WHERE DEADLOCK_ID IN (
    SELECT TOP 5 ID FROM CON_DEADLOCK_1 ORDER BY D DESC
)
ORDER BY DEADLOCK_ID DESC, PIECE
```

### Monitor Users Table Locking
```sql
SELECT resource_type, resource_description,
       request_mode, request_status
FROM sys.dm_tran_locks
WHERE resource_database_id = DB_ID('EDS')
  AND resource_associated_entity_id = OBJECT_ID('Users')
```

---

## Related Issues

- [Jan 6 Incident](../incidents/2026-01-06-blocking.md) - Also involved Users table
- [Performance Overview](../index.md) - Overall state

---

## References

- [Schema: Users Table](../../schema/by-domain/users-security.md)
- [Troubleshooting: Deadlocks](../../troubleshooting/deadlocks.md)
- [Architecture: Application Stack](../../architecture/application-stack.md)
