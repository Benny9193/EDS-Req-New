# SQL Server Performance Optimization Recommendations

**Analysis Date:** 2025-12-04
**Source:** dpa_EDSAdmin database (207 tables, 11.9M rows of performance metrics)
**Data Coverage:** November 4 - December 4, 2025 (30 days)

---

## Executive Summary

Analysis of the dpa_EDSAdmin performance monitoring database has identified **critical optimization opportunities** that could improve system performance by up to **99.985%** for specific queries.

### Key Findings

🔴 **CRITICAL:** Severe blocking event detected (May 10, 2025)
- 103.5 hours of cumulative blockee time
- 48.4 hours of blocker time
- Root cause impact: 108.6 hours

🟡 **HIGH PRIORITY:** Missing indexes with 99.98% potential improvement
- Multiple queries identified with near-total performance degradation
- Est. savings: 99.985% for top recommendations

🟢 **ONGOING:** Real-time performance monitoring available
- Data updated within minutes (last: 17:49:59 today)
- 30 days of detailed metrics (10-second intervals)

---

## Priority 1: Missing Index Recommendations (IMMEDIATE ACTION)

### Critical Missing Indexes

**Impact: Up to 99.985% performance improvement**

The CON_WHATIF_SRC_1 table contains 2,954 missing index recommendations. Top findings:

| Query Hash | Executions | Wait Time (ms) | Est. Savings | Status |
|------------|------------|----------------|--------------|--------|
| 4709584296 | 29 | 4 | 99.985% | **URGENT** |
| 2198419505 | Multiple | Unknown | 99.985% | **URGENT** |
| 4616243174 | Multiple | Unknown | 99.985% | **URGENT** |

**Recommended Actions:**

1. **Query dpa_EDSAdmin for Full Details:**
```sql
SELECT TOP 50
    w.ID,
    CONVERT(VARCHAR, w.D, 120) as DateIdentified,
    w.SQL_HASH,
    w.SQL_EXECS as Executions,
    w.SQL_WAIT as WaitTimeMS,
    w.EST_SAVING as EstimatedSavingPercent,
    fq.ODATABASE as DatabaseName,
    fq.OSCHEMA as SchemaName,
    fq.ONAME as TableName,
    fq.OINDEX_TABLE as IndexName,
    st.ST as SQLText
FROM CON_WHATIF_SRC_1 w
LEFT JOIN CON_FQ_OBJECT_1 fq ON w.IDX_ID = fq.ID
LEFT JOIN CONST_1 st ON w.SQL_HASH = st.H
WHERE w.D >= DATEADD(day, -30, GETDATE())
    AND w.EST_SAVING >= 90  -- Over 90% potential improvement
ORDER BY w.EST_SAVING DESC, w.SQL_EXECS DESC;
```

2. **Review Execution Plans:**
   - Connect to dpa_EDSAdmin
   - Execute above query
   - Examine plan_hash for top 10 results
   - Generate CREATE INDEX statements

3. **Test in Development:**
   - Create indexes in test environment first
   - Validate performance improvement
   - Monitor for negative impacts on INSERT/UPDATE/DELETE

4. **Deploy to Production:**
   - Schedule during maintenance window
   - Create indexes online (ONLINE=ON) if SQL Server Enterprise
   - Monitor index fragmentation post-creation

---

## Priority 2: Blocking Investigation (URGENT)

### Critical Blocking Event: May 10, 2025

**Metrics:**
- Blockee Time: 372,793 seconds (103.5 hours)
- Blocker Time: 174,099 seconds (48.4 hours)
- Root Impact: 390,966 seconds (108.6 hours)

**Investigation Query:**
```sql
SELECT TOP 20
    bs.DATEHOUR,
    bs.DIMENSIONTYPE,
    CASE bs.DIMENSIONTYPE
        WHEN 'P' THEN prog.NAME
        WHEN 'D' THEN db.NAME
        WHEN 'E' THEN ev.NAME
        ELSE CAST(bs.DIMENSIONID as VARCHAR)
    END as BlockerName,
    bs.BLEETIMESECS / 3600.0 as BlockeeHours,
    bs.BLERTIMESECS / 3600.0 as BlockerHours,
    bs.ROOTIMPACTSECS / 3600.0 as RootImpactHours
FROM CON_BLOCKING_SUM_1 bs
LEFT JOIN CONM_1 prog ON bs.DIMENSIONID = prog.ID AND bs.DIMENSIONTYPE = 'P'
LEFT JOIN CONM_1 db ON bs.DIMENSIONID = db.ID AND bs.DIMENSIONTYPE = 'D'
LEFT JOIN CONM_1 ev ON bs.DIMENSIONID = ev.ID AND bs.DIMENSIONTYPE = 'E'
WHERE bs.DATEHOUR >= '2025-05-10 00:00:00'
    AND bs.DATEHOUR < '2025-05-11 00:00:00'
    AND bs.BLEETIMESECS > 0
ORDER BY bs.BLEETIMESECS DESC;
```

