#!/usr/bin/env python3
"""
Add Column Descriptions to EDS Database - Version 2

Expanded coverage for remaining undocumented columns.
"""

import os
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Exact column name matches
EXACT_DESCRIPTIONS = {
    # Common fields
    'Fax': 'Fax number',
    'Id': 'Unique identifier',
    'Title': 'Title or heading text',
    'Attention': 'Attention line for correspondence',
    'EMail': 'Email address',
    'Email': 'Email address',
    'Address1': 'Primary street address line',
    'Address2': 'Secondary street address line',
    'Address3': 'Third address line (suite, building)',
    'County': 'County name',
    'CountyId': 'Foreign key to Counties table',
    'Created': 'Record creation timestamp',
    'Updated': 'Record last update timestamp',
    'Deleted': 'Soft delete flag or deletion timestamp',
    'Level': 'Hierarchy or permission level',
    'Type': 'Record type or category',
    'Package': 'Package or bundle identifier',
    'Category': 'Category classification',
    'Action': 'Action performed or action type',
    'Frequency': 'Frequency of occurrence',
    'Manufacturer': 'Manufacturer name',
    'Priority': 'Priority level (1=highest)',
    'Sequence': 'Display or processing sequence',
    'Version': 'Version number',
    'Revision': 'Revision number',
    'Notes': 'Additional notes or comments',
    'Message': 'Message text content',
    'Subject': 'Subject line or title',
    'Body': 'Body content or message text',
    'Summary': 'Summary text',
    'Remarks': 'Remarks or observations',
    'Reference': 'Reference number or identifier',
    'Source': 'Data source identifier',
    'Target': 'Target destination or entity',
    'Value': 'Stored value',
    'Result': 'Result or outcome',
    'Response': 'Response text or code',
    'Request': 'Request text or identifier',
    'Reason': 'Reason code or description',
    'Exception': 'Exception or error details',
    'Error': 'Error message or code',
    'Warning': 'Warning message',
    'Info': 'Information text',
    'Label': 'Display label text',
    'Tag': 'Tag or label identifier',
    'Group': 'Group classification',
    'Class': 'Class or category',
    'Section': 'Section identifier',
    'Segment': 'Segment identifier',
    'Region': 'Geographic region',
    'Zone': 'Zone or area identifier',
    'Area': 'Area designation',
    'Location': 'Location description',
    'Position': 'Position or rank',
    'Rank': 'Ranking position',
    'Order': 'Sort order or sequence',
    'Index': 'Index position',
    'Offset': 'Offset value',
    'Size': 'Size measurement',
    'Length': 'Length measurement',
    'Width': 'Width measurement',
    'Height': 'Height measurement',
    'Depth': 'Depth measurement',
    'Volume': 'Volume measurement',
    'Capacity': 'Capacity amount',
    'Limit': 'Maximum limit value',
    'Threshold': 'Threshold value',
    'Minimum': 'Minimum value',
    'Maximum': 'Maximum value',
    'Average': 'Average value',
    'Total': 'Total amount',
    'Subtotal': 'Subtotal amount',
    'Balance': 'Balance amount',
    'Rate': 'Rate or percentage',
    'Ratio': 'Ratio value',
    'Factor': 'Multiplier factor',
    'Percent': 'Percentage value',
    'Percentage': 'Percentage value',
    'Discount': 'Discount amount or percentage',
    'Markup': 'Markup percentage',
    'Margin': 'Margin percentage',
    'Tax': 'Tax amount',
    'Fee': 'Fee amount',
    'Charge': 'Charge amount',
    'Credit': 'Credit amount',
    'Debit': 'Debit amount',
    'Payment': 'Payment amount',
    'Deposit': 'Deposit amount',
    'Refund': 'Refund amount',
    'Adjustment': 'Adjustment amount',
    'Variance': 'Variance from expected',
    'Difference': 'Difference amount',
    'Change': 'Change amount',
    'Delta': 'Delta/change value',
    'Count': 'Count or quantity',
    'Qty': 'Quantity',
    'Quantity': 'Quantity amount',
    'Units': 'Number of units',
    'Pieces': 'Number of pieces',
    'Days': 'Number of days',
    'Hours': 'Number of hours',
    'Minutes': 'Number of minutes',
    'Months': 'Number of months',
    'Years': 'Number of years',
    'Duration': 'Duration in time units',
    'Interval': 'Time interval',
    'Period': 'Time period',
    'Term': 'Term or duration',
    'Cycle': 'Cycle number or period',
    'Round': 'Round number',
    'Attempt': 'Attempt number',
    'Retry': 'Retry count',
    'Tries': 'Number of tries',
    'Success': 'Success flag or count',
    'Failure': 'Failure flag or count',
    'Score': 'Score value',
    'Rating': 'Rating value',
    'Grade': 'Grade or classification',
    'Tier': 'Tier level',
    'Enabled': 'Feature enabled flag (1=enabled)',
    'Disabled': 'Feature disabled flag (1=disabled)',
    'Locked': 'Lock status (1=locked)',
    'Visible': 'Visibility flag (1=visible)',
    'Hidden': 'Hidden flag (1=hidden)',
    'Public': 'Public visibility flag',
    'Private': 'Private flag',
    'Required': 'Required field flag',
    'Optional': 'Optional field flag',
    'Default': 'Default value flag',
    'Custom': 'Custom/user-defined flag',
    'System': 'System-generated flag',
    'Manual': 'Manually entered flag',
    'Auto': 'Auto-generated flag',
    'Approved': 'Approval status (1=approved)',
    'Rejected': 'Rejection status (1=rejected)',
    'Pending': 'Pending status (1=pending)',
    'Complete': 'Completion status (1=complete)',
    'Completed': 'Completion status (1=completed)',
    'Processing': 'Processing status flag',
    'Processed': 'Processed status (1=processed)',
    'Submitted': 'Submission status (1=submitted)',
    'Cancelled': 'Cancellation status (1=cancelled)',
    'Canceled': 'Cancellation status (1=canceled)',
    'Expired': 'Expiration status (1=expired)',
    'Valid': 'Validity flag (1=valid)',
    'Invalid': 'Invalid flag (1=invalid)',
    'Verified': 'Verification status (1=verified)',
    'Confirmed': 'Confirmation status (1=confirmed)',
    'Sent': 'Sent status (1=sent)',
    'Received': 'Received status (1=received)',
    'Read': 'Read status (1=read)',
    'Opened': 'Opened status (1=opened)',
    'Closed': 'Closed status (1=closed)',
    'Open': 'Open status (1=open)',
    'New': 'New status flag',
    'Old': 'Old/legacy flag',
    'Current': 'Current/active flag',
    'Previous': 'Previous value or status',
    'Next': 'Next value or sequence',
    'First': 'First in sequence flag',
    'Last': 'Last in sequence flag',
    'Latest': 'Latest/most recent flag',
    'Original': 'Original value',
    'Modified': 'Modification timestamp or flag',
    'Changed': 'Changed flag',
    'Dirty': 'Dirty/unsaved flag',
    'Clean': 'Clean/saved flag',
    'Sync': 'Synchronization status',
    'Synced': 'Synced status (1=synced)',

    # Date/Time specific
    'SendDate': 'Date sent',
    'AddDate': 'Date added',
    'DateModified': 'Date last modified',
    'DateCreated': 'Date created',
    'StatusDate': 'Date of status change',
    'ChangeDate': 'Date of change',
    'FollowUpDate': 'Follow-up date',
    'EffectiveFrom': 'Effective start date',
    'EffectiveUntil': 'Effective end date',
    'EffectiveDate': 'Effective date',
    'ExpirationDate': 'Expiration date',
    'ExpireDate': 'Expiration date',
    'StartDate': 'Start date',
    'EndDate': 'End date',
    'DueDate': 'Due date',
    'ClosedDate': 'Date closed',
    'OpenedDate': 'Date opened',
    'PostDate': 'Posting date',
    'PostedDate': 'Date posted',
    'EntryDate': 'Entry date',
    'RecordDate': 'Record date',
    'TransactionDate': 'Transaction date',
    'OrderDate': 'Order date',
    'ShipDate': 'Ship date',
    'DeliveryDate': 'Delivery date',
    'ReceiveDate': 'Receive date',
    'ReceivedDate': 'Date received',
    'InvoiceDate': 'Invoice date',
    'PaymentDate': 'Payment date',
    'ApprovalDate': 'Approval date',
    'ApprovedDate': 'Date approved',
    'SubmitDate': 'Submission date',
    'SubmittedDate': 'Date submitted',
    'ReviewDate': 'Review date',
    'LastLogin': 'Last login timestamp',
    'LastAccess': 'Last access timestamp',
    'LastActivity': 'Last activity timestamp',
    'LastUpdate': 'Last update timestamp',
    'LastModified': 'Last modified timestamp',
    'CreatedAt': 'Creation timestamp',
    'UpdatedAt': 'Update timestamp',
    'DeletedAt': 'Deletion timestamp',
    'Timestamp': 'Record timestamp',

    # ID/Key fields
    'ShippingId': 'Shipping method or record ID',
    'ApprovalLevel': 'Approval level number',
    'CometId': 'Comet system reference ID',
    'TMImportId': 'TM Import batch ID',
    'DocId': 'Document unique identifier',
    'DocType': 'Document type code',
    'IBTypeId': 'Instruction book type ID',
    'ApproverId': 'Approver user ID',
    'BidTradeCountyId': 'Bid trade county reference ID',
    'DocumentId': 'Document unique identifier',
    'RequisitionId': 'Requisition reference ID',
    'RegistrationId': 'Registration reference ID',
    'TransactionId': 'Transaction reference ID',
    'OrderId': 'Order reference ID',
    'InvoiceId': 'Invoice reference ID',
    'PaymentId': 'Payment reference ID',
    'AccountId': 'Account reference ID',
    'ContactId': 'Contact reference ID',
    'AddressId': 'Address reference ID',
    'LocationId': 'Location reference ID',
    'DepartmentId': 'Department reference ID',
    'SchoolId': 'School reference ID',
    'ClassId': 'Class reference ID',
    'CourseId': 'Course reference ID',
    'StudentId': 'Student reference ID',
    'TeacherId': 'Teacher reference ID',
    'EmployeeId': 'Employee reference ID',
    'CustomerId': 'Customer reference ID',
    'SupplierId': 'Supplier reference ID',
    'ProductId': 'Product reference ID',
    'ServiceId': 'Service reference ID',
    'ProjectId': 'Project reference ID',
    'TaskId': 'Task reference ID',
    'JobId': 'Job reference ID',
    'BatchId': 'Batch reference ID',
    'GroupId': 'Group reference ID',
    'TeamId': 'Team reference ID',
    'RoleId': 'Role reference ID',
    'PermissionId': 'Permission reference ID',
    'ProfileId': 'Profile reference ID',
    'SettingId': 'Setting reference ID',
    'ConfigId': 'Configuration reference ID',
    'TemplateId': 'Template reference ID',
    'FormId': 'Form reference ID',
    'ReportId': 'Report reference ID',
    'FileId': 'File reference ID',
    'ImageId': 'Image reference ID',
    'AttachmentId': 'Attachment reference ID',
    'CommentId': 'Comment reference ID',
    'NoteId': 'Note reference ID',
    'MessageId': 'Message reference ID',
    'NotificationId': 'Notification reference ID',
    'AlertId': 'Alert reference ID',
    'EventId': 'Event reference ID',
    'LogId': 'Log entry reference ID',
    'AuditId': 'Audit record reference ID',
    'HistoryId': 'History record reference ID',
    'VersionId': 'Version reference ID',
    'RevisionId': 'Revision reference ID',

    # Business-specific
    'MessageContent': 'Message body content',
    'MessageReceiptConfirmed': 'Flag: message receipt confirmed',
    'ResolvedFlag': 'Flag: issue resolved (1=resolved)',
    'UseOptions': 'Flag: use optional features',
    'AllowAddenda': 'Flag: allow bid addenda',
    'DisplaySequence': 'Display order sequence number',
    'DistrictVisible': 'Flag: visible to district',
    'DocumentType': 'Type of document',
    'NotificationType': 'Type of notification',
    'PagesCaptured': 'Number of pages captured/scanned',
    'RangeBase': 'Base value for range calculation',
    'EmailAddress2': 'Secondary email address',
    'Zipcode': 'ZIP/postal code',
    'ZipCode': 'ZIP/postal code',

    # Vendor fields
    'VendorName': 'Vendor company name',
    'VendorCode': 'Vendor identifier code',
    'VendorNumber': 'Vendor account number',
    'VendorType': 'Vendor classification type',
    'VendorStatus': 'Vendor status code',
    'VendorEmail': 'Vendor email address',
    'VendorPhone': 'Vendor phone number',
    'VendorFax': 'Vendor fax number',
    'VendorContact': 'Vendor contact person',
    'VendorAddress': 'Vendor street address',
    'VendorCity': 'Vendor city',
    'VendorState': 'Vendor state/province',
    'VendorZip': 'Vendor ZIP code',

    # Bid fields
    'BidNumber': 'Bid identification number',
    'BidName': 'Bid/solicitation name',
    'BidTitle': 'Bid title',
    'BidDescription': 'Bid description text',
    'BidStatus': 'Current bid status',
    'BidType': 'Type of bid/solicitation',
    'BidDate': 'Bid date',
    'BidAmount': 'Bid amount',
    'BidPrice': 'Bid price',
    'BidQuantity': 'Bid quantity',
    'BidUnit': 'Bid unit of measure',
    'BidComments': 'Bid comments',
    'BidNotes': 'Bid notes',

    # Item fields
    'ItemNumber': 'Item identification number',
    'ItemName': 'Item name',
    'ItemDescription': 'Item description',
    'ItemCode': 'Item code',
    'ItemType': 'Item type classification',
    'ItemStatus': 'Item status',
    'ItemPrice': 'Item price',
    'ItemCost': 'Item cost',
    'ItemQuantity': 'Item quantity',
    'ItemUnit': 'Item unit of measure',

    # District fields
    'DistrictName': 'District name',
    'DistrictCode': 'District code',
    'DistrictNumber': 'District number',
    'DistrictType': 'District type',

    # User fields
    'UserName': 'User login name',
    'Username': 'User login name',
    'FirstName': 'First name',
    'LastName': 'Last name',
    'MiddleName': 'Middle name',
    'FullName': 'Full name',
    'DisplayName': 'Display name',
    'NickName': 'Nickname',
    'Prefix': 'Name prefix (Mr., Mrs., etc.)',
    'Suffix': 'Name suffix (Jr., Sr., etc.)',
    'Salutation': 'Salutation text',
    'JobTitle': 'Job title',
    'Department': 'Department name',
    'Division': 'Division name',
    'Company': 'Company name',
    'Organization': 'Organization name',

    # Contact fields
    'Phone1': 'Primary phone number',
    'Phone2': 'Secondary phone number',
    'HomePhone': 'Home phone number',
    'WorkPhone': 'Work phone number',
    'MobilePhone': 'Mobile phone number',
    'CellPhone': 'Cell phone number',
    'Fax1': 'Primary fax number',
    'Fax2': 'Secondary fax number',
    'Website': 'Website URL',
    'WebSite': 'Website URL',
    'URL': 'URL address',

    # Status fields
    'StatusId': 'Status reference ID',
    'StatusCode': 'Status code',
    'StatusName': 'Status name',
    'StatusDescription': 'Status description',

    # Additional common fields
    'Remarks': 'Additional remarks',
    'Instructions': 'Instructions text',
    'Terms': 'Terms and conditions',
    'Conditions': 'Conditions text',
    'Policy': 'Policy text',
    'Agreement': 'Agreement text',
    'Contract': 'Contract reference',
    'License': 'License information',
    'Certificate': 'Certificate information',
    'Certification': 'Certification details',
    'Qualification': 'Qualification details',
    'Specification': 'Specification details',
    'Requirement': 'Requirement details',
    'Criteria': 'Criteria details',
    'Standard': 'Standard reference',
    'Compliance': 'Compliance status',
    'Regulation': 'Regulation reference',
    'Classification': 'Classification code',
    'Categorization': 'Categorization details',
}

