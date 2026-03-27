#!/usr/bin/env python3
"""
Document Remaining Columns

Final pass to document any remaining undocumented columns in tables and views.
Uses aggressive pattern matching and context-aware descriptions.
"""

import os
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Additional column descriptions for remaining undocumented columns
ADDITIONAL_DESCRIPTIONS = {
    # Numeric/ID patterns
    'Seq': 'Sequence number',
    'Num': 'Number value',
    'Cnt': 'Count value',
    'Amt': 'Amount value',
    'Qty': 'Quantity value',
    'Pct': 'Percentage value',
    'Rate': 'Rate value',
    'Factor': 'Factor/multiplier value',
    'Ratio': 'Ratio value',
    'Index': 'Index value',
    'Level': 'Level indicator',
    'Rank': 'Rank/priority value',
    'Order': 'Sort order value',
    'Position': 'Position value',
    'Priority': 'Priority level',
    'Weight': 'Weight/importance value',
    'Score': 'Score value',
    'Points': 'Points value',
    'Count': 'Count value',
    'Total': 'Total value',
    'Sum': 'Sum value',
    'Avg': 'Average value',
    'Min': 'Minimum value',
    'Max': 'Maximum value',

    # Text patterns
    'Desc': 'Description text',
    'Name': 'Name value',
    'Title': 'Title text',
    'Label': 'Label text',
    'Caption': 'Caption text',
    'Text': 'Text content',
    'Msg': 'Message text',
    'Note': 'Note/comment text',
    'Comment': 'Comment text',
    'Remark': 'Remark text',
    'Memo': 'Memo text',
    'Info': 'Information text',
    'Detail': 'Detail text',
    'Summary': 'Summary text',
    'Body': 'Body content',
    'Content': 'Content data',
    'Value': 'Value data',
    'Data': 'Data content',
    'Result': 'Result value',
    'Output': 'Output data',
    'Input': 'Input data',
    'Source': 'Source reference',
    'Target': 'Target reference',
    'Ref': 'Reference value',
    'Key': 'Key value',
    'Tag': 'Tag identifier',
    'Type': 'Type indicator',
    'Kind': 'Kind/type indicator',
    'Class': 'Class/category',
    'Group': 'Group identifier',
    'Category': 'Category identifier',
    'Section': 'Section identifier',
    'Part': 'Part identifier',
    'Segment': 'Segment identifier',
    'Block': 'Block identifier',
    'Chunk': 'Chunk identifier',
    'Piece': 'Piece identifier',
    'Item': 'Item identifier',
    'Element': 'Element identifier',
    'Component': 'Component identifier',
    'Module': 'Module identifier',
    'Unit': 'Unit identifier',
    'Entity': 'Entity identifier',
    'Object': 'Object reference',
    'Record': 'Record reference',
    'Row': 'Row identifier',
    'Col': 'Column identifier',
    'Field': 'Field identifier',
    'Attr': 'Attribute value',
    'Prop': 'Property value',
    'Param': 'Parameter value',
    'Arg': 'Argument value',
    'Option': 'Option value',
    'Setting': 'Setting value',
    'Config': 'Configuration value',
    'Pref': 'Preference value',

    # Date/Time patterns
    'Date': 'Date value',
    'Time': 'Time value',
    'DateTime': 'Date and time value',
    'Timestamp': 'Timestamp value',
    'Year': 'Year value',
    'Month': 'Month value',
    'Day': 'Day value',
    'Hour': 'Hour value',
    'Minute': 'Minute value',
    'Second': 'Second value',
    'Week': 'Week number',
    'Quarter': 'Quarter number',
    'Period': 'Period identifier',
    'Duration': 'Duration value',
    'Interval': 'Interval value',
    'Span': 'Time span value',
    'Age': 'Age value',

    # Status/State patterns
    'Status': 'Status indicator',
    'State': 'State indicator',
    'Phase': 'Phase indicator',
    'Stage': 'Stage indicator',
    'Step': 'Step indicator',
    'Mode': 'Mode indicator',
    'Flag': 'Boolean flag',
    'Indicator': 'Indicator value',
    'Signal': 'Signal value',
    'Marker': 'Marker value',
    'Switch': 'Switch/toggle value',
    'Toggle': 'Toggle value',

    # Person/Contact patterns
    'First': 'First name',
    'Last': 'Last name',
    'Middle': 'Middle name/initial',
    'Suffix': 'Name suffix',
    'Prefix': 'Name prefix',
    'Phone': 'Phone number',
    'Fax': 'Fax number',
    'Email': 'Email address',
    'Mobile': 'Mobile phone number',
    'Cell': 'Cell phone number',
    'Address': 'Address text',
    'Street': 'Street address',
    'City': 'City name',
    'State': 'State/province',
    'Zip': 'ZIP/postal code',
    'Country': 'Country name',
    'Region': 'Region identifier',
    'Area': 'Area identifier',
    'Zone': 'Zone identifier',
    'District': 'District identifier',
    'Location': 'Location identifier',
    'Place': 'Place identifier',
    'Site': 'Site identifier',
    'Venue': 'Venue identifier',

    # File/Path patterns
    'File': 'File reference',
    'Filename': 'File name',
    'Path': 'File/folder path',
    'Dir': 'Directory path',
    'Folder': 'Folder path',
    'Ext': 'File extension',
    'Format': 'Format identifier',
    'Mime': 'MIME type',
    'Size': 'Size value',
    'Length': 'Length value',
    'Width': 'Width value',
    'Height': 'Height value',
    'Depth': 'Depth value',

    # Web/URL patterns
    'URL': 'URL address',
    'Uri': 'URI address',
    'Link': 'Link/URL',
    'Href': 'Hyperlink reference',
    'Host': 'Host name/address',
    'Port': 'Port number',
    'Domain': 'Domain name',
    'Protocol': 'Protocol identifier',
    'Scheme': 'URL scheme',

    # Security patterns
    'Password': 'Password (encrypted)',
    'Secret': 'Secret value (encrypted)',
    'Token': 'Security token',
    'Hash': 'Hash value',
    'Salt': 'Password salt',
    'Key': 'Encryption key',
    'Cert': 'Certificate data',
    'Signature': 'Digital signature',

    # Business patterns
    'Price': 'Price amount',
    'Cost': 'Cost amount',
    'Fee': 'Fee amount',
    'Tax': 'Tax amount',
    'Discount': 'Discount amount/percentage',
    'Markup': 'Markup amount/percentage',
    'Margin': 'Margin amount/percentage',
    'Commission': 'Commission amount',
    'Balance': 'Balance amount',
    'Credit': 'Credit amount',
    'Debit': 'Debit amount',
    'Payment': 'Payment amount',
    'Invoice': 'Invoice reference',
    'Receipt': 'Receipt reference',
    'Order': 'Order reference',
    'Quote': 'Quote reference',
    'Contract': 'Contract reference',
    'Account': 'Account reference',
    'Customer': 'Customer reference',
    'Vendor': 'Vendor reference',
    'Supplier': 'Supplier reference',
    'Client': 'Client reference',
    'Partner': 'Partner reference',
    'Employee': 'Employee reference',
    'Staff': 'Staff reference',
    'Manager': 'Manager reference',
    'Owner': 'Owner reference',
    'Author': 'Author reference',
    'Creator': 'Creator reference',
    'Editor': 'Editor reference',
    'Reviewer': 'Reviewer reference',
    'Approver': 'Approver reference',
}

