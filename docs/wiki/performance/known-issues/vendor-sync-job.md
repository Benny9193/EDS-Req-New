# KI-002: Vendor Sync Job Inefficiency

[Home](../../index.md) > [Performance](../index.md) > [Known Issues](index.md) > Vendor Sync Job

---

## Summary

| Field | Value |
|-------|-------|
| **Issue ID** | KI-002 |
| **Priority** | P2 High |
| **Status** | Active |
| **First Detected** | Pre-2025 |
| **Impact** | 59 hours/month wasted |
| **Affected Area** | Background processing, resource consumption |

---

## Symptoms

- Job runs **every hour, 24/7** (336 times in 14 days)
- Each execution takes **4-5 minutes**
- Full table scans on VendorCategoryPP (17K rows)
- Consumes **~2 hours of DB time per day**
- No incremental logic - compares all records every time

---

## Root Cause Analysis

### 1. Excessive Frequency
The job runs every hour but vendor data rarely changes that frequently.

**Evidence:** Same results produced hour after hour with minimal changes

### 2. Full Comparison Logic
Instead of tracking changes, the job:
- Scans ALL vendors from EDS
- Compares to ALL registrations
- Updates ALL matching records

### 3. No Change Detection
No `LastModified` timestamp or change tracking mechanism exists.

---

## Execution Pattern

### Typical Execution (Last 14 Days)
| Metric | Value |
|--------|-------|
| Frequency | Every hour |
| Duration | 4.3-5.0 minutes |
| Daily Time | ~2 hours |
| Monthly Time | ~59 hours |

### Time by Hour
```
Hour  Duration (min)
00:00     4.8
01:00     4.9
02:00     5.0  (slightly higher - less contention)
...
08:00     4.8
...
22:00     4.8
23:00     4.8
```

---

## Affected SQL

```sql
-- Insert new vendors (full scan comparison)
INSERT registrations (active, vendorid, code, password, email, ...)
SELECT vendors.active, vendors.vendorid, vendors.code, ...
FROM eds.dbo.vendors AS Vendors
LEFT OUTER JOIN registrations ON registrations.vendorId = Vendors.VendorId
WHERE registrations.registrationid IS NULL

-- Deactivate deleted vendors (full scan)
UPDATE registrations SET active = 0
FROM registrations
LEFT OUTER JOIN eds.dbo.vendors AS Vendors
  ON Vendors.VendorId = registrations.vendorid
WHERE vendors.vendorid IS NULL
  AND registrations.active = 1

-- Update all vendor info (full scan)
UPDATE registrations
SET name = vendors.name,
    address1 = vendors.Address1,
    ...
FROM registrations
JOIN eds.dbo.vendors AS Vendors ON ...
```

---

## Business Impact

| Impact | Description |
|--------|-------------|
| Resource Waste | 59 hrs/month of unnecessary processing |
| Blocking Risk | Can block other operations during execution |
| CPU Usage | Consistent baseline CPU consumption |
| I/O Load | Repeated full table scans |

---

## Mitigation Options

### Quick Win: Reduce Frequency

**Current:** Every hour (24x daily)
**Recommended:** 4x daily (6 AM, 12 PM, 6 PM, 12 AM)

**Savings:** ~75% reduction = ~44 hours/month saved

```sql
-- Change SQL Agent job schedule to 4x daily
-- No code changes required
```

### Short-Term: Add Change Tracking

1. **Add LastModified column to Vendors**
   ```sql
   ALTER TABLE Vendors ADD LastModified DATETIME DEFAULT GETDATE()
   ```

2. **Create trigger to update timestamp**
   ```sql
   CREATE TRIGGER trg_Vendors_Modified ON Vendors
   AFTER UPDATE AS
   UPDATE Vendors SET LastModified = GETDATE()
   FROM Vendors v JOIN inserted i ON v.VendorId = i.VendorId
   ```

3. **Modify sync to use timestamp**
   ```sql
   -- Only sync vendors modified since last run
   WHERE Vendors.LastModified > @LastSyncTime
   ```

### Long-Term: Implement CDC

Use SQL Server Change Data Capture for automated change detection.

---

## Monitoring

### Check Job Status
```sql
-- Recent executions
SELECT j.name, h.run_date, h.run_time, h.run_duration
FROM msdb.dbo.sysjobs j
JOIN msdb.dbo.sysjobhistory h ON j.job_id = h.job_id
WHERE j.name LIKE '%Vendor%Sync%'
ORDER BY h.run_date DESC, h.run_time DESC
```

### Check Time Consumption (DPA)
```sql
SELECT DATEHOUR, SUM(TIMESECS)/60 as Minutes
FROM CON_SQL_SUM_1
WHERE SQLHASH = 3967956687  -- Vendor sync hash
  AND DATEHOUR > DATEADD(day, -7, GETDATE())
GROUP BY DATEHOUR
ORDER BY DATEHOUR DESC
```

---

## Related Issues

- [Performance Overview](../index.md) - Overall performance state
- [Recommendations](../recommendations.md) - Full optimization plan

---

## References

- [Operations: SQL Agent Jobs](../../operations/sql-agent-jobs.md)
- [Business: Vendors](../../business/entities/vendors.md)