# Suffix patterns (applied if no exact match)
SUFFIX_PATTERNS = {
    'Id': 'Reference identifier',
    'ID': 'Reference identifier',
    'Key': 'Unique key identifier',
    'Code': 'Code value',
    'Number': 'Number value',
    'No': 'Number value',
    'Nbr': 'Number value',
    'Num': 'Number value',
    'Name': 'Name value',
    'Desc': 'Description text',
    'Description': 'Description text',
    'Text': 'Text content',
    'Value': 'Value',
    'Amount': 'Amount value',
    'Price': 'Price value',
    'Cost': 'Cost value',
    'Rate': 'Rate value',
    'Pct': 'Percentage value',
    'Percent': 'Percentage value',
    'Count': 'Count value',
    'Qty': 'Quantity value',
    'Quantity': 'Quantity value',
    'Total': 'Total value',
    'Sum': 'Sum total',
    'Avg': 'Average value',
    'Min': 'Minimum value',
    'Max': 'Maximum value',
    'Date': 'Date value',
    'Time': 'Time value',
    'DateTime': 'Date and time value',
    'Timestamp': 'Timestamp value',
    'Start': 'Start value',
    'End': 'End value',
    'From': 'From/start value',
    'To': 'To/end value',
    'By': 'By user or reference',
    'At': 'At timestamp or location',
    'On': 'On date or condition',
    'Flag': 'Boolean flag (1=true, 0=false)',
    'Indicator': 'Indicator flag',
    'Status': 'Status value',
    'State': 'State value',
    'Type': 'Type classification',
    'Kind': 'Kind/type value',
    'Mode': 'Mode setting',
    'Level': 'Level value',
    'Tier': 'Tier level',
    'Rank': 'Rank value',
    'Order': 'Order/sequence value',
    'Seq': 'Sequence number',
    'Sequence': 'Sequence number',
    'Index': 'Index value',
    'Position': 'Position value',
    'Priority': 'Priority value',
    'Weight': 'Weight value',
    'Score': 'Score value',
    'Rating': 'Rating value',
    'Grade': 'Grade value',
    'Size': 'Size value',
    'Length': 'Length value',
    'Width': 'Width value',
    'Height': 'Height value',
    'Depth': 'Depth value',
    'Color': 'Color value',
    'Style': 'Style value',
    'Format': 'Format specification',
    'Pattern': 'Pattern value',
    'Template': 'Template reference',
    'Path': 'File or URL path',
    'URL': 'URL address',
    'Uri': 'URI address',
    'Link': 'Link URL or reference',
    'File': 'File reference',
    'Image': 'Image reference',
    'Icon': 'Icon reference',
    'Logo': 'Logo reference',
    'Photo': 'Photo reference',
    'Picture': 'Picture reference',
    'Attachment': 'Attachment reference',
    'Document': 'Document reference',
    'Report': 'Report reference',
    'Message': 'Message content',
    'Comment': 'Comment text',
    'Note': 'Note text',
    'Remark': 'Remark text',
    'Label': 'Label text',
    'Title': 'Title text',
    'Header': 'Header text',
    'Footer': 'Footer text',
    'Subject': 'Subject text',
    'Body': 'Body content',
    'Content': 'Content text',
    'Html': 'HTML content',
    'Json': 'JSON data',
    'Xml': 'XML data',
    'Data': 'Data content',
    'Blob': 'Binary large object',
    'Hash': 'Hash value',
    'Token': 'Token value',
    'Guid': 'GUID identifier',
    'Uuid': 'UUID identifier',
}

