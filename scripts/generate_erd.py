#!/usr/bin/env python3
"""
Generate ERD (Entity Relationship Diagram)

Creates a Mermaid ERD diagram for core database tables showing
relationships and key columns.
"""

import os
import sys
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def generate_erd(database='EDS', output_dir='docs', min_rows=10000):
    """Generate ERD for tables with significant data."""

    logger = setup_logging('generate_erd')
    logger.info(f"Generating ERD for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get tables with row counts (dbo schema, minimum rows)
    tables = db.execute_query(f'''
        SELECT
            t.name AS TableName,
            ISNULL(p.row_count, 0) AS [Rows]
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.dm_db_partition_stats p ON t.object_id = p.object_id AND p.index_id < 2
        WHERE s.name = 'dbo'
        AND ISNULL(p.row_count, 0) >= ?
        ORDER BY p.row_count DESC
    ''', params=(min_rows,))
    logger.info(f"Found {len(tables)} tables with >= {min_rows:,} rows")

    table_names = [t[0] for t in tables]

    # Get foreign keys
    fks = db.execute_query('''
        SELECT
            t.name AS TableName,
            c.name AS ColumnName,
            rt.name AS RefTable,
            rc.name AS RefColumn
        FROM sys.foreign_key_columns fkc
        INNER JOIN sys.foreign_keys fk ON fkc.constraint_object_id = fk.object_id
        INNER JOIN sys.tables t ON fkc.parent_object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        INNER JOIN sys.columns c ON fkc.parent_object_id = c.object_id AND fkc.parent_column_id = c.column_id
        INNER JOIN sys.tables rt ON fkc.referenced_object_id = rt.object_id
        INNER JOIN sys.columns rc ON fkc.referenced_object_id = rc.object_id AND fkc.referenced_column_id = rc.column_id
        WHERE s.name = 'dbo'
    ''')
    logger.info(f"Found {len(fks)} foreign key relationships")

    # Get primary key columns for included tables
    pks = db.execute_query('''
        SELECT
            t.name AS TableName,
            c.name AS ColumnName
        FROM sys.indexes i
        INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
        INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE i.is_primary_key = 1 AND s.name = 'dbo'
        ORDER BY t.name, ic.key_ordinal
    ''')

    # Get key columns for each table (PK + important columns)
    columns = db.execute_query('''
        SELECT
            t.name AS TableName,
            c.name AS ColumnName,
            ty.name AS DataType,
            c.is_nullable,
            c.column_id
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        INNER JOIN sys.types ty ON c.user_type_id = ty.user_type_id
        WHERE s.name = 'dbo'
        AND c.column_id <= 8  -- First 8 columns only for diagram clarity
        ORDER BY t.name, c.column_id
    ''')

    db.disconnect()

    # Build lookups
    pk_lookup = {}
    for pk in pks:
        if pk[0] not in pk_lookup:
            pk_lookup[pk[0]] = []
        pk_lookup[pk[0]].append(pk[1])

    col_lookup = {}
    for col in columns:
        if col[0] not in col_lookup:
            col_lookup[col[0]] = []
        col_lookup[col[0]].append({
            'name': col[1],
            'type': col[2],
            'nullable': col[3]
        })

    # Filter FKs to only include tables in our list
    filtered_fks = [fk for fk in fks if fk[0] in table_names and fk[2] in table_names]

    # Also find implicit relationships by naming convention (e.g., BidHeaderId -> BidHeaders)
    implicit_rels = []
    for table in table_names:
        if table in col_lookup:
            for col in col_lookup[table]:
                col_name = col['name']
                # Check if column name suggests a relationship
                if col_name.endswith('Id') and col_name != f'{table}Id':
                    # Try to find matching table
                    potential_table = col_name[:-2] + 's'  # e.g., BidHeaderId -> BidHeaders
                    if potential_table in table_names:
                        implicit_rels.append((table, col_name, potential_table, potential_table[:-1] + 'Id'))
                    # Also try without 's'
                    potential_table2 = col_name[:-2]
                    if potential_table2 in table_names:
                        implicit_rels.append((table, col_name, potential_table2, col_name))

    logger.info(f"Found {len(implicit_rels)} implicit relationships by naming convention")

    # Generate Mermaid ERD
    logger.info("Generating ERD diagram...")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_ERD.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Entity Relationship Diagram\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write(f'Tables shown: {len(tables)} (with >= {min_rows:,} rows)\n\n')
        f.write('---\n\n')

        # Summary table
        f.write('## Tables Included\n\n')
        f.write('| Table | Rows | Primary Key |\n')
        f.write('|-------|------|-------------|\n')
        for t in tables[:50]:  # Top 50
            pk = ', '.join(pk_lookup.get(t[0], ['*None*']))
            f.write(f'| {t[0]} | {t[1]:,} | {pk} |\n')
        if len(tables) > 50:
            f.write(f'\n*...and {len(tables) - 50} more tables*\n')
        f.write('\n---\n\n')

        # Mermaid ERD - Core tables only (top 30 for readability)
        core_tables = [t[0] for t in tables[:30]]

        f.write('## Core Tables ERD\n\n')
        f.write('```mermaid\nerDiagram\n')

        # Define entities with key attributes
        for table in core_tables:
            f.write(f'    {table} {{\n')
            if table in pk_lookup:
                for pk_col in pk_lookup[table]:
                    f.write(f'        int {pk_col} PK\n')
            if table in col_lookup:
                for col in col_lookup[table][:6]:  # First 6 non-PK columns
                    if table not in pk_lookup or col['name'] not in pk_lookup[table]:
                        nullable = '' if col['nullable'] else ' "NOT NULL"'
                        f.write(f'        {col["type"]} {col["name"]}{nullable}\n')
            f.write('    }\n')

        f.write('\n')

        # Add relationships (FKs)
        added_rels = set()
        for fk in filtered_fks:
            if fk[0] in core_tables and fk[2] in core_tables:
                rel_key = f'{fk[0]}-{fk[2]}'
                if rel_key not in added_rels:
                    f.write(f'    {fk[2]} ||--o{{ {fk[0]} : "{fk[1]}"\n')
                    added_rels.add(rel_key)

        # Add implicit relationships
        for rel in implicit_rels:
            if rel[0] in core_tables and rel[2] in core_tables:
                rel_key = f'{rel[0]}-{rel[2]}'
                if rel_key not in added_rels:
                    f.write(f'    {rel[2]} ||--o{{ {rel[0]} : "{rel[1]}"\n')
                    added_rels.add(rel_key)

        f.write('```\n\n')

        # Bid-related tables ERD
        bid_tables = [t for t in table_names if 'Bid' in t and t in core_tables]
        if bid_tables:
            f.write('---\n\n## Bidding System ERD\n\n')
            f.write('```mermaid\nerDiagram\n')

            for table in bid_tables[:15]:
                f.write(f'    {table} {{\n')
                if table in pk_lookup:
                    for pk_col in pk_lookup[table]:
                        f.write(f'        int {pk_col} PK\n')
                if table in col_lookup:
                    for col in col_lookup[table][:5]:
                        if table not in pk_lookup or col['name'] not in pk_lookup[table]:
                            f.write(f'        {col["type"]} {col["name"]}\n')
                f.write('    }\n')

            f.write('\n')

            for rel in implicit_rels:
                if rel[0] in bid_tables and rel[2] in bid_tables:
                    rel_key = f'{rel[0]}-{rel[2]}'
                    if rel_key not in added_rels:
                        f.write(f'    {rel[2]} ||--o{{ {rel[0]} : "{rel[1]}"\n')

            f.write('```\n\n')

        # Relationship summary
        f.write('---\n\n## Relationships Summary\n\n')
        f.write('### Defined Foreign Keys\n\n')
        if filtered_fks:
            f.write('| From Table | Column | To Table | To Column |\n')
            f.write('|------------|--------|----------|----------|\n')
            for fk in filtered_fks:
                f.write(f'| {fk[0]} | {fk[1]} | {fk[2]} | {fk[3]} |\n')
        else:
            f.write('*No foreign keys defined between these tables*\n')

        f.write('\n### Implied Relationships (by naming convention)\n\n')
        f.write('| From Table | Column | To Table | Implied |\n')
        f.write('|------------|--------|----------|--------|\n')
        for rel in implicit_rels[:50]:
            f.write(f'| {rel[0]} | {rel[1]} | {rel[2]} | {rel[1]} → {rel[3]} |\n')
        if len(implicit_rels) > 50:
            f.write(f'\n*...and {len(implicit_rels) - 50} more*\n')

    logger.info(f"[OK] ERD saved to {output_file}")
    print(f"\nERD diagram saved to: {output_file}")
    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate ERD diagram')
    parser.add_argument('--database', '-d', default='EDS', help='Database name (default: EDS)')
    parser.add_argument('--output', '-o', default='docs', help='Output directory (default: docs)')
    parser.add_argument('--min-rows', '-m', type=int, default=10000, help='Minimum rows (default: 10000)')

    args = parser.parse_args()

    try:
        generate_erd(database=args.database, output_dir=args.output, min_rows=args.min_rows)
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
