#!/usr/bin/env python3
"""
Analyze Archive Schema

Compares archive schema vs dbo schema to understand
archival patterns, data volumes, and provide recommendations.
"""

import os
import sys
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def analyze_archive_schema(database='EDS', output_dir='docs'):
    """Analyze and compare archive schema with dbo schema."""

    logger = setup_logging('analyze_archive_schema')
    logger.info(f"Analyzing archive schema for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get tables in both schemas with size info
    tables = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            ISNULL(p.row_count, 0) AS [Rows],
            CAST(SUM(a.total_pages) * 8 / 1024.0 AS DECIMAL(18,2)) AS SizeMB,
            t.create_date,
            t.modify_date
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.dm_db_partition_stats p ON t.object_id = p.object_id AND p.index_id < 2
        LEFT JOIN sys.allocation_units a ON p.partition_id = a.container_id
        WHERE s.name IN ('dbo', 'archive')
        GROUP BY s.name, t.name, p.row_count, t.create_date, t.modify_date
        ORDER BY s.name, t.name
    ''')
    logger.info(f"Found {len(tables)} tables in dbo and archive schemas")

    # Build lookup by table name
    dbo_tables = {}
    archive_tables = {}

    for table in tables:
        schema, name, rows, size_mb, created, modified = table
        data = {
            'rows': rows,
            'size_mb': size_mb or 0,
            'created': created,
            'modified': modified
        }
        if schema == 'dbo':
            dbo_tables[name] = data
        else:
            archive_tables[name] = data

    # Find tables that exist in both schemas
    common_tables = set(dbo_tables.keys()) & set(archive_tables.keys())
    dbo_only = set(dbo_tables.keys()) - set(archive_tables.keys())
    archive_only = set(archive_tables.keys()) - set(dbo_tables.keys())

    logger.info(f"  Common tables: {len(common_tables)}")
    logger.info(f"  dbo only: {len(dbo_only)}")
    logger.info(f"  archive only: {len(archive_only)}")

    # Calculate totals
    dbo_total_rows = sum(t['rows'] for t in dbo_tables.values())
    dbo_total_size = sum(t['size_mb'] for t in dbo_tables.values())
    archive_total_rows = sum(t['rows'] for t in archive_tables.values())
    archive_total_size = sum(t['size_mb'] for t in archive_tables.values())

    db.disconnect()

    # Generate markdown
    logger.info("Generating documentation...")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_ARCHIVE_ANALYSIS.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Archive Schema Analysis\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('This document analyzes the archive schema compared to the active dbo schema.\n\n')
        f.write('---\n\n')

        # Executive Summary
        f.write('## Executive Summary\n\n')
        f.write('| Metric | dbo (Active) | archive | Ratio |\n')
        f.write('|--------|--------------|---------|-------|\n')
        f.write(f'| **Tables** | {len(dbo_tables)} | {len(archive_tables)} | - |\n')
        f.write(f'| **Total Rows** | {dbo_total_rows:,} | {archive_total_rows:,} | {archive_total_rows/dbo_total_rows:.1%} |\n')
        f.write(f'| **Total Size (MB)** | {dbo_total_size:,.0f} | {archive_total_size:,.0f} | {archive_total_size/dbo_total_size:.1%} |\n')
        f.write(f'| **Total Size (GB)** | {dbo_total_size/1024:,.1f} | {archive_total_size/1024:,.1f} | - |\n')
        f.write('\n')

        # Key findings
        f.write('### Key Findings\n\n')
        f.write(f'- **{len(common_tables)}** tables exist in both schemas (archived copies)\n')
        f.write(f'- **{len(dbo_only)}** tables exist only in dbo (no archive)\n')
        f.write(f'- **{len(archive_only)}** tables exist only in archive (no active version)\n')
        f.write(f'- Archive schema holds **{archive_total_size/dbo_total_size:.0%}** of the data volume\n')
        f.write('\n---\n\n')

        # Tables in Both Schemas
        f.write('## Tables in Both Schemas\n\n')
        f.write('These tables have both active (dbo) and archived copies.\n\n')
        f.write('| Table | dbo Rows | archive Rows | dbo Size (MB) | archive Size (MB) | Archive % |\n')
        f.write('|-------|----------|--------------|---------------|-------------------|----------|\n')

        common_list = []
        for name in sorted(common_tables):
            dbo = dbo_tables[name]
            arch = archive_tables[name]
            ratio = (arch['rows'] / dbo['rows'] * 100) if dbo['rows'] > 0 else 0
            common_list.append((name, dbo, arch, ratio))

        # Sort by archive size descending
        common_list.sort(key=lambda x: -x[2]['size_mb'])

        for name, dbo, arch, ratio in common_list:
            f.write(f'| {name} | {dbo["rows"]:,} | {arch["rows"]:,} | {dbo["size_mb"]:,.0f} | {arch["size_mb"]:,.0f} | {ratio:.0f}% |\n')

        f.write('\n---\n\n')

        # Large Archive Tables
        f.write('## Largest Archive Tables\n\n')
        f.write('Tables consuming the most archive storage.\n\n')
        f.write('| Table | Rows | Size (MB) | Size (GB) | % of Archive |\n')
        f.write('|-------|------|-----------|-----------|-------------|\n')

        sorted_archive = sorted(archive_tables.items(), key=lambda x: -x[1]['size_mb'])
        for name, data in sorted_archive[:20]:
            pct = (data['size_mb'] / archive_total_size * 100) if archive_total_size > 0 else 0
            f.write(f'| {name} | {data["rows"]:,} | {data["size_mb"]:,.0f} | {data["size_mb"]/1024:,.2f} | {pct:.1f}% |\n')

        f.write('\n---\n\n')

        # Tables Only in dbo (No Archive)
        f.write('## Tables Without Archive (dbo only)\n\n')
        f.write('These tables exist only in dbo with no archived copy.\n\n')

        large_dbo_only = [(name, dbo_tables[name]) for name in dbo_only if dbo_tables[name]['rows'] > 10000]
        large_dbo_only.sort(key=lambda x: -x[1]['rows'])

        if large_dbo_only:
            f.write('### Large Tables (>10K rows) Without Archive\n\n')
            f.write('| Table | Rows | Size (MB) | Consider Archiving? |\n')
            f.write('|-------|------|-----------|--------------------|\n')

            for name, data in large_dbo_only[:30]:
                # Recommendation based on size and age
                recommend = 'Yes' if data['size_mb'] > 100 else 'Maybe' if data['size_mb'] > 10 else 'No'
                f.write(f'| {name} | {data["rows"]:,} | {data["size_mb"]:,.0f} | {recommend} |\n')

            f.write('\n')

        f.write(f'*Total dbo-only tables: {len(dbo_only)}*\n\n')
        f.write('---\n\n')

        # Tables Only in Archive
        if archive_only:
            f.write('## Orphaned Archive Tables\n\n')
            f.write('These tables exist only in archive with no active dbo version.\n')
            f.write('Consider whether these can be dropped or if the dbo table was renamed.\n\n')
            f.write('| Table | Rows | Size (MB) | Created | Modified |\n')
            f.write('|-------|------|-----------|---------|----------|\n')

            archive_only_list = [(name, archive_tables[name]) for name in archive_only]
            archive_only_list.sort(key=lambda x: -x[1]['rows'])

            for name, data in archive_only_list:
                f.write(f'| {name} | {data["rows"]:,} | {data["size_mb"]:,.0f} | {data["created"]} | {data["modified"]} |\n')

            f.write('\n---\n\n')

        # Recommendations
        f.write('## Recommendations\n\n')

        f.write('### Storage Optimization\n\n')

        # Find candidates for cleanup
        large_archive = [(n, d) for n, d in archive_tables.items() if d['size_mb'] > 1000]
        if large_archive:
            f.write('**Large archive tables (>1 GB) to review:**\n\n')
            for name, data in sorted(large_archive, key=lambda x: -x[1]['size_mb'])[:5]:
                f.write(f'- `archive.{name}` - {data["size_mb"]/1024:.1f} GB, {data["rows"]:,} rows\n')
            f.write('\n')

        f.write('### Archive Strategy\n\n')

        if large_dbo_only:
            f.write('**Tables that should be considered for archiving:**\n\n')
            for name, data in large_dbo_only[:5]:
                if data['size_mb'] > 100:
                    f.write(f'- `dbo.{name}` - {data["size_mb"]:,.0f} MB, {data["rows"]:,} rows\n')
            f.write('\n')

        f.write('### Data Retention\n\n')
        f.write('Consider implementing:\n\n')
        f.write('1. **Retention Policy**: Define how long archived data should be kept\n')
        f.write('2. **Purge Schedule**: Regular cleanup of old archive data\n')
        f.write('3. **Compression**: Enable page/row compression on archive tables\n')
        f.write('4. **Partitioning**: Consider partitioning large tables by date\n')

    logger.info(f"[OK] Documentation saved to {output_file}")
    print(f"\nArchive analysis saved to: {output_file}")
    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Analyze archive schema')
    parser.add_argument('--database', '-d', default='EDS', help='Database name (default: EDS)')
    parser.add_argument('--output', '-o', default='docs', help='Output directory (default: docs)')

    args = parser.parse_args()

    try:
        analyze_archive_schema(database=args.database, output_dir=args.output)
    except DatabaseConnectionError as e:
        print(f"Connection failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
