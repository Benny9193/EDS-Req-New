"""
Generate CREATE INDEX Scripts
Reads missing index recommendations and generates SQL scripts

Usage:
    python scripts/generate_index_scripts.py [--top N]

Arguments:
    --top: Number of top recommendations to generate scripts for (default: 10)

Inputs:
    - output/performance/missing_indexes_full.json

Outputs:
    - output/performance/create_missing_indexes_top_10.sql
    - output/performance/create_missing_indexes_all.sql
    - output/performance/index_implementation_plan.md
"""

import sys
import os
import json
from datetime import datetime

class IndexScriptGenerator:
    """Generates CREATE INDEX SQL scripts from missing index recommendations."""

    def __init__(self):
        self.output_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'output', 'performance'
        )
        self.recommendations = []

    def load_recommendations(self):
        """Load missing index recommendations from JSON file."""
        input_file = os.path.join(self.output_dir, 'missing_indexes_full.json')

        if not os.path.exists(input_file):
            raise FileNotFoundError(
                f"Missing index data not found: {input_file}\n"
                "Please run extract_missing_indexes.py first"
            )

        print(f"Loading recommendations from: {input_file}")

        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        self.recommendations = data.get('recommendations', [])
        print(f"[OK] Loaded {len(self.recommendations)} recommendations\n")

        return self.recommendations

    def generate_create_index_statement(self, rec):
        """Generate CREATE INDEX SQL statement for a single recommendation.

        Args:
            rec: Recommendation dictionary

        Returns:
            SQL script as string
        """
        db = rec.get('DatabaseName', 'UnknownDB')
        schema = rec.get('SchemaName', 'dbo')
        table = rec.get('TableName', 'UnknownTable')
        columns = rec.get('IndexColumns', '')
        included = rec.get('IncludedColumns', '')
        saving = rec.get('EstimatedSavingPercent', 0)
        execs = rec.get('Executions', 0)
        wait_time = rec.get('WaitTimeMS', 0)

        # Generate index name if not provided
        index_name = rec.get('IndexName')
        if not index_name:
            # Create index name from columns
            col_parts = columns.replace(', ', '_').replace(',', '_') if columns else 'Unknown'
            col_parts = col_parts.replace('[', '').replace(']', '')
            # Limit length
            if len(col_parts) > 50:
                col_parts = col_parts[:50]
            index_name = f"IX_{table}_{col_parts}"

        # Build CREATE INDEX statement
        script = f"""-- ============================================================================
-- Missing Index Recommendation
-- ============================================================================
-- Database: {db}
-- Table: {schema}.{table}
-- Estimated Improvement: {saving:.3f}%
-- Query Executions: {execs}
-- Wait Time: {wait_time} ms
-- Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
-- ============================================================================

USE [{db}];
GO

CREATE NONCLUSTERED INDEX [{index_name}]
ON [{schema}].[{table}] ({columns})
"""

        # Add INCLUDE clause if there are included columns
        if included:
            script += f"INCLUDE ({included})\n"

        # Add WITH options
        script += """WITH (
    ONLINE = ON,           -- Zero downtime (Enterprise Edition only)
    FILLFACTOR = 90,       -- Leave 10% free space for future inserts
    PAD_INDEX = ON,        -- Apply fillfactor to index pages
    SORT_IN_TEMPDB = ON,   -- Reduce load on user database
    STATISTICS_NORECOMPUTE = OFF
);
GO

"""

        # Add verification query
        script += f"""-- Verify index creation
SELECT
    i.name as IndexName,
    i.type_desc as IndexType,
    i.is_disabled
FROM sys.indexes i
JOIN sys.tables t ON i.object_id = t.object_id
WHERE t.name = '{table}'
    AND i.name = '{index_name}';
GO

"""

        return script

    def generate_drop_index_statement(self, rec):
        """Generate DROP INDEX statement for rollback.

        Args:
            rec: Recommendation dictionary

        Returns:
            DROP INDEX SQL statement
        """
        db = rec.get('DatabaseName', 'UnknownDB')
        schema = rec.get('SchemaName', 'dbo')
        table = rec.get('TableName', 'UnknownTable')
        columns = rec.get('IndexColumns', '')

        # Generate index name (must match create script)
        index_name = rec.get('IndexName')
        if not index_name:
            col_parts = columns.replace(', ', '_').replace(',', '_') if columns else 'Unknown'
            col_parts = col_parts.replace('[', '').replace(']', '')
            if len(col_parts) > 50:
                col_parts = col_parts[:50]
            index_name = f"IX_{table}_{col_parts}"

        script = f"""-- Rollback: Drop index {index_name}
USE [{db}];
GO
DROP INDEX IF EXISTS [{index_name}] ON [{schema}].[{table}];
GO

"""
        return script

    def generate_top_n_script(self, n=10):
        """Generate SQL script for top N recommendations.

        Args:
            n: Number of top recommendations to include
        """
        output_file = os.path.join(self.output_dir, f'create_missing_indexes_top_{n}.sql')

        print(f"Generating CREATE INDEX scripts for top {n} recommendations...")

        with open(output_file, 'w', encoding='utf-8') as f:
            # Header
            f.write(f"""/*
================================================================================
CREATE MISSING INDEXES - TOP {n} RECOMMENDATIONS
================================================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Source: dpa_EDSAdmin missing index recommendations

IMPORTANT:
- Review each index recommendation before executing
- Test in development environment first
- Monitor disk space during index creation
- ONLINE = ON requires Enterprise Edition
- Have rollback scripts ready (see drop_missing_indexes_top_{n}.sql)

Execution order: Highest estimated saving first
================================================================================
*/

""")

            # Generate script for each recommendation
            for i, rec in enumerate(self.recommendations[:n], 1):
                f.write(f"-- Recommendation {i} of {n}\n")
                f.write(self.generate_create_index_statement(rec))
                f.write("\n")

            # Footer
            f.write(f"""/*
================================================================================
END OF SCRIPT - {n} indexes created
================================================================================
*/
""")

        print(f"[OK] SQL script saved to: {output_file}")

        # Generate corresponding DROP script for rollback
        drop_file = os.path.join(self.output_dir, f'drop_missing_indexes_top_{n}.sql')
        with open(drop_file, 'w', encoding='utf-8') as f:
            f.write(f"""/*
================================================================================
DROP MISSING INDEXES - ROLLBACK SCRIPT
================================================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

WARNING: This script will drop all indexes created by create_missing_indexes_top_{n}.sql
Use this only if you need to rollback the index creation.
================================================================================
*/

""")
            for i, rec in enumerate(self.recommendations[:n], 1):
                f.write(f"-- Drop index {i} of {n}\n")
                f.write(self.generate_drop_index_statement(rec))

        print(f"[OK] Rollback script saved to: {drop_file}")

    def generate_all_script(self):
        """Generate SQL script for all recommendations."""
        output_file = os.path.join(self.output_dir, 'create_missing_indexes_all.sql')

        print(f"Generating CREATE INDEX scripts for all {len(self.recommendations)} recommendations...")

        with open(output_file, 'w', encoding='utf-8') as f:
            # Header
            f.write(f"""/*
================================================================================
CREATE MISSING INDEXES - ALL RECOMMENDATIONS
================================================================================
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Total Recommendations: {len(self.recommendations)}

WARNING:
- This script contains ALL missing index recommendations
- Review carefully before executing
- Consider implementing high-impact indexes first (see top_10 script)
- Monitor disk space and server performance
================================================================================
*/

""")

            # Generate script for each recommendation
            for i, rec in enumerate(self.recommendations, 1):
                f.write(f"-- Recommendation {i} of {len(self.recommendations)}\n")
                f.write(self.generate_create_index_statement(rec))
                f.write("\n")

        print(f"[OK] SQL script saved to: {output_file}")

    def generate_implementation_plan(self, n=10):
        """Generate implementation plan markdown file.

        Args:
            n: Number of top recommendations to focus on
        """
        output_file = os.path.join(self.output_dir, 'index_implementation_plan.md')

        print(f"Generating implementation plan...")

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(f"""# Index Implementation Plan

**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Total Recommendations:** {len(self.recommendations)}
**Focus:** Top {n} high-impact indexes

---

## Executive Summary

This plan outlines the implementation approach for the top {n} missing index recommendations identified by dpa_EDSAdmin. These indexes have the highest potential for performance improvement.

### Expected Benefits
""")

            # Calculate summary statistics
            if self.recommendations:
                top_n = self.recommendations[:n]
                avg_saving = sum(r.get('EstimatedSavingPercent', 0) for r in top_n) / len(top_n)
                total_execs = sum(r.get('Executions', 0) for r in top_n)

                f.write(f"""
- **Average Estimated Improvement:** {avg_saving:.2f}%
- **Total Query Executions Affected:** {total_execs:,}
- **Indexes to Implement:** {n}

---

## Top {n} Recommendations

""")

                # List each recommendation
                for i, rec in enumerate(top_n, 1):
                    db = rec.get('DatabaseName', 'Unknown')
                    schema = rec.get('SchemaName', 'dbo')
                    table = rec.get('TableName', 'Unknown')
                    saving = rec.get('EstimatedSavingPercent', 0)
                    execs = rec.get('Executions', 0)
                    columns = rec.get('IndexColumns', 'Unknown')

                    f.write(f"""### {i}. {db}.{schema}.{table}

**Estimated Improvement:** {saving:.3f}%
**Query Executions:** {execs:,}
**Index Columns:** {columns}

""")

            f.write("""---

## Implementation Phases

### Phase 1: Pre-Implementation (Before Deployment)

**Tasks:**
1. **Backup Databases**
   - Take full backup of each database before index creation
   - Verify backup integrity

2. **Verify Disk Space**
   - Estimate index size (typically 10-20% of table size)
   - Ensure adequate free space on data drive
   - Check tempdb space (SORT_IN_TEMPDB = ON requires space)

3. **Review Execution Plans**
   - Capture current execution plans for affected queries
   - Establish baseline query performance metrics

4. **Schedule Maintenance Window** (if ONLINE = OFF)
   - Coordinate with application teams
   - Plan for 1-4 hours per index (varies by table size)

---

### Phase 2: Test Environment Deployment

**Tasks:**
1. **Deploy to Test/Dev Environment**
   - Execute create_missing_indexes_top_10.sql in test
   - Monitor index creation progress
   - Verify indexes created successfully

2. **Validate Performance**
   - Re-run affected queries
   - Compare execution plans (before vs after)
   - Measure actual performance improvement
   - Check for negative impacts on INSERT/UPDATE/DELETE

3. **Monitor Write Performance**
   - Test INSERT/UPDATE/DELETE operations
   - Check for excessive fragmentation
   - Verify no locking issues introduced

**Success Criteria:**
- Indexes created without errors
- Query performance improved by >= 50%
- No significant impact on write operations
- No locking or blocking issues

---

### Phase 3: Production Deployment

**Tasks:**
1. **Pre-Deployment**
   - Final backup of production databases
   - Alert monitoring teams
   - Prepare rollback scripts (drop_missing_indexes_top_10.sql)

2. **Execute Index Creation**
   - Run create_missing_indexes_top_10.sql
   - Monitor index creation progress (sys.dm_exec_requests)
   - Log start/end times for each index

3. **Post-Deployment Validation**
   - Verify all indexes created successfully
   - Check index usage (sys.dm_db_index_usage_stats)
   - Monitor query performance improvements
   - Check for blocking or locking issues

**Rollback Plan:**
- If critical issues occur, execute drop_missing_indexes_top_10.sql
- Restore from backup if necessary

---

### Phase 4: Post-Implementation Monitoring

**Tasks (First 7 Days):**
1. **Daily Monitoring**
   - Check index usage stats
   - Monitor query execution times
   - Review blocking events
   - Check index fragmentation

2. **Performance Validation**
   - Compare against baseline metrics
   - Verify estimated improvements achieved
   - Document actual performance gains

3. **Identify Issues**
   - Unused indexes (0 seeks/scans)
   - Excessive write overhead
   - Fragmentation >30%

**Tasks (First 30 Days):**
- Weekly performance reports
- Index maintenance planning
- Identify next batch of indexes to implement

---

## Risk Mitigation

### Risk 1: Index Creation Failure
**Mitigation:**
- Test in dev environment first
- Verify disk space before execution
- Use TRY...CATCH blocks in SQL scripts
- Have rollback scripts ready

### Risk 2: Production Performance Impact
**Mitigation:**
- Use ONLINE = ON (Enterprise Edition)
- Schedule during low-traffic periods
- Monitor query performance in real-time
- Rollback immediately if critical issues occur

### Risk 3: Disk Space Exhaustion
**Mitigation:**
- Pre-calculate index size estimates
- Ensure 20-30% free space buffer
- Monitor disk space during creation
- Implement indexes in batches if needed

### Risk 4: Blocking/Locking Issues
**Mitigation:**
- Use ONLINE = ON to minimize locks
- Schedule during maintenance window if ONLINE not available
- Monitor blocking with sp_who2 or DMVs
- Have DBA on standby during deployment

---

## SQL Scripts Reference

- **create_missing_indexes_top_10.sql** - Main deployment script
- **drop_missing_indexes_top_10.sql** - Rollback script
- **create_missing_indexes_all.sql** - All recommendations (for reference)

---

## Success Metrics

**Immediate (24 hours):**
- All indexes created without errors
- No critical performance degradation
- No blocking issues introduced

**Short-term (7 days):**
- Query performance improved by >= 50% for affected queries
- Index usage confirmed (seeks/scans > 0)
- No excessive write performance degradation

**Long-term (30 days):**
- Sustained performance improvements
- Reduced query wait times
- Lower overall CPU/IO utilization

---

## Next Steps

1. Review this implementation plan
2. Get approval from DBA team and stakeholders
3. Schedule test environment deployment
4. Execute Phase 1 pre-implementation tasks
5. Proceed with phased deployment

---

**Document Version:** 1.0
**Last Updated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
**Status:** Ready for Review
""")

        print(f"[OK] Implementation plan saved to: {output_file}")


def main():
    """Main execution."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate CREATE INDEX SQL scripts')
    parser.add_argument('--top', type=int, default=10, help='Number of top recommendations to generate (default: 10)')

    args = parser.parse_args()

    print("\n" + "="*80)
    print("INDEX SCRIPT GENERATOR")
    print("="*80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        generator = IndexScriptGenerator()
        recommendations = generator.load_recommendations()

        if not recommendations:
            print("[ERROR] No recommendations found")
            return 1

        # Generate scripts
        generator.generate_top_n_script(args.top)
        generator.generate_all_script()
        generator.generate_implementation_plan(args.top)

        print("\n" + "="*80)
        print("SCRIPT GENERATION COMPLETE")
        print("="*80)
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Total Recommendations: {len(recommendations)}")
        print(f"Top N Generated: {args.top}")
        print("\nGenerated Files:")
        print(f"  - create_missing_indexes_top_{args.top}.sql")
        print(f"  - drop_missing_indexes_top_{args.top}.sql")
        print(f"  - create_missing_indexes_all.sql")
        print(f"  - index_implementation_plan.md")
        print("="*80)

        return 0

    except Exception as e:
        print(f"\n[ERROR] Script generation failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
