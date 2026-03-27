"""
Deploy Indexes to Test Environment
Executes CREATE INDEX scripts in test environment with monitoring

Usage:
    python scripts/deploy_indexes_test.py [--script SCRIPT_FILE] [--dry-run]

Arguments:
    --script: SQL script to execute (default: create_missing_indexes_top_10.sql)
    --dry-run: Parse and validate script without executing

Outputs:
    - output/performance/index_deployment_test_log.json
    - output/performance/index_deployment_test_summary.txt
"""

import sys
import os
import json
import re
from datetime import datetime
import time

# Add scripts directory to path for imports
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError, DatabaseQueryError
from logging_config import setup_logging


class IndexDeployer:
    """Deploys indexes to test environment with monitoring."""

    def __init__(self):
        self.output_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'output', 'performance'
        )
        self.conn_cache = {}  # Cache connections per database
        self.deployment_log = []
        self.logger = setup_logging('deploy_indexes_test')

    def connect_to_database(self, database_name):
        """Connect to a specific database.

        Args:
            database_name: Name of database to connect to

        Returns:
            DatabaseConnection object
        """
        # Check cache
        if database_name in self.conn_cache:
            return self.conn_cache[database_name]

        self.logger.info("Connecting to %s...", database_name)

        try:
            db = DatabaseConnection(database=database_name)
            db.connect()
            self.conn_cache[database_name] = db
            self.logger.info("[OK] Connected to %s", database_name)
            return db
        except DatabaseConnectionError as e:
            raise DatabaseConnectionError(f"Failed to connect to {database_name}: {e}")

    def disconnect_all(self):
        """Close all cached connections."""
        for db_name, db in self.conn_cache.items():
            if db:
                db.disconnect()
                self.logger.info("Disconnected from %s", db_name)

    def parse_sql_script(self, script_path):
        """Parse SQL script and extract individual index creation statements.

        Args:
            script_path: Path to SQL script file

        Returns:
            List of dictionaries containing index info and SQL
        """
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"SQL script not found: {script_path}")

        print(f"Parsing SQL script: {script_path}\n")

        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Split by GO statements
        batches = re.split(r'\nGO\s*\n', content, flags=re.IGNORECASE)

        indexes = []
        current_index = {}

        for batch in batches:
            batch = batch.strip()
            if not batch or batch.startswith('/*') or batch.startswith('--'):
                continue

            # Extract database name from USE statement
            use_match = re.search(r'USE\s+\[([^\]]+)\]', batch, re.IGNORECASE)
            if use_match:
                current_index['database'] = use_match.group(1)
                continue

            # Extract CREATE INDEX statement
            create_match = re.search(
                r'CREATE\s+NONCLUSTERED\s+INDEX\s+\[([^\]]+)\]\s+ON\s+\[([^\]]+)\]\.\[([^\]]+)\]',
                batch,
                re.IGNORECASE | re.DOTALL
            )
            if create_match:
                index_name = create_match.group(1)
                schema = create_match.group(2)
                table = create_match.group(3)

                # Extract estimated improvement from comments
                improvement_match = re.search(r'Estimated Improvement:\s+([\d.]+)%', batch)
                improvement = float(improvement_match.group(1)) if improvement_match else 0

                indexes.append({
                    'database': current_index.get('database', 'Unknown'),
                    'schema': schema,
                    'table': table,
                    'index_name': index_name,
                    'estimated_improvement': improvement,
                    'sql': batch
                })

        print(f"[OK] Parsed {len(indexes)} index creation statements\n")
        return indexes

    def estimate_index_size(self, db, schema, table):
        """Estimate index size based on table size.

        Args:
            db: DatabaseConnection object
            schema: Schema name
            table: Table name

        Returns:
            Estimated size in MB
        """
        try:
            query = """
            SELECT
                SUM(a.total_pages) * 8 / 1024.0 as TableSizeMB
            FROM sys.tables t
            JOIN sys.schemas s ON t.schema_id = s.schema_id
            JOIN sys.indexes i ON t.object_id = i.object_id
            JOIN sys.partitions p ON i.object_id = p.object_id AND i.index_id = p.index_id
            JOIN sys.allocation_units a ON p.partition_id = a.container_id
            WHERE s.name = ? AND t.name = ?
            GROUP BY s.name, t.name
            """

            row = db.fetch_one(query, (schema, table))

            if row and row[0]:
                # Estimate index as 15% of table size
                return round(row[0] * 0.15, 2)
            else:
                return 0
        except DatabaseQueryError as e:
            self.logger.warning("Could not estimate index size: %s", e)
            return 0

    def check_disk_space(self, db):
        """Check available disk space.

        Args:
            db: DatabaseConnection object

        Returns:
            Dictionary with disk space info
        """
        try:
            query = """
            SELECT
                DB_NAME() as DatabaseName,
                SUM(size) * 8 / 1024.0 as CurrentSizeMB,
                SUM(CASE WHEN max_size = -1 THEN 1000000 ELSE max_size END) * 8 / 1024.0 as MaxSizeMB
            FROM sys.database_files
            WHERE type = 0  -- Data files only
            """

            row = db.fetch_one(query)

            if row:
                return {
                    'database': row[0],
                    'current_size_mb': round(row[1], 2),
                    'max_size_mb': round(row[2], 2),
                    'available_mb': round(row[2] - row[1], 2)
                }
            else:
                return None
        except DatabaseQueryError as e:
            self.logger.warning("Could not check disk space: %s", e)
            return None

    def execute_index_creation(self, db, index_info, dry_run=False):
        """Execute single index creation statement.

        Args:
            db: DatabaseConnection object
            index_info: Dictionary with index details
            dry_run: If True, validate but don't execute

        Returns:
            Dictionary with execution results
        """
        start_time = time.time()

        result = {
            'database': index_info['database'],
            'schema': index_info['schema'],
            'table': index_info['table'],
            'index_name': index_info['index_name'],
            'estimated_improvement': index_info['estimated_improvement'],
            'start_time': datetime.now().isoformat(),
            'status': 'pending',
            'duration_seconds': 0,
            'error': None
        }

        self.logger.info("%sCreating index: %s", '[DRY RUN] ' if dry_run else '', index_info['index_name'])
        self.logger.info("  Database: %s", index_info['database'])
        self.logger.info("  Table: %s.%s", index_info['schema'], index_info['table'])
        self.logger.info("  Estimated Improvement: %.2f%%", index_info['estimated_improvement'])

        # Estimate disk space needed
        estimated_size = self.estimate_index_size(db, index_info['schema'], index_info['table'])
        if estimated_size > 0:
            self.logger.info("  Estimated Size: %.2f MB", estimated_size)

        if dry_run:
            self.logger.info("  [DRY RUN] Skipping execution")
            result['status'] = 'dry_run'
            result['duration_seconds'] = 0
            return result

        try:
            # Execute CREATE INDEX statement (DDL - no parameters)
            self.logger.info("  Executing...")
            db.execute_non_query(index_info['sql'])

            duration = time.time() - start_time
            result['duration_seconds'] = round(duration, 2)
            result['status'] = 'success'

            self.logger.info("  [OK] Index created successfully in %.2f seconds", duration)

        except DatabaseQueryError as e:
            duration = time.time() - start_time
            result['duration_seconds'] = round(duration, 2)
            result['status'] = 'failed'
            result['error'] = str(e)

            self.logger.error("  [ERROR] Index creation failed: %s", e)

        result['end_time'] = datetime.now().isoformat()
        return result

    def deploy_indexes(self, script_path, dry_run=False):
        """Deploy all indexes from script.

        Args:
            script_path: Path to SQL script
            dry_run: If True, validate but don't execute

        Returns:
            List of deployment results
        """
        self.logger.info("=" * 80)
        self.logger.info("INDEX DEPLOYMENT %s", '(DRY RUN)' if dry_run else '(TEST ENVIRONMENT)')
        self.logger.info("=" * 80)
        self.logger.info("Script: %s", script_path)
        self.logger.info("Start Time: %s", datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

        # Parse script
        indexes = self.parse_sql_script(script_path)

        if not indexes:
            self.logger.error("[ERROR] No indexes found in script")
            return []

        # Group by database
        by_database = {}
        for idx in indexes:
            db_name = idx['database']
            if db_name not in by_database:
                by_database[db_name] = []
            by_database[db_name].append(idx)

        self.logger.info("Databases affected: %s", ', '.join(by_database.keys()))

        # Check disk space for each database
        if not dry_run:
            self.logger.info("Checking disk space...")
            for db_name in by_database.keys():
                try:
                    db = self.connect_to_database(db_name)
                    space_info = self.check_disk_space(db)
                    if space_info:
                        self.logger.info("  %s: %.2f MB available", db_name, space_info['available_mb'])
                except DatabaseConnectionError as e:
                    self.logger.warning("  %s: Could not check disk space - %s", db_name, e)

        # Deploy indexes
        results = []
        total = len(indexes)

        for i, index_info in enumerate(indexes, 1):
            self.logger.info("Index %d of %d", i, total)
            self.logger.info("-" * 80)

            try:
                # Connect to database
                db = self.connect_to_database(index_info['database'])

                # Execute index creation
                result = self.execute_index_creation(db, index_info, dry_run)
                results.append(result)
                self.deployment_log.append(result)

            except (DatabaseConnectionError, DatabaseQueryError) as e:
                result = {
                    'database': index_info['database'],
                    'index_name': index_info['index_name'],
                    'status': 'failed',
                    'error': f"Connection or execution error: {e}",
                    'start_time': datetime.now().isoformat()
                }
                results.append(result)
                self.deployment_log.append(result)
                self.logger.error("[ERROR] %s", e)

        return results

    def save_deployment_log(self, results, script_path):
        """Save deployment log to JSON file."""
        output_file = os.path.join(self.output_dir, 'index_deployment_test_log.json')

        log_data = {
            'deployment_date': datetime.now().isoformat(),
            'script': os.path.basename(script_path),
            'total_indexes': len(results),
            'successful': sum(1 for r in results if r['status'] == 'success'),
            'failed': sum(1 for r in results if r['status'] == 'failed'),
            'dry_run': sum(1 for r in results if r['status'] == 'dry_run'),
            'results': results
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2)

        print(f"[OK] Deployment log saved to: {output_file}")

    def generate_summary(self, results, script_path):
        """Generate deployment summary report."""
        output_file = os.path.join(self.output_dir, 'index_deployment_test_summary.txt')

        successful = [r for r in results if r['status'] == 'success']
        failed = [r for r in results if r['status'] == 'failed']
        dry_run = [r for r in results if r['status'] == 'dry_run']

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("INDEX DEPLOYMENT SUMMARY - TEST ENVIRONMENT\n")
            f.write("="*80 + "\n")
            f.write(f"Deployment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Script: {os.path.basename(script_path)}\n\n")

            f.write("SUMMARY\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total Indexes: {len(results)}\n")
            f.write(f"Successful: {len(successful)}\n")
            f.write(f"Failed: {len(failed)}\n")
            if dry_run:
                f.write(f"Dry Run: {len(dry_run)}\n")
            f.write("\n")

            if successful:
                f.write("SUCCESSFUL DEPLOYMENTS\n")
                f.write("-" * 80 + "\n")
                total_duration = sum(r['duration_seconds'] for r in successful)
                avg_duration = total_duration / len(successful)

                f.write(f"Total Duration: {total_duration:.2f} seconds\n")
                f.write(f"Average Duration: {avg_duration:.2f} seconds per index\n\n")

                for r in successful:
                    f.write(f"  - {r['database']}.{r['schema']}.{r['table']}.{r['index_name']}\n")
                    f.write(f"    Duration: {r['duration_seconds']:.2f}s, ")
                    f.write(f"Improvement: {r['estimated_improvement']:.2f}%\n")
                f.write("\n")

            if failed:
                f.write("FAILED DEPLOYMENTS\n")
                f.write("-" * 80 + "\n")
                for r in failed:
                    f.write(f"  - {r['database']}.{r.get('schema', 'N/A')}.{r.get('table', 'N/A')}.{r['index_name']}\n")
                    f.write(f"    Error: {r['error']}\n")
                f.write("\n")

            f.write("="*80 + "\n")
            f.write("Next Steps:\n")
            if failed:
                f.write("  1. Review failed index creations above\n")
                f.write("  2. Resolve errors and retry\n")
            if successful:
                f.write("  3. Run validate_index_performance.py to verify improvements\n")
                f.write("  4. Monitor index usage over next 48 hours\n")
                f.write("  5. If successful, proceed with production deployment\n")

        print(f"[OK] Summary saved to: {output_file}")

        # Print summary to console
        print("\n" + "="*80)
        print("DEPLOYMENT SUMMARY")
        print("="*80)
        print(f"Total: {len(results)}, Success: {len(successful)}, Failed: {len(failed)}")
        if successful:
            total_duration = sum(r['duration_seconds'] for r in successful)
            print(f"Total Duration: {total_duration:.2f} seconds")
        print("="*80)


def main():
    """Main execution."""
    import argparse

    parser = argparse.ArgumentParser(description='Deploy indexes to test environment')
    parser.add_argument('--script', type=str, default='create_missing_indexes_top_10.sql',
                        help='SQL script to execute (default: create_missing_indexes_top_10.sql)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Parse and validate without executing')

    args = parser.parse_args()

    # Resolve script path
    script_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'output', 'performance',
        args.script
    )

    print("\n" + "="*80)
    print("INDEX DEPLOYMENT TOOL - TEST ENVIRONMENT")
    print("="*80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        deployer = IndexDeployer()
        results = deployer.deploy_indexes(script_path, dry_run=args.dry_run)

        if results:
            deployer.save_deployment_log(results, script_path)
            deployer.generate_summary(results, script_path)

        deployer.disconnect_all()

        print("\n" + "="*80)
        print("DEPLOYMENT COMPLETE")
        print("="*80)
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)

        # Exit code based on failures
        failed_count = sum(1 for r in results if r['status'] == 'failed')
        return 1 if failed_count > 0 else 0

    except Exception as e:
        print(f"\n[ERROR] Deployment failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
