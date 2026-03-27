# EDS Database - Views Business Guide

Generated: 2026-01-15

This guide provides business context and usage guidance for the key views in the EDS database. For complete column documentation, see EDS_VIEWS.md.

---

## Overview

The EDS database contains 475 views organized into functional domains. Views provide denormalized access to data for reporting, UI display, and application integration.

### Schema Distribution

| Schema | Views | Purpose |
|--------|-------|---------|
| `dbo` | 460 | Main application views |
| `EDSIQWebUser` | 11 | Web application specific views |
| `VMS` | 2 | Vendor Management System |
| `EDSIQEndUser` | 1 | End user portal |

### Naming Conventions

| Prefix | Purpose | Example |
|--------|---------|---------|
| `vw_` | Standard view | `vw_Requisitions` |
| `vw_FA_` | Front-end Application | `vw_FA_UserList` |
| `vw_AR` | Approval/Requisition | `vw_ARAccounts` |
| `vw_Bid` | Bidding related | `vw_BidHeadersList` |
| `vw_Req` | Requisition related | `vw_ReqDetail` |
| `vw_PO` | Purchase Order related | `vw_POStatus` |
| `vw_MSRP` | MSRP pricing views | `vw_MSRPVendorsBySession` |
| `rs_` | Reporting Services | `rs_DistrictSummary` |
| `pa_` | Processing Application | `pa_ReqList` |
| `cfv_` | Custom Filter Views | `cfv_Districts` |

---

## Requisition Views

### Core Requisition Views

These views support the requisition entry and management workflow.

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_Requisitions` | Master requisition view | Display requisition lists |
| `vw_RequisitionList` | Filtered requisition list | User requisition screens |
| `vw_RequisitionStatus` | Status with descriptions | Status display/filtering |
| `vw_RequisitionStatusBySession` | Session-filtered status | Current user context |
| `vw_IsRequisitionLocked` | Lock status check | Edit permission logic |
| `vw_RequisitionIsVisible` | Visibility permissions | Security filtering |

### Requisition Detail Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_ReqDetail` | Full line item details | Requisition display/print |
| `vw_ReqDetail1` | Alternate detail format | Legacy compatibility |
| `vw_ReqDetailPrint` | Print-formatted detail | Report generation |
| `vw_ReqDetailSummary` | Summarized detail | Dashboard display |
| `vw_ReqDetailTab` | Tab-delimited export | Data export |
| `vw_FormattedDetailDescription` | Formatted descriptions | UI display |
| `vw_JavaReqDetail` | Java application format | Java client integration |

### Requisition Category & Vendor Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_ReqCategories` | Categories on requisition | Category filtering |
| `vw_ReqVendors` | Vendors on requisition | Vendor display |
| `vw_ReqTotalsByVendor` | Totals by vendor | PO creation preview |
| `vw_RequisitionCatalogList` | Available catalogs | Catalog selection |
| `vw_AvailableReqBids` | Bids for requisition | Bid selection |

### Requisition Financial Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_RequisitionAccountBalance` | Account balances | Budget validation |
| `vw_RequisitionsAccounts` | Accounts on requisition | Account display |
| `vw_RequisitionShippingCosts` | Shipping totals | Cost calculation |
| `vw_RequisitionShippingLocations` | Delivery locations | Shipping options |

---

## Approval Workflow Views

### Approval Display Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_ApproveRequisitions` | Pending approvals | Approver dashboard |
| `vw_ApproveRequisitionsBySession` | Session-filtered approvals | Current approver view |
| `vw_ApprovalsHistory` | Approval audit trail | History display |

### Approval Reference Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_ARAccounts` | Accounts for approval | Account dropdown |
| `vw_ARBudgets` | Budgets for approval | Budget dropdown |
| `vw_ARCategories` | Categories for approval | Category dropdown |
| `vw_ARSchools` | Schools for approval | School dropdown |
| `vw_ARStatuses` | Statuses for approval | Status dropdown |
| `vw_ARUsers` | Users for approval | User dropdown |

---

## Purchase Order Views

### PO Header Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `POHeader` | Complete PO header | PO display |
| `POHeaderSummary` | PO summary data | PO lists |
| `vw_POStatus` | PO with status | Status tracking |
| `POAttentionList` | POs needing attention | Dashboard alerts |

