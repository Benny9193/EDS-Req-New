#!/usr/bin/env python3
"""
Generate Alert Dashboard SQL Query
===================================
Creates comprehensive SQL queries for daily performance monitoring dashboard.

This script generates:
1. alert_dashboard.sql - Complete SQL query for daily monitoring
2. DAILY_MONITORING_GUIDE.md - Usage instructions for operations team

Metrics Included:
- New missing indexes (last 24 hours)
- Blocking events (last hour)
- I/O latency spikes (>100ms avg in last hour)
- Slow queries (>10M buffer gets)
- Overall database health summary

Output Files:
- scripts/alert_dashboard.sql
- docs/guides/DAILY_MONITORING_GUIDE.md

Usage:
    python scripts/generate_alert_dashboard.py

    # Then run the generated SQL:
    sqlcmd -S server -d dpa_EDSAdmin -i scripts/alert_dashboard.sql
"""

import os
import sys
from datetime import datetime

def generate_dashboard_sql():
    """Generate comprehensive dashboard SQL query."""

    sql = """/*
================================================================================
SQL Server Performance Monitoring Dashboard
================================================================================
Purpose: Daily summary of key performance metrics from dpa_EDSAdmin

Run this query each morning to get overnight performance summary.
Review all sections for potential issues requiring investigation.

Generated: {timestamp}
================================================================================
*/

USE dpa_EDSAdmin;
GO

PRINT '================================================================================'
PRINT 'SQL SERVER PERFORMANCE DASHBOARD - {date}'
PRINT '================================================================================'
PRINT ''

/*
================================================================================
SECTION 1: NEW MISSING INDEXES (Last 24 Hours)
================================================================================
High-impact missing index recommendations identified since yesterday.
Action: Review indexes with EST_SAVING > 95% for immediate implementation.
*/

PRINT '1. NEW MISSING INDEXES (Last 24 Hours)'
PRINT '--------------------------------------'

SELECT TOP 20
    CONVERT(VARCHAR, w.D, 120) as DateIdentified,
    w.EST_SAVING as EstSavingPercent,
    w.SQL_EXECS as Executions,
    fq.ODATABASE as DatabaseName,
    fq.OSCHEMA + '.' + fq.ONAME as TableName,
    fq.OINDEX_COLUMNS as IndexColumns,
    CASE
        WHEN w.EST_SAVING > 95 THEN 'CRITICAL'
        WHEN w.EST_SAVING > 80 THEN 'HIGH'
        WHEN w.EST_SAVING > 50 THEN 'MEDIUM'
        ELSE 'LOW'
    END as Priority
FROM CON_WHATIF_SRC_1 w
LEFT JOIN CON_FQ_OBJECT_1 fq ON w.IDX_ID = fq.ID
WHERE w.D >= DATEADD(day, -1, GETDATE())
    AND w.EST_SAVING >= 50  -- Only show indexes with 50%+ improvement potential
ORDER BY w.EST_SAVING DESC, w.SQL_EXECS DESC;

DECLARE @NewHighImpactIndexes INT
SELECT @NewHighImpactIndexes = COUNT(*)
FROM CON_WHATIF_SRC_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND EST_SAVING > 95;

PRINT ''
PRINT 'Summary: ' + CAST(@NewHighImpactIndexes AS VARCHAR) + ' new high-impact indexes (>95% improvement) detected'
PRINT ''

/*
================================================================================
SECTION 2: BLOCKING EVENTS (Last 24 Hours)
================================================================================
Blocking events that caused significant wait time.
Action: Investigate events >5 minutes. Review query patterns causing blocks.
*/

PRINT '2. BLOCKING EVENTS (Last 24 Hours)'
PRINT '-----------------------------------'

SELECT TOP 15
    CONVERT(VARCHAR, bs.DATEHOUR, 120) as BlockingDateTime,
    CASE bs.DIMENSIONTYPE
        WHEN 'P' THEN 'Program'
        WHEN 'D' THEN 'Database'
        WHEN 'E' THEN 'Event'
        ELSE 'Unknown'
    END as BlockingType,
    m.NAME as BlockingEntity,
    CAST(bs.BLEETIMESECS / 60.0 AS DECIMAL(10,2)) as BlockeeMinutes,
    CAST(bs.BLERTIMESECS / 60.0 AS DECIMAL(10,2)) as BlockerMinutes,
    CASE
        WHEN bs.BLEETIMESECS > 3600 THEN 'CRITICAL'
        WHEN bs.BLEETIMESECS > 300 THEN 'HIGH'
        WHEN bs.BLEETIMESECS > 60 THEN 'MEDIUM'
        ELSE 'LOW'
    END as Severity
FROM CON_BLOCKING_SUM_1 bs
LEFT JOIN CONM_1 m ON bs.DIMENSIONID = m.ID
WHERE bs.DATEHOUR >= DATEADD(day, -1, GETDATE())
    AND bs.BLEETIMESECS > 60  -- Only show blocking >1 minute
ORDER BY bs.BLEETIMESECS DESC;

DECLARE @TotalBlockingHours DECIMAL(10,2)
DECLARE @BlockingEventCount INT

SELECT
    @TotalBlockingHours = CAST(SUM(BLEETIMESECS) / 3600.0 AS DECIMAL(10,2)),
    @BlockingEventCount = COUNT(*)
FROM CON_BLOCKING_SUM_1
WHERE DATEHOUR >= DATEADD(day, -1, GETDATE())
    AND BLEETIMESECS > 60;

PRINT ''
PRINT 'Summary: ' + CAST(@BlockingEventCount AS VARCHAR) + ' blocking events, ' + CAST(@TotalBlockingHours AS VARCHAR) + ' hours total blockee time'
PRINT ''

/*
================================================================================
SECTION 3: I/O LATENCY SPIKES (Last 24 Hours)
================================================================================
Periods where disk I/O latency exceeded acceptable thresholds.
Action: Investigate spikes >100ms average. Check storage health.
*/

PRINT '3. I/O LATENCY SPIKES (Last 24 Hours)'
PRINT '--------------------------------------'

SELECT TOP 20
    CONVERT(VARCHAR, D, 120) as DateTime,
    CAST(READ_LATENCY AS DECIMAL(10,2)) as AvgReadLatencyMS,
    CAST(WRITE_LATENCY AS DECIMAL(10,2)) as AvgWriteLatencyMS,
    CAST(TOTAL_LATENCY AS DECIMAL(10,2)) as TotalLatencyMS,
    CASE
        WHEN READ_LATENCY > 200 OR WRITE_LATENCY > 200 THEN 'CRITICAL'
        WHEN READ_LATENCY > 100 OR WRITE_LATENCY > 100 THEN 'HIGH'
        WHEN READ_LATENCY > 50 OR WRITE_LATENCY > 50 THEN 'MEDIUM'
        ELSE 'LOW'
    END as Severity
FROM CON_IO_DETAIL_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND (READ_LATENCY > 50 OR WRITE_LATENCY > 50)  -- Only show problematic latency
ORDER BY TOTAL_LATENCY DESC;

DECLARE @MaxReadLatency DECIMAL(10,2)
DECLARE @AvgReadLatency DECIMAL(10,2)
DECLARE @HighLatencyCount INT

SELECT
    @MaxReadLatency = CAST(MAX(READ_LATENCY) AS DECIMAL(10,2)),
    @AvgReadLatency = CAST(AVG(READ_LATENCY) AS DECIMAL(10,2)),
    @HighLatencyCount = COUNT(*)
FROM CON_IO_DETAIL_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND READ_LATENCY > 100;

PRINT ''
PRINT 'Summary: ' + CAST(@HighLatencyCount AS VARCHAR) + ' high latency events (>100ms), Max: ' + CAST(@MaxReadLatency AS VARCHAR) + 'ms, Avg: ' + CAST(@AvgReadLatency AS VARCHAR) + 'ms'
PRINT ''

/*
================================================================================
SECTION 4: SLOW QUERIES (Last 24 Hours)
================================================================================
Queries with excessive buffer gets (logical reads), indicating potential issues.
Action: Review queries >10M buffer gets. Check for missing indexes or bad plans.
*/

PRINT '4. SLOW QUERIES (Last 24 Hours)'
PRINT '--------------------------------'

SELECT TOP 15
    CONVERT(VARCHAR, qp.D, 120) as DateTime,
    qp.SQL_HASH as QueryHash,
    CAST(qp.SQL_BUFFER_GETS / 1000000.0 AS DECIMAL(10,2)) as BufferGetsMillions,
    qp.SQL_EXECS as Executions,
    CAST(qp.SQL_BUFFER_GETS / NULLIF(qp.SQL_EXECS, 0) AS BIGINT) as AvgBufferGetsPerExec,
    CAST(qp.SQL_ELAPSED_TIME / 1000.0 AS DECIMAL(10,2)) as ElapsedTimeSeconds,
    CASE
        WHEN qp.SQL_BUFFER_GETS > 100000000 THEN 'CRITICAL'
        WHEN qp.SQL_BUFFER_GETS > 10000000 THEN 'HIGH'
        WHEN qp.SQL_BUFFER_GETS > 1000000 THEN 'MEDIUM'
        ELSE 'LOW'
    END as Severity
FROM CON_QUERY_PLAN_1 qp
WHERE qp.D >= DATEADD(day, -1, GETDATE())
    AND qp.SQL_BUFFER_GETS > 10000000  -- >10M buffer gets
ORDER BY qp.SQL_BUFFER_GETS DESC;

DECLARE @SlowQueryCount INT
SELECT @SlowQueryCount = COUNT(DISTINCT SQL_HASH)
FROM CON_QUERY_PLAN_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND SQL_BUFFER_GETS > 10000000;

PRINT ''
PRINT 'Summary: ' + CAST(@SlowQueryCount AS VARCHAR) + ' distinct slow queries detected (>10M buffer gets)'
PRINT ''

/*
================================================================================
SECTION 5: DATABASE HEALTH SUMMARY
================================================================================
Overall health indicators for the past 24 hours.
*/

PRINT '5. DATABASE HEALTH SUMMARY (Last 24 Hours)'
PRINT '-------------------------------------------'

DECLARE @HealthScore INT = 100

-- Deduct points for issues
IF @NewHighImpactIndexes > 10 SET @HealthScore = @HealthScore - 20
IF @NewHighImpactIndexes > 5 SET @HealthScore = @HealthScore - 10

IF @TotalBlockingHours > 5 SET @HealthScore = @HealthScore - 25
IF @TotalBlockingHours > 1 SET @HealthScore = @HealthScore - 10

IF @HighLatencyCount > 100 SET @HealthScore = @HealthScore - 25
IF @HighLatencyCount > 50 SET @HealthScore = @HealthScore - 15

IF @SlowQueryCount > 20 SET @HealthScore = @HealthScore - 20
IF @SlowQueryCount > 10 SET @HealthScore = @HealthScore - 10

SELECT
    'Database Health Score' as Metric,
    CAST(@HealthScore AS VARCHAR) + '/100' as Value,
    CASE
        WHEN @HealthScore >= 90 THEN 'EXCELLENT'
        WHEN @HealthScore >= 75 THEN 'GOOD'
        WHEN @HealthScore >= 60 THEN 'FAIR'
        WHEN @HealthScore >= 40 THEN 'POOR'
        ELSE 'CRITICAL'
    END as Status

UNION ALL

SELECT
    'New High-Impact Indexes',
    CAST(@NewHighImpactIndexes AS VARCHAR),
    CASE
        WHEN @NewHighImpactIndexes = 0 THEN 'GOOD'
        WHEN @NewHighImpactIndexes < 5 THEN 'FAIR'
        WHEN @NewHighImpactIndexes < 10 THEN 'POOR'
        ELSE 'CRITICAL'
    END

UNION ALL

SELECT
    'Blocking Events (Hours)',
    CAST(@TotalBlockingHours AS VARCHAR),
    CASE
        WHEN @TotalBlockingHours = 0 THEN 'GOOD'
        WHEN @TotalBlockingHours < 1 THEN 'FAIR'
        WHEN @TotalBlockingHours < 5 THEN 'POOR'
        ELSE 'CRITICAL'
    END

UNION ALL

SELECT
    'High I/O Latency Events',
    CAST(@HighLatencyCount AS VARCHAR),
    CASE
        WHEN @HighLatencyCount = 0 THEN 'GOOD'
        WHEN @HighLatencyCount < 50 THEN 'FAIR'
        WHEN @HighLatencyCount < 100 THEN 'POOR'
        ELSE 'CRITICAL'
    END

UNION ALL

SELECT
    'Slow Queries',
    CAST(@SlowQueryCount AS VARCHAR),
    CASE
        WHEN @SlowQueryCount = 0 THEN 'GOOD'
        WHEN @SlowQueryCount < 10 THEN 'FAIR'
        WHEN @SlowQueryCount < 20 THEN 'POOR'
        ELSE 'CRITICAL'
    END;

PRINT ''
PRINT '================================================================================'
PRINT 'END OF DASHBOARD - ' + CONVERT(VARCHAR, GETDATE(), 120)
PRINT '================================================================================'
PRINT ''
PRINT 'RECOMMENDED ACTIONS:'
PRINT '  1. Review all CRITICAL and HIGH severity items'
PRINT '  2. Implement high-impact missing indexes (>95% improvement)'
PRINT '  3. Investigate blocking events >5 minutes'
PRINT '  4. Check storage health if I/O latency >100ms'
PRINT '  5. Analyze slow queries for optimization opportunities'
PRINT ''

GO
""".format(
        timestamp=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        date=datetime.now().strftime('%Y-%m-%d')
    )

    return sql

