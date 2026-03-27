#!/usr/bin/env python3
"""
Generate Extended Properties Script

Creates SQL scripts to add MS_Description extended properties
to tables and columns in SQL Server for inline documentation.
"""

import os
import sys
from datetime import datetime

# Add scripts directory to path
sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection, DatabaseConnectionError
from logging_config import setup_logging


# Table descriptions based on naming patterns and business domain analysis
TABLE_DESCRIPTIONS = {
    # Bidding System
    'BidHeaders': 'Master bid/solicitation records containing bid numbers, dates, and status',
    'BidItems': 'Line items within bids specifying products/services being solicited',
    'BidResults': 'Awarded bid results linking vendors to bid items with pricing',
    'BidRequests': 'Vendor requests to participate in bids',
    'BidDocuments': 'Documents attached to bids (specs, terms, addenda)',
    'BidSchedule': 'Scheduled dates and milestones for bid processes',
    'BidScheduleCats': 'Categories for bid scheduling',
    'BidVendors': 'Vendors invited or participating in specific bids',
    'BidQuestions': 'Questions submitted by vendors during bid process',
    'BidAnswers': 'Answers to vendor questions on bids',
    'BidAddendums': 'Addendums and modifications to published bids',

    # Orders & Purchasing
    'PO': 'Purchase order headers with vendor, dates, and totals',
    'Detail': 'Purchase order line items with quantities and prices',
    'Requisitions': 'Purchase requisition requests before PO creation',
    'RequisitionDetails': 'Line items within requisitions',
    'OrderBooks': 'Order book/catalog management',
    'Contracts': 'Contract agreements with vendors',
    'ContractItems': 'Line items within contracts',

    # Vendors
    'Vendors': 'Master vendor/supplier records with contact information',
    'VendorDocuments': 'Documents uploaded by or for vendors',
    'Registrations': 'Vendor registration records and status',
    'VendorCategories': 'Category classifications for vendors',
    'VendorCertifications': 'Vendor certifications (minority, small business, etc.)',
    'VendorContacts': 'Contact persons at vendor companies',
    'VendorLocations': 'Vendor address and location information',

    # Items & Inventory
    'Items': 'Master item/product catalog',
    'ItemCategories': 'Category hierarchy for items',
    'Inventory': 'Current inventory levels and locations',
    'ItemPrices': 'Pricing information for items',

    # Users & Security
    'UserAccounts': 'User login accounts and credentials',
    'Users': 'User profile information',
    'Approvals': 'Approval workflow records',
    'ApprovalLevels': 'Approval hierarchy and thresholds',
    'Permissions': 'User permission assignments',
    'Roles': 'Security role definitions',
    'Sessions': 'User session tracking',
    'AuditLog': 'System audit trail for changes',

    # Organizations
    'Districts': 'School districts or organizational units',
    'Schools': 'Individual schools within districts',
    'Departments': 'Departmental divisions',
    'Locations': 'Physical location addresses',

    # Documents
    'Documents': 'General document storage metadata',
    'Attachments': 'File attachments linked to various records',
    'Templates': 'Document templates for forms and reports',

    # Finance
    'Budgets': 'Budget allocations and tracking',
    'BudgetCodes': 'Budget account codes',
    'Accounts': 'Chart of accounts',
    'Transactions': 'Financial transaction records',
    'Invoices': 'Vendor invoices',
    'Payments': 'Payment records',

    # Reporting
    'Reports': 'Saved report definitions',
    'ReportSchedule': 'Scheduled report execution',
    'TransactionLog': 'Transaction logging for reporting',

    # Configuration
    'Settings': 'System configuration settings',
    'Parameters': 'System parameters and thresholds',
    'LookupValues': 'Lookup/reference data values',
    'Categories': 'General category definitions',
}

