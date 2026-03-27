#!/usr/bin/env python3
"""
Generate Views Documentation

Creates a comprehensive markdown document with all database views,
their columns, and SQL definitions.
"""

import os
import sys
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def generate_views_documentation(database='EDS', output_dir='docs'):
    """Generate documentation for all database views."""

    logger = setup_logging('generate_views_docs')
    logger.info(f"Generating views documentation for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all views
    views = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName,
            v.create_date,
            v.modify_date,
            OBJECT_DEFINITION(v.object_id) AS ViewDefinition
        FROM sys.views v
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        ORDER BY s.name, v.name
    ''')
    logger.info(f"Found {len(views)} views")

    # Get columns for all views
    columns = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName,
            c.name AS ColumnName,
            t.name AS DataType,
            c.max_length,
            c.precision,
            c.scale,
            c.is_nullable,
            c.column_id
        FROM sys.columns c
        INNER JOIN sys.views v ON c.object_id = v.object_id
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        INNER JOIN sys.types t ON c.user_type_id = t.user_type_id
        ORDER BY s.name, v.name, c.column_id
    ''')
    logger.info(f"Found {len(columns)} view columns")

    # Get view dependencies (what tables/views each view references)
    dependencies = db.execute_query('''
        SELECT DISTINCT
            s.name AS ViewSchema,
            v.name AS ViewName,
            COALESCE(rs.name, 'dbo') AS RefSchema,
            COALESCE(OBJECT_NAME(d.referenced_id), d.referenced_entity_name) AS RefObject,
            CASE
                WHEN rt.type = 'U' THEN 'Table'
                WHEN rt.type = 'V' THEN 'View'
                ELSE 'Other'
            END AS RefType
        FROM sys.views v
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        INNER JOIN sys.sql_expression_dependencies d ON v.object_id = d.referencing_id
        LEFT JOIN sys.objects rt ON d.referenced_id = rt.object_id
        LEFT JOIN sys.schemas rs ON rt.schema_id = rs.schema_id
        WHERE d.referenced_id IS NOT NULL OR d.referenced_entity_name IS NOT NULL
        ORDER BY s.name, v.name, RefObject
    ''')
    logger.info(f"Found {len(dependencies)} view dependencies")

    db.disconnect()

    # Build column lookup
    col_lookup = {}
    for col in columns:
        key = f'{col[0]}.{col[1]}'
        if key not in col_lookup:
            col_lookup[key] = []

        # Format type
        data_type = col[3]
        max_len = col[4]
        precision = col[5]
        scale = col[6]

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

        col_lookup[key].append({
            'name': col[2],
            'type': type_str,
            'nullable': col[7]
        })

    # Build dependency lookup
    dep_lookup = {}
    for dep in dependencies:
        key = f'{dep[0]}.{dep[1]}'
        if key not in dep_lookup:
            dep_lookup[key] = []
        dep_lookup[key].append({
            'schema': dep[2],
            'object': dep[3],
            'type': dep[4]
        })

    # Generate markdown
    logger.info("Generating documentation...")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_VIEWS.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Views Documentation\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Summary\n\n')
        f.write('| Metric | Count |\n')
        f.write('|--------|-------|\n')
        f.write(f'| Total Views | {len(views)} |\n')
        f.write(f'| Total Columns | {len(columns)} |\n')
        f.write(f'| Views with Dependencies | {len(dep_lookup)} |\n')
        f.write('\n')

        # Group by schema
        schemas = {}
        for view in views:
            schema = view[0]
            if schema not in schemas:
                schemas[schema] = 0
            schemas[schema] += 1

        f.write('### By Schema\n\n')
        f.write('| Schema | Views |\n')
        f.write('|--------|-------|\n')
        for schema, count in sorted(schemas.items()):
            f.write(f'| {schema} | {count} |\n')
        f.write('\n---\n\n')

        # Table of contents
        f.write('## Table of Contents\n\n')
        current_schema = ''
        for view in views:
            schema, name = view[0], view[1]
            if schema != current_schema:
                f.write(f'\n### Schema: {schema}\n\n')
                current_schema = schema
            anchor = f'{schema}-{name}'.lower().replace('_', '-')
            f.write(f'- [{name}](#{anchor})\n')

        f.write('\n---\n\n')

        # View details
        f.write('## View Definitions\n\n')

        current_schema = ''
        for view in views:
            schema, name, created, modified, definition = view
            view_key = f'{schema}.{name}'
            anchor = f'{schema}-{name}'.lower().replace('_', '-')

            if schema != current_schema:
                f.write(f'---\n\n## Schema: {schema}\n\n')
                current_schema = schema

            f.write(f'### {name} {{{anchor}}}\n\n')
            f.write('| Property | Value |\n')
            f.write('|----------|-------|\n')
            f.write(f'| **Schema** | {schema} |\n')
            f.write(f'| **Created** | {created} |\n')
            f.write(f'| **Modified** | {modified} |\n')
            f.write('\n')

            # Columns
            if view_key in col_lookup:
                f.write('#### Columns\n\n')
                f.write('| # | Column | Type | Nullable |\n')
                f.write('|---|--------|------|----------|\n')
                for i, col in enumerate(col_lookup[view_key], 1):
                    nullable = 'Yes' if col['nullable'] else 'No'
                    f.write(f'| {i} | {col["name"]} | {col["type"]} | {nullable} |\n')
                f.write('\n')

            # Dependencies
            if view_key in dep_lookup:
                f.write('#### Dependencies\n\n')
                f.write('| Object | Type |\n')
                f.write('|--------|------|\n')
                for dep in dep_lookup[view_key]:
                    f.write(f'| {dep["schema"]}.{dep["object"]} | {dep["type"]} |\n')
                f.write('\n')

            # SQL Definition
            f.write('#### SQL Definition\n\n')
            if definition:
                # Truncate very long definitions
                if len(definition) > 8000:
                    f.write(f'*Definition truncated ({len(definition):,} characters). First 8000 shown:*\n\n')
                    definition = definition[:8000] + '\n-- ... truncated ...'
                f.write('```sql\n')
                f.write(definition)
                f.write('\n```\n\n')
            else:
                f.write('*Definition not available (encrypted or permission denied)*\n\n')

    logger.info(f"[OK] Documentation saved to {output_file}")
    print(f"\nViews documentation saved to: {output_file}")
    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate views documentation')
    parser.add_argument('--database', '-d', default='EDS', help='Database name (default: EDS)')
    parser.add_argument('--output', '-o', default='docs', help='Output directory (default: docs)')

    args = parser.parse_args()

    try:
        generate_views_documentation(database=args.database, output_dir=args.output)
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