### PO Detail Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `PODetail` | Full PO line items | PO display/print |
| `PODetailExport` | Export format | Data export |
| `PODetailJavaExport` | Java export format | Java client |
| `vw_POHeaderBidImports` | Bid import tracking | Import verification |

### Multi-Vendor PO Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_MultiVendorPODistrictsAndBudgets` | Districts/budgets for multi-vendor | Multi-vendor PO creation |

---

## Bidding Domain Views

The bidding domain has the most complex view structure, supporting bid creation, vendor response, evaluation, and award processes.

### Bid Header Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_BidHeadersList` | Active bid list | Bid management |
| `BidHeadersView` | Full bid header data | Bid display |
| `vw_ActiveBids` | Currently active bids | Bid selection |
| `BidsView` | Complete bid information | Reporting |

### Bid Request Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `BidRequestDetail` | Bid request line items | Request display |
| `BidRequestItemsView` | Items on bid request | Item listing |
| `BidRequestItemsCrossRefsView` | Cross-refs for items | Pricing lookup |
| `BidRequestItemsWeightView` | Weighted items | Evaluation |

### Bid Analysis Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `BidAnalysisDetail` | Detailed bid analysis | Bid evaluation |
| `vw_BidAnalysisDetail` | Analysis with vendor | Comparison |
| `vw_BidAnalysisVendorSummary` | Vendor summary | Award decision |
| `vw_BidAnalysisVendorSummaryByDistrict` | By district | District reporting |

### Bid Results Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `BidResultsView` | Vendor submissions | Result review |
| `vw_AwardedBidResults` | Awarded results | Award tracking |
| `vw_BidLines` | Line-level results | Detail analysis |

### MSRP Bidding Views

