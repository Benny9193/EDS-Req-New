#!/usr/bin/env python3
"""
Document Final Columns

Adds specific descriptions to the remaining undocumented columns.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from db_utils import DatabaseConnection
from logging_config import setup_logging

# Specific descriptions for remaining table columns
TABLE_COLUMN_DESCRIPTIONS = {
    # archive schema
    'archive.VendorQueryMSRPDetail.MSRPQuery': 'MSRP query reference identifier',

    # ChargeTypes
    'dbo.ChargeTypes.Repeats': 'Number of repetitions for charge',
    'dbo.ChargeTypes.LM': 'Last month indicator flag',

    # Debug/Log tables
    'dbo.DebugMsgs_Orig.sysid': 'System record identifier',
    'dbo.EmailBlastLog.Attachment': 'Email attachment file path',
    'dbo.ImageErrors.error': 'Error message text',
    'dbo.ImageLog.headers': 'HTTP headers from image request',
    'dbo.IPQueue.Queue': 'Queue name or identifier',
    'dbo.SDSErrors.error': 'SDS error message text',
    'dbo.SDSLog.headers': 'HTTP headers from SDS request',

    # District/Charges
    'dbo.DistrictCharges.Repeats': 'Number of charge repetitions',

    # Reference data
    'dbo.Months.Abbrev': 'Month abbreviation (3 chars)',
    'dbo.States.code': 'State/province code',

    # PO/Orders
    'dbo.POLayouts.Copies': 'Number of copies to print',

    # Product Verification
    'dbo.ProductVerificationResults.Reasoning': 'AI reasoning for verification result',

    # Questionnaire
    'dbo.QuestionnaireResponses.qrid': 'Questionnaire response identifier',
    'dbo.QuestionnaireResponses.userid': 'Responding user identifier',

    # RTK (Right-To-Know) chemical data
    'dbo.RTK_2010NJHSL.SHHS List': 'Special Health Hazard Substance list entry',
    'dbo.RTK_2010NJHSL.synonym': 'Chemical synonym name',
    'dbo.RTK_2010NJHSL.F3': 'Field 3 data',

    # SDS (Safety Data Sheets)
    'dbo.SDS_Rpt_Bridge.SDSDoc': 'SDS document reference',
    'dbo.SDSDocs.Document': 'SDS document binary content',

    # SSO/Authentication
    'dbo.SSOLoginTracking.SSOProvider': 'Single Sign-On provider name',
    'dbo.Users.SSOProvider': 'User SSO provider name',

    # Sulphite (chemical tracking)
    'dbo.Sulphite.Z2Exclude': 'Zone 2 exclusion flag',
    'dbo.SulphiteImport.Suggested alternate': 'Suggested alternate product',

    # Suppression
    'dbo.Suppression.Locator': 'Record locator identifier',
    'dbo.Suppression.Handled': 'Flag: suppression has been handled',

    # System tables
    'dbo.sysdiagrams.definition': 'Diagram definition binary data',

    # TAGFILE (legacy system)
    'dbo.TAGFILEP.USR': 'User identifier',
    'dbo.TAGFILEP.TBL': 'Table identifier',
    'dbo.TAGFILEP.POS': 'Position code',
    'dbo.TAGFILEP.VAL': 'Value data',
    'dbo.TagFilePos_.Pos': 'Position code',

    # Temp/Import tables
    'dbo.TempIrvingtonWincap.F3': 'Import field 3',
    'dbo.TempIrvingtonWincap.F7': 'Import field 7',
    'dbo.TempIrvingtonWincap.F8': 'Import field 8',
    'dbo.TempIrvingtonWincap.F9': 'Import field 9',
    'dbo.TempIrvingtonWincap.Building': 'Building name/code',
    'dbo.TempIrvingtonWincap.F11': 'Import field 11',
    'dbo.TempIrvingtonWincap.Dept for Apprvl': 'Department for approval',
    'dbo.TempIrvingtonWincap.Supervisor': 'Supervisor name',
    'dbo.TempIrvingtonWincap.F20': 'Import field 20',
    'dbo.TempIrvingtonWincap.F23': 'Import field 23',
    'dbo.TempIrvingtonWincap.F24': 'Import field 24',
    'dbo.TempIrvingtonWincap.EOL': 'End of line marker',

    # TM Survey
    'dbo.TMSurvey.Submitter': 'Survey submitter name',
    'dbo.TMSurvey.Finished': 'Survey completion timestamp',

    # User Admin
    'dbo.UserAdminLog.submituserid': 'Submitting user identifier',
    'dbo.UserAdminLog.action': 'Admin action performed',
    'dbo.UserImports.School': 'School name for import',
    'dbo.UserTrees.utid': 'User tree identifier',

    # Vendor
    'dbo.VendorQueryMSRPDetail.MSRPQuery': 'MSRP query reference identifier',
    'dbo.VendorUploads.cxmlsessionid': 'cXML session identifier',
    'dbo.VendorUploads.poid': 'Purchase order identifier',

    # Wizard/Help
    'dbo.WizHelpFile.Proc': 'Procedure name for help',

    # Misc
    'dbo.z4zbReqDetail.Filtered': 'Filtered record flag',
}

# Specific descriptions for remaining view columns
VIEW_COLUMN_DESCRIPTIONS = {
    # Bid Analysis
    'dbo.BidAnalysisDetail.Compliant1st': 'Flag: first compliant bid',
    'dbo.BidAnalysisDetailReq.Compliant1st': 'Flag: first compliant bid',
    'dbo.vw_BidAnalysisDetail.Compliant1st': 'Flag: first compliant bid',

    # Savings views
    'dbo.cvw_NJSavings.CYDollars': 'Current year dollar savings',
    'dbo.cvw_NJSavings.GTDollars': 'Grand total dollar savings',
    'dbo.cvw_NYSavings.CYDollars': 'Current year dollar savings',
    'dbo.cvw_NYSavings.GTDollars': 'Grand total dollar savings',
    'dbo.cvw_Savings.CYDollars': 'Current year dollar savings',
    'dbo.cvw_Savings.GTDollars': 'Grand total dollar savings',
    'dbo.vw_Savings1.CYDollars': 'Current year dollar savings',
    'dbo.vw_Savings1.GTDollars': 'Grand total dollar savings',
    'dbo.vw_Savings5.CYDollars': 'Current year dollar savings',
    'dbo.vw_Savings5.GTDollars': 'Grand total dollar savings',
    'dbo.vw_SavingsTotals5.GTSavings': 'Grand total savings amount',
    'dbo.vw_SavingsTotals5NonFiltered.GTSavings': 'Grand total savings (unfiltered)',
    'dbo.vw_SavingsTotals5Test.GTSavings': 'Grand total savings (test)',

    # User/Tree views
    'dbo.UserTreeView.Children': 'Number of child nodes',

    # Vendor views
    'dbo.VendorBidLookup.calendarid': 'Bid calendar identifier',
    'dbo.VendorBidLookup.code': 'Vendor code',
    'dbo.VendorContactProblemView.CODE': 'Vendor code',
    'dbo.VendorContactProblemView.BIDCONTACT': 'Bid contact flag',
    'dbo.VendorContactProblemView.POCONTACT': 'PO contact flag',
    'dbo.vw_ActiveVendors.Contact': 'Primary contact name',
    'dbo.vw_VendorPOView.POLines': 'Number of PO line items',
    'dbo.vw_VendorPOView1.POLines': 'Number of PO line items',
    'dbo.vw_VendorPOView2.POLines': 'Number of PO line items',

    # Approval/Workflow views
    'dbo.vw_ApprovalsHistory.Submitter': 'Approval submitter name',

    # At A Glance dashboard
    'dbo.vw_AtAGlance.Schedule': 'Schedule group name',
    'dbo.vw_AtAGlance.BAApprovals': 'Budget account approvals count',

    # Award views
    'dbo.vw_AwardedBidResults.UPC / EAN / ISBN': 'Product barcode (UPC/EAN/ISBN)',

    # Catalog views
    'dbo.vw_CatalogCompare.sysid': 'System record identifier',

    # Charge views
    'dbo.vw_ContinuanceCharges.LM': 'Last month indicator',
    'dbo.vw_ContinuanceSection1Charges.Covering': 'Coverage period description',

    # Budget views
    'dbo.vw_DistrictBudgetList.selected': 'Selection flag',
    'dbo.vw_DistrictBudgetPP.selected': 'Selection flag',
    'dbo.vw_DistrictsNeedingReview.Schedule': 'Schedule group name',

    # Requisition views
    'dbo.vw_ExistingRequisitions.Available': 'Available budget amount',
    'dbo.vw_ReqDetail.SDSAvail': 'SDS document available flag',
    'dbo.vw_ReqDetail_BK20241205.SDSAvail': 'SDS document available flag',
    'dbo.vw_ReqDetail_BK20241227.SDSAvail': 'SDS document available flag',
    'dbo.vw_ReqDetailSummary.Lines': 'Number of line items',
    'dbo.vw_RequisitionList.POCreated': 'PO created flag',
    'dbo.vw_RequisitionsShippingLocations.Requisitionid': 'Requisition identifier',

    # Financial Accounting views
    'dbo.vw_FA_ALLBudgetAccounts.Allocated': 'Allocated budget amount',
    'dbo.vw_FA_ALLBudgetAccounts.Spent': 'Spent budget amount',
    'dbo.vw_FA_ALLUserAccounts.Allocated': 'Allocated amount',
    'dbo.vw_FA_ALLUserAccounts.Spent': 'Spent amount',
    'dbo.vw_FA_BudgetAccounts.Allocated': 'Allocated budget amount',
    'dbo.vw_FA_BudgetAccounts.Spent': 'Spent budget amount',
    'dbo.vw_FA_EDSUser.Role': 'User role name',
    'dbo.vw_FA_UserAccounts.Allocated': 'Allocated amount',
    'dbo.vw_FA_UserAccounts.Spent': 'Spent amount',

    # Report views
    'dbo.vw_RptMissingURLsByBidAndVendor.bidheaderid': 'Bid header identifier',

    # RTK views
    'dbo.vw_RTK_Sites.RTKContact': 'RTK contact person',
    'dbo.vw_RTKInfo.Purpose': 'Chemical purpose/use',
    'dbo.vw_RTKInfoAnnual.Purpose': 'Chemical purpose/use',

    # Survey views
    'dbo.vw_TMSurveys.Submitter': 'Survey submitter name',
    'dbo.vw_TMSurveys.Finished': 'Survey completion timestamp',

    # VMS schema
    'VMS.vw_BidsByVendor.PK': 'Primary key value',
}


def document_final_columns(database='EDS'):
    """Add descriptions to final remaining columns."""

    logger = setup_logging('document_final_columns')
    logger.info(f"Documenting final columns for {database}")

    db = DatabaseConnection(database=database)
    db.connect()

    # Document table columns
    logger.info("Processing table columns...")
    table_success = 0
    table_errors = 0

    for key, desc in TABLE_COLUMN_DESCRIPTIONS.items():
        parts = key.split('.')
        if len(parts) != 3:
            continue
        schema, table, column = parts

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'TABLE', @level1name = ?,
                    @level2type = N'COLUMN', @level2name = ?
            ''', (desc, schema, table, column))
            table_success += 1
        except Exception as e:
            table_errors += 1
            logger.debug(f"Error on {key}: {str(e)[:50]}")

    logger.info(f"Table columns: {table_success} success, {table_errors} errors")

    # Document view columns
    logger.info("Processing view columns...")
    view_success = 0
    view_errors = 0

    for key, desc in VIEW_COLUMN_DESCRIPTIONS.items():
        parts = key.split('.')
        if len(parts) != 3:
            continue
        schema, view, column = parts

        # Add (View) prefix
        full_desc = f'(View) {desc}'

        try:
            db.execute_non_query('''
                EXEC sp_addextendedproperty
                    @name = N'MS_Description',
                    @value = ?,
                    @level0type = N'SCHEMA', @level0name = ?,
                    @level1type = N'VIEW', @level1name = ?,
                    @level2type = N'COLUMN', @level2name = ?
            ''', (full_desc, schema, view, column))
            view_success += 1
        except Exception as e:
            view_errors += 1
            logger.debug(f"Error on {key}: {str(e)[:50]}")

    db.disconnect()

    logger.info(f"[OK] Final columns documented")
    logger.info(f"  Table columns: {table_success} success, {table_errors} errors")
    logger.info(f"  View columns: {view_success} success, {view_errors} errors")

    print(f"\n=== Final Column Documentation Complete ===")
    print(f"Table columns: {table_success} documented, {table_errors} errors")
    print(f"View columns: {view_success} documented, {view_errors} errors")
    print(f"Total: {table_success + view_success} columns documented")

    return table_success, view_success


if __name__ == '__main__':
    document_final_columns()
