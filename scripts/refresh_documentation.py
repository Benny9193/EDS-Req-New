#!/usr/bin/env python3
"""
Refresh Documentation

Automated script to regenerate all database documentation after schema changes.
Can be scheduled or run manually to keep documentation up-to-date.
"""

import os
import sys
import subprocess
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from logging_config import setup_logging


def run_script(script_path, description, logger):
    """Run a Python script and capture output."""
    logger.info(f"Running: {description}")
    try:
        result = subprocess.run(
            [sys.executable, script_path],
            capture_output=True,
            text=True,
            cwd=os.path.dirname(script_path),
            timeout=600  # 10 minute timeout
        )
        if result.returncode == 0:
            logger.info(f"  [OK] {description}")
            return True
        else:
            logger.error(f"  [FAIL] {description}: {result.stderr[:200]}")
            return False
    except subprocess.TimeoutExpired:
        logger.error(f"  [TIMEOUT] {description}")
        return False
    except Exception as e:
        logger.error(f"  [ERROR] {description}: {str(e)[:200]}")
        return False


def refresh_documentation(database='EDS', scripts_dir=None, output_dir='docs'):
    """Regenerate all documentation."""

    logger = setup_logging('refresh_documentation')
    logger.info(f"Starting documentation refresh for {database}")
    start_time = datetime.now()

    if scripts_dir is None:
        scripts_dir = os.path.dirname(__file__)

    # List of documentation scripts to run in order
    doc_scripts = [
        ('document_tables.py', 'Table documentation'),
        ('document_columns.py', 'Column documentation'),
        ('document_views.py', 'View documentation'),
        ('document_stored_procedures.py', 'Stored procedure documentation'),
        ('document_sp_parameters.py', 'SP parameter documentation'),
        ('document_remaining_columns.py', 'Remaining column documentation'),
        ('generate_erd.py', 'ERD diagram'),
        ('document_indexes.py', 'Index documentation'),
        ('generate_summary_report.py', 'Summary report'),
    ]

    results = []
    for script_name, description in doc_scripts:
        script_path = os.path.join(scripts_dir, script_name)
        if os.path.exists(script_path):
            success = run_script(script_path, description, logger)
            results.append((description, success))
        else:
            logger.warning(f"Script not found: {script_name}")
            results.append((description, None))

    # Generate refresh log
    os.makedirs(output_dir, exist_ok=True)
    log_file = os.path.join(output_dir, 'REFRESH_LOG.md')

    with open(log_file, 'w', encoding='utf-8') as f:
        f.write(f'# Documentation Refresh Log\n\n')
        f.write(f'**Database:** {database}\n')
        f.write(f'**Refresh Time:** {start_time.strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write(f'**Duration:** {(datetime.now() - start_time).total_seconds():.1f} seconds\n\n')
        f.write('---\n\n')

        f.write('## Script Results\n\n')
        f.write('| Script | Status |\n')
        f.write('|--------|--------|\n')

        success_count = 0
        fail_count = 0
        skip_count = 0

        for desc, success in results:
            if success is True:
                status = 'OK'
                success_count += 1
            elif success is False:
                status = 'FAILED'
                fail_count += 1
            else:
                status = 'SKIPPED'
                skip_count += 1
            f.write(f'| {desc} | {status} |\n')

        f.write('\n---\n\n')
        f.write('## Summary\n\n')
        f.write(f'- Successful: {success_count}\n')
        f.write(f'- Failed: {fail_count}\n')
        f.write(f'- Skipped: {skip_count}\n')

        if fail_count == 0:
            f.write('\n**All documentation successfully refreshed!**\n')
        else:
            f.write(f'\n**Warning:** {fail_count} script(s) failed. Check logs for details.\n')

    # Print summary
    elapsed = (datetime.now() - start_time).total_seconds()
    logger.info(f"Documentation refresh complete in {elapsed:.1f}s")
    logger.info(f"  Success: {success_count}, Failed: {fail_count}, Skipped: {skip_count}")

    print(f"\n{'='*50}")
    print(f"DOCUMENTATION REFRESH COMPLETE")
    print(f"{'='*50}")
    print(f"Database: {database}")
    print(f"Duration: {elapsed:.1f} seconds")
    print(f"Success: {success_count} | Failed: {fail_count} | Skipped: {skip_count}")
    print(f"Log saved to: {log_file}")

    return fail_count == 0


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Refresh all database documentation')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')
    parser.add_argument('--scripts', '-s', help='Scripts directory (default: same as this script)')

    args = parser.parse_args()

    try:
        success = refresh_documentation(
            database=args.database,
            scripts_dir=args.scripts,
            output_dir=args.output
        )
        sys.exit(0 if success else 1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