# Column descriptions for common patterns
COLUMN_DESCRIPTIONS = {
    # ID columns
    'Id': 'Primary key identifier',
    'ID': 'Primary key identifier',

    # Foreign keys (by suffix pattern)
    'HeaderId': 'Foreign key to parent header record',
    'VendorId': 'Foreign key to Vendors table',
    'UserId': 'Foreign key to Users/UserAccounts table',
    'DistrictId': 'Foreign key to Districts table',
    'ItemId': 'Foreign key to Items table',
    'BudgetId': 'Foreign key to Budgets table',

    # Common fields
    'CreatedDate': 'Record creation timestamp',
    'ModifiedDate': 'Last modification timestamp',
    'CreatedBy': 'User who created the record',
    'ModifiedBy': 'User who last modified the record',
    'IsActive': 'Indicates if record is active (1) or inactive (0)',
    'IsDeleted': 'Soft delete flag (1=deleted, 0=active)',
    'Status': 'Current status of the record',
    'StatusId': 'Foreign key to status lookup',
    'Description': 'Text description of the record',
    'Name': 'Display name',
    'Code': 'Short code or identifier',
    'Notes': 'Additional notes or comments',
    'Amount': 'Monetary amount',
    'Quantity': 'Numeric quantity',
    'UnitPrice': 'Price per unit',
    'TotalAmount': 'Calculated total amount',
    'StartDate': 'Effective start date',
    'EndDate': 'Effective end date',
    'DueDate': 'Due or deadline date',
    'Email': 'Email address',
    'Phone': 'Phone number',
    'Address': 'Street address',
    'City': 'City name',
    'State': 'State/province code',
    'Zip': 'Postal/ZIP code',
    'ZipCode': 'Postal/ZIP code',
}


