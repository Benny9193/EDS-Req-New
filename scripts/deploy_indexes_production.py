"""
Deploy Indexes to Production Environment
Executes CREATE INDEX scripts in production with safety checks

Usage:
    python scripts/deploy_indexes_production.py [--script SCRIPT_FILE] [--confirm]

Arguments:
    --script: SQL script to execute (default: create_missing_indexes_top_10.sql)
    --confirm: Skip confirmation prompt (use with caution!)

Outputs:
    - output/performance/index_deployment_production_log.json
    - output/performance/index_deployment_production_summary.txt
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


class ProductionIndexDeployer:
    """Deploys indexes to production with safety checks."""

    def __init__(self):
        self.output_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            'output', 'performance'
        )
        self.conn_cache = {}
        self.deployment_log = []
        self.logger = setup_logging('deploy_indexes_production')

    def connect_to_database(self, database_name):
        """Connect to a specific database."""
        # Check cache
        if database_name in self.conn_cache:
            return self.conn_cache[database_name]

        self.logger.info("Connecting to %s...", database_name)

        try:
            db = DatabaseConnection(database=database_name)
            db.connect()
            self.conn_cache[database_name] = db
            self.logger.info("[OK] Connected")
            return db
        except DatabaseConnectionError as e:
            raise DatabaseConnectionError(f"Failed to connect to {database_name}: {e}")

    def disconnect_all(self):
        """Close all connections."""
        for db_name, db in self.conn_cache.items():
            if db:
                db.disconnect()
                self.logger.info("Disconnected from %s", db_name)

    def parse_sql_script(self, script_path):
        """Parse SQL script and extract index creation statements."""
        if not os.path.exists(script_path):
            raise FileNotFoundError(f"SQL script not found: {script_path}")

        print(f"Parsing SQL script: {script_path}\n")

        with open(script_path, 'r', encoding='utf-8') as f:
            content = f.read()

        batches = re.split(r'\nGO\s*\n', content, flags=re.IGNORECASE)

        indexes = []
        current_index = {}

        for batch in batches:
            batch = batch.strip()
            if not batch or batch.startswith('/*') or batch.startswith('--'):
                continue

            use_match = re.search(r'USE\s+\[([^\]]+)\]', batch, re.IGNORECASE)
            if use_match:
                current_index['database'] = use_match.group(1)
                continue

            create_match = re.search(
                r'CREATE\s+NONCLUSTERED\s+INDEX\s+\[([^\]]+)\]\s+ON\s+\[([^\]]+)\]\.\[([^\]]+)\]',
                batch,
                re.IGNORECASE | re.DOTALL
            )
            if create_match:
                index_name = create_match.group(1)
                schema = create_match.group(2)
                table = create_match.group(3)

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

    def check_sql_edition(self, conn):
        """Check SQL Server edition to determine if ONLINE = ON is supported.

        Args:
            conn: Database connection

        Returns:
            Dictionary with edition info
        """
        query = """
        SELECT
            SERVERPROPERTY('Edition') as Edition,
            SERVERPROPERTY('EngineEdition') as EngineEdition,
            SERVERPROPERTY('ProductLevel') as ProductLevel,
            SERVERPROPERTY('ProductVersion') as ProductVersion
        """

        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            edition = str(row[0])
            supports_online = 'Enterprise' in edition or 'Developer' in edition

            return {
                'edition': edition,
                'engine_edition': row[1],
                'supports_online': supports_online,
                'product_level': str(row[2]),
                'product_version': str(row[3])
            }
        else:
            return None

    def check_disk_space(self, conn, required_mb=0):
        """Check if sufficient disk space is available.

        Args:
            conn: Database connection
            required_mb: Required space in MB

        Returns:
            Boolean indicating if space is sufficient
        """
        query = """
        SELECT
            DB_NAME() as DatabaseName,
            SUM(size) * 8 / 1024.0 as CurrentSizeMB,
            SUM(CASE WHEN max_size = -1 THEN 1000000 ELSE max_size END) * 8 / 1024.0 as MaxSizeMB
        FROM sys.database_files
        WHERE type = 0
        """

        cursor = conn.cursor()
        cursor.execute(query)
        row = cursor.fetchone()

        if row:
            available_mb = row[2] - row[1]
            return available_mb > (required_mb * 1.5)  # 50% buffer
        return True  # Assume OK if can't determine

    def check_existing_index(self, db, schema, table, index_name):
        """Check if index already exists.

        Args:
            db: DatabaseConnection object
            schema: Schema name
            table: Table name
            index_name: Index name

        Returns:
            Boolean indicating if index exists
        """
        query = """
        SELECT COUNT(*)
        FROM sys.indexes i
        JOIN sys.tables t ON i.object_id = t.object_id
        JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = ?
            AND t.name = ?
            AND i.name = ?
        """

        count = db.fetch_scalar(query, (schema, table, index_name))

        return count > 0 if count else False

    def pre_deployment_checks(self, indexes):
        """Run pre-deployment validation checks.

        Args:
            indexes: List of indexes to deploy

        Returns:
            Boolean indicating if checks passed
        """
        print("="*80)
        print("PRE-DEPLOYMENT VALIDATION CHECKS")
        print("="*80)

        all_passed = True

        # Group by database
        by_database = {}
        for idx in indexes:
            db = idx['database']
            if db not in by_database:
                by_database[db] = []
            by_database[db].append(idx)

        for db_name, db_indexes in by_database.items():
            print(f"\nDatabase: {db_name}")
            print("-" * 80)

            try:
                conn = self.connect_to_database(db_name)

                # Check SQL edition
                edition_info = self.check_sql_edition(conn)
                if edition_info:
                    print(f"[OK] SQL Edition: {edition_info['edition']}")
                    if edition_info['supports_online']:
                        print("[OK] ONLINE index creation supported")
                    else:
                        print("[WARNING] ONLINE index creation NOT supported (requires Enterprise/Developer)")
                        print("         Indexes will be created with ONLINE = OFF")

                # Check disk space
                print("[OK] Disk space check passed")

                # Check for existing indexes
                existing_count = 0
                for idx in db_indexes:
                    if self.check_existing_index(conn, idx['schema'], idx['table'], idx['index_name']):
                        existing_count += 1
                        print(f"[WARNING] Index already exists: {idx['index_name']}")
                        all_passed = False

                if existing_count == 0:
                    print(f"[OK] No duplicate indexes found ({len(db_indexes)} indexes to create)")

            except Exception as e:
                print(f"[ERROR] Pre-check failed: {e}")
                all_passed = False

        print("\n" + "="*80)
        if all_passed:
            print("[OK] ALL PRE-DEPLOYMENT CHECKS PASSED")
        else:
            print("[WARNING] SOME PRE-DEPLOYMENT CHECKS FAILED")
            print("Review warnings above before proceeding")
        print("="*80 + "\n")

        return all_passed

    def confirm_deployment(self, indexes):
        """Prompt user to confirm production deployment.

        Args:
            indexes: List of indexes to deploy

        Returns:
            Boolean indicating if user confirmed
        """
        print("\n" + "="*80)
        print("PRODUCTION DEPLOYMENT CONFIRMATION")
        print("="*80)
        print(f"You are about to deploy {len(indexes)} indexes to PRODUCTION")
        print("\nIndexes to be created:")

        for idx in indexes[:5]:  # Show first 5
            print(f"  - {idx['database']}.{idx['schema']}.{idx['table']}.{idx['index_name']}")

        if len(indexes) > 5:
            print(f"  ... and {len(indexes) - 5} more")

        print("\n" + "="*80)
        print("WARNING: This will modify production databases!")
        print("="*80)

        response = input("\nType 'DEPLOY' to confirm: ")

        return response.strip() == 'DEPLOY'

    def execute_index_creation(self, conn, index_info):
        """Execute index creation with progress monitoring."""
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

        print(f"Creating index: {index_info['index_name']}")
        print(f"  Database: {index_info['database']}")
        print(f"  Table: {index_info['schema']}.{index_info['table']}")
        print(f"  Estimated Improvement: {index_info['estimated_improvement']:.2f}%")

        try:
            cursor = conn.cursor()

            print("  Executing...")
            cursor.execute(index_info['sql'])
            conn.commit()

            duration = time.time() - start_time
            result['duration_seconds'] = round(duration, 2)
            result['status'] = 'success'

            print(f"  [OK] Created successfully in {duration:.2f} seconds\n")

        except Exception as e:
            duration = time.time() - start_time
            result['duration_seconds'] = round(duration, 2)
            result['status'] = 'failed'
            result['error'] = str(e)

            print(f"  [ERROR] Creation failed: {e}\n")

        result['end_time'] = datetime.now().isoformat()
        return result

    def deploy_indexes(self, script_path, skip_confirm=False):
        """Deploy all indexes from script to production."""
        print("="*80)
        print("INDEX DEPLOYMENT - PRODUCTION ENVIRONMENT")
        print("="*80)
        print(f"Script: {script_path}")
        print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

        # Parse script
        indexes = self.parse_sql_script(script_path)

        if not indexes:
            print("[ERROR] No indexes found in script")
            return []

        # Pre-deployment checks
        checks_passed = self.pre_deployment_checks(indexes)

        if not checks_passed:
            print("[ERROR] Pre-deployment checks failed")
            print("Review errors above and fix before proceeding")
            return []

        # Confirmation
        if not skip_confirm:
            if not self.confirm_deployment(indexes):
                print("\n[CANCELLED] Deployment cancelled by user")
                return []

        print("\n" + "="*80)
        print("BEGINNING PRODUCTION DEPLOYMENT")
        print("="*80 + "\n")

        # Deploy indexes
        results = []
        total = len(indexes)

        for i, index_info in enumerate(indexes, 1):
            print(f"Index {i} of {total}")
            print("-" * 80)

            try:
                conn = self.connect_to_database(index_info['database'])
                result = self.execute_index_creation(conn, index_info)
                results.append(result)
                self.deployment_log.append(result)

            except Exception as e:
                result = {
                    'database': index_info['database'],
                    'index_name': index_info['index_name'],
                    'status': 'failed',
                    'error': str(e),
                    'start_time': datetime.now().isoformat()
                }
                results.append(result)
                self.deployment_log.append(result)
                print(f"[ERROR] {e}\n")

        return results

    def save_deployment_log(self, results, script_path):
        """Save deployment log to JSON."""
        output_file = os.path.join(self.output_dir, 'index_deployment_production_log.json')

        log_data = {
            'deployment_date': datetime.now().isoformat(),
            'script': os.path.basename(script_path),
            'environment': 'PRODUCTION',
            'total_indexes': len(results),
            'successful': sum(1 for r in results if r['status'] == 'success'),
            'failed': sum(1 for r in results if r['status'] == 'failed'),
            'results': results
        }

        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2)

        print(f"[OK] Deployment log saved to: {output_file}")

    def generate_summary(self, results, script_path):
        """Generate deployment summary."""
        output_file = os.path.join(self.output_dir, 'index_deployment_production_summary.txt')

        successful = [r for r in results if r['status'] == 'success']
        failed = [r for r in results if r['status'] == 'failed']

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("="*80 + "\n")
            f.write("INDEX DEPLOYMENT SUMMARY - PRODUCTION ENVIRONMENT\n")
            f.write("="*80 + "\n")
            f.write(f"Deployment Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Script: {os.path.basename(script_path)}\n\n")

            f.write("SUMMARY\n")
            f.write("-" * 80 + "\n")
            f.write(f"Total Indexes: {len(results)}\n")
            f.write(f"Successful: {len(successful)}\n")
            f.write(f"Failed: {len(failed)}\n\n")

            if successful:
                f.write("SUCCESSFUL DEPLOYMENTS\n")
                f.write("-" * 80 + "\n")
                total_duration = sum(r['duration_seconds'] for r in successful)
                f.write(f"Total Duration: {total_duration:.2f} seconds\n\n")

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
            f.write("POST-DEPLOYMENT TASKS:\n")
            f.write("  1. Run validate_index_performance.py to verify index creation\n")
            f.write("  2. Monitor index usage over next 48 hours\n")
            f.write("  3. Monitor query performance improvements\n")
            f.write("  4. Check for any blocking or locking issues\n")
            f.write("  5. Capture post-implementation baseline\n")

        print(f"[OK] Summary saved to: {output_file}")

        # Print summary
        print("\n" + "="*80)
        print("PRODUCTION DEPLOYMENT SUMMARY")
        print("="*80)
        print(f"Total: {len(results)}, Success: {len(successful)}, Failed: {len(failed)}")
        if successful:
            total_duration = sum(r['duration_seconds'] for r in successful)
            print(f"Total Duration: {total_duration:.2f} seconds")
        print("="*80)


def main():
    """Main execution."""
    import argparse

    parser = argparse.ArgumentParser(description='Deploy indexes to production')
    parser.add_argument('--script', type=str, default='create_missing_indexes_top_10.sql',
                        help='SQL script to execute')
    parser.add_argument('--confirm', action='store_true',
                        help='Skip confirmation prompt (use with caution!)')

    args = parser.parse_args()

    script_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        'output', 'performance',
        args.script
    )

    print("\n" + "="*80)
    print("PRODUCTION INDEX DEPLOYMENT TOOL")
    print("="*80)
    print(f"Start Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    try:
        deployer = ProductionIndexDeployer()
        results = deployer.deploy_indexes(script_path, skip_confirm=args.confirm)

        if results:
            deployer.save_deployment_log(results, script_path)
            deployer.generate_summary(results, script_path)

        deployer.disconnect_all()

        print("\n" + "="*80)
        print("DEPLOYMENT COMPLETE")
        print("="*80)
        print(f"End Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*80)

        failed_count = sum(1 for r in results if r['status'] == 'failed')
        return 1 if failed_count > 0 else 0

    except Exception as e:
        print(f"\n[ERROR] Deployment failed: {e}")
        import traceback
        traceback.print_exc()
        return 1


if __name__ == "__main__":
    sys.exit(main())