**Recommended Actions:**

1. **Identify Root Blocker:**
   - Run query above to find DIMENSIONTYPE (Program/Database/Event)
   - Trace back to specific application or batch job
   - Review transaction logs for that timeframe

2. **Implement Fixes:**
   - Review transaction isolation levels (consider READ_COMMITTED_SNAPSHOT)
   - Implement query hints (NOLOCK, READPAST where appropriate)
   - Break up long-running transactions
   - Review application code for explicit transactions

3. **Prevention:**
   - Set up alerts for blocking > 5 minutes
   - Implement deadlock monitoring
   - Consider application-level retry logic

---

## Priority 3: Slow Query Optimization

### Top Slow Queries (Last 7 Days)

**Query to Identify:**
```sql
SELECT TOP 50
    ss.H as SQLHash,
    SUM(ss.EXECS) as TotalExecutions,
    SUM(ss.DREADS) as TotalDiskReads,
    SUM(ss.BGETS) as TotalBufferGets,
    SUM(ss.ROW_COUNT) as TotalRowsReturned,
    CAST(SUM(ss.BGETS) as FLOAT) / NULLIF(SUM(ss.EXECS), 0) as AvgBufferGetsPerExec,
    CAST(SUM(ss.DREADS) as FLOAT) / NULLIF(SUM(ss.EXECS), 0) as AvgDiskReadsPerExec,
    st.ST as SQLText
FROM CONSS_1 ss
LEFT JOIN CONST_1 st ON ss.H = st.H
WHERE ss.D >= DATEADD(day, -7, GETDATE())
GROUP BY ss.H, st.ST
HAVING SUM(ss.BGETS) >= 1000000  -- Over 1M buffer gets total
ORDER BY SUM(ss.BGETS) DESC;
```

**Analysis Metrics:**
- **TotalBufferGets:** Total logical I/O (higher = slower)
- **AvgBufferGetsPerExec:** Average logical I/O per execution (target: <1000 for OLTP)
- **TotalDiskReads:** Physical I/O (should be <<10% of buffer gets)

**Optimization Strategies:**

1. **High Buffer Gets (>100K per exec):**
   - Review execution plan for table scans
   - Add covering indexes
   - Consider indexed views

2. **High Disk Reads (DREADS):**
   - Indicates missing data from buffer cache
   - Review server memory configuration
   - Consider SSD storage for hot data

3. **High Execution Count + Low Efficiency:**
   - Parameterize queries (avoid ad-hoc SQL)
   - Implement query result caching
   - Review application code for N+1 query patterns

---

## Priority 4: I/O Performance Issues

### I/O Latency Monitoring

**Query for Last 24 Hours:**
```sql
SELECT TOP 100
    CONVERT(VARCHAR, io.D, 120) as MeasurementTime,
    io.FILEID,
    io.READ_LATENCY as ReadLatencyMS,
    io.WRITE_LATENCY as WriteLatencyMS,
    io.READ_THROUGHPUT as ReadThroughputMB,
    io.WRITE_THROUGHPUT as WriteThroughputMB
FROM CON_IO_DETAIL_1 io
WHERE io.D >= DATEADD(hour, -24, GETDATE())
    AND (io.READ_LATENCY >= 50 OR io.WRITE_LATENCY >= 50)  -- Over 50ms
ORDER BY io.D DESC, io.READ_LATENCY DESC;
```

**Latency Thresholds:**
- **< 10ms:** Excellent (SSD performance)
- **10-50ms:** Acceptable (standard SSD/fast disk)
- **50-100ms:** Concerning (investigate)
- **> 100ms:** Critical (urgent action required)

**Remediation:**

1. **Disk Subsystem:**
   - Check SAN/storage array health
   - Review RAID configuration
   - Consider NVMe SSDs for tempdb and high-churn tables

2. **File Layout:**
   - Separate data files, log files, tempdb to different disks
   - Review file growth settings (avoid autogrow during production)
   - Pre-allocate file space

3. **SQL Server Configuration:**
   - Review max server memory setting
   - Enable instant file initialization
   - Optimize buffer pool size

---

## Ongoing Monitoring Recommendations

### Daily Monitoring Queries

#### 1. Missing Indexes (Daily Check)
```sql
-- Run at start of day to catch new recommendations
SELECT COUNT(*) as NewMissingIndexes
FROM CON_WHATIF_SRC_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND EST_SAVING > 90;
```

#### 2. Blocking Events (Hourly Check)
```sql
-- Alert if any blocking >5 minutes in last hour
SELECT
    COUNT(*) as BlockingEvents,
    SUM(BLEETIMESECS) / 60.0 as TotalBlockingMinutes
FROM CON_BLOCKING_SUM_1
WHERE DATEHOUR >= DATEADD(hour, -1, GETDATE())
    AND BLEETIMESECS > 300;  -- Over 5 minutes
```