def generate_monitoring_guide():
    """Generate daily monitoring guide documentation."""

    guide = """# Daily Performance Monitoring Guide

## Overview

This guide describes the daily performance monitoring workflow using the automated dashboard query.

**Dashboard Query**: `scripts/alert_dashboard.sql`
**Target Database**: `dpa_EDSAdmin`
**Frequency**: Daily (recommended: morning, before business hours)
**Duration**: ~30-60 seconds to execute

---

## Quick Start

### Option 1: SQL Server Management Studio (SSMS)

1. Open SSMS and connect to SQL Server
2. Open file: `C:\\Users\\conno\\Desktop\\Work\\scripts\\alert_dashboard.sql`
3. Ensure database is set to `dpa_EDSAdmin` (top-left dropdown)
4. Press F5 to execute
5. Review results in Results pane

### Option 2: Command Line (sqlcmd)

```bash
sqlcmd -S eds-sqlserver.eastus2.cloudapp.azure.com,1433 ^
       -d dpa_EDSAdmin ^
       -U your_username ^
       -P your_password ^
       -i scripts\\alert_dashboard.sql ^
       -o output\\dashboard_results.txt
```

### Option 3: PowerShell

```powershell
Invoke-Sqlcmd -ServerInstance "eds-sqlserver.eastus2.cloudapp.azure.com,1433" `
              -Database "dpa_EDSAdmin" `
              -InputFile "scripts\\alert_dashboard.sql" `
              -Username "your_username" `
              -Password "your_password"
```

---

## Dashboard Sections

### Section 1: New Missing Indexes (Last 24 Hours)

**What it shows**: Newly identified missing index recommendations with >50% estimated improvement

**Priority Levels**:
- **CRITICAL** (>95%): Implement immediately in test, deploy within 24 hours
- **HIGH** (80-95%): Schedule for implementation within 1 week
- **MEDIUM** (50-80%): Review and prioritize for monthly maintenance
- **LOW** (<50%): Not shown in dashboard

**Action Steps**:
1. Note all CRITICAL indexes
2. Run: `python scripts\\extract_missing_indexes.py`
3. Run: `python scripts\\generate_index_scripts.py`
4. Review generated CREATE INDEX scripts
5. Deploy to test environment first
6. Validate performance improvements
7. Deploy to production during maintenance window

**Red Flags**:
- More than 10 CRITICAL indexes in 24 hours → investigate query patterns
- Same table appearing repeatedly → consider redesigning queries

---

### Section 2: Blocking Events (Last 24 Hours)

**What it shows**: Blocking events where queries waited >1 minute for locks

**Severity Levels**:
- **CRITICAL** (>1 hour): Immediate investigation required
- **HIGH** (5-60 min): Investigate within 4 hours
- **MEDIUM** (1-5 min): Monitor, investigate if recurring
- **LOW** (<1 min): Not shown in dashboard

**Action Steps**:
1. Identify blocking entity (Program, Database, Event)
2. Check if blocking is recurring (same entity, time of day)
3. For recurring blocks:
   - Review transaction isolation levels
   - Consider enabling READ_COMMITTED_SNAPSHOT (already implemented)
   - Optimize long-running transactions
   - Add query hints (NOLOCK, READPAST) where appropriate
4. For one-time blocks:
   - Document and monitor
   - Investigate if blockee time >5 minutes

**Red Flags**:
- Total blocking >5 hours/day → critical issue, requires immediate action
- Same program blocking repeatedly → application bug or inefficient transactions
- Blocking during business hours → impacts user experience

---

### Section 3: I/O Latency Spikes (Last 24 Hours)

**What it shows**: Periods where disk read/write latency exceeded healthy thresholds

**Severity Levels**:
- **CRITICAL** (>200ms): Storage emergency, page DBA on-call
- **HIGH** (>100ms): Investigate within 1 hour
- **MEDIUM** (50-100ms): Monitor closely
- **LOW** (<50ms): Not shown in dashboard

**Action Steps**:
1. Check storage array health (SAN, Azure Premium Storage)
2. Review disk queue lengths in Performance Monitor
3. Check for heavy backup/maintenance jobs during spike times
4. Verify tempdb configuration (enough space, proper file count)
5. Check RAID controller cache status
6. Review I/O-intensive queries running during spike

**Healthy Baselines**:
- SSD: <10ms average, <50ms max
- Standard SSD: 10-20ms average, <100ms max
- HDD: 20-50ms average, <200ms max

**Red Flags**:
- Consistent >100ms latency → storage bottleneck
- Spikes correlating with business hours → capacity planning needed
- Sudden increase in max latency → storage hardware issue

---

### Section 4: Slow Queries (Last 24 Hours)

**What it shows**: Queries with >10 million buffer gets (excessive logical reads)

**Severity Levels**:
- **CRITICAL** (>100M buffer gets): Investigate immediately
- **HIGH** (10M-100M): Review within 24 hours
- **MEDIUM** (1M-10M): Not shown in dashboard (too many)
- **LOW** (<1M): Normal operation

**Action Steps**:
1. Copy SQL_HASH value
2. Query for full SQL text:
   ```sql
   SELECT SQL_TEXT
   FROM dpa_EDSAdmin.dbo.CON_QUERY_PLAN_1
   WHERE SQL_HASH = [hash_value]
   ```
3. Analyze execution plan
4. Check for missing indexes (Section 1)
5. Look for:
   - Table scans on large tables
   - Implicit conversions
   - Nested loops with high row counts
   - Missing WHERE clauses
   - Inefficient JOIN strategies

**Red Flags**:
- >20 slow queries/day → systemic issue with application queries
- Same query appearing repeatedly → prime candidate for index optimization
- Buffer gets increasing over time → data growth without index maintenance

---

### Section 5: Database Health Summary

**What it shows**: Aggregated health score (0-100) and status indicators

**Health Score Interpretation**:
- **90-100 (EXCELLENT)**: No action required, maintain current state
- **75-89 (GOOD)**: Minor issues, address during regular maintenance
- **60-74 (FAIR)**: Multiple issues detected, prioritize remediation this week
- **40-59 (POOR)**: Significant performance degradation, immediate action required
- **0-39 (CRITICAL)**: Emergency situation, escalate to senior DBA

**Health Score Calculation**:
```
Starting Score: 100
- New high-impact indexes >10: -20 points
- New high-impact indexes >5: -10 points
- Blocking >5 hours: -25 points
- Blocking >1 hour: -10 points
- High I/O latency events >100: -25 points
- High I/O latency events >50: -15 points
- Slow queries >20: -20 points
- Slow queries >10: -10 points
```

---

## Daily Workflow

### Morning Routine (15 minutes)

**Time: 8:00 AM - Before business hours**

1. **Execute Dashboard** (2 min)
   - Run `alert_dashboard.sql` in SSMS
   - Save results to `output\\dashboard_results\\dashboard_YYYY-MM-DD.txt`

2. **Review Health Score** (1 min)
   - Check overall health score
   - Note any CRITICAL or POOR status

3. **Triage Issues** (5 min)
   - Count CRITICAL items across all sections
   - Identify urgent action items (>5 min blocking, >100ms I/O latency, >95% missing indexes)

4. **Prioritize Actions** (5 min)
   - Create task list for the day
   - Escalate CRITICAL issues to senior DBA
   - Schedule index deployments

5. **Document** (2 min)
   - Log findings in DBA team log
   - Update performance tracking spreadsheet

---

## Weekly Review (30 minutes)

**Time: Friday afternoon**

1. **Trend Analysis**
   - Compare health scores across the week
   - Identify recurring issues (same blocking entity, same slow queries)
   - Plot I/O latency trends

2. **Index Implementation Review**
   - Verify deployed indexes are being used
   - Run: `python scripts\\validate_index_performance.py`
   - Drop unused indexes (0 seeks for 7+ days)

3. **Alert Tuning**
   - Review SQL Agent job alerts for false positives
   - Adjust thresholds if needed
   - Check alert email delivery

4. **Capacity Planning**
   - Review database growth trends
   - Check tempdb usage (for snapshot isolation)
   - Forecast storage needs for next 90 days

---

## Monthly Tasks

**Time: First Monday of each month (2 hours)**

1. **Comprehensive Performance Report**
   - Run: `python scripts\\generate_final_performance_report.py`
   - Review before/after metrics since last month

2. **Index Maintenance**
   - Identify fragmented indexes (>30% fragmentation)
   - Schedule REBUILD for critical indexes
   - Drop unused indexes (0 seeks for 30+ days)

3. **Alert History Review**
   - Query SQL Agent job history:
     ```sql
     EXEC msdb.dbo.sp_help_jobhistory
         @job_name = 'Alert - I/O Latency',
         @mode = 'SUMMARY'
     ```
   - Review blocking alert frequency
   - Tune thresholds if needed

4. **Documentation Update**
   - Update `PERFORMANCE_RECOMMENDATIONS.md` with completed items
   - Document new optimization opportunities
   - Update runbook with lessons learned

---

## Escalation Procedures

### Severity 1: CRITICAL (Immediate Action)

**Triggers**:
- Health score <40
- I/O latency >500ms for >10 minutes
- Blocking >2 hours (single event)
- Total blocking >10 hours/day

**Actions**:
1. Page DBA on-call immediately
2. Execute emergency diagnostic scripts
3. Consider emergency maintenance window
4. Notify application team
5. Document incident for post-mortem

### Severity 2: HIGH (4-Hour Response)

**Triggers**:
- Health score 40-59
- I/O latency >200ms sustained
- Blocking 1-2 hours
- >20 CRITICAL missing indexes

**Actions**:
1. Email DBA team lead
2. Create incident ticket
3. Begin investigation
4. Schedule remediation within 24 hours

### Severity 3: MEDIUM (24-Hour Response)

**Triggers**:
- Health score 60-74
- I/O latency 100-200ms
- Blocking 5-60 minutes
- 10-20 HIGH missing indexes

**Actions**:
1. Log in DBA team log
2. Add to weekly maintenance plan
3. Monitor for escalation

---

## Troubleshooting

### Dashboard Query Times Out

**Cause**: dpa_EDSAdmin database too large or poorly indexed

**Solution**:
1. Add WHERE clause to limit time range (e.g., last 12 hours instead of 24)
2. Check dpa_EDSAdmin database maintenance (index fragmentation)
3. Verify tempdb has adequate space
4. Contact SolarWinds support for DPA performance tuning

### No Data Returned

**Cause**: dpa_EDSAdmin not collecting data or connection issues

**Solution**:
1. Verify DPA data collection service is running
2. Check SQL Server Agent jobs in dpa_EDSAdmin
3. Review DPA logs for errors
4. Test connectivity: `SELECT TOP 10 * FROM dpa_EDSAdmin.dbo.CON_WHATIF_SRC_1`

### Health Score Always Low

**Cause**: Thresholds too aggressive or systemic performance issues

**Solution**:
1. Review scoring logic in dashboard query
2. Adjust thresholds based on baseline performance
3. If legitimate issues, escalate for architectural review

---

## Reference

### Related Scripts
- `scripts/capture_performance_baseline.py` - Capture performance metrics
- `scripts/extract_missing_indexes.py` - Extract top missing index recommendations
- `scripts/generate_index_scripts.py` - Generate CREATE INDEX statements
- `scripts/investigate_blocking_event.py` - Detailed blocking analysis
- `scripts/validate_index_performance.py` - Validate index usage after deployment

### SQL Agent Jobs
- **Alert - I/O Latency**: Every 5 minutes, >100ms avg or >500ms max
- **Alert - Blocking Events**: Every 15 minutes, >5 minutes blocking
- **Alert - Missing Indexes**: Daily at 8 AM, >95% improvement potential

### Documentation
- `PERFORMANCE_RECOMMENDATIONS.md` - Original performance analysis findings
- `docs/guides/PERFORMANCE_MONITORING_RUNBOOK.md` - Detailed operations runbook
- `docs/guides/INDEX_MAINTENANCE_GUIDE.md` - Index lifecycle management

---

## Contact

**DBA Team**: dba-team@company.com
**DBA On-Call**: dba-oncall@company.com
**Escalation**: Senior DBA Manager

---

**Document Version**: 1.0
**Created**: {date}
**Last Updated**: {date}
**Maintained By**: DBA Team
""".format(date=datetime.now().strftime('%Y-%m-%d'))

    return guide

