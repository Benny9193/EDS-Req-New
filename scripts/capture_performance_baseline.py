"""
Performance Baseline Capture
Captures current performance metrics from dpa_EDSAdmin for comparison

Usage:
    python scripts/capture_performance_baseline.py

Outputs:
    - output/performance/baseline_YYYY-MM-DD.json
    - output/performance/baseline_YYYY-MM-DD.txt
"""

import sys
import os
import json
from datetime import datetime

# Add scripts directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


class BaselineCapture:
    """Captures performance baseline metrics from dpa_EDSAdmin."""

    def __init__(self, database='dpa_EDSAdmin'):
        self.database = database
        self._db = None
        self.output_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'output', 'performance'
        )
        os.makedirs(self.output_dir, exist_ok=True)
        self.baseline_date = datetime.now().strftime('%Y-%m-%d')
        self.logger = setup_logging('capture_performance_baseline')

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

    def get_query_execution_stats(self):
        """Get query execution statistics for last 7 days."""
        self.logger.info("Capturing query execution statistics (last 7 days)...")

        query = """
        SELECT
            COUNT(*) as TotalQueries,
            SUM(EXECS) as TotalExecutions,
            AVG(CAST(BGETS as FLOAT) / NULLIF(EXECS, 0)) as AvgBufferGetsPerExec,
            SUM(DREADS) as TotalDiskReads,
            SUM(BGETS) as TotalBufferGets
        FROM CONSS_1
        WHERE D >= DATEADD(day, -7, GETDATE())
        """

        row = self._db.fetch_one(query)

        return {
            'total_queries': row[0] if row[0] else 0,
            'total_executions': row[1] if row[1] else 0,
            'avg_buffer_gets_per_exec': round(row[2], 2) if row[2] else 0,
            'total_disk_reads': row[3] if row[3] else 0,
            'total_buffer_gets': row[4] if row[4] else 0
        }

    def get_blocking_summary(self):
        """Get blocking events summary for last 7 days."""
        self.logger.info("Capturing blocking events summary (last 7 days)...")

        query = """
        SELECT
            COUNT(*) as TotalBlockingEvents,
            SUM(BLEETIMESECS) / 60.0 as TotalBlockingMinutes,
            MAX(BLEETIMESECS) / 60.0 as MaxSingleBlockingMinutes,
            AVG(BLEETIMESECS) / 60.0 as AvgBlockingMinutes
        FROM CON_BLOCKING_SUM_1
        WHERE DATEHOUR >= DATEADD(day, -7, GETDATE())
            AND BLEETIMESECS > 0
        """

        row = self._db.fetch_one(query)

        return {
            'total_blocking_events': row[0] if row[0] else 0,
            'total_blocking_minutes': round(row[1], 2) if row[1] else 0,
            'max_single_blocking_minutes': round(row[2], 2) if row[2] else 0,
            'avg_blocking_minutes': round(row[3], 2) if row[3] else 0
        }

    def get_io_latency_stats(self):
        """Get I/O latency statistics for last 7 days."""
        self.logger.info("Capturing I/O latency statistics (last 7 days)...")

        query = """
        SELECT
            AVG(READ_LATENCY) as AvgReadLatency,
            AVG(WRITE_LATENCY) as AvgWriteLatency,
            MAX(READ_LATENCY) as MaxReadLatency,
            MAX(WRITE_LATENCY) as MaxWriteLatency,
            MIN(READ_LATENCY) as MinReadLatency,
            MIN(WRITE_LATENCY) as MinWriteLatency
        FROM CON_IO_DETAIL_1
        WHERE D >= DATEADD(day, -7, GETDATE())
        """

        row = self._db.fetch_one(query)

        return {
            'avg_read_latency_ms': round(row[0], 2) if row[0] else 0,
            'avg_write_latency_ms': round(row[1], 2) if row[1] else 0,
            'max_read_latency_ms': round(row[2], 2) if row[2] else 0,
            'max_write_latency_ms': round(row[3], 2) if row[3] else 0,
            'min_read_latency_ms': round(row[4], 2) if row[4] else 0,
            'min_write_latency_ms': round(row[5], 2) if row[5] else 0
        }

    def get_missing_index_count(self):
        """Get missing index recommendation count."""
        self.logger.info("Capturing missing index count (last 30 days)...")

        query = """
        SELECT
            COUNT(*) as TotalMissingIndexes,
            SUM(CASE WHEN EST_SAVING >= 90 THEN 1 ELSE 0 END) as HighImpactCount,
            SUM(CASE WHEN EST_SAVING >= 99 THEN 1 ELSE 0 END) as CriticalImpactCount,
            AVG(EST_SAVING) as AvgEstimatedSaving
        FROM CON_WHATIF_SRC_1
        WHERE D >= DATEADD(day, -30, GETDATE())
        """

        row = self._db.fetch_one(query)

        return {
            'total_missing_indexes': row[0] if row[0] else 0,
            'high_impact_count': row[1] if row[1] else 0,  # >= 90%
            'critical_impact_count': row[2] if row[2] else 0,  # >= 99%
            'avg_estimated_saving_pct': round(row[3], 2) if row[3] else 0
        }

    def capture_baseline(self):
        """Capture all baseline metrics."""
        print("\n" + "="*80)
        print("PERFORMANCE BASELINE CAPTURE")
        print("="*80)
        print(f"Baseline Date: {self.baseline_date}")
        print(f"Period: Last 7 days (30 days for missing indexes)\n")

        baseline = {
            'capture_date': self.baseline_date,
            'capture_timestamp': datetime.now().isoformat(),
            'period_days': 7,
            'metrics': {}
        }

        # Capture all metrics
        baseline['metrics']['query_execution'] = self.get_query_execution_stats()
        baseline['metrics']['blocking'] = self.get_blocking_summary()
        baseline['metrics']['io_latency'] = self.get_io_latency_stats()
        baseline['metrics']['missing_indexes'] = self.get_missing_index_count()

        return baseline

    def save_baseline(self, baseline):
        """Save baseline to JSON and text files."""
        # Save JSON
        json_file = os.path.join(self.output_dir, f'baseline_{self.baseline_date}.json')
        with open(json_file, 'w', encoding='utf-8') as f:
            json.dump(baseline, f, indent=2)
        print(f"\n[OK] JSON saved to: {json_file}")

        # Save human-readable text
        txt_file = os.path.join(self.output_dir, f'baseline_{self.baseline_date}.txt')
        with open(txt_file, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("SQL SERVER PERFORMANCE BASELINE\n")
            f.write("="*80 + "\n")
            f.write(f"Capture Date: {baseline['capture_date']}\n")
            f.write(f"Timestamp: {baseline['capture_timestamp']}\n")
            f.write(f"Period: Last {baseline['period_days']} days\n\n")

            # Query Execution Stats
            f.write("QUERY EXECUTION STATISTICS\n")
            f.write("-" * 80 + "\n")
            qe = baseline['metrics']['query_execution']
            f.write(f"Total Queries: {qe['total_queries']:,}\n")
            f.write(f"Total Executions: {qe['total_executions']:,}\n")
            f.write(f"Avg Buffer Gets per Exec: {qe['avg_buffer_gets_per_exec']:,.2f}\n")
            f.write(f"Total Disk Reads: {qe['total_disk_reads']:,}\n")
            f.write(f"Total Buffer Gets: {qe['total_buffer_gets']:,}\n\n")

            # Blocking Summary
            f.write("BLOCKING EVENTS SUMMARY\n")
            f.write("-" * 80 + "\n")
            bl = baseline['metrics']['blocking']
            f.write(f"Total Blocking Events: {bl['total_blocking_events']}\n")
            f.write(f"Total Blocking Time: {bl['total_blocking_minutes']:.2f} minutes\n")
            f.write(f"Max Single Blocking Event: {bl['max_single_blocking_minutes']:.2f} minutes\n")
            f.write(f"Avg Blocking Time: {bl['avg_blocking_minutes']:.2f} minutes\n\n")

            # I/O Latency
            f.write("I/O LATENCY STATISTICS\n")
            f.write("-" * 80 + "\n")
            io = baseline['metrics']['io_latency']
            f.write(f"Avg Read Latency: {io['avg_read_latency_ms']:.2f} ms\n")
            f.write(f"Avg Write Latency: {io['avg_write_latency_ms']:.2f} ms\n")
            f.write(f"Max Read Latency: {io['max_read_latency_ms']:.2f} ms\n")
            f.write(f"Max Write Latency: {io['max_write_latency_ms']:.2f} ms\n")
            f.write(f"Min Read Latency: {io['min_read_latency_ms']:.2f} ms\n")
            f.write(f"Min Write Latency: {io['min_write_latency_ms']:.2f} ms\n\n")

            # Missing Indexes
            f.write("MISSING INDEX RECOMMENDATIONS\n")
            f.write("-" * 80 + "\n")
            mi = baseline['metrics']['missing_indexes']
            f.write(f"Total Missing Indexes: {mi['total_missing_indexes']}\n")
            f.write(f"High Impact (>= 90%): {mi['high_impact_count']}\n")
            f.write(f"Critical Impact (>= 99%): {mi['critical_impact_count']}\n")
            f.write(f"Avg Estimated Saving: {mi['avg_estimated_saving_pct']:.2f}%\n\n")

            f.write("="*80 + "\n")
            f.write("Use this baseline to compare against post-optimization metrics\n")

        print(f"[OK] Text report saved to: {txt_file}")

        # Print summary to console
        print("\n" + "="*80)
        print("BASELINE SUMMARY")
        print("="*80)
        print(f"Query Execution:")
        print(f"  - Total Executions: {qe['total_executions']:,}")
        print(f"  - Avg Buffer Gets/Exec: {qe['avg_buffer_gets_per_exec']:,.2f}")
        print(f"\nBlocking Events:")
        print(f"  - Total Events: {bl['total_blocking_events']}")
        print(f"  - Total Time: {bl['total_blocking_minutes']:.2f} minutes")
        print(f"\nI/O Latency:")
        print(f"  - Avg Read: {io['avg_read_latency_ms']:.2f} ms")
        print(f"  - Avg Write: {io['avg_write_latency_ms']:.2f} ms")
        print(f"\nMissing Indexes:")
        print(f"  - Total: {mi['total_missing_indexes']}")
        print(f"  - High Impact (>= 90%): {mi['high_impact_count']}")
        print("="*80)


def main():
    """Main execution."""
    print("\n" + "="*80)
    print("PERFORMANCE BASELINE CAPTURE TOOL")
    print("="*80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        capturer = BaselineCapture()
        capturer.connect()

        baseline = capturer.capture_baseline()
        capturer.save_baseline(baseline)

        capturer.disconnect()

        print("\n" + "="*80)
        print("BASELINE CAPTURE COMPLETE")
        print("="*80)
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)

        return 0

    except Exception as e:
        print(f"\n[ERROR] Baseline capture failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
