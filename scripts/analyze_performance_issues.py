"""
Performance Analysis Tool
Queries dpa_EDSAdmin to identify optimization opportunities.

Usage:
    python scripts/analyze_performance_issues.py --all
    python scripts/analyze_performance_issues.py --missing-indexes
    python scripts/analyze_performance_issues.py --slow-queries
    python scripts/analyze_performance_issues.py --blocking
    python scripts/analyze_performance_issues.py --io-issues

Outputs:
    - output/performance/{report_name}.csv
    - output/performance/performance_report.txt
"""

import sys
import os
import csv
from datetime import datetime
from typing import List, Dict, Any, Optional

# Add scripts directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError, DatabaseQueryError
from config import get_config, get_output_path, validate_params
from logging_config import setup_logging, LogContext


class PerformanceAnalyzer:
    """Analyzes SQL Server performance using dpa_EDSAdmin data."""

    def __init__(self, database: str = None):
        """
        Initialize the performance analyzer.

        Args:
            database: Database name (default: from config)
        """
        self.config = get_config()
        self.database = database or self.config.database.name
        self.output_dir = get_output_path()
        self.logger = setup_logging('analyze_performance')
        self._db: Optional[DatabaseConnection] = None

    def __enter__(self) -> 'PerformanceAnalyzer':
        """Enter context manager."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager."""
        self.disconnect()

    def connect(self) -> None:
        """Connect to dpa_EDSAdmin database."""
        self.logger.info("Connecting to %s...", self.database)
        self._db = DatabaseConnection(database=self.database)
        self._db.connect()
        self.logger.info("Connected successfully")

    def disconnect(self) -> None:
        """Close database connection."""
        if self._db:
            self._db.disconnect()
            self._db = None
            self.logger.info("Disconnected")

    def get_missing_indexes(
        self,
        days: int = None,
        min_saving: int = None
    ) -> List[Dict[str, Any]]:
        """
        Get top missing index recommendations.

        Args:
            days: Look back period in days (default: from config)
            min_saving: Minimum estimated saving percentage (default: from config)

        Returns:
            List of missing index recommendations
        """
        # Use config defaults if not specified
        days = days or self.config.analysis.missing_indexes_days
        min_saving = min_saving or self.config.thresholds.missing_index.high

        # Validate parameters
        validate_params(days=days, min_saving=min_saving)

        self.logger.info("=" * 80)
        self.logger.info("MISSING INDEX RECOMMENDATIONS")
        self.logger.info("=" * 80)
        self.logger.info("Period: Last %d days", days)
        self.logger.info("Minimum potential improvement: %d%%", min_saving)

        # Parameterized query - prevents SQL injection
        query = """
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
            SUBSTRING(st.ST, 1, 500) as SQLTextPreview
        FROM CON_WHATIF_SRC_1 w
        LEFT JOIN CON_FQ_OBJECT_1 fq ON w.IDX_ID = fq.ID
        LEFT JOIN CONST_1 st ON w.SQL_HASH = st.H
        WHERE w.D >= DATEADD(day, -?, GETDATE())
            AND w.EST_SAVING >= ?
        ORDER BY w.EST_SAVING DESC, w.SQL_EXECS DESC
        """

        with LogContext(self.logger, "Querying missing indexes"):
            rows = self._db.execute_query(query, (days, min_saving))

        results = []
        for row in rows:
            results.append({
                'ID': row[0],
                'DateIdentified': str(row[1]) if row[1] else '',
                'SQLHash': row[2],
                'Executions': row[3],
                'WaitTimeMS': row[4],
                'EstimatedSaving%': row[5],
                'Database': row[6],
                'Schema': row[7],
                'Table': row[8],
                'IndexName': row[9],
                'SQLPreview': (row[10][:100] if row[10] else '')
            })

        # Save to CSV
        output_file = self.output_dir / 'missing_indexes.csv'
        if results:
            self._save_csv(output_file, results)
            self.logger.info("[OK] Found %d missing index recommendations", len(results))
            self.logger.info("[OK] Saved to: %s", output_file)

            # Log top 10
            self.logger.info("\nTop 10 Recommendations:")
            self.logger.info("%-10s %-10s %-15s %-30s", "Saving%", "Execs", "Database", "Table")
            self.logger.info("-" * 80)
            for r in results[:10]:
                self.logger.info(
                    "%-10.2f %-10s %-15s %-30s",
                    r['EstimatedSaving%'],
                    r['Executions'],
                    r['Database'] or 'N/A',
                    r['Table'] or 'N/A'
                )
        else:
            self.logger.info("[INFO] No missing indexes found meeting criteria")

        return results

    def get_slow_queries(
        self,
        days: int = None,
        min_buffer_gets: int = None
    ) -> List[Dict[str, Any]]:
        """
        Get slowest queries by logical I/O.

        Args:
            days: Look back period
            min_buffer_gets: Minimum total buffer gets to include

        Returns:
            List of slow query records
        """
        days = days or self.config.analysis.slow_queries_days
        min_buffer_gets = min_buffer_gets or self.config.thresholds.slow_query.min_buffer_gets

        validate_params(days=days)

        self.logger.info("\n" + "=" * 80)
        self.logger.info("SLOWEST QUERIES (BY LOGICAL I/O)")
        self.logger.info("=" * 80)
        self.logger.info("Period: Last %d days", days)
        self.logger.info("Minimum buffer gets: %s", f"{min_buffer_gets:,}")

        # Parameterized query
        query = """
        SELECT TOP 50
            ss.H as SQLHash,
            SUM(ss.EXECS) as TotalExecutions,
            SUM(ss.DREADS) as TotalDiskReads,
            SUM(ss.BGETS) as TotalBufferGets,
            SUM(ss.ROW_COUNT) as TotalRowsReturned,
            CASE WHEN SUM(ss.EXECS) > 0
                THEN CAST(SUM(ss.BGETS) as FLOAT) / SUM(ss.EXECS)
                ELSE 0 END as AvgBufferGetsPerExec,
            CASE WHEN SUM(ss.EXECS) > 0
                THEN CAST(SUM(ss.DREADS) as FLOAT) / SUM(ss.EXECS)
                ELSE 0 END as AvgDiskReadsPerExec,
            SUBSTRING(st.ST, 1, 500) as SQLTextPreview
        FROM CONSS_1 ss
        LEFT JOIN CONST_1 st ON ss.H = st.H
        WHERE ss.D >= DATEADD(day, -?, GETDATE())
        GROUP BY ss.H, st.ST
        HAVING SUM(ss.BGETS) >= ?
        ORDER BY SUM(ss.BGETS) DESC
        """

        with LogContext(self.logger, "Querying slow queries"):
            rows = self._db.execute_query(query, (days, min_buffer_gets))

        results = []
        for row in rows:
            results.append({
                'SQLHash': row[0],
                'TotalExecutions': row[1],
                'TotalDiskReads': row[2],
                'TotalBufferGets': row[3],
                'TotalRowsReturned': row[4],
                'AvgBufferGetsPerExec': round(row[5], 2) if row[5] else 0,
                'AvgDiskReadsPerExec': round(row[6], 2) if row[6] else 0,
                'SQLPreview': (row[7][:200] if row[7] else '')
            })

        output_file = self.output_dir / 'slow_queries.csv'
        if results:
            self._save_csv(output_file, results)
            self.logger.info("[OK] Found %d slow queries", len(results))
            self.logger.info("[OK] Saved to: %s", output_file)
        else:
            self.logger.info("[INFO] No slow queries found meeting criteria")

        return results

    def get_blocking_events(
        self,
        days: int = None,
        min_hours: float = 1
    ) -> List[Dict[str, Any]]:
        """
        Get top blocking events.

        Args:
            days: Look back period
            min_hours: Minimum blocking hours to include

        Returns:
            List of blocking event records
        """
        days = days or self.config.analysis.blocking_days

        validate_params(days=days)

        self.logger.info("\n" + "=" * 80)
        self.logger.info("BLOCKING EVENTS ANALYSIS")
        self.logger.info("=" * 80)
        self.logger.info("Period: Last %d days", days)
        self.logger.info("Minimum blocking: %.1f hours", min_hours)

        min_seconds = int(min_hours * 3600)

        # Parameterized query
        query = """
        SELECT TOP 50
            CONVERT(VARCHAR, bs.DATEHOUR, 120) as BlockingDateTime,
            bs.DIMENSIONTYPE,
            CASE bs.DIMENSIONTYPE
                WHEN 'P' THEN 'Program'
                WHEN 'D' THEN 'Database'
                WHEN 'E' THEN 'Event'
                ELSE 'Unknown'
            END as DimensionTypeName,
            bs.DIMENSIONID,
            m.NAME as DimensionName,
            bs.BLEETIMESECS as BlockeeTimeSeconds,
            bs.BLERTIMESECS as BlockerTimeSeconds,
            bs.ROOTIMPACTSECS as RootImpactSeconds,
            bs.BLEETIMESECS / 3600.0 as BlockeeHours,
            bs.BLERTIMESECS / 3600.0 as BlockerHours
        FROM CON_BLOCKING_SUM_1 bs
        LEFT JOIN CONM_1 m ON bs.DIMENSIONID = m.ID
        WHERE bs.DATEHOUR >= DATEADD(day, -?, GETDATE())
            AND bs.BLEETIMESECS >= ?
        ORDER BY bs.BLEETIMESECS DESC
        """

        with LogContext(self.logger, "Querying blocking events"):
            rows = self._db.execute_query(query, (days, min_seconds))

        results = []
        for row in rows:
            results.append({
                'DateTime': str(row[0]) if row[0] else '',
                'DimensionType': row[1],
                'TypeName': row[2],
                'DimensionID': row[3],
                'Name': row[4],
                'BlockeeSeconds': row[5],
                'BlockerSeconds': row[6],
                'RootImpactSeconds': row[7],
                'BlockeeHours': round(row[8], 2) if row[8] else 0,
                'BlockerHours': round(row[9], 2) if row[9] else 0
            })

        output_file = self.output_dir / 'blocking_events.csv'
        if results:
            self._save_csv(output_file, results)
            self.logger.info("[OK] Found %d blocking events", len(results))
            self.logger.info("[OK] Saved to: %s", output_file)
        else:
            self.logger.info("[INFO] No blocking events found meeting criteria")

        return results

    def get_io_issues(
        self,
        hours: int = None,
        latency_threshold: int = None
    ) -> List[Dict[str, Any]]:
        """
        Get I/O performance issues.

        Args:
            hours: Look back period in hours
            latency_threshold: Latency threshold in milliseconds

        Returns:
            List of I/O issue records
        """
        hours = hours or self.config.analysis.io_issues_hours
        latency_threshold = latency_threshold or self.config.thresholds.io_latency.medium_ms

        validate_params(hours=hours, latency_ms=latency_threshold)

        self.logger.info("\n" + "=" * 80)
        self.logger.info("I/O LATENCY ISSUES")
        self.logger.info("=" * 80)
        self.logger.info("Period: Last %d hours", hours)
        self.logger.info("Latency threshold: %dms", latency_threshold)

        # Parameterized query
        query = """
        SELECT TOP 100
            CONVERT(VARCHAR, io.D, 120) as MeasurementTime,
            io.FILEID,
            io.READ_LATENCY as ReadLatencyMS,
            io.WRITE_LATENCY as WriteLatencyMS,
            io.READ_THROUGHPUT as ReadThroughputMB,
            io.WRITE_THROUGHPUT as WriteThroughputMB,
            io.READ_LATENCY_SCORE,
            io.WRITE_LATENCY_SCORE
        FROM CON_IO_DETAIL_1 io
        WHERE io.D >= DATEADD(hour, -?, GETDATE())
            AND (io.READ_LATENCY >= ? OR io.WRITE_LATENCY >= ?)
        ORDER BY io.D DESC, io.READ_LATENCY DESC
        """

        with LogContext(self.logger, "Querying I/O issues"):
            rows = self._db.execute_query(
                query,
                (hours, latency_threshold, latency_threshold)
            )

        results = []
        for row in rows:
            results.append({
                'MeasurementTime': str(row[0]) if row[0] else '',
                'FileID': row[1],
                'ReadLatencyMS': row[2],
                'WriteLatencyMS': row[3],
                'ReadThroughputMB': round(row[4], 2) if row[4] else 0,
                'WriteThroughputMB': round(row[5], 2) if row[5] else 0,
                'ReadLatencyScore': row[6],
                'WriteLatencyScore': row[7]
            })

        output_file = self.output_dir / 'io_issues.csv'
        if results:
            self._save_csv(output_file, results)
            self.logger.info("[OK] Found %d I/O latency issues", len(results))
            self.logger.info("[OK] Saved to: %s", output_file)
        else:
            self.logger.info("[INFO] No I/O issues found (latency >%dms)", latency_threshold)

        return results

    def generate_summary_report(
        self,
        missing_indexes: List[Dict],
        slow_queries: List[Dict],
        blocking_events: List[Dict],
        io_issues: List[Dict]
    ) -> None:
        """Generate text summary report."""
        output_file = self.output_dir / 'performance_report.txt'

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("=" * 80 + "\n")
            f.write("SQL SERVER PERFORMANCE ANALYSIS REPORT\n")
            f.write("=" * 80 + "\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Source: {self.database} database\n\n")

            # Summary
            f.write("EXECUTIVE SUMMARY\n")
            f.write("-" * 80 + "\n")
            f.write(f"Missing Indexes Found: {len(missing_indexes)}\n")
            f.write(f"Slow Queries Identified: {len(slow_queries)}\n")
            f.write(f"Blocking Events: {len(blocking_events)}\n")
            f.write(f"I/O Latency Issues: {len(io_issues)}\n\n")

            # Top Issues
            if missing_indexes:
                f.write("TOP 5 MISSING INDEX RECOMMENDATIONS\n")
                f.write("-" * 80 + "\n")
                for i, idx in enumerate(missing_indexes[:5], 1):
                    f.write(f"{i}. {idx['Database']}.{idx['Schema']}.{idx['Table']}\n")
                    f.write(f"   Potential Improvement: {idx['EstimatedSaving%']:.2f}%\n")
                    f.write(f"   Executions: {idx['Executions']}\n")
                    f.write(f"   Wait Time: {idx['WaitTimeMS']}ms\n\n")

            if slow_queries:
                f.write("TOP 5 SLOWEST QUERIES (BY I/O)\n")
                f.write("-" * 80 + "\n")
                for i, q in enumerate(slow_queries[:5], 1):
                    f.write(f"{i}. SQL Hash: {q['SQLHash']}\n")
                    f.write(f"   Total Buffer Gets: {q['TotalBufferGets']:,}\n")
                    f.write(f"   Avg Buffer Gets/Exec: {q['AvgBufferGetsPerExec']:,.2f}\n")
                    f.write(f"   Executions: {q['TotalExecutions']}\n")
                    f.write(f"   Preview: {q['SQLPreview'][:100]}\n\n")

            if blocking_events:
                f.write("TOP 5 BLOCKING EVENTS\n")
                f.write("-" * 80 + "\n")
                for i, b in enumerate(blocking_events[:5], 1):
                    f.write(f"{i}. {b['DateTime']}\n")
                    f.write(f"   Type: {b['TypeName']} - {b['Name']}\n")
                    f.write(f"   Blockee Time: {b['BlockeeHours']:.2f} hours\n")
                    f.write(f"   Blocker Time: {b['BlockerHours']:.2f} hours\n\n")

            f.write("=" * 80 + "\n")
            f.write("See CSV files in output/performance/ for complete details\n")

        self.logger.info("[OK] Summary report saved to: %s", output_file)

    def _save_csv(self, filepath, data: List[Dict]) -> None:
        """Save data to CSV file."""
        if not data:
            return
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)