def generate_extended_properties(database='EDS', output_dir='docs'):
    """Generate SQL script to add extended properties."""

    logger = setup_logging('generate_extended_properties')
    logger.info(f"Generating extended properties script for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all tables
    tables = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = 'dbo'
        ORDER BY t.name
    ''')
    logger.info(f"Found {len(tables)} tables")

    # Get all columns
    columns = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            c.name AS ColumnName
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = 'dbo'
        ORDER BY t.name, c.column_id
    ''')
    logger.info(f"Found {len(columns)} columns")

    # Check existing extended properties
    existing = db.execute_query('''
        SELECT
            OBJECT_NAME(ep.major_id) AS TableName,
            c.name AS ColumnName,
            ep.value AS Description
        FROM sys.extended_properties ep
        LEFT JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id
        WHERE ep.name = 'MS_Description'
        AND ep.class = 1
    ''')
    logger.info(f"Found {len(existing)} existing descriptions")

    db.disconnect()

    # Build set of existing descriptions
    existing_set = set()
    for ex in existing:
        if ex[1]:  # Column description
            existing_set.add(f"{ex[0]}.{ex[1]}")
        else:  # Table description
            existing_set.add(ex[0])

    # Generate SQL script
    os.makedirs(output_dir, exist_ok=True)
    output_file = os.path.join(output_dir, f'{database}_EXTENDED_PROPERTIES.sql')

    table_count = 0
    column_count = 0

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f'-- {database} Database Extended Properties Script\n')
        f.write(f'-- Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}\n')
        f.write('-- Adds MS_Description extended properties for documentation\n')
        f.write('--\n')
        f.write('-- Run this script to add inline documentation to SQL Server\n')
        f.write('-- These descriptions appear in SSMS and documentation tools\n')
        f.write('--\n\n')

        f.write('USE [' + database + '];\nGO\n\n')

        # Table descriptions
        f.write('-- ============================================\n')
        f.write('-- TABLE DESCRIPTIONS\n')
        f.write('-- ============================================\n\n')

        for schema, table in tables:
            if table in existing_set:
                continue  # Skip if already has description

            # Find description
            desc = TABLE_DESCRIPTIONS.get(table)
            if not desc:
                # Try to infer from name
                if 'Bid' in table:
                    desc = f'Bidding system table for {table}'
                elif 'Vendor' in table:
                    desc = f'Vendor management table for {table}'
                elif 'PO' in table or 'Order' in table:
                    desc = f'Purchase order table for {table}'
                elif 'User' in table or 'Account' in table:
                    desc = f'User/security table for {table}'
                elif 'Budget' in table:
                    desc = f'Budget/finance table for {table}'
                elif 'Report' in table:
                    desc = f'Reporting table for {table}'
                elif 'Log' in table or 'Audit' in table:
                    desc = f'Audit/logging table for {table}'
                elif 'Config' in table or 'Setting' in table:
                    desc = f'Configuration table for {table}'
                else:
                    desc = f'{table} data table'

            # Escape single quotes
            desc = desc.replace("'", "''")

            f.write(f"-- {table}\n")
            f.write(f"IF NOT EXISTS (SELECT 1 FROM sys.extended_properties WHERE major_id = OBJECT_ID('{schema}.{table}') AND minor_id = 0 AND name = 'MS_Description')\n")
            f.write(f"    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'{desc}', @level0type = N'SCHEMA', @level0name = N'{schema}', @level1type = N'TABLE', @level1name = N'{table}';\n")
            f.write('GO\n\n')
            table_count += 1

        # Column descriptions
        f.write('\n-- ============================================\n')
        f.write('-- COLUMN DESCRIPTIONS\n')
        f.write('-- ============================================\n\n')

        current_table = ''
        for schema, table, column in columns:
            col_key = f"{table}.{column}"
            if col_key in existing_set:
                continue

            # Find description
            desc = None

            # Check exact match
            if column in COLUMN_DESCRIPTIONS:
                desc = COLUMN_DESCRIPTIONS[column]
            else:
                # Check suffix patterns
                for pattern, pattern_desc in COLUMN_DESCRIPTIONS.items():
                    if column.endswith(pattern) and len(pattern) > 2:
                        desc = pattern_desc
                        break

                # Check if it's a foreign key by naming convention
                if not desc and column.endswith('Id') and column != 'Id':
                    ref_table = column[:-2]
                    if ref_table + 's' in [t[1] for t in tables]:
                        desc = f'Foreign key to {ref_table}s table'
                    elif ref_table in [t[1] for t in tables]:
                        desc = f'Foreign key to {ref_table} table'

            if not desc:
                continue  # Skip columns we can't describe

            # Escape single quotes
            desc = desc.replace("'", "''")

            if table != current_table:
                f.write(f'\n-- Table: {table}\n')
                current_table = table

            f.write(f"IF NOT EXISTS (SELECT 1 FROM sys.extended_properties ep JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id WHERE ep.major_id = OBJECT_ID('{schema}.{table}') AND c.name = '{column}' AND ep.name = 'MS_Description')\n")
            f.write(f"    EXEC sp_addextendedproperty @name = N'MS_Description', @value = N'{desc}', @level0type = N'SCHEMA', @level0name = N'{schema}', @level1type = N'TABLE', @level1name = N'{table}', @level2type = N'COLUMN', @level2name = N'{column}';\n")
            f.write('GO\n')
            column_count += 1

    logger.info(f"[OK] Script saved to {output_file}")
    logger.info(f"  Table descriptions: {table_count}")
    logger.info(f"  Column descriptions: {column_count}")

    print(f"\nExtended properties script saved to: {output_file}")
    print(f"  - {table_count} table descriptions")
    print(f"  - {column_count} column descriptions")
    print(f"\nReview and run in SSMS to add documentation to SQL Server")

    return output_file


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Generate extended properties SQL script')
    parser.add_argument('--database', '-d', default='EDS', help='Database name (default: EDS)')
    parser.add_argument('--output', '-o', default='docs', help='Output directory (default: docs)')

    args = parser.parse_args()

    try:
        generate_extended_properties(database=args.database, output_dir=args.output)
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
