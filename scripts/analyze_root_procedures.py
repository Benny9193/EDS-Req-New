#!/usr/bin/env python3
"""
Analyze Root Procedures

Identifies and documents the main entry point stored procedures -
those that call other procedures but are not called by any.
"""

import os
import sys
import re
from datetime import datetime
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def analyze_root_procedures(database='EDS', output_dir='docs'):
    """Analyze root/entry point stored procedures."""

    logger = setup_logging('analyze_root_procedures')
    logger.info(f"Analyzing root procedures for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all stored procedures with definitions
    procedures = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            p.create_date,
            p.modify_date,
            OBJECT_DEFINITION(p.object_id) AS Definition,
            ISNULL(ep.value, '') AS Description
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON p.object_id = ep.major_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        ORDER BY s.name, p.name
    ''')
    logger.info(f"Found {len(procedures)} stored procedures")

    # Get SQL dependencies
    sql_deps = db.execute_query('''
        SELECT DISTINCT
            OBJECT_SCHEMA_NAME(d.referencing_id) AS CallerSchema,
            OBJECT_NAME(d.referencing_id) AS CallerName,
            d.referenced_entity_name AS RefName,
            o.type_desc AS RefType
        FROM sys.sql_expression_dependencies d
        INNER JOIN sys.procedures p ON d.referencing_id = p.object_id
        LEFT JOIN sys.objects o ON d.referenced_id = o.object_id
        WHERE d.referenced_entity_name IS NOT NULL
    ''')

    # Get parameter info for each procedure
    params = db.execute_query('''
        SELECT
            OBJECT_SCHEMA_NAME(p.object_id) AS SchemaName,
            OBJECT_NAME(p.object_id) AS ProcName,
            p.name AS ParamName,
            TYPE_NAME(p.user_type_id) AS ParamType,
            p.max_length,
            p.is_output
        FROM sys.parameters p
        INNER JOIN sys.procedures pr ON p.object_id = pr.object_id
        WHERE p.parameter_id > 0
        ORDER BY OBJECT_NAME(p.object_id), p.parameter_id
    ''')

    db.disconnect()

    # Build dependency maps
    sp_calls_sp = defaultdict(set)
    sp_accesses_table = defaultdict(set)
    called_procs = set()

    for dep in sql_deps:
        caller = f"{dep[0]}.{dep[1]}"
        if dep[3] == 'SQL_STORED_PROCEDURE':
            sp_calls_sp[caller].add(dep[2])
            called_procs.add(dep[2])
        elif dep[3] in ('USER_TABLE', 'SYSTEM_TABLE'):
            sp_accesses_table[caller].add(dep[2])

    # Also check EXEC patterns
    exec_pattern = re.compile(r'\bEXEC(?:UTE)?\s+(?:\[?(\w+)\]?\.)?\[?(\w+)\]?', re.IGNORECASE)
    sp_names = {p[1] for p in procedures}

    for schema, proc, _, _, definition, _ in procedures:
        if definition:
            caller = f"{schema}.{proc}"
            matches = exec_pattern.findall(definition)
            for _, match_proc in matches:
                if match_proc in sp_names and match_proc != proc:
                    sp_calls_sp[caller].add(match_proc)
                    called_procs.add(match_proc)

    # Find root procedures
    all_callers = {p.split('.')[-1] for p in sp_calls_sp.keys()}
    root_proc_names = all_callers - called_procs

    # Build parameter lookup
    param_lookup = defaultdict(list)
    for schema, proc, param, ptype, length, is_output in params:
        param_lookup[proc].append({
            'name': param,
            'type': ptype,
            'length': length,
            'output': is_output
        })

    # Get root procedure details
    root_procs = []
    for schema, proc, created, modified, definition, desc in procedures:
        if proc in root_proc_names:
            key = f"{schema}.{proc}"
            calls = sp_calls_sp.get(key, set())
            tables = sp_accesses_table.get(key, set())
            root_procs.append({
                'schema': schema,
                'name': proc,
                'created': created,
                'modified': modified,
                'description': desc,
                'calls': calls,
                'tables': tables,
                'params': param_lookup.get(proc, []),
                'definition': definition
            })

    logger.info(f"Found {len(root_procs)} root procedures")

    # Categorize by naming convention
    categories = defaultdict(list)
    for proc in root_procs:
        name = proc['name'].lower()
        if 'bid' in name:
            categories['Bidding'].append(proc)
        elif 'req' in name:
            categories['Requisitions'].append(proc)
        elif 'po' in name or 'order' in name:
            categories['Purchase Orders'].append(proc)
        elif 'report' in name or 'rpt' in name:
            categories['Reporting'].append(proc)
        elif 'user' in name or 'account' in name:
            categories['User Management'].append(proc)
        elif 'email' in name or 'blast' in name:
            categories['Email/Notifications'].append(proc)
        elif 'import' in name or 'export' in name:
            categories['Import/Export'].append(proc)
        elif 'budget' in name:
            categories['Budgets'].append(proc)
        else:
            categories['Other'].append(proc)

    # Generate documentation
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_ROOT_PROCEDURES.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Root Procedure Analysis\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('Root procedures are entry points that call other procedures but are not called by any.\n')
        f.write('These represent the main business operations and workflows.\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Summary\n\n')
        f.write(f'**Total Root Procedures:** {len(root_procs)}\n\n')
        f.write('| Category | Count |\n')
        f.write('|----------|-------|\n')
        for cat in sorted(categories.keys()):
            f.write(f'| {cat} | {len(categories[cat])} |\n')
        f.write('\n---\n\n')

        # Category sections
        for cat in ['Bidding', 'Requisitions', 'Purchase Orders', 'Budgets',
                    'User Management', 'Email/Notifications', 'Reporting',
                    'Import/Export', 'Other']:
            procs = categories.get(cat, [])
            if not procs:
                continue

            f.write(f'## {cat} ({len(procs)} procedures)\n\n')

            for proc in sorted(procs, key=lambda x: x['name']):
                f.write(f'### {proc["name"]}\n\n')

                if proc['description']:
                    f.write(f'*{proc["description"]}*\n\n')

                f.write(f'- **Schema:** {proc["schema"]}\n')
                f.write(f'- **Created:** {proc["created"]}\n')
                f.write(f'- **Modified:** {proc["modified"]}\n')

                if proc['params']:
                    f.write(f'- **Parameters:** {len(proc["params"])}\n')
                    for p in proc['params']:
                        out = ' (OUTPUT)' if p['output'] else ''
                        f.write(f'  - `{p["name"]}` {p["type"]}{out}\n')

                if proc['calls']:
                    f.write(f'- **Calls:** {", ".join(sorted(proc["calls"]))}\n')

                if proc['tables']:
                    f.write(f'- **Tables accessed:** {", ".join(sorted(list(proc["tables"])[:10]))}\n')
                    if len(proc['tables']) > 10:
                        f.write(f'  - *...and {len(proc["tables"]) - 10} more*\n')

                f.write('\n')

            f.write('---\n\n')

        # Call chain depth analysis
        f.write('## Call Chain Analysis\n\n')
        f.write('Root procedures ranked by call chain complexity:\n\n')
        f.write('| Procedure | Direct Calls | Tables | Parameters |\n')
        f.write('|-----------|--------------|--------|------------|\n')

        sorted_procs = sorted(root_procs,
                             key=lambda x: len(x['calls']) + len(x['tables']),
                             reverse=True)
        for proc in sorted_procs[:30]:
            f.write(f'| {proc["name"]} | {len(proc["calls"])} | {len(proc["tables"])} | {len(proc["params"])} |\n')

        f.write('\n---\n\n')

        # Workflow diagram
        f.write('## Main Workflows\n\n')
        f.write('```mermaid\nflowchart TD\n')
        f.write('    subgraph Bidding\n')
        for proc in categories.get('Bidding', [])[:5]:
            p_id = proc['name'].replace(' ', '_')
            f.write(f'        {p_id}["{proc["name"]}"]\n')
        f.write('    end\n')
        f.write('    subgraph Requisitions\n')
        for proc in categories.get('Requisitions', [])[:5]:
            p_id = proc['name'].replace(' ', '_')
            f.write(f'        {p_id}["{proc["name"]}"]\n')
        f.write('    end\n')
        f.write('    subgraph PurchaseOrders["Purchase Orders"]\n')
        for proc in categories.get('Purchase Orders', [])[:5]:
            p_id = proc['name'].replace(' ', '_')
            f.write(f'        {p_id}["{proc["name"]}"]\n')
        f.write('    end\n')
        f.write('```\n')

    logger.info(f"[OK] Root procedure analysis saved to {output_file}")
    print(f"\nRoot procedure analysis saved to: {output_file}")
    print(f"  Total root procedures: {len(root_procs)}")
    for cat in sorted(categories.keys()):
        print(f"  - {cat}: {len(categories[cat])}")

    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Analyze root procedures')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')

    args = parser.parse_args()

    try:
        analyze_root_procedures(database=args.database, output_dir=args.output)
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
