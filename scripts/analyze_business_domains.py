#!/usr/bin/env python3
"""
Analyze Business Domains

Organizes database tables into functional business domains
based on naming patterns and relationships.
"""

import os
import sys
from datetime import datetime
from collections import defaultdict

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


# Domain classification rules based on table name patterns
DOMAIN_PATTERNS = {
    'Bidding': ['Bid', 'Award', 'BidHeader', 'BidItem', 'BidResult', 'BidRequest', 'BidImport', 'BidMgr'],
    'Orders & Purchasing': ['PO', 'Order', 'Requisition', 'Detail', 'Batch'],
    'Vendors': ['Vendor', 'Registration', 'Supplier'],
    'Inventory & Items': ['Item', 'Catalog', 'CrossRef', 'Product', 'Price'],
    'Users & Security': ['User', 'Account', 'Approval', 'Session', 'Login', 'Permission'],
    'Reporting': ['Report', 'Dashboard', 'Alert', 'Log', 'Audit', 'Debug'],
    'Documents': ['Document', 'DMS', 'Image', 'File', 'Attachment'],
    'Finance & Budgets': ['Budget', 'Account', 'Billing', 'Invoice', 'Payment'],
    'Configuration': ['Config', 'Setting', 'Parameter', 'Prm', 'Option', 'Threshold'],
    'Communication': ['Email', 'Message', 'Notification', 'Contact'],
}


def classify_table(table_name):
    """Classify a table into a business domain based on name patterns."""
    table_upper = table_name.upper()

    for domain, patterns in DOMAIN_PATTERNS.items():
        for pattern in patterns:
            if pattern.upper() in table_upper:
                return domain

    return 'Other'


