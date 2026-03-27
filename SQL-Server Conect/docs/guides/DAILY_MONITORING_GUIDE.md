# Daily Performance Monitoring Guide

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
2. Open file: `C:\Users\conno\Desktop\Work\scripts\alert_dashboard.sql`
3. Ensure database is set to `dpa_EDSAdmin` (top-left dropdown)
4. Press F5 to execute
5. Review results in Results pane

### Option 2: Command Line (sqlcmd)

```bash
sqlcmd -S eds-sqlserver.eastus2.cloudapp.azure.com,1433 ^
       -d dpa_EDSAdmin ^
       -U your_username ^
       -P your_password ^
       -i scripts\alert_dashboard.sql ^
       -o output\dashboard_results.txt
```

### Option 3: PowerShell

```powershell
Invoke-Sqlcmd -ServerInstance "eds-sqlserver.eastus2.cloudapp.azure.com,1433" `
              -Database "dpa_EDSAdmin" `
              -InputFile "scripts\alert_dashboard.sql" `
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
2. Run: `python scripts\extract_missing_indexes.py`
3. Run: `python scripts\generate_index_scripts.py`
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
   - Save results to `output\dashboard_results\dashboard_YYYY-MM-DD.txt`

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
   - Run: `python scripts\validate_index_performance.py`
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
   - Run: `python scripts\generate_final_performance_report.py`
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
**Created**: 2025-12-04
**Last Updated**: 2025-12-04
**Maintained By**: DBA Team
