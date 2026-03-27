#!/usr/bin/env python3
"""
Generate Stored Procedure Documentation

Creates a comprehensive markdown document with all stored procedures,
their parameters, and source code.
"""

import os
import sys
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def generate_sproc_documentation(database='EDS', output_dir='docs'):
    """Generate documentation for all stored procedures."""

    logger = setup_logging('generate_sproc_docs')
    logger.info(f"Generating stored procedure documentation for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all stored procedures
    procs = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            p.create_date,
            p.modify_date,
            OBJECT_DEFINITION(p.object_id) AS ProcDefinition
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        ORDER BY s.name, p.name
    ''')
    logger.info(f"Found {len(procs)} stored procedures")

    # Get parameters for all procedures
    params = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            o.name AS ProcName,
            p.name AS ParamName,
            t.name AS DataType,
            p.max_length,
            p.precision,
            p.scale,
            p.is_output,
            p.has_default_value,
            p.parameter_id
        FROM sys.parameters p
        INNER JOIN sys.objects o ON p.object_id = o.object_id
        INNER JOIN sys.schemas s ON o.schema_id = s.schema_id
        INNER JOIN sys.types t ON p.user_type_id = t.user_type_id
        WHERE o.type = 'P'
        ORDER BY s.name, o.name, p.parameter_id
    ''')
    logger.info(f"Found {len(params)} parameters")

    db.disconnect()

    # Build parameter lookup
    param_lookup = {}
    for p in params:
        key = f'{p[0]}.{p[1]}'
        if key not in param_lookup:
            param_lookup[key] = []

        # Format type
        data_type = p[3]
        max_len = p[4]
        precision = p[5]
        scale = p[6]

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

        param_lookup[key].append({
            'name': p[2],
            'type': type_str,
            'is_output': p[7],
            'has_default': p[8]
        })

    # Generate markdown
    logger.info("Generating documentation...")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_STORED_PROCEDURES.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Stored Procedures\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Summary\n\n')
        f.write(f'| Metric | Count |\n')
        f.write(f'|--------|-------|\n')
        f.write(f'| Total Stored Procedures | {len(procs)} |\n')
        f.write(f'| Total Parameters | {len(params)} |\n')
        f.write('\n')

        # Group by prefix for categorization
        prefixes = {}
        for proc in procs:
            name = proc[1]
            if name.startswith('sp_'):
                prefix = 'sp_'
            elif name.startswith('usp_'):
                prefix = 'usp_'
            elif name.startswith('fn_'):
                prefix = 'fn_'
            elif '_' in name:
                prefix = name.split('_')[0] + '_'
            else:
                prefix = 'Other'

            if prefix not in prefixes:
                prefixes[prefix] = 0
            prefixes[prefix] += 1

        f.write('### By Naming Convention\n\n')
        f.write('| Prefix | Count | Description |\n')
        f.write('|--------|-------|-------------|\n')
        for prefix, count in sorted(prefixes.items(), key=lambda x: -x[1]):
            desc = ''
            if prefix == 'sp_':
                desc = 'Standard stored procedures'
            elif prefix == 'usp_':
                desc = 'User stored procedures'
            elif prefix == 'fn_':
                desc = 'Functions'
            f.write(f'| {prefix} | {count} | {desc} |\n')
        f.write('\n')

        # Recently modified
        recent = sorted(procs, key=lambda x: x[3] if x[3] else datetime.min, reverse=True)[:20]
        f.write('### Recently Modified (Top 20)\n\n')
        f.write('| Procedure | Modified | Created |\n')
        f.write('|-----------|----------|--------|\n')
        for proc in recent:
            anchor = f'{proc[0]}-{proc[1]}'.lower().replace('_', '-')
            f.write(f'| [{proc[1]}](#{anchor}) | {proc[3]} | {proc[2]} |\n')
        f.write('\n---\n\n')

        # Table of contents
        f.write('## Table of Contents\n\n')
        current_schema = ''
        for proc in procs:
            schema, name = proc[0], proc[1]
            if schema != current_schema:
                f.write(f'\n### Schema: {schema}\n\n')
                current_schema = schema
            anchor = f'{schema}-{name}'.lower().replace('_', '-')
            f.write(f'- [{name}](#{anchor})\n')

        f.write('\n---\n\n')

        # Procedure details
        f.write('## Procedure Definitions\n\n')

        current_schema = ''
        for proc in procs:
            schema, name, created, modified, definition = proc
            proc_key = f'{schema}.{name}'
            anchor = f'{schema}-{name}'.lower().replace('_', '-')

            if schema != current_schema:
                f.write(f'---\n\n## Schema: {schema}\n\n')
                current_schema = schema

            f.write(f'### {name} {{{anchor}}}\n\n')
            f.write(f'| Property | Value |\n')
            f.write(f'|----------|-------|\n')
            f.write(f'| **Schema** | {schema} |\n')
            f.write(f'| **Created** | {created} |\n')
            f.write(f'| **Modified** | {modified} |\n')
            f.write('\n')

            # Parameters
            if proc_key in param_lookup:
                f.write('#### Parameters\n\n')
                f.write('| Parameter | Type | Direction | Default |\n')
                f.write('|-----------|------|-----------|--------|\n')
                for param in param_lookup[proc_key]:
                    direction = 'OUTPUT' if param['is_output'] else 'INPUT'
                    has_default = 'Yes' if param['has_default'] else 'No'
                    f.write(f'| {param["name"]} | {param["type"]} | {direction} | {has_default} |\n')
                f.write('\n')
            else:
                f.write('#### Parameters\n\n*No parameters*\n\n')

            # Source code
            f.write('#### Source Code\n\n')
            if definition:
                # Truncate very long procedures
                if len(definition) > 5000:
                    f.write(f'*Source truncated ({len(definition):,} characters). First 5000 shown:*\n\n')
                    definition = definition[:5000] + '\n-- ... truncated ...'
                f.write('```sql\n')
                f.write(definition)
                f.write('\n```\n\n')
            else:
                f.write('*Source code not available (encrypted or permission denied)*\n\n')

    logger.info(f"[OK] Documentation saved to {output_file}")
    print(f"\nStored procedure documentation saved to: {output_file}")
    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate stored procedure documentation')
    parser.add_argument('--database', '-d', default='EDS', help='Database name (default: EDS)')
    parser.add_argument('--output', '-o', default='docs', help='Output directory (default: docs)')

    args = parser.parse_args()

    try:
        generate_sproc_documentation(database=args.database, output_dir=args.output)
    except DatabaseConnectionError as e:
        print(f"Connection failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
