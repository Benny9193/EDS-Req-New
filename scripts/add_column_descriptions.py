#!/usr/bin/env python3
"""
Add Column Descriptions to EDS Database

Adds MS_Description extended properties to undocumented columns
based on business context and naming patterns.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Column descriptions by name pattern (business-specific)
COLUMN_DESCRIPTIONS = {
    # Transaction/Logging
    'SysId': 'System-generated unique identifier for the record',
    'RequestStart': 'Timestamp when the HTTP request started',
    'RequestEnd': 'Timestamp when the HTTP request completed',
    'SessionId': 'User session identifier for tracking',
    'TargetServer': 'Name of the server handling the request',
    'URL': 'Full URL of the HTTP request',
    'Headers': 'HTTP request headers (JSON or raw format)',
    'Content': 'HTTP request/response body content',
    'Method': 'HTTP method (GET, POST, PUT, DELETE, etc.)',
    'Protocol': 'Protocol version (HTTP/1.1, HTTP/2, etc.)',
    'LogDate': 'Date and time when log entry was created',
    'Msg': 'Debug message text content',

    # Report Session
    'RSLId': 'Report Session Link unique identifier',
    'RSId': 'Report Session identifier (foreign key)',
    'IntId': 'Internal reference identifier',
    'AuxId': 'Auxiliary/secondary reference identifier',

    # Cross References (Product catalog)
    'CrossRefId': 'Cross reference unique identifier',
    'CrossRefId_Old': 'Legacy cross reference ID for migration',
    'CatalogPrice': 'Price listed in product catalog',
    'Page': 'Catalog page number reference',
    'CatalogYear': 'Year of catalog publication',
    'CrossRefLocation': 'Location code for cross reference',
    'Manufacturor': 'Manufacturer name (legacy spelling)',
    'ManufacturorPartNumber': 'Manufacturer part/SKU number',
    'DateDeactivated': 'Date when record was deactivated',
    'DateUpdated': 'Date of last update',
    'GrossPrice': 'Gross price before discounts',
    'DoNotDiscount': 'Flag: 1=no discount allowed, 0=discountable',
    'RTK_MSDSId': 'Right-To-Know MSDS document reference ID',
    'RTK_MSDSNotNeeded': 'Flag: 1=MSDS not required for this item',
    'ReplacementCrossRefId': 'ID of replacement item if discontinued',
    'AdditionalShipping': 'Flag: 1=requires additional shipping charges',
    'UOM': 'Unit of measure (Each, Box, Case, etc.)',
    'MatchKey': 'Key used for product matching/deduplication',
    'ProductLine': 'Product line or category name',
    'ItemsPerUnit': 'Number of items in each unit/package',
    'MSDSFlag': 'Material Safety Data Sheet required flag',
    'MSDSRef': 'MSDS document reference URL or path',
    'Heading': 'Category heading for display',
    'UniqueItemNumber': 'Unique item identifier across systems',
    'keyword': 'Search keywords for item lookup',
    'ImageURL': 'URL to product image',
    'UPC_ISBN': 'Universal Product Code or ISBN',
    'UNSPSC': 'United Nations Standard Products/Services Code',
    'PerishableItem': 'Flag: 1=item is perishable',
    'PrescriptionRequired': 'Flag: 1=prescription required for purchase',
    'DigitallyDelivered': 'Flag: 1=delivered electronically',
    'HashKey': 'Computed hash for change detection',
    'ProductNames': 'Alternative product names for search',
    'TypeAheads': 'Auto-complete suggestions for search',
    'AIShortDesc': 'AI-generated short description',
    'AIFullDesc': 'AI-generated full description',
    'AIUNSPSC': 'AI-suggested UNSPSC classification',
    'AIDate': 'Date of AI description generation',

    # Bid Header Detail
    'BidHeaderDetailId': 'Bid header detail unique identifier',
    'DateAdded': 'Date record was added',
    'BidHeaderKey': 'Foreign key to BidHeaders table',

    # Bid Results
    'BidResultsId': 'Bid results unique identifier',
    'Units': 'Unit of measure for bid item',
    'Alternate': 'Alternate item description or substitution',
    'ItemBidType': 'Type of bid item (A=Award, N=No Bid, etc.)',
    'Cost': 'Cost/price for the bid item',
    'QuantityBid': 'Quantity offered in the bid',
    'Comments': 'Vendor or buyer comments on bid',
    'PageNo': 'Page number in bid document',
    'ModifiedSessionId': 'Session ID when last modified',
    'ContractNumber': 'Associated contract reference number',
    'OriginalAwardedItem': 'Flag: 1=originally awarded item',
    'VOMId': 'Vendor Order Management reference ID',
    'ManufacturerBid': 'Manufacturer name on vendor bid',
    'ManufPartNoBid': 'Manufacturer part number on bid',
    'LinerGaugeMicrons': 'Liner thickness in microns (for bags)',
    'LinerGaugeMil': 'Liner thickness in mils (for bags)',
    'LinerCaseWeight': 'Weight of liner case',
    'LinerDimWidth': 'Liner width dimension',
    'LinerDimDepth': 'Liner depth dimension',
    'LinerDimLength': 'Liner length dimension',
    'PackedManufPartNoBid': 'Normalized manufacturer part number',
    'SDS_URL': 'Safety Data Sheet document URL',

    # Detail (Order details)
    'DetailId': 'Order detail line unique identifier',
    'AddendumItem': 'Flag: 1=item added via addendum',
    'BidPrice': 'Price from winning bid',
    'DiscountRate': 'Discount percentage applied',
    'CatalogPage': 'Reference page in catalog',
    'Modified': 'Date/time of last modification',
    'ModifiedById': 'User ID who last modified',
    'SourceId': 'Source system or import ID',
    'SortSeq': 'Sort sequence for display ordering',
    'ReProc': 'Reprocessing flag',
    'UseGrossPrices': 'Flag: 1=use gross pricing',
    'DistrictRequisitionNumber': 'District-specific requisition number',
    'HeadingTitle': 'Category heading title',
    'Keyword': 'Search keyword',
    'ItemMustBeBid': 'Flag: 1=item requires competitive bid',
    'AddedFromAddenda': 'Date added from bid addendum',
    'LastAlteredSessionId': 'Session ID of last alteration',
    'ShippingCost': 'Shipping cost for the item',
    'ShippingUpdated': 'Date shipping was last updated',
    'DeliveryDate': 'Expected or actual delivery date',
    'DEANumber': 'DEA registration number (controlled substances)',

    # Items (Product master)
    'ItemId': 'Item unique identifier',
    'ParentCatalogId': 'Parent catalog category ID',
    'RTK': 'Right-To-Know hazardous material flag',
    'EditionId': 'Edition identifier for textbooks',
    'CopyrightYear': 'Copyright year for publications',
    'ManufacturorNumber': 'Manufacturer catalog number',
    'VendorPartNumber': 'Vendor-specific part number',
    'ListPrice': 'Manufacturer suggested list price',
    'ExtraDetail': 'Additional item details/specifications',
    'UOMDivisor': 'Divisor for unit conversion',
    'ListPriceSource': 'Source of list price (1=catalog, 2=vendor)',
    'CrossRefText': 'Cross reference description text',
    'StandardItem': 'Flag: 1=standard catalog item',
    'BidderToSupplyVendor': 'Flag: 1=bidder must specify vendor',
    'BidderToSupplyVendorPartNbr': 'Flag: 1=bidder must provide part number',
    'VendorToSupplyManufacturer': 'Flag: 1=vendor must specify manufacturer',
    'ProductLineId': 'Product line category ID',
    'HeadingKeywordId': 'Heading keyword lookup ID',

    # Bid Request Items
    'BidRequestItemId': 'Bid request item unique identifier',
    'BidRequestItemId_OLD': 'Legacy bid request item ID',
    'BidRequest': 'Parent bid request ID',
    'RequisitionCount': 'Number of requisitions for this item',
    'Checksum': 'Data integrity checksum',
    'MasterItemCodePtr': 'Pointer to master item code',

    # Bid Items
    'BidItemId': 'Bid item unique identifier',
    'BidItemId_Old': 'Legacy bid item ID',
    'Price': 'Bid price for the item',

    # Order Book Detail
    'OrderBookDetailId': 'Order book detail unique identifier',
    'Weight': 'Item weight for shipping calculation',
    'BasePrice': 'Base price before adjustments',
    'ParentAwardId': 'Parent award reference ID',

    # Common columns
    'Active': 'Record active status (1=active, 0=inactive)',
    'id': 'Unique identifier (GUID)',
}


def add_column_descriptions(database='EDS'):
    """Add descriptions to undocumented columns."""

    logger = setup_logging('add_column_descriptions')
    logger.info(f"Adding column descriptions for {database}")

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
        desc = COLUMN_DESCRIPTIONS.get(column)
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
            if success % 100 == 0:
                logger.info(f"  Applied {success} descriptions...")
        except Exception as e:
            errors += 1
            if errors <= 5:
                logger.warning(f"Error on {table}.{column}: {str(e)[:50]}")

    db.disconnect()

    logger.info(f"[OK] Column descriptions added: {success}")
    logger.info(f"  Columns without matching description: {skipped}")
    logger.info(f"  Errors: {errors}")

    print(f"\nColumn descriptions added: {success}")
    print(f"Columns without matching description: {skipped}")
    print(f"Errors: {errors}")

    return success


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description='Add column descriptions to database')
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
