#!/usr/bin/env python3
"""
Generate Stored Procedure Dependency Diagrams

Creates Mermaid diagrams showing:
- Which stored procedures call other procedures
- Which tables/views each procedure accesses
- Dependency chains and clusters
"""

import os
import sys
import re
from datetime import datetime
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def generate_sp_dependencies(database='EDS', output_dir='docs'):
    """Generate stored procedure dependency diagrams."""

    logger = setup_logging('generate_sp_dependencies')
    logger.info(f"Analyzing SP dependencies for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all stored procedures with their definitions
    procedures = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            OBJECT_DEFINITION(p.object_id) AS Definition
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        ORDER BY s.name, p.name
    ''')
    logger.info(f"Found {len(procedures)} stored procedures")

    # Get all table names
    tables = db.execute_query('''
        SELECT s.name AS SchemaName, t.name AS TableName
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
    ''')
    table_names = {f"{t[0]}.{t[1]}" for t in tables}
    table_names.update({t[1] for t in tables})  # Also add without schema

    # Get all view names
    views = db.execute_query('''
        SELECT s.name AS SchemaName, v.name AS ViewName
        FROM sys.views v
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
    ''')
    view_names = {f"{v[0]}.{v[1]}" for v in views}
    view_names.update({v[1] for v in views})

    # Get SQL Server dependency info
    sql_deps = db.execute_query('''
        SELECT DISTINCT
            OBJECT_SCHEMA_NAME(d.referencing_id) AS CallerSchema,
            OBJECT_NAME(d.referencing_id) AS CallerName,
            COALESCE(d.referenced_schema_name, 'dbo') AS RefSchema,
            d.referenced_entity_name AS RefName,
            o.type_desc AS RefType
        FROM sys.sql_expression_dependencies d
        INNER JOIN sys.procedures p ON d.referencing_id = p.object_id
        LEFT JOIN sys.objects o ON d.referenced_id = o.object_id
        WHERE d.referenced_entity_name IS NOT NULL
    ''')
    logger.info(f"Found {len(sql_deps)} SQL dependencies")

    db.disconnect()

    # Build dependency maps
    sp_calls_sp = defaultdict(set)  # SP -> SPs it calls
    sp_accesses_table = defaultdict(set)  # SP -> tables it accesses
    sp_accesses_view = defaultdict(set)  # SP -> views it accesses

    sp_names = {f"{p[0]}.{p[1]}" for p in procedures}
    sp_names.update({p[1] for p in procedures})

    # Process SQL Server dependencies
    for dep in sql_deps:
        caller = f"{dep[0]}.{dep[1]}"
        ref = f"{dep[2]}.{dep[3]}"
        ref_short = dep[3]

        if dep[4] == 'SQL_STORED_PROCEDURE':
            sp_calls_sp[caller].add(ref_short)
        elif dep[4] in ('USER_TABLE', 'SYSTEM_TABLE'):
            sp_accesses_table[caller].add(ref_short)
        elif dep[4] == 'VIEW':
            sp_accesses_view[caller].add(ref_short)

    # Also analyze definitions for EXEC calls (catches dynamic calls)
    exec_pattern = re.compile(r'\bEXEC(?:UTE)?\s+(?:\[?(\w+)\]?\.)?\[?(\w+)\]?', re.IGNORECASE)

    for schema, proc, definition in procedures:
        if definition:
            caller = f"{schema}.{proc}"
            matches = exec_pattern.findall(definition)
            for match_schema, match_proc in matches:
                if match_proc in sp_names or f"dbo.{match_proc}" in sp_names:
                    sp_calls_sp[caller].add(match_proc)

    # Find procedures that are called by others
    called_procs = set()
    for calls in sp_calls_sp.values():
        called_procs.update(calls)

    # Find root procedures (call others but aren't called)
    all_callers = set(sp_calls_sp.keys())
    root_procs = {p.split('.')[-1] for p in all_callers} - called_procs

    # Find leaf procedures (don't call others)
    leaf_procs = {p[1] for p in procedures if f"{p[0]}.{p[1]}" not in sp_calls_sp}

    # Find most connected tables (accessed by many SPs)
    table_access_count = defaultdict(int)
    for tables in sp_accesses_table.values():
        for t in tables:
            table_access_count[t] += 1

    # Generate documentation
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_SP_DEPENDENCIES.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Stored Procedure Dependencies\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('---\n\n')

        # Summary statistics
        f.write('## Summary\n\n')
        f.write('| Metric | Count |\n')
        f.write('|--------|-------|\n')
        f.write(f'| Total Stored Procedures | {len(procedures)} |\n')
        f.write(f'| SPs that call other SPs | {len(sp_calls_sp)} |\n')
        f.write(f'| Root SPs (callers, not called) | {len(root_procs)} |\n')
        f.write(f'| Leaf SPs (don\'t call others) | {len(leaf_procs)} |\n')
        f.write(f'| Unique table accesses | {len(table_access_count)} |\n')
        f.write('\n---\n\n')

        # Most accessed tables
        f.write('## Most Accessed Tables\n\n')
        f.write('Tables accessed by the most stored procedures:\n\n')
        f.write('| Table | SPs Accessing |\n')
        f.write('|-------|---------------|\n')
        top_tables = sorted(table_access_count.items(), key=lambda x: x[1], reverse=True)[:25]
        for table, count in top_tables:
            f.write(f'| {table} | {count} |\n')
        f.write('\n---\n\n')

        # SP Call Chain Diagram (top callers)
        f.write('## Stored Procedure Call Chains\n\n')
        f.write('Procedures that call other procedures:\n\n')
        f.write('```mermaid\nflowchart LR\n')

        # Group by cluster (connected components)
        added_nodes = set()
        edge_count = 0
        max_edges = 100  # Limit for readability

        # Sort by number of calls (most connected first)
        sorted_callers = sorted(sp_calls_sp.items(), key=lambda x: len(x[1]), reverse=True)

        for caller, callees in sorted_callers[:30]:
            caller_short = caller.split('.')[-1]
            for callee in list(callees)[:5]:  # Limit callees per caller
                if edge_count < max_edges:
                    # Sanitize names for Mermaid
                    c1 = caller_short.replace(' ', '_').replace('-', '_')
                    c2 = callee.replace(' ', '_').replace('-', '_')
                    f.write(f'    {c1}["{caller_short}"] --> {c2}["{callee}"]\n')
                    added_nodes.add(c1)
                    added_nodes.add(c2)
                    edge_count += 1

        f.write('```\n\n')

        if len(sp_calls_sp) > 30:
            f.write(f'*Showing top 30 of {len(sp_calls_sp)} calling procedures*\n\n')

        f.write('---\n\n')

        # Table Access Diagram (core tables)
        f.write('## Core Table Access Patterns\n\n')
        f.write('Which procedures access the most critical tables:\n\n')
        f.write('```mermaid\nflowchart TD\n')

        # Style definitions
        f.write('    classDef tableStyle fill:#e1f5fe,stroke:#01579b\n')
        f.write('    classDef spStyle fill:#fff3e0,stroke:#e65100\n\n')

        # Show top 10 tables and their top accessors
        for table, count in top_tables[:10]:
            t_id = table.replace(' ', '_').replace('-', '_')
            f.write(f'    {t_id}[("{table}")]\n')
            f.write(f'    class {t_id} tableStyle\n')

            # Find SPs that access this table
            accessors = []
            for sp, tables in sp_accesses_table.items():
                if table in tables:
                    accessors.append(sp.split('.')[-1])

            for accessor in accessors[:3]:  # Top 3 accessors
                a_id = accessor.replace(' ', '_').replace('-', '_')
                f.write(f'    {a_id}["{accessor}"] --> {t_id}\n')
                f.write(f'    class {a_id} spStyle\n')

        f.write('```\n\n')
        f.write('---\n\n')

        # Detailed dependency list
        f.write('## Detailed Dependencies\n\n')

        # Group SPs by the number of dependencies
        f.write('### SPs with Most Dependencies\n\n')

        sp_dep_count = []
        for schema, proc, _ in procedures:
            key = f"{schema}.{proc}"
            dep_count = len(sp_calls_sp.get(key, set())) + \
                       len(sp_accesses_table.get(key, set())) + \
                       len(sp_accesses_view.get(key, set()))
            if dep_count > 0:
                sp_dep_count.append((proc, dep_count,
                                    len(sp_calls_sp.get(key, set())),
                                    len(sp_accesses_table.get(key, set())),
                                    len(sp_accesses_view.get(key, set()))))

        sp_dep_count.sort(key=lambda x: x[1], reverse=True)

        f.write('| Procedure | Total Deps | SP Calls | Tables | Views |\n')
        f.write('|-----------|------------|----------|--------|-------|\n')
        for proc, total, sp_count, tbl_count, view_count in sp_dep_count[:50]:
            f.write(f'| {proc} | {total} | {sp_count} | {tbl_count} | {view_count} |\n')
        f.write('\n---\n\n')

        # Root procedures (entry points)
        f.write('### Root Procedures (Entry Points)\n\n')
        f.write('These procedures call others but are not called by any procedure:\n\n')
        for proc in sorted(list(root_procs)[:50]):
            f.write(f'- `{proc}`\n')
        if len(root_procs) > 50:
            f.write(f'\n*...and {len(root_procs) - 50} more*\n')
        f.write('\n---\n\n')

        # Domain-specific diagrams
        f.write('## Domain-Specific Dependency Diagrams\n\n')

        # Bid-related SPs
        bid_sps = [(s, p) for s, p, _ in procedures if 'Bid' in p]
        if bid_sps:
            f.write('### Bidding System Procedures\n\n')
            f.write('```mermaid\nflowchart TD\n')
            f.write('    classDef bidSP fill:#c8e6c9,stroke:#2e7d32\n\n')

            bid_edges = 0
            for schema, proc in bid_sps[:20]:
                key = f"{schema}.{proc}"
                p_id = proc.replace(' ', '_').replace('-', '_')
                f.write(f'    {p_id}["{proc}"]\n')
                f.write(f'    class {p_id} bidSP\n')

                for callee in list(sp_calls_sp.get(key, set()))[:3]:
                    if bid_edges < 40:
                        c_id = callee.replace(' ', '_').replace('-', '_')
                        f.write(f'    {p_id} --> {c_id}\n')
                        bid_edges += 1

            f.write('```\n\n')

        # Report-related SPs
        rpt_sps = [(s, p) for s, p, _ in procedures if 'Rpt' in p or 'Report' in p]
        if rpt_sps:
            f.write('### Reporting Procedures\n\n')
            f.write('```mermaid\nflowchart TD\n')
            f.write('    classDef rptSP fill:#ffecb3,stroke:#ff8f00\n\n')

            rpt_edges = 0
            for schema, proc in rpt_sps[:15]:
                key = f"{schema}.{proc}"
                p_id = proc.replace(' ', '_').replace('-', '_')
                f.write(f'    {p_id}["{proc}"]\n')
                f.write(f'    class {p_id} rptSP\n')

                for callee in list(sp_calls_sp.get(key, set()))[:3]:
                    if rpt_edges < 30:
                        c_id = callee.replace(' ', '_').replace('-', '_')
                        f.write(f'    {p_id} --> {c_id}\n')
                        rpt_edges += 1

            f.write('```\n\n')

    logger.info(f"[OK] SP dependencies saved to {output_file}")
    print(f"\nSP dependency diagrams saved to: {output_file}")
    print(f"  Total procedures: {len(procedures)}")
    print(f"  Procedures with SP calls: {len(sp_calls_sp)}")
    print(f"  Root procedures: {len(root_procs)}")
    print(f"  Tables accessed: {len(table_access_count)}")

    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate SP dependency diagrams')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')

    args = parser.parse_args()

    try:
        generate_sp_dependencies(database=args.database, output_dir=args.output)
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
