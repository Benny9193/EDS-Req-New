"""
Validate Index Performance
Validates created indexes and measures performance improvements.

Usage:
    python scripts/validate_index_performance.py [--log LOG_FILE]

Arguments:
    --log: Deployment log file to validate (default: index_deployment_test_log.json)

Outputs:
    - output/performance/index_validation_results.json
    - output/performance/index_validation_report.md
"""

import sys
import os
import json
from datetime import datetime
from typing import Dict, List, Any, Optional

# Add scripts directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError, DatabaseQueryError
from config import get_config, get_output_path
from logging_config import setup_logging


class IndexValidator:
    """Validates index creation and performance."""

    def __init__(self):
        self.config = get_config()
        self.output_dir = get_output_path()
        self.logger = setup_logging('validate_index_performance')
        self._conn_cache: Dict[str, DatabaseConnection] = {}

    def connect_to_database(self, database_name: str) -> DatabaseConnection:
        """Connect to a specific database."""
        if database_name in self._conn_cache:
            return self._conn_cache[database_name]

        self.logger.info("Connecting to %s...", database_name)
        db = DatabaseConnection(database=database_name)
        db.connect()
        self._conn_cache[database_name] = db
        self.logger.info("[OK] Connected")
        return db

    def disconnect_all(self) -> None:
        """Close all connections."""
        for db_name, db in self._conn_cache.items():
            if db:
                db.disconnect()
                self.logger.info("Disconnected from %s", db_name)
        self._conn_cache.clear()

    def check_index_exists(
        self,
        db: DatabaseConnection,
        schema: str,
        table: str,
        index_name: str
    ) -> Dict[str, Any]:
        """
        Check if index exists on table.

        Args:
            db: Database connection
            schema: Schema name
            table: Table name
            index_name: Index name

        Returns:
            Dictionary with index existence info
        """
        # Parameterized query - prevents SQL injection
        query = """
        SELECT
            i.name as IndexName,
            i.type_desc as IndexType,
            i.is_disabled as IsDisabled,
            i.is_hypothetical as IsHypothetical,
            STATS_DATE(i.object_id, i.index_id) as LastUpdated
        FROM sys.indexes i
        JOIN sys.tables t ON i.object_id = t.object_id
        JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = ?
            AND t.name = ?
            AND i.name = ?
        """

        row = db.fetch_one(query, (schema, table, index_name))

        if row:
            return {
                'exists': True,
                'index_name': row[0],
                'type': row[1],
                'is_disabled': bool(row[2]),
                'is_hypothetical': bool(row[3]),
                'last_updated': str(row[4]) if row[4] else None
            }
        return {'exists': False}

    def get_index_usage_stats(
        self,
        db: DatabaseConnection,
        schema: str,
        table: str,
        index_name: str
    ) -> Dict[str, Any]:
        """
        Get index usage statistics.

        Args:
            db: Database connection
            schema: Schema name
            table: Table name
            index_name: Index name

        Returns:
            Dictionary with usage stats
        """
        query = """
        SELECT
            ius.user_seeks as UserSeeks,
            ius.user_scans as UserScans,
            ius.user_lookups as UserLookups,
            ius.user_updates as UserUpdates,
            ius.last_user_seek as LastSeek,
            ius.last_user_scan as LastScan,
            ius.last_user_lookup as LastLookup,
            ius.last_user_update as LastUpdate
        FROM sys.dm_db_index_usage_stats ius
        JOIN sys.indexes i
            ON ius.object_id = i.object_id AND ius.index_id = i.index_id
        JOIN sys.tables t ON i.object_id = t.object_id
        JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE ius.database_id = DB_ID()
            AND s.name = ?
            AND t.name = ?
            AND i.name = ?
        """

        row = db.fetch_one(query, (schema, table, index_name))

        if row:
            return {
                'user_seeks': row[0] or 0,
                'user_scans': row[1] or 0,
                'user_lookups': row[2] or 0,
                'user_updates': row[3] or 0,
                'last_seek': str(row[4]) if row[4] else None,
                'last_scan': str(row[5]) if row[5] else None,
                'last_lookup': str(row[6]) if row[6] else None,
                'last_update': str(row[7]) if row[7] else None,
                'total_reads': (row[0] or 0) + (row[1] or 0) + (row[2] or 0)
            }
        return {
            'user_seeks': 0,
            'user_scans': 0,
            'user_lookups': 0,
            'user_updates': 0,
            'total_reads': 0,
            'last_seek': None,
            'last_scan': None,
            'last_lookup': None,
            'last_update': None
        }

    def get_index_fragmentation(
        self,
        db: DatabaseConnection,
        schema: str,
        table: str,
        index_name: str
    ) -> Optional[Dict[str, Any]]:
        """
        Get index fragmentation statistics.

        Args:
            db: Database connection
            schema: Schema name
            table: Table name
            index_name: Index name

        Returns:
            Dictionary with fragmentation info or None
        """
        query = """
        SELECT
            ips.avg_fragmentation_in_percent as AvgFragmentation,
            ips.fragment_count as FragmentCount,
            ips.page_count as PageCount,
            ips.avg_page_space_used_in_percent as AvgPageSpaceUsed
        FROM sys.dm_db_index_physical_stats(
            DB_ID(), NULL, NULL, NULL, 'LIMITED'
        ) ips
        JOIN sys.indexes i
            ON ips.object_id = i.object_id AND ips.index_id = i.index_id
        JOIN sys.tables t ON i.object_id = t.object_id
        JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = ?
            AND t.name = ?
            AND i.name = ?
        """

        row = db.fetch_one(query, (schema, table, index_name))

        if row:
            return {
                'avg_fragmentation_percent': round(row[0], 2) if row[0] else 0,
                'fragment_count': row[1] or 0,
                'page_count': row[2] or 0,
                'avg_page_space_used_percent': round(row[3], 2) if row[3] else 0
            }
        return None

    def get_index_size(
        self,
        db: DatabaseConnection,
        schema: str,
        table: str,
        index_name: str
    ) -> float:
        """
        Get index size.

        Args:
            db: Database connection
            schema: Schema name
            table: Table name
            index_name: Index name

        Returns:
            Size in MB
        """
        query = """
        SELECT
            SUM(a.total_pages) * 8 / 1024.0 as SizeMB
        FROM sys.indexes i
        JOIN sys.tables t ON i.object_id = t.object_id
        JOIN sys.schemas s ON t.schema_id = s.schema_id
        JOIN sys.partitions p
            ON i.object_id = p.object_id AND i.index_id = p.index_id
        JOIN sys.allocation_units a ON p.partition_id = a.container_id
        WHERE s.name = ?
            AND t.name = ?
            AND i.name = ?
        GROUP BY s.name, t.name, i.name
        """

        result = db.fetch_scalar(query, (schema, table, index_name))
        return round(result, 2) if result else 0

    def validate_deployment(self, log_file: str) -> List[Dict[str, Any]]:
        """
        Validate all indexes from deployment log.

        Args:
            log_file: Path to deployment log JSON file

        Returns:
            List of validation results
        """
        if not os.path.exists(log_file):
            raise FileNotFoundError(f"Deployment log not found: {log_file}")

        self.logger.info("=" * 80)
        self.logger.info("INDEX VALIDATION")
        self.logger.info("=" * 80)
        self.logger.info("Log File: %s", os.path.basename(log_file))

        with open(log_file, 'r', encoding='utf-8') as f:
            log_data = json.load(f)

        self.logger.info("Deployment Date: %s", log_data['deployment_date'])
        self.logger.info("Total Indexes: %d", log_data['total_indexes'])
        self.logger.info("Successful Deployments: %d", log_data['successful'])

        successful = [r for r in log_data['results'] if r['status'] == 'success']

        if not successful:
            self.logger.info("[INFO] No successful deployments to validate")
            return []

        self.logger.info("Validating %d indexes...", len(successful))

        validation_results = []

        for i, deployment in enumerate(successful, 1):
            self.logger.info("Index %d of %d", i, len(successful))
            self.logger.info("-" * 80)
            self.logger.info("Index: %s", deployment['index_name'])
            self.logger.info("Database: %s", deployment['database'])
            self.logger.info(
                "Table: %s.%s",
                deployment['schema'],
                deployment['table']
            )

            try:
                db = self.connect_to_database(deployment['database'])

                existence = self.check_index_exists(
                    db,
                    deployment['schema'],
                    deployment['table'],
                    deployment['index_name']
                )

                if not existence['exists']:
                    self.logger.warning("Index not found!")
                    result = {
                        **deployment,
                        'validation_status': 'not_found',
                        'validation_date': datetime.now().isoformat()
                    }
                    validation_results.append(result)
                    continue

                self.logger.info(
                    "[OK] Index exists (Type: %s)", existence['type']
                )

                usage = self.get_index_usage_stats(
                    db,
                    deployment['schema'],
                    deployment['table'],
                    deployment['index_name']
                )

                self.logger.info(
                    "  Seeks: %d, Scans: %d, Lookups: %d",
                    usage['user_seeks'],
                    usage['user_scans'],
                    usage['user_lookups']
                )
                self.logger.info(
                    "  Updates: %d, Total Reads: %d",
                    usage['user_updates'],
                    usage['total_reads']
                )

                fragmentation = self.get_index_fragmentation(
                    db,
                    deployment['schema'],
                    deployment['table'],
                    deployment['index_name']
                )

                if fragmentation:
                    frag_pct = fragmentation['avg_fragmentation_percent']
                    status = "(Good)" if frag_pct < 10 else \
                             "(Acceptable)" if frag_pct < 30 else \
                             "(High - consider rebuild)"
                    self.logger.info(
                        "  Fragmentation: %.2f%% %s", frag_pct, status
                    )

                size_mb = self.get_index_size(
                    db,
                    deployment['schema'],
                    deployment['table'],
                    deployment['index_name']
                )

                self.logger.info("  Size: %.2f MB", size_mb)

                if usage['total_reads'] > 0:
                    validation_status = 'in_use'
                elif fragmentation and frag_pct > 30:
                    validation_status = 'fragmented'
                else:
                    validation_status = 'created_not_used'

                result = {
                    **deployment,
                    'validation_status': validation_status,
                    'validation_date': datetime.now().isoformat(),
                    'existence': existence,
                    'usage_stats': usage,
                    'fragmentation': fragmentation,
                    'size_mb': size_mb
                }

                validation_results.append(result)

            except DatabaseConnectionError as e:
                self.logger.error("Connection error: %s", e)
                result = {
                    **deployment,
                    'validation_status': 'error',
                    'validation_error': str(e),
                    'validation_date': datetime.now().isoformat()
                }
                validation_results.append(result)
            except DatabaseQueryError as e:
                self.logger.error("Query error: %s", e)
                result = {
                    **deployment,
                    'validation_status': 'error',
                    'validation_error': str(e),
                    'validation_date': datetime.now().isoformat()
                }
                validation_results.append(result)

        return validation_results

    def save_validation_results(self, results: List[Dict]) -> None:
        """Save validation results to JSON."""
        output_file = self.output_dir / 'index_validation_results.json'

        data = {
            'validation_date': datetime.now().isoformat(),
            'total_indexes': len(results),
            'in_use': sum(
                1 for r in results if r['validation_status'] == 'in_use'
            ),
            'created_not_used': sum(
                1 for r in results if r['validation_status'] == 'created_not_used'
            ),
            'not_found': sum(
                1 for r in results if r['validation_status'] == 'not_found'
            ),
            'errors': sum(
                1 for r in results if r['validation_status'] == 'error'
            ),
            'results': results
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2)

        self.logger.info("[OK] Validation results saved to: %s", output_file)

    def generate_validation_report(self, results: List[Dict]) -> None:
        """Generate validation report in markdown."""
        output_file = self.output_dir / 'index_validation_report.md'

        in_use = [r for r in results if r['validation_status'] == 'in_use']
        not_used = [
            r for r in results if r['validation_status'] == 'created_not_used'
        ]
        not_found = [r for r in results if r['validation_status'] == 'not_found']
        errors = [r for r in results if r['validation_status'] == 'error']

        total = len(results) or 1  # Avoid division by zero

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# Index Validation Report\n\n")
            f.write(f"**Validation Date:** ")
            f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"**Total Indexes Validated:** {len(results)}\n\n")
            f.write("---\n\n")
            f.write("## Summary\n\n")
            f.write(f"- **Indexes In Use:** {len(in_use)} ")
            f.write(f"({len(in_use)/total*100:.1f}%)\n")
            f.write(f"- **Created But Not Yet Used:** {len(not_used)} ")
            f.write(f"({len(not_used)/total*100:.1f}%)\n")
            f.write(f"- **Not Found:** {len(not_found)}\n")
            f.write(f"- **Validation Errors:** {len(errors)}\n\n")
            f.write("---\n\n")

            f.write(f"## Indexes In Use ({len(in_use)})\n\n")
            f.write("These indexes are actively being used by queries.\n\n")

            if in_use:
                f.write("| Database | Table | Index | Reads | Seeks | ")
                f.write("Updates | Frag% | Size MB |\n")
                f.write("|----------|-------|-------|-------|-------|")
                f.write("---------|-------|--------|\n")

                for r in in_use:
                    usage = r.get('usage_stats', {})
                    frag = r.get('fragmentation', {})
                    frag_pct = frag.get('avg_fragmentation_percent', 0) if frag else 0

                    f.write(f"| {r['database']} | {r['table']} | ")
                    f.write(f"{r['index_name']} | ")
                    f.write(f"{usage.get('total_reads', 0)} | ")
                    f.write(f"{usage.get('user_seeks', 0)} | ")
                    f.write(f"{usage.get('user_updates', 0)} | ")
                    f.write(f"{frag_pct:.1f} | ")
                    f.write(f"{r.get('size_mb', 0):.2f} |\n")

            f.write(f"\n---\n\n## Not Yet Used ({len(not_used)})\n\n")
            f.write("These indexes were created but have not been used yet.\n\n")

            if not_used:
                f.write("| Database | Table | Index | Size MB |\n")
                f.write("|----------|-------|-------|---------|\n")
                for r in not_used:
                    f.write(f"| {r['database']} | {r['table']} | ")
                    f.write(f"{r['index_name']} | ")
                    f.write(f"{r.get('size_mb', 0):.2f} |\n")

            if not_found:
                f.write(f"\n---\n\n## Not Found ({len(not_found)})\n\n")
                f.write("**WARNING:** These indexes cannot be found.\n\n")
                for r in not_found:
                    f.write(f"- {r['database']}.{r['schema']}.")
                    f.write(f"{r['table']}.{r['index_name']}\n")

            if errors:
                f.write(f"\n---\n\n## Errors ({len(errors)})\n\n")
                for r in errors:
                    f.write(f"- {r['index_name']}: ")
                    f.write(f"{r.get('validation_error', 'Unknown')}\n")

            f.write("\n---\n\n## Recommendations\n\n")
            f.write("1. Monitor unused indexes for 7 days\n")
            f.write("2. Rebuild indexes with >30% fragmentation\n")
            f.write("3. Verify performance improvements in dpa_EDSAdmin\n")

        self.logger.info("[OK] Validation report saved to: %s", output_file)

        self.logger.info("=" * 80)
        self.logger.info("VALIDATION SUMMARY")
        self.logger.info("=" * 80)
        self.logger.info("Total: %d", len(results))
        self.logger.info("In Use: %d", len(in_use))
        self.logger.info("Not Yet Used: %d", len(not_used))
        self.logger.info("Not Found: %d", len(not_found))
        self.logger.info("Errors: %d", len(errors))
        self.logger.info("=" * 80)


