#!/usr/bin/env python3
"""
Add Column Descriptions to EDS Database - Version 4

Final cleanup for remaining undocumented columns.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Remaining column descriptions
DESCRIPTIONS = {
    # AccountingFormats
    'LocationCodeRequired': 'Flag: location code required',
    'VendorBidNumberRequired': 'Flag: vendor bid number required',
    'VendorBidCommentsRequired': 'Flag: vendor bid comments required',
    'IncidentalOrdersSupported': 'Flag: incidental orders supported',
    'useFirstLast': 'Flag: use first/last name format',

    # AccountingUserFields
    'FieldPos': 'Field position in form',

    # additems (uppercase columns - import table)
    'ITEMCODE': 'Item code (import field)',
    'DESCRIPTION': 'Item description (import field)',
    'CATALOGPRICE': 'Catalog price (import field)',
    'PAGE': 'Catalog page (import field)',
    'BIDPRICE': 'Bid price (import field)',
    'CONTRACTNUMBER': 'Contract number (import field)',
    'VENDORITEMCODE': 'Vendor item code (import field)',

    # AnswerTypes
    'Mask': 'Input mask pattern',
    'RegExp': 'Regular expression for validation',

    # Audit
    'AuditAction': 'Type of audit action performed',
    'AuditRecord': 'Audit record data (JSON/XML)',

    # Awardings
    'NotificationsCreated': 'Number of notifications created',
    'NotificationsSent': 'Number of notifications sent',

    # BatchBook
    'Errors': 'Error count or messages',
    'DuplicateOk': 'Flag: duplicate allowed',
    'DuplicateDetected': 'Flag: duplicate was detected',
    'AmountOk': 'Flag: amount validated',

    # BatchDetail
    'OrigCategory': 'Original category before change',
    'ErrorField': 'Field with error',
    'PackComplete': 'Flag: package is complete',

    # BatchDetailInserts
    'qty': 'Quantity value',

    # BidAnswersJournal
    'BidAnswerExtended': 'Extended bid answer data',

    # BidCalendar
    'DateAvailable': 'Date available for bidding',

    # BidDocument
    'DocumentFilename': 'Document file name',

    # BidDocumentTypes
    'VendorSpecific': 'Flag: vendor-specific document',
    'OnlyShowOne': 'Flag: show only one instance',
    'Grouping': 'Document grouping category',
    'VendorUnique': 'Flag: unique per vendor',
    'Expires': 'Flag: document expires',

    # BidImports
    'FreeDeliveryMinimum': 'Minimum order for free delivery',
    'ContactFax': 'Contact fax number',
    'CatalogDiscountComments': 'Comments on catalog discount',

    # BidMgrConfiguration
    'CheckListHeaderRTF': 'Checklist header in RTF format',

    # BidMgrTagFile
    'Ptr': 'Pointer value',
    'OrigVal': 'Original value',

    # BidMSRPResultsProductLines
    'WeightedDiscount': 'Weighted average discount',

    # BidRequestItemMergeActions_Saved_101521
    'rowguid': 'Row GUID identifier',

    # BidResultChanges
    'PrevActive': 'Previous active status',
    'PrevComments': 'Previous comments',

    # BidTrades
    'Specifications': 'Trade specifications text',

    # BudgetAccounts
    'AmountAvailable': 'Available budget amount',

    # Budgets
    'VisibleUntil': 'Visible until date',
    'AnnualCutoff': 'Annual budget cutoff date',
    'EditUntil': 'Editable until date',

    # Category
    'AllowedCategories': 'List of allowed sub-categories',
    'DisplayOnWeb': 'Flag: display on web interface',
    'HasChildren': 'Flag: has child categories',
    'IncludeInSearch': 'Flag: include in search results',
    'ParentCategory': 'Parent category reference',
    'SortPriority': 'Sort priority value',

    # District (remaining)
    'AllowBackOrders': 'Flag: allow back orders',
    'AllowPartialShipments': 'Flag: allow partial shipments',
    'AutoApproveThreshold': 'Auto-approval dollar threshold',
    'BidOpeningLocation': 'Bid opening location address',
    'BudgetYearStartMonth': 'Budget year start month (1-12)',
    'DefaultShipVia': 'Default shipping method',
    'FiscalYearEndMonth': 'Fiscal year end month',
    'MaxLineItems': 'Maximum line items per order',
    'PONumberFormat': 'PO number format string',
    'RequireApproval': 'Flag: require approval for POs',
    'UseAccountCodes': 'Flag: use account codes',
    'UseBudgetCodes': 'Flag: use budget codes',

    # Vendors (remaining)
    'AcceptsPCard': 'Flag: accepts P-Card payments',
    'AllowDirectOrders': 'Flag: allow direct orders',
    'ContractEndDate': 'Contract end date',
    'ContractStartDate': 'Contract start date',
    'CreditLimit': 'Credit limit amount',
    'DefaultPaymentTerms': 'Default payment terms',
    'DefaultShipMethod': 'Default shipping method',
    'FederalTaxId': 'Federal tax ID (EIN)',
    'LeadTimeDays': 'Lead time in days',
    'MinimumOrderAmount': 'Minimum order amount',
    'PaymentTermsDays': 'Payment terms in days',

    # EmailBlast
    'BlastSubject': 'Email blast subject line',
    'BlastBody': 'Email blast body content',
    'RecipientCount': 'Number of recipients',
    'ScheduledTime': 'Scheduled send time',
    'SentCount': 'Number sent',
    'BouncedCount': 'Number bounced',

    # SessionTable
    'SessionData': 'Session data (serialized)',
    'LastAccessed': 'Last accessed timestamp',
    'IPAddress': 'Client IP address',
    'UserAgent': 'Browser user agent',
    'ExpiresAt': 'Session expiration time',
    'IsAuthenticated': 'Flag: user is authenticated',

    # ReportSession
    'ReportName': 'Report name',
    'Parameters': 'Report parameters (JSON)',
    'OutputFormat': 'Output format (PDF, Excel, etc.)',
    'GeneratedAt': 'Generation timestamp',
    'FileSize': 'Output file size',

    # OrderBooks
    'BookName': 'Order book name',
    'BookYear': 'Order book year',
    'IsLocked': 'Flag: book is locked',
    'TotalOrders': 'Total orders in book',
    'TotalAmount': 'Total amount in book',

    # dtproperties (system table)
    'objectid': 'Object identifier',
    'property': 'Property name',
    'value': 'Property value',
    'uvalue': 'Unicode property value',
    'lvalue': 'Large value (binary)',
    'version': 'Version number',

    # MSRPExcelImport/Export (Base columns)
    'Base1': 'Base price tier 1',
    'Base2': 'Base price tier 2',
    'Base3': 'Base price tier 3',
    'Base4': 'Base price tier 4',
    'Base5': 'Base price tier 5',
    'Base6': 'Base price tier 6',
    'Base7': 'Base price tier 7',
    'Base8': 'Base price tier 8',
    'Base9': 'Base price tier 9',
    'Base10': 'Base price tier 10',
    'RangeBase1': 'Range base price 1',
    'RangeBase2': 'Range base price 2',
    'RangeBase3': 'Range base price 3',
    'RangeBase4': 'Range base price 4',
    'RangeBase5': 'Range base price 5',
    'RangeBase6': 'Range base price 6',
    'RangeWeight1': 'Range weight tier 1',
    'RangeWeight2': 'Range weight tier 2',
    'RangeWeight3': 'Range weight tier 3',
    'RangeWeight4': 'Range weight tier 4',
    'RangeWeight5': 'Range weight tier 5',
    'RangeWeight6': 'Range weight tier 6',
    'Discount1': 'Discount tier 1 percentage',
    'Discount2': 'Discount tier 2 percentage',
    'Discount3': 'Discount tier 3 percentage',
    'Discount4': 'Discount tier 4 percentage',
    'Discount5': 'Discount tier 5 percentage',
    'Discount6': 'Discount tier 6 percentage',

    # RTK (Right-To-Know) chemical fields
    'CA': 'California hazard indicator',
    'CO': 'Colorado hazard indicator',
    'F2': 'Flammability level 2',
    'F4': 'Flammability level 4',
    'MU': 'Mutagen indicator',
    'R1': 'Reactivity level 1',
    'R2': 'Reactivity level 2',
    'R3': 'Reactivity level 3',
    'R4': 'Reactivity level 4',
    'TE': 'Teratogen indicator',

    # Common remaining patterns
    'Config': 'Configuration data',
    'Options': 'Options or settings',
    'Preferences': 'User preferences',
    'Settings': 'System settings',
    'Data': 'Data content',
    'Content': 'Content text',
    'Html': 'HTML content',
    'Xml': 'XML content',
    'Json': 'JSON content',
    'Binary': 'Binary data',
    'Blob': 'Binary large object',
    'Image': 'Image data',
    'File': 'File content',
    'Path': 'File path',
    'Url': 'URL address',
    'Link': 'Link reference',
    'Key': 'Key value',
    'Token': 'Token value',
    'Hash': 'Hash value',
    'Guid': 'GUID value',
    'Uuid': 'UUID value',
}


def add_column_descriptions(database='EDS'):
    """Add descriptions to remaining undocumented columns."""

    logger = setup_logging('add_column_descriptions_v4')
    logger.info(f"Adding column descriptions for {database} (v4 - cleanup)")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get undocumented columns
    undoc_cols = db.execute_query('''
        SELECT t.name AS TableName, c.name AS ColumnName
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON c.object_id = ep.major_id
            AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE s.name = 'dbo' AND ep.value IS NULL
        ORDER BY t.name, c.column_id
    ''')

    logger.info(f"Found {len(undoc_cols)} undocumented columns")

    success = 0
    skipped = 0
    errors = 0

    for table, column in undoc_cols:
        desc = DESCRIPTIONS.get(column)

        if not desc:
            skipped += 1
            continue

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = N'dbo',
                    @level1type = N'TABLE', @level1name = ?,
                    @level2type = N'COLUMN', @level2name = ?
            ''', (desc, table, column))
            success += 1
            if success % 50 == 0:
                logger.info(f"  Applied {success} descriptions...")
        except Exception as e:
            errors += 1
            if errors <= 5:
                logger.warning(f"Error on {table}.{column}: {str(e)[:50]}")

    db.disconnect()

    logger.info(f"[OK] Column descriptions added: {success}")
    logger.info(f"  Columns without description: {skipped}")
    logger.info(f"  Errors: {errors}")

    print(f"\nColumn descriptions added: {success}")
    print(f"Columns still undocumented: {skipped}")
    print(f"Errors: {errors}")

    return success


if __name__ == '__main__':
    add_column_descriptions()
