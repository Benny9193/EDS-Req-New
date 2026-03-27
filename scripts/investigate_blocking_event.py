"""
Investigate Blocking Event
Analyzes blocking events from dpa_EDSAdmin to identify root causes

Usage:
    python scripts/investigate_blocking_event.py --date YYYY-MM-DD [--hours N]

Arguments:
    --date: Date to investigate (e.g., 2025-05-10)
    --hours: Number of hours to analyze (default: 24)

Outputs:
    - output/performance/blocking_event_{date}_analysis.json
    - output/performance/blocking_event_{date}_report.md
    - output/performance/blocking_remediation_plan.md
"""

import sys
import os
import json
from datetime import datetime, timedelta

# Add scripts directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError, DatabaseQueryError
from logging_config import setup_logging


class BlockingEventInvestigator:
    """Investigates blocking events from dpa_EDSAdmin."""

    def __init__(self, database='dpa_EDSAdmin'):
        self.database = database
        self._db = None
        self.output_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'output', 'performance'
        )
        os.makedirs(self.output_dir, exist_ok=True)
        self.logger = setup_logging('investigate_blocking_event')

    def connect(self):
        """Connect to dpa_EDSAdmin database."""
        self.logger.info("Connecting to %s...", self.database)

        try:
            self._db = DatabaseConnection(database=self.database)
            self._db.connect()
            self.logger.info("Connected successfully")
        except DatabaseConnectionError as e:
            raise DatabaseConnectionError(
                f"Failed to connect to {self.database}: {e}"
            ) from e

    def disconnect(self):
        """Close database connection."""
        if self._db:
            self._db.disconnect()
            self.logger.info("Disconnected")

    def investigate_blocking(self, target_date, hours=24):
        """Investigate blocking events for a specific date.

        Args:
            target_date: Date to investigate (datetime object)
            hours: Number of hours to analyze

        Returns:
            Dictionary containing blocking event analysis
        """
        self.logger.info("=" * 80)
        self.logger.info("BLOCKING EVENT INVESTIGATION")
        self.logger.info("=" * 80)
        self.logger.info("Target Date: %s", target_date.strftime('%Y-%m-%d'))
        self.logger.info("Analysis Period: %d hours", hours)

        start_time = target_date
        end_time = target_date + timedelta(hours=hours)

        self.logger.info("Querying blocking events from %s to %s...",
                         start_time, end_time)

        # Query blocking summary with parameterized query
        query = """
        SELECT TOP 50
            CONVERT(VARCHAR, bs.DATEHOUR, 120) as BlockingDateTime,
            bs.DIMENSIONTYPE,
            CASE bs.DIMENSIONTYPE
                WHEN 'P' THEN 'Program/Application'
                WHEN 'D' THEN 'Database'
                WHEN 'E' THEN 'Event/Wait Type'
                WHEN 'U' THEN 'User'
                ELSE 'Unknown'
            END as DimensionTypeName,
            bs.DIMENSIONID,
            m.NAME as DimensionName,
            bs.BLEETIMESECS as BlockeeTimeSeconds,
            bs.BLERTIMESECS as BlockerTimeSeconds,
            bs.ROOTIMPACTSECS as RootImpactSeconds,
            bs.BLEETIMESECS / 3600.0 as BlockeeHours,
            bs.BLERTIMESECS / 3600.0 as BlockerHours,
            bs.ROOTIMPACTSECS / 3600.0 as RootImpactHours
        FROM CON_BLOCKING_SUM_1 bs
        LEFT JOIN CONM_1 m ON bs.DIMENSIONID = m.ID
        WHERE bs.DATEHOUR >= ?
            AND bs.DATEHOUR < ?
            AND bs.BLEETIMESECS > 0
        ORDER BY bs.BLEETIMESECS DESC
        """

        rows = self._db.execute_query(query, (start_time, end_time))

        events = []
        total_blockee_hours = 0
        total_blocker_hours = 0
        total_root_impact_hours = 0

        for row in rows:
            event = {
                'datetime': str(row[0]),
                'dimension_type': row[1],
                'dimension_type_name': row[2],
                'dimension_id': row[3],
                'dimension_name': row[4],
                'blockee_seconds': row[5],
                'blocker_seconds': row[6],
                'root_impact_seconds': row[7],
                'blockee_hours': round(row[8], 2),
                'blocker_hours': round(row[9], 2),
                'root_impact_hours': round(row[10], 2)
            }
            events.append(event)

            total_blockee_hours += event['blockee_hours']
            total_blocker_hours += event['blocker_hours']
            total_root_impact_hours += event['root_impact_hours']

        self.logger.info("[OK] Found %d blocking events", len(events))

        # Analyze by dimension type
        by_type = {}
        for event in events:
            dim_type = event['dimension_type_name']
            if dim_type not in by_type:
                by_type[dim_type] = {
                    'count': 0,
                    'total_blockee_hours': 0,
                    'events': []
                }

            by_type[dim_type]['count'] += 1
            by_type[dim_type]['total_blockee_hours'] += event['blockee_hours']
            by_type[dim_type]['events'].append(event)

        # Identify top blockers
        top_blockers = {}
        for event in events:
            key = f"{event['dimension_type_name']}: {event['dimension_name'] or 'Unknown'}"
            if key not in top_blockers:
                top_blockers[key] = {
                    'count': 0,
                    'total_blockee_hours': 0,
                    'max_single_event_hours': 0
                }

            top_blockers[key]['count'] += 1
            top_blockers[key]['total_blockee_hours'] += event['blockee_hours']
            top_blockers[key]['max_single_event_hours'] = max(
                top_blockers[key]['max_single_event_hours'],
                event['blockee_hours']
            )

        # Sort top blockers by total blockee time
        top_blockers_sorted = sorted(
            top_blockers.items(),
            key=lambda x: x[1]['total_blockee_hours'],
            reverse=True
        )[:10]

        analysis = {
            'investigation_date': datetime.now().isoformat(),
            'target_date': target_date.strftime('%Y-%m-%d'),
            'analysis_period_hours': hours,
            'summary': {
                'total_events': len(events),
                'total_blockee_hours': round(total_blockee_hours, 2),
                'total_blocker_hours': round(total_blocker_hours, 2),
                'total_root_impact_hours': round(total_root_impact_hours, 2),
                'max_single_event_hours': max([e['blockee_hours'] for e in events]) if events else 0
            },
            'by_dimension_type': by_type,
            'top_blockers': [
                {
                    'name': name,
                    'count': data['count'],
                    'total_blockee_hours': round(data['total_blockee_hours'], 2),
                    'max_single_event_hours': round(data['max_single_event_hours'], 2)
                }
                for name, data in top_blockers_sorted
            ],
            'all_events': events
        }

        self.print_summary(analysis)

        return analysis

    def print_summary(self, analysis):
        """Print blocking analysis summary to console."""
        print("BLOCKING SUMMARY")
        print("="*80)
        summary = analysis['summary']
        print(f"Total Blocking Events: {summary['total_events']}")
        print(f"Total Blockee Time: {summary['total_blockee_hours']:.2f} hours")
        print(f"Total Blocker Time: {summary['total_blocker_hours']:.2f} hours")
        print(f"Total Root Impact: {summary['total_root_impact_hours']:.2f} hours")
        print(f"Max Single Event: {summary['max_single_event_hours']:.2f} hours\n")

        print("TOP 10 BLOCKERS (by total blockee time)")
        print("-"*80)
        print(f"{'Blocker':<50} {'Events':<10} {'Total Hrs':<12} {'Max Event':<12}")
        print("-"*80)

        for blocker in analysis['top_blockers']:
            name = blocker['name'][:48]
            print(f"{name:<50} {blocker['count']:<10} {blocker['total_blockee_hours']:<12.2f} {blocker['max_single_event_hours']:<12.2f}")

        print("="*80 + "\n")

    def save_analysis(self, analysis, target_date):
        """Save analysis to JSON file."""
        date_str = target_date.strftime('%Y-%m-%d')
        output_file = os.path.join(self.output_dir, f'blocking_event_{date_str}_analysis.json')

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(analysis, f, indent=2)

        print(f"[OK] Analysis saved to: {output_file}")

    def generate_report(self, analysis, target_date):
        """Generate markdown report."""
        date_str = target_date.strftime('%Y-%m-%d')
        output_file = os.path.join(self.output_dir, f'blocking_event_{date_str}_report.md')

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"""# Blocking Event Investigation Report

**Target Date:** {target_date.strftime('%Y-%m-%d')}
**Investigation Date:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Analysis Period:** {analysis['analysis_period_hours']} hours
**Source:** dpa_EDSAdmin database

---

## Executive Summary

""")

            summary = analysis['summary']
            f.write(f"""
Critical blocking event detected on {target_date.strftime('%Y-%m-%d')}:

- **Total Blocking Events:** {summary['total_events']}
- **Total Blockee Time:** {summary['total_blockee_hours']:.2f} hours
- **Total Blocker Time:** {summary['total_blocker_hours']:.2f} hours
- **Root Impact:** {summary['total_root_impact_hours']:.2f} hours
- **Max Single Event:** {summary['max_single_event_hours']:.2f} hours

""")

            if summary['total_blockee_hours'] > 100:
                f.write("""
**SEVERITY:** CRITICAL - Over 100 hours of cumulative blocking time detected

**IMMEDIATE ACTION REQUIRED:**
1. Identify root blocker (see Top Blockers section)
2. Review application code for long-running transactions
3. Consider enabling snapshot isolation
4. Implement blocking alerts

""")

            f.write("""---

## Top 10 Blockers (by Total Blockee Time)

""")

            f.write("| Blocker | Event Count | Total Blockee Hours | Max Single Event |\n")
            f.write("|---------|-------------|---------------------|------------------|\n")

            for blocker in analysis['top_blockers']:
                name = blocker['name']
                count = blocker['count']
                total = blocker['total_blockee_hours']
                max_event = blocker['max_single_event_hours']
                f.write(f"| {name} | {count} | {total:.2f} | {max_event:.2f} |\n")

            f.write("""
---

## Analysis by Dimension Type

""")

            for dim_type, data in analysis['by_dimension_type'].items():
                f.write(f"""
### {dim_type}

- **Event Count:** {data['count']}
- **Total Blockee Time:** {data['total_blockee_hours']:.2f} hours

""")

            # Root cause analysis
            f.write("""---

## Root Cause Analysis

""")

            if analysis['top_blockers']:
                top_blocker = analysis['top_blockers'][0]
                f.write(f"""
### Suspected Root Cause

**Primary Blocker:** {top_blocker['name']}
- Event Count: {top_blocker['count']}
- Total Impact: {top_blocker['total_blockee_hours']:.2f} hours

### Investigation Steps

1. **Identify the blocker:**
   - Review the primary blocker details above
   - Determine if it's a specific application, database, or process

2. **Review transaction logs:**
   - Check SQL Server error logs for {target_date.strftime('%Y-%m-%d')}
   - Look for long-running transactions
   - Identify any application deployments or batch jobs

3. **Analyze query patterns:**
   - Review query execution history for the blocker
   - Look for queries holding locks for extended periods
   - Check for missing indexes causing table scans

4. **Application review:**
   - If blocker is a program/application, review code for:
     - Explicit transactions not being committed
     - Batch operations without commit intervals
     - Inefficient queries within transactions

""")

            f.write("""---

## Recommended Actions

### Immediate (Within 24 hours)

1. **Enable Blocking Alerts**
   - Set up SQL Agent job to alert on blocking >5 minutes
   - Configure email notifications to DBA team
   - See: PERFORMANCE_RECOMMENDATIONS.md for alert setup

2. **Review Application Code**
   - Identify application causing blocking (from Top Blockers)
   - Review transaction handling
   - Check for missing COMMIT statements

### Short-term (Within 1 week)

3. **Enable READ_COMMITTED_SNAPSHOT Isolation**
   ```sql
   ALTER DATABASE [YourDatabase]
   SET READ_COMMITTED_SNAPSHOT ON
   WITH ROLLBACK IMMEDIATE;
   ```
   - Reduces blocking for read queries
   - Test in development first
   - Monitor tempdb growth

4. **Optimize Long-Running Queries**
   - Implement missing indexes (see missing index recommendations)
   - Break up large batch operations
   - Add explicit COMMIT every N rows in batch jobs

5. **Implement Query Hints (Where Appropriate)**
   - Use NOLOCK for reporting queries (if dirty reads acceptable)
   - Use READPAST for queue processing
   - Document all hints added

### Long-term (Within 1 month)

6. **Transaction Isolation Review**
   - Audit all application transaction isolation levels
   - Implement snapshot isolation for reporting workloads
   - Minimize transaction duration

7. **Monitoring & Alerting**
   - Implement real-time blocking dashboard
   - Set up automated blocking reports (daily)
   - Configure escalation for blocking >30 minutes

8. **Application Architecture**
   - Review batch job scheduling
   - Implement retry logic for blocked queries
   - Consider queue-based processing for high-contention tables

---

## Follow-up Actions

- [ ] Review this report with DBA team
- [ ] Identify root cause blocker
- [ ] Test remediation in development environment
- [ ] Implement blocking alerts (see remediation plan)
- [ ] Monitor for recurrence over next 30 days

---

**Report Version:** 1.0
**Generated by:** investigate_blocking_event.py
**Next Review:** {(datetime.now() + timedelta(days=7)).strftime('%Y-%m-%d')}
""")

        print(f"[OK] Report saved to: {output_file}")

    def generate_remediation_plan(self):
        """Generate blocking remediation plan."""
        output_file = os.path.join(self.output_dir, 'blocking_remediation_plan.md')

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"""# Blocking Remediation Plan

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Purpose:** Prevent and mitigate SQL Server blocking events

---

## Strategy 1: Enable READ_COMMITTED_SNAPSHOT Isolation

**Benefit:** Reduces blocking for read queries by using row versioning

**Implementation:**

```sql
-- For each user database (NOT master, tempdb, msdb, model)
ALTER DATABASE [YourDatabase]
SET READ_COMMITTED_SNAPSHOT ON
WITH ROLLBACK IMMEDIATE;
```

**Prerequisites:**
- Verify tempdb has adequate space (monitor after enabling)
- Test in development environment first
- Notify application teams

**Risks:**
- Tempdb growth (requires monitoring)
- Increased I/O on tempdb
- Older data versions may be read (by design)

**Rollback:**
```sql
ALTER DATABASE [YourDatabase]
SET READ_COMMITTED_SNAPSHOT OFF;
```

---

## Strategy 2: Optimize Transaction Duration

**Principle:** Minimize time transactions hold locks

**Implementation:**

### 2.1 Review Explicit Transactions
```sql
-- BAD: Long transaction holding locks
BEGIN TRANSACTION
    -- 10,000 row update
    UPDATE LargeTable SET Status = 'Processed'
    WHERE BatchID = @BatchID
    -- Other operations
COMMIT TRANSACTION

-- GOOD: Batch with periodic commits
DECLARE @BatchSize INT = 1000
WHILE EXISTS (SELECT 1 FROM LargeTable WHERE BatchID = @BatchID AND Status = 'Pending')
BEGIN
    UPDATE TOP (@BatchSize) LargeTable
    SET Status = 'Processed'
    WHERE BatchID = @BatchID AND Status = 'Pending'

    COMMIT -- Commit every batch
END
```

### 2.2 Review Application Code
- Search for BEGIN TRANSACTION without corresponding COMMIT
- Check error handling (ensure ROLLBACK on errors)
- Minimize operations within transactions

---

## Strategy 3: Query Hints for Specific Scenarios

**Use cautiously and document each instance**

### 3.1 NOLOCK (Dirty Reads)
```sql
-- For reporting queries where dirty reads acceptable
SELECT * FROM Orders WITH (NOLOCK)
WHERE OrderDate >= '2025-01-01'
```

**When to use:**
- Reporting queries
- Dashboard queries
- Analytics workloads
- Non-critical data

**When NOT to use:**
- Financial transactions
- Inventory management
- Critical business logic

### 3.2 READPAST (Skip Locked Rows)
```sql
-- For queue processing (skip locked items)
UPDATE TOP (1) WorkQueue WITH (READPAST)
SET Status = 'Processing', WorkerID = @WorkerID
WHERE Status = 'Pending'
```

**When to use:**
- Queue processing systems
- Work item processing
- Concurrent worker scenarios

---

## Strategy 4: Implement Blocking Alerts

**SQL Agent Job - Blocking Alert (Run every 15 minutes)**

```sql
USE msdb;
GO

-- Create operator for alerts (configure email first)
EXEC msdb.dbo.sp_add_operator
    @name = N'DBATeam',
    @email_address = N'dba-team@company.com';
GO

-- Create job
EXEC msdb.dbo.sp_add_job
    @job_name = N'Alert - Blocking Events',
    @enabled = 1,
    @description = N'Alert on blocking events >5 minutes';
GO

-- Add job step
EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'Alert - Blocking Events',
    @step_name = N'Check for Blocking',
    @subsystem = N'TSQL',
    @command = N'
DECLARE @BlockingCount INT;
DECLARE @TotalBlockingMinutes FLOAT;
DECLARE @EmailBody NVARCHAR(MAX);

-- Check dpa_EDSAdmin for recent blocking
SELECT
    @BlockingCount = COUNT(*),
    @TotalBlockingMinutes = SUM(BLEETIMESECS) / 60.0
FROM dpa_EDSAdmin.dbo.CON_BLOCKING_SUM_1
WHERE DATEHOUR >= DATEADD(minute, -15, GETDATE())
    AND BLEETIMESECS > 300;  -- Over 5 minutes

IF @BlockingCount > 0
BEGIN
    SET @EmailBody = ''Blocking detected: '' + CAST(@BlockingCount AS VARCHAR) + '' events, Total: '' + CAST(@TotalBlockingMinutes AS VARCHAR) + '' minutes'';

    EXEC msdb.dbo.sp_send_dbmail
        @profile_name = ''Default'',
        @recipients = ''dba-team@company.com'',
        @subject = ''SQL Server Blocking Alert'',
        @body = @EmailBody;
END
';
GO

-- Schedule job (every 15 minutes)
EXEC msdb.dbo.sp_add_jobschedule
    @job_name = N'Alert - Blocking Events',
    @name = N'Every 15 minutes',
    @freq_type = 4,  -- Daily
    @freq_interval = 1,
    @freq_subday_type = 4,  -- Minutes
    @freq_subday_interval = 15;
GO

EXEC msdb.dbo.sp_add_jobserver
    @job_name = N'Alert - Blocking Events',
    @server_name = N'(local)';
GO
```

---

## Strategy 5: Index Optimization

**Cross-reference with missing index recommendations**

Implementing missing indexes reduces:
- Table scan duration
- Lock hold time
- Blocking frequency

See: `create_missing_indexes_top_10.sql`

---

## Implementation Timeline

### Week 1: Monitoring & Analysis
- [ ] Implement blocking alerts
- [ ] Review blocking patterns for 7 days
- [ ] Identify top blocking sources

### Week 2: Quick Wins
- [ ] Add query hints to non-critical reporting queries
- [ ] Review and optimize explicit transactions in batch jobs
- [ ] Implement top 5 missing indexes

### Week 3: Snapshot Isolation (Test)
- [ ] Enable READ_COMMITTED_SNAPSHOT in test environment
- [ ] Monitor tempdb growth
- [ ] Validate application behavior
- [ ] Performance test

### Week 4: Snapshot Isolation (Production)
- [ ] Enable READ_COMMITTED_SNAPSHOT in production
- [ ] Monitor for 48 hours
- [ ] Rollback if critical issues
- [ ] Document results

---

## Success Metrics

**Baseline (Current State):**
- Review blocking event report for current metrics

**Target State (30 days):**
- Blocking events: <1 hour/day total
- Max single blocking event: <5 minutes
- Blocking alerts: <5 per day

---

## Rollback Plans

### If READ_COMMITTED_SNAPSHOT Causes Issues:
```sql
ALTER DATABASE [YourDatabase]
SET READ_COMMITTED_SNAPSHOT OFF;
```

### If Query Hints Cause Data Issues:
- Remove NOLOCK/READPAST hints
- Document which queries modified
- Test application thoroughly

---

## Monitoring Queries

### Check Current Blocking:
```sql
SELECT
    blocking_session_id,
    wait_duration_ms / 1000.0 as wait_seconds,
    wait_type,
    DB_NAME(database_id) as database_name,
    OBJECT_NAME(object_id) as object_name
FROM sys.dm_exec_requests
WHERE blocking_session_id <> 0
ORDER BY wait_duration_ms DESC;
```

### Check READ_COMMITTED_SNAPSHOT Status:
```sql
SELECT name, is_read_committed_snapshot_on
FROM sys.databases
WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb');
```

---

**Plan Version:** 1.0
**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Status:** Ready for Implementation
""")

        print(f"[OK] Remediation plan saved to: {output_file}")


