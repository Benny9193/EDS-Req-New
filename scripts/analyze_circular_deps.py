#!/usr/bin/env python3
"""
Analyze Circular Dependencies

Identifies stored procedures with circular/recursive dependencies
and potential issues in call chains.
"""

import os
import sys
import re
from datetime import datetime
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def find_cycles(graph, start, visited=None, path=None):
    """Find cycles in a directed graph using DFS."""
    if visited is None:
        visited = set()
    if path is None:
        path = []

    cycles = []
    visited.add(start)
    path.append(start)

    for neighbor in graph.get(start, []):
        if neighbor in path:
            # Found a cycle
            cycle_start = path.index(neighbor)
            cycles.append(path[cycle_start:] + [neighbor])
        elif neighbor not in visited:
            cycles.extend(find_cycles(graph, neighbor, visited, path))

    path.pop()
    return cycles


def analyze_circular_deps(database='EDS', output_dir='docs'):
    """Analyze circular dependencies in stored procedures."""

    logger = setup_logging('analyze_circular_deps')
    logger.info(f"Analyzing circular dependencies for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all stored procedures
    procedures = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            OBJECT_DEFINITION(p.object_id) AS Definition
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
    ''')
    logger.info(f"Found {len(procedures)} stored procedures")

    # Get SQL dependencies
    sql_deps = db.execute_query('''
        SELECT DISTINCT
            OBJECT_NAME(d.referencing_id) AS CallerName,
            d.referenced_entity_name AS RefName
        FROM sys.sql_expression_dependencies d
        INNER JOIN sys.procedures p ON d.referencing_id = p.object_id
        INNER JOIN sys.procedures p2 ON d.referenced_id = p2.object_id
    ''')

    db.disconnect()

    # Build call graph
    call_graph = defaultdict(set)
    sp_names = {p[1] for p in procedures}

    for caller, callee in sql_deps:
        if callee in sp_names:
            call_graph[caller].add(callee)

    # Also check EXEC patterns for dynamic calls
    exec_pattern = re.compile(r'\bEXEC(?:UTE)?\s+(?:\[?(\w+)\]?\.)?\[?(\w+)\]?', re.IGNORECASE)

    for schema, proc, definition in procedures:
        if definition:
            matches = exec_pattern.findall(definition)
            for _, match_proc in matches:
                if match_proc in sp_names:
                    call_graph[proc].add(match_proc)

    # Find self-referential procedures
    self_calls = []
    for proc in sp_names:
        if proc in call_graph.get(proc, set()):
            self_calls.append(proc)

    logger.info(f"Found {len(self_calls)} self-calling procedures")

    # Find all cycles
    all_cycles = []
    visited_global = set()

    for proc in call_graph.keys():
        if proc not in visited_global:
            cycles = find_cycles(dict(call_graph), proc)
            for cycle in cycles:
                # Normalize cycle (start with smallest name)
                min_idx = cycle.index(min(cycle[:-1]))
                normalized = cycle[min_idx:-1] + cycle[:min_idx] + [cycle[min_idx]]
                if normalized not in all_cycles:
                    all_cycles.append(normalized)
            visited_global.add(proc)

    # Remove duplicates and self-calls from cycles
    unique_cycles = []
    seen = set()
    for cycle in all_cycles:
        if len(cycle) > 2:  # More than just A -> A
            key = tuple(sorted(cycle[:-1]))
            if key not in seen:
                unique_cycles.append(cycle)
                seen.add(key)

    logger.info(f"Found {len(unique_cycles)} unique cycles")

    # Analyze call depths
    def get_max_depth(proc, visited=None, depth=0):
        if visited is None:
            visited = set()
        if proc in visited or depth > 20:
            return depth
        visited.add(proc)
        max_d = depth
        for callee in call_graph.get(proc, []):
            max_d = max(max_d, get_max_depth(callee, visited.copy(), depth + 1))
        return max_d

    proc_depths = []
    for proc in call_graph.keys():
        depth = get_max_depth(proc)
        if depth > 1:
            proc_depths.append((proc, depth))

    proc_depths.sort(key=lambda x: x[1], reverse=True)

    # Generate documentation
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_CIRCULAR_DEPS.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Circular Dependency Analysis\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Summary\n\n')
        f.write('| Metric | Count |\n')
        f.write('|--------|-------|\n')
        f.write(f'| Total Procedures | {len(procedures)} |\n')
        f.write(f'| Procedures with calls | {len(call_graph)} |\n')
        f.write(f'| Self-calling procedures | {len(self_calls)} |\n')
        f.write(f'| Circular dependency chains | {len(unique_cycles)} |\n')
        f.write(f'| Max call depth | {proc_depths[0][1] if proc_depths else 0} |\n')
        f.write('\n---\n\n')

        # Self-calling procedures
        f.write('## Self-Calling Procedures (Recursive)\n\n')
        if self_calls:
            f.write('These procedures call themselves, which may be intentional recursion:\n\n')
            for proc in sorted(self_calls):
                f.write(f'- `{proc}`\n')
            f.write('\n**Note:** Self-recursion can be intentional (tree traversal, hierarchical data) ')
            f.write('or a bug. Review each case.\n\n')
        else:
            f.write('*No self-calling procedures found.*\n\n')
        f.write('---\n\n')

        # Circular chains
        f.write('## Circular Dependency Chains\n\n')
        if unique_cycles:
            f.write('These procedures form circular call chains:\n\n')
            for i, cycle in enumerate(unique_cycles[:20], 1):
                chain = ' → '.join(cycle)
                f.write(f'{i}. `{chain}`\n')
            if len(unique_cycles) > 20:
                f.write(f'\n*...and {len(unique_cycles) - 20} more cycles*\n')
            f.write('\n**Warning:** Circular dependencies can cause infinite loops if not ')
            f.write('properly guarded with termination conditions.\n\n')

            # Diagram for top cycles
            f.write('### Circular Dependency Diagram\n\n')
            f.write('```mermaid\nflowchart LR\n')
            f.write('    classDef cycleNode fill:#ffcdd2,stroke:#c62828\n\n')

            added = set()
            for cycle in unique_cycles[:10]:
                for i in range(len(cycle) - 1):
                    edge = (cycle[i], cycle[i+1])
                    if edge not in added:
                        p1 = cycle[i].replace(' ', '_')
                        p2 = cycle[i+1].replace(' ', '_')
                        f.write(f'    {p1}["{cycle[i]}"] --> {p2}["{cycle[i+1]}"]\n')
                        f.write(f'    class {p1} cycleNode\n')
                        f.write(f'    class {p2} cycleNode\n')
                        added.add(edge)

            f.write('```\n\n')
        else:
            f.write('*No circular dependency chains found (good!)*\n\n')
        f.write('---\n\n')

        # Deep call chains
        f.write('## Deepest Call Chains\n\n')
        f.write('Procedures with the deepest call hierarchies:\n\n')
        f.write('| Procedure | Max Depth |\n')
        f.write('|-----------|----------|\n')
        for proc, depth in proc_depths[:25]:
            f.write(f'| {proc} | {depth} |\n')
        f.write('\n**Note:** Deep call chains (>5 levels) may indicate complex business logic ')
        f.write('that could benefit from refactoring.\n\n')
        f.write('---\n\n')

        # Recommendations
        f.write('## Recommendations\n\n')

        if self_calls:
            f.write('### Self-Calling Procedures\n')
            f.write('1. Verify each self-calling procedure has proper termination conditions\n')
            f.write('2. Check for maximum recursion depth limits (SQL Server default: 32)\n')
            f.write('3. Consider using CTEs for recursive operations instead\n\n')

        if unique_cycles:
            f.write('### Circular Dependencies\n')
            f.write('1. Review each cycle to ensure it\'s intentional\n')
            f.write('2. Add guards to prevent infinite loops\n')
            f.write('3. Consider breaking cycles by extracting common logic\n\n')

        if proc_depths and proc_depths[0][1] > 5:
            f.write('### Deep Call Chains\n')
            f.write('1. Consider flattening deeply nested call chains\n')
            f.write('2. Extract common operations to reduce nesting\n')
            f.write('3. Document the business logic that requires deep nesting\n\n')

    logger.info(f"[OK] Circular dependency analysis saved to {output_file}")
    print(f"\nCircular dependency analysis saved to: {output_file}")
    print(f"  Self-calling procedures: {len(self_calls)}")
    print(f"  Circular chains: {len(unique_cycles)}")
    print(f"  Max call depth: {proc_depths[0][1] if proc_depths else 0}")

    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Analyze circular dependencies')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')

    args = parser.parse_args()

    try:
        analyze_circular_deps(database=args.database, output_dir=args.output)
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
