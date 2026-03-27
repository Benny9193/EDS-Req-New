# KI-003: trig_DetailUpdate Blocking

[Home](../../index.md) > [Performance](../index.md) > [Known Issues](index.md) > Trigger Blocking

---

## Summary

| Field | Value |
|-------|-------|
| **Issue ID** | KI-003 |
| **Priority** | P3 High |
| **Status** | Active |
| **First Detected** | 2026-01-06 |
| **Impact** | Up to 82 minutes blocking per incident |
| **Affected Area** | Requisition entry, bulk operations |

---

## Symptoms

- Long blocking chains during requisition entry
- CrossRef lookups blocked for extended periods
- Other users unable to save requisitions
- Cascade of blocked queries
- Particularly severe during bulk operations

---

## Root Cause Analysis

### 1. Complex Trigger Logic
`trig_DetailUpdate` fires on every INSERT/UPDATE to the Detail table and performs extensive operations while holding locks.

**Operations performed:**
- Price lookups from CrossRefs
- Item remapping via BidMappedItems
- Vendor matching
- Award lookups
- Multiple table updates

### 2. Lock Escalation
When multiple rows are affected:
- Row locks escalate to page locks
- Page locks escalate to table locks
- Other queries must wait

### 3. Function Calls in Trigger
The trigger calls `uf_RequisitionIsVisible` which performs additional queries while locks are held.

---

## Blocking Analysis (Jan 6, 2026 Incident)

### Queries Blocked by This Trigger
| Query | Blocked Time |
|-------|--------------|
| CrossRef lookups | 82.8 minutes |
| uf_RequisitionIsVisible | 63.8 minutes |
| DELETE FROM vw_ReqDetail | 31.4 minutes |
| SELECT from vw_ExistingRequisitions | 27.9 minutes |

### Blocking Chain
```
trig_DetailUpdate (root blocker)
    └── Holds locks on Detail, Items, CrossRefs
        └── Blocks: CrossRef SELECT queries
        └── Blocks: uf_RequisitionIsVisible
        └── Blocks: Other Detail modifications
            └── Blocks: Cascade to more queries
```

---

## Trigger Code Analysis

```sql
CREATE TRIGGER [dbo].[trig_DetailUpdate] ON [dbo].[Detail]
AFTER INSERT, UPDATE NOT FOR REPLICATION
AS
SET NOCOUNT ON

-- Table variables for processing
DECLARE @BidsList TABLE (RequisitionId int, BidHeaderId int null)
DECLARE @CatPrices TABLE (...)
DECLARE @FrozenReqs TABLE (...)

-- Remap items with new IDs (BLOCKING OPERATION)
UPDATE Detail
SET ItemId = MappedItems.NewItemId,
    OriginalItemId = COALESCE(Detail.OriginalItemId, MappedItems.OrigItemId)
FROM inserted WITH (UPDLOCK, ROWLOCK)  -- Lock hints don't prevent escalation
JOIN Detail ON Detail.DetailId = inserted.DetailId
JOIN Items ON Items.ItemId = Detail.ItemId
JOIN BidMappedItems ON ...

-- Update pricing from CrossRefs (BLOCKING OPERATION)
UPDATE Detail
SET BidPrice = CrossRefs.CatalogPrice,
    CatalogPage = CrossRefs.Page,
    ...
FROM inserted
JOIN CrossRefs ON ...  -- Holds locks on CrossRefs
JOIN BidHeaders ON ...
...
```

---

## Business Impact

| Impact | Description |
|--------|-------------|
| User Experience | Users unable to save requisitions |
| Data Entry | Bulk imports cause system-wide slowdown |
| Productivity | Staff waiting for system response |
| Support Calls | Increased helpdesk tickets |

---

## Mitigation Options

### Immediate (Quick Wins)

1. **Add NOLOCK hints for read operations**
   ```sql
   -- In trigger, for read-only lookups
   JOIN CrossRefs WITH (NOLOCK) ON ...
   ```
   **Risk:** Dirty reads possible (acceptable for pricing lookups)

2. **Process in smaller batches**
   For bulk operations, process 100 rows at a time instead of all at once.

### Short-Term

1. **Move non-critical logic to async**
   - Keep only essential updates in trigger
   - Queue price recalculations for background processing

2. **Optimize uf_RequisitionIsVisible**
   - Add appropriate indexes
   - Consider caching results

### Long-Term

1. **Redesign trigger architecture**
   - Use Service Broker for async processing
   - Event-driven price updates
   - Separate read and write paths

2. **Consider removing trigger**
   - Move logic to application layer
   - Use stored procedures instead

---

## Monitoring

### Check Current Blocking
```sql
-- Real-time blocking
SELECT blocking_session_id, session_id, wait_type, wait_time,
       wait_resource, command
FROM sys.dm_exec_requests
WHERE blocking_session_id > 0
```

### Check Historical Blocking (DPA)
```sql
SELECT DATEHOUR, SUM(BLERTIMESECS)/60 as BlockerMinutes
FROM CON_BLOCKING_SUM_1
WHERE DIMENSIONID = 4326641057  -- trig_DetailUpdate hash
  AND DIMENSIONTYPE = 'S'
  AND DATEHOUR > DATEADD(day, -7, GETDATE())
GROUP BY DATEHOUR
ORDER BY DATEHOUR DESC
```

---

## Related Issues

- [CrossRef Blocking](crossref-blocking.md) - Victim of this trigger
- [Jan 6 Incident](../incidents/2026-01-06-blocking.md) - Major incident

---

## References

- [Schema: Triggers](../../schema/triggers.md)
- [Schema: Detail Table](../../schema/by-domain/orders-purchasing.md)
- [Troubleshooting: Blocking](../../troubleshooting/blocking.md)
