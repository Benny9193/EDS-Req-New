#!/usr/bin/env python3
"""
Document Stored Procedures

Adds MS_Description extended properties to stored procedures based on naming patterns.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Specific procedure descriptions
PROC_DESCRIPTIONS = {
    # Common CRUD patterns
    'sp_Insert': 'Insert new record into',
    'sp_Update': 'Update existing record in',
    'sp_Delete': 'Delete record from',
    'sp_Get': 'Retrieve record(s) from',
    'sp_Select': 'Select data from',
    'sp_Save': 'Save (insert or update) record in',
    'sp_Add': 'Add new record to',
    'sp_Remove': 'Remove record from',
    'sp_Create': 'Create new',
    'sp_Modify': 'Modify existing',

    # Bid Management
    'BidMgr': 'Bid manager procedure for',
    'Bid_': 'Bid processing procedure for',
    'Award': 'Award processing procedure for',
    'BidResult': 'Bid result processing for',
    'BidRequest': 'Bid request processing for',
    'BidHeader': 'Bid header management for',
    'BidItem': 'Bid item processing for',

    # Catalog/Items
    'Catalog': 'Catalog management procedure for',
    'Item': 'Item management procedure for',
    'Category': 'Category management procedure for',
    'Price': 'Pricing procedure for',

    # Order Management
    'PO': 'Purchase order procedure for',
    'Order': 'Order processing procedure for',
    'Requisition': 'Requisition procedure for',
    'Detail': 'Detail record procedure for',

    # Vendor Management
    'Vendor': 'Vendor management procedure for',
    'VPO': 'Vendor portal procedure for',

    # User/Security
    'User': 'User management procedure for',
    'Approval': 'Approval workflow procedure for',
    'Session': 'Session management procedure for',
    'Login': 'Login/authentication procedure for',
    'Password': 'Password management procedure for',

    # Reports
    'Report': 'Report generation procedure for',
    'rpt_': 'Report procedure for',
    'Export': 'Export procedure for',
    'Import': 'Import procedure for',

    # Email/Notifications
    'Email': 'Email procedure for',
    'Notify': 'Notification procedure for',
    'Alert': 'Alert procedure for',
    'Blast': 'Email blast procedure for',

    # Batch/Processing
    'Batch': 'Batch processing procedure for',
    'Process': 'Processing procedure for',
    'Job': 'Job procedure for',
    'Queue': 'Queue management procedure for',

    # Archive/Cleanup
    'Archive': 'Archive procedure for',
    'Cleanup': 'Cleanup procedure for',
    'Purge': 'Purge procedure for',

    # Validation/Check
    'Validate': 'Validation procedure for',
    'Check': 'Check/verify procedure for',
    'Verify': 'Verification procedure for',

    # Search/Lookup
    'Search': 'Search procedure for',
    'Lookup': 'Lookup procedure for',
    'Find': 'Find procedure for',
    'List': 'List procedure for',

    # Calculate/Compute
    'Calc': 'Calculation procedure for',
    'Compute': 'Computation procedure for',
    'Sum': 'Summation procedure for',
    'Total': 'Total calculation procedure for',

    # Sync/Transfer
    'Sync': 'Synchronization procedure for',
    'Transfer': 'Transfer procedure for',
    'Copy': 'Copy procedure for',
    'Move': 'Move procedure for',

    # Logging/Audit
    'Log': 'Logging procedure for',
    'Audit': 'Audit procedure for',
    'Track': 'Tracking procedure for',

    # Configuration
    'Config': 'Configuration procedure for',
    'Setting': 'Settings procedure for',
    'Setup': 'Setup procedure for',
    'Init': 'Initialization procedure for',
}

# Action verb mappings for procedure names
ACTION_VERBS = {
    'Get': 'Retrieve',
    'Set': 'Set/update',
    'Add': 'Add new',
    'Insert': 'Insert new',
    'Update': 'Update existing',
    'Delete': 'Delete',
    'Remove': 'Remove',
    'Create': 'Create new',
    'Save': 'Save',
    'Load': 'Load',
    'Find': 'Find',
    'Search': 'Search for',
    'List': 'List',
    'Count': 'Count',
    'Check': 'Check/validate',
    'Validate': 'Validate',
    'Verify': 'Verify',
    'Process': 'Process',
    'Execute': 'Execute',
    'Run': 'Run',
    'Start': 'Start',
    'Stop': 'Stop',
    'Enable': 'Enable',
    'Disable': 'Disable',
    'Generate': 'Generate',
    'Build': 'Build',
    'Calculate': 'Calculate',
    'Compute': 'Compute',
    'Send': 'Send',
    'Receive': 'Receive',
    'Import': 'Import',
    'Export': 'Export',
    'Copy': 'Copy',
    'Move': 'Move',
    'Archive': 'Archive',
    'Restore': 'Restore',
    'Reset': 'Reset',
    'Clear': 'Clear',
    'Purge': 'Purge old',
    'Cleanup': 'Clean up',
    'Merge': 'Merge',
    'Split': 'Split',
    'Lock': 'Lock',
    'Unlock': 'Unlock',
    'Approve': 'Approve',
    'Reject': 'Reject',
    'Submit': 'Submit',
    'Cancel': 'Cancel',
    'Close': 'Close',
    'Open': 'Open',
    'Print': 'Print',
    'Email': 'Email',
    'Notify': 'Notify',
    'Log': 'Log',
    'Track': 'Track',
}


def get_proc_description(proc_name):
    """Generate description for a stored procedure based on its name."""

    # Check specific patterns first
    for pattern, desc_prefix in PROC_DESCRIPTIONS.items():
        if pattern.lower() in proc_name.lower():
            # Extract the subject from the procedure name
            subject = proc_name.replace('sp_', '').replace('usp_', '')
            for p in PROC_DESCRIPTIONS.keys():
                subject = subject.replace(p, '')
            subject = subject.strip('_')
            if subject:
                return f'{desc_prefix} {subject}'
            return f'{desc_prefix} data'

    # Try to parse action verb + subject pattern
    clean_name = proc_name.replace('sp_', '').replace('usp_', '').replace('proc_', '')

    # Check for action verbs at the start
    for verb, verb_desc in ACTION_VERBS.items():
        if clean_name.startswith(verb):
            subject = clean_name[len(verb):].strip('_')
            if subject:
                # Convert CamelCase to readable
                import re
                subject = re.sub(r'([a-z])([A-Z])', r'\1 \2', subject)
                subject = subject.replace('_', ' ').lower()
                return f'{verb_desc} {subject}'

    # Default description
    clean_name = clean_name.replace('_', ' ')
    return f'Stored procedure: {clean_name}'


def document_stored_procedures(database='EDS'):
    """Add MS_Description to stored procedures."""

    logger = setup_logging('document_stored_procedures')
    logger.info(f"Documenting stored procedures for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get stored procedures without descriptions
    procs = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName
        FROM sys.procedures p
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON p.object_id = ep.major_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        WHERE ep.value IS NULL
        ORDER BY s.name, p.name
    ''')

    logger.info(f"Found {len(procs)} undocumented stored procedures")

    success = 0
    errors = 0

    for schema, proc in procs:
        desc = get_proc_description(proc)

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'PROCEDURE', @level1name = ?
            ''', (desc, schema, proc))
            success += 1
            if success % 50 == 0:
                logger.info(f"  Applied {success} procedure descriptions...")
        except Exception as e:
            errors += 1
            if errors <= 5:
                logger.warning(f"Error on {schema}.{proc}: {str(e)[:50]}")

    db.disconnect()

    logger.info(f"[OK] Stored procedure descriptions added: {success}")
    logger.info(f"  Errors: {errors}")

    print(f"\nStored procedure descriptions added: {success}")
    print(f"Errors: {errors}")

    return success


if __name__ == '__main__':
    document_stored_procedures()