# Suffix patterns for column names
SUFFIX_PATTERNS = {
    'Id': 'identifier',
    'ID': 'identifier',
    'Nbr': 'number',
    'No': 'number',
    'Num': 'number',
    'Cd': 'code',
    'Code': 'code',
    'Nm': 'name',
    'Name': 'name',
    'Desc': 'description',
    'Description': 'description',
    'Dt': 'date',
    'Date': 'date',
    'Tm': 'time',
    'Time': 'time',
    'Ts': 'timestamp',
    'Amt': 'amount',
    'Amount': 'amount',
    'Qty': 'quantity',
    'Quantity': 'quantity',
    'Pct': 'percentage',
    'Percent': 'percentage',
    'Percentage': 'percentage',
    'Flg': 'flag',
    'Flag': 'flag',
    'Ind': 'indicator',
    'Indicator': 'indicator',
    'Txt': 'text',
    'Text': 'text',
    'Val': 'value',
    'Value': 'value',
    'Cnt': 'count',
    'Count': 'count',
    'Seq': 'sequence',
    'Sequence': 'sequence',
    'Idx': 'index',
    'Index': 'index',
    'Lvl': 'level',
    'Level': 'level',
    'Typ': 'type',
    'Type': 'type',
    'Sts': 'status',
    'Status': 'status',
    'Path': 'path',
    'URL': 'URL',
    'Url': 'URL',
}