# Prefix patterns
PREFIX_PATTERNS = {
    'Is': 'Boolean flag: ',
    'Has': 'Boolean flag: has ',
    'Can': 'Boolean flag: can ',
    'Allow': 'Boolean flag: allow ',
    'Enable': 'Boolean flag: enable ',
    'Show': 'Boolean flag: show ',
    'Hide': 'Boolean flag: hide ',
    'Include': 'Boolean flag: include ',
    'Exclude': 'Boolean flag: exclude ',
    'Use': 'Boolean flag: use ',
    'Require': 'Boolean flag: require ',
    'Need': 'Boolean flag: need ',
    'Want': 'Boolean flag: want ',
    'Default': 'Default value for ',
    'Original': 'Original value of ',
    'Previous': 'Previous value of ',
    'Current': 'Current value of ',
    'New': 'New value of ',
    'Old': 'Old/legacy value of ',
    'Last': 'Last/most recent ',
    'First': 'First ',
    'Min': 'Minimum ',
    'Max': 'Maximum ',
    'Total': 'Total ',
    'Sum': 'Sum of ',
    'Avg': 'Average ',
    'Count': 'Count of ',
    'Num': 'Number of ',
}


def get_description(column_name):
    """Get description for a column based on name patterns."""

    # Check exact match first
    if column_name in EXACT_DESCRIPTIONS:
        return EXACT_DESCRIPTIONS[column_name]

    # Check prefix patterns
    for prefix, desc_prefix in PREFIX_PATTERNS.items():
        if column_name.startswith(prefix) and len(column_name) > len(prefix):
            remainder = column_name[len(prefix):]
            # Convert camelCase to readable
            readable = re.sub(r'([A-Z])', r' \1', remainder).strip().lower()
            return f'{desc_prefix}{readable}'

    # Check suffix patterns
    for suffix, desc in SUFFIX_PATTERNS.items():
        if column_name.endswith(suffix) and len(column_name) > len(suffix):
            prefix_part = column_name[:-len(suffix)]
            # Convert camelCase to readable
            readable = re.sub(r'([A-Z])', r' \1', prefix_part).strip()
            if readable:
                return f'{readable} {desc.lower()}'
            return desc

    return None


def add_column_descriptions(database='EDS'):
    """Add descriptions to undocumented columns."""

    logger = setup_logging('add_column_descriptions_v2')
    logger.info(f"Adding column descriptions for {database} (v2)")

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
        desc = get_description(column)
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
            if success % 200 == 0:
                logger.info(f"  Applied {success} descriptions...")
        except Exception as e:
            errors += 1
            if errors <= 5:
                logger.warning(f"Error on {table}.{column}: {str(e)[:50]}")

    db.disconnect()

    logger.info(f"[OK] Column descriptions added: {success}")
    logger.info(f"  Columns without matching pattern: {skipped}")
    logger.info(f"  Errors: {errors}")

    print(f"\nColumn descriptions added: {success}")
    print(f"Columns without matching pattern: {skipped}")
    print(f"Errors: {errors}")

    return success


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Add column descriptions v2')
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
