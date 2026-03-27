# KI-004: CrossRef Lookup Blocking

[Home](../../index.md) > [Performance](../index.md) > [Known Issues](index.md) > CrossRef Blocking

---

## Summary

| Field | Value |
|-------|-------|
| **Issue ID** | KI-004 |
| **Priority** | P4 Medium |
| **Status** | Active |
| **First Detected** | 2026-01-06 |
| **Impact** | 12+ hours blocked (accumulated) |
| **Affected Area** | Item lookups, pricing queries |

---

## Symptoms

- Simple CrossRef lookups taking minutes instead of milliseconds
- Queries waiting on locks held by other operations
- Users experiencing slow item searches
- Pricing information delayed during requisition entry

---

## Root Cause Analysis

### This Issue is a VICTIM

CrossRef lookups are blocked BY other operations, not causing blocking themselves.

**Primary Blockers:**
1. `trig_DetailUpdate` - Holds locks during price updates
2. Bulk INSERT/UPDATE operations on Detail table
3. CrossRef trigger (`trig_CrossRefs`) during catalog imports

### Blocking Pattern
```
Blocker: trig_DetailUpdate (82 min)
    └── Victim: CrossRef SELECT (12+ hrs accumulated)

Blocker: Bulk Detail inserts
    └── Victim: CrossRef lookups

Blocker: trig_CrossRefs
    └── Victim: Other CrossRef queries
```

---

## Affected Query

```sql
-- Simple lookup that gets blocked
SELECT CrossRefId,
       COALESCE(PerishableItem, 0) as PerishableItem,
       COALESCE(PrescriptionRequired, 0) as PrescriptionRequired,
       COALESCE(DigitallyDelivered, 0) as DigitallyDelivered,
       COALESCE(MinimumOrderQuantity, 0) as MinimumOrderQuantity
FROM CrossRefs
WHERE CrossRefId = @P0
```

This query should execute in <10ms but was blocked for 737 minutes on Jan 6, 2026.

---

## Blocking Timeline (Jan 6, 2026)

| Time | Blocked Duration |
|------|------------------|
| 21:00 | 29.3 minutes |
| 22:00 | 737.8 minutes |
| Total | 767+ minutes |

**Note:** The 22:00 spike was during a bulk operation that triggered `trig_DetailUpdate` extensively.

---

## Business Impact

| Impact | Description |
|--------|-------------|
| Item Lookups | Slow during requisition entry |
| Pricing Display | Delayed pricing information |
| User Experience | Perceived system slowness |
| Cascading Delays | Other queries wait for CrossRef data |

---

## Mitigation Options

### Immediate (Apply to Calling Queries)

1. **Add NOLOCK hint**
   ```sql
   SELECT CrossRefId, ...
   FROM CrossRefs WITH (NOLOCK)
   WHERE CrossRefId = @P0
   ```
   **Risk:** Dirty reads possible (acceptable for display purposes)

2. **Add query timeout**
   ```sql
   SET LOCK_TIMEOUT 5000  -- 5 second timeout
   ```

### Short-Term (Address Root Cause)

1. **Fix trig_DetailUpdate** - See [KI-003](trigger-blocking.md)
2. **Optimize bulk operations** - Process in smaller batches
3. **Add covering index**
   ```sql
   CREATE INDEX IX_CrossRefs_Lookup
   ON CrossRefs (CrossRefId)
   INCLUDE (PerishableItem, PrescriptionRequired,
            DigitallyDelivered, MinimumOrderQuantity)
   ```

### Long-Term

1. **Implement read replicas** for lookup queries
2. **Cache frequently accessed CrossRef data**
3. **Separate OLTP and reporting workloads**

---

## Monitoring

### Check If Currently Blocked
```sql
SELECT r.session_id, r.blocking_session_id,
       r.wait_type, r.wait_time,
       t.text as QueryText
FROM sys.dm_exec_requests r
CROSS APPLY sys.dm_exec_sql_text(r.sql_handle) t
WHERE t.text LIKE '%CrossRef%'
  AND r.blocking_session_id > 0
```

### Historical Blocking (DPA)
```sql
SELECT DATEHOUR, SUM(BLEETIMESECS)/60 as BlockedMinutes
FROM CON_BLOCKING_SUM_1
WHERE DIMENSIONID = 3173750858  -- CrossRef query hash
  AND DIMENSIONTYPE = 'S'
  AND DATEHOUR > DATEADD(day, -7, GETDATE())
GROUP BY DATEHOUR
HAVING SUM(BLEETIMESECS) > 0
ORDER BY DATEHOUR DESC
```

---

## Related Issues

- [trig_DetailUpdate Blocking](trigger-blocking.md) - Root cause
- [Jan 6 Incident](../incidents/2026-01-06-blocking.md) - Major incident
- [usp_GetIndexData](usp-getindexdata.md) - Also accesses CrossRefs

---

## References

- [Schema: CrossRefs Table](../../schema/by-domain/inventory-catalog.md)
- [Troubleshooting: Blocking](../../troubleshooting/blocking.md)