def get_column_description(column_name, table_name=''):
    """Generate description for a column based on its name."""

    # Check exact match in additional descriptions
    if column_name in ADDITIONAL_DESCRIPTIONS:
        return ADDITIONAL_DESCRIPTIONS[column_name]

    # Check case-insensitive match
    for key, desc in ADDITIONAL_DESCRIPTIONS.items():
        if key.lower() == column_name.lower():
            return desc

    # Check if column contains any key pattern
    for key, desc in ADDITIONAL_DESCRIPTIONS.items():
        if key.lower() in column_name.lower():
            # Extract prefix before the pattern
            idx = column_name.lower().find(key.lower())
            prefix = column_name[:idx]
            if prefix:
                # Convert CamelCase to readable
                prefix = re.sub(r'([a-z])([A-Z])', r'\1 \2', prefix)
                prefix = prefix.replace('_', ' ').strip()
                return f'{prefix} {desc.lower()}'
            return desc

    # Check suffix patterns
    for suffix, meaning in SUFFIX_PATTERNS.items():
        if column_name.endswith(suffix):
            prefix = column_name[:-len(suffix)]
            if prefix:
                # Convert CamelCase to readable
                prefix = re.sub(r'([a-z])([A-Z])', r'\1 \2', prefix)
                prefix = prefix.replace('_', ' ').strip()
                return f'{prefix} {meaning}'
            return f'{suffix} {meaning}'

    # Parse CamelCase or underscore-separated name
    readable = re.sub(r'([a-z])([A-Z])', r'\1 \2', column_name)
    readable = readable.replace('_', ' ').strip()

    if readable != column_name:
        return f'{readable} value'

    return None


def document_remaining_table_columns(database='EDS'):
    """Document remaining undocumented table columns."""

    logger = setup_logging('document_remaining_columns')
    logger.info(f"Documenting remaining table columns for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get undocumented table columns
    undoc = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            t.name AS TableName,
            c.name AS ColumnName
        FROM sys.columns c
        INNER JOIN sys.tables t ON c.object_id = t.object_id
        INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON c.object_id = ep.major_id
            AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE ep.value IS NULL
        ORDER BY s.name, t.name, c.column_id
    ''')

    logger.info(f"Found {len(undoc)} undocumented table columns")

    success = 0
    skipped = 0

    for schema, table, column in undoc:
        desc = get_column_description(column, table)

        if not desc:
            skipped += 1
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

    logger.info(f"Table columns documented: {success}")
    logger.info(f"Skipped (no match): {skipped}")

    return success, skipped


def document_remaining_view_columns(database='EDS'):
    """Document remaining undocumented view columns."""

    logger = setup_logging('document_remaining_columns')
    logger.info(f"Documenting remaining view columns for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get undocumented view columns
    undoc = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName,
            c.name AS ColumnName
        FROM sys.columns c
        INNER JOIN sys.views v ON c.object_id = v.object_id
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON c.object_id = ep.major_id
            AND c.column_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE ep.value IS NULL
        ORDER BY s.name, v.name, c.column_id
    ''')

    logger.info(f"Found {len(undoc)} undocumented view columns")

    success = 0
    skipped = 0

    for schema, view, column in undoc:
        desc = get_column_description(column, view)

        if not desc:
            skipped += 1
            continue

        # Add "(View)" prefix
        desc = f'(View) {desc}'

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'VIEW', @level1name = ?,
                    @level2type = N'COLUMN', @level2name = ?
            ''', (desc, schema, view, column))
            success += 1
            if success % 100 == 0:
                logger.info(f"  Applied {success} view column descriptions...")
        except:
            pass

    db.disconnect()

    logger.info(f"View columns documented: {success}")
    logger.info(f"Skipped (no match): {skipped}")

    return success, skipped


def main():
    """Document all remaining columns."""

    logger = setup_logging('document_remaining_columns')

    # Document table columns
    table_success, table_skipped = document_remaining_table_columns()

    # Document view columns
    view_success, view_skipped = document_remaining_view_columns()

    print(f"\n=== Remaining Columns Documentation Complete ===")
    print(f"Table columns documented: {table_success}")
    print(f"Table columns skipped: {table_skipped}")
    print(f"View columns documented: {view_success}")
    print(f"View columns skipped: {view_skipped}")
    print(f"Total documented: {table_success + view_success}")


if __name__ == '__main__':
    main()
