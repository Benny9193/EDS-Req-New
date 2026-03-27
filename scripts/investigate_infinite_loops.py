#!/usr/bin/env python3
"""
Investigate Potential Infinite Loops

Analyzes stored procedures for dangerous patterns that could
cause infinite loops, and generates a report with findings.
"""

import os
import sys
import re
from datetime import datetime

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


DANGEROUS_PATTERNS = [
    {
        'name': 'Infinite WHILE loop',
        'pattern': r'WHILE\s+1\s*=\s*1',
        'severity': 'HIGH',
        'description': 'WHILE 1=1 loop without visible BREAK condition',
        'recommendation': 'Add explicit BREAK condition or refactor to bounded loop'
    },
    {
        'name': 'WHILE TRUE loop',
        'pattern': r'WHILE\s+TRUE',
        'severity': 'HIGH',
        'description': 'WHILE TRUE loop without visible BREAK condition',
        'recommendation': 'Add explicit BREAK condition or use bounded iteration'
    },
    {
        'name': 'Unconditional recursive call',
        'pattern': r'EXEC\s+(?:dbo\.)?\w+\s*(?:;|\s*$)',
        'severity': 'MEDIUM',
        'description': 'Recursive call that may not have termination',
        'recommendation': 'Ensure recursion has depth limit or base case'
    },
    {
        'name': 'Missing BREAK in WHILE',
        'pattern': r'WHILE\s+[^B]+(?:BEGIN.*?END)',
        'severity': 'LOW',
        'description': 'WHILE loop may be missing BREAK statement',
        'recommendation': 'Review loop logic for proper exit conditions'
    },
]


