#!/usr/bin/env python3
"""
Document Recursive Procedures

Analyzes self-calling (recursive) stored procedures and adds
documentation explaining their purpose and recursion patterns.
"""

import os
import sys
import re
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


# Patterns to identify recursion purpose
RECURSION_PATTERNS = {
    'tree_traversal': {
        'patterns': [r'parent', r'child', r'tree', r'hierarchy', r'level', r'depth'],
        'description': 'Traverses hierarchical/tree data structure'
    },
    'approval_chain': {
        'patterns': [r'approv', r'workflow', r'chain', r'next', r'step'],
        'description': 'Processes approval workflow chain'
    },
    'org_hierarchy': {
        'patterns': [r'district', r'school', r'user.*tree', r'org'],
        'description': 'Navigates organizational hierarchy'
    },
    'bill_of_materials': {
        'patterns': [r'component', r'assembly', r'bom', r'part'],
        'description': 'Processes bill of materials/component hierarchy'
    },
    'category_tree': {
        'patterns': [r'category', r'subcategory', r'catalog'],
        'description': 'Traverses category/catalog hierarchy'
    },
    'document_chain': {
        'patterns': [r'document', r'sds', r'attachment', r'link'],
        'description': 'Follows document/attachment chain'
    },
    'requisition_chain': {
        'patterns': [r'requisition', r'req', r'order', r'detail'],
        'description': 'Processes requisition/order hierarchy'
    },
    'budget_rollup': {
        'patterns': [r'budget', r'account', r'rollup', r'total'],
        'description': 'Calculates budget rollups through hierarchy'
    },
    'copy_operation': {
        'patterns': [r'copy', r'clone', r'duplicate'],
        'description': 'Recursively copies related records'
    }
}


def analyze_recursive_purpose(proc_name, definition):
    """Analyze procedure definition to determine recursion purpose."""
    if not definition:
        return 'Unknown', 'Definition not available'

    def_lower = definition.lower()

    # Check each pattern category
    matches = []
    for category, info in RECURSION_PATTERNS.items():
        for pattern in info['patterns']:
            if re.search(pattern, def_lower):
                matches.append((category, info['description']))
                break

    if matches:
        # Return the most specific match
        return matches[0]

    # Check for common SQL recursion patterns
    if 'cte' in def_lower or 'with ' in def_lower and 'recursive' in def_lower:
        return 'cte_recursion', 'Uses Common Table Expression for recursion'

    if 'while' in def_lower:
        return 'iterative', 'Uses iterative loop (WHILE) instead of true recursion'

    if 'cursor' in def_lower:
        return 'cursor_based', 'Uses cursor-based iteration'

    return 'general', 'General recursive processing'