def main():
    """Main execution function."""

    print("=" * 80)
    print("Generate Alert Dashboard")
    print("=" * 80)
    print()

    # Create output directories if needed
    scripts_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_guides_dir = os.path.join(scripts_dir, 'docs', 'guides')

    os.makedirs(docs_guides_dir, exist_ok=True)

    print("[1/2] Generating dashboard SQL query...")
    dashboard_sql = generate_dashboard_sql()

    sql_output_path = os.path.join(scripts_dir, 'scripts', 'alert_dashboard.sql')
    with open(sql_output_path, 'w', encoding='utf-8') as f:
        f.write(dashboard_sql)

    print(f"[OK] Dashboard SQL written to: {sql_output_path}")
    print()

    print("[2/2] Generating daily monitoring guide...")
    monitoring_guide = generate_monitoring_guide()

    guide_output_path = os.path.join(docs_guides_dir, 'DAILY_MONITORING_GUIDE.md')
    with open(guide_output_path, 'w', encoding='utf-8') as f:
        f.write(monitoring_guide)

    print(f"[OK] Monitoring guide written to: {guide_output_path}")
    print()

    print("=" * 80)
    print("DASHBOARD GENERATION COMPLETE")
    print("=" * 80)
    print()
    print("Generated Files:")
    print(f"  1. {sql_output_path}")
    print(f"  2. {guide_output_path}")
    print()
    print("Usage:")
    print("  1. Execute dashboard query:")
    print(f"     sqlcmd -S server -d dpa_EDSAdmin -i \"{sql_output_path}\"")
    print()
    print("  2. Or open in SSMS:")
    print(f"     File -> Open -> {sql_output_path}")
    print()
    print("  3. Read usage guide:")
    print(f"     {guide_output_path}")
    print()
    print("Dashboard Query Features:")
    print("  - New missing indexes (last 24 hours)")
    print("  - Blocking events (last 24 hours)")
    print("  - I/O latency spikes (last 24 hours)")
    print("  - Slow queries (>10M buffer gets)")
    print("  - Database health score (0-100)")
    print()
    print("Next Steps:")
    print("  1. Test dashboard query in SSMS")
    print("  2. Review monitoring guide")
    print("  3. Add to daily morning routine")
    print("  4. Share with operations team")
    print()

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"[ERROR] {str(e)}")
        sys.exit(1)