MSRP (Manufacturer's Suggested Retail Price) views support percentage-discount bidding.

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_MSRPVendorsBySession` | MSRP vendors in session | Vendor selection |
| `vw_MSRPCategoriesBySession` | MSRP categories | Category filtering |
| `vw_MSRPManufacturersBySession` | Manufacturers | MFG selection |
| `vw_MSRPBidResultsManufRev2` | MSRP results | Result analysis |
| `vw_MSRPRankManufacturerAWD` | Ranked manufacturers | Award ranking |
| `vw_MSRPRankProductLineAWD` | Ranked product lines | Award ranking |
| `BidMgrMSRPVendorBidsView` | Vendor MSRP bids | Bid review |

### Bid Document Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_BidDocumentsList` | Bid documents | Document access |
| `vw_BidDocumentTypeNames` | Document types | Type lookup |
| `vw_BidMgrBidderDocs` | Bidder documents | Document review |

### Bid Compliance Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_BidComplianceBySession` | Compliance status | Compliance check |
| `vw_BidLeadComplianceBySession` | Lead compliance | Lead review |
| `vw_BidAnswers` | Bid Q&A | Response review |

---

## Vendor Views

### Vendor Lookup Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_ActiveVendors` | Active vendor list | Vendor selection |
| `VendorBidLookup` | Vendors by bid | Bid-vendor matching |
| `vw_BidContactsVendorList` | Vendor contacts for bids | Contact lookup |
| `VendorContactProblemView` | Contact issues | Data quality |

### Awarded Vendor Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_AwardedVendorsAllCurrentBids` | Current awarded vendors | Active awards |
| `vw_AwardedVendorsAllCurrentAndFutureBids` | Including future | Award planning |
| `vw_AVVendorsBySession` | Session awarded vendors | Current context |
| `vw_AVBidsVendorsCategoriesBySession` | Vendor categories | Category filtering |

---

## Catalog & Item Views

### Item Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `SearchItemsView` | Item search results | Product search |
| `SearchItemsHeadingsView` | With headings | Category search |
| `SearchItemsKeywordsView` | With keywords | Keyword search |
| `vw_ItemDescription` | Full item description | Display |
| `vw_ItemDescriptionNoExtra` | Without extras | Simple display |
| `vw_ItemPricing` | Item with pricing | Price display |
| `vw_ItemsByBid` | Items on bid | Bid item list |
| `ItemsBidHeaderView` | Bid header items | Header display |

### Catalog Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_ActiveCatalogs` | Active catalogs | Catalog selection |
| `vw_LatestCrossRef` | Latest cross-refs | Current pricing |
| `vw_LowestPrice` | Lowest prices | Price comparison |
| `vw_PLCatalog` | Price list catalog | Price lists |

### Heading & Keyword Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_HeadingsByBid` | Headings on bid | Bid headings |
| `vw_HeadingsByReq` | Headings on requisition | Req headings |
| `vw_KeywordsByBid` | Keywords on bid | Bid search |
| `vw_KeywordsbyReqHeading` | Keywords by heading | Heading search |
| `vw_MPIHeadings` | MPI headings | MPI lookup |

---

## District & Organization Views

### District Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_ActiveDistrictList` | Active districts | District selection |
| `cfv_Districts` | Custom filter districts | Filtered lists |
| `vw_NJDistricts` | New Jersey districts | NJ specific |
| `vw_NY_TM_Districts` | NY districts | NY specific |
| `TMDistrictInfo` | District info | District display |
| `DistrictContactProblemView` | Contact issues | Data quality |

### School Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `cfv_Schools` | Custom filter schools | School lists |

### Report Summary Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `rs_DistrictSummary` | District summary | Reporting |
| `rs_DistrictSummaryAwardLetter` | Award letters | Letter generation |
| `rs_DistrictSummaryVendors` | Vendors by district | Vendor reporting |

---

## User & Security Views

### User Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `cfv_Users` | Custom filter users | User lists |
| `vw_FA_UserList` | Front-end user list | User selection |
| `vw_FA_UserDisplayName` | Display names | Name display |
| `vw_FA_UserLogin` | Login info | Authentication |
| `UserListView` | Complete user list | User management |
| `DistrictUsersView` | Users by district | District users |
| `UserContactProblemView` | Contact issues | Data quality |

### User Account Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_AvailableUserAccounts` | Available accounts | Account selection |
| `UsersApprovees` | User approvees | Approval chain |
| `UserTreeView` | User hierarchy | Org tree |

---

## Financial & Budget Views

### Budget Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `BudgetsView` | Complete budget info | Budget display |
| `vw_Financials` | Financial data | Financial reporting |

### Account Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `pa_Accounts` | Processing accounts | Account processing |
| `pa_Budgets` | Processing budgets | Budget processing |

### Savings Analysis Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `cvw_Savings` | Savings calculations | Savings reports |
| `cvw_NJSavings` | NJ savings | NJ reporting |
| `cvw_NYSavings` | NY savings | NY reporting |

---

## Order Book Views

Order book views support consolidated ordering.

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `OrderBookView` | Order book header | Book display |
| `OrderBookDetailView` | Book line items | Book details |
| `vw_IncidentalOrderDownloads` | Incidental orders | Download tracking |
| `vw_IncidentalOrderDownloadsDetail` | Download details | Detail tracking |

---

## Instruction Book Views

Instruction book views support catalog printing.

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `InstructionBookView` | Instruction book | Book display |
| `InstructionBookCalendar` | Book calendar | Calendar display |
| `vw_InstructionBookCalendar` | Calendar view | Schedule display |
| `vw_InstructionBookContents` | Book contents | TOC generation |

---

## Right-to-Know (RTK) Views

RTK views support hazardous material tracking.

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `RTK_Item_StructureView` | RTK item structure | Structure display |
| `vw_RTK_MSDSandCC` | MSDS and Content Central | Safety data |
| `vw_RTK_Sites` | RTK sites | Site tracking |
| `vw_RTKContentCentralMSDS` | Content Central MSDS | MSDS lookup |
| `vw_GetMSDSInfo` | MSDS info | MSDS display |

---

## Reporting Views

### Report Session Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `pa_ReqList` | Requisition list | Report data |
| `pa_Category` | Category list | Report data |
| `pa_School` | School list | Report data |
| `pa_Status` | Status list | Report data |
| `pa_Users` | User list | Report data |

### SBS (School Budget Summary) Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `rs_SBS_SchoolSummary` | School summary | School reporting |
| `rs_SBS_SchoolSummary_Detail` | Detail summary | Detailed reports |
| `rs_SBS_AccountRecap_District` | District recap | District reporting |
| `rs_SBS_AccountRecap_School` | School recap | School reporting |
| `rs_SBS_UserRecap_District` | User recap district | User reporting |
| `rs_SBS_UserRecap_School` | User recap school | User reporting |
| `rs_SBS_VendorRecap_District` | Vendor recap district | Vendor reporting |
| `rs_SBS_VendorRecap_School` | Vendor recap school | Vendor reporting |
| `rs_SBS_VendorRecap_User` | Vendor recap user | Vendor reporting |

### Expiration Reporting Views

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_RptExpireDateBidDocs` | Expiring bid docs | Expiration tracking |
| `vw_RptExpireDateBidDocsAndMore` | Extended expiration | Full tracking |
| `vw_RptMarkedReadyEmailBlastStats` | Email blast stats | Communication stats |

---

## EDSIQWebUser Schema Views

These views are specific to the EDSIQ web application.

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `CoverViewSrc` | Cover page source | Cover generation |
| `MissingCoverView` | Missing covers | Cover validation |
| `OrderBookDetailView` | Order book details | Book display |
| `OrderBookView` | Order book header | Book display |
| `POAccountList` | PO accounts | Account selection |
| `POAccountsUsed` | Used accounts | Account tracking |
| `ScheduledByPricePlanCategory` | Schedule by plan | Schedule display |
| `ScheduledDistrictsByPricePlanCategory` | Districts by plan | District display |

---

## VMS Schema Views

Vendor Management System views.

| View | Purpose | Key Use Case |
|------|---------|--------------|
| `vw_BidsByVendor` | Bids by vendor | Vendor portal |
| `vw_Login` | Vendor login | Authentication |

---

## View Categories Summary

| Category | Count | Key Views |
|----------|-------|-----------|
| Bidding | ~55 | vw_BidHeadersList, BidAnalysisDetail |
| Requisitions | ~30 | vw_Requisitions, vw_ReqDetail |
| Vendors | ~30 | vw_ActiveVendors, VendorBidLookup |
| Catalog/Items | ~14 | SearchItemsView, vw_ItemPricing |
| Districts | ~11 | vw_ActiveDistrictList, cfv_Districts |
| Approval | ~10 | vw_ApproveRequisitions, vw_ARAccounts |
| Details | ~8 | DetailView, vw_FormattedDetailDescription |
| PO | ~12 | POHeader, PODetail, vw_POStatus |
| Reporting | ~25 | rs_*, cvw_* |
| Other | ~279 | Specialized views |

---

## Performance Considerations

### High-Volume Views

These views query large tables and should be used with appropriate filters:

| View | Notes |
|------|-------|
| `vw_ReqDetail` | Joins Detail (30.8M rows) - filter by requisition |
| `BidAnalysisDetail` | Joins multiple bid tables - filter by bid header |
| `PODetail` | Joins PO detail tables - filter by PO |
| `SearchItemsView` | Searches Items (30.1M rows) - use search criteria |

### Session-Filtered Views

These views require session context and should not be used in batch jobs:

| View Pattern | Context Required |
|--------------|-----------------|
| `*BySession` | SessionTable.SessionId |
| `vw_AR*` | User context |
| `vw_FA_*` | Front-end session |

---

## Common View Usage Patterns

### Requisition Display

```
User logs in
    ↓
vw_RequisitionList (filtered by user/school)
    ↓
Click requisition → vw_ReqDetail (by RequisitionId)
    ↓
Display line items with vw_FormattedDetailDescription
```

### Approval Workflow

```
Approver logs in
    ↓
vw_ApproveRequisitionsBySession (pending approvals)
    ↓
Select requisition → vw_ReqDetail
    ↓
Check budget → vw_RequisitionAccountBalance
    ↓
Approve/Reject
```

### Bid Evaluation

```
Bid manager accesses bid
    ↓
vw_BidHeadersList (select bid)
    ↓
BidAnalysisDetail (view all responses)
    ↓
vw_BidAnalysisVendorSummary (compare vendors)
    ↓
vw_AwardedBidResults (after award)
```

### PO Generation

```
Generate PO from requisition
    ↓
vw_ReqTotalsByVendor (preview by vendor)
    ↓
Create PO
    ↓
POHeader / PODetail (view created PO)
    ↓
vw_POStatus (track status)
```

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial views business guide | Phase 3 Documentation |

