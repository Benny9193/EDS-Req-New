#!/usr/bin/env python3
"""
Add Column Descriptions - Final Pass

Documents remaining business columns.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Remaining column descriptions
DESCRIPTIONS = {
    # cxmlSession (punchout catalog)
    'payloadId': 'cXML payload identifier',
    'buyerCookie': 'Buyer session cookie token',
    'BrowserFormPost': 'Browser form post data',
    'fromDomain': 'cXML sender from domain',
    'fromIdentity': 'cXML sender from identity',
    'toDomain': 'cXML recipient to domain',
    'toIdentity': 'cXML recipient to identity',
    'senderDomain': 'cXML sender domain',
    'senderIdentity': 'cXML sender identity',
    'senderSharedSecret': 'cXML sender shared secret (encrypted)',
    'fromUserAgent': 'HTTP user agent string',
    'deploymentMode': 'Deployment mode (test/production)',
    'extrinsic': 'cXML extrinsic data',
    'timestamp': 'Transaction timestamp',
    'RequestURL': 'Request URL',
    'RequestContent': 'Request content/payload',
    'ResponseURL': 'Response URL',
    'ResponseContent': 'Response content/payload',
    'OrderRequestURL': 'Order request URL',
    'OrderResponseContent': 'Order response content',

    # District
    'POsBySchool': 'Flag: generate POs by school',
    'ReqsBySchool': 'Flag: generate requisitions by school',
    'POConsolidation': 'PO consolidation method code',
    'TextbookPercentage': 'Textbook percentage allocation',
    'NoBooklets': 'Flag: do not print booklets',
    'RightToKnow': 'Right-To-Know compliance level',
    'NoAdvises': 'Flag: do not send advise notifications',
    'TimeAndMaterialBids': 'Flag: allow time & material bids',
    'PrintBidAs': 'Print bid format option',
    'IncidentalPOGenerationMethod': 'Incidental PO generation method',
    'IncidentalOrdersPrefix': 'Prefix for incidental order numbers',
    'POApprovalThreshold': 'PO approval threshold amount',

    # Vendors
    'ShippingPercentage': 'Default shipping percentage rate',
    'HostPort': 'FTP/API host port number',
    'HostDirectory': 'FTP/API host directory path',
    'HostPassword': 'FTP/API host password (encrypted)',
    'UploadEMailList': 'Email list for upload notifications',
    'POPassword': 'PO access password (encrypted)',
    'DisplayAs': 'Display name format',
    'incXMLFromDomain': 'Incoming XML from domain',
    'incXMLFromIdentity': 'Incoming XML from identity',
    'incXMLSharedSecret': 'Incoming XML shared secret (encrypted)',
    'incXMLToDomain': 'Incoming XML to domain',

    # EmailBlast
    'SQLStmt': 'SQL statement for recipient query',
    'ReportWhereClause': 'WHERE clause for report filter',
    'ReadReceipt': 'Flag: request read receipt',
    'BlastVar1': 'Email blast variable 1',
    'BlastVar2': 'Email blast variable 2',
    'VarDataSQL': 'SQL for variable data population',

    # RTK_Sites
    'NJEIN': 'New Jersey Environmental ID Number',
    'MailingAddress3': 'Mailing address line 3',
    'MailingAddress4': 'Mailing address line 4',
    'ResponsibleOfficial': 'Responsible official name',
    'TitleResponsibleOfficial': 'Title of responsible official',
    'PhoneResponsibleOfficial': 'Phone of responsible official',

    # SessionTable
    'Mode': 'Session mode identifier',
    'SessionLast': 'Last session activity timestamp',
    'ResolutionX': 'Screen resolution width',
    'ResolutionY': 'Screen resolution height',
    'TabSelected': 'Currently selected tab',
    'ReloadPage': 'Flag: page needs reload',

    # OrderBooks
    'OrderBookYear': 'Order book fiscal year',
    'OrderBookCreated': 'Order book creation date',
    'MasterBook': 'Master book reference ID',
    'MasterLetter': 'Master book letter code',
    'KeepZeroPages': 'Flag: keep pages with zero items',

    # Category
    'KeywordExamples': 'Example keywords for category',
    'BreakOnHeadingChange': 'Flag: page break on heading change',
    'MasterBookCopies': 'Number of master book copies',
    'useCatalogViewer': 'Flag: use catalog viewer',
    'RTKLocation': 'Right-To-Know storage location',

    # ReportSession
    'ReportStarted': 'Report generation start time',
    'ReportEnded': 'Report generation end time',
    'ReportOption': 'Report option selection',
    'PrintPages': 'Number of pages to print',
    'PrintCopies': 'Number of copies to print',

    # VPORegistrations
    'VPOPassword': 'Vendor PO portal password (encrypted)',
    'VPOLastChange': 'Last password change date',
    'VPOEMail': 'Vendor portal email address',
    'VPOAllowedRetries': 'Allowed login retry attempts',
    'VPOCanCreateUser': 'Flag: can create sub-users',

    # CalendarDates
    'Date1': 'Calendar date 1',
    'Date2': 'Calendar date 2',
    'Date3': 'Calendar date 3',
    'Date4': 'Calendar date 4',

    # CoverView
    'SchoolAddress3': 'School address line 3',
    'SchoolZipcode': 'School ZIP code',
    'RepMsg': 'Representative message',
    'ScheduleGroup': 'Schedule group assignment',

    # OBView
    'DistrictUsed': 'Flag: used by district',
    'ExpandAll': 'Flag: expand all sections',
    'MustKeep': 'Flag: must keep item',
    'Compliant': 'Flag: item is compliant',

    # OrderBookLog
    'Printed': 'Print timestamp',
    'ItemsPrinted': 'Number of items printed',
    'PagesPrinted': 'Number of pages printed',
    'Device': 'Print device name',

    # PricingAddenda
    'BidResponseAddendum': 'Bid response addendum text',
    'BidResponsePricingType': 'Bid response pricing type',
    'BidResponsePricingDate': 'Bid response pricing date',
    'BidResponsePricingNotes': 'Bid response pricing notes',

    # Additional common columns
    'SQLStatement': 'SQL statement text',
    'WhereClause': 'WHERE clause text',
    'OrderByClause': 'ORDER BY clause text',
    'FilterExpression': 'Filter expression',
    'SortExpression': 'Sort expression',
    'GroupByExpression': 'GROUP BY expression',
    'ParameterList': 'Parameter list',
    'ParameterValues': 'Parameter values',
    'ReturnValue': 'Return value',
    'ErrorMessage': 'Error message text',
    'WarningMessage': 'Warning message text',
    'InfoMessage': 'Information message text',
    'DebugMessage': 'Debug message text',
    'LogMessage': 'Log message text',
    'AuditMessage': 'Audit message text',
    'NotificationMessage': 'Notification message text',
    'AlertMessage': 'Alert message text',
    'ConfirmationMessage': 'Confirmation message text',
    'ValidationMessage': 'Validation message text',
    'SuccessMessage': 'Success message text',
    'FailureMessage': 'Failure message text',
}


def add_descriptions(database='EDS'):
    """Add descriptions to remaining columns."""

    logger = setup_logging('add_column_descriptions_final')
    logger.info(f"Final pass for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get undocumented columns
    undoc = db.execute_query('''
        SELECT s.name, t.name, c.name
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON c.object_id = ep.major_id
            AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE ep.value IS NULL
    ''')

    logger.info(f"Found {len(undoc)} undocumented columns")

    success = 0
    for schema, table, column in undoc:
        desc = DESCRIPTIONS.get(column)
        if not desc:
            continue

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'TABLE', @level1name = ?,
                    @level2type = N'COLUMN', @level2name = ?
            ''', (desc, schema, table, column))
            success += 1
        except:
            pass

    db.disconnect()

    logger.info(f"[OK] Added {success} descriptions")
    print(f"\nColumn descriptions added: {success}")
    return success


if __name__ == '__main__':
    add_descriptions()