def main():
    """Main execution."""
    import argparse

    parser = argparse.ArgumentParser(description='Investigate blocking events')
    parser.add_argument('--date', type=str, required=True, help='Date to investigate (YYYY-MM-DD)')
    parser.add_argument('--hours', type=int, default=24, help='Number of hours to analyze (default: 24)')

    args = parser.parse_args()

    # Parse target date
    try:
        target_date = datetime.strptime(args.date, '%Y-%m-%d')
    except ValueError:
        print("[ERROR] Invalid date format. Use YYYY-MM-DD")
        return 1

    print("\n" + "="*80)
    print("BLOCKING EVENT INVESTIGATOR")
    print("="*80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        investigator = BlockingEventInvestigator()
        investigator.connect()

        analysis = investigator.investigate_blocking(target_date, args.hours)

        if analysis['summary']['total_events'] > 0:
            investigator.save_analysis(analysis, target_date)
            investigator.generate_report(analysis, target_date)
            investigator.generate_remediation_plan()
        else:
            print("[INFO] No blocking events found for the specified date/period")

        investigator.disconnect()

        print("\n" + "="*80)
        print("INVESTIGATION COMPLETE")
        print("="*80)
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Events Found: {analysis['summary']['total_events']}")
        print("="*80)

        return 0

    except Exception as e:
        print(f"\n[ERROR] Investigation failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
