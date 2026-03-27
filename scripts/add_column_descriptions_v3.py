#!/usr/bin/env python3
"""
Add Column Descriptions to EDS Database - Version 3

Final pass for remaining undocumented columns with table-specific context.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Multi-table column descriptions
MULTI_TABLE_DESCRIPTIONS = {
    'Description': 'Descriptive text for the record',
    'Started': 'Process start timestamp',
    'Tbl': 'Table name reference',
    'Usr': 'User identifier or name',
    'AmountBid': 'Bid amount submitted',
    'CategoryIdSpecific': 'Specific category classification ID',
    'CommonQuestion': 'Flag: common question shared across bids',
    'DateExported': 'Date data was exported',
    'DateUploaded': 'Date file/data was uploaded',
    'EmailBCC': 'Blind carbon copy email addresses',
    'EmailCC': 'Carbon copy email addresses',
    'ItemsBid': 'Number of items in bid',
    'Merged': 'Flag: record has been merged',
    'Note': 'Note or comment text',
    'Password': 'Encrypted password (do not expose)',
    'Records': 'Number of records',
    'Requested': 'Request timestamp or flag',
    'StateContractDiscount': 'State contract discount percentage',
    'Val': 'Value field',
    'ValidUntil': 'Valid until date/expiration',
    'Year': 'Year value',
    'AddressFromRep': 'Address from sales representative',
    'AlertMsg': 'Alert message text',
    'AllocationAvailable': 'Budget allocation available amount',
    'Attachments': 'Number of attachments or attachment data',
    'BidAnswer': 'Answer to bid question',
    'BlastHTML': 'HTML content for email blast',
    'Command': 'Command or action to execute',
    'CrossRefIdBid': 'Cross reference ID for bid item',
    'dateChecked': 'Date last checked/verified',
    'dateDeleted': 'Date record was deleted',
    'dateLoaded': 'Date data was loaded',
    'DatePrinted': 'Date document was printed',
    'DatePrintedDetail': 'Date detail section was printed',
    'DateReceived': 'Date received',
    'DistrictAddress1': 'District primary address line',
    'DistrictAddress2': 'District secondary address line',
    'DistrictAddress3': 'District third address line',
    'DistrictZipcode': 'District ZIP code',
    'EarlyAccess': 'Flag: early access enabled',
    'EmailText': 'Email body text content',
    'ExcelFile': 'Excel file reference or content',
    'ExpectedTimeOfArrival': 'Expected arrival time',
    'FieldName': 'Field name reference',
    'FileName': 'File name',
    'FilePath': 'File path location',
    'FileSize': 'File size in bytes',
    'FileType': 'File type/extension',
    'FromEmailAddress': 'Sender email address',
    'FullText': 'Full text content',
    'HTMLBody': 'HTML body content',
    'ItemCodeBid': 'Item code on bid submission',
    'ItemDescriptionBid': 'Item description on bid',
    'LastSent': 'Last sent timestamp',
    'LinkedDocId': 'Linked document ID',
    'ManufacturerBid': 'Manufacturer on bid submission',
    'ManufPartNoBid': 'Manufacturer part number on bid',
    'MatchCode': 'Matching code for deduplication',
    'MessageText': 'Message text content',
    'NotificationSent': 'Flag: notification has been sent',
    'OriginalFileName': 'Original uploaded file name',
    'PDFFile': 'PDF file reference',
    'PhoneExt': 'Phone extension number',
    'PlainTextBody': 'Plain text body content',
    'PONumber': 'Purchase order number',
    'PrintSeq': 'Print sequence order',
    'ProcessedDate': 'Date processed',
    'QuantityOrdered': 'Quantity ordered',
    'QuantityReceived': 'Quantity received',
    'QuantityShipped': 'Quantity shipped',
    'RecordCount': 'Number of records',
    'ReplyTo': 'Reply-to email address',
    'RowNumber': 'Row number in sequence',
    'RunDate': 'Execution/run date',
    'SchoolAddress1': 'School primary address',
    'SchoolAddress2': 'School secondary address',
    'SchoolName': 'School name',
    'SendTo': 'Recipient email address',
    'ShipToAddress1': 'Ship-to primary address',
    'ShipToAddress2': 'Ship-to secondary address',
    'ShipToCity': 'Ship-to city',
    'ShipToName': 'Ship-to recipient name',
    'ShipToState': 'Ship-to state',
    'ShipToZip': 'Ship-to ZIP code',
    'SortOrder': 'Sort order sequence',
    'SourceTable': 'Source table name',
    'StatusMessage': 'Status message text',
    'SubjectLine': 'Email subject line',
    'TableName': 'Table name reference',
    'TextBody': 'Text body content',
    'ToEmailAddress': 'Recipient email address',
    'TotalAmount': 'Total amount',
    'TotalCount': 'Total count',
    'TotalRecords': 'Total number of records',
    'UnitPriceBid': 'Unit price on bid',
    'UpdateDate': 'Last update date',
    'UploadDate': 'Upload date',
    'UserEmail': 'User email address',
    'UserPhone': 'User phone number',
    'VendorAddress1': 'Vendor primary address',
    'VendorAddress2': 'Vendor secondary address',
    'VendorAddress3': 'Vendor third address',
    'VendorCity': 'Vendor city',
    'VendorContactName': 'Vendor contact person name',
    'VendorEmail': 'Vendor email address',
    'VendorFax': 'Vendor fax number',
    'VendorPhone': 'Vendor phone number',
    'VendorState': 'Vendor state',
    'VendorZipcode': 'Vendor ZIP code',
    'XMLData': 'XML data content',
}

# Table-specific column descriptions
TABLE_SPECIFIC_DESCRIPTIONS = {
    # District table
    'District.AccountingSystemOptions': 'Accounting system configuration options',
    'District.AccountSeparator': 'Character separator for account codes',
    'District.AnnualPOGenerationMethod': 'Method for annual PO generation',
    'District.CooperativeBids': 'Flag: participates in cooperative bids',
    'District.DisableLogins': 'Flag: user logins disabled',
    'District.DoNotShipCatalogs': 'Flag: do not ship physical catalogs',
    'District.DRsbySchool': 'Flag: delivery receipts by school',
    'District.FixedPOMsg': 'Fixed message on purchase orders',
    'District.GroupByBudgetCode': 'Flag: group items by budget code',
    'District.GroupByCategory': 'Flag: group items by category',
    'District.GroupByVendor': 'Flag: group items by vendor',
    'District.HideInactiveBudgets': 'Flag: hide inactive budget codes',
    'District.HideItemsWithNoBid': 'Flag: hide items without bids',
    'District.HidePricesFromBidders': 'Flag: hide prices from bidders',
    'District.InactivateHold': 'Flag: inactivate items on hold',
    'District.LimitPOAmounts': 'Flag: enforce PO amount limits',
    'District.MaxPOAmount': 'Maximum allowed PO amount',
    'District.MinPOAmount': 'Minimum required PO amount',
    'District.POPrefix': 'Prefix for PO numbers',
    'District.RequireBudgetCode': 'Flag: budget code required',

    # Vendors table (cXML fields)
    'Vendors.BusinessUnit': 'Business unit identifier',
    'Vendors.cXMLFromDomain': 'cXML sender from domain',
    'Vendors.cXMLFromIdentity': 'cXML sender from identity',
    'Vendors.cXMLSenderDomain': 'cXML sender domain',
    'Vendors.cXMLSenderIdentity': 'cXML sender identity',
    'Vendors.cXMLSenderSharedSecret': 'cXML sender shared secret (encrypted)',
    'Vendors.cXMLToDomain': 'cXML recipient to domain',
    'Vendors.cXMLToIdentity': 'cXML recipient to identity',
    'Vendors.EDICapable': 'Flag: vendor supports EDI',
    'Vendors.PunchoutEnabled': 'Flag: punchout catalog enabled',
    'Vendors.PunchoutURL': 'Punchout catalog URL',
    'Vendors.SupplierANSId': 'Supplier ANSI identifier',
    'Vendors.SupplierDUNS': 'Supplier DUNS number',
    'Vendors.TaxExempt': 'Flag: vendor is tax exempt',
    'Vendors.W9OnFile': 'Flag: W-9 form on file',
    'Vendors.InsuranceOnFile': 'Flag: insurance certificate on file',
    'Vendors.MinorityOwned': 'Flag: minority-owned business',
    'Vendors.WomanOwned': 'Flag: woman-owned business',

    # Catalog table
    'Catalog.BeginDefault': 'Default beginning value',
    'Catalog.CrossRefLetter': 'Cross reference letter code',
    'Catalog.NotValidForOB': 'Flag: not valid for order book',
    'Catalog.PackExp': 'Package expression for parsing',
    'Catalog.PackReplace': 'Package replacement string',
    'Catalog.Page1': 'Starting page number',
    'Catalog.PDFAvailable': 'Flag: PDF catalog available',
    'Catalog.pdfDirectory': 'PDF file directory path',

    # Images table
    'Images.channels': 'Number of color channels',
    'Images.density': 'Image density (DPI)',
    'Images.depth': 'Color depth in bits',
    'Images.height': 'Image height in pixels',
    'Images.imageResized': 'Resized image binary data',
    'Images.imageSpace': 'Color space (RGB, CMYK, etc.)',
    'Images.imageThumbnail': 'Thumbnail image binary data',
    'Images.width': 'Image width in pixels',

    # Batches table
    'Batches.Amount': 'Batch total amount',
    'Batches.Converted': 'Flag: batch has been converted',
    'Batches.Imported': 'Flag: batch has been imported',
    'Batches.ImportedRecords': 'Number of imported records',
    'Batches.InputRecords': 'Number of input records',
    'Batches.Loaded': 'Flag: batch has been loaded',
    'Batches.Scheduled': 'Flag: batch is scheduled',

    # BidMSRPResults table
    'BidMSRPResults.AuthorizationLetter': 'Authorization letter document',
    'BidMSRPResults.DiscountRateString': 'Discount rate as text string',
    'BidMSRPResults.ExcelFileApproved': 'Flag: Excel file approved',
    'BidMSRPResults.ProductCatalog': 'Product catalog reference',
    'BidMSRPResults.SubmittedExcel': 'Submitted Excel file data',
    'BidMSRPResults.WinningBidOverride': 'Flag: winning bid manually overridden',
    'BidMSRPResults.WriteInManufacturer': 'Write-in manufacturer name',

    # BidHeaders table
    'BidHeaders.AwardMsg': 'Award notification message',
    'BidHeaders.BudgetYearOption': 'Budget year selection option',
    'BidHeaders.CompliantAlert': 'Compliance alert message',
    'BidHeaders.ImageURLRuleset': 'Rules for image URL validation',
    'BidHeaders.MarkAsOriginal': 'Flag: mark as original bid',
    'BidHeaders.ScheduledReaward': 'Scheduled re-award date',
    'BidHeaders.UpdateHold': 'Flag: updates on hold',

    # BidQuestions table
    'BidQuestions.AnswerPositionX': 'Answer X position on form',
    'BidQuestions.AnswerPositionY': 'Answer Y position on form',
    'BidQuestions.AnswerTypeMask': 'Bitmask for answer types',
    'BidQuestions.BidSection': 'Bid document section',
    'BidQuestions.ExtdCalcMask': 'Extended calculation bitmask',
    'BidQuestions.ExtendCalculation': 'Extended calculation formula',
    'BidQuestions.OnChecklist': 'Flag: appears on checklist',
    'BidQuestions.QuestionPositionX': 'Question X position on form',
    'BidQuestions.QuestionPositionY': 'Question Y position on form',

    # CXmlSession table
    'CXmlSession.BrowserFormPost': 'Browser form post data',
    'CXmlSession.buyerCookie': 'Buyer session cookie',
    'CXmlSession.fromDomain': 'cXML from domain',
    'CXmlSession.fromIdentity': 'cXML from identity',
    'CXmlSession.fromUserAgent': 'HTTP user agent string',
    'CXmlSession.senderDomain': 'cXML sender domain',
    'CXmlSession.senderIdentity': 'cXML sender identity',
    'CXmlSession.toDomain': 'cXML to domain',
    'CXmlSession.toIdentity': 'cXML to identity',

    # Users table
    'Users.allowMSRP': 'Flag: allow MSRP pricing access',
    'Users.DisableNewRequisition': 'Flag: disable new requisition creation',
    'Users.PasswordOld': 'Previous password (encrypted)',
    'Users.POAccess': 'PO access level',
    'Users.ResetPasswordCodeExpiration': 'Password reset code expiration time',

    # VendorContacts table
    'VendorContacts.ARContact': 'Flag: accounts receivable contact',
    'VendorContacts.BidContact': 'Flag: bid/sales contact',
    'VendorContacts.CSContact': 'Flag: customer service contact',
    'VendorContacts.FreightContact': 'Flag: freight/shipping contact',
    'VendorContacts.POContact': 'Flag: purchase order contact',

    # BidderCheckList table
    'BidderCheckList.AdditionalInfoRTF': 'Additional info in RTF format',
    'BidderCheckList.DocNumberReqd': 'Flag: document number required',
    'BidderCheckList.ExpirationDateReqd': 'Flag: expiration date required',
    'BidderCheckList.OnFileEligible': 'Flag: eligible for on-file status',
    'BidderCheckList.UploadEligible': 'Flag: eligible for upload',

    # SDSResults table
    'SDSResults.DocumentURLError': 'Error with document URL',
    'SDSResults.ElasticError': 'Elasticsearch error message',
    'SDSResults.SDSCacheError': 'SDS cache error message',
    'SDSResults.SDSURLError': 'SDS URL error message',
    'SDSResults.ValidCache': 'Flag: cache is valid',
    'SDSResults.ValidSDSUrl': 'Flag: SDS URL is valid',

    # TaskSchedule table
    'TaskSchedule.EndDateActual': 'Actual end date',
    'TaskSchedule.EndDateOrig': 'Original planned end date',
    'TaskSchedule.EndDateProjected': 'Projected end date',
    'TaskSchedule.StartDateActual': 'Actual start date',
    'TaskSchedule.StartDateOrig': 'Original planned start date',
    'TaskSchedule.StartDateProjected': 'Projected start date',

    # POLayoutDetail table
    'POLayoutDetail.HorizontalPos': 'Horizontal position on layout',
    'POLayoutDetail.Image': 'Image element reference',
    'POLayoutDetail.Literal': 'Literal text content',
    'POLayoutDetail.PrintWhen': 'Condition for printing',
    'POLayoutDetail.VerticalPos': 'Vertical position on layout',
    'POLayoutDetail.WrapAround': 'Flag: text wrap enabled',

    # Imports table
    'Imports.CatalogId1': 'First catalog ID mapping',
    'Imports.CatalogId2': 'Second catalog ID mapping',
    'Imports.CatalogId3': 'Third catalog ID mapping',
    'Imports.CatalogId4': 'Fourth catalog ID mapping',
    'Imports.CatalogId5': 'Fifth catalog ID mapping',
    'Imports.CatalogId6': 'Sixth catalog ID mapping',

    # RTK_Sites table
    'RTK_Sites.EmailResponsibleOfficial': 'Responsible official email',
    'RTK_Sites.FacilityEmergencyContact': 'Emergency contact for facility',
    'RTK_Sites.FacilityLocation1': 'Facility location line 1',
    'RTK_Sites.FacilityLocation2': 'Facility location line 2',
    'RTK_Sites.FacilityLocation3': 'Facility location line 3',
    'RTK_Sites.FacilityLocation4': 'Facility location line 4',
    'RTK_Sites.MailingAddress1': 'Mailing address line 1',
    'RTK_Sites.MailingAddress2': 'Mailing address line 2',
    'RTK_Sites.MailingCity': 'Mailing city',
    'RTK_Sites.MailingState': 'Mailing state',
    'RTK_Sites.MailingZip': 'Mailing ZIP code',
    'RTK_Sites.ResponsibleOfficialName': 'Name of responsible official',
    'RTK_Sites.ResponsibleOfficialTitle': 'Title of responsible official',

    # RTK_CASFile table (Chemical data)
    'RTK_CASFile.Carcinogen': 'Flag: substance is carcinogen',
    'RTK_CASFile.CompoundContaining': 'Compounds containing this substance',
    'RTK_CASFile.Corrosive': 'Flag: substance is corrosive',
    'RTK_CASFile.F3_Flammable3rd': 'Flammability rating level 3',
    'RTK_CASFile.F4_Flammable4th': 'Flammability rating level 4',
    'RTK_CASFile.Mutagen': 'Flag: substance is mutagen',
    'RTK_CASFile.R2_Reactive2nd': 'Reactivity rating level 2',
    'RTK_CASFile.R3_Reactive3rd': 'Reactivity rating level 3',
    'RTK_CASFile.R4_Reactive4th': 'Reactivity rating level 4',
    'RTK_CASFile.Teratogen': 'Flag: substance is teratogen',
    'RTK_CASFile.ToxicByIngestion': 'Flag: toxic by ingestion',
    'RTK_CASFile.ToxicByInhalation': 'Flag: toxic by inhalation',

    # QuestionnaireResponses table
    'QuestionnaireResponses.districtid': 'District identifier',
    'QuestionnaireResponses.qr1': 'Response to question 1',
    'QuestionnaireResponses.qr2': 'Response to question 2',
    'QuestionnaireResponses.qr3': 'Response to question 3',
    'QuestionnaireResponses.qr4': 'Response to question 4',
    'QuestionnaireResponses.qr5': 'Response to question 5',
    'QuestionnaireResponses.qr6': 'Response to question 6',
    'QuestionnaireResponses.qr7': 'Response to question 7',
    'QuestionnaireResponses.qr8': 'Response to question 8',
    'QuestionnaireResponses.qr9': 'Response to question 9',
    'QuestionnaireResponses.qr10': 'Response to question 10',
}


def add_column_descriptions(database='EDS'):
    """Add descriptions to remaining undocumented columns."""

    logger = setup_logging('add_column_descriptions_v3')
    logger.info(f"Adding column descriptions for {database} (v3 - final pass)")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get undocumented columns from dbo schema
    undoc_cols = db.execute_query('''
        SELECT
            t.name AS TableName,
            c.name AS ColumnName
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
        # Check table-specific first
        table_key = f'{table}.{column}'
        desc = TABLE_SPECIFIC_DESCRIPTIONS.get(table_key)

        # Then check multi-table descriptions
        if not desc:
            desc = MULTI_TABLE_DESCRIPTIONS.get(column)

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


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Add column descriptions v3')
    parser.add_argument('--database', '-d', default='EDS', help='Database name')

    args = parser.parse_args()

    try:
        add_column_descriptions(database=args.database)
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()