def investigate_infinite_loops(database='EDS', output_dir='docs'):
    """Investigate potential infinite loop patterns."""

    logger = setup_logging('investigate_infinite_loops')
    logger.info(f"Investigating infinite loops in {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all stored procedures
    procedures = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            OBJECT_DEFINITION(p.object_id) AS Definition,
            p.modify_date
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        ORDER BY s.name, p.name
    ''')
    logger.info(f"Analyzing {len(procedures)} stored procedures")

    db.disconnect()

    # Analyze each procedure
    findings = []
    for schema, proc, definition, modified in procedures:
        if not definition:
            continue

        proc_findings = []
        for pattern_info in DANGEROUS_PATTERNS:
            if re.search(pattern_info['pattern'], definition, re.IGNORECASE | re.DOTALL):
                # Check if there's a BREAK nearby for WHILE loops
                if 'WHILE' in pattern_info['name']:
                    # Look for BREAK statement after the WHILE
                    while_match = re.search(pattern_info['pattern'], definition, re.IGNORECASE)
                    if while_match:
                        after_while = definition[while_match.end():while_match.end() + 500]
                        if 'BREAK' in after_while.upper():
                            continue  # Has a BREAK, skip this finding

                proc_findings.append({
                    'pattern': pattern_info['name'],
                    'severity': pattern_info['severity'],
                    'description': pattern_info['description'],
                    'recommendation': pattern_info['recommendation']
                })

        if proc_findings:
            findings.append({
                'schema': schema,
                'name': proc,
                'modified': modified,
                'findings': proc_findings,
                'definition_snippet': definition[:500] if definition else ''
            })

    logger.info(f"Found {len(findings)} procedures with potential issues")

    # Generate report
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_INFINITE_LOOP_ANALYSIS.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Infinite Loop Analysis\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('This report identifies stored procedures with patterns that could cause infinite loops.\n\n')
        f.write('---\n\n')

        # Summary
        high_count = sum(1 for p in findings for f in p['findings'] if f['severity'] == 'HIGH')
        medium_count = sum(1 for p in findings for f in p['findings'] if f['severity'] == 'MEDIUM')
        low_count = sum(1 for p in findings for f in p['findings'] if f['severity'] == 'LOW')

        f.write('## Summary\n\n')
        f.write(f'**Total Procedures Analyzed:** {len(procedures)}\n')
        f.write(f'**Procedures with Issues:** {len(findings)}\n\n')
        f.write('| Severity | Count |\n')
        f.write('|----------|-------|\n')
        f.write(f'| HIGH | {high_count} |\n')
        f.write(f'| MEDIUM | {medium_count} |\n')
        f.write(f'| LOW | {low_count} |\n')
        f.write('\n---\n\n')

        # HIGH severity findings
        if high_count > 0:
            f.write('## HIGH Severity Issues\n\n')
            f.write('**These require immediate attention:**\n\n')

            for proc in findings:
                high_findings = [x for x in proc['findings'] if x['severity'] == 'HIGH']
                if high_findings:
                    f.write(f'### {proc["schema"]}.{proc["name"]}\n\n')
                    f.write(f'*Last modified: {proc["modified"]}*\n\n')

                    for finding in high_findings:
                        f.write(f'**Issue:** {finding["pattern"]}\n')
                        f.write(f'- {finding["description"]}\n')
                        f.write(f'- **Recommendation:** {finding["recommendation"]}\n\n')

                    # Show code snippet
                    f.write('**Code snippet:**\n')
                    f.write('```sql\n')
                    # Find the WHILE loop in the definition
                    snippet = proc['definition_snippet']
                    while_match = re.search(r'WHILE\s+1\s*=\s*1.*?(?:END|$)',
                                           snippet, re.IGNORECASE | re.DOTALL)
                    if while_match:
                        f.write(while_match.group(0)[:300])
                    else:
                        f.write(snippet[:300])
                    f.write('\n```\n\n')

            f.write('---\n\n')

        # MEDIUM severity findings
        if medium_count > 0:
            f.write('## MEDIUM Severity Issues\n\n')
            f.write('**Review these for potential problems:**\n\n')
            f.write('| Procedure | Issue | Recommendation |\n')
            f.write('|-----------|-------|----------------|\n')

            for proc in findings:
                medium_findings = [x for x in proc['findings'] if x['severity'] == 'MEDIUM']
                for finding in medium_findings:
                    f.write(f'| {proc["name"]} | {finding["pattern"]} | {finding["recommendation"]} |\n')

            f.write('\n---\n\n')

        # LOW severity findings
        if low_count > 0:
            f.write('## LOW Severity Issues\n\n')
            f.write('**Informational - may be false positives:**\n\n')

            for proc in findings:
                low_findings = [x for x in proc['findings'] if x['severity'] == 'LOW']
                for finding in low_findings:
                    f.write(f'- `{proc["name"]}`: {finding["pattern"]}\n')

            f.write('\n---\n\n')

        # Best practices
        f.write('## Best Practices to Prevent Infinite Loops\n\n')
        f.write('1. **Always include explicit exit conditions:**\n')
        f.write('   ```sql\n')
        f.write('   WHILE @counter < @maxIterations\n')
        f.write('   BEGIN\n')
        f.write('       -- Process\n')
        f.write('       SET @counter = @counter + 1\n')
        f.write('   END\n')
        f.write('   ```\n\n')
        f.write('2. **Use BREAK with WHILE 1=1:**\n')
        f.write('   ```sql\n')
        f.write('   WHILE 1=1\n')
        f.write('   BEGIN\n')
        f.write('       -- Process\n')
        f.write('       IF @condition BREAK  -- Explicit exit\n')
        f.write('   END\n')
        f.write('   ```\n\n')
        f.write('3. **Add depth parameter to recursive calls:**\n')
        f.write('   ```sql\n')
        f.write('   CREATE PROCEDURE sp_Recursive @id INT, @depth INT = 0\n')
        f.write('   AS BEGIN\n')
        f.write('       IF @depth > 100 RETURN  -- Max depth\n')
        f.write('       EXEC sp_Recursive @next_id, @depth + 1\n')
        f.write('   END\n')
        f.write('   ```\n\n')
        f.write('4. **Use TRY/CATCH with timeout:**\n')
        f.write('   ```sql\n')
        f.write('   SET LOCK_TIMEOUT 30000  -- 30 second timeout\n')
        f.write('   ```\n')

    logger.info(f"[OK] Report saved to {output_file}")
    print(f"\nInfinite loop analysis saved to: {output_file}")
    print(f"  Procedures analyzed: {len(procedures)}")
    print(f"  Issues found: HIGH={high_count}, MEDIUM={medium_count}, LOW={low_count}")

    return output_file, findings


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Investigate infinite loops')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')
    parser.add_argument('--output', '-o', default='docs', help='Output directory')

    args = parser.parse_args()

    try:
        investigate_infinite_loops(database=args.database, output_dir=args.output)
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