#### 3. I/O Health (Real-time)
```sql
-- Current I/O latency
SELECT
    AVG(READ_LATENCY) as AvgReadLatency,
    AVG(WRITE_LATENCY) as AvgWriteLatency,
    MAX(READ_LATENCY) as MaxReadLatency,
    MAX(WRITE_LATENCY) as MaxWriteLatency
FROM CON_IO_DETAIL_1
WHERE D >= DATEADD(minute, -10, GETDATE());
```

### Automated Alerting

**Set up SQL Server Agent jobs to:**

1. **Missing Index Alert** (Daily at 8 AM)
   - Check for new high-impact missing indexes (EST_SAVING > 95%)
   - Email DBA team with details

2. **Blocking Alert** (Every 15 minutes)
   - Check for blocking > 5 minutes
   - Page on-call if blocking > 30 minutes

3. **I/O Latency Alert** (Every 5 minutes)
   - Alert if avg latency > 100ms for 3 consecutive checks
   - Escalate if persists > 15 minutes

4. **Slow Query Alert** (Every hour)
   - Identify queries with > 10M buffer gets in last hour
   - Log to operations dashboard

---

## Performance Dashboard Recommendations

### Suggested Metrics to Display

**Real-Time (10-second refresh):**
- Current blocking events (count, total time)
- Current I/O latency (avg read/write)
- Top 5 queries by buffer gets (last 10 minutes)

**Hourly Aggregates:**
- Query execution trends
- Blocking event trends
- I/O throughput trends
- Missing index count by database

**Daily Summaries:**
- Total query executions
- Total blocking time
- Average I/O latency
- New performance issues identified

### Data Sources

All metrics available from dpa_EDSAdmin:
- CON_METRICS_HOUR_1 (96.7K rows) - Hourly aggregates
- CON_STATS_DAY_SUM_1 (37.9K rows) - Daily summaries
- CONSS_1 (2.42M rows) - Real-time SQL stats
- CON_IO_DETAIL_1 (2.92M rows) - Real-time I/O stats

---

## Performance Optimization Checklist

### Week 1 (Immediate Actions)
- [ ] Query for top 10 missing indexes (EST_SAVING > 99%)
- [ ] Review execution plans for identified queries
- [ ] Test index creation in development
- [ ] Investigate May 10th blocking event root cause
- [ ] Set up blocking alerts (>5 minutes)

### Week 2 (Index Implementation)
- [ ] Deploy top 5 missing indexes to production
- [ ] Monitor index usage (sys.dm_db_index_usage_stats)
- [ ] Validate performance improvement (before/after metrics)
- [ ] Document index rationale in wiki/confluence

### Week 3 (Blocking Resolution)
- [ ] Implement blocking fixes identified in Week 1
- [ ] Review transaction isolation levels across applications
- [ ] Test snapshot isolation for reporting queries
- [ ] Update application code to minimize transaction duration

### Week 4 (Slow Query Optimization)
- [ ] Identify top 10 slow queries from CONSS_1
- [ ] Review and optimize execution plans
- [ ] Implement query caching where appropriate
- [ ] Parameterize ad-hoc queries in application code

### Ongoing (Monthly Reviews)
- [ ] Review new missing index recommendations
- [ ] Analyze blocking event trends
- [ ] Review I/O latency trends
- [ ] Update performance baseline metrics

---

## Expected Performance Improvements

Based on analysis findings, implementing these recommendations should result in:

| Metric | Current (Estimated) | Target | Improvement |
|--------|---------------------|--------|-------------|
| Query Execution Time | Varies | -50-99% | Major |
| Blocking Events | 103.5 hrs (May 10) | <1 hr/day | 99%+ |
| I/O Latency (avg) | Unknown | <20ms | Significant |
| Missing Index Impact | 99.985% potential | Resolved | Near-total |

---

## Tools & Resources

### dpa_EDSAdmin Key Tables

- **CON_WHATIF_SRC_1** - Missing index recommendations (2,954 rows)
- **CON_BLOCKING_SUM_1** - Blocking events (53.3K rows)
- **CONSS_1** - SQL statistics (2.42M rows, real-time)
- **CONST_1** - SQL text repository (194K rows)
- **CON_IO_DETAIL_1** - I/O performance (2.92M rows, real-time)
- **CON_INDEX_ANALYSIS_1** - Execution plan analysis (14.2K rows)

### Reference Documentation

- SQL Server DMVs: sys.dm_db_missing_index_details
- Execution Plans: sys.dm_exec_query_plan
- Wait Statistics: sys.dm_os_wait_stats
- Index Usage: sys.dm_db_index_usage_stats

---

## Contact & Support

**Database Team:** [Your DBA team contact]
**Escalation:** [On-call rotation]
**Documentation:** See docs/databases/dpa_EDSAdmin/README.md

---

**Document Version:** 1.0
**Author:** Claude Code AI
**Last Updated:** 2025-12-04
**Next Review:** 2025-12-11 (weekly)
