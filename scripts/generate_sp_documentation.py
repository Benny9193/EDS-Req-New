#!/usr/bin/env python3
"""
Generate Stored Procedure Documentation

Creates a comprehensive markdown document with all stored procedure definitions,
parameters, and descriptions.
"""

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def generate_sp_documentation(database='EDS', output_dir='docs'):
    """Generate stored procedure documentation."""

    logger = setup_logging('generate_sp_documentation')
    logger.info(f"Generating SP documentation for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all stored procedures with descriptions
    procs = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            ISNULL(CAST(ep.value AS NVARCHAR(MAX)), '') AS Description,
            p.create_date,
            p.modify_date
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON p.object_id = ep.major_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        ORDER BY s.name, p.name
    ''')
    logger.info(f"Found {len(procs)} stored procedures")

    # Get all parameters with descriptions
    params = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            pm.name AS ParamName,
            pm.parameter_id,
            t.name AS DataType,
            pm.max_length,
            pm.precision,
            pm.scale,
            pm.is_output,
            pm.has_default_value,
            ISNULL(CAST(ep.value AS NVARCHAR(MAX)), '') AS Description
        FROM sys.parameters pm
        INNER JOIN sys.procedures p ON pm.object_id = p.object_id
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        INNER JOIN sys.types t ON pm.user_type_id = t.user_type_id
        LEFT JOIN sys.extended_properties ep ON pm.object_id = ep.major_id
            AND pm.parameter_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE pm.parameter_id > 0
        ORDER BY s.name, p.name, pm.parameter_id
    ''')
    logger.info(f"Found {len(params)} parameters")

    # Get procedure definitions (first 4000 chars to avoid huge output)
    definitions = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            LEFT(OBJECT_DEFINITION(p.object_id), 4000) AS Definition
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        ORDER BY s.name, p.name
    ''')
    logger.info(f"Retrieved {len(definitions)} procedure definitions")

    db.disconnect()

    # Build lookups
    param_lookup = {}
    for p in params:
        key = f'{p[0]}.{p[1]}'
        if key not in param_lookup:
            param_lookup[key] = []
        param_lookup[key].append({
            'name': p[2],
            'id': p[3],
            'type': p[4],
            'max_length': p[5],
            'precision': p[6],
            'scale': p[7],
            'is_output': p[8],
            'has_default': p[9],
            'description': p[10]
        })

    def_lookup = {}
    for d in definitions:
        key = f'{d[0]}.{d[1]}'
        def_lookup[key] = d[2] if d[2] else ''

    # Generate markdown
    logger.info("Generating markdown documentation...")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_STORED_PROCEDURES.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Stored Procedures Documentation\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Summary\n\n')
        f.write('| Metric | Count |\n')
        f.write('|--------|-------|\n')
        f.write(f'| Total Stored Procedures | {len(procs)} |\n')
        f.write(f'| Total Parameters | {len(params)} |\n')

        # Count documented
        documented_procs = sum(1 for p in procs if p[2])
        documented_params = sum(1 for p in params if p[10])
        f.write(f'| Documented Procedures | {documented_procs} ({100*documented_procs/len(procs):.1f}%) |\n')
        f.write(f'| Documented Parameters | {documented_params} ({100*documented_params/len(params):.1f}%) |\n')
        f.write('\n')

        # Table of contents
        f.write('## Table of Contents\n\n')
        current_schema = ''
        for proc in procs:
            schema, name = proc[0], proc[1]
            if schema != current_schema:
                f.write(f'\n### Schema: {schema}\n\n')
                current_schema = schema
            anchor = f'sp-{schema}-{name}'.lower().replace('_', '-')
            f.write(f'- [{name}](#{anchor})\n')

        f.write('\n---\n\n')

        # Procedure details
        f.write('## Stored Procedure Definitions\n\n')
        current_schema = ''

        for proc in procs:
            schema, name, desc, created, modified = proc
            proc_key = f'{schema}.{name}'
            anchor = f'sp-{schema}-{name}'.lower().replace('_', '-')

            if schema != current_schema:
                f.write(f'---\n\n## Schema: {schema}\n\n')
                current_schema = schema

            f.write(f'### {name} {{{anchor}}}\n\n')

            # Description
            if desc:
                f.write(f'> {desc}\n\n')

            # Properties
            f.write('| Property | Value |\n')
            f.write('|----------|-------|\n')
            f.write(f'| **Schema** | {schema} |\n')
            f.write(f'| **Created** | {created} |\n')
            f.write(f'| **Modified** | {modified} |\n')

            proc_params = param_lookup.get(proc_key, [])
            f.write(f'| **Parameters** | {len(proc_params)} |\n')
            f.write('\n')

            # Parameters table
            if proc_params:
                f.write('#### Parameters\n\n')
                f.write('| # | Parameter | Type | Direction | Description |\n')
                f.write('|---|-----------|------|-----------|-------------|\n')

                for param in proc_params:
                    # Format type
                    data_type = param['type']
                    max_len = param['max_length']
                    precision = param['precision']
                    scale = param['scale']

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

                    direction = 'OUTPUT' if param['is_output'] else 'INPUT'
                    if param['has_default']:
                        direction += ' (optional)'

                    param_desc = param['description'].replace('|', '\\|') if param['description'] else ''

                    f.write(f'| {param["id"]} | {param["name"]} | {type_str} | {direction} | {param_desc} |\n')

                f.write('\n')

            # Procedure definition (truncated)
            definition = def_lookup.get(proc_key, '')
            if definition:
                f.write('#### Definition\n\n')
                f.write('```sql\n')
                # Clean up and truncate definition
                def_clean = definition.strip()
                if len(def_clean) >= 3900:
                    def_clean = def_clean[:3900] + '\n\n-- [Definition truncated...]'
                f.write(def_clean)
                f.write('\n```\n\n')

            f.write('\n')

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
        generate_sp_documentation(database=args.database, output_dir=args.output)
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
