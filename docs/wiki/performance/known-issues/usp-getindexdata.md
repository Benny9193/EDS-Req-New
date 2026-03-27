# KI-001: usp_GetIndexData Performance Issue

[Home](../../index.md) > [Performance](../index.md) > [Known Issues](index.md) > usp_GetIndexData

---

## Summary

| Field | Value |
|-------|-------|
| **Issue ID** | KI-001 |
| **Priority** | P1 Critical |
| **Status** | Investigating |
| **First Detected** | Pre-2025 |
| **Impact** | 24+ hours execution time |
| **Affected Area** | Bid pricing, catalog lookups |

---

## Symptoms

- Query executes for 24+ hours
- Multiple execution plans (19 different plans observed)
- 33 million row scans on BidResults table
- High RESOURCE_SEMAPHORE waits (memory grants)
- Blocking other queries during execution

---

## Root Cause Analysis

### 1. Parameter Sniffing
The stored procedure receives `@BidHeaderId` parameter but generates wildly different execution plans based on the first-compiled parameter value.

**Evidence:** 19 different execution plans in last 30 days

### 2. Large Table Scans
The procedure scans several large tables:

| Table | Rows Scanned | Issue |
|-------|--------------|-------|
| BidResults | 33M | Full scan |
| CrossRefs | 20M+ | Full scan |
| PricingConsolidated | Variable | No covering index |
| VendorCategoryPP | 17K | Clustered scan |

### 3. Expensive Functions
- `String_Agg()` - Aggregation function in hot path
- `master.dbo.ufn_RegExReplace()` - Regex function called per row
- Subquery with `FOR JSON AUTO` - JSON serialization overhead

### 4. Temp Table Issues
- `#Items` temp table created without optimal indexes
- Multiple scans of temp table during processing

---

## Execution Analysis

### Time Distribution (Last 14 Days)
| Date | Time (hrs) |
|------|------------|
| 2026-01-06 | 12.88 (spike) |
| 2026-01-12 | 2.04 |
| Other days | 1.0-2.3 |

### Wait Events
| Wait Type | Description |
|-----------|-------------|
| RESOURCE_SEMAPHORE | Waiting for memory grant |
| LCK_M_IS | Intent shared locks |
| CXPACKET | Parallelism coordination |

---

## Affected SQL

```sql
CREATE procedure [dbo].[usp_getIndexData] @BidHeaderId int
as
begin
  create table #Items (
    ItemId int not null,
    Refs int not null,
    IdList varchar(4096) null,
    JsonData varchar(max) null,
    FirstItemId bigint null
  )

  create clustered index PK_Item on #Items(ItemId)

  -- Initial population with String_Agg
  insert #Items (ItemId, Refs, IdList, FirstItemId)
  select ItemId, count(*), String_Agg(PricingConsolidatedId,','), ...
  from PricingConsolidated
  where bidheaderid = @BidHeaderId
  group by ItemId

  -- Update with RegEx function (SLOW)
  Update I
  set IDList = pco.pco,
      FirstItemId = master.dbo.ufn_RegExReplace(pco.pco,...)
  from #Items I
  ...

  -- Final SELECT with JSON subquery
  select ...
    (select ... for json auto) potc
  from #Items i
  join PricingConsolidated on ...
  join CrossRefs on ...
  join BidResults on ...  -- 33M row scan!
  ...
end
```

---

## Mitigation Options

### Immediate (Quick Wins)

1. **Add OPTION (RECOMPILE)**
   ```sql
   -- At end of procedure
   OPTION (RECOMPILE)
   ```
   **Pros:** Eliminates parameter sniffing
   **Cons:** Compilation overhead each execution

2. **Create Plan Guide**
   Force a known-good execution plan

### Short-Term

1. **Add Covering Index on BidResults**
   ```sql
   CREATE INDEX IX_BidResults_Covering
   ON BidResults (BidHeaderId, ItemId)
   INCLUDE (ImageURL, SDS_URL, ...)
   ```

2. **Add Index on PricingConsolidated**
   ```sql
   CREATE INDEX IX_PricingConsolidated_BidHeader
   ON PricingConsolidated (BidHeaderId, ItemId)
   INCLUDE (PricingConsolidatedId, BidItemFlag, BidPrice)
   ```

### Long-Term

1. **Rewrite Procedure**
   - Remove `ufn_RegExReplace` calls
   - Pre-compute FirstItemId
   - Use indexed temp tables
   - Remove or optimize JSON subquery

2. **Consider Materialized View**
   Pre-compute bid pricing data

---

## Monitoring

### How to Check Current Status
```sql
-- Current executions
SELECT * FROM sys.dm_exec_requests
WHERE command LIKE '%GetIndexData%'

-- Historical (DPA)
SELECT DATEHOUR, SUM(TIMESECS)/3600 as Hours
FROM CON_SQL_SUM_1
WHERE SQLHASH IN (SELECT H FROM CONST_1 WHERE ST LIKE '%usp_getIndexData%')
  AND DATEHOUR > DATEADD(day, -7, GETDATE())
GROUP BY DATEHOUR ORDER BY DATEHOUR DESC
```

---

## Related Issues

- [CrossRef Blocking](crossref-blocking.md) - Blocked by this procedure
- [Trigger Blocking](trigger-blocking.md) - Related blocking pattern

---

## References

- [Performance Overview](../index.md)
- [Schema: Stored Procedures](../../schema/stored-procedures.md)
- [Recommendations](../recommendations.md)
