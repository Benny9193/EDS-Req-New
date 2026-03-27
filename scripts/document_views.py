#!/usr/bin/env python3
"""
Document Database Views

Adds MS_Description extended properties to database views.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# View descriptions - specific views
VIEW_DESCRIPTIONS = {
    # Bid Analysis views
    'BidAnalysisDetail': 'Detailed bid analysis with item-level pricing and vendor comparisons',
    'BidAnalysisDetailReq': 'Bid analysis detail for requisition items',
    'BidHeadersView': 'Summary view of bid headers with key information',
    'bidinfolookup': 'Bid information lookup for quick reference',
    'BidItemsView': 'View of items included in bids',
    'BidItemView': 'Individual bid item details with pricing',

    # Bid Manager views
    'BidMgrBidRankingMSRPView': 'MSRP bid ranking with manufacturer pricing comparison',
    'BidMgrBidRequestAndWriteInMSRPView': 'Bid requests and write-ins with MSRP pricing',
    'BidMgrBidRequestDetail': 'Detailed bid request information',
    'BidMgrBidRequestMSRPView': 'Bid requests with MSRP pricing data',
    'BidMgrBidResultsMSRPView': 'Bid results with MSRP comparison',
    'BidMgrBidTradeCountiesView': 'Bid trades by county for geographic analysis',
    'BidMgrBidTradeCountyTotals': 'County-level totals for bid trades',
    'BidMgrBidTradeLowBidder': 'Lowest bidder analysis by trade category',
    'BidMgrMSRP2ResultsView': 'MSRP v2 bid results with enhanced pricing',
    'BidMgrMSRP2VendorReportView': 'Vendor report for MSRP v2 bids',
    'BidMgrMSRP2VendorReportViewTemp': 'Temporary vendor report for MSRP v2 processing',
    'BidMgrMSRPVendorBidsView': 'Vendor bids with MSRP pricing',
    'BidMgrView': 'Bid manager main view with bid summaries',
    'BidMgrView2': 'Extended bid manager view with additional fields',

    # Bid Results views
    'BidResultChangesView': 'Audit trail of bid result changes',
    'BidResultsNoInactiveView': 'Active bid results excluding inactive entries',
    'BidResultsView': 'Complete bid results with vendor and pricing',
    'BidResultsView2': 'Extended bid results with additional details',

    # Catalog views
    'CatalogAllItems': 'All catalog items across categories',
    'CatalogItemsAll': 'Complete catalog item listing',
    'CatalogItemView': 'Individual catalog item details',
    'CatalogView': 'Main catalog view for browsing',
    'CatalogViewerView': 'Catalog viewer interface data',

    # Category views
    'CategoryItemsView': 'Items organized by category',
    'CategoryView': 'Category hierarchy and details',

    # Contract views
    'ContractPricesView': 'Contract pricing information',
    'ContractView': 'Contract summary and terms',

    # Cover/Order Book views
    'CoverView': 'Order book cover page data',
    'OBView': 'Order book view for printing',
    'OBViewBooklet': 'Order book booklet format',
    'OBViewExpand': 'Expanded order book view',

    # Detail views
    'DetailView': 'Purchase order detail line items',
    'DetailViewQuantity': 'Detail view with quantity breakdowns',

    # District views
    'DistrictView': 'District information and settings',
    'DistrictSetupView': 'District setup configuration',

    # Import views
    'ImportBidResultsView': 'Imported bid results staging',
    'ImportedCatalogView': 'Imported catalog data',
    'ImportPricesView': 'Imported pricing data',

    # Invoice views
    'InvoiceDetailView': 'Invoice line item details',
    'InvoiceView': 'Invoice summary information',

    # Item views
    'ItemCatalogView': 'Item catalog with pricing',
    'ItemsView': 'Master item list',
    'ItemView': 'Individual item details',

    # Order views
    'OrderBookLog': 'Order book activity log',
    'OrderItemsView': 'Ordered items listing',
    'OrdersView': 'Purchase order summary',

    # PO views
    'PODetailView': 'PO line item details',
    'POHeaderView': 'PO header information',
    'POView': 'Purchase order complete view',
    'POViewAll': 'All purchase orders view',

    # Pricing views
    'PriceListView': 'Price list for items',
    'PricingView': 'Pricing configuration view',
    'PricingViewAll': 'All pricing data',

    # Report views
    'ReportDataView': 'Report data source',
    'ReportView': 'Report configuration',

    # Requisition views
    'RequisitionDetailView': 'Requisition line items',
    'RequisitionsView': 'Requisition summary',
    'RequisitionView': 'Individual requisition details',

    # School views
    'SchoolItemsView': 'School-level item allocations',
    'SchoolsView': 'School listing and details',
    'SchoolView': 'Individual school information',

    # User views
    'UserAccountsView': 'User account information',
    'UserPermissionsView': 'User permission assignments',
    'UsersView': 'User listing',

    # Vendor views
    'VendorBidsView': 'Vendor bid submissions',
    'VendorCatalogView': 'Vendor catalog items',
    'VendorContactsView': 'Vendor contact information',
    'VendorDocumentsView': 'Vendor document listing',
    'VendorItemsView': 'Vendor item catalog',
    'VendorPOView': 'Vendor purchase orders',
    'VendorQueryView': 'Vendor query results',
    'VendorsView': 'Vendor listing',
    'VendorView': 'Individual vendor details',

    # Workflow views
    'ApprovalHistoryView': 'Approval workflow history',
    'ApprovalsView': 'Pending approvals',
    'ApprovalView': 'Approval details',

    # Miscellaneous
    'AuditView': 'Audit trail records',
    'BatchView': 'Batch processing status',
    'DashboardView': 'Dashboard summary data',
    'EmailBlastView': 'Email blast campaigns',
    'NotificationView': 'System notifications',
    'SessionView': 'User session information',
    'TransactionLogView': 'Transaction log entries',
}

# Pattern-based descriptions for views not in the specific list
VIEW_PATTERNS = {
    'BidMgr': 'Bid manager view for',
    'BidAnalysis': 'Bid analysis view showing',
    'BidResult': 'Bid results view with',
    'BidRequest': 'Bid request view for',
    'BidHeader': 'Bid header view with',
    'BidItem': 'Bid item view displaying',
    'BidTrade': 'Bid trade view for',
    'Catalog': 'Catalog view for',
    'Category': 'Category view showing',
    'Contract': 'Contract view with',
    'Cover': 'Cover page view for',
    'Detail': 'Detail view showing',
    'District': 'District view with',
    'Import': 'Import view for',
    'Invoice': 'Invoice view showing',
    'Item': 'Item view displaying',
    'OB': 'Order book view for',
    'Order': 'Order view with',
    'PO': 'Purchase order view showing',
    'Pricing': 'Pricing view with',
    'Price': 'Price view showing',
    'Report': 'Report view for',
    'Requisition': 'Requisition view with',
    'School': 'School view showing',
    'User': 'User view displaying',
    'Vendor': 'Vendor view for',
    'Approval': 'Approval workflow view',
    'Audit': 'Audit view showing',
    'Batch': 'Batch processing view',
    'Email': 'Email view for',
    'Session': 'Session view with',
    'Transaction': 'Transaction view showing',
    'Query': 'Query view for',
    'MSRP': 'MSRP pricing view with',
    'TandM': 'Time and materials view for',
    'T&M': 'Time and materials view for',
    'Doc': 'Document view showing',
    'Log': 'Log view with',
    'History': 'Historical view of',
    'Summary': 'Summary view showing',
    'All': 'Complete listing view of',
    'Lookup': 'Lookup view for',
    'List': 'List view showing',
    'Info': 'Information view with',
    'Status': 'Status view showing',
    'Count': 'Count/total view for',
    'Total': 'Totals view showing',
}


def get_view_description(view_name):
    """Get description for a view based on name or patterns."""
    # Check exact match first
    if view_name in VIEW_DESCRIPTIONS:
        return VIEW_DESCRIPTIONS[view_name]

    # Try pattern matching
    for pattern, desc_prefix in VIEW_PATTERNS.items():
        if pattern.lower() in view_name.lower():
            # Create description based on pattern
            clean_name = view_name.replace('View', '').replace('view', '')
            return f'{desc_prefix} {clean_name} data'

    # Default description
    return f'Database view: {view_name}'


def document_views(database='EDS'):
    """Add MS_Description to database views."""

    logger = setup_logging('document_views')
    logger.info(f"Documenting views for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Get views without descriptions
    views = db.execute_query('''
        SELECT
            s.name AS SchemaName,
            v.name AS ViewName
        FROM sys.views v
        INNER JOIN sys.schemas s ON v.schema_id = s.schema_id
        LEFT JOIN sys.extended_properties ep ON v.object_id = ep.major_id
            AND ep.minor_id = 0 AND ep.name = 'MS_Description'
        WHERE ep.value IS NULL
        ORDER BY s.name, v.name
    ''')

    logger.info(f"Found {len(views)} undocumented views")

    success = 0
    errors = 0

    for schema, view in views:
        desc = get_view_description(view)

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'VIEW', @level1name = ?
            ''', (desc, schema, view))
            success += 1
            if success % 50 == 0:
                logger.info(f"  Applied {success} view descriptions...")
        except Exception as e:
            errors += 1
            if errors <= 5:
                logger.warning(f"Error on {schema}.{view}: {str(e)[:50]}")

    db.disconnect()

    logger.info(f"[OK] View descriptions added: {success}")
    logger.info(f"  Errors: {errors}")

    print(f"\nView descriptions added: {success}")
    print(f"Errors: {errors}")

    return success


if __name__ == '__main__':
    document_views()
