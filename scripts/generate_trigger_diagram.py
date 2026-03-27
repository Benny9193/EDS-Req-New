#!/usr/bin/env python3
"""
Generate Trigger Dependency Diagram

Creates documentation and diagrams showing database triggers,
which tables they're attached to, and what actions they perform.
"""

import os
import sys
import re
from datetime import datetime
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


def generate_trigger_diagram(database='EDS', output_dir='docs'):
    """Generate trigger dependency documentation and diagrams."""

    logger = setup_logging('generate_trigger_diagram')
    logger.info(f"Analyzing triggers for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all triggers with details
    triggers = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TriggerName,
            OBJECT_NAME(t.parent_id) AS ParentTable,
            t.is_instead_of_trigger,
            t.is_disabled,
            t.create_date,
            t.modify_date,
            OBJECT_DEFINITION(t.object_id) AS Definition,
            OBJECTPROPERTY(t.object_id, 'ExecIsInsertTrigger') AS IsInsert,
            OBJECTPROPERTY(t.object_id, 'ExecIsUpdateTrigger') AS IsUpdate,
            OBJECTPROPERTY(t.object_id, 'ExecIsDeleteTrigger') AS IsDelete
        FROM sys.triggers t
        INNER JOIN sys.tables tbl ON t.parent_id = tbl.object_id
        INNER JOIN sys.schemas s ON tbl.schema_id = s.schema_id
        WHERE t.parent_class = 1  -- Object triggers only
        ORDER BY s.name, OBJECT_NAME(t.parent_id), t.name
    ''')
    logger.info(f"Found {len(triggers)} triggers")

    # Get trigger dependencies (what tables/SPs they reference)
    trigger_deps = db.execute_query('''
        SELECT DISTINCT
            OBJECT_NAME(d.referencing_id) AS TriggerName,
            d.referenced_entity_name AS RefName,
            o.type_desc AS RefType
        FROM sys.sql_expression_dependencies d
        INNER JOIN sys.triggers t ON d.referencing_id = t.object_id
        LEFT JOIN sys.objects o ON d.referenced_id = o.object_id
        WHERE d.referenced_entity_name IS NOT NULL
    ''')

    db.disconnect()

    # Build trigger info
    trigger_info = []
    for trig in triggers:
        events = []
        if trig[8]:
            events.append('INSERT')
        if trig[9]:
            events.append('UPDATE')
        if trig[10]:
            events.append('DELETE')

        trigger_info.append({
            'schema': trig[0],
            'name': trig[1],
            'table': trig[2],
            'instead_of': trig[3],
            'disabled': trig[4],
            'created': trig[5],
            'modified': trig[6],
            'definition': trig[7],
            'events': events
        })

    # Build dependency map
    trigger_refs = defaultdict(lambda: {'tables': set(), 'procedures': set(), 'other': set()})
    for trig_name, ref_name, ref_type in trigger_deps:
        if ref_type == 'USER_TABLE':
            trigger_refs[trig_name]['tables'].add(ref_name)
        elif ref_type == 'SQL_STORED_PROCEDURE':
            trigger_refs[trig_name]['procedures'].add(ref_name)
        else:
            trigger_refs[trig_name]['other'].add(ref_name)

    # Group triggers by table
    triggers_by_table = defaultdict(list)
    for trig in trigger_info:
        triggers_by_table[trig['table']].append(trig)

    # Analyze trigger patterns from definitions
    for trig in trigger_info:
        if trig['definition']:
            # Check for RAISERROR (validation triggers)
            if 'RAISERROR' in trig['definition'].upper():
                trig['pattern'] = 'Validation'
            # Check for INSERT INTO (audit/logging triggers)
            elif re.search(r'INSERT\s+INTO\s+\w*log|audit|history', trig['definition'], re.IGNORECASE):
                trig['pattern'] = 'Audit/Logging'
            # Check for UPDATE statements
            elif 'UPDATE ' in trig['definition'].upper() and 'INSERTED' in trig['definition'].upper():
                trig['pattern'] = 'Cascade Update'
            else:
                trig['pattern'] = 'Other'
        else:
            trig['pattern'] = 'Unknown'

    # Generate documentation
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_TRIGGERS.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Trigger Documentation\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Summary\n\n')
        f.write('| Metric | Count |\n')
        f.write('|--------|-------|\n')
        f.write(f'| Total Triggers | {len(triggers)} |\n')
        f.write(f'| Tables with Triggers | {len(triggers_by_table)} |\n')
        f.write(f'| Disabled Triggers | {sum(1 for t in trigger_info if t["disabled"])} |\n')
        f.write(f'| INSTEAD OF Triggers | {sum(1 for t in trigger_info if t["instead_of"])} |\n')
        f.write(f'| AFTER Triggers | {sum(1 for t in trigger_info if not t["instead_of"])} |\n')
        f.write('\n')

        # Event breakdown
        insert_count = sum(1 for t in trigger_info if 'INSERT' in t['events'])
        update_count = sum(1 for t in trigger_info if 'UPDATE' in t['events'])
        delete_count = sum(1 for t in trigger_info if 'DELETE' in t['events'])

        f.write('### Event Types\n\n')
        f.write(f'- INSERT triggers: {insert_count}\n')
        f.write(f'- UPDATE triggers: {update_count}\n')
        f.write(f'- DELETE triggers: {delete_count}\n')
        f.write('\n---\n\n')

        # Main diagram
        f.write('## Trigger Dependency Diagram\n\n')
        f.write('```mermaid\nflowchart TD\n')
        f.write('    classDef tableStyle fill:#e3f2fd,stroke:#1565c0\n')
        f.write('    classDef triggerStyle fill:#fff3e0,stroke:#ef6c00\n')
        f.write('    classDef disabledStyle fill:#f5f5f5,stroke:#9e9e9e,stroke-dasharray: 5 5\n')
        f.write('    classDef spStyle fill:#e8f5e9,stroke:#2e7d32\n\n')

        # Show tables with their triggers
        shown_tables = set()
        for table, trigs in sorted(triggers_by_table.items())[:20]:
            t_id = table.replace(' ', '_').replace('-', '_')
            f.write(f'    {t_id}["{table}"]\n')
            f.write(f'    class {t_id} tableStyle\n')
            shown_tables.add(table)

            for trig in trigs:
                trig_id = trig['name'].replace(' ', '_').replace('-', '_')
                events = '/'.join(trig['events'])
                label = f"{trig['name']}\\n({events})"
                f.write(f'    {trig_id}["{label}"]\n')

                if trig['disabled']:
                    f.write(f'    class {trig_id} disabledStyle\n')
                else:
                    f.write(f'    class {trig_id} triggerStyle\n')

                # Connect table to trigger
                f.write(f'    {t_id} --> {trig_id}\n')

                # Show SP calls from this trigger
                refs = trigger_refs.get(trig['name'], {})
                for sp in list(refs.get('procedures', []))[:2]:
                    sp_id = sp.replace(' ', '_').replace('-', '_')
                    f.write(f'    {trig_id} -.-> {sp_id}["{sp}"]\n')
                    f.write(f'    class {sp_id} spStyle\n')

        f.write('```\n\n')

        if len(triggers_by_table) > 20:
            f.write(f'*Showing 20 of {len(triggers_by_table)} tables with triggers*\n\n')

        f.write('---\n\n')

        # Detailed trigger list by table
        f.write('## Triggers by Table\n\n')

        for table in sorted(triggers_by_table.keys()):
            trigs = triggers_by_table[table]
            f.write(f'### {table}\n\n')

            for trig in trigs:
                status = ' *(DISABLED)*' if trig['disabled'] else ''
                timing = 'INSTEAD OF' if trig['instead_of'] else 'AFTER'
                events = ', '.join(trig['events'])

                f.write(f'**{trig["name"]}**{status}\n')
                f.write(f'- Type: {timing} {events}\n')
                f.write(f'- Pattern: {trig["pattern"]}\n')
                f.write(f'- Modified: {trig["modified"]}\n')

                refs = trigger_refs.get(trig['name'], {'tables': set(), 'procedures': set(), 'other': set()})
                if refs.get('tables'):
                    other_tables = refs['tables'] - {table}
                    if other_tables:
                        f.write(f'- References tables: {", ".join(sorted(other_tables))}\n')
                if refs.get('procedures'):
                    f.write(f'- Calls procedures: {", ".join(sorted(refs["procedures"]))}\n')

                f.write('\n')

        f.write('---\n\n')

        # Disabled triggers
        disabled = [t for t in trigger_info if t['disabled']]
        if disabled:
            f.write('## Disabled Triggers\n\n')
            f.write('These triggers are currently disabled and not executing:\n\n')
            f.write('| Trigger | Table | Events | Last Modified |\n')
            f.write('|---------|-------|--------|---------------|\n')
            for trig in disabled:
                events = ', '.join(trig['events'])
                f.write(f'| {trig["name"]} | {trig["table"]} | {events} | {trig["modified"]} |\n')
            f.write('\n**Consider:** Remove disabled triggers if no longer needed.\n\n')
            f.write('---\n\n')

        # Pattern analysis
        f.write('## Trigger Patterns\n\n')
        patterns = defaultdict(list)
        for trig in trigger_info:
            patterns[trig['pattern']].append(trig)

        for pattern, trigs in sorted(patterns.items()):
            f.write(f'### {pattern} ({len(trigs)})\n\n')
            for trig in trigs[:10]:
                f.write(f'- `{trig["name"]}` on `{trig["table"]}`\n')
            if len(trigs) > 10:
                f.write(f'- *...and {len(trigs) - 10} more*\n')
            f.write('\n')

    logger.info(f"[OK] Trigger documentation saved to {output_file}")
    print(f"\nTrigger documentation saved to: {output_file}")
    print(f"  Total triggers: {len(triggers)}")
    print(f"  Tables with triggers: {len(triggers_by_table)}")
    print(f"  Disabled triggers: {sum(1 for t in trigger_info if t['disabled'])}")

    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate trigger documentation')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')

    args = parser.parse_args()

    try:
        generate_trigger_diagram(database=args.database, output_dir=args.output)
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
