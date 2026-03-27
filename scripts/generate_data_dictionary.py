#!/usr/bin/env python3
"""
Generate EDS Database Data Dictionary

Creates a comprehensive markdown document with all tables, columns,
data types, constraints, and relationships.
"""

import os
import sys
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def generate_data_dictionary(database='EDS', output_dir='docs'):
    """Generate a complete data dictionary for the specified database."""

    logger = setup_logging('generate_data_dictionary')
    logger.info(f"Generating data dictionary for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    logger.info("Extracting schema information...")

    # Get all tables with row counts
    tables = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            ISNULL(p.row_count, 0) AS [Rows],
            t.create_date,
            t.modify_date
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.dm_db_partition_stats p ON t.object_id = p.object_id AND p.index_id < 2
        ORDER BY s.name, t.name
    ''')
    logger.info(f"Found {len(tables)} tables")

    # Get all columns
    columns = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            c.name AS ColumnName,
            ty.name AS DataType,
            c.max_length,
            c.precision,
            c.scale,
            c.is_nullable,
            c.is_identity,
            ISNULL(dc.definition, '') AS DefaultValue,
            c.column_id
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        INNER JOIN sys.types ty ON c.user_type_id = ty.user_type_id
        LEFT JOIN sys.default_constraints dc ON c.default_object_id = dc.object_id
        ORDER BY s.name, t.name, c.column_id
    ''')
    logger.info(f"Found {len(columns)} columns")

    # Get primary keys
    pks = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            c.name AS ColumnName,
            i.name AS PKName
        FROM sys.indexes i
        INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
        INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE i.is_primary_key = 1
        ORDER BY s.name, t.name, ic.key_ordinal
    ''')
    logger.info(f"Found {len(pks)} primary key columns")

    # Get foreign keys
    fks = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            c.name AS ColumnName,
            fk.name AS FKName,
            rs.name AS RefSchema,
            rt.name AS RefTable,
            rc.name AS RefColumn
        FROM sys.foreign_key_columns fkc
        INNER JOIN sys.foreign_keys fk ON fkc.constraint_object_id = fk.object_id
        INNER JOIN sys.tables t ON fkc.parent_object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        INNER JOIN sys.columns c ON fkc.parent_object_id = c.object_id AND fkc.parent_column_id = c.column_id
        INNER JOIN sys.tables rt ON fkc.referenced_object_id = rt.object_id
        INNER JOIN sys.schemas rs ON rt.schema_id = rs.schema_id
        INNER JOIN sys.columns rc ON fkc.referenced_object_id = rc.object_id AND fkc.referenced_column_id = rc.column_id
        ORDER BY s.name, t.name
    ''')
    logger.info(f"Found {len(fks)} foreign key relationships")

    # Get indexes
    indexes = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            i.name AS IndexName,
            i.type_desc AS IndexType,
            i.is_unique,
            STRING_AGG(c.name, ', ') WITHIN GROUP (ORDER BY ic.key_ordinal) AS Columns
        FROM sys.indexes i
        INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
        INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
        INNER JOIN sys.tables t ON i.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE i.type > 0 AND i.is_primary_key = 0
        GROUP BY s.name, t.name, i.name, i.type_desc, i.is_unique
        ORDER BY s.name, t.name, i.name
    ''')
    logger.info(f"Found {len(indexes)} indexes")

    # Get table descriptions (MS_Description extended properties)
    table_descs = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            CAST(ep.value AS NVARCHAR(MAX)) AS Description
        FROM sys.extended_properties ep
        INNER JOIN sys.tables t ON ep.major_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE ep.name = 'MS_Description' AND ep.minor_id = 0
    ''')
    logger.info(f"Found {len(table_descs)} table descriptions")

    # Get column descriptions (MS_Description extended properties)
    col_descs = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            c.name AS ColumnName,
            CAST(ep.value AS NVARCHAR(MAX)) AS Description
        FROM sys.extended_properties ep
        INNER JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE ep.name = 'MS_Description'
    ''')
    logger.info(f"Found {len(col_descs)} column descriptions")

    # Get views
    views = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName,
            (SELECT COUNT(*) FROM sys.columns WHERE object_id = v.object_id) AS ColumnCount,
            v.create_date,
            v.modify_date
        FROM sys.views v
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        ORDER BY s.name, v.name
    ''')
    logger.info(f"Found {len(views)} views")

    # Get view descriptions
    view_descs = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName,
            CAST(ep.value AS NVARCHAR(MAX)) AS Description
        FROM sys.extended_properties ep
        INNER JOIN sys.views v ON ep.major_id = v.object_id
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        WHERE ep.name = 'MS_Description' AND ep.minor_id = 0
    ''')
    logger.info(f"Found {len(view_descs)} view descriptions")

    # Get view columns
    view_columns = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName,
            c.name AS ColumnName,
            ty.name AS DataType,
            c.max_length,
            c.precision,
            c.scale,
            c.is_nullable,
            c.column_id
        FROM sys.columns c
        INNER JOIN sys.views v ON c.object_id = v.object_id
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        INNER JOIN sys.types ty ON c.user_type_id = ty.user_type_id
        ORDER BY s.name, v.name, c.column_id
    ''')
    logger.info(f"Found {len(view_columns)} view columns")

    # Get view column descriptions
    view_col_descs = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName,
            c.name AS ColumnName,
            CAST(ep.value AS NVARCHAR(MAX)) AS Description
        FROM sys.extended_properties ep
        INNER JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id
        INNER JOIN sys.views v ON c.object_id = v.object_id
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        WHERE ep.name = 'MS_Description'
    ''')
    logger.info(f"Found {len(view_col_descs)} view column descriptions")

    db.disconnect()

    # Build lookup dictionaries
    pk_lookup = {}
    for pk in pks:
        key = f'{pk[0]}.{pk[1]}'
        if key not in pk_lookup:
            pk_lookup[key] = []
        pk_lookup[key].append(pk[2])

    fk_lookup = {}
    for fk in fks:
        key = f'{fk[0]}.{fk[1]}.{fk[2]}'
        fk_lookup[key] = f'{fk[4]}.{fk[5]}.{fk[6]}'

    idx_lookup = {}
    for idx in indexes:
        key = f'{idx[0]}.{idx[1]}'
        if key not in idx_lookup:
            idx_lookup[key] = []
        idx_lookup[key].append({
            'name': idx[2],
            'type': idx[3],
            'unique': idx[4],
            'columns': idx[5]
        })

    # Build description lookups
    table_desc_lookup = {}
    for td in table_descs:
        key = f'{td[0]}.{td[1]}'
        table_desc_lookup[key] = td[2]

    col_desc_lookup = {}
    for cd in col_descs:
        key = f'{cd[0]}.{cd[1]}.{cd[2]}'
        col_desc_lookup[key] = cd[3]

    # Build view description lookups
    view_desc_lookup = {}
    for vd in view_descs:
        key = f'{vd[0]}.{vd[1]}'
        view_desc_lookup[key] = vd[2]

    view_col_desc_lookup = {}
    for vcd in view_col_descs:
        key = f'{vcd[0]}.{vcd[1]}.{vcd[2]}'
        view_col_desc_lookup[key] = vcd[3]

    # Generate markdown
    logger.info("Generating documentation...")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_DATA_DICTIONARY.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database Data Dictionary\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Summary\n\n')
        f.write('| Metric | Count |\n')
        f.write('|--------|-------|\n')
        f.write(f'| Tables | {len(tables)} |\n')
        f.write(f'| Table Columns | {len(columns)} |\n')
        f.write(f'| Views | {len(views)} |\n')
        f.write(f'| View Columns | {len(view_columns)} |\n')
        f.write(f'| Tables with Primary Keys | {len(pk_lookup)} |\n')
        f.write(f'| Foreign Key Relationships | {len(fks)} |\n')
        f.write(f'| Non-PK Indexes | {len(indexes)} |\n')
        f.write('\n')

        # Documentation coverage
        f.write('### Documentation Coverage\n\n')
        f.write('| Object Type | Documented | Total | Coverage |\n')
        f.write('|-------------|------------|-------|----------|\n')
        f.write(f'| Tables | {len(table_desc_lookup)} | {len(tables)} | {100*len(table_desc_lookup)/len(tables):.1f}% |\n')
        f.write(f'| Table Columns | {len(col_desc_lookup)} | {len(columns)} | {100*len(col_desc_lookup)/len(columns):.1f}% |\n')
        f.write(f'| Views | {len(view_desc_lookup)} | {len(views)} | {100*len(view_desc_lookup)/len(views):.1f}% |\n')
        f.write(f'| View Columns | {len(view_col_desc_lookup)} | {len(view_columns)} | {100*len(view_col_desc_lookup)/len(view_columns):.1f}% |\n')
        f.write('\n')

        # Tables without PKs
        tables_without_pk = [t for t in tables if f'{t[0]}.{t[1]}' not in pk_lookup]
        if tables_without_pk:
            f.write(f'### Tables Without Primary Keys ({len(tables_without_pk)})\n\n')
            f.write('| Schema | Table | Rows |\n')
            f.write('|--------|-------|------|\n')
            for t in tables_without_pk[:20]:
                f.write(f'| {t[0]} | {t[1]} | {t[2]:,} |\n')
            if len(tables_without_pk) > 20:
                f.write(f'\n*...and {len(tables_without_pk) - 20} more*\n')
            f.write('\n')

        f.write('---\n\n')

        # Table of contents
        f.write('## Table of Contents\n\n')
        current_schema = ''
        for tbl in tables:
            schema, name = tbl[0], tbl[1]
            if schema != current_schema:
                f.write(f'\n### Schema: {schema}\n\n')
                current_schema = schema
            anchor = f'{schema}-{name}'.lower().replace('_', '-')
            f.write(f'- [{name}](#{anchor})\n')

        f.write('\n---\n\n')

        # Table details
        f.write('## Table Definitions\n\n')

        current_schema = ''

        for tbl in tables:
            schema, name, rows, created, modified = tbl
            table_key = f'{schema}.{name}'
            anchor = f'{schema}-{name}'.lower().replace('_', '-')

            if schema != current_schema:
                f.write(f'---\n\n## Schema: {schema}\n\n')
                current_schema = schema

            f.write(f'### {name} {{{anchor}}}\n\n')

            # Table description
            if table_key in table_desc_lookup:
                f.write(f'> {table_desc_lookup[table_key]}\n\n')

            f.write(f'| Property | Value |\n')
            f.write(f'|----------|-------|\n')
            f.write(f'| **Schema** | {schema} |\n')
            f.write(f'| **Rows** | {rows:,} |\n')
            f.write(f'| **Created** | {created} |\n')
            f.write(f'| **Modified** | {modified} |\n')

            # Primary key
            if table_key in pk_lookup:
                f.write(f'| **Primary Key** | {", ".join(pk_lookup[table_key])} |\n')
            else:
                f.write(f'| **Primary Key** | *None* |\n')

            f.write('\n')

            # Columns table
            f.write('#### Columns\n\n')
            f.write('| # | Column | Type | Nullable | Default | Key | Description |\n')
            f.write('|---|--------|------|----------|---------|-----|-------------|\n')

            # Get columns for this table
            table_cols = [c for c in columns if c[0] == schema and c[1] == name]

            for col in table_cols:
                col_id = col[10]
                col_name = col[2]
                data_type = col[3]
                max_len = col[4]
                precision = col[5]
                scale = col[6]
                nullable = 'Yes' if col[7] else 'No'
                is_identity = col[8]
                default = col[9] if col[9] else ''

                # Format type
                if data_type in ('varchar', 'nvarchar', 'char', 'nchar', 'varbinary'):
                    if max_len == -1:
                        type_str = f'{data_type}(MAX)'
                    elif data_type.startswith('n'):
                        type_str = f'{data_type}({max_len // 2})'
                    else:
                        type_str = f'{data_type}({max_len})'
                elif data_type in ('decimal', 'numeric'):
                    type_str = f'{data_type}({precision},{scale})'
                else:
                    type_str = data_type

                if is_identity:
                    type_str += ' IDENTITY'

                # Key indicator
                key = ''
                if table_key in pk_lookup and col_name in pk_lookup[table_key]:
                    key = 'PK'
                fk_key = f'{schema}.{name}.{col_name}'
                if fk_key in fk_lookup:
                    key = f'FK → {fk_lookup[fk_key]}'

                # Escape pipe characters in default values
                default = default.replace('|', '\\|')

                # Get column description
                col_desc_key = f'{schema}.{name}.{col_name}'
                col_description = col_desc_lookup.get(col_desc_key, '')
                col_description = col_description.replace('|', '\\|') if col_description else ''

                f.write(f'| {col_id} | {col_name} | {type_str} | {nullable} | {default} | {key} | {col_description} |\n')

            # Indexes
            if table_key in idx_lookup:
                f.write('\n#### Indexes\n\n')
                f.write('| Index Name | Type | Unique | Columns |\n')
                f.write('|------------|------|--------|--------|\n')
                for idx in idx_lookup[table_key]:
                    unique = 'Yes' if idx['unique'] else 'No'
                    f.write(f'| {idx["name"]} | {idx["type"]} | {unique} | {idx["columns"]} |\n')

            f.write('\n')

        # =====================================================================
        # Views Section
        # =====================================================================
        f.write('\n---\n\n')
        f.write('# Database Views\n\n')
        f.write(f'Total Views: {len(views)}\n\n')

        # Views table of contents
        f.write('## Views Table of Contents\n\n')
        current_schema = ''
        for vw in views:
            schema, name = vw[0], vw[1]
            if schema != current_schema:
                f.write(f'\n### Schema: {schema}\n\n')
                current_schema = schema
            anchor = f'view-{schema}-{name}'.lower().replace('_', '-')
            f.write(f'- [{name}](#{anchor})\n')

        f.write('\n---\n\n')

        # View details
        f.write('## View Definitions\n\n')
        current_schema = ''

        for vw in views:
            schema, name, col_count, created, modified = vw
            view_key = f'{schema}.{name}'
            anchor = f'view-{schema}-{name}'.lower().replace('_', '-')

            if schema != current_schema:
                f.write(f'---\n\n## Views in Schema: {schema}\n\n')
                current_schema = schema

            f.write(f'### {name} {{{anchor}}}\n\n')

            # View description
            if view_key in view_desc_lookup:
                f.write(f'> {view_desc_lookup[view_key]}\n\n')

            f.write(f'| Property | Value |\n')
            f.write(f'|----------|-------|\n')
            f.write(f'| **Schema** | {schema} |\n')
            f.write(f'| **Columns** | {col_count} |\n')
            f.write(f'| **Created** | {created} |\n')
            f.write(f'| **Modified** | {modified} |\n')
            f.write('\n')

            # View columns table
            f.write('#### Columns\n\n')
            f.write('| # | Column | Type | Nullable | Description |\n')
            f.write('|---|--------|------|----------|-------------|\n')

            # Get columns for this view
            vw_cols = [c for c in view_columns if c[0] == schema and c[1] == name]

            for col in vw_cols:
                col_id = col[8]
                col_name = col[2]
                data_type = col[3]
                max_len = col[4]
                precision = col[5]
                scale = col[6]
                nullable = 'Yes' if col[7] else 'No'

                # Format type
                if data_type in ('varchar', 'nvarchar', 'char', 'nchar', 'varbinary'):
                    if max_len == -1:
                        type_str = f'{data_type}(MAX)'
                    elif data_type.startswith('n'):
                        type_str = f'{data_type}({max_len // 2})'
                    else:
                        type_str = f'{data_type}({max_len})'
                elif data_type in ('decimal', 'numeric'):
                    type_str = f'{data_type}({precision},{scale})'
                else:
                    type_str = data_type

                # Get column description
                col_desc_key = f'{schema}.{name}.{col_name}'
                col_description = view_col_desc_lookup.get(col_desc_key, '')
                col_description = col_description.replace('|', '\\|') if col_description else ''

                f.write(f'| {col_id} | {col_name} | {type_str} | {nullable} | {col_description} |\n')

            f.write('\n')

    logger.info(f"[OK] Documentation saved to {output_file}")
    print(f"\nData dictionary saved to: {output_file}")
    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate database data dictionary')
    parser.add_argument('--database', '-d', default='EDS', help='Database name (default: EDS)')
    parser.add_argument('--output', '-o', default='docs', help='Output directory (default: docs)')

    args = parser.parse_args()

    try:
        generate_data_dictionary(database=args.database, output_dir=args.output)
    except DatabaseConnectionError as e:
        print(f"Connection failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