def analyze_business_domains(database='EDS', output_dir='docs'):
    """Analyze and document tables by business domain."""

    logger = setup_logging('analyze_business_domains')
    logger.info(f"Analyzing business domains for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all tables with details
    tables = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            ISNULL(p.row_count, 0) AS [Rows],
            t.create_date,
            t.modify_date,
            (SELECT COUNT(*) FROM sys.columns WHERE object_id = t.object_id) AS ColumnCount
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.dm_db_partition_stats p ON t.object_id = p.object_id AND p.index_id < 2
        ORDER BY s.name, t.name
    ''')
    logger.info(f"Found {len(tables)} tables")

    # Get key columns for relationship analysis
    key_columns = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            c.name AS ColumnName,
            CASE
                WHEN pk.column_id IS NOT NULL THEN 'PK'
                WHEN c.name LIKE '%Id' AND c.name != t.name + 'Id' THEN 'FK?'
                ELSE ''
            END AS KeyType
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN (
            SELECT ic.object_id, ic.column_id
            FROM sys.index_columns ic
            INNER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
            WHERE i.is_primary_key = 1
        ) pk ON c.object_id = pk.object_id AND c.column_id = pk.column_id
        WHERE c.name LIKE '%Id' OR pk.column_id IS NOT NULL
        ORDER BY s.name, t.name, c.column_id
    ''')

    db.disconnect()

    # Build key column lookup
    key_lookup = defaultdict(list)
    for col in key_columns:
        key = f'{col[0]}.{col[1]}'
        if col[3]:  # Has a key type
            key_lookup[key].append({'column': col[2], 'type': col[3]})

    # Classify tables into domains
    domains = defaultdict(list)
    for table in tables:
        schema, name, rows, created, modified, col_count = table
        domain = classify_table(name)

        # Only include dbo schema in main analysis
        if schema == 'dbo':
            domains[domain].append({
                'schema': schema,
                'name': name,
                'rows': rows,
                'created': created,
                'modified': modified,
                'columns': col_count,
                'keys': key_lookup.get(f'{schema}.{name}', [])
            })

    # Generate markdown
    logger.info("Generating documentation...")

    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_BUSINESS_DOMAINS.md')

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'# {database} Database - Business Domain Guide\n\n')
        f.write(f'Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n\n')
        f.write('This document organizes database tables by functional business domain ')
        f.write('to help understand the database structure and relationships.\n\n')
        f.write('---\n\n')

        # Summary
        f.write('## Domain Summary\n\n')
        f.write('| Domain | Tables | Total Rows | Description |\n')
        f.write('|--------|--------|------------|-------------|\n')

        domain_descriptions = {
            'Bidding': 'Bid management, awards, and bid request processing',
            'Orders & Purchasing': 'Purchase orders, requisitions, and order details',
            'Vendors': 'Vendor registration, profiles, and management',
            'Inventory & Items': 'Product catalog, items, and pricing',
            'Users & Security': 'User accounts, sessions, and approvals',
            'Reporting': 'Reports, alerts, audit logs, and analytics',
            'Documents': 'Document management and file storage',
            'Finance & Budgets': 'Budget tracking and financial data',
            'Configuration': 'System settings and parameters',
            'Communication': 'Email, notifications, and messaging',
            'Other': 'Miscellaneous and utility tables'
        }

        for domain in DOMAIN_PATTERNS.keys():
            if domain in domains:
                table_count = len(domains[domain])
                total_rows = sum(t['rows'] for t in domains[domain])
                desc = domain_descriptions.get(domain, '')
                f.write(f'| [{domain}](#{domain.lower().replace(" ", "-").replace("&", "")}) | {table_count} | {total_rows:,} | {desc} |\n')

        if 'Other' in domains:
            table_count = len(domains['Other'])
            total_rows = sum(t['rows'] for t in domains['Other'])
            f.write(f'| [Other](#other) | {table_count} | {total_rows:,} | Miscellaneous tables |\n')

        f.write('\n---\n\n')

        # Detailed sections for each domain
        for domain in list(DOMAIN_PATTERNS.keys()) + ['Other']:
            if domain not in domains:
                continue

            anchor = domain.lower().replace(' ', '-').replace('&', '')
            f.write(f'## {domain} {{{anchor}}}\n\n')
            f.write(f'{domain_descriptions.get(domain, "")}\n\n')

            # Sort by row count descending
            sorted_tables = sorted(domains[domain], key=lambda x: -x['rows'])

            # Key tables (top 10 by row count)
            f.write('### Key Tables\n\n')
            f.write('| Table | Rows | Columns | Primary Key | Potential FKs |\n')
            f.write('|-------|------|---------|-------------|---------------|\n')

            for table in sorted_tables[:10]:
                pk_cols = [k['column'] for k in table['keys'] if k['type'] == 'PK']
                fk_cols = [k['column'] for k in table['keys'] if k['type'] == 'FK?']

                pk_str = ', '.join(pk_cols) if pk_cols else '*None*'
                fk_str = ', '.join(fk_cols[:3])  # Limit to 3
                if len(fk_cols) > 3:
                    fk_str += f' (+{len(fk_cols) - 3})'

                f.write(f'| {table["name"]} | {table["rows"]:,} | {table["columns"]} | {pk_str} | {fk_str} |\n')

            f.write('\n')

            # All tables in domain
            if len(sorted_tables) > 10:
                f.write('### All Tables\n\n')
                f.write('<details>\n<summary>Click to expand all tables</summary>\n\n')
                f.write('| Table | Rows | Modified |\n')
                f.write('|-------|------|----------|\n')
                for table in sorted_tables:
                    f.write(f'| {table["name"]} | {table["rows"]:,} | {table["modified"]} |\n')
                f.write('\n</details>\n\n')

            # Common relationships in this domain
            f.write('### Common Relationships\n\n')

            # Find common FK patterns
            fk_patterns = defaultdict(int)
            for table in sorted_tables:
                for key in table['keys']:
                    if key['type'] == 'FK?':
                        # Extract the referenced table name from the FK column
                        col_name = key['column']
                        if col_name.endswith('Id'):
                            ref_table = col_name[:-2]
                            fk_patterns[ref_table] += 1

            if fk_patterns:
                f.write('Based on naming conventions, tables in this domain commonly reference:\n\n')
                for ref, count in sorted(fk_patterns.items(), key=lambda x: -x[1])[:5]:
                    f.write(f'- **{ref}** (referenced by {count} tables)\n')
            else:
                f.write('*No common FK patterns detected*\n')

            f.write('\n---\n\n')

        # Cross-domain relationships
        f.write('## Cross-Domain Relationships\n\n')
        f.write('Key tables that are referenced across multiple domains:\n\n')

        # Find most referenced table patterns
        all_refs = defaultdict(set)
        for domain, domain_tables in domains.items():
            for table in domain_tables:
                for key in table['keys']:
                    if key['type'] == 'FK?':
                        ref = key['column'][:-2] if key['column'].endswith('Id') else key['column']
                        all_refs[ref].add(domain)

        # Tables referenced in 3+ domains
        cross_domain_refs = [(ref, doms) for ref, doms in all_refs.items() if len(doms) >= 3]
        cross_domain_refs.sort(key=lambda x: -len(x[1]))

        if cross_domain_refs:
            f.write('| Table Pattern | Referenced By Domains |\n')
            f.write('|---------------|----------------------|\n')
            for ref, doms in cross_domain_refs[:15]:
                f.write(f'| {ref}Id | {", ".join(sorted(doms))} |\n')
        else:
            f.write('*No significant cross-domain references detected*\n')

    logger.info(f"[OK] Documentation saved to {output_file}")
    print(f"\nBusiness domain guide saved to: {output_file}")
    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Analyze business domains')
    parser.add_argument('--database', '-d', default='EDS', help='Database name (default: EDS)')
    parser.add_argument('--output', '-o', default='docs', help='Output directory (default: docs)')

    args = parser.parse_args()

    try:
        analyze_business_domains(database=args.database, output_dir=args.output)
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
