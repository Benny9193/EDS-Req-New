#!/usr/bin/env python3
"""
Document Archive Schema

Adds MS_Description extended properties to archive schema tables and columns.
Archive tables mirror dbo tables for historical data retention.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Archive table descriptions (based on dbo counterparts)
ARCHIVE_TABLE_DESCRIPTIONS = {
    'BidResults': 'Archived bid results - historical vendor bid responses and awards',
    'BidHeaderDetail': 'Archived bid header details - historical bid line item data',
    'Detail': 'Archived purchase order details - historical order line items',
    'PODetailItems': 'Archived PO detail items - historical order item records',
    'BidRequestItems': 'Archived bid request items - historical items requested for bid',
    'BatchDetail': 'Archived batch details - historical batch processing records',
    'Approvals': 'Archived approvals - historical approval workflow records',
    'UserAccounts': 'Archived user accounts - historical user credential records',
    'UserAccountsUserAccountId_CrossMapping': 'Archived user account ID cross-reference mapping',
    'RequisitionChangeLog': 'Archived requisition changes - historical change tracking',
    'Requisitions': 'Archived requisitions - historical purchase requests',
    'PO': 'Archived purchase orders - historical PO header records',
    'ApprovalsHistory': 'Archived approval history - historical approval actions',
    'Bids': 'Archived bids - historical bid/solicitation records',
    'Awards': 'Archived awards - historical bid award records',
    'cxmlSession': 'Archived cXML sessions - historical punchout sessions',
    'BidImports': 'Archived bid imports - historical vendor bid file imports',
    'VendorQueryDetail': 'Archived vendor query details - historical vendor inquiry records',
    'TMAwards': 'Archived TM awards - historical term contract awards',
    'BidHeaderDocument': 'Archived bid header documents - historical bid attachments',
    'BidMSRPResults': 'Archived MSRP bid results - historical manufacturer pricing bids',
    'BidHeaderCheckList': 'Archived bid checklists - historical bid compliance checks',
    'VendorQuery': 'Archived vendor queries - historical vendor inquiry records',
    'BidHeaders': 'Archived bid headers - historical bid/solicitation headers',
    'Catalog': 'Archived catalog data - historical product catalog records',
    'DetailMatch': 'Archived detail matches - historical order matching records',
    'OrderBooks': 'Archived order books - historical order book records',
    'BidTrades': 'Archived bid trades - historical commodity trade classifications',
    'VendorQueryTandM': 'Archived T&M vendor queries - historical time & materials inquiries',
    'VendorQueryTandMDetail': 'Archived T&M query details - historical T&M line items',
    'VendorDocRequest': 'Archived vendor document requests - historical doc requests',
    'VendorDocRequestDetail': 'Archived vendor doc request details - historical request items',
    'VendorQueryMSRP': 'Archived MSRP vendor queries - historical MSRP pricing inquiries',
    'VendorQueryMSRPDetail': 'Archived MSRP query details - historical MSRP line items',
    'DetailHold': 'Archived detail holds - historical held order items',
    'BidRequestManufacturer': 'Archived bid request manufacturers - historical manufacturer bids',
    'BidRequestOptions': 'Archived bid request options - historical optional bid items',
    'BidRequestPriceRanges': 'Archived bid price ranges - historical tiered pricing',
    'POTempDetails': 'Archived temporary PO details - historical staging records',
    'Prices': 'Archived prices - historical pricing records',
    'PricingConsolidatedOrderCounts': 'Archived pricing order counts - historical volume data',
    'PricingMap': 'Archived pricing maps - historical price mapping rules',
    'PricingUpdate': 'Archived pricing updates - historical price change records',
    'DMSBidDocuments': 'Archived DMS bid documents - historical document management records',
    'DMSVendorBidDocuments': 'Archived DMS vendor bid docs - historical vendor documents',
    'FreezeItems': 'Archived frozen items - historical price-frozen items',
    'ItemContractPrices': 'Archived item contract prices - historical contract pricing',
    'allitems': 'Archived all items - historical complete item catalog',
    'BidHeaderDocuments': 'Archived bid header documents - historical bid attachments',
    'BidReawards': 'Archived bid re-awards - historical re-awarded bid items',
    'BidMappedItems': 'Archived bid mapped items - historical item mappings',
}


def document_archive_schema(database='EDS'):
    """Add documentation to archive schema tables and columns."""

    logger = setup_logging('document_archive_schema')
    logger.info(f"Documenting archive schema for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get archive tables
    tables = db.execute_query('''
        SELECT t.name
        FROM sys.tables t
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE s.name = 'archive'
    ''')
    logger.info(f"Found {len(tables)} archive tables")

    # Add table descriptions
    table_success = 0
    for (table,) in tables:
        desc = ARCHIVE_TABLE_DESCRIPTIONS.get(table, f'Archived {table} data - historical records')

        # Check if already has description
        existing = db.fetch_one('''
            SELECT 1 FROM sys.extended_properties
            WHERE major_id = OBJECT_ID(?) AND minor_id = 0 AND name = 'MS_Description'
        ''', (f'archive.{table}',))

        if existing:
            continue

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = N'archive',
                    @level1type = N'TABLE', @level1name = ?
            ''', (desc, table))
            table_success += 1
        except Exception as e:
            logger.warning(f"Error on table {table}: {str(e)[:50]}")

    logger.info(f"Added {table_success} table descriptions")

    # Get column descriptions from dbo schema to copy to archive
    logger.info("Copying column descriptions from dbo to archive...")

    # Get dbo column descriptions
    dbo_descs = db.execute_query('''
        SELECT
            t.name AS TableName,
            c.name AS ColumnName,
            CAST(ep.value AS NVARCHAR(MAX)) AS Description
        FROM sys.extended_properties ep
        INNER JOIN sys.columns c ON ep.major_id = c.object_id AND ep.minor_id = c.column_id
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        WHERE ep.name = 'MS_Description' AND s.name = 'dbo'
    ''')

    # Build lookup
    dbo_lookup = {}
    for table, col, desc in dbo_descs:
        key = f'{table}.{col}'
        dbo_lookup[key] = desc

    logger.info(f"Found {len(dbo_lookup)} dbo column descriptions to copy")

    # Get archive columns without descriptions
    archive_cols = db.execute_query('''
        SELECT
            t.name AS TableName,
            c.name AS ColumnName
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON c.object_id = ep.major_id
            AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE s.name = 'archive' AND ep.value IS NULL
    ''')

    logger.info(f"Found {len(archive_cols)} undocumented archive columns")

    col_success = 0
    col_skipped = 0

    for table, column in archive_cols:
        # Look up description from dbo
        key = f'{table}.{column}'
        desc = dbo_lookup.get(key)

        if not desc:
            col_skipped += 1
            continue

        # Add "Archived: " prefix to distinguish
        desc = f'(Archived) {desc}'

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = N'archive',
                    @level1type = N'TABLE', @level1name = ?,
                    @level2type = N'COLUMN', @level2name = ?
            ''', (desc, table, column))
            col_success += 1
            if col_success % 100 == 0:
                logger.info(f"  Applied {col_success} column descriptions...")
        except Exception as e:
            pass  # Skip errors silently

    db.disconnect()

    logger.info(f"[OK] Archive documentation complete")
    logger.info(f"  Table descriptions: {table_success}")
    logger.info(f"  Column descriptions: {col_success}")
    logger.info(f"  Columns without dbo match: {col_skipped}")

    print(f"\nArchive schema documentation complete:")
    print(f"  Table descriptions added: {table_success}")
    print(f"  Column descriptions added: {col_success}")
    print(f"  Columns without dbo match: {col_skipped}")

    return table_success, col_success


if __name__ == '__main__':
    document_archive_schema()
