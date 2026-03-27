#!/usr/bin/env python3
"""
Document Stored Procedure Parameters

Adds MS_Description extended properties to stored procedure parameters.
"""

import os
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Parameter name patterns and descriptions
PARAM_DESCRIPTIONS = {
    # Common parameter names
    '@Id': 'Record identifier',
    '@ID': 'Record identifier',
    '@Name': 'Name value',
    '@Description': 'Description text',
    '@Status': 'Status code',
    '@Active': 'Active flag (1=active, 0=inactive)',
    '@Enabled': 'Enabled flag',
    '@Deleted': 'Deleted flag',
    '@CreatedBy': 'Created by user ID',
    '@CreatedDate': 'Creation date',
    '@ModifiedBy': 'Modified by user ID',
    '@ModifiedDate': 'Last modified date',
    '@StartDate': 'Start date',
    '@EndDate': 'End date',
    '@Date': 'Date value',
    '@DateTime': 'Date and time value',
    '@Year': 'Year value',
    '@Month': 'Month value',
    '@Day': 'Day value',
    '@Amount': 'Amount value',
    '@Price': 'Price value',
    '@Quantity': 'Quantity value',
    '@Total': 'Total value',
    '@Count': 'Count value',
    '@PageSize': 'Number of records per page',
    '@PageNumber': 'Page number for pagination',
    '@SortColumn': 'Column to sort by',
    '@SortDirection': 'Sort direction (ASC/DESC)',
    '@SearchText': 'Search text filter',
    '@Filter': 'Filter criteria',
    '@UserId': 'User identifier',
    '@UserName': 'User name',
    '@Email': 'Email address',
    '@Password': 'Password (should be hashed)',
    '@VendorId': 'Vendor identifier',
    '@CustomerId': 'Customer identifier',
    '@OrderId': 'Order identifier',
    '@POId': 'Purchase order identifier',
    '@BidId': 'Bid identifier',
    '@ItemId': 'Item identifier',
    '@CategoryId': 'Category identifier',
    '@SchoolId': 'School identifier',
    '@DistrictId': 'District identifier',
    '@RequisitionId': 'Requisition identifier',
    '@ContractId': 'Contract identifier',
    '@SessionId': 'Session identifier',
    '@Debug': 'Debug mode flag',
    '@ReturnValue': 'Output return value',
    '@ErrorMessage': 'Output error message',
    '@RowCount': 'Output row count',
    '@Success': 'Output success flag',
}

# Suffix patterns for parameters
PARAM_SUFFIX_PATTERNS = {
    'Id': 'identifier',
    'ID': 'identifier',
    'Code': 'code',
    'Name': 'name',
    'Desc': 'description',
    'Description': 'description',
    'Date': 'date',
    'Time': 'time',
    'DateTime': 'date and time',
    'Amount': 'amount',
    'Amt': 'amount',
    'Price': 'price',
    'Qty': 'quantity',
    'Quantity': 'quantity',
    'Count': 'count',
    'Cnt': 'count',
    'Total': 'total',
    'Flag': 'flag',
    'Flg': 'flag',
    'Status': 'status',
    'Type': 'type',
    'Number': 'number',
    'Num': 'number',
    'No': 'number',
    'List': 'list/array',
    'XML': 'XML data',
    'Json': 'JSON data',
    'Text': 'text',
    'Path': 'path',
    'URL': 'URL',
    'Email': 'email address',
    'Phone': 'phone number',
}


def get_param_description(param_name):
    """Generate description for a parameter based on its name."""

    # Check exact match
    if param_name in PARAM_DESCRIPTIONS:
        return PARAM_DESCRIPTIONS[param_name]

    # Remove @ prefix for pattern matching
    clean_name = param_name.lstrip('@')

    # Check suffix patterns
    for suffix, meaning in PARAM_SUFFIX_PATTERNS.items():
        if clean_name.endswith(suffix):
            prefix = clean_name[:-len(suffix)]
            if prefix:
                # Convert CamelCase to readable
                prefix = re.sub(r'([a-z])([A-Z])', r'\1 \2', prefix)
                prefix = prefix.replace('_', ' ').strip()
                return f'{prefix} {meaning}'
            return f'{meaning.capitalize()}'

    # Parse name into readable form
    readable = re.sub(r'([a-z])([A-Z])', r'\1 \2', clean_name)
    readable = readable.replace('_', ' ').strip()

    if readable != clean_name:
        return f'{readable} parameter'

    return f'{clean_name} parameter'


def document_sp_parameters(database='EDS'):
    """Add MS_Description to stored procedure parameters."""

    logger = setup_logging('document_sp_parameters')
    logger.info(f"Documenting SP parameters for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get all SP parameters without descriptions
    params = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            p.name AS ProcName,
            pm.name AS ParamName,
            pm.parameter_id AS ParamId
        FROM sys.parameters pm
        INNER JOIN sys.procedures p ON pm.object_id = p.object_id
        INNER JOIN sys.schemas s ON p.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON pm.object_id = ep.major_id
            AND pm.parameter_id = ep.minor_id AND ep.name = 'MS_Description'
        WHERE pm.parameter_id > 0  -- Exclude return value (parameter_id = 0)
            AND ep.value IS NULL
        ORDER BY s.name, p.name, pm.parameter_id
    ''')

    logger.info(f"Found {len(params)} undocumented SP parameters")

    success = 0
    errors = 0

    for schema, proc, param, param_id in params:
        desc = get_param_description(param)

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'PROCEDURE', @level1name = ?,
                    @level2type = N'PARAMETER', @level2name = ?
            ''', (desc, schema, proc, param))
            success += 1
            if success % 100 == 0:
                logger.info(f"  Applied {success} parameter descriptions...")
        except Exception as e:
            errors += 1
            if errors <= 5:
                logger.warning(f"Error on {schema}.{proc}.{param}: {str(e)[:50]}")

    db.disconnect()

    logger.info(f"[OK] SP parameter descriptions added: {success}")
    logger.info(f"  Errors: {errors}")

    print(f"\nSP parameter descriptions added: {success}")
    print(f"Errors: {errors}")

    return success


if __name__ == '__main__':
    document_sp_parameters()