def main() -> int:
    """Main execution."""
    import argparse

    parser = argparse.ArgumentParser(description='Analyze SQL Server performance issues')
    parser.add_argument('--all', action='store_true', help='Run all analyses')
    parser.add_argument('--missing-indexes', action='store_true', help='Analyze missing indexes')
    parser.add_argument('--slow-queries', action='store_true', help='Analyze slow queries')
    parser.add_argument('--blocking', action='store_true', help='Analyze blocking events')
    parser.add_argument('--io-issues', action='store_true', help='Analyze I/O issues')
    parser.add_argument('--days', type=int, help='Override lookback period in days')
    parser.add_argument('--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
                        default='INFO', help='Logging level')

    args = parser.parse_args()

    # Default to all if nothing specified
    if not any([args.all, args.missing_indexes, args.slow_queries, args.blocking, args.io_issues]):
        args.all = True

    logger = setup_logging('analyze_performance', log_level=args.log_level)

    logger.info("\n" + "=" * 80)
    logger.info("SQL SERVER PERFORMANCE ANALYZER")
    logger.info("=" * 80)
    logger.info("Start Time: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    try:
        with PerformanceAnalyzer() as analyzer:
            missing_indexes = []
            slow_queries = []
            blocking_events = []
            io_issues = []

            if args.all or args.missing_indexes:
                missing_indexes = analyzer.get_missing_indexes(days=args.days)

            if args.all or args.slow_queries:
                slow_queries = analyzer.get_slow_queries(days=args.days)

            if args.all or args.blocking:
                blocking_events = analyzer.get_blocking_events(days=args.days)

            if args.all or args.io_issues:
                io_issues = analyzer.get_io_issues()

            # Generate summary report
            analyzer.generate_summary_report(
                missing_indexes, slow_queries, blocking_events, io_issues
            )

        logger.info("\n" + "=" * 80)
        logger.info("ANALYSIS COMPLETE")
        logger.info("=" * 80)
        logger.info("End Time: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logger.info("Reports saved to: output/performance/")
        logger.info("=" * 80)

        return 0

    except DatabaseConnectionError as e:
        logger.error("Connection failed: %s", e)
        return 1
    except DatabaseQueryError as e:
        logger.error("Query failed: %s", e)
        return 1
    except ValueError as e:
        logger.error("Invalid parameter: %s", e)
        return 1
    except Exception as e:
        logger.exception("Analysis failed: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