def main() -> int:
    """Main execution."""
    import argparse

    parser = argparse.ArgumentParser(description='Validate index performance')
    parser.add_argument(
        '--log', type=str, default='index_deployment_test_log.json',
        help='Deployment log file (default: index_deployment_test_log.json)'
    )
    parser.add_argument(
        '--log-level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR'],
        default='INFO', help='Logging level'
    )

    args = parser.parse_args()

    logger = setup_logging('validate_index_performance', log_level=args.log_level)

    log_file = get_output_path() / args.log

    logger.info("=" * 80)
    logger.info("INDEX PERFORMANCE VALIDATOR")
    logger.info("=" * 80)
    logger.info("Start Time: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    try:
        validator = IndexValidator()
        results = validator.validate_deployment(str(log_file))

        if results:
            validator.save_validation_results(results)
            validator.generate_validation_report(results)

        validator.disconnect_all()

        logger.info("=" * 80)
        logger.info("VALIDATION COMPLETE")
        logger.info("=" * 80)
        logger.info("End Time: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        logger.info("=" * 80)

        return 0

    except FileNotFoundError as e:
        logger.error("File not found: %s", e)
        return 1
    except DatabaseConnectionError as e:
        logger.error("Connection failed: %s", e)
        return 1
    except DatabaseQueryError as e:
        logger.error("Query failed: %s", e)
        return 1
    except json.JSONDecodeError as e:
        logger.error("Invalid JSON in log file: %s", e)
        return 1
    except Exception as e:
        logger.exception("Validation failed: %s", e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
