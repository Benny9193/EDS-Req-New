#!/usr/bin/env python3
"""
Document Indexes

Generates documentation for all database indexes including their purpose,
columns, and usage statistics.
"""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def document_indexes(database='EDS', output_dir='docs'):
    """Generate comprehensive index documentation."""

    logger = setup_logging('document_indexes')
    logger.info(f"Documenting indexes for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all indexes with details
    indexes = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            i.name AS IndexName,
            i.type_desc AS IndexType,
            i.is_unique AS IsUnique,
            i.is_primary_key AS IsPK,
            i.is_unique_constraint AS IsUniqueConstraint,
            ISNULL(ps.row_count, 0) AS TableRows,
            ISNULL(ius.user_seeks, 0) AS UserSeeks,
            ISNULL(ius.user_scans, 0) AS UserScans,
            ISNULL(ius.user_lookups, 0) AS UserLookups,
            ISNULL(ius.user_updates, 0) AS UserUpdates,
            ISNULL(ius.last_user_seek, '1900-01-01') AS LastSeek,
            ISNULL(ius.last_user_scan, '1900-01-01') AS LastScan,
            CAST(ISNULL(ps.used_page_count * 8.0 / 1024, 0) AS DECIMAL(10,2)) AS SizeMB
        FROM sys.indexes i
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.dm_db_index_usage_stats ius ON i.object_id = ius.object_id
            AND i.index_id = ius.index_id AND ius.database_id = DB_ID()
        LEFT JOIN sys.dm_db_partition_stats ps ON i.object_id = ps.object_id
            AND i.index_id = ps.index_id
        WHERE i.name IS NOT NULL
        ORDER BY s.name, t.name, i.index_id
    ''')
    logger.info(f"Found {len(indexes)} indexes")

    # Get index columns
    index_columns = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            i.name AS IndexName,
            c.name AS ColumnName,
            ic.key_ordinal AS KeyOrdinal,
            ic.is_descending_key AS IsDesc,
            ic.is_included_column AS IsIncluded
        FROM sys.index_columns ic
        INNER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
        INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE i.name IS NOT NULL
        ORDER BY s.name, t.name, i.name, ic.key_ordinal, ic.is_included_column
    ''')

    # Build column lookup
    col_lookup = {}
    for col in index_columns:
        key = f"{col[0]}.{col[1]}.{col[2]}"
        if key not in col_lookup:
            col_lookup[key] = {'key_cols': [], 'included_cols': []}
        if col[6]:  # Is included
            col_lookup[key]['included_cols'].append(col[3])
        else:
            desc = ' DESC' if col[5] else ''
            col_lookup[key]['key_cols'].append(f"{col[3]}{desc}")

    # Get unused indexes (no seeks, scans, or lookups)
    unused_indexes = [idx for idx in indexes
                      if idx[8] == 0 and idx[9] == 0 and idx[10] == 0
                      and not idx[5] and not idx[6]]  # Not PK or unique constraint

    # Get high-update, low-read indexes
    costly_indexes = [idx for idx in indexes
                      if idx[11] > 1000 and (idx[8] + idx[9] + idx[10]) < 100
                      and not idx[5] and not idx[6]]

    db.disconnect()

    # Generate documentation
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_INDEXES.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Index Documentation\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write(f'Total indexes documented: {len(indexes)}\n\n')
        f.write('---\n\n')

        # Summary statistics
        f.write('## Summary Statistics\n\n')

        pk_count = sum(1 for idx in indexes if idx[5])
        unique_count = sum(1 for idx in indexes if idx[4] and not idx[5])
        nonclustered = sum(1 for idx in indexes if idx[3] == 'NONCLUSTERED')
        clustered = sum(1 for idx in indexes if idx[3] == 'CLUSTERED')

        f.write('| Metric | Count |\n')
        f.write('|--------|-------|\n')
        f.write(f'| Total Indexes | {len(indexes)} |\n')
        f.write(f'| Primary Keys | {pk_count} |\n')
        f.write(f'| Unique Indexes | {unique_count} |\n')
        f.write(f'| Clustered | {clustered} |\n')
        f.write(f'| Non-Clustered | {nonclustered} |\n')
        f.write(f'| Unused Indexes | {len(unused_indexes)} |\n')
        f.write(f'| High-Cost Indexes | {len(costly_indexes)} |\n')
        f.write('\n---\n\n')

        # Unused indexes (potential for removal)
        if unused_indexes:
            f.write('## Unused Indexes (Review for Removal)\n\n')
            f.write('These indexes have no seeks, scans, or lookups since last restart.\n\n')
            f.write('| Schema | Table | Index | Type | Size MB |\n')
            f.write('|--------|-------|-------|------|--------|\n')
            for idx in unused_indexes[:30]:
                f.write(f'| {idx[0]} | {idx[1]} | {idx[2]} | {idx[3]} | {idx[14]} |\n')
            if len(unused_indexes) > 30:
                f.write(f'\n*...and {len(unused_indexes) - 30} more*\n')
            f.write('\n---\n\n')

        # High-cost indexes
        if costly_indexes:
            f.write('## High-Cost Indexes (High Updates, Low Reads)\n\n')
            f.write('These indexes are updated frequently but rarely used for queries.\n\n')
            f.write('| Schema | Table | Index | Updates | Reads |\n')
            f.write('|--------|-------|-------|---------|-------|\n')
            for idx in costly_indexes[:20]:
                reads = idx[8] + idx[9] + idx[10]
                f.write(f'| {idx[0]} | {idx[1]} | {idx[2]} | {idx[11]:,} | {reads:,} |\n')
            f.write('\n---\n\n')

        # Most used indexes
        f.write('## Most Used Indexes (Top 50)\n\n')
        sorted_by_usage = sorted(indexes, key=lambda x: x[8] + x[9] + x[10], reverse=True)
        f.write('| Schema | Table | Index | Seeks | Scans | Lookups |\n')
        f.write('|--------|-------|-------|-------|-------|--------|\n')
        for idx in sorted_by_usage[:50]:
            f.write(f'| {idx[0]} | {idx[1]} | {idx[2]} | {idx[8]:,} | {idx[9]:,} | {idx[10]:,} |\n')
        f.write('\n---\n\n')

        # All indexes by table
        f.write('## All Indexes by Table\n\n')

        current_table = None
        for idx in indexes:
            table_key = f"{idx[0]}.{idx[1]}"

            if table_key != current_table:
                if current_table:
                    f.write('\n')
                f.write(f'### {table_key}\n\n')
                f.write(f'*Table rows: {idx[7]:,}*\n\n')
                current_table = table_key

            idx_key = f"{idx[0]}.{idx[1]}.{idx[2]}"
            cols = col_lookup.get(idx_key, {'key_cols': [], 'included_cols': []})

            # Index type badge
            type_badge = ''
            if idx[5]:
                type_badge = '**[PK]** '
            elif idx[6]:
                type_badge = '**[UQ]** '
            elif idx[4]:
                type_badge = '*[Unique]* '

            f.write(f'**{type_badge}{idx[2]}** ({idx[3]})\n')
            f.write(f'- Key columns: `{", ".join(cols["key_cols"]) or "N/A"}`\n')
            if cols['included_cols']:
                f.write(f'- Included: `{", ".join(cols["included_cols"])}`\n')
            f.write(f'- Usage: {idx[8]:,} seeks, {idx[9]:,} scans, {idx[10]:,} lookups\n')
            f.write(f'- Size: {idx[14]} MB\n\n')

    logger.info(f"[OK] Index documentation saved to {output_file}")
    print(f"\nIndex documentation saved to: {output_file}")
    print(f"  Total indexes: {len(indexes)}")
    print(f"  Unused indexes: {len(unused_indexes)}")
    print(f"  High-cost indexes: {len(costly_indexes)}")

    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate index documentation')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')

    args = parser.parse_args()

    try:
        document_indexes(database=args.database, output_dir=args.output)
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