def document_recursive_procs(database='EDS', output_dir='docs'):
    """Document recursive stored procedures."""

    logger = setup_logging('document_recursive_procs')
    logger.info(f"Documenting recursive procedures for {database}")

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
            ISNULL(ep.value, '') AS CurrentDesc
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON p.object_id = ep.major_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        ORDER BY s.name, p.name
    ''')

    # Get dependencies
    deps = db.execute_query('''
        SELECT DISTINCT
            OBJECT_NAME(d.referencing_id) AS CallerName,
            d.referenced_entity_name AS RefName
        FROM sys.sql_expression_dependencies d
        INNER JOIN sys.procedures p ON d.referencing_id = p.object_id
        INNER JOIN sys.procedures p2 ON d.referenced_id = p2.object_id
    ''')

    # Build call graph
    sp_names = {p[1] for p in procedures}
    call_graph = {}
    for caller, callee in deps:
        if caller not in call_graph:
            call_graph[caller] = set()
        if callee in sp_names:
            call_graph[caller].add(callee)

    # Also check EXEC patterns
    exec_pattern = re.compile(r'\bEXEC(?:UTE)?\s+(?:\[?(\w+)\]?\.)?\[?(\w+)\]?', re.IGNORECASE)

    proc_defs = {}
    for schema, proc, created, modified, definition, desc in procedures:
        proc_defs[proc] = {
            'schema': schema,
            'created': created,
            'modified': modified,
            'definition': definition,
            'current_desc': desc
        }
        if definition:
            if proc not in call_graph:
                call_graph[proc] = set()
            matches = exec_pattern.findall(definition)
            for _, match_proc in matches:
                if match_proc in sp_names:
                    call_graph[proc].add(match_proc)

    # Find self-calling procedures
    recursive_procs = []
    for proc, callees in call_graph.items():
        if proc in callees:
            info = proc_defs.get(proc, {})
            category, purpose = analyze_recursive_purpose(proc, info.get('definition', ''))
            recursive_procs.append({
                'name': proc,
                'schema': info.get('schema', 'dbo'),
                'created': info.get('created'),
                'modified': info.get('modified'),
                'current_desc': info.get('current_desc', ''),
                'definition': info.get('definition', ''),
                'category': category,
                'purpose': purpose,
                'other_calls': callees - {proc}
            })

    logger.info(f"Found {len(recursive_procs)} recursive procedures")

    # Generate descriptions for procedures without good ones
    descriptions_to_add = []
    for proc in recursive_procs:
        if not proc['current_desc'] or 'recursive' not in proc['current_desc'].lower():
            new_desc = f"(Recursive) {proc['purpose']}"
            descriptions_to_add.append({
                'schema': proc['schema'],
                'name': proc['name'],
                'description': new_desc
            })

    # Add/update descriptions in database
    added = 0
    for item in descriptions_to_add:
        try:
            # Try to add new property
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'PROCEDURE', @level1name = ?
            ''', (item['description'], item['schema'], item['name']))
            added += 1
        except Exception:
            try:
                # Update existing
                db.execute_non_query('''
                    EXEC sp_updateextendedproperty
                        @name = N'MS_Description',
                        @value = ?,
                        @level0type = N'SCHEMA', @level0name = ?,
                        @level1type = N'PROCEDURE', @level1name = ?
                ''', (item['description'], item['schema'], item['name']))
                added += 1
            except Exception:
                pass

    db.disconnect()

    logger.info(f"Updated {added} procedure descriptions")

    # Generate documentation file
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_RECURSIVE_PROCEDURES.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Recursive Procedure Documentation\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('This document explains the purpose of each self-calling (recursive) stored procedure.\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Summary\n\n')
        f.write(f'**Total Recursive Procedures:** {len(recursive_procs)}\n\n')

        # Group by category
        categories = {}
        for proc in recursive_procs:
            cat = proc['category']
            if cat not in categories:
                categories[cat] = []
            categories[cat].append(proc)

        f.write('### By Category\n\n')
        f.write('| Category | Count | Description |\n')
        f.write('|----------|-------|-------------|\n')
        for cat, procs in sorted(categories.items(), key=lambda x: -len(x[1])):
            desc = RECURSION_PATTERNS.get(cat, {}).get('description', cat.replace('_', ' ').title())
            f.write(f'| {cat.replace("_", " ").title()} | {len(procs)} | {desc} |\n')
        f.write('\n---\n\n')

        # Detailed documentation by category
        for cat in ['tree_traversal', 'org_hierarchy', 'approval_chain', 'requisition_chain',
                    'copy_operation', 'budget_rollup', 'document_chain', 'category_tree',
                    'general', 'iterative', 'cursor_based', 'cte_recursion']:
            procs = categories.get(cat, [])
            if not procs:
                continue

            cat_title = cat.replace('_', ' ').title()
            f.write(f'## {cat_title} ({len(procs)} procedures)\n\n')

            desc = RECURSION_PATTERNS.get(cat, {}).get('description', '')
            if desc:
                f.write(f'*{desc}*\n\n')

            for proc in sorted(procs, key=lambda x: x['name']):
                f.write(f'### {proc["name"]}\n\n')

                f.write(f'- **Schema:** {proc["schema"]}\n')
                f.write(f'- **Purpose:** {proc["purpose"]}\n')
                f.write(f'- **Modified:** {proc["modified"]}\n')

                if proc['other_calls']:
                    f.write(f'- **Also calls:** {", ".join(sorted(proc["other_calls"]))}\n')

                # Extract key info from definition
                if proc['definition']:
                    def_text = proc['definition']

                    # Find parameters
                    param_match = re.search(r'CREATE\s+PROC(?:EDURE)?\s+\S+\s*\((.*?)\)\s*AS', def_text, re.IGNORECASE | re.DOTALL)
                    if param_match:
                        params = param_match.group(1).strip()
                        if params:
                            f.write(f'- **Parameters:** `{params[:100]}{"..." if len(params) > 100 else ""}`\n')

                    # Check for termination condition
                    if re.search(r'IF\s+.*RETURN|WHERE\s+.*IS\s+NULL|@@ROWCOUNT\s*=\s*0', def_text, re.IGNORECASE):
                        f.write('- **Termination:** Has explicit termination condition ✓\n')
                    else:
                        f.write('- **Warning:** No obvious termination condition found ⚠️\n')

                    # Check max recursion
                    if 'MAXRECURSION' in def_text.upper():
                        f.write('- **Safety:** Uses MAXRECURSION limit ✓\n')

                f.write('\n')

            f.write('---\n\n')

        # Best practices section
        f.write('## Best Practices for Recursive Procedures\n\n')
        f.write('1. **Always include termination conditions** - Check for NULL, empty result, or max depth\n')
        f.write('2. **Use MAXRECURSION option** for CTEs (default is 100, max is 32767)\n')
        f.write('3. **Avoid deep recursion** - SQL Server has a max stack depth of 32\n')
        f.write('4. **Consider iterative alternatives** - WHILE loops may be more efficient\n')
        f.write('5. **Test with large datasets** - Recursion can cause stack overflow\n')
        f.write('6. **Add comments** explaining the recursion purpose and exit conditions\n')

    logger.info(f"[OK] Documentation saved to {output_file}")
    print(f"\nRecursive procedure documentation saved to: {output_file}")
    print(f"  Total recursive procedures: {len(recursive_procs)}")
    print(f"  Descriptions updated: {added}")
    print(f"  Categories identified: {len(categories)}")

    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Document recursive procedures')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')

    args = parser.parse_args()

    try:
        document_recursive_procs(database=args.database, output_dir=args.output)
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
