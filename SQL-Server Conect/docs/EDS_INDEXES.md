# EDS Database - Index Documentation

Generated: 2026-01-09 11:58:06

Total indexes documented: 815

---

## Summary Statistics

| Metric | Count |
|--------|-------|
| Total Indexes | 815 |
| Primary Keys | 344 |
| Unique Indexes | 31 |
| Clustered | 344 |
| Non-Clustered | 471 |
| Unused Indexes | 59 |
| High-Cost Indexes | 40 |

---

## Unused Indexes (Review for Removal)

These indexes have no seeks, scans, or lookups since last restart.

| Schema | Table | Index | Type | Size MB |
|--------|-------|-------|------|--------|
| dbo | ApprovalLevels | SK_ApprovalLevel | NONCLUSTERED | 0.02 |
| dbo | Awards | _dta_index_Awards_7_793105916__K4_K2_K18_9_17 | NONCLUSTERED | 0.00 |
| dbo | BatchBook | SK_DCCatCCBatch | NONCLUSTERED | 5.16 |
| dbo | BatchDetail | SK_BatchBook | NONCLUSTERED | 80.30 |
| dbo | BatchDetail | SK_Category | NONCLUSTERED | 99.35 |
| dbo | BatchDetail | SK_PCCat | NONCLUSTERED | 125.72 |
| dbo | BatchDetail | SK_ErrorCheck | NONCLUSTERED | 91.12 |
| dbo | BatchDetail | SKI_Batch_DistrictCode | NONCLUSTERED | 82.45 |
| dbo | BatchDetail | SKI_BatchActiveCategory_ItemCode | NONCLUSTERED | 195.66 |
| dbo | Batches | SK_Loaded | NONCLUSTERED | 0.30 |
| dbo | BidHeaderDetail_Orig | _dta_index_BidHeaderDetail_7_747201762__K2_K4_K1_K3 | NONCLUSTERED | 2602.15 |
| dbo | BidHeaderDetail_Orig | IX_BidHeaderDetail | NONCLUSTERED | 2429.40 |
| dbo | BidImportCounties | SKI_Active_BidImportIdBidTRadeCountyId | NONCLUSTERED | 1.38 |
| dbo | BidRequestItems_Orig | SK_BidItem | NONCLUSTERED | 494.95 |
| dbo | BidRequestOptions | SK_BRManufacturer_OptionProductName | NONCLUSTERED | 18.16 |
| dbo | BidRequestPriceRanges | SK_Lookups | NONCLUSTERED | 67.53 |
| dbo | BidRequestPriceRanges | SKI_BidHeader_Etc | NONCLUSTERED | 73.80 |
| dbo | Bids | SK_Vendor | NONCLUSTERED | 6.36 |
| dbo | CatalogText | SKI_CatalogId_PageText | NONCLUSTERED | 1697.40 |
| dbo | Category | SK_EDS | NONCLUSTERED | 0.02 |
| dbo | Counties | SK_StateName | NONCLUSTERED | 0.02 |
| dbo | CrossRefs | SKI_ActiveSDSRef_Catalog | NONCLUSTERED | 15261.21 |
| dbo | Detail | SKI_CrossRef_BidItemId | NONCLUSTERED | 624.30 |
| dbo | Detail | IX_Detail_RequisitionId_ItemId | NONCLUSTERED | 752.95 |
| dbo | Detail | Detail_ItemId_index | NONCLUSTERED | 658.55 |
| dbo | DetailChangeLog | SK_DetailOldNewQty | NONCLUSTERED | 73.37 |
| dbo | DetailNotifications | SKI_DetailDate_Etal | NONCLUSTERED | 277.34 |
| dbo | FreezeItems | ti_Crossref_Id | NONCLUSTERED | 0.41 |
| dbo | HolidayCalendar | HolidayCalendar_Year_Month_index | NONCLUSTERED | 0.02 |
| dbo | NextNumber | SK_IDType | NONCLUSTERED | 0.32 |

*...and 29 more*

---

## High-Cost Indexes (High Updates, Low Reads)

These indexes are updated frequently but rarely used for queries.

| Schema | Table | Index | Updates | Reads |
|--------|-------|-------|---------|-------|
| dbo | BidResults | SKI_AIDate_HashKey | 4,917 | 1 |
| dbo | CrossRefs | _dta_index_CrossRefs_12_389628481__K3_K1_K12 | 3,480 | 6 |
| dbo | CrossRefs | SK_CatalogActiveLastUpdated | 3,784 | 31 |
| dbo | CrossRefs | SKI_UniqueCatalog_ImageURLId | 3,801 | 1 |
| dbo | CrossRefs | SKI_ActiveSDSRef_Catalog | 3,784 | 0 |
| dbo | CrossRefs | ski_VICCatalogActive_DateUpdatedCrossRefIdImageURL | 3,784 | 1 |
| dbo | CrossRefs | ski_CatActiveManufacturerPartNumber_VICUPCSDManUnique | 3,801 | 49 |
| dbo | CrossRefs | IX_CrossRefs_MSDSRef_ItemId | 3,775 | 1 |
| dbo | CrossRefs | CrossRefs_MinimumOrderQuantity_index | 3,489 | 9 |
| dbo | CrossRefs | SKI_ImageURLCatalogActive_VendorItemCodeUnique | 3,801 | 1 |
| dbo | CrossRefs | SK_AIDate | 2,637,280 | 1 |
| dbo | CrossRefs | SKI_AIDate_KashKey | 2,637,280 | 2 |
| dbo | DebugMsgs | Idx_LogDate | 202,726 | 3 |
| dbo | Detail | SKI_CrossRef_BidItemId | 980,857 | 0 |
| dbo | Detail | ti_CrossRef_Detail | 980,857 | 10 |
| dbo | Detail | SK_DetailReq | 153,322 | 2 |
| dbo | Detail | SK_BHOnly | 256,800 | 1 |
| dbo | Detail | _dta_index_Detail_7_581629165__K1_K2_7 | 259,532 | 9 |
| dbo | Detail | _dta_index_Detail_7_581629165__K1_K2_K4_29_30 | 878,830 | 5 |
| dbo | Detail | IX_Detail_RequisitionId_ItemId | 1,084,307 | 0 |

---

## Most Used Indexes (Top 50)

| Schema | Table | Index | Seeks | Scans | Lookups |
|--------|-------|-------|-------|-------|--------|
| dbo | Users | PK_Users | 85,156,525 | 10,139 | 73,329 |
| dbo | Requisitions | PK_Requisitions | 33,026,263 | 89 | 2,571,511 |
| dbo | BidHeaders | PK_BidHeaders_1 | 149,985 | 41,777 | 27,421,916 |
| dbo | Catalog | PK_Catalog | 26,075,474 | 7,709 | 6,128 |
| dbo | BidHeaders | SK_BidHeaderEffective | 21,119,894 | 3,783 | 0 |
| dbo | SessionTable | PK_SessionTable | 20,534,078 | 21 | 11,115 |
| dbo | BidHeaderDetail | SK_Detail_2 | 18,429,160 | 1 | 0 |
| dbo | BidRequestItems | PK_BidRequestItems | 14,830,545 | 8 | 3,028,670 |
| dbo | CrossRefs | PK_CrossRefs2 | 15,932,368 | 29 | 194,963 |
| dbo | PricePlans | PK_PricePlans | 14,974,298 | 8,376 | 0 |
| dbo | BidHeaderDetail | PK_BidHeaderDetail | 1 | 5 | 14,768,840 |
| dbo | Budgets | SK_BudgetDistrict | 12,796,623 | 407,281 | 0 |
| dbo | BidHeaders | SKI_BidHeaderId_TypeAlert | 10,678,269 | 405,553 | 0 |
| dbo | Detail | PK_Detail | 6,151,987 | 51 | 3,370,512 |
| dbo | Awards | PK_Bids | 8,922,618 | 2,396 | 951 |
| dbo | Category | PK_Category | 8,114,056 | 487,122 | 47,246 |
| dbo | BidResults | PK_BidResults | 6,760,237 | 59 | 939,420 |
| dbo | CrossRefs | SKI_ItemActive_Etc | 7,636,159 | 1 | 0 |
| dbo | Items | PK_Items | 7,162,948 | 49 | 779 |
| dbo | BidItems | PK_BidItems2 | 6,980,620 | 56 | 172,772 |
| dbo | Bids | SK_BidHeaderActiveBidVendor | 7,022,128 | 20 | 0 |
| dbo | VendorContacts | SKI_Vendor_All | 6,919,407 | 5,725 | 0 |
| dbo | DMSSDSDocuments | SKI_MSDS_IDDoc | 6,373,142 | 2 | 0 |
| dbo | Bids | SKI_BidheaderActive_Bidid | 6,306,066 | 0 | 0 |
| dbo | Approvals | SKI_RequisitionApprovaldate_ApprovalidStatusid | 6,205,786 | 0 | 0 |
| dbo | District | PK_District | 6,012,339 | 46,418 | 1,702 |
| dbo | Detail | SKI_Requisition_QuantityBidPriceVendorBidHeader | 5,227,495 | 1 | 0 |
| dbo | Vendors | _dta_index_Vendors_9_752057765__K1_K4 | 4,783,958 | 414 | 0 |
| dbo | Vendors | PK_Vendors | 4,230,695 | 5,581 | 8,542 |
| dbo | DistrictCategories | SKI_DistrictCategory_Active | 4,133,042 | 396 | 0 |
| dbo | BidsCatalogList | PK__BidsCatalogList__5A254709 | 193,350 | 0 | 3,936,799 |
| dbo | Bids | PK_Bids_1 | 3,313,947 | 19,044 | 743,047 |
| dbo | Requisitions | SK_ReqBudget | 4,068,000 | 112 | 0 |
| dbo | BookTypes | PK_BookTypes | 2,575,661 | 1,424,289 | 0 |
| dbo | BidsCatalogList | SK_Bid | 3,936,800 | 0 | 0 |
| dbo | Approvals | PK_Approvals | 716,934 | 4 | 3,039,616 |
| dbo | StatusTable | PK_StatusTable | 3,576,350 | 71,145 | 14,524 |
| dbo | Items | _dta_index_Items_7_1509632471__K1_K24_K6_K15_K18_K11_K7_K3_K8_4_5_10_12_16_17_19_20_22 | 3,530,391 | 56 | 0 |
| dbo | CrossRefs | _dta_index_CrossRefs_7_389628481__K2_K3_K5_K1_K6 | 3,441,262 | 0 | 0 |
| dbo | SecurityRoleUsers | SKI_UserId_UserRoleIdRoleId | 3,433,922 | 4 | 0 |
| dbo | SafetyDataSheets | PK__SafetyDa__C9A3658F59DFE532 | 0 | 3,117,616 | 139,176 |
| dbo | RTK_ReportItems | SKI_MSDS_ItemId | 3,186,572 | 0 | 0 |
| dbo | RTK_Items | SKI_Item_Codes | 3,186,571 | 0 | 0 |
| dbo | SecurityRoles | PK__Security__F829C791160AB647 | 3,154,203 | 5 | 0 |
| dbo | VendorCategory | SKI_VendorCategory_Name | 3,138,572 | 478 | 0 |
| dbo | VendorContacts | _dta_index_VendorContacts_7_183372118__K2_K1_8_9_10_11_12_13 | 3,046,675 | 0 | 0 |
| dbo | BidRequestItems | SK_ItemBidRequestHeader_2 | 3,025,600 | 1 | 0 |
| dbo | BidResults | SKI_BidImportItemVOM_ItemBidTypeBidResults | 2,991,755 | 29 | 0 |
| dbo | BidImports | _dta_index_BidImports_7_475200793__K2_K3_K4_K1_5 | 2,954,270 | 0 | 0 |
| dbo | DistrictCategories | PK_DistrictCategories | 821 | 1,694 | 2,822,080 |

---

## All Indexes by Table

### archive.BidHeaders

*Table rows: 3,395*

**Idx_BidHeaders** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 3 seeks, 12 scans, 0 lookups
- Size: 0.08 MB


### dbo.AccountingDetail

*Table rows: 0*

****[PK]** PK__AccountingDetail__7988E3C9** (CLUSTERED)
- Key columns: `AccountingDetailId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.AccountingFormats

*Table rows: 49*

****[PK]** PK_AccountingFormats** (CLUSTERED)
- Key columns: `AccountingFormatId`
- Usage: 143,561 seeks, 440 scans, 0 lookups
- Size: 0.02 MB


### dbo.AccountingUserFields

*Table rows: 80*

****[PK]** PK__Accounti__9EC55982690305A6** (CLUSTERED)
- Key columns: `AccountingUserFieldId`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 0.02 MB


### dbo.Accounts

*Table rows: 108,701*

****[PK]** PK_Accounts** (CLUSTERED)
- Key columns: `AccountId`
- Usage: 1,427,045 seeks, 89 scans, 1,288 lookups
- Size: 8.40 MB

**SK_AccountDistrict** (NONCLUSTERED)
- Key columns: `DistrictId, Code`
- Usage: 1,339 seeks, 166 scans, 0 lookups
- Size: 6.56 MB

**SK_ActiveCode** (NONCLUSTERED)
- Key columns: `Active, Code`
- Usage: 317,407 seeks, 0 scans, 0 lookups
- Size: 7.29 MB

**_dta_index_Accounts_7_1035202788__K1_5** (NONCLUSTERED)
- Key columns: `AccountId`
- Included: `Code`
- Usage: 313,650 seeks, 44 scans, 0 lookups
- Size: 7.29 MB


### dbo.AccountSeparators

*Table rows: 0*

****[PK]** PK_AccountSeparators** (CLUSTERED)
- Key columns: `AccountSeparatorId`
- Usage: 1 seeks, 254 scans, 0 lookups
- Size: 0.00 MB


### dbo.AddendumItems

*Table rows: 0*

****[PK]** PK_AddendumItems** (CLUSTERED)
- Key columns: `ItemId`
- Usage: 0 seeks, 8 scans, 0 lookups
- Size: 0.00 MB


### dbo.additems

*Table rows: 0*

****[PK]** PK__additems__4AB81AF0** (CLUSTERED)
- Key columns: `ITEMID`
- Usage: 0 seeks, 6 scans, 0 lookups
- Size: 0.00 MB


### dbo.Alerts

*Table rows: 4*

****[PK]** PK__Alerts__EBB16AED20733621** (CLUSTERED)
- Key columns: `AlertID`
- Usage: 0 seeks, 55,281 scans, 0 lookups
- Size: 0.02 MB


### dbo.AnswerTypes

*Table rows: 0*

****[PK]** PK__AnswerTy__4D81A3671812FA4A** (CLUSTERED)
- Key columns: `AnswerTypeId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.ApprovalLevels

*Table rows: 9*

***[Unique]* PK_ApprovalLevelId** (CLUSTERED)
- Key columns: `ApprovalLevelId`
- Usage: 0 seeks, 3,418 scans, 0 lookups
- Size: 0.02 MB

**SK_ApprovalLevel** (NONCLUSTERED)
- Key columns: `ApprovalLevel`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

****[PK]** PK_ApprovalLevels** (NONCLUSTERED)
- Key columns: `ApprovalLevelId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.02 MB


### dbo.Approvals

*Table rows: 7,825,030*

****[PK]** PK_Approvals** (CLUSTERED)
- Key columns: `ApprovalId`
- Usage: 716,934 seeks, 4 scans, 3,039,616 lookups
- Size: 483.64 MB

**SK_RequisitionId** (NONCLUSTERED)
- Key columns: `RequisitionId`
- Usage: 269,779 seeks, 111 scans, 0 lookups
- Size: 122.55 MB

**SKI_RequisitionApprovaldate_ApprovalidStatusid** (NONCLUSTERED)
- Key columns: `RequisitionId, ApprovalDate`
- Included: `ApprovalId, StatusId`
- Usage: 6,205,786 seeks, 0 scans, 0 lookups
- Size: 216.84 MB

**SKI_RequisitionStatusApprovalDate_Id** (NONCLUSTERED)
- Key columns: `RequisitionId, StatusId, ApprovalDate`
- Included: `ApprovalId`
- Usage: 1,607,409 seeks, 48 scans, 0 lookups
- Size: 214.20 MB


### dbo.ApprovalsHistory

*Table rows: 332,112*

****[PK]** PK_ApprovalsHistory** (CLUSTERED)
- Key columns: `ApprovalId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 21.34 MB

**SK_Requisition** (NONCLUSTERED)
- Key columns: `RequisitionId`
- Usage: 9,581 seeks, 0 scans, 0 lookups
- Size: 6.39 MB


### dbo.Audit

*Table rows: 2,568,656*

****[PK]** PK_Audit** (CLUSTERED)
- Key columns: `AuditId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 172.23 MB


### dbo.Awardings

*Table rows: 11,023*

****[PK]** PK__Awarding__F43393FB9B614318** (CLUSTERED)
- Key columns: `AwardingId`
- Usage: 42 seeks, 7 scans, 0 lookups
- Size: 0.96 MB


### dbo.Awards

*Table rows: 135,686*

****[PK]** PK_Bids** (CLUSTERED)
- Key columns: `AwardId`
- Usage: 8,922,618 seeks, 2,396 scans, 951 lookups
- Size: 18.64 MB

**SK_Bid** (NONCLUSTERED)
- Key columns: `BidId`
- Usage: 386,705 seeks, 15 scans, 0 lookups
- Size: 3.09 MB

**SK_BidHeader** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 166 seeks, 0 scans, 0 lookups
- Size: 3.19 MB

**SK_BidActive** (NONCLUSTERED)
- Key columns: `BidId, Active`
- Usage: 439 seeks, 0 scans, 0 lookups
- Size: 3.86 MB

**_dta_index_Awards_9_352056340__K2_K1_K3** (NONCLUSTERED)
- Key columns: `Active, AwardId, BidId`
- Usage: 293 seeks, 1 scans, 0 lookups
- Size: 3.74 MB

**SK_VendorBidActive** (NONCLUSTERED)
- Key columns: `VendorId, Active, BidHeaderId`
- Usage: 693 seeks, 11 scans, 0 lookups
- Size: 6.30 MB

**_dta_index_Awards_7_793105916__K4_K2_K18_9_17** (NONCLUSTERED)
- Key columns: `VendorId, Active, BidHeaderId`
- Included: `VendorBidNumber, UseGrossPrices`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.AwardsCatalogList

*Table rows: 82,484*

****[PK]** PK__AwardsCatalogLis__583CFE97** (CLUSTERED)
- Key columns: `AwardCatalogId`
- Usage: 84 seeks, 0 scans, 79 lookups
- Size: 6.51 MB

**SK_Award** (NONCLUSTERED)
- Key columns: `AwardId`
- Usage: 113 seeks, 0 scans, 0 lookups
- Size: 1.34 MB

**SK_AwardCatalog** (NONCLUSTERED)
- Key columns: `AwardId, CatalogId`
- Usage: 95 seeks, 0 scans, 0 lookups
- Size: 1.70 MB

**_dta_index_AwardsCatalogList_9_1464392286__K3_K2_K4** (NONCLUSTERED)
- Key columns: `CatalogId, AwardId, DiscountRate`
- Usage: 301 seeks, 35 scans, 0 lookups
- Size: 3.05 MB


### dbo.AwardTypes

*Table rows: 2*

****[PK]** PK__AwardTyp__0F1CCD9E79596900** (CLUSTERED)
- Key columns: `AwardTypeId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.02 MB


### dbo.BatchBook

*Table rows: 217,611*

****[PK]** PK_BatchBook** (CLUSTERED)
- Key columns: `BatchBookId`
- Usage: 0 seeks, 5 scans, 0 lookups
- Size: 35.50 MB

**SK_DCU** (NONCLUSTERED)
- Key columns: `DistrictId, CategoryId, UserId, Active`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 5.41 MB

**SK_Batch** (NONCLUSTERED)
- Key columns: `BatchId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 2.59 MB

**SK_DCCatCCBatch** (NONCLUSTERED)
- Key columns: `DistrictCode, Category, CometCode, BatchId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 5.16 MB

**SK_DistrictId** (NONCLUSTERED)
- Key columns: `DistrictId, CategoryId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 4.23 MB


### dbo.BatchDetail

*Table rows: 5,020,036*

****[PK]** PK_BatchDetail** (CLUSTERED)
- Key columns: `BatchDetailId`
- Usage: 3 seeks, 0 scans, 0 lookups
- Size: 1013.38 MB

**SK_BatchBook** (NONCLUSTERED)
- Key columns: `BatchBookId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 80.30 MB

**SK_Category** (NONCLUSTERED)
- Key columns: `Category, DistrictCode, CometId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 99.35 MB

**SK_Batch** (NONCLUSTERED)
- Key columns: `BatchId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 59.62 MB

**SK_PCCat** (NONCLUSTERED)
- Key columns: `CategoryId, PackedCode`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 125.72 MB

**SK_ErrorCheck** (NONCLUSTERED)
- Key columns: `BatchBookId, Active, ErrorField`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 91.12 MB

**SKI_Batch_DistrictCode** (NONCLUSTERED)
- Key columns: `BatchId`
- Included: `DistrictCode`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 82.45 MB

**SKI_BatchActiveCategory_ItemCode** (NONCLUSTERED)
- Key columns: `BatchId, Active, CategoryId`
- Included: `ItemCode`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 195.66 MB


### dbo.BatchDetailInserts

*Table rows: 1,176*

****[PK]** PK_BatchDetailInserts** (CLUSTERED)
- Key columns: `BatchDetailInsertId`
- Usage: 0 seeks, 5 scans, 0 lookups
- Size: 0.08 MB


### dbo.Batches

*Table rows: 14,507*

****[PK]** PK_ImportBatches** (CLUSTERED)
- Key columns: `BatchId`
- Usage: 0 seeks, 212 scans, 0 lookups
- Size: 2.04 MB

**SK_Loaded** (NONCLUSTERED)
- Key columns: `Loaded`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.30 MB


### dbo.BidAnswers

*Table rows: 546,401*

****[PK]** PK__BidAnswe__7B1D995A4E6F0AFB** (CLUSTERED)
- Key columns: `BidAnswerId`
- Usage: 7,216 seeks, 1 scans, 2,163 lookups
- Size: 26.45 MB

**SK_TradeCountyImport_Question** (NONCLUSTERED)
- Key columns: `BidTradeId, CountyId, BidImportId`
- Included: `BidQuestionId`
- Usage: 7,802 seeks, 0 scans, 0 lookups
- Size: 13.46 MB

**SK_QuestionImportTradeCounty** (NONCLUSTERED)
- Key columns: `BidQuestionId, BidImportId, CountyId, BidTradeId`
- Usage: 296 seeks, 7 scans, 0 lookups
- Size: 13.27 MB

**SK_ImportTradeCounty_Question** (NONCLUSTERED)
- Key columns: `BidImportId, BidTradeId, CountyId`
- Included: `BidQuestionId`
- Usage: 2,122 seeks, 0 scans, 0 lookups
- Size: 13.63 MB


### dbo.BidAnswersJournal

*Table rows: 1,253,422*

****[PK]** PK__BidAnswe__8AD205EB523F9BDF** (CLUSTERED)
- Key columns: `BidAnswerJournalId`
- Usage: 15,656 seeks, 0 scans, 0 lookups
- Size: 76.33 MB

**SK_BidAnswer** (NONCLUSTERED)
- Key columns: `BidAnswerId, DateModified DESC, BidAnswerJournalId DESC`
- Usage: 15,360 seeks, 1 scans, 0 lookups
- Size: 25.02 MB


### dbo.BidCalendar

*Table rows: 1*

****[PK]** PK__BidCalendar__6458BCB9** (CLUSTERED)
- Key columns: `CalendarId`
- Usage: 0 seeks, 5 scans, 0 lookups
- Size: 0.02 MB


### dbo.BidderCheckList

*Table rows: 140*

****[PK]** PK_BidderCheckList** (CLUSTERED)
- Key columns: `BidderCheckListId`
- Usage: 30,358 seeks, 274 scans, 0 lookups
- Size: 0.08 MB

**SK_DocumentTypeBidderCheckListId** (NONCLUSTERED)
- Key columns: `DocumentTypeId, BidderCheckListId`
- Usage: 2,212 seeks, 2 scans, 0 lookups
- Size: 0.02 MB


### dbo.BidderCheckListPkgDetail

*Table rows: 1,195*

****[PK]** PK_BidderCheckListPkgDetail** (CLUSTERED)
- Key columns: `BidderCheckListPkgDetailId`
- Usage: 603 seeks, 44 scans, 0 lookups
- Size: 0.07 MB


### dbo.BidderCheckListPkgHeader

*Table rows: 56*

****[PK]** PK_CheckListPackageHeader** (CLUSTERED)
- Key columns: `BidderCheckListPkgHeaderId`
- Usage: 508 seeks, 73 scans, 0 lookups
- Size: 0.02 MB


### dbo.BidDocument

*Table rows: 10,558*

****[PK]** PK_BidDocument** (CLUSTERED)
- Key columns: `BidDocumentId`
- Usage: 18,473 seeks, 98 scans, 0 lookups
- Size: 3.30 MB


### dbo.BidDocumentTypes

*Table rows: 298*

****[PK]** PK__BidDocum__DBABDC6F43326279** (CLUSTERED)
- Key columns: `BidDocumentTypeId`
- Usage: 998 seeks, 2 scans, 0 lookups
- Size: 0.05 MB

**SK_DocLookup** (NONCLUSTERED)
- Key columns: `BidType, Name, VendorSpecific`
- Included: `DistrictVisible, OnlyShowOne`
- Usage: 1,268 seeks, 827 scans, 0 lookups
- Size: 0.04 MB


### dbo.BidHeaderCheckList

*Table rows: 110,423*

****[PK]** PK_BidHeaderCheckList** (CLUSTERED)
- Key columns: `BidHeaderCheckListId`
- Usage: 650 seeks, 5 scans, 59 lookups
- Size: 7.79 MB

**SKI_BidHeaderBidderCheckListIdDisplaySeq_Id** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidderCheckListId, DisplaySequence`
- Included: `BidHeaderCheckListId`
- Usage: 4,489 seeks, 0 scans, 0 lookups
- Size: 3.52 MB


### dbo.BidHeaderDetail

*Table rows: 123,789,710*

****[PK]** PK_BidHeaderDetail** (CLUSTERED)
- Key columns: `BidHeaderDetailId`
- Usage: 1 seeks, 5 scans, 14,768,840 lookups
- Size: 7973.59 MB

**_dta_index_BidHeaderDetail_K2_K4_K1_K3** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidRequestItemId, BidHeaderDetailId, DetailId`
- Usage: 3,486 seeks, 0 scans, 0 lookups
- Size: 3267.98 MB

**_dta_index_BidHeaderDetail_K4_K1_K3** (NONCLUSTERED)
- Key columns: `BidRequestItemId, BidHeaderDetailId, DetailId`
- Usage: 101 seeks, 1 scans, 0 lookups
- Size: 2765.16 MB

**IX_BidHeaderDetail_2** (NONCLUSTERED)
- Key columns: `BidHeaderId, DetailId`
- Usage: 450 seeks, 0 scans, 0 lookups
- Size: 3160.09 MB

**SK_BidHeader_2** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 4 seeks, 4 scans, 0 lookups
- Size: 2351.48 MB

**SK_Detail_2** (NONCLUSTERED)
- Key columns: `DetailId`
- Included: `BidHeaderDetailId, BidHeaderId`
- Usage: 18,429,160 seeks, 1 scans, 0 lookups
- Size: 3400.17 MB

****[UQ]** UQ__BidHeade__3213E83E12D014FD** (NONCLUSTERED)
- Key columns: `id`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 3632.71 MB


### dbo.BidHeaderDetail_Orig

*Table rows: 102,658,927*

****[PK]** PK_BidHeaderDetail_Orig** (CLUSTERED)
- Key columns: `BidHeaderDetailId`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 6095.11 MB

**_dta_index_BidHeaderDetail_7_747201762__K2_K4_K1_K3** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidRequestItemId, BidHeaderDetailId, DetailId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 2602.15 MB

**_dta_index_BidHeaderDetail_7_747201762__K4_K1_K3** (NONCLUSTERED)
- Key columns: `BidRequestItemId, BidHeaderDetailId, DetailId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 2197.25 MB

**IX_BidHeaderDetail** (NONCLUSTERED)
- Key columns: `BidHeaderId, DetailId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 2429.40 MB

**SK_BidHeader** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 1 seeks, 4 scans, 0 lookups
- Size: 1989.20 MB

**SK_Detail** (NONCLUSTERED)
- Key columns: `DetailId`
- Included: `BidHeaderDetailId, BidHeaderId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 2454.56 MB


### dbo.BidHeaderDocument

*Table rows: 161,488*

****[PK]** PK_BidHeaderDocumentLinks** (CLUSTERED)
- Key columns: `BidHeaderDocumentId`
- Usage: 2,593 seeks, 441 scans, 0 lookups
- Size: 7.01 MB


### dbo.BidHeaderDocuments

*Table rows: 1*

****[PK]** PK__BidHeaderDocumen__5C8290C7** (CLUSTERED)
- Key columns: `BidHeaderDocumentId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.08 MB


### dbo.BidHeaders

*Table rows: 9,548*

****[PK]** PK_BidHeaders_1** (CLUSTERED)
- Key columns: `BidHeaderKey`
- Usage: 149,985 seeks, 41,777 scans, 27,421,916 lookups
- Size: 6.29 MB

**SK_CatPPAwardDate** (NONCLUSTERED)
- Key columns: `CategoryId, PricePlanId, BidAwardDate`
- Usage: 14 seeks, 3 scans, 0 lookups
- Size: 0.56 MB

**SK_CatPPActive** (NONCLUSTERED)
- Key columns: `CategoryId, PricePlanId, Active`
- Included: `EffectiveFrom, EffectiveUntil, BidDate, BidAwardDate, BidType, BidHeaderKey, BidHeaderId`
- Usage: 58,038 seeks, 4,094 scans, 0 lookups
- Size: 1.31 MB

**SKI_AwardDateActive_HeaderCatPPDistrictKey** (NONCLUSTERED)
- Key columns: `BidAwardDate, Active`
- Included: `BidHeaderId, CategoryId, PricePlanId, DistrictId, BidHeaderKey`
- Usage: 10,141 seeks, 103,498 scans, 0 lookups
- Size: 0.41 MB

**SK_CatAwardDate** (NONCLUSTERED)
- Key columns: `PricePlanId, CategoryId, Active, BidAwardDate`
- Usage: 6,150 seeks, 0 scans, 0 lookups
- Size: 0.59 MB

***[Unique]* SKI_BidHeaderId_TypeAlert** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Included: `BidType, CompliantAlert`
- Usage: 10,678,269 seeks, 405,553 scans, 0 lookups
- Size: 0.23 MB

**SK_BHPricePlan** (NONCLUSTERED)
- Key columns: `BidHeaderId, PricePlanId`
- Included: `BidAwardDate, Description, CategoryId`
- Usage: 1,012,211 seeks, 19 scans, 0 lookups
- Size: 1.31 MB

**_dta_index_BidHeaders_9_45243216__K2_K16_K15_K3_K4_K1** (NONCLUSTERED)
- Key columns: `Active, CategoryId, EffectiveUntil, EffectiveFrom, PricePlanId, BidHeaderId`
- Usage: 48,427 seeks, 0 scans, 0 lookups
- Size: 0.91 MB

***[Unique]* SK_BidHeaderEffective** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active, EffectiveFrom, EffectiveUntil`
- Usage: 21,119,894 seeks, 3,783 scans, 0 lookups
- Size: 0.67 MB

****[UQ]** IX_BidHeaders** (NONCLUSTERED)
- Key columns: `Active, BidType, BidHeaderId`
- Usage: 107 seeks, 0 scans, 0 lookups
- Size: 0.27 MB

**SKI_Date** (NONCLUSTERED)
- Key columns: `EffectiveFrom, EffectiveUntil, CategoryId, Active, BidHeaderId`
- Usage: 1,315,813 seeks, 0 scans, 0 lookups
- Size: 0.77 MB

**SK_BidGrouper** (NONCLUSTERED)
- Key columns: `CategoryId, PricePlanId, BidAwardDate, BidType`
- Included: `BidHeaderId, EffectiveFrom, EffectiveUntil`
- Usage: 109 seeks, 0 scans, 0 lookups
- Size: 1.20 MB

**SKI_ActiveFromUntil_IdParent** (NONCLUSTERED)
- Key columns: `Active, EffectiveFrom, EffectiveUntil`
- Included: `BidHeaderId, ParentBidHeaderId`
- Usage: 1 seeks, 212,354 scans, 0 lookups
- Size: 0.63 MB

**SKI_ActiveFromUntil_etc** (NONCLUSTERED)
- Key columns: `Active, EffectiveFrom, EffectiveUntil`
- Included: `BidHeaderId, CategoryId, PricePlanId, DistrictId, BidType, ParentBidHeaderId`
- Usage: 61,968 seeks, 40,799 scans, 0 lookups
- Size: 0.86 MB

**_dta_index_BidHeaders_12_2024706611__K9** (NONCLUSTERED)
- Key columns: `BidType`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.19 MB

**_dta_index_BidHeaders_7_2024706611__K1_7_17** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Included: `BidAwardDate, Description`
- Usage: 0 seeks, 162 scans, 0 lookups
- Size: 1.20 MB

**IX_BIdHeaders_BidHeaderId** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 14,602 seeks, 104,593 scans, 0 lookups
- Size: 0.21 MB

**SK_ParentBidHeaderId** (NONCLUSTERED)
- Key columns: `ParentBidHeaderId`
- Usage: 111,087 seeks, 38 scans, 0 lookups
- Size: 0.16 MB

**SKI_ActiveParentFromUntil_CatPPDisType** (NONCLUSTERED)
- Key columns: `Active, ParentBidHeaderId, EffectiveFrom, EffectiveUntil`
- Included: `BidHeaderId, CategoryId, PricePlanId, DistrictId, BidType`
- Usage: 354,867 seeks, 0 scans, 0 lookups
- Size: 0.87 MB


### dbo.BidImportCatalogList

*Table rows: 32,921*

****[PK]** PK__BidImportCatalog__0D3AD6BB** (CLUSTERED)
- Key columns: `BidImportCatalogId`
- Usage: 1,448 seeks, 848 scans, 582 lookups
- Size: 1.91 MB

**SKI_CatalogBidImport_DiscountRateId** (NONCLUSTERED)
- Key columns: `CatalogId, BidImportId`
- Included: `BidImportCatalogId, DiscountRate`
- Usage: 32,659 seeks, 633 scans, 0 lookups
- Size: 0.80 MB

**SKI_BidImportCatalog_Id** (NONCLUSTERED)
- Key columns: `BidImportId, CatalogId`
- Included: `BidImportCatalogId, DiscountRate`
- Usage: 6,606 seeks, 0 scans, 0 lookups
- Size: 0.94 MB


### dbo.BidImportCounties

*Table rows: 64,339*

****[PK]** PK__BidImpor__C2DF818B7D29F9E4** (CLUSTERED)
- Key columns: `BidImportCountyId`
- Usage: 0 seeks, 1 scans, 2,693 lookups
- Size: 5.30 MB

**SKI_Active_BidImportIdBidTRadeCountyId** (NONCLUSTERED)
- Key columns: `Active`
- Included: `BidImportId, BidTradeCountyId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1.38 MB

**SKI_BidTRadeCountyIdActive_BidImportId** (NONCLUSTERED)
- Key columns: `BidTradeCountyId, Active`
- Included: `BidImportId`
- Usage: 59,882 seeks, 0 scans, 0 lookups
- Size: 1.63 MB

**SKI_BidImportId_BidImportCountyIdBidTradeCountyId** (NONCLUSTERED)
- Key columns: `BidImportId`
- Included: `BidImportCountyId, BidTradeCountyId`
- Usage: 2,893 seeks, 3 scans, 0 lookups
- Size: 1.08 MB


### dbo.BidImports

*Table rows: 54,708*

****[PK]** PK_BidImports** (CLUSTERED)
- Key columns: `BidImportId`
- Usage: 148,913 seeks, 147 scans, 44,706 lookups
- Size: 17.98 MB

**SK_BidHeader** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Included: `BidImportId, Active, VendorId`
- Usage: 37,039 seeks, 95 scans, 0 lookups
- Size: 1.89 MB

**SK_Vendor** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `BidImportId, BidHeaderId, VendorBidNumber`
- Usage: 254 seeks, 0 scans, 0 lookups
- Size: 3.72 MB

**_dta_index_BidImports_7_475200793__K2_K1_K3_K4_5_9_10** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidImportId, Active, VendorId`
- Included: `BidItemDiscountRate, ItemsBid, AmountBid`
- Usage: 6,623 seeks, 0 scans, 0 lookups
- Size: 3.26 MB

**_dta_index_BidImports_7_475200793__K3_K2_K1_K4_5_9_10** (NONCLUSTERED)
- Key columns: `Active, BidHeaderId, BidImportId, VendorId`
- Included: `BidItemDiscountRate, ItemsBid, AmountBid`
- Usage: 9,995 seeks, 0 scans, 0 lookups
- Size: 3.28 MB

**_dta_index_BidImports_7_475200793__K3_K1_K2_K4_5_9_10** (NONCLUSTERED)
- Key columns: `Active, BidImportId, BidHeaderId, VendorId`
- Included: `BidItemDiscountRate, ItemsBid, AmountBid`
- Usage: 936,568 seeks, 0 scans, 0 lookups
- Size: 2.97 MB

**_dta_index_BidImports_7_475200793__K1_K4** (NONCLUSTERED)
- Key columns: `BidImportId, VendorId`
- Usage: 342 seeks, 59 scans, 0 lookups
- Size: 1.33 MB

**_dta_index_BidImports_7_475200793__K1** (NONCLUSTERED)
- Key columns: `BidImportId`
- Usage: 0 seeks, 166 scans, 0 lookups
- Size: 0.94 MB

**_dta_index_BidImports_7_475200793__K2_K3_K4_K1_5** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active, VendorId, BidImportId`
- Included: `BidItemDiscountRate`
- Usage: 2,954,270 seeks, 0 scans, 0 lookups
- Size: 2.23 MB

**_dta_index_BidImports_7_475200793__K1_K3_K4_K2_5** (NONCLUSTERED)
- Key columns: `BidImportId, Active, VendorId, BidHeaderId`
- Included: `BidItemDiscountRate`
- Usage: 4,799 seeks, 299 scans, 0 lookups
- Size: 2.16 MB

**SKI_VendorImport_Header** (NONCLUSTERED)
- Key columns: `VendorId, BidImportId`
- Included: `BidHeaderId, Active`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 3.34 MB

**_dta_index_BidImports_7_1640249494__K1_K4_K26_2_8** (NONCLUSTERED)
- Key columns: `BidImportId, VendorId, POVendorContactId`
- Included: `BidHeaderId, VendorBidNumber`
- Usage: 58,362 seeks, 2 scans, 0 lookups
- Size: 2.94 MB


### dbo.BidItems

*Table rows: 26,906,489*

****[PK]** PK_BidItems2** (CLUSTERED)
- Key columns: `BidItemId`
- Usage: 6,980,620 seeks, 56 scans, 172,772 lookups
- Size: 3989.91 MB

**_dta_index_BidItems_7_1321107797__K1_K2** (NONCLUSTERED)
- Key columns: `BidItemId, BidId`
- Usage: 244,279 seeks, 39 scans, 0 lookups
- Size: 372.66 MB

**_dta_index_BidItems_9_416056568__K2_K3_K6_K4_K10** (NONCLUSTERED)
- Key columns: `BidId, ItemId, BidQuantity, Price, CrossRefId`
- Included: `BidResultsId`
- Usage: 167,317 seeks, 2 scans, 0 lookups
- Size: 1130.15 MB

**_dta_index_BidItems_9_416056568__K3_K2_K10_K1_K5_K9_K4** (NONCLUSTERED)
- Key columns: `ItemId, BidId, CrossRefId, BidItemId, Alternate, VendorItemCode, Price`
- Usage: 198,965 seeks, 0 scans, 0 lookups
- Size: 1643.40 MB

**SK_BidPackedVendor** (NONCLUSTERED)
- Key columns: `BidId, PackedVendorItemCode`
- Included: `BidItemId`
- Usage: 38,542 seeks, 2 scans, 0 lookups
- Size: 652.50 MB

**SK_ItemBid** (NONCLUSTERED)
- Key columns: `ItemId, BidId`
- Included: `BidItemId, Price, Alternate, VendorItemCode, CrossRefId`
- Usage: 49,335 seeks, 3 scans, 0 lookups
- Size: 1619.16 MB

**SK_Tune1** (NONCLUSTERED)
- Key columns: `ItemId, BidItemId, BidId, Price, Alternate, BidQuantity, AwardId, VendorItemCode`
- Usage: 3,783 seeks, 26 scans, 0 lookups
- Size: 1760.84 MB

**ti_Crossref_BidItemId** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `BidItemId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 377.66 MB

**SKI_BidResults_Bid_Item** (NONCLUSTERED)
- Key columns: `BidResultsId`
- Included: `BidId, ItemId`
- Usage: 42 seeks, 0 scans, 0 lookups
- Size: 602.73 MB

**SKI_BidResults_BidItem** (NONCLUSTERED)
- Key columns: `BidResultsId`
- Included: `BidId, ItemId`
- Usage: 1 seeks, 733 scans, 0 lookups
- Size: 602.60 MB


### dbo.BidItems_Old

*Table rows: 16,238,384*

****[PK]** PK_BidItems** (CLUSTERED)
- Key columns: `BidItemId`
- Usage: 0 seeks, 26 scans, 0 lookups
- Size: 2269.95 MB


### dbo.BidManagers

*Table rows: 0*

****[PK]** PK__BidManag__D819B22B2B5AD8E8** (CLUSTERED)
- Key columns: `BidManagerId`
- Usage: 1 seeks, 310 scans, 0 lookups
- Size: 0.00 MB


### dbo.BidManufacturers

*Table rows: 252,521*

****[PK]** PK__BidManuf__8D2BDD186E9E4570** (CLUSTERED)
- Key columns: `BMAId`
- Usage: 5 seeks, 0 scans, 0 lookups
- Size: 13.01 MB

**SKI_Manufacturer_BidDiscount** (NONCLUSTERED)
- Key columns: `ManufacturerId`
- Included: `BidId, DiscountRate`
- Usage: 89,912 seeks, 1 scans, 0 lookups
- Size: 7.23 MB

**SKI_BidManufacturer_Discount** (NONCLUSTERED)
- Key columns: `BidId, ManufacturerId`
- Included: `DiscountRate`
- Usage: 38,168 seeks, 85,316 scans, 0 lookups
- Size: 6.60 MB


### dbo.BidMappedItems

*Table rows: 1,456,772*

****[PK]** PK__BidMappe__6B5A9CC727E67581** (CLUSTERED)
- Key columns: `BidMappedItemId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 150.10 MB

**SKI_BidHeader_OrigNew** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Included: `OrigItemId, NewItemId`
- Usage: 43,528 seeks, 0 scans, 0 lookups
- Size: 52.32 MB

**SKI_BidHeaderReason_BidMappedItem** (NONCLUSTERED)
- Key columns: `BidHeaderId, ReasonCode`
- Included: `BidMappedItemId`
- Usage: 84 seeks, 0 scans, 0 lookups
- Size: 56.59 MB


### dbo.BidMgrConfiguration

*Table rows: 1*

****[PK]** PK_BidMgrConfiguration** (CLUSTERED)
- Key columns: `BidMgrConfigurationId`
- Usage: 0 seeks, 20 scans, 0 lookups
- Size: 0.02 MB


### dbo.BidMgrTagFile

*Table rows: 4,338,798*

****[PK]** PK_BidMgrTagFile** (CLUSTERED)
- Key columns: `BidMgrTagFileId`
- Usage: 49,229 seeks, 0 scans, 8,415 lookups
- Size: 281.98 MB

**SK_BidMgrTagFile_Usr_Tbl_Ptr** (NONCLUSTERED)
- Key columns: `Usr, Tbl, Ptr`
- Usage: 2,997 seeks, 0 scans, 0 lookups
- Size: 101.72 MB

**SK_BidMgrTagFile_Usr_Tbl** (NONCLUSTERED)
- Key columns: `Usr, Tbl`
- Usage: 44 seeks, 76 scans, 0 lookups
- Size: 83.54 MB

**SKI_Ptr_TagUsrTblVal** (NONCLUSTERED)
- Key columns: `Ptr`
- Included: `BidMgrTagFileId, Usr, Tbl, Val`
- Usage: 5,419 seeks, 0 scans, 0 lookups
- Size: 151.70 MB


### dbo.BidMSRPResultPrices

*Table rows: 422,692*

****[PK]** PK__BidMSRPR__6BDB670123093B9D** (CLUSTERED)
- Key columns: `BidMSRPResultPricesId`
- Usage: 853 seeks, 1 scans, 406 lookups
- Size: 26.37 MB

**SKI_ProductLine_** (NONCLUSTERED)
- Key columns: `BidMSRPResultsProductLineId`
- Included: `BidMSRPResultPricesId, BidMSRPResultsId, RangeWeight`
- Usage: 635 seeks, 1 scans, 0 lookups
- Size: 10.27 MB


### dbo.BidMSRPResults

*Table rows: 40,980*

****[PK]** PK__BidMSRPR__0E57068669D99053** (CLUSTERED)
- Key columns: `BidMSRPResultsId`
- Usage: 7,699 seeks, 18 scans, 10,814 lookups
- Size: 5.75 MB

**SKI_BidHeaderManufacturer_Results** (NONCLUSTERED)
- Key columns: `BidHeaderId, ManufacturerId`
- Included: `BidMSRPResultsId, Active, BidImportId, WinningBidOverride, TotalAward`
- Usage: 312 seeks, 56 scans, 0 lookups
- Size: 1.42 MB

**SKI_BidImportActive_BidHeader** (NONCLUSTERED)
- Key columns: `Active, BidImportId`
- Included: `BidMSRPResultsId, BidHeaderId`
- Usage: 10,548 seeks, 268 scans, 0 lookups
- Size: 0.98 MB


### dbo.BidMSRPResultsProductLines

*Table rows: 110,442*

****[PK]** PK_BidMSRPResultsProductLine** (CLUSTERED)
- Key columns: `BidMSRPResultsProductLineId`
- Usage: 2,568 seeks, 2 scans, 688 lookups
- Size: 10.23 MB

**SKI_BidResults_** (NONCLUSTERED)
- Key columns: `BidMSRPResultsId`
- Included: `BidMSRPResultsProductLineId, Active, MSRPOptionId, ManufacturerProductLineId, OptionName`
- Usage: 1,423 seeks, 102 scans, 0 lookups
- Size: 5.33 MB


### dbo.BidPackage

*Table rows: 50*

****[PK]** PK_BidDocumentPackage** (CLUSTERED)
- Key columns: `BidPackageId`
- Usage: 1,726 seeks, 538 scans, 0 lookups
- Size: 0.02 MB


### dbo.BidPackageDocument

*Table rows: 1,430*

****[PK]** PK_BidPackageDocument** (CLUSTERED)
- Key columns: `BidPackageDocumentId`
- Usage: 2,302 seeks, 613 scans, 0 lookups
- Size: 0.08 MB


### dbo.BidProductLinePrices

*Table rows: 1,323,391*

****[PK]** PK__BidProductLinePrices** (CLUSTERED)
- Key columns: `BidProductLinePriceId`
- Usage: 1,828 seeks, 0 scans, 0 lookups
- Size: 71.14 MB

**SKI_BidProductLinePrices** (NONCLUSTERED)
- Key columns: `BidProductLineId, RangeBase`
- Included: `BidProductLinePriceId, DiscountRate`
- Usage: 1,026 seeks, 3 scans, 0 lookups
- Size: 35.91 MB

**SKI_BidProductLinePricesDesc** (NONCLUSTERED)
- Key columns: `BidProductLineId, RangeBase DESC`
- Included: `BidProductLinePriceId, DiscountRate`
- Usage: 2,630 seeks, 0 scans, 0 lookups
- Size: 36.56 MB


### dbo.BidProductLines

*Table rows: 286,318*

****[PK]** PK__BidProdu__B50DDCA01F360E8C** (CLUSTERED)
- Key columns: `BidProductLineId`
- Usage: 0 seeks, 924 scans, 0 lookups
- Size: 15.63 MB


### dbo.BidQuestions

*Table rows: 23,509*

****[PK]** PK__BidQuest__25F2DBFE1BE38B2E** (CLUSTERED)
- Key columns: `BidQuestionId`
- Usage: 30,550 seeks, 5 scans, 0 lookups
- Size: 12.72 MB


### dbo.BidReawards

*Table rows: 611*

****[PK]** PK__BidReawa__14AE8FDE4B2C318A** (CLUSTERED)
- Key columns: `BidReawardId`
- Usage: 24,218 seeks, 8,461 scans, 0 lookups
- Size: 0.06 MB


### dbo.BidRequestItemMergeActions

*Table rows: 36,542*

****[PK]** PK_BidRequestItemMergeHistory** (CLUSTERED)
- Key columns: `BidRequestItemMergeActionsId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 1.65 MB


### dbo.BidRequestItemMergeActions_Orig

*Table rows: 27,168*

****[PK]** PK_BidRequestItemMergeHistory_Orig** (CLUSTERED)
- Key columns: `BidRequestItemMergeActionsId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 1.02 MB


### dbo.BidRequestItems

*Table rows: 27,855,481*

****[PK]** PK_BidRequestItems** (CLUSTERED)
- Key columns: `BidRequestItemId`
- Usage: 14,830,545 seeks, 8 scans, 3,028,670 lookups
- Size: 1929.58 MB

**IX_BidRequestItems_Old** (NONCLUSTERED)
- Key columns: `BidRequestItemId_OLD`
- Usage: 2 seeks, 11 scans, 0 lookups
- Size: 381.58 MB

**_dta_index_BidRequestItems_K2_K1_K5** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidRequestItemId, Active`
- Usage: 18,455 seeks, 4 scans, 0 lookups
- Size: 417.91 MB

**_dta_index_BidRequestItems_K2_K5_K1_3_4_7_8** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active, BidRequestItemId`
- Included: `ItemId, BidRequest, Status, Comments`
- Usage: 2,513 seeks, 3 scans, 0 lookups
- Size: 643.73 MB

**_dta_index_BidRequestItems_K2_K5_K1_K3** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active, BidRequestItemId, ItemId`
- Usage: 22,640 seeks, 6 scans, 0 lookups
- Size: 532.33 MB

**SK_BidItem_2** (NONCLUSTERED)
- Key columns: `BidHeaderId, ItemId`
- Usage: 1,422 seeks, 0 scans, 0 lookups
- Size: 579.98 MB

**SK_ItemBidRequestHeader_2** (NONCLUSTERED)
- Key columns: `ItemId, BidHeaderId, BidRequest`
- Usage: 3,025,600 seeks, 1 scans, 0 lookups
- Size: 743.33 MB

**SKI_BidHeader_RequestItemItemQuantityActiveReqcount_2** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidRequestItemId`
- Included: `ItemId, BidRequest, Active, RequisitionCount`
- Usage: 623 seeks, 1 scans, 0 lookups
- Size: 736.23 MB


### dbo.BidRequestItems_Orig

*Table rows: 25,521,585*

****[PK]** PK_BidRequestItems_Orig** (CLUSTERED)
- Key columns: `BidRequestItemId`
- Usage: 0 seeks, 7 scans, 0 lookups
- Size: 1757.88 MB

**_dta_index_BidRequestItems_7_363200394__K2_K1_K5** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidRequestItemId, Active`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 376.04 MB

**_dta_index_BidRequestItems_7_363200394__K2_K5_K1_3_4_7_8** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active, BidRequestItemId`
- Included: `ItemId, BidRequest, Status, Comments`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 579.39 MB

**_dta_index_BidRequestItems_7_363200394__K2_K5_K1_K3** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active, BidRequestItemId, ItemId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 477.92 MB

**IX_BidRequestItemID_OLD** (NONCLUSTERED)
- Key columns: `BidRequestItemId_OLD`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 347.30 MB

**SK_BidItem** (NONCLUSTERED)
- Key columns: `BidHeaderId, ItemId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 494.95 MB

**SK_ItemBidRequestHeader** (NONCLUSTERED)
- Key columns: `ItemId, BidHeaderId, BidRequest`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 603.27 MB

**SKI_BidHeader_RequestItemItemQuantityActiveReqcount** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidRequestItemId`
- Included: `ItemId, BidRequest, Active, RequisitionCount`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 671.02 MB


### dbo.BidRequestManufacturer

*Table rows: 104,823*

****[PK]** PK_BidRequestManufacturer** (CLUSTERED)
- Key columns: `BidRequestManufacturerId`
- Usage: 1,374 seeks, 4 scans, 36 lookups
- Size: 5.70 MB

**SKI_Manufact** (NONCLUSTERED)
- Key columns: `BidHeaderId, ManufacturerId`
- Included: `BidRequestManufacturerId, Active`
- Usage: 332 seeks, 14 scans, 0 lookups
- Size: 2.70 MB


### dbo.BidRequestOptions

*Table rows: 422,035*

****[PK]** PK__BidReque__9B394ED17D189CDF** (CLUSTERED)
- Key columns: `BidRequestOptionId`
- Usage: 3 seeks, 0 scans, 1 lookups
- Size: 33.77 MB

**SK_BRManufacturer_OptionProductName** (NONCLUSTERED)
- Key columns: `BidRequestManufacturerId`
- Included: `OptionId, BidRequestProductLineId, Name`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 18.16 MB

**SKI_ManufacturerProduct_OptionNameId** (NONCLUSTERED)
- Key columns: `BidRequestProductLineId, BidRequestManufacturerId`
- Included: `BidRequestOptionId, OptionId, Name`
- Usage: 316 seeks, 12 scans, 0 lookups
- Size: 17.94 MB

**SKI_OptionProduct_ETC** (NONCLUSTERED)
- Key columns: `BidRequestProductLineId, BidRequestOptionId`
- Included: `OptionId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 8.49 MB


### dbo.BidRequestPriceRanges

*Table rows: 1,897,760*

****[PK]** PK_BidRequestPriceRanges** (CLUSTERED)
- Key columns: `BidRequestPriceRangeId`
- Usage: 3 seeks, 0 scans, 1 lookups
- Size: 113.02 MB

***[Unique]* SK_Lookups** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidRequestManufacturerId, BidRequestProductLineId, BidRequestMSRPOptionId, RangeBase, BidRequestPriceRangeId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 67.53 MB

**SKI_BidHeader_Etc** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Included: `BidRequestPriceRangeId, BidRequestManufacturerId, BidRequestProductLineId, RangeBase, RangeWeight, BidRequestMSRPOptionId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 73.80 MB

**SKI_BRPR** (NONCLUSTERED)
- Key columns: `BidRequestProductLineId, BidRequestMSRPOptionId`
- Included: `BidRequestPriceRangeId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 35.20 MB


### dbo.BidRequestProductLines

*Table rows: 175,875*

****[PK]** PK__BidReque__D2B2584279480BFB** (CLUSTERED)
- Key columns: `BidRequestProductLineId`
- Usage: 1,365 seeks, 0 scans, 1 lookups
- Size: 7.56 MB

**SKI_BidRequestProduct_** (NONCLUSTERED)
- Key columns: `BidRequestManufacturerId`
- Included: `BidRequestProductLineId, Active, ManufacturerProductLineId`
- Usage: 286 seeks, 0 scans, 0 lookups
- Size: 4.14 MB

**SKI_BidRequestManufacturer_** (NONCLUSTERED)
- Key columns: `BidRequestManufacturerId`
- Included: `BidRequestProductLineId, Active, ManufacturerProductLineId`
- Usage: 0 seeks, 47 scans, 0 lookups
- Size: 4.14 MB


### dbo.BidResponses

*Table rows: 1*

****[PK]** PK__BidRespo__4C059DB21FB41C12** (CLUSTERED)
- Key columns: `BidResponseId`
- Usage: 1 seeks, 3 scans, 0 lookups
- Size: 0.02 MB


### dbo.BidResultChanges

*Table rows: 18,229,521*

****[PK]** PK__BidResultChanges__31783731** (CLUSTERED)
- Key columns: `BRChangeId`
- Usage: 0 seeks, 12 scans, 0 lookups
- Size: 1334.30 MB


### dbo.BidResults

*Table rows: 33,034,634*

****[PK]** PK_BidResults** (CLUSTERED)
- Key columns: `BidResultsId`
- Usage: 6,760,237 seeks, 59 scans, 939,420 lookups
- Size: 13462.04 MB

**Ix_BidHeaderId_2** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 33 seeks, 31 scans, 0 lookups
- Size: 453.89 MB

**SK_BidRequestItem_2** (NONCLUSTERED)
- Key columns: `BidRequestItemId`
- Usage: 896,629 seeks, 1 scans, 0 lookups
- Size: 491.27 MB

**SKI_BidImportBidRequestItem_ActiveBidTypeBidResultsUnitPrice_2** (NONCLUSTERED)
- Key columns: `BidImportId, BidRequestItemId`
- Included: `BidResultsId, DistrictId, Quantity, ItemBidType, UnitPrice`
- Usage: 1,516 seeks, 97 scans, 0 lookups
- Size: 1159.44 MB

**SK_ImportSDSRefSKI** (NONCLUSTERED)
- Key columns: `BidImportId, SDS_URL`
- Usage: 1,302 seeks, 7 scans, 0 lookups
- Size: 470.60 MB

**SKI_SDSRef_Import** (NONCLUSTERED)
- Key columns: `SDS_URL`
- Included: `BidImportId`
- Usage: 632 seeks, 0 scans, 0 lookups
- Size: 485.27 MB

**ski_VendorItemCodeImageURL_BidImportId** (NONCLUSTERED)
- Key columns: `VendorItemCode, ImageURL`
- Included: `BidImportId, BidResultsId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 905.41 MB

**SKI_BidImportVIC_ItemImage** (NONCLUSTERED)
- Key columns: `BidImportId, VendorItemCode`
- Included: `ItemId, ImageURL`
- Usage: 15 seeks, 1 scans, 0 lookups
- Size: 848.39 MB

**SKI_BidImportItemVOM_ItemBidTypeBidResults** (NONCLUSTERED)
- Key columns: `BidImportId, ItemId, VOMId`
- Included: `BidResultsId, ItemBidType`
- Usage: 2,991,755 seeks, 29 scans, 0 lookups
- Size: 793.39 MB

**SKI_ItemId_Info** (NONCLUSTERED)
- Key columns: `ItemId`
- Included: `ItemCode, VendorItemCode, ManufacturerBid, ManufPartNoBid, SDS_URL`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 1303.96 MB

**SKI_SDSURL_Info** (NONCLUSTERED)
- Key columns: `SDS_URL`
- Included: `ItemId, ItemCode, VendorItemCode, ManufacturerBid, ManufPartNoBid`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 1137.59 MB

**IX_BidResults_SDSURL_ItemId** (NONCLUSTERED)
- Key columns: `SDS_URL, ItemId`
- Usage: 0 seeks, 6 scans, 0 lookups
- Size: 596.64 MB

**IX_SDS_URL** (NONCLUSTERED)
- Key columns: `SDS_URL`
- Usage: 0 seeks, 12 scans, 0 lookups
- Size: 341.13 MB

**SK_HashKey** (NONCLUSTERED)
- Key columns: `HashKey`
- Usage: 1,427 seeks, 0 scans, 0 lookups
- Size: 438.58 MB

**SKI_AIDate_HashKey** (NONCLUSTERED)
- Key columns: `AIDate`
- Included: `HashKey`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 766.30 MB


### dbo.BidResults_Orig

*Table rows: 55,592,743*

****[PK]** PK_BidResults_Rebuilt_Orig** (CLUSTERED)
- Key columns: `BidResultsId`
- Usage: 0 seeks, 43 scans, 0 lookups
- Size: 10119.73 MB

**Ix_BidHeaderId** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 1 seeks, 4 scans, 0 lookups
- Size: 753.34 MB

**SK_BidRequestItem** (NONCLUSTERED)
- Key columns: `BidRequestItemId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 753.41 MB

**SKI_BidImportBidRequestItem_ActiveBidTypeBidResultsUnitPrice** (NONCLUSTERED)
- Key columns: `BidImportId, BidRequestItemId`
- Included: `BidResultsId, DistrictId, Quantity, ItemBidType, UnitPrice`
- Usage: 1 seeks, 6 scans, 0 lookups
- Size: 1885.86 MB


### dbo.BidResultsChangeLog

*Table rows: 238,978*

****[PK]** PK__BidResultsChange__247341CE** (CLUSTERED)
- Key columns: `BRChangeLogId`
- Usage: 0 seeks, 5 scans, 0 lookups
- Size: 19.74 MB


### dbo.Bids

*Table rows: 143,697*

****[PK]** PK_Bids_1** (CLUSTERED)
- Key columns: `BidId`
- Usage: 3,313,947 seeks, 19,044 scans, 743,047 lookups
- Size: 31.54 MB

**SK_BidHeader** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 62,897 seeks, 48 scans, 0 lookups
- Size: 3.44 MB

***[Unique]* SK_BidHeaderActiveBidVendor** (NONCLUSTERED)
- Key columns: `BidId, BidHeaderId, VendorId, Active`
- Usage: 7,022,128 seeks, 20 scans, 0 lookups
- Size: 5.16 MB

**SK_BidImport** (NONCLUSTERED)
- Key columns: `BidImportId, VendorId`
- Included: `BidId`
- Usage: 162 seeks, 6 scans, 0 lookups
- Size: 3.05 MB

**SK_ActiveHeaders** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active`
- Usage: 1,926,137 seeks, 0 scans, 0 lookups
- Size: 3.59 MB

**_dta_index_Bids_9_512056910__K19_K2_K1_K11** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active, BidId, VendorId`
- Usage: 500,412 seeks, 85,373 scans, 0 lookups
- Size: 4.42 MB

**_dta_index_Bids_9_512056910__K1_K2_K19_K11_K12** (NONCLUSTERED)
- Key columns: `BidId, Active, BidHeaderId, VendorId, BidDiscountRate`
- Usage: 254,185 seeks, 0 scans, 0 lookups
- Size: 6.38 MB

**SKI_BidHeaderVendorActive_Bid** (NONCLUSTERED)
- Key columns: `BidHeaderId, VendorId, Active`
- Included: `BidId, BidImportId, AdditionalHandlingAmount, FreeHandlingAmount, FreeHandlingStart, FreeHandlingEnd`
- Usage: 860,272 seeks, 0 scans, 0 lookups
- Size: 9.05 MB

**_dta_index_Bids_7_1785109450__K1_K11_K2_K19_K21** (NONCLUSTERED)
- Key columns: `BidId, VendorId, Active, BidHeaderId, BidImportId`
- Usage: 67,198 seeks, 0 scans, 0 lookups
- Size: 6.22 MB

**SKI_Active_BidVendorBidDiscountRateBidHeader** (NONCLUSTERED)
- Key columns: `Active`
- Included: `BidId, VendorId, BidDiscountRate, BidHeaderId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 6.35 MB

**SKI_Active_VendorBidheaderidBidImportid** (NONCLUSTERED)
- Key columns: `Active`
- Included: `VendorId, BidHeaderId, BidImportId`
- Usage: 40,791 seeks, 0 scans, 0 lookups
- Size: 6.16 MB

**SKI_BidheaderActive_Bidid** (NONCLUSTERED)
- Key columns: `BidHeaderId, Active, DateModified`
- Included: `BidId`
- Usage: 6,306,066 seeks, 0 scans, 0 lookups
- Size: 5.16 MB

**SK_Vendor** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `BidId, BidImportId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 6.36 MB

**SKI_ActiveVendor_BidImport** (NONCLUSTERED)
- Key columns: `Active, VendorId`
- Included: `BidHeaderId, BidImportId`
- Usage: 1,402 seeks, 42 scans, 0 lookups
- Size: 5.73 MB


### dbo.BidsCatalogList

*Table rows: 82,649*

****[PK]** PK__BidsCatalogList__5A254709** (CLUSTERED)
- Key columns: `BidCatalogId`
- Usage: 193,350 seeks, 0 scans, 3,936,799 lookups
- Size: 4.40 MB

**SK_Bid** (NONCLUSTERED)
- Key columns: `BidId`
- Included: `BidCatalogId`
- Usage: 3,936,800 seeks, 0 scans, 0 lookups
- Size: 1.61 MB

**SKI_Catalog_BidCatalogId** (NONCLUSTERED)
- Key columns: `CatalogId`
- Usage: 48 seeks, 0 scans, 0 lookups
- Size: 1.88 MB

**_dta_index_BidsCatalogList_7_171199710__K3_K1_K2** (NONCLUSTERED)
- Key columns: `CatalogId, BidCatalogId, BidId`
- Usage: 126,262 seeks, 1,318,155 scans, 0 lookups
- Size: 2.44 MB


### dbo.BidTradeCounties

*Table rows: 42,912*

****[PK]** PK__BidTrade__0909D2D914426966** (CLUSTERED)
- Key columns: `BidTradeCountyId`
- Usage: 6,708 seeks, 2 scans, 41 lookups
- Size: 1.73 MB

**SK_TradeCounty** (NONCLUSTERED)
- Key columns: `BidTradeId, CountyId`
- Usage: 36,468 seeks, 5 scans, 0 lookups
- Size: 1.12 MB

**SK_CountyTrade** (NONCLUSTERED)
- Key columns: `CountyId, BidTradeId`
- Included: `BidTradeCountyId`
- Usage: 26,553 seeks, 2 scans, 0 lookups
- Size: 1.48 MB


### dbo.BidTrades

*Table rows: 1,591*

****[PK]** PK__BidTrade__3200D0811071D882** (CLUSTERED)
- Key columns: `BidTradeId`
- Usage: 10,398 seeks, 0 scans, 1,349 lookups
- Size: 12.28 MB

**SK_BidHeaderId** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Included: `BidTradeId, TradeId, Title`
- Usage: 62,412 seeks, 6 scans, 0 lookups
- Size: 0.14 MB


### dbo.BidTypes

*Table rows: 2*

****[PK]** PK__BidTypes__332B7579** (CLUSTERED)
- Key columns: `BidTypeId`
- Usage: 0 seeks, 309 scans, 0 lookups
- Size: 0.02 MB


### dbo.BookTypes

*Table rows: 4*

****[PK]** PK_BookTypes** (CLUSTERED)
- Key columns: `BookTypeId`
- Usage: 2,575,661 seeks, 1,424,289 scans, 0 lookups
- Size: 0.02 MB


### dbo.BudgetAccounts

*Table rows: 1,399,990*

****[PK]** PK_BudgetAccounts** (CLUSTERED)
- Key columns: `BudgetAccountId`
- Usage: 1,602,950 seeks, 0 scans, 508,657 lookups
- Size: 83.30 MB

**SK_Budget** (NONCLUSTERED)
- Key columns: `BudgetId, Active`
- Usage: 394,279 seeks, 0 scans, 0 lookups
- Size: 23.99 MB

**SK_ActiveAccount** (NONCLUSTERED)
- Key columns: `Active, AccountId`
- Usage: 6,305 seeks, 0 scans, 0 lookups
- Size: 40.88 MB

**SK_BAUseAllocations** (NONCLUSTERED)
- Key columns: `UseAllocations, BudgetAccountId`
- Usage: 108,483 seeks, 0 scans, 0 lookups
- Size: 16.64 MB

**SK_UseAllocationsBA** (NONCLUSTERED)
- Key columns: `UseAllocations, BudgetAccountId`
- Usage: 0 seeks, 33 scans, 0 lookups
- Size: 17.30 MB

**SKI_Account_BudgetaccountActive** (NONCLUSTERED)
- Key columns: `AccountId`
- Included: `BudgetAccountId, Active`
- Usage: 974 seeks, 0 scans, 0 lookups
- Size: 40.95 MB

**_dta_index_BudgetAccounts_7_11199140__K1_4** (NONCLUSTERED)
- Key columns: `BudgetAccountId`
- Included: `AccountId`
- Usage: 179,473 seeks, 42 scans, 0 lookups
- Size: 19.95 MB


### dbo.Budgets

*Table rows: 16,376*

****[PK]** PK_Budgets** (CLUSTERED)
- Key columns: `BudgetId`
- Usage: 1,018,593 seeks, 0 scans, 174,132 lookups
- Size: 2.15 MB

**SK_District** (NONCLUSTERED)
- Key columns: `DistrictId`
- Usage: 361,574 seeks, 71,068 scans, 0 lookups
- Size: 0.41 MB

**SK_DistrictDate** (NONCLUSTERED)
- Key columns: `DistrictId, EndDate, StartDate`
- Usage: 139,019 seeks, 369 scans, 0 lookups
- Size: 0.86 MB

**SK_BudgetDistrict** (NONCLUSTERED)
- Key columns: `BudgetId, DistrictId`
- Included: `Active, Name, StartDate, EndDate, VisibleFrom, VisibleUntil, AnnualCutoff, EditFrom, EditUntil, EarlyAccess`
- Usage: 12,796,623 seeks, 407,281 scans, 0 lookups
- Size: 1.76 MB

**_dta_index_Budgets_7_2030682332__K3_K2_K1_4_5_6** (NONCLUSTERED)
- Key columns: `Active, DistrictId, BudgetId`
- Included: `Name, StartDate, EndDate`
- Usage: 122,422 seeks, 0 scans, 0 lookups
- Size: 1.23 MB

**SKI_Active_BudgetDistrictNameFromUntil** (NONCLUSTERED)
- Key columns: `Active`
- Included: `BudgetId, DistrictId, Name, VisibleFrom, VisibleUntil`
- Usage: 458,572 seeks, 376 scans, 0 lookups
- Size: 0.88 MB


### dbo.CalDistricts

*Table rows: 0*

****[PK]** PK__CalDistricts__6641052B** (CLUSTERED)
- Key columns: `CalDistrictId`
- Usage: 1 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.CalendarDates

*Table rows: 2,261*

****[PK]** PK__Calendar__D3AE10E05AE9F079** (CLUSTERED)
- Key columns: `CalendarDateId`
- Usage: 0 seeks, 11,757 scans, 0 lookups
- Size: 0.32 MB


### dbo.CalendarIB

*Table rows: 684*

****[PK]** PK__Calendar__AAF83A2A665BA325** (CLUSTERED)
- Key columns: `CalendarIBId`
- Usage: 0 seeks, 11,756 scans, 0 lookups
- Size: 0.05 MB


### dbo.CalendarItems

*Table rows: 0*

****[PK]** PK_CalendarItems** (CLUSTERED)
- Key columns: `CalendarItemId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.Calendars

*Table rows: 300*

****[PK]** PK__Calendar__53CFC44D628B1241** (CLUSTERED)
- Key columns: `CalendarId`
- Usage: 11,757 seeks, 5 scans, 0 lookups
- Size: 0.30 MB


### dbo.CalendarTypes

*Table rows: 2*

****[PK]** PK__Calendar__024C0F7C5348CEB1** (CLUSTERED)
- Key columns: `CalendarTypeId`
- Usage: 11,754 seeks, 4 scans, 0 lookups
- Size: 0.02 MB


### dbo.Carolina Living Items

*Table rows: 2,017*

****[PK]** PK_Carolina Living Items** (CLUSTERED)
- Key columns: `inventorynumber`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.23 MB


### dbo.Catalog

*Table rows: 3,897*

****[PK]** PK_Catalog** (CLUSTERED)
- Key columns: `CatalogId`
- Usage: 26,075,474 seeks, 7,709 scans, 6,128 lookups
- Size: 2.17 MB

**SKI_VendorCategoryActiveYearCatalog_Name** (NONCLUSTERED)
- Key columns: `VendorId, CategoryId, Active, CatalogYear DESC, CatalogId DESC`
- Included: `Name`
- Usage: 1,000,787 seeks, 0 scans, 0 lookups
- Size: 0.38 MB

**SKI_CategoryActiveYear_IdVendorName** (NONCLUSTERED)
- Key columns: `CategoryId, Active, CatalogYear`
- Included: `CatalogId, VendorId, Name, DisplayedVendorName`
- Usage: 206,868 seeks, 2,214,539 scans, 0 lookups
- Size: 0.30 MB

**SK_ActiveVendorPost** (NONCLUSTERED)
- Key columns: `Active, VendorId, PostDate`
- Usage: 1,319,559 seeks, 57 scans, 0 lookups
- Size: 0.14 MB


### dbo.CatalogImportFields

*Table rows: 15*

****[PK]** PK__CatalogI__DDA8F6524AD38441** (CLUSTERED)
- Key columns: `CatalogImportFieldId`
- Usage: 2 seeks, 1 scans, 0 lookups
- Size: 0.02 MB


### dbo.CatalogImportMap

*Table rows: 0*

****[PK]** PK__CatalogI__3420EF794EA41525** (CLUSTERED)
- Key columns: `CatalogImportMapId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.CatalogPricing

*Table rows: 0*

****[PK]** PK__CatalogP__F5B22BC60E9E9EA9** (CLUSTERED)
- Key columns: `CPId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.CatalogRequest

*Table rows: 0*

****[PK]** PK_CatalogRequest** (CLUSTERED)
- Key columns: `CatalogRequestId`
- Usage: 2 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.CatalogRequestDetail

*Table rows: 0*

****[PK]** PK_CatalogRequestDetail** (CLUSTERED)
- Key columns: `CatalogRequestDetailId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.CatalogRequestStatus

*Table rows: 0*

****[PK]** PK_CatalogRequestStatus** (CLUSTERED)
- Key columns: `CatalogRequestStatusId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.CatalogText

*Table rows: 112,799*

****[PK]** PK__CatalogT__D89517CF03D6F773** (CLUSTERED)
- Key columns: `CatalogTextId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 1689.45 MB

**SKI_CatalogId_PageText** (NONCLUSTERED)
- Key columns: `CatalogId`
- Included: `PageNbr, TextData`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1697.40 MB


### dbo.CatalogTextParts

*Table rows: 17,179,537*

****[PK]** PK__CatalogT__3489609851EE58DE** (CLUSTERED)
- Key columns: `CatalogTextPartId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 1044.75 MB

**SKI_CatalogTextId_OffsetPart** (NONCLUSTERED)
- Key columns: `CatalogTextId`
- Included: `BaseOffset, TextPart`
- Usage: 0 seeks, 8 scans, 0 lookups
- Size: 708.74 MB


### dbo.Category

*Table rows: 134*

****[PK]** PK_Category** (CLUSTERED)
- Key columns: `CategoryId`
- Usage: 8,114,056 seeks, 487,122 scans, 47,246 lookups
- Size: 0.05 MB

**SK_EDS** (NONCLUSTERED)
- Key columns: `EDSId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

**SK_Active** (NONCLUSTERED)
- Key columns: `Active`
- Usage: 162,435 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

**SK_Name** (NONCLUSTERED)
- Key columns: `Name`
- Usage: 920 seeks, 3,064 scans, 0 lookups
- Size: 0.02 MB

**SK_CategoryType** (NONCLUSTERED)
- Key columns: `Type, CategoryId`
- Usage: 433,255 seeks, 80 scans, 0 lookups
- Size: 0.02 MB

***[Unique]* SKI_Category_NameExtraTitle** (NONCLUSTERED)
- Key columns: `CategoryId`
- Included: `Name, ExtraTitle`
- Usage: 2,523,109 seeks, 18,391 scans, 0 lookups
- Size: 0.02 MB


### dbo.CertificateAuthority

*Table rows: 1*

****[PK]** PK__Certific__38B8FA6C28296682** (CLUSTERED)
- Key columns: `CertificateAuthorityId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 0.02 MB


### dbo.ChargeTypes

*Table rows: 14*

****[PK]** PK__ChargeTypes__31272A29** (CLUSTERED)
- Key columns: `ChargeTypeId`
- Usage: 824 seeks, 489 scans, 0 lookups
- Size: 0.02 MB


### dbo.CommonVendorQueryAnswer

*Table rows: 0*

****[PK]** PK__CommonVe__5BDEDA942A8A3EB4** (CLUSTERED)
- Key columns: `CommonVendorQueryAnswerId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.ContractTypes

*Table rows: 0*

****[PK]** PK_ContractTypes** (CLUSTERED)
- Key columns: `ContractId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.Control

*Table rows: 1*

****[PK]** PK__Control__77B5A9F0** (CLUSTERED)
- Key columns: `ControlId`
- Usage: 0 seeks, 11,901 scans, 0 lookups
- Size: 0.02 MB


### dbo.Coops

*Table rows: 20*

****[PK]** PK_Coops** (CLUSTERED)
- Key columns: `CoopId`
- Usage: 2 seeks, 2 scans, 0 lookups
- Size: 0.02 MB


### dbo.CopyRequests

*Table rows: 23,572*

****[PK]** PK__CopyRequests__4CB63D52** (CLUSTERED)
- Key columns: `CopyRequestId`
- Usage: 319 seeks, 3,389 scans, 0 lookups
- Size: 1.70 MB


### dbo.Counties

*Table rows: 78*

****[PK]** PK__Counties__71CC8A7A** (CLUSTERED)
- Key columns: `CountyId`
- Usage: 8,800 seeks, 1 scans, 0 lookups
- Size: 0.02 MB

**SK_StateName** (NONCLUSTERED)
- Key columns: `State, Name`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

**SK_StateIDName** (NONCLUSTERED)
- Key columns: `Name, StateId`
- Usage: 73,232 seeks, 1,029 scans, 0 lookups
- Size: 0.02 MB


### dbo.CoverView

*Table rows: 0*

****[PK]** PK_CoverView** (CLUSTERED)
- Key columns: `CoverViewId`
- Usage: 0 seeks, 7 scans, 0 lookups
- Size: 0.00 MB


### dbo.CrossRefs

*Table rows: 150,631,340*

****[PK]** PK_CrossRefs2** (CLUSTERED)
- Key columns: `CrossRefId`
- Usage: 15,932,368 seeks, 29 scans, 194,963 lookups
- Size: 111819.28 MB

**_dta_index_CrossRefs_12_389628481__K3_K1_K12** (NONCLUSTERED)
- Key columns: `ItemId, CrossRefId, ManufacturorPartNumber`
- Usage: 5 seeks, 1 scans, 0 lookups
- Size: 5347.63 MB

**_dta_index_CrossRefs_7_389628481__K1_K2_K3_K5_K6_21** (NONCLUSTERED)
- Key columns: `CrossRefId, Active, ItemId, CatalogId, CatalogPrice DESC`
- Included: `AdditionalShipping`
- Usage: 193,705 seeks, 5 scans, 0 lookups
- Size: 4180.26 MB

**_dta_index_CrossRefs_7_389628481__K2_K3_K5_K1_K6** (NONCLUSTERED)
- Key columns: `Active, ItemId, CatalogId, CrossRefId, CatalogPrice DESC`
- Usage: 3,441,262 seeks, 0 scans, 0 lookups
- Size: 6117.98 MB

**_dta_index_CrossRefs_9_457768688__K1_K6_K7** (NONCLUSTERED)
- Key columns: `CrossRefId, CatalogPrice, Page`
- Usage: 112 seeks, 2 scans, 0 lookups
- Size: 3464.14 MB

**_dta_index_CrossRefs_9_457768688__K2_K3_K1_K5_K6_K7_K4_K15_K16** (NONCLUSTERED)
- Key columns: `Active, ItemId, CrossRefId, CatalogId, CatalogPrice, Page, VendorItemCode, GrossPrice, DoNotDiscount`
- Usage: 3,352 seeks, 29 scans, 0 lookups
- Size: 11519.40 MB

**SK_CatItem** (NONCLUSTERED)
- Key columns: `CatalogId, ItemId, Active`
- Usage: 152,934 seeks, 10 scans, 0 lookups
- Size: 3227.78 MB

**SK_Item** (NONCLUSTERED)
- Key columns: `ItemId`
- Included: `CrossRefId`
- Usage: 89,911 seeks, 1 scans, 0 lookups
- Size: 2895.16 MB

**SK_CatalogActiveLastUpdated** (NONCLUSTERED)
- Key columns: `Active, CatalogId, DateUpdated`
- Usage: 30 seeks, 1 scans, 0 lookups
- Size: 3396.52 MB

**SKI_UniqueCatalog_ImageURLId** (NONCLUSTERED)
- Key columns: `UniqueItemNumber, CatalogId`
- Included: `ImageURL, CrossRefId, Active`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 15160.90 MB

***[Unique]* SKI_CrossRef_** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `Active, ItemId, VendorItemCode, CatalogId, Page, PackedCode`
- Usage: 52,953 seeks, 339 scans, 0 lookups
- Size: 8273.39 MB

**SKI_ItemActive_Etc** (NONCLUSTERED)
- Key columns: `ItemId, Active, CatalogId`
- Included: `CrossRefId, VendorItemCode, Page, PackedCode, CatalogYear, GrossPrice, CatalogPrice, DoNotDiscount`
- Usage: 7,636,159 seeks, 1 scans, 0 lookups
- Size: 14326.34 MB

**SKI_PackedCatalogActive_Item** (NONCLUSTERED)
- Key columns: `PackedCode, CatalogId, Active`
- Included: `CrossRefId, ItemId`
- Usage: 153,770 seeks, 1 scans, 0 lookups
- Size: 6706.31 MB

**SKI_PackedItem_Page** (NONCLUSTERED)
- Key columns: `PackedCode, Active, ItemId, CatalogId`
- Included: `Page, CatalogYear, Manufacturor, ManufacturorPartNumber, GrossPrice, DoNotDiscount`
- Usage: 2,900 seeks, 1 scans, 0 lookups
- Size: 14554.84 MB

**SK_ActiveCatalogSDSRef** (NONCLUSTERED)
- Key columns: `Active, CatalogId, MSDSRef`
- Usage: 844 seeks, 2 scans, 0 lookups
- Size: 2493.45 MB

**SKI_ActiveSDSRef_Catalog** (NONCLUSTERED)
- Key columns: `Active, MSDSRef`
- Included: `CatalogId, ItemId, VendorItemCode, Manufacturor, ManufacturorPartNumber, ImageURL`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 15261.21 MB

**ski_VICCatalogActive_DateUpdatedCrossRefIdImageURL** (NONCLUSTERED)
- Key columns: `VendorItemCode, CatalogId, Active`
- Included: `DateUpdated, CrossRefId, ImageURL`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 17183.65 MB

**ski_CatActiveManufacturerPartNumber_VICUPCSDManUnique** (NONCLUSTERED)
- Key columns: `CatalogId, Active, ManufacturorPartNumber`
- Included: `VendorItemCode, UPC_ISBN, ShortDescription, Manufacturor, UniqueItemNumber`
- Usage: 47 seeks, 2 scans, 0 lookups
- Size: 14718.53 MB

**IX_CrossRefs_MSDSRef_ItemId** (NONCLUSTERED)
- Key columns: `MSDSRef, ItemId, Active`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 3530.20 MB

**CrossRefs_MinimumOrderQuantity_index** (NONCLUSTERED)
- Key columns: `MinimumOrderQuantity`
- Usage: 0 seeks, 9 scans, 0 lookups
- Size: 2048.00 MB

**SKI_ImageURLCatalogActive_VendorItemCodeUnique** (NONCLUSTERED)
- Key columns: `ImageURL, CatalogId, Active`
- Included: `CrossRefId, VendorItemCode, UniqueItemNumber`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 14645.02 MB

**SK_AIDate** (NONCLUSTERED)
- Key columns: `AIDate`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 2908.26 MB

**SKI_HashKey_CrossRefId** (NONCLUSTERED)
- Key columns: `HashKey, CatalogId, Active`
- Included: `CrossRefId, Manufacturor, ManufacturorPartNumber, FullDescription, ShortDescription`
- Usage: 1,315,167 seeks, 1 scans, 0 lookups
- Size: 43069.17 MB

**SKI_AIDate_KashKey** (NONCLUSTERED)
- Key columns: `AIDate`
- Included: `HashKey`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 5187.97 MB


### dbo.CSCommands

*Table rows: 16*

****[PK]** PK__CSComman__4EE1C29071B84738** (CLUSTERED)
- Key columns: `CSCommandId`
- Usage: 1 seeks, 3,305 scans, 0 lookups
- Size: 0.02 MB


### dbo.CSMessageFiles

*Table rows: 0*

****[PK]** PK__CSMessag__D10EA1397F6BDA51** (CLUSTERED)
- Key columns: `CSMessageFileID`
- Usage: 1 seeks, 27 scans, 0 lookups
- Size: 0.00 MB


### dbo.CSMessages

*Table rows: 11,622*

****[PK]** PK__CSMessag__B3A813227B9B496D** (CLUSTERED)
- Key columns: `CSMessageID`
- Usage: 51 seeks, 3 scans, 0 lookups
- Size: 3.14 MB


### dbo.CSRep

*Table rows: 45*

****[PK]** PK_CSRep** (CLUSTERED)
- Key columns: `CSRepId`
- Usage: 19,678 seeks, 9,826 scans, 0 lookups
- Size: 0.02 MB

**SK_User** (NONCLUSTERED)
- Key columns: `UserId`
- Usage: 36,054 seeks, 20,211 scans, 0 lookups
- Size: 0.02 MB


### dbo.CXmlSession

*Table rows: 64,854*

****[PK]** PK__CXmlSession__4AB2BD59** (CLUSTERED)
- Key columns: `SessionId`
- Usage: 368,971 seeks, 235 scans, 0 lookups
- Size: 18.04 MB


### dbo.DebugMsgs

*Table rows: 20,848,708*

****[PK]** PK_DebugMsgs1** (CLUSTERED)
- Key columns: `SysId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 7368.47 MB

**Idx_LogDate** (NONCLUSTERED)
- Key columns: `LogDate`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 447.08 MB


### dbo.DebugMsgs_Orig

*Table rows: 5,211,696*

****[PK]** PK_DebugMsgs** (CLUSTERED)
- Key columns: `sysid`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1827.66 MB


### dbo.Detail

*Table rows: 30,842,292*

****[PK]** PK_Detail** (CLUSTERED)
- Key columns: `DetailId`
- Usage: 6,151,987 seeks, 51 scans, 3,370,512 lookups
- Size: 19390.39 MB

**SK_Requisition** (NONCLUSTERED)
- Key columns: `RequisitionId`
- Usage: 1,554,404 seeks, 111 scans, 0 lookups
- Size: 488.98 MB

**SK_ReqSortSeq** (NONCLUSTERED)
- Key columns: `RequisitionId, SortSeq`
- Usage: 10,947 seeks, 1 scans, 0 lookups
- Size: 1461.27 MB

***[Unique]* SKI_Detail_RequisitionItem** (NONCLUSTERED)
- Key columns: `DetailId`
- Included: `RequisitionId, ItemId, BidItemId, ExtraDescription, SortSeq`
- Usage: 671,867 seeks, 0 scans, 0 lookups
- Size: 1633.41 MB

**SKI_CrossRef_BidItemId** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `BidItemId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 624.30 MB

**SK_ReqItem** (NONCLUSTERED)
- Key columns: `RequisitionId, ItemId, DetailId`
- Included: `ExtraDescription, OriginalItemId`
- Usage: 255,048 seeks, 6 scans, 0 lookups
- Size: 752.77 MB

**ti_CrossRef_Detail** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `DetailId`
- Usage: 0 seeks, 10 scans, 0 lookups
- Size: 484.73 MB

***[Unique]* SK_DetailReq** (NONCLUSTERED)
- Key columns: `DetailId, RequisitionId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 496.29 MB

**SK_ItemReq** (NONCLUSTERED)
- Key columns: `ItemId, RequisitionId`
- Usage: 3,837 seeks, 2 scans, 0 lookups
- Size: 652.70 MB

**_dta_index_Detail_9_16055143__K2_K4_K7** (NONCLUSTERED)
- Key columns: `RequisitionId, ItemId, Quantity`
- Usage: 1,936,153 seeks, 0 scans, 0 lookups
- Size: 758.42 MB

**SK_BHOnly** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 506.61 MB

**SKI_MustBeBid_DetailReqItemPrice** (NONCLUSTERED)
- Key columns: `ItemMustBeBid`
- Included: `DetailId, RequisitionId, ItemId, BidPrice, AwardId, VendorId, BidItemId, BidHeaderId`
- Usage: 29,778 seeks, 468 scans, 0 lookups
- Size: 1493.47 MB

**_dta_index_Detail_7_581629165__K1_K2_7** (NONCLUSTERED)
- Key columns: `DetailId, RequisitionId`
- Included: `Quantity`
- Usage: 8 seeks, 1 scans, 0 lookups
- Size: 594.53 MB

**_dta_index_Detail_7_581629165__K1_K2_K4_29_30** (NONCLUSTERED)
- Key columns: `DetailId, RequisitionId, ItemId`
- Included: `BidItemId, ExtraDescription`
- Usage: 0 seeks, 5 scans, 0 lookups
- Size: 727.85 MB

**SKI_Requisition_QuantityBidPriceVendorBidHeader** (NONCLUSTERED)
- Key columns: `RequisitionId`
- Included: `Quantity, BidPrice, VendorId, BidHeaderId, DetailId, ItemId, BidItemId, ItemMustBeBid, AddedFromAddenda`
- Usage: 5,227,495 seeks, 1 scans, 0 lookups
- Size: 1729.45 MB

**IX_Detail_RequisitionId_ItemId** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `RequisitionId, ItemId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 752.95 MB

**SKI_BidItem_QuantityDetailReq** (NONCLUSTERED)
- Key columns: `BidItemId`
- Included: `Quantity, DetailId, RequisitionId`
- Usage: 11 seeks, 1 scans, 0 lookups
- Size: 833.67 MB

**Detail_ItemId_index** (NONCLUSTERED)
- Key columns: `ItemId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 658.55 MB


### dbo.DetailChangeLog

*Table rows: 2,924,942*

****[PK]** PK__DetailChangeLog__265B8A40** (CLUSTERED)
- Key columns: `DetailChangeId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 335.74 MB

**SK_Requisition** (NONCLUSTERED)
- Key columns: `RequisitionId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 36.01 MB

**SK_Detail** (NONCLUSTERED)
- Key columns: `DetailId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 35.95 MB

**SK_Item** (NONCLUSTERED)
- Key columns: `ItemId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 192.48 MB

**SK_User** (NONCLUSTERED)
- Key columns: `UserId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 46.41 MB

**SK_DetailOldNewQty** (NONCLUSTERED)
- Key columns: `DetailId, OrigQty, NewQty`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 73.37 MB


### dbo.DetailChanges

*Table rows: 26,502,061*

****[PK]** PK__DetailChanges__2F8FEEBF** (CLUSTERED)
- Key columns: `DetailChangeId`
- Usage: 0 seeks, 5 scans, 0 lookups
- Size: 1955.76 MB

**SK_Detail** (NONCLUSTERED)
- Key columns: `DetailId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 408.74 MB

**SK_Requisition** (NONCLUSTERED)
- Key columns: `RequisitionId`
- Usage: 1 seeks, 6 scans, 0 lookups
- Size: 408.32 MB

**SK_DetailOldNewQtyDate** (NONCLUSTERED)
- Key columns: `DetailId, OrigQty, NewQty, ChangeDate`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 891.52 MB


### dbo.DetailNotifications

*Table rows: 2,779,169*

****[PK]** PK__DetailNo__B32A2B6002470E89** (CLUSTERED)
- Key columns: `DetailNotificationId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 298.38 MB

**SKI_DetailDateNewVendorOrigVendor_Id** (NONCLUSTERED)
- Key columns: `DetailId, DateCreated, OrigVendorId, NewVendorId`
- Included: `DetailNotificationId, OrigItemId, NewItemId, OrigBidPrice, NewBidPrice`
- Usage: 41 seeks, 1 scans, 0 lookups
- Size: 254.95 MB

**SKI_Notification_DetailId** (NONCLUSTERED)
- Key columns: `NotificationId`
- Included: `DetailId, DetailNotificationId, DateCreated, OrigItemId, NewItemId, OrigVendorId, NewVendorId, OrigBidPrice, NewBidPrice`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 245.71 MB

**SKI_DetailDate_Etal** (NONCLUSTERED)
- Key columns: `DetailId, DateCreated`
- Included: `DetailNotificationId, NotificationId, OrigItemId, NewItemId, OrigVendorId, NewVendorId, OrigBidPrice, NewBidPrice`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 277.34 MB


### dbo.DetailUploads

*Table rows: 0*

****[PK]** PK__DetailUp__CA367AE1FDEFCFEB** (CLUSTERED)
- Key columns: `DetailUploadId`
- Usage: 1,312 seeks, 6,310 scans, 0 lookups
- Size: 0.00 MB


### dbo.District

*Table rows: 968*

****[PK]** PK_District** (CLUSTERED)
- Key columns: `DistrictId`
- Usage: 6,012,339 seeks, 46,418 scans, 1,702 lookups
- Size: 0.50 MB

**SK_DistrictCode** (NONCLUSTERED)
- Key columns: `DistrictCode`
- Usage: 535 seeks, 0 scans, 0 lookups
- Size: 0.04 MB

**SK_CSRep** (NONCLUSTERED)
- Key columns: `CSRepId`
- Usage: 1 seeks, 2,443 scans, 0 lookups
- Size: 0.03 MB

**SK_POSchool** (NONCLUSTERED)
- Key columns: `POsBySchool`
- Usage: 0 seeks, 1,903 scans, 0 lookups
- Size: 0.03 MB

**_dta_index_District_7_1582680736__K1_4** (NONCLUSTERED)
- Key columns: `DistrictId`
- Included: `Name`
- Usage: 367,824 seeks, 7,720 scans, 0 lookups
- Size: 0.09 MB

***[Unique]* SK_DistrictIdActiveCountyStateDC** (NONCLUSTERED)
- Key columns: `DistrictId, Active, County, State, DistrictCode`
- Usage: 160,681 seeks, 2,301 scans, 0 lookups
- Size: 0.07 MB

**_dta_index_District_7_605438543__K1_2_4_5_6_7_8_9_10_12_21_22_53** (NONCLUSTERED)
- Key columns: `DistrictId`
- Included: `DistrictCode, Name, Address1, Address2, Address3, City, State, Zipcode, POsBySchool, PhoneNumber, Fax, UseEDSVendorCodes`
- Usage: 9,631 seeks, 995 scans, 0 lookups
- Size: 0.18 MB


### dbo.DistrictCategories

*Table rows: 125,118*

****[PK]** PK_DistrictCategories** (CLUSTERED)
- Key columns: `DistrictCategoryId`
- Usage: 821 seeks, 1,694 scans, 2,822,080 lookups
- Size: 8.13 MB

**SKI_ActiveCategory_District** (NONCLUSTERED)
- Key columns: `Active, CategoryId`
- Included: `DistrictId`
- Usage: 4,767 seeks, 26 scans, 0 lookups
- Size: 3.77 MB

**SK_Category** (NONCLUSTERED)
- Key columns: `CategoryId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 2.74 MB

**SK_DistrictCategory** (NONCLUSTERED)
- Key columns: `DistrictId, CategoryId`
- Usage: 2,554,197 seeks, 0 scans, 0 lookups
- Size: 4.29 MB

**SK_DKAAllow** (NONCLUSTERED)
- Key columns: `AllowAddenda, DistrictId, CategoryId, Active`
- Usage: 317,514 seeks, 1 scans, 0 lookups
- Size: 4.08 MB

**_dta_index_DistrictCategories_9_763149764__K3_K4_K9** (NONCLUSTERED)
- Key columns: `CategoryId, DistrictId, AllowAddenda`
- Usage: 153,775 seeks, 0 scans, 0 lookups
- Size: 3.69 MB

**_dta_index_DistrictCategories_7_1550680622__K4_K3_K1_5** (NONCLUSTERED)
- Key columns: `DistrictId, CategoryId, DistrictCategoryId`
- Included: `Title`
- Usage: 903,386 seeks, 0 scans, 0 lookups
- Size: 4.20 MB

**SKI_DistrictCategory_Active** (NONCLUSTERED)
- Key columns: `DistrictId, CategoryId`
- Included: `DistrictCategoryId, Active, Title, AllowAddenda, AllowIncidentals, OrderBookTypeId, BidItemsOnly`
- Usage: 4,133,042 seeks, 396 scans, 0 lookups
- Size: 6.23 MB


### dbo.DistrictCategoryTitles

*Table rows: 0*

****[PK]** PK__DistrictCategory__7266E4EE** (CLUSTERED)
- Key columns: `DistrictCategoryTitleId`
- Usage: 1 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.DistrictCharges

*Table rows: 22,477*

****[PK]** PK__DistrictCharges__330F729B** (CLUSTERED)
- Key columns: `DistrictChargeId`
- Usage: 1 seeks, 320 scans, 0 lookups
- Size: 2.65 MB


### dbo.DistrictChargesNotes

*Table rows: 0*

****[PK]** PK__District__ABAFBCC17B56E6FB** (CLUSTERED)
- Key columns: `DistrictChargeNoteId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.DistrictContacts

*Table rows: 3,815*

****[PK]** PK__District__DEBBC8B95C331A6D** (CLUSTERED)
- Key columns: `DistrictContactId`
- Usage: 58,301 seeks, 283 scans, 11,988 lookups
- Size: 1.10 MB

**SK_DistrictContacttype** (NONCLUSTERED)
- Key columns: `DistrictId, DistrictContactTypeId`
- Usage: 69,905 seeks, 4 scans, 0 lookups
- Size: 0.16 MB


### dbo.DistrictContactTypes

*Table rows: 7*

****[PK]** PK__District__D7F61BD758628989** (CLUSTERED)
- Key columns: `DistrictContactTypeId`
- Usage: 623 seeks, 1,148 scans, 0 lookups
- Size: 0.02 MB


### dbo.DistrictContinuances

*Table rows: 14,395*

****[PK]** PK__District__3214EC073BD65497** (CLUSTERED)
- Key columns: `Id`
- Usage: 1,219 seeks, 2,418 scans, 0 lookups
- Size: 2.21 MB


### dbo.DistrictNotes

*Table rows: 75*

****[PK]** PK_DistrictNotes** (CLUSTERED)
- Key columns: `DistrictNotesId`
- Usage: 2 seeks, 89 scans, 0 lookups
- Size: 0.04 MB


### dbo.DistrictNotifications

*Table rows: 6,043*

****[PK]** PK__District__89A5C1BB4AB835BD** (CLUSTERED)
- Key columns: `DistrictNotificationId`
- Usage: 0 seeks, 938 scans, 0 lookups
- Size: 0.80 MB


### dbo.DistrictPP

*Table rows: 9,242*

****[PK]** PK_DistrictPP** (CLUSTERED)
- Key columns: `DistrictPPId`
- Usage: 75 seeks, 0 scans, 0 lookups
- Size: 0.42 MB

**SK_DistrictId** (NONCLUSTERED)
- Key columns: `DistrictId`
- Usage: 31 seeks, 0 scans, 0 lookups
- Size: 0.17 MB

**SK_DistrictPP** (NONCLUSTERED)
- Key columns: `DistrictId, PricePlanId`
- Usage: 474,696 seeks, 14 scans, 0 lookups
- Size: 0.22 MB

**SK_PPDistrict** (NONCLUSTERED)
- Key columns: `PricePlanId, DistrictId`
- Usage: 362,921 seeks, 2,535 scans, 0 lookups
- Size: 0.25 MB


### dbo.DistrictReports

*Table rows: 11*

****[PK]** PK__District__CF9EF8CE03D372A6** (CLUSTERED)
- Key columns: `DistrictReportId`
- Usage: 18 seeks, 16 scans, 0 lookups
- Size: 0.02 MB


### dbo.DistrictTypes

*Table rows: 6*

****[PK]** PK_DistrictTypes** (CLUSTERED)
- Key columns: `DistrictTypeId`
- Usage: 27,942 seeks, 475 scans, 0 lookups
- Size: 0.02 MB


### dbo.DistrictVendor

*Table rows: 315,687*

****[PK]** PK_DistrictVendor** (CLUSTERED)
- Key columns: `DistrictVendorId`
- Usage: 117 seeks, 0 scans, 0 lookups
- Size: 14.31 MB

***[Unique]* SK_DistrictVendor** (NONCLUSTERED)
- Key columns: `DistrictId, VendorId`
- Included: `DistrictVendorId, VendorsAccountCode`
- Usage: 6,776 seeks, 465 scans, 0 lookups
- Size: 6.51 MB

**SK_District** (NONCLUSTERED)
- Key columns: `DistrictId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 5.30 MB

**SKI_District_DistrictvendorVendorValueVAC** (NONCLUSTERED)
- Key columns: `DistrictId, VendorId, Active`
- Included: `DistrictVendorId, Value, VendorsAccountCode`
- Usage: 833,515 seeks, 144 scans, 0 lookups
- Size: 10.56 MB


### dbo.DMSBidDocuments

*Table rows: 29,032*

****[PK]** PK_DMSBidDocuments** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 27,226 scans, 0 lookups
- Size: 9.73 MB


### dbo.DMSSDSDocuments

*Table rows: 602*

****[PK]** PK__DMSSDSDo__3214EC07C9C46946** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 1,268 scans, 1 lookups
- Size: 0.11 MB

**SKI_MSDS_IDDoc** (NONCLUSTERED)
- Key columns: `MSDSId, DocId`
- Included: `Id`
- Usage: 6,373,142 seeks, 2 scans, 0 lookups
- Size: 0.05 MB


### dbo.DMSVendorBidDocuments

*Table rows: 736,489*

****[PK]** PK_DMSVendorBidDocuments** (CLUSTERED)
- Key columns: `Id`
- Usage: 4 seeks, 634 scans, 32,016 lookups
- Size: 253.51 MB

**SKI_BidHeaderVendorCodeDocType_Id** (NONCLUSTERED)
- Key columns: `BidHeaderId, VendorCode, DocType`
- Included: `Id`
- Usage: 33,690 seeks, 538 scans, 0 lookups
- Size: 52.93 MB


### dbo.DMSVendorDocuments

*Table rows: 6,485*

****[PK]** PK_DMSVendorDocuments** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 2,086 scans, 0 lookups
- Size: 2.98 MB


### dbo.dtproperties

*Table rows: 42*

****[PK]** pk_dtproperties** (CLUSTERED)
- Key columns: `id, property`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.16 MB


### dbo.EmailBlast

*Table rows: 16,701*

****[PK]** PK_EmailBlast** (CLUSTERED)
- Key columns: `EmailBlastId`
- Usage: 10,080 seeks, 699 scans, 0 lookups
- Size: 169.64 MB


### dbo.EmailBlastCopy

*Table rows: 3*

****[PK]** PK_EmailBlastCopy** (CLUSTERED)
- Key columns: `EmailBlastId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.02 MB


### dbo.EmailBlastLog

*Table rows: 1,437,244*

****[PK]** PK_EmailBlastLog** (CLUSTERED)
- Key columns: `EmailBlastLogId`
- Usage: 51 seeks, 21 scans, 0 lookups
- Size: 3779.13 MB


### dbo.FreezeItems

*Table rows: 15,435*

****[PK]** PK__FreezeIt__3214EC074D34D55C** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1.79 MB

**SKI_BidHeaderItemVendor_Etc** (NONCLUSTERED)
- Key columns: `BidHeaderId, ItemId, VendorId`
- Included: `Id, CrossRefId, VendorItemCode, GrossPrice`
- Usage: 99,731 seeks, 3,711 scans, 0 lookups
- Size: 1.36 MB

**ti_Crossref_Id** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `Id`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.41 MB


### dbo.FreezeItems2015

*Table rows: 102,339*

**SKI_Detail_Etc** (NONCLUSTERED)
- Key columns: `DetailId`
- Included: `OrigVendorItemCode, OrigBidPrice, OrigVendorId, OrigAwardId, OrigCatalogId, OrigCatalogPrice`
- Usage: 103,401 seeks, 1 scans, 0 lookups
- Size: 6.64 MB


### dbo.Headings

*Table rows: 166,699*

****[PK]** PK_Headings** (CLUSTERED)
- Key columns: `HeadingId`
- Usage: 177,083 seeks, 580 scans, 23,500 lookups
- Size: 19.23 MB

**_dta_index_Headings_7_1374679995__K1_K2_6** (NONCLUSTERED)
- Key columns: `HeadingId, Active`
- Included: `Title`
- Usage: 810,035 seeks, 0 scans, 0 lookups
- Size: 8.00 MB

**_dta_index_Headings_7_1374679995__K2_K1_6** (NONCLUSTERED)
- Key columns: `Active, HeadingId`
- Included: `Title`
- Usage: 19,025 seeks, 0 scans, 0 lookups
- Size: 7.91 MB

**SKI_ExpandAll_Heading** (NONCLUSTERED)
- Key columns: `ExpandAll`
- Included: `HeadingId`
- Usage: 47 seeks, 5 scans, 0 lookups
- Size: 2.35 MB

***[Unique]* SKI_HeadingId_Title** (NONCLUSTERED)
- Key columns: `HeadingId`
- Included: `Title`
- Usage: 0 seeks, 149 scans, 0 lookups
- Size: 7.50 MB

**SK_ActiveCategoryTitleDistrict** (NONCLUSTERED)
- Key columns: `Active, CategoryId, Title, DistrictId`
- Usage: 6,132 seeks, 4,687 scans, 0 lookups
- Size: 11.34 MB


### dbo.HolidayCalendar

*Table rows: 29*

****[PK]** HolidayCalendar_pk** (CLUSTERED)
- Key columns: `Year, Month`
- Usage: 1,275 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

**HolidayCalendar_Year_Month_index** (NONCLUSTERED)
- Key columns: `Year, Month`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.HolidayCalendarVendor

*Table rows: 7*

****[PK]** HolidayCalendarVendor_pk** (CLUSTERED)
- Key columns: `Year, Month, VendorId`
- Usage: 5 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

**HolidayCalendarVendor_Year_Month_index** (NONCLUSTERED)
- Key columns: `Year, Month, VendorId`
- Usage: 1,280 seeks, 1 scans, 0 lookups
- Size: 0.02 MB


### dbo.ImageErrors

*Table rows: 26,727*

****[PK]** PK__ImageErr__FE6831C29F922480** (CLUSTERED)
- Key columns: `imageErrorId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 53.36 MB

**NonClusteredIndex-20210628-091606** (NONCLUSTERED)
- Key columns: `imageURL, imageErrorId`
- Included: `error, logDate`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 36.91 MB


### dbo.ImageLog

*Table rows: 1,788,706*

****[PK]** PK__ImageLog** (CLUSTERED)
- Key columns: `imageLogId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 2156.07 MB

**NonClusteredIndex-20250321-091731** (NONCLUSTERED)
- Key columns: `imageURL, writeStatus, writeDate DESC`
- Included: `imageLogId, imageId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 243.83 MB


### dbo.Images

*Table rows: 1,736,177*

****[PK]** PK__Images__336E9B55906715A9** (CLUSTERED)
- Key columns: `imageId`
- Usage: 0 seeks, 0 scans, 1,746 lookups
- Size: 971.13 MB

**SK_URLLoaded** (NONCLUSTERED)
- Key columns: `imageURL, dateLoaded`
- Usage: 1,746 seeks, 0 scans, 0 lookups
- Size: 184.19 MB

**DPA_RECIDX_416** (NONCLUSTERED)
- Key columns: `pHash, imageSize, imageFormat`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 156.86 MB


### dbo.ImportCatalogDetail

*Table rows: 17,646*

****[PK]** PK_ImportCatalogDetail** (CLUSTERED)
- Key columns: `ImportCatalogDetailId`
- Usage: 83 seeks, 56 scans, 0 lookups
- Size: 2.11 MB


### dbo.ImportCatalogHeader

*Table rows: 2,822*

****[PK]** PK_ImportCatalogHeader** (CLUSTERED)
- Key columns: `ImportCatalogHeaderId`
- Usage: 47 seeks, 121 scans, 0 lookups
- Size: 0.16 MB


### dbo.ImportDetail

*Table rows: 882,935*

****[PK]** PK_ImportDetail** (CLUSTERED)
- Key columns: `ImportDetailId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 239.72 MB


### dbo.ImportMessages

*Table rows: 5,500*

****[PK]** PK_ImportMessages** (CLUSTERED)
- Key columns: `MessageId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.45 MB


### dbo.ImportProcesses

*Table rows: 754*

****[PK]** PK_Processes** (CLUSTERED)
- Key columns: `ProcessId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.05 MB


### dbo.Imports

*Table rows: 301*

****[PK]** PK_Imports** (CLUSTERED)
- Key columns: `ImportId`
- Usage: 0 seeks, 6 scans, 0 lookups
- Size: 0.05 MB


### dbo.InstructionBookContents

*Table rows: 31*

****[PK]** PK__Instruct__9001CA154AB388B0** (CLUSTERED)
- Key columns: `IBCId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.07 MB


### dbo.InstructionBookTypes

*Table rows: 6*

****[PK]** PK__Instruct__E64A5E1636AC9003** (CLUSTERED)
- Key columns: `IBTypeId`
- Usage: 23,392 seeks, 2,663 scans, 0 lookups
- Size: 0.02 MB


### dbo.Instructions

*Table rows: 7*

****[PK]** PK__Instruct__CE06947129C65AB9** (CLUSTERED)
- Key columns: `InstructionId`
- Usage: 0 seeks, 22,239 scans, 0 lookups
- Size: 0.04 MB


### dbo.Invoices

*Table rows: 0*

****[PK]** PK__Invoices__1F247CCC** (CLUSTERED)
- Key columns: `InvoiceId`
- Usage: 2 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.InvoiceTypes

*Table rows: 0*

****[PK]** PK__InvoiceTypes__1D3C345A** (CLUSTERED)
- Key columns: `InvoiceTypeId`
- Usage: 2 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.IPQueue

*Table rows: 5,038*

****[PK]** PK__IPQueue__4EC586B738FC4C6D** (CLUSTERED)
- Key columns: `IPQueueId`
- Usage: 0 seeks, 76,026 scans, 0 lookups
- Size: 0.54 MB


### dbo.IPQueueUsers

*Table rows: 489,217*

****[PK]** PK__IPQueueU__5793EB133CCCDD51** (CLUSTERED)
- Key columns: `IPQueueUserId`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 85.22 MB


### dbo.ItemContractPrices

*Table rows: 0*

****[PK]** PK__ItemCont__9F03B0683B0730CC** (CLUSTERED)
- Key columns: `ICPId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.ItemDocuments

*Table rows: 0*

****[PK]** PK__ItemDocu__2D6D2FEFEB03F9C0** (CLUSTERED)
- Key columns: `ItemDocumentId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.Items

*Table rows: 30,153,956*

****[PK]** PK_Items** (CLUSTERED)
- Key columns: `ItemId`
- Usage: 7,162,948 seeks, 49 scans, 779 lookups
- Size: 8107.64 MB

**SK_ItemCodeCategory** (NONCLUSTERED)
- Key columns: `ItemCode, CategoryId`
- Usage: 783 seeks, 1 scans, 0 lookups
- Size: 1024.01 MB

***[Unique]* SKI_Item_CategoryHeadingKeywordItemCodeUnit** (NONCLUSTERED)
- Key columns: `ItemId`
- Included: `CategoryId, ItemCode, UnitId, HeadingId, KeywordId`
- Usage: 452,671 seeks, 2 scans, 0 lookups
- Size: 1212.10 MB

**SKI_HeadingActiveCategoryDistrict_Item** (NONCLUSTERED)
- Key columns: `HeadingId, Active, CategoryId, DistrictId`
- Included: `ItemId`
- Usage: 14,300 seeks, 0 scans, 0 lookups
- Size: 744.48 MB

**SK_ItemItemCodeCategory** (NONCLUSTERED)
- Key columns: `ItemId, ItemCode, CategoryId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 920.99 MB

**DPA_RECIDX_18** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `CategoryId`
- Usage: 6 seeks, 49 scans, 0 lookups
- Size: 529.26 MB

**SK_Heading** (NONCLUSTERED)
- Key columns: `HeadingId`
- Included: `ItemId`
- Usage: 48 seeks, 1 scans, 0 lookups
- Size: 471.72 MB

***[Unique]* SKI_ItemCategoryActive_HeadingKeyword** (NONCLUSTERED)
- Key columns: `ItemId, CategoryId, Active`
- Included: `HeadingId, KeywordId, DistrictId`
- Usage: 9 seeks, 0 scans, 0 lookups
- Size: 773.78 MB

**_dta_index_Items_12_1509632471__K1_K6_K15_K8_K24_5_10** (NONCLUSTERED)
- Key columns: `ItemId, UnitId, DistrictId, HeadingId, KeywordId`
- Included: `Description, SortSeq`
- Usage: 3,109 seeks, 1 scans, 0 lookups
- Size: 3647.90 MB

**SK_CategoryUnit** (NONCLUSTERED)
- Key columns: `CategoryId, UnitId`
- Usage: 525 seeks, 6 scans, 0 lookups
- Size: 572.18 MB

**SK_ItemActiveDistrict** (NONCLUSTERED)
- Key columns: `ItemId, Active, DistrictId`
- Usage: 152,981 seeks, 2 scans, 0 lookups
- Size: 482.28 MB

**SKI_ActiveCategory_Heading** (NONCLUSTERED)
- Key columns: `Active, CategoryId`
- Included: `HeadingId`
- Usage: 10 seeks, 0 scans, 0 lookups
- Size: 566.45 MB

**ski_CategoryDistrictActive_Heading** (NONCLUSTERED)
- Key columns: `CategoryId, DistrictId, Active`
- Included: `HeadingId, ItemId`
- Usage: 4,843 seeks, 0 scans, 0 lookups
- Size: 688.03 MB

**_dta_index_Items_7_1509632471__K1_K24_K6_K15_K18_K11_K7_K3_K8_4_5_10_12_16_17_19_20_22** (NONCLUSTERED)
- Key columns: `ItemId, KeywordId, UnitId, DistrictId, VendorId, EditionId, ParentCatalogId, CategoryId, HeadingId`
- Included: `ItemCode, Description, SortSeq, CopyrightYear, BrandName, ManufacturorNumber, VendorPartNumber, ItemsPerUnit, ExtraDetail`
- Usage: 3,530,391 seeks, 56 scans, 0 lookups
- Size: 5125.30 MB

**SK_ItemHeading** (NONCLUSTERED)
- Key columns: `Active`
- Included: `ItemId, HeadingId`
- Usage: 250 seeks, 35 scans, 0 lookups
- Size: 447.38 MB

**SKI_ItemCode** (NONCLUSTERED)
- Key columns: `ItemCode`
- Included: `SortSeq`
- Usage: 1,642 seeks, 1 scans, 0 lookups
- Size: 1738.48 MB

**SKI_ActiveHeading_ItemItemcodeDescrUnitSortseq** (NONCLUSTERED)
- Key columns: `Active, HeadingId`
- Included: `ItemId, ItemCode, Description, UnitId, SortSeq, DistrictId, ListPrice`
- Usage: 2 seeks, 1 scans, 0 lookups
- Size: 4256.57 MB

**SK_CategoryPackedcode_ItemIdActiveItemCodeDescUnitParentHeadingRTKSortDist** (NONCLUSTERED)
- Key columns: `CategoryId, PackedCode`
- Included: `ItemId, Active, ItemCode, Description, UnitId, ParentCatalogId, HeadingId, RTK, SortSeq, DistrictId`
- Usage: 8,712 seeks, 4 scans, 0 lookups
- Size: 4452.03 MB


### dbo.ItemUpdates

*Table rows: 198,886*

****[PK]** PK_ItemUpdates** (CLUSTERED)
- Key columns: `ItemUpdateId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 16.12 MB


### dbo.jSessions

*Table rows: 0*

****[PK]** PK__jSession__DD84209B32A6F4F5** (CLUSTERED)
- Key columns: `jSessionId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.Keywords

*Table rows: 25,261*

****[PK]** PK_Keywords** (CLUSTERED)
- Key columns: `KeywordId`
- Usage: 80,983 seeks, 0 scans, 25,109 lookups
- Size: 2.09 MB

**SK_Heading** (NONCLUSTERED)
- Key columns: `HeadingId`
- Usage: 25,112 seeks, 3 scans, 0 lookups
- Size: 0.39 MB

**SK_Category** (NONCLUSTERED)
- Key columns: `CategoryId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.44 MB

**_dta_index_Keywords_7_1246679539__K2_K1_6** (NONCLUSTERED)
- Key columns: `Active, KeywordId`
- Included: `Keyword`
- Usage: 580,169 seeks, 0 scans, 0 lookups
- Size: 0.74 MB

**_dta_index_Keywords_7_1246679539__K1_6** (NONCLUSTERED)
- Key columns: `KeywordId`
- Included: `Keyword`
- Usage: 214,293 seeks, 2 scans, 0 lookups
- Size: 0.61 MB

***[Unique]* SKI_KeywordId_Keyword** (NONCLUSTERED)
- Key columns: `KeywordId`
- Included: `Keyword`
- Usage: 0 seeks, 848 scans, 0 lookups
- Size: 0.61 MB

**SKI_KeywordHeadingDistrictActive_KeywordId** (NONCLUSTERED)
- Key columns: `Keyword, HeadingId, DistrictId, Active`
- Included: `KeywordId, CategoryId`
- Usage: 9,378 seeks, 1 scans, 0 lookups
- Size: 1.84 MB


### dbo.Ledger

*Table rows: 0*

****[PK]** PK__Ledger__1D072A30** (CLUSTERED)
- Key columns: `LedgerId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.LL_RepArea

*Table rows: 0*

****[PK]** PK_LL_RepArea** (CLUSTERED)
- Key columns: `Ref`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.LL_RepLay

*Table rows: 0*

****[PK]** PK_LL_RepLay** (CLUSTERED)
- Key columns: `Ref`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.ManufacturerProductLines

*Table rows: 14,298*

****[PK]** PK__Manufact__4837625B00E92DC3** (CLUSTERED)
- Key columns: `ManufacturerProductLineId`
- Usage: 3,215 seeks, 64 scans, 0 lookups
- Size: 0.75 MB


### dbo.Manufacturers

*Table rows: 9,007*

****[PK]** PK__Manufact__357E5CC16608FF6F** (CLUSTERED)
- Key columns: `ManufacturerId`
- Usage: 26,625 seeks, 265 scans, 0 lookups
- Size: 1.16 MB


### dbo.MappedItems

*Table rows: 2*

****[PK]** PK__MappedIt__64ED12E457E92F51** (CLUSTERED)
- Key columns: `MappedItemId`
- Usage: 1 seeks, 41 scans, 0 lookups
- Size: 0.02 MB

***[Unique]* SK_Map** (NONCLUSTERED)
- Key columns: `OrigItemId`
- Included: `NewItemId`
- Usage: 190,538 seeks, 2,773 scans, 0 lookups
- Size: 0.02 MB


### dbo.Menus

*Table rows: 4*

****[PK]** PK__Menus__C99ED23062C01C6B** (CLUSTERED)
- Key columns: `MenuId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.02 MB


### dbo.Messages

*Table rows: 0*

****[PK]** PK_Messages** (CLUSTERED)
- Key columns: `MessageId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.Months

*Table rows: 12*

****[PK]** PK__MonthNam__9FA83FA626129C39** (CLUSTERED)
- Key columns: `MonthId`
- Usage: 0 seeks, 235 scans, 0 lookups
- Size: 0.02 MB


### dbo.MSDS

*Table rows: 58,726*

****[PK]** PK_MSDS** (CLUSTERED)
- Key columns: `MSDSId`
- Usage: 1,850 seeks, 15 scans, 0 lookups
- Size: 7.41 MB

**SKI_CurrentVersion_DocId** (NONCLUSTERED)
- Key columns: `CurrentVersionMSDSId`
- Included: `MSDSId, ContentCentralMSDSDocId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.86 MB


### dbo.MSDSDetail

*Table rows: 138,516*

****[PK]** PK_MSDSDetail** (CLUSTERED)
- Key columns: `MSDSDetailID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 9.37 MB

**SKI_MSDSCAS_Id** (NONCLUSTERED)
- Key columns: `MSDSID, RTK_CASFileId`
- Included: `MSDSDetailID`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 2.43 MB


### dbo.MSRPExcelExport

*Table rows: 563*

****[PK]** PK_MSRPExcelExport** (CLUSTERED)
- Key columns: `MSRPExcelExportId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.12 MB


### dbo.MSRPExcelImport

*Table rows: 76,315*

****[PK]** PK_MSRPExcelImport** (CLUSTERED)
- Key columns: `MSRPExcelImportId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 17.23 MB


### dbo.MSRPOptions

*Table rows: 12*

****[PK]** PK__MSRPOpti__FBF27A777BA25A27** (CLUSTERED)
- Key columns: `MSRPOptionId`
- Usage: 942 seeks, 7 scans, 0 lookups
- Size: 0.02 MB

**SKI_Name_OptionId** (NONCLUSTERED)
- Key columns: `MSRPOptionName`
- Included: `MSRPOptionId, Active`
- Usage: 81 seeks, 87 scans, 0 lookups
- Size: 0.02 MB


### dbo.NextNumber

*Table rows: 24,263*

****[PK]** PK_ReqPONext** (CLUSTERED)
- Key columns: `NextNumberId`
- Usage: 44 seeks, 0 scans, 1,389 lookups
- Size: 1.63 MB

***[Unique]* SK_BIS** (NONCLUSTERED)
- Key columns: `BudgetId, IdType, SchoolId`
- Usage: 5,884 seeks, 0 scans, 0 lookups
- Size: 0.60 MB

***[Unique]* IX_NextNumber_Composite** (NONCLUSTERED)
- Key columns: `DistrictId, SchoolId, BudgetId, IdType`
- Included: `Prefix, Suffix, NextNumber`
- Usage: 36,813 seeks, 0 scans, 0 lookups
- Size: 1.37 MB

**SK_IDType** (NONCLUSTERED)
- Key columns: `IdType`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.32 MB

**_dta_index_NextNumber_7_1182679311__K4_K5_3_11** (NONCLUSTERED)
- Key columns: `BudgetId, IdType`
- Included: `SchoolId, FFMessage`
- Usage: 444 seeks, 145 scans, 0 lookups
- Size: 0.58 MB


### dbo.NotificationOptions

*Table rows: 4*

****[PK]** PK__Notifica__EC3B5DF0BADE7CE9** (CLUSTERED)
- Key columns: `NotificationOptionId`
- Usage: 253 seeks, 3,199 scans, 0 lookups
- Size: 0.02 MB


### dbo.Notifications

*Table rows: 720*

***[Unique]* PK_Notifications** (CLUSTERED)
- Key columns: `NotificationId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 3.13 MB


### dbo.OBPrices

*Table rows: 0*

**SK_Item** (NONCLUSTERED)
- Key columns: `ItemId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB

**SK_PricePlan** (NONCLUSTERED)
- Key columns: `PricePlanId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB

**SK_Vendor** (NONCLUSTERED)
- Key columns: `VendorId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB

**SK_Award** (NONCLUSTERED)
- Key columns: `AwardId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB

**SK_Category** (NONCLUSTERED)
- Key columns: `CategoryId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.00 MB

**SK_BidItem** (NONCLUSTERED)
- Key columns: `BidItemId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.00 MB

**SK_PPCat** (NONCLUSTERED)
- Key columns: `PricePlanId, CategoryId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.OBView

*Table rows: 0*

****[PK]** PK__OBView__744F2D60** (CLUSTERED)
- Key columns: `OBDWorkId`
- Usage: 0 seeks, 6 scans, 0 lookups
- Size: 0.00 MB


### dbo.Options

*Table rows: 0*

****[PK]** PK_Options** (CLUSTERED)
- Key columns: `OptionId`
- Usage: 3 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.OptionsLink

*Table rows: 0*

****[PK]** PK_OptionsLink** (CLUSTERED)
- Key columns: `OptionLinkId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.OrderBookAlwaysAdd

*Table rows: 9*

****[PK]** PK_OrderBookAlwaysAdd** (CLUSTERED)
- Key columns: `OBAAId`
- Usage: 0 seeks, 70 scans, 0 lookups
- Size: 0.02 MB


### dbo.OrderBookDetail

*Table rows: 37,804,007*

****[PK]** PK_OrderBookDetail** (CLUSTERED)
- Key columns: `OrderBookDetailId`
- Usage: 0 seeks, 23 scans, 429 lookups
- Size: 4212.03 MB

**SKI_OrderBook_Item** (NONCLUSTERED)
- Key columns: `OrderBookId`
- Included: `ItemId`
- Usage: 715 seeks, 3 scans, 0 lookups
- Size: 676.76 MB

**ti_CrossRef_OrderBookDetailId** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `OrderBookDetailId`
- Usage: 1 seeks, 4 scans, 0 lookups
- Size: 528.70 MB


### dbo.OrderBookDetailOld

*Table rows: 187,630,151*

****[PK]** PK_OrderBookDetailOld** (CLUSTERED)
- Key columns: `OrderBookDetailId`
- Usage: 0 seeks, 22 scans, 0 lookups
- Size: 3446.95 MB

**SK_OrderBook** (NONCLUSTERED)
- Key columns: `OrderBookId`
- Usage: 1 seeks, 4 scans, 0 lookups
- Size: 2542.67 MB

**SK_OrderBookItem** (NONCLUSTERED)
- Key columns: `OrderBookId, ItemId`
- Included: `OrderBookDetailId, BidItemId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 3995.20 MB

**SK_IPKey1** (NONCLUSTERED)
- Key columns: `OrderBookId, Active`
- Included: `OrderBookDetailId, ItemId, BidItemId, Weight, CatalogId, CrossRefId, BidPrice, CatalogPage, CatalogYear, VendorCode, VendorName, VendorItemCode, AwardId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 8831.27 MB

**SKI_OrderBook_OBDetailVendorCodeNameId** (NONCLUSTERED)
- Key columns: `OrderBookId`
- Included: `OrderBookDetailId, VendorCode, VendorName, VendorId`
- Usage: 0 seeks, 5 scans, 0 lookups
- Size: 3333.49 MB


### dbo.OrderBookLog

*Table rows: 474,297*

****[PK]** PK__OrderBookLog__3528CC84** (CLUSTERED)
- Key columns: `OrderBookLogId`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 45.13 MB


### dbo.OrderBooks

*Table rows: 30,399*

****[PK]** PK_OrderBooks** (CLUSTERED)
- Key columns: `OrderBookId`
- Usage: 955 seeks, 19,767 scans, 0 lookups
- Size: 5.30 MB


### dbo.OrderBookTypes

*Table rows: 12*

****[PK]** PK__OrderBookTypes__7405149D** (CLUSTERED)
- Key columns: `OrderBookTypeId`
- Usage: 68 seeks, 53 scans, 0 lookups
- Size: 0.02 MB


### dbo.Payments

*Table rows: 0*

****[PK]** PK__Payments__22F50DB0** (CLUSTERED)
- Key columns: `PaymentId`
- Usage: 1 seeks, 4 scans, 0 lookups
- Size: 0.00 MB


### dbo.PaymentTypes

*Table rows: 0*

****[PK]** PK__PaymentTypes__210CC53E** (CLUSTERED)
- Key columns: `PaymentTypeId`
- Usage: 2 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.PendingApprovals

*Table rows: 567,122*

****[PK]** PK_PendingApprovals** (CLUSTERED)
- Key columns: `SysId`
- Usage: 0 seeks, 5 scans, 630 lookups
- Size: 57.31 MB

**SK_SessionId** (NONCLUSTERED)
- Key columns: `SessionId`
- Usage: 462 seeks, 0 scans, 0 lookups
- Size: 8.84 MB

**SK_LastApproval** (NONCLUSTERED)
- Key columns: `LastApprovalId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 9.09 MB

**SK_SessionNextApproverStatus** (NONCLUSTERED)
- Key columns: `SessionId, NextApproverId, StatusId`
- Usage: 146 seeks, 0 scans, 0 lookups
- Size: 14.13 MB

**SK_SessionRequisition** (NONCLUSTERED)
- Key columns: `SessionId, RequisitionId`
- Usage: 64 seeks, 1 scans, 0 lookups
- Size: 11.83 MB


### dbo.PO

*Table rows: 2,462,030*

****[PK]** PK_PO** (CLUSTERED)
- Key columns: `POId`
- Usage: 18,126 seeks, 23 scans, 927 lookups
- Size: 420.70 MB

**SK_Requisition** (NONCLUSTERED)
- Key columns: `RequisitionId`
- Usage: 87,293 seeks, 157 scans, 0 lookups
- Size: 38.87 MB

**SK__Vendor_ReqPONumber** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `POId, RequisitionId, PONumber`
- Usage: 52 seeks, 2 scans, 0 lookups
- Size: 73.84 MB

**SK_ReqVen1** (NONCLUSTERED)
- Key columns: `RequisitionId, VendorId, POId, PONumber, PODate, DatePrinted, DatePrintedDetail, DateExported, Amount, ItemCount, DiscountAmount, TotalGross, DiscountRate, ShippingAmount`
- Usage: 120,167 seeks, 0 scans, 0 lookups
- Size: 298.18 MB

**SKI_Vendor_ReqUploadCancelled** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `RequisitionId, UploadId, Cancelled`
- Usage: 791 seeks, 62 scans, 0 lookups
- Size: 57.81 MB

**_dta_index_PO_7_1070678912__K3_K2_K19_K21** (NONCLUSTERED)
- Key columns: `VendorId, RequisitionId, UploadId, Cancelled`
- Usage: 4 seeks, 0 scans, 0 lookups
- Size: 62.94 MB

**_dta_index_PO_7_1070678912__K2_K1_K3_4_5_6_7_8_11_12_14_15_16_17_18** (NONCLUSTERED)
- Key columns: `RequisitionId, POId, VendorId`
- Included: `PONumber, PODate, DatePrinted, DatePrintedDetail, DateExported, Amount, ItemCount, DiscountAmount, TotalGross, DiscountRate, ShippingAmount, ExportedToVendor`
- Usage: 286,391 seeks, 533 scans, 0 lookups
- Size: 281.09 MB


### dbo.PODetailItems

*Table rows: 24,327,549*

****[PK]** PK_PODetailItems** (CLUSTERED)
- Key columns: `PODetailItemId`
- Usage: 0 seeks, 9 scans, 1,443 lookups
- Size: 2580.59 MB

**SK_PO** (NONCLUSTERED)
- Key columns: `POId`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 361.66 MB

**SK_Detail** (NONCLUSTERED)
- Key columns: `DetailId`
- Usage: 69,502 seeks, 1 scans, 0 lookups
- Size: 379.51 MB

**SKI_POVendorDetailBidItem_Award** (NONCLUSTERED)
- Key columns: `POId, VendorId, DetailId, BidItemId`
- Included: `AwardId`
- Usage: 11,401 seeks, 2 scans, 0 lookups
- Size: 724.70 MB

**SKI_POVendor_Detail** (NONCLUSTERED)
- Key columns: `POId, VendorId`
- Included: `DetailId`
- Usage: 1,776 seeks, 1 scans, 0 lookups
- Size: 524.04 MB


### dbo.POIDTable

*Table rows: 0*

****[PK]** PK__POIDTabl__9899C8AA58B78F44** (CLUSTERED)
- Key columns: `POIDID`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.POLayoutDetail

*Table rows: 6,841*

****[PK]** PK_POLayoutDetail** (CLUSTERED)
- Key columns: `POLayoutDetailId`
- Usage: 0 seeks, 487 scans, 0 lookups
- Size: 0.63 MB


### dbo.POLayoutFields

*Table rows: 56*

****[PK]** PK_POLayoutFields** (CLUSTERED)
- Key columns: `POLayoutFieldId`
- Usage: 470 seeks, 18 scans, 0 lookups
- Size: 0.02 MB


### dbo.POLayouts

*Table rows: 632*

****[PK]** PK_POLayouts** (CLUSTERED)
- Key columns: `POLayoutId`
- Usage: 499 seeks, 613 scans, 0 lookups
- Size: 0.06 MB


### dbo.POPageSummary

*Table rows: 73,456*

****[PK]** PK_POPageSummary** (CLUSTERED)
- Key columns: `POPageId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 3.58 MB


### dbo.POPrintTaggedPOFile

*Table rows: 120,950*

****[PK]** PK_POPrintTaggedPOFile** (CLUSTERED)
- Key columns: `SysId`
- Usage: 0 seeks, 1 scans, 91 lookups
- Size: 9.93 MB

**TPF_BYRSID** (NONCLUSTERED)
- Key columns: `RSID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1.91 MB

**SK_RSDistrictPOOrder** (NONCLUSTERED)
- Key columns: `RSID, DISTRICTID, POOrderSeq`
- Included: `PONUMBER, AccountId, AwardsBidHeaderId, BudgetId`
- Usage: 339 seeks, 3 scans, 0 lookups
- Size: 5.27 MB


### dbo.POQueue

*Table rows: 26,749*

****[PK]** PK__POQueue__91383C3E79617699** (CLUSTERED)
- Key columns: `POQueueId`
- Usage: 5,490 seeks, 38,029 scans, 42 lookups
- Size: 9.10 MB

**SK_QueueRequestDate** (NONCLUSTERED)
- Key columns: `POQueueId, RequestDate DESC`
- Usage: 43 seeks, 82 scans, 0 lookups
- Size: 0.61 MB


### dbo.POQueueItems

*Table rows: 398,106*

****[PK]** PK__POQueueI__1E7B80021701E1C0** (CLUSTERED)
- Key columns: `POQueueItemId`
- Usage: 216 seeks, 0 scans, 5,153 lookups
- Size: 88.45 MB

**SKI_Queue_Id** (NONCLUSTERED)
- Key columns: `POQueueId`
- Included: `POQueueItemId`
- Usage: 95 seeks, 3 scans, 0 lookups
- Size: 7.24 MB

**SKI_POIdPOQueue_Started** (NONCLUSTERED)
- Key columns: `POId, POQueueId`
- Included: `SendStarted`
- Usage: 5,358 seeks, 1 scans, 0 lookups
- Size: 11.96 MB


### dbo.POStatus

*Table rows: 406,160*

****[PK]** PK__POStatus__DE88A18037256B49** (CLUSTERED)
- Key columns: `POStatusId`
- Usage: 2 seeks, 0 scans, 0 lookups
- Size: 20.63 MB

**SKI_PO_Status** (NONCLUSTERED)
- Key columns: `POId, StatusDate DESC`
- Included: `StatusId, UserId`
- Usage: 5,222 seeks, 2 scans, 0 lookups
- Size: 13.84 MB


### dbo.POStatusTable

*Table rows: 0*

****[PK]** PK__POStatus__F880A40749754BB4** (CLUSTERED)
- Key columns: `POStatusID`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.02 MB


### dbo.PostCatalogDetail

*Table rows: 39,099*

****[PK]** PK_PostCatalogDetail** (CLUSTERED)
- Key columns: `PostCatalogDetailId`
- Usage: 8 seeks, 285 scans, 0 lookups
- Size: 5.12 MB


### dbo.PostCatalogHeader

*Table rows: 3,327*

****[PK]** PK_PostCatalogHeader** (CLUSTERED)
- Key columns: `PostCatalogHeaderId`
- Usage: 92 seeks, 59 scans, 0 lookups
- Size: 0.18 MB


### dbo.PPCatalogs

*Table rows: 1,664*

****[PK]** PK_PPCatalogs** (CLUSTERED)
- Key columns: `PPCatalogId`
- Usage: 4 seeks, 1 scans, 4,766 lookups
- Size: 0.33 MB

**SK_CatalogId** (NONCLUSTERED)
- Key columns: `CatalogId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.09 MB

**SK_PricePlan** (NONCLUSTERED)
- Key columns: `PricePlanId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.06 MB

**SK_PPCat** (NONCLUSTERED)
- Key columns: `PricePlanId, CategoryId, CatalogId`
- Usage: 73,731 seeks, 72,716 scans, 0 lookups
- Size: 0.08 MB

**SK_Cat** (NONCLUSTERED)
- Key columns: `CategoryId`
- Usage: 4,767 seeks, 2 scans, 0 lookups
- Size: 0.07 MB


### dbo.PPCategory

*Table rows: 1,457*

****[PK]** PK__CategoryPP__5E7FE7D2** (CLUSTERED)
- Key columns: `PPCategoryId`
- Usage: 0 seeks, 0 scans, 71,203 lookups
- Size: 0.09 MB

**SK_PPCat** (NONCLUSTERED)
- Key columns: `PricePlanId, CategoryId`
- Usage: 488,426 seeks, 547 scans, 0 lookups
- Size: 0.05 MB

**SK_Category** (NONCLUSTERED)
- Key columns: `CategoryId`
- Usage: 71,203 seeks, 1 scans, 0 lookups
- Size: 0.04 MB


### dbo.PriceHolds

*Table rows: 0*

****[PK]** PK__PriceHol__CC37109B40E005B3** (CLUSTERED)
- Key columns: `PriceHoldId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.PriceListTypes

*Table rows: 2*

****[PK]** PK__PriceLis__1D8486F504B9BEA7** (CLUSTERED)
- Key columns: `PriceListTypeId`
- Usage: 1 seeks, 14 scans, 0 lookups
- Size: 0.02 MB


### dbo.PricePlans

*Table rows: 584*

****[PK]** PK_PricePlans** (CLUSTERED)
- Key columns: `PricePlanId`
- Usage: 14,974,298 seeks, 8,376 scans, 0 lookups
- Size: 0.07 MB


### dbo.PriceRanges

*Table rows: 120,619*

****[PK]** PK__PriceRan__B8A301DF1F38AAB9** (CLUSTERED)
- Key columns: `PriceRangeId`
- Usage: 0 seeks, 6 scans, 0 lookups
- Size: 7.25 MB


### dbo.Prices

*Table rows: 0*

****[PK]** PK_Prices** (CLUSTERED)
- Key columns: `PriceId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.PricingAddenda

*Table rows: 205,658*

****[PK]** PK_PricingAddenda** (CLUSTERED)
- Key columns: `PricingAddendaId`
- Usage: 4,977 seeks, 58 scans, 3,828 lookups
- Size: 66.28 MB

**ti_CrossRef_PricingAddendaId** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `PricingAddendaId`
- Usage: 3,285 seeks, 0 scans, 0 lookups
- Size: 4.52 MB

**SKI_CategoryHeadingKeywordDistrict_Id** (NONCLUSTERED)
- Key columns: `CategoryId, HeadingId, KeywordId, DistrictId`
- Included: `PricingAddendaId`
- Usage: 19,435 seeks, 3 scans, 0 lookups
- Size: 10.05 MB


### dbo.PricingConsolidatedOrderCounts

*Table rows: 401,387*

****[PK]** PK__PricingC__720259A0ACB8C0D2** (CLUSTERED)
- Key columns: `PCOCId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 11.29 MB

**SK_BidHeaderIdItemId** (NONCLUSTERED)
- Key columns: `BidHeaderId, ItemId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 8.59 MB


### dbo.PricingMap

*Table rows: 0*

****[PK]** PK__PricingM__3214EC0777224648** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.PricingUpdate

*Table rows: 59,384*

****[PK]** PK__PricingU__40D9B4ECDC40BD26** (CLUSTERED)
- Key columns: `PricingUpdateId`
- Usage: 0 seeks, 78 scans, 0 lookups
- Size: 2.63 MB


### dbo.PrintDocuments

*Table rows: 0*

****[PK]** PK__PrintDoc__D48DBA3968C69B45** (CLUSTERED)
- Key columns: `PrintDocumentId`
- Usage: 1 seeks, 4 scans, 0 lookups
- Size: 0.00 MB


### dbo.Printers

*Table rows: 18*

****[PK]** PK_Printers** (CLUSTERED)
- Key columns: `PrinterId`
- Usage: 1,364 seeks, 180 scans, 0 lookups
- Size: 0.02 MB


### dbo.ProductVerificationResults

*Table rows: 197,830*

****[PK]** PK__ProductV__306D49075BA4BA78** (CLUSTERED)
- Key columns: `VerificationId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 665.79 MB

****[UQ]** UQ_EntryId_QueryType** (NONCLUSTERED)
- Key columns: `EntryId, QueryType`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 17.03 MB

**IX_EntryId_QueryType** (NONCLUSTERED)
- Key columns: `EntryId, QueryType`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 17.04 MB

**IX_VerificationResult** (NONCLUSTERED)
- Key columns: `VerificationResult`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 4.16 MB

**IX_QueryType** (NONCLUSTERED)
- Key columns: `QueryType`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 8.04 MB


### dbo.ProjectTasks

*Table rows: 14*

****[PK]** PK_ProjectTasks** (CLUSTERED)
- Key columns: `ProjectTasksId`
- Usage: 29 seeks, 16 scans, 37 lookups
- Size: 0.02 MB

**SK_Seq** (NONCLUSTERED)
- Key columns: `TaskSeqNum`
- Usage: 0 seeks, 55 scans, 0 lookups
- Size: 0.02 MB


### dbo.QuestionnaireResponses

*Table rows: 0*

****[PK]** PK_QuestionnaireResponses** (CLUSTERED)
- Key columns: `qrid`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.Rates

*Table rows: 0*

****[PK]** PK__Rates__58A7CF5C1768EED4** (CLUSTERED)
- Key columns: `RateId`
- Usage: 1 seeks, 4 scans, 0 lookups
- Size: 0.00 MB


### dbo.RateTypes

*Table rows: 0*

****[PK]** PK__RateType__B06796C80FC7CD0C** (CLUSTERED)
- Key columns: `RateTypeId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.RateUnits

*Table rows: 0*

****[PK]** PK__RateUnit__1AC7298A13985DF0** (CLUSTERED)
- Key columns: `RateUnitId`
- Usage: 3 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.Receiving

*Table rows: 0*

****[PK]** PK_Receiving** (CLUSTERED)
- Key columns: `ReceivingId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.ReportSession

*Table rows: 5,282,698*

****[PK]** PK_ReportSession** (CLUSTERED)
- Key columns: `RSId`
- Usage: 2,527 seeks, 13 scans, 0 lookups
- Size: 392.21 MB


### dbo.ReportSessionLinks

*Table rows: 51,991,223*

****[PK]** PK_ReportSessionLinks** (CLUSTERED)
- Key columns: `RSLId`
- Usage: 3,221 seeks, 1 scans, 12,625 lookups
- Size: 2280.69 MB

**RS_RSLink** (NONCLUSTERED)
- Key columns: `RSId, IntId`
- Usage: 23,265 seeks, 5 scans, 0 lookups
- Size: 1031.95 MB


### dbo.ReqAudit

*Table rows: 0*

****[PK]** PK_ReqAudit** (CLUSTERED)
- Key columns: `ReqAuditId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.RequisitionChangeLog

*Table rows: 1,938,491*

****[PK]** PK__RequisitionChang__2843D2B2** (CLUSTERED)
- Key columns: `RequisitionChangeId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 331.24 MB


### dbo.RequisitionNoteEmails

*Table rows: 16,161*

****[PK]** PK__Requisit__234DFCF713193B03** (CLUSTERED)
- Key columns: `RequisitionNoteEmailID`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 0.70 MB


### dbo.RequisitionNotes

*Table rows: 24,753*

****[PK]** PK__Requisit__4A9C7A5E0F48AA1F** (CLUSTERED)
- Key columns: `RequisitionNoteID`
- Usage: 32 seeks, 0 scans, 197 lookups
- Size: 3.14 MB

**SK_RequisitionId** (NONCLUSTERED)
- Key columns: `RequisitionID`
- Usage: 119,232 seeks, 4 scans, 0 lookups
- Size: 0.41 MB


### dbo.Requisitions

*Table rows: 2,078,555*

****[PK]** PK_Requisitions** (CLUSTERED)
- Key columns: `RequisitionId`
- Usage: 33,026,263 seeks, 89 scans, 2,571,511 lookups
- Size: 626.03 MB

**Requisitions9** (NONCLUSTERED)
- Key columns: `UserAccountId`
- Usage: 1,086,352 seeks, 26 scans, 0 lookups
- Size: 32.59 MB

**SK_BudgetUser** (NONCLUSTERED)
- Key columns: `BudgetId, UserId`
- Usage: 236,006 seeks, 0 scans, 0 lookups
- Size: 40.88 MB

**SK_SchoolId** (NONCLUSTERED)
- Key columns: `SchoolId`
- Usage: 281 seeks, 106 scans, 0 lookups
- Size: 34.77 MB

**SK_BudgetAccount** (NONCLUSTERED)
- Key columns: `BudgetAccountId`
- Usage: 1,297,930 seeks, 0 scans, 0 lookups
- Size: 32.80 MB

**SK_Budget** (NONCLUSTERED)
- Key columns: `BudgetId`
- Included: `RequisitionId, BidHeaderId`
- Usage: 39,129 seeks, 2,497 scans, 0 lookups
- Size: 40.40 MB

**SKI_UserAccount_Req** (NONCLUSTERED)
- Key columns: `UserAccountId, RequisitionId`
- Included: `SchoolId, UserId, BudgetId, BudgetAccountId, CategoryId, ShippingId, DateEntered, BidHeaderId, OrderType`
- Usage: 606 seeks, 32 scans, 0 lookups
- Size: 119.25 MB

**SK_CatSchool** (NONCLUSTERED)
- Key columns: `CategoryId, SchoolId`
- Usage: 172 seeks, 0 scans, 0 lookups
- Size: 45.55 MB

**SK_User** (NONCLUSTERED)
- Key columns: `UserId`
- Included: `BudgetId, CategoryId`
- Usage: 39,485 seeks, 1,711 scans, 0 lookups
- Size: 55.38 MB

**SK_Category** (NONCLUSTERED)
- Key columns: `CategoryId`
- Usage: 5,051 seeks, 160 scans, 0 lookups
- Size: 30.30 MB

**SK_BidHeader** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Usage: 3,776 seeks, 124 scans, 0 lookups
- Size: 31.53 MB

**SK_RUBBaCSRnAAc** (NONCLUSTERED)
- Key columns: `RequisitionId, UserId, BudgetId, BudgetAccountId, CategoryId, ShippingId, RequisitionNumber, Attention, AccountCode`
- Usage: 1,586,842 seeks, 26 scans, 0 lookups
- Size: 214.12 MB

**SK_ReqBudget** (NONCLUSTERED)
- Key columns: `RequisitionId, BudgetId`
- Included: `RequisitionNumber, BudgetAccountId, UserAccountId, CategoryId, ShippingId, Attention, BidHeaderId`
- Usage: 4,068,000 seeks, 112 scans, 0 lookups
- Size: 138.29 MB

**_dta_index_Requisitions_7_354152357__K4_K1_K6_K10_K5_K9_K7_K29_K8_3_11** (NONCLUSTERED)
- Key columns: `SchoolId, RequisitionId, BudgetId, ShippingId, UserId, CategoryId, BudgetAccountId, BidHeaderId, UserAccountId`
- Included: `RequisitionNumber, Attention`
- Usage: 723 seeks, 0 scans, 0 lookups
- Size: 167.34 MB

**SK_CatBudget** (NONCLUSTERED)
- Key columns: `CategoryId, BudgetId`
- Usage: 354,930 seeks, 1 scans, 0 lookups
- Size: 40.49 MB

**SKI_CategoryEntered_UserBudgetBid** (NONCLUSTERED)
- Key columns: `CategoryId, DateEntered`
- Included: `UserId, BudgetId, BidHeaderId`
- Usage: 1 seeks, 91 scans, 0 lookups
- Size: 73.17 MB

**SKI_BudgetCategory_Etc** (NONCLUSTERED)
- Key columns: `BudgetId, CategoryId, RequisitionId`
- Included: `RequisitionNumber, SchoolId, UserId, BudgetAccountId, UserAccountId, ShippingId, Attention, BidHeaderId`
- Usage: 4,409 seeks, 4 scans, 0 lookups
- Size: 150.52 MB

**SKI_BudgetAccountShippingUserSchool_ReqNbr** (NONCLUSTERED)
- Key columns: `BudgetAccountId, ShippingId, UserId, SchoolId`
- Included: `RequisitionNumber`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 79.23 MB


### dbo.ResetPasswordTracking

*Table rows: 86,912*

**IX_ResetPasswordTracking_ResetCode** (NONCLUSTERED)
- Key columns: `ResetPasswordCode`
- Included: `UserIds, SchoolId, DistrictId, Email`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 10.19 MB


### dbo.Rights

*Table rows: 0*

****[PK]** PK_Rights** (CLUSTERED)
- Key columns: `RightsId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.RightsLink

*Table rows: 0*

****[PK]** PK_RightsLink** (CLUSTERED)
- Key columns: `RightsLinkId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.RTK_CASFile

*Table rows: 7,881*

****[PK]** PK_RTK_CASFile** (CLUSTERED)
- Key columns: `RTK_CASFileId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.96 MB


### dbo.RTK_ContainerCodes

*Table rows: 21*

****[PK]** PK_RTK_ContainerCodes** (CLUSTERED)
- Key columns: `ContainerCodesID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.RTK_Documents

*Table rows: 0*

****[PK]** PK__RTK_Docu__D61B7C4C075678D3** (CLUSTERED)
- Key columns: `RTKDocumentId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.RTK_FactSheets

*Table rows: 2,459*

****[PK]** PK__RTK_Fact__C8B2BFBC12C82B7F** (CLUSTERED)
- Key columns: `RTKFactSheetId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.40 MB


### dbo.RTK_HealthHazardCodes

*Table rows: 9*

****[PK]** PK_RTK_HealthHazardCodes** (CLUSTERED)
- Key columns: `HealthHazardCodesID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.RTK_Inventories

*Table rows: 658*

****[PK]** PK__RTK_Inve__A3434811D0E797E1** (CLUSTERED)
- Key columns: `RTK_InventoryId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.07 MB


### dbo.RTK_InventoryRangeCodes

*Table rows: 12*

****[PK]** PK_RTK_InventoryRangeCodes** (CLUSTERED)
- Key columns: `InventoryRangeCodesID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.RTK_Items

*Table rows: 64,627*

****[PK]** PK_RTK_ItemsId** (CLUSTERED)
- Key columns: `RTK_ItemsId`
- Usage: 1,841 seeks, 22 scans, 0 lookups
- Size: 11.49 MB

**KeyLegacyCometCode** (NONCLUSTERED)
- Key columns: `LegacyCometCode`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1.44 MB

**SK_CategoryItem** (NONCLUSTERED)
- Key columns: `CategoryId, ItemId`
- Usage: 2 seeks, 0 scans, 0 lookups
- Size: 1.14 MB

**SKI_Item_Codes** (NONCLUSTERED)
- Key columns: `ItemId`
- Included: `RTK_ItemsId, ContainerCodesId, UOMCodesId, MSDSId`
- Usage: 3,186,571 seeks, 0 scans, 0 lookups
- Size: 1.64 MB

**SKI_MSDSCategory_Item** (NONCLUSTERED)
- Key columns: `MSDSId, CategoryId`
- Included: `RTK_ItemsId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1.16 MB

**SKI_MSDSItemCode_Id** (NONCLUSTERED)
- Key columns: `MSDSId, ItemCode`
- Included: `RTK_ItemsId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 1.58 MB

**SKI_MSDS_ItemId** (NONCLUSTERED)
- Key columns: `MSDSId`
- Included: `RTK_ItemsId, ItemId`
- Usage: 1 seeks, 3 scans, 0 lookups
- Size: 1.14 MB


### dbo.RTK_LegacyDistrictCodesMap

*Table rows: 78*

****[PK]** PK_RTK_LegacyDistrictCodesMap** (CLUSTERED)
- Key columns: `RTK_DistrictCodesMapId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.02 MB


### dbo.RTK_LegacySchoolFile

*Table rows: 6,766*

****[PK]** PK_LegacySchoolFile** (CLUSTERED)
- Key columns: `LegacySchoolFileId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 1.21 MB


### dbo.RTK_MixtureCodes

*Table rows: 11*

****[PK]** PK_RTK_MixtureCodes** (CLUSTERED)
- Key columns: `MixtureCodesID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.RTK_MSDSDetail

*Table rows: 151,665*

****[PK]** PK_RTK_MSDSDetail** (CLUSTERED)
- Key columns: `RTK_MSDSDetailID`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 10.25 MB

**IX_RTK_MSDSDetail** (NONCLUSTERED)
- Key columns: `RTK_MSDSDetailID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1.16 MB

**IX_RTK_MSDSDetail_1** (NONCLUSTERED)
- Key columns: `RTK_ItemsID, RTK_MSDSDetailID`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 2.30 MB


### dbo.RTK_Purposes

*Table rows: 35*

****[PK]** PK__RTK_Purp__3213E83F0B50C8C2** (CLUSTERED)
- Key columns: `RTK_PurposeID`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 0.02 MB


### dbo.RTK_ReportItems

*Table rows: 1,006,140*

****[PK]** PK_RTK_ReportItems** (CLUSTERED)
- Key columns: `RTK_ReportItemsId`
- Usage: 3,692 seeks, 33 scans, 19 lookups
- Size: 92.32 MB

**IX_RTK_ReportItems_byYear** (NONCLUSTERED)
- Key columns: `Year`
- Included: `RTK_ReportItemsId, ItemId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 19.50 MB

**IX_RTK_ReportItems_byDistrictId** (NONCLUSTERED)
- Key columns: `DistrictId`
- Usage: 15 seeks, 0 scans, 0 lookups
- Size: 15.45 MB

**IX_RTK_ReportItems_byItemId** (NONCLUSTERED)
- Key columns: `ItemId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 17.42 MB

**SKI_ItemSiteYear_Id** (NONCLUSTERED)
- Key columns: `ItemId, RTK_SitesId, Year`
- Included: `RTK_ReportItemsId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 35.59 MB

**SKI_Year_All** (NONCLUSTERED)
- Key columns: `Year, DistrictId, RTK_SitesId`
- Included: `RTK_ReportItemsId, ItemId, CategoryId, Quantity, ExactLocationOnSite, MSDSId, RTK_ItemsId`
- Usage: 2 seeks, 1 scans, 0 lookups
- Size: 44.27 MB

**SKI_ItemYear_DistrictSite** (NONCLUSTERED)
- Key columns: `RTK_ItemsId, Year`
- Included: `DistrictId, RTK_SitesId`
- Usage: 1 seeks, 3 scans, 0 lookups
- Size: 29.68 MB

**SKI_MSDS_ItemId** (NONCLUSTERED)
- Key columns: `MSDSId`
- Included: `RTK_ReportItemsId, ItemId`
- Usage: 3,186,572 seeks, 0 scans, 0 lookups
- Size: 18.45 MB


### dbo.RTK_Sites

*Table rows: 823*

****[PK]** PK_RTK_Sites** (CLUSTERED)
- Key columns: `RTK_SitesId`
- Usage: 1,844 seeks, 50 scans, 0 lookups
- Size: 0.27 MB


### dbo.RTK_Surveys

*Table rows: 0*

****[PK]** PK__RTK_Surv__4E40C4ED188104D5** (CLUSTERED)
- Key columns: `RTKSurveyId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.RTK_Training

*Table rows: 0*

****[PK]** PK__RTK_Trai__AE6AAE51019D9F7D** (CLUSTERED)
- Key columns: `RTKTrainingId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.RTK_UOMCodes

*Table rows: 3*

****[PK]** PK_RTK_UOMCodes** (CLUSTERED)
- Key columns: `UOMCodesID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.RTK_VendorLinks

*Table rows: 0*

****[PK]** PK__RTK_Vend__724EEC6A0D0F5229** (CLUSTERED)
- Key columns: `RTKVendorLinkId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.SafetyDataSheets

*Table rows: 154,540*

****[PK]** PK__SafetyDa__C9A3658F59DFE532** (CLUSTERED)
- Key columns: `SafetyDataSheetId`
- Usage: 0 seeks, 3,117,616 scans, 139,176 lookups
- Size: 19.55 MB

**SK_URL** (NONCLUSTERED)
- Key columns: `SDSURL`
- Usage: 304,877 seeks, 635 scans, 0 lookups
- Size: 14.21 MB


### dbo.Salutations

*Table rows: 5*

****[PK]** PK__Salutati__562AE14F0EBE9A3A** (CLUSTERED)
- Key columns: `SalutationId`
- Usage: 24,337 seeks, 6,158 scans, 0 lookups
- Size: 0.02 MB


### dbo.ScanEvents

*Table rows: 389,487*

****[PK]** PK__ScanEven__316CC94A551BCD8E** (CLUSTERED)
- Key columns: `ScanEventId`
- Usage: 123 seeks, 3 scans, 0 lookups
- Size: 578.10 MB


### dbo.ScanJobs

*Table rows: 3*

****[PK]** PK__ScanJobs__8A1E9DAD341935C8** (CLUSTERED)
- Key columns: `ScanJobId`
- Usage: 1,641 seeks, 4 scans, 0 lookups
- Size: 0.02 MB


### dbo.ScannerZones

*Table rows: 10*

****[PK]** PK__ScannerZ__57E358B33E936515** (CLUSTERED)
- Key columns: `ScannerZoneId`
- Usage: 0 seeks, 7 scans, 0 lookups
- Size: 0.02 MB


### dbo.ScheduledTask

*Table rows: 12*

****[PK]** PK__Schedule__7C6949B192A05F7B** (CLUSTERED)
- Key columns: `TaskId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.ScheduleTypes

*Table rows: 10*

****[PK]** PK__ScheduleTypes__1348B5CC** (CLUSTERED)
- Key columns: `ScheduleId`
- Usage: 11,700 seeks, 12,346 scans, 0 lookups
- Size: 0.02 MB


### dbo.School

*Table rows: 6,582*

****[PK]** PK_School** (CLUSTERED)
- Key columns: `SchoolId`
- Usage: 2,429,101 seeks, 4,846 scans, 16,705 lookups
- Size: 1.27 MB

**SK_District** (NONCLUSTERED)
- Key columns: `DistrictId`
- Usage: 13,499 seeks, 415 scans, 0 lookups
- Size: 0.13 MB

**SKI_Active_School** (NONCLUSTERED)
- Key columns: `Active`
- Included: `SchoolId`
- Usage: 16,343 seeks, 35 scans, 0 lookups
- Size: 0.09 MB

**_dta_index_School_7_510676917__K2_K1_4_5_6_7_8_9_10** (NONCLUSTERED)
- Key columns: `DistrictId, SchoolId`
- Included: `Name, Address1, Address2, Address3, City, State, Zipcode`
- Usage: 18,240 seeks, 1,733 scans, 0 lookups
- Size: 1.08 MB


### dbo.SDS_Rpt_Bridge

*Table rows: 99*

**IX_SDS_Rpt_Bridge** (CLUSTERED)
- Key columns: `SessionId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.06 MB


### dbo.SDSDocs

*Table rows: 161,387*

****[PK]** PK__SDSDocs__3214EC07599E86FE** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 31.58 MB

**SKI_Item_Id** (NONCLUSTERED)
- Key columns: `ItemId`
- Included: `Id`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 4.32 MB

**SKI_MSDS_ItemId** (NONCLUSTERED)
- Key columns: `MSDSId`
- Included: `Id, ItemId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 4.78 MB

**ti_CrossRef_Id** (NONCLUSTERED)
- Key columns: `CrossRefId`
- Included: `Id`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 4.09 MB


### dbo.SDSErrors

*Table rows: 0*

****[PK]** PK__SDSError__1FC45DBB3D51DD76** (CLUSTERED)
- Key columns: `sdsErrorId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.SDSLog

*Table rows: 0*

****[PK]** PK__SDSLog__BE04475849B83273** (CLUSTERED)
- Key columns: `sdsLogId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.SDSResults

*Table rows: 116,893*

****[PK]** PK__SDSResul__FAB2B42F07B89792** (CLUSTERED)
- Key columns: `SDSResultsId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 91.70 MB


### dbo.SDSs

*Table rows: 0*

****[PK]** PK__SDSs__27BDF69229E64697** (CLUSTERED)
- Key columns: `sdsId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.SDSSyncStatus

*Table rows: 26,483*

****[PK]** PK__SDSSyncS__C9A3658FEE1B713F** (CLUSTERED)
- Key columns: `SafetyDataSheetId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 3.11 MB

**IX_SDSSyncStatus_SyncStatus** (NONCLUSTERED)
- Key columns: `SyncStatus`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.78 MB

**IX_SDSSyncStatus_LastSyncedAt** (NONCLUSTERED)
- Key columns: `LastSyncedAt`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.76 MB


### dbo.SearchKeywords

*Table rows: 0*

****[PK]** PK__SearchKe__3F57263943E68087** (CLUSTERED)
- Key columns: `SearchKeywordId`
- Usage: 1 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.SearchSets

*Table rows: 43,913*

****[PK]** PK_SearchSets** (CLUSTERED)
- Key columns: `SSId`
- Usage: 814 seeks, 2 scans, 2,442 lookups
- Size: 3.98 MB

**SK_Session** (NONCLUSTERED)
- Key columns: `SessionId`
- Usage: 2,772 seeks, 0 scans, 0 lookups
- Size: 0.73 MB


### dbo.Sections

*Table rows: 18*

****[PK]** PK__Sections__744F2D60** (CLUSTERED)
- Key columns: `SectionId`
- Usage: 4 seeks, 478 scans, 0 lookups
- Size: 0.02 MB

**SK_Category** (NONCLUSTERED)
- Key columns: `CategoryId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 0.02 MB


### dbo.SecurityKeys

*Table rows: 14*

****[PK]** PK__Security__405262811466F737** (CLUSTERED)
- Key columns: `SecurityKeyID`
- Usage: 1,577,101 seeks, 3 scans, 0 lookups
- Size: 0.02 MB


### dbo.SecurityRoleKeys

*Table rows: 65*

****[PK]** PK__Security__ABE2F2671837881B** (CLUSTERED)
- Key columns: `SecurityRoleKeyID`
- Usage: 0 seeks, 1,577,105 scans, 0 lookups
- Size: 0.02 MB


### dbo.SecurityRoles

*Table rows: 5*

****[PK]** PK__Security__F829C791160AB647** (CLUSTERED)
- Key columns: `SecurityRoleId`
- Usage: 3,154,203 seeks, 5 scans, 0 lookups
- Size: 0.02 MB


### dbo.SecurityRoleUsers

*Table rows: 355,373*

****[PK]** PK__Security__E7F0D603703A131A** (CLUSTERED)
- Key columns: `SecurityRoleUserId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 13.95 MB

**SKI_UserId_UserRoleIdRoleId** (NONCLUSTERED)
- Key columns: `UserId`
- Included: `SecurityRoleUserId, SecurityRoleId`
- Usage: 3,433,922 seeks, 4 scans, 0 lookups
- Size: 7.13 MB


### dbo.Services

*Table rows: 0*

****[PK]** PK__Services__C51BB00A0BF73C28** (CLUSTERED)
- Key columns: `ServiceId`
- Usage: 2 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.SessionCmds

*Table rows: 0*

****[PK]** PK__SessionC__D4B6857B1F942081** (CLUSTERED)
- Key columns: `SessionCmdId`
- Usage: 1 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.SessionTable

*Table rows: 12,395,976*

****[PK]** PK_SessionTable** (CLUSTERED)
- Key columns: `SessionId`
- Usage: 20,534,078 seeks, 21 scans, 11,115 lookups
- Size: 1953.89 MB

**SK_Budget** (NONCLUSTERED)
- Key columns: `BudgetId`
- Usage: 9,072 seeks, 3 scans, 0 lookups
- Size: 193.23 MB

**SKI_DistrictEnd_UserRepLevel** (NONCLUSTERED)
- Key columns: `DistrictId, SessionEnd`
- Included: `UserId, CSRepId, ApprovalLevel`
- Usage: 584,042 seeks, 7 scans, 0 lookups
- Size: 389.77 MB

**IX_SessionTable_SessionId** (NONCLUSTERED)
- Key columns: `SessionId`
- Included: `DistrictId, SchoolId, UserId, BudgetId, CurrentBudgetId, NextBudgetId`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 408.80 MB


### dbo.ShipLocations

*Table rows: 6,868*

****[PK]** PK_ShipLocations** (CLUSTERED)
- Key columns: `ShippingId`
- Usage: 3,592 seeks, 129 scans, 76,361 lookups
- Size: 1.23 MB

**SK_District** (NONCLUSTERED)
- Key columns: `DistrictId`
- Usage: 76,362 seeks, 763 scans, 0 lookups
- Size: 0.13 MB

**_dta_index_ShipLocations_7_1576757070__K1_4_5_6_7_8_9_10_14** (NONCLUSTERED)
- Key columns: `ShippingId`
- Included: `Name, Address1, Address2, Address3, City, State, ZipCode, LocationCode`
- Usage: 103,947 seeks, 6,932 scans, 0 lookups
- Size: 1.02 MB


### dbo.ShippingCosts

*Table rows: 954*

****[PK]** PK__Shipping__AB3F978E04C3C730** (CLUSTERED)
- Key columns: `ShippingCostId`
- Usage: 33 seeks, 164 scans, 81 lookups
- Size: 0.08 MB

**SK_ShippingRequestId** (NONCLUSTERED)
- Key columns: `ShippingRequestId`
- Usage: 82 seeks, 0 scans, 0 lookups
- Size: 0.03 MB


### dbo.ShippingRequests

*Table rows: 635*

****[PK]** PK__Shipping__4DDC37ED82F7C8BD** (CLUSTERED)
- Key columns: `ShippingRequestId`
- Usage: 15 seeks, 473 scans, 0 lookups
- Size: 0.13 MB


### dbo.ShippingVendor

*Table rows: 38,754*

****[PK]** PK__Shipping__F29A100E04561A60** (CLUSTERED)
- Key columns: `ShippingVendorId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 3.40 MB

**SKI_VendorId_Code** (NONCLUSTERED)
- Key columns: `VendorId, ShippingId`
- Included: `ShippingCode`
- Usage: 192 seeks, 1 scans, 0 lookups
- Size: 1.06 MB


### dbo.SSOLoginTracking

*Table rows: 123,359*

**IX_SSOLoginTracking_ResetCode** (NONCLUSTERED)
- Key columns: `Email, SSOProvider, Action`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 17.24 MB


### dbo.States

*Table rows: 3*

****[PK]** PK_States** (CLUSTERED)
- Key columns: `StateId`
- Usage: 16,600 seeks, 39,470 scans, 0 lookups
- Size: 0.02 MB


### dbo.StatusTable

*Table rows: 53*

****[PK]** PK_StatusTable** (CLUSTERED)
- Key columns: `StatusId`
- Usage: 3,576,350 seeks, 71,145 scans, 14,524 lookups
- Size: 0.02 MB

**SK_StatusCode** (NONCLUSTERED)
- Key columns: `StatusCode`
- Usage: 35,303 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

**SK_RequiredLevel** (NONCLUSTERED)
- Key columns: `RequiredLevel`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

**SK_Name** (NONCLUSTERED)
- Key columns: `Name`
- Usage: 0 seeks, 14,545 scans, 0 lookups
- Size: 0.02 MB

***[Unique]* SK_OptionValue** (NONCLUSTERED)
- Key columns: `OptionValue`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.Sulphite

*Table rows: 49*

****[PK]** PK__Sulphite__677FE68D64B095AA** (CLUSTERED)
- Key columns: `SulphiteId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.02 MB


### dbo.SulphiteUsers

*Table rows: 1,209*

****[PK]** PK__Sulphite__6D55B3EA13F94E2C** (CLUSTERED)
- Key columns: `SulphiteUserId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.06 MB


### dbo.Suppression

*Table rows: 4,367*

****[PK]** PK__Suppress__3214EC079C958FED** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 109 scans, 441 lookups
- Size: 2.91 MB

***[Unique]* Suppression_uindex** (NONCLUSTERED)
- Key columns: `Email, SuppressionType`
- Usage: 441 seeks, 0 scans, 0 lookups
- Size: 0.35 MB


### dbo.sysdiagrams

*Table rows: 9*

****[PK]** PK__sysdiagr__C2B05B616A96485D** (CLUSTERED)
- Key columns: `diagram_id`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.23 MB

****[UQ]** UK_principal_name** (NONCLUSTERED)
- Key columns: `principal_id, name`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.TableOfContents

*Table rows: 0*

****[PK]** PK_TableOfContents** (CLUSTERED)
- Key columns: `TCId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.TAGFILEP

*Table rows: 0*

****[PK]** PK__TAGFILEP__47DBAE45** (CLUSTERED)
- Key columns: `USR, TBL, POS`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.TaskEvent

*Table rows: 122,103*

****[PK]** PK_TaskEvent** (CLUSTERED)
- Key columns: `TaskEventId`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 8.60 MB


### dbo.TaskSchedule

*Table rows: 1,544,400*

****[PK]** PK_TaskSchedule** (CLUSTERED)
- Key columns: `TaskScheduleId`
- Usage: 499 seeks, 1 scans, 467 lookups
- Size: 190.01 MB

**SK_ProjectTasks** (NONCLUSTERED)
- Key columns: `ProjectTasksId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 18.55 MB

**SKI_CategoryDistrictCycle_PricePlan** (NONCLUSTERED)
- Key columns: `ProjectTasksId, CategoryId, DistrictId, BidCycleDate`
- Included: `TaskScheduleId, PricePlanId, StartDateActual`
- Usage: 511 seeks, 3 scans, 0 lookups
- Size: 63.70 MB


### dbo.TM_UOM

*Table rows: 77*

****[PK]** PK__TM_UOM__330FAB5B0CA1479E** (CLUSTERED)
- Key columns: `TM_UOMId`
- Usage: 11,290 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.TMAwards

*Table rows: 89,597*

****[PK]** PK__TMAwards__D13C98351130F291** (CLUSTERED)
- Key columns: `TMAwardId`
- Usage: 0 seeks, 67 scans, 37,092 lookups
- Size: 5.90 MB

**SK_BidTradeCounty** (NONCLUSTERED)
- Key columns: `BidHeaderId, BidTradeCountyId, Active, AwardAmount`
- Included: `BidImportId, VendorId`
- Usage: 102,058 seeks, 2 scans, 0 lookups
- Size: 4.21 MB


### dbo.TMImport

*Table rows: 3,114*

****[PK]** PK__TMImport__C8E74C496C34780C** (CLUSTERED)
- Key columns: `TMImportId`
- Usage: 1 seeks, 5 scans, 0 lookups
- Size: 0.42 MB


### dbo.TmpTaskSchedule

*Table rows: 4,884*

****[PK]** PK_TmpTaskSchedule** (CLUSTERED)
- Key columns: `TmpTaskScheduleId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.52 MB


### dbo.TMSurvey

*Table rows: 796*

****[PK]** PK__TMSurvey__3514BEAE5921A398** (CLUSTERED)
- Key columns: `TMSurveyId`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 0.12 MB


### dbo.TMSurveyNewTrades

*Table rows: 89*

****[PK]** PK__TMSurvey__24912C0360C2C560** (CLUSTERED)
- Key columns: `TMSurveyNewTradeId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.03 MB


### dbo.TMSurveyNewVendors

*Table rows: 186*

****[PK]** PK__TMSurvey__00123ED364935644** (CLUSTERED)
- Key columns: `TMSurveyNewVendorId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.05 MB


### dbo.TMSurveyResults

*Table rows: 89,650*

****[PK]** PK__TMSurvey__99EA30475CF2347C** (CLUSTERED)
- Key columns: `TMSurveyResultId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 5.92 MB

**SK_Survey_VendorBTCRateComments** (NONCLUSTERED)
- Key columns: `TMSurveyId`
- Included: `TMVendorId, BidTradeCountyId, Rating, Comments`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 3.52 MB


### dbo.TMVendors

*Table rows: 16,173*

****[PK]** PK__TMVendor__7C1EB3C7555112B4** (CLUSTERED)
- Key columns: `TMVendorId`
- Usage: 0 seeks, 6 scans, 0 lookups
- Size: 1.35 MB


### dbo.TopUOM

*Table rows: 4,579*

****[PK]** PK_TopUOM** (CLUSTERED)
- Key columns: `TopUOMId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.20 MB

**SK_CatUnit** (NONCLUSTERED)
- Key columns: `CategoryId, UnitId`
- Usage: 5,223 seeks, 1 scans, 0 lookups
- Size: 0.11 MB


### dbo.Trades

*Table rows: 107*

****[PK]** PK__Trades__3028BB5B0826AB44** (CLUSTERED)
- Key columns: `TradeId`
- Usage: 66,045 seeks, 10 scans, 0 lookups
- Size: 0.05 MB


### dbo.TransactionLog_HISTORY

*Table rows: 99,019,937*

****[PK]** PK__Transact__EB33B1C2BA5D0C0D** (CLUSTERED)
- Key columns: `SysId`
- Usage: 0 seeks, 7 scans, 0 lookups
- Size: 173804.37 MB

**ski_RequestStart_Session** (NONCLUSTERED)
- Key columns: `RequestStart`
- Included: `SessionId, SysId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 7082.17 MB

**SKI_SessionRequestStart** (NONCLUSTERED)
- Key columns: `SessionId, RequestStart`
- Included: `SysId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 7337.16 MB


### dbo.TransactionLogCF

*Table rows: 33,703,572*

****[PK]** PK__Transact__EB33B1C261E2A3C5** (CLUSTERED)
- Key columns: `SysId`
- Usage: 1,577,770 seeks, 6 scans, 0 lookups
- Size: 119604.81 MB

**SKI_RequestStart_SessionHeadersSysId** (NONCLUSTERED)
- Key columns: `RequestStart`
- Included: `SysId, SessionId, Headers`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 79142.06 MB

**SKI_SessionRequestStart_HeadersSysId** (NONCLUSTERED)
- Key columns: `SessionId, RequestStart`
- Included: `SysId, Headers`
- Usage: 0 seeks, 4 scans, 0 lookups
- Size: 78391.69 MB


### dbo.TransactionTypes

*Table rows: 0*

****[PK]** PK__TransactionTypes__1EEF72A2** (CLUSTERED)
- Key columns: `TransactionTypeId`
- Usage: 2 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### dbo.TransmitLog

*Table rows: 143,230*

****[PK]** PK__Transmit__63FDBAB3BAF604AA** (CLUSTERED)
- Key columns: `TransmitId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 120.30 MB


### dbo.Units

*Table rows: 11,218*

****[PK]** PK_Units** (CLUSTERED)
- Key columns: `UnitId`
- Usage: 57,306 seeks, 516 scans, 0 lookups
- Size: 0.60 MB

**SK_Code** (NONCLUSTERED)
- Key columns: `Code`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.30 MB

**_dta_index_Units_7_334676290__K1_3** (NONCLUSTERED)
- Key columns: `UnitId`
- Included: `Code`
- Usage: 248,319 seeks, 0 scans, 0 lookups
- Size: 0.32 MB

***[Unique]* SKI_UnitId_Code** (NONCLUSTERED)
- Key columns: `UnitId`
- Included: `Code`
- Usage: 0 seeks, 8,469 scans, 0 lookups
- Size: 0.31 MB


### dbo.UNSPSCs

*Table rows: 50,317*

****[PK]** PK__UNSPSCs__C2A3FEE54B5BDC5F** (CLUSTERED)
- Key columns: `UNSPSCId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 5.28 MB


### dbo.UnsubscriptionEmail

*Table rows: 0*

****[PK]** PK_UnsubscriptionEmail** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.02 MB

***[Unique]* UnsubscriptionEmail_uindex** (NONCLUSTERED)
- Key columns: `Email`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.UserAccounts

*Table rows: 3,329,159*

****[PK]** PK_UserAccounts** (CLUSTERED)
- Key columns: `UserAccountId`
- Usage: 1,813,147 seeks, 26 scans, 630,705 lookups
- Size: 216.91 MB

**UserAccounts34** (NONCLUSTERED)
- Key columns: `BudgetId, Active, AccountId, UserId`
- Usage: 12,906 seeks, 0 scans, 0 lookups
- Size: 81.13 MB

**SK_BudgetAccount** (NONCLUSTERED)
- Key columns: `Active, BudgetAccountId`
- Usage: 208,155 seeks, 0 scans, 0 lookups
- Size: 52.12 MB

**SK_BA** (NONCLUSTERED)
- Key columns: `BudgetAccountId`
- Usage: 8,204 seeks, 0 scans, 0 lookups
- Size: 48.31 MB

**SK_User** (NONCLUSTERED)
- Key columns: `UserId, Active`
- Usage: 388,875 seeks, 0 scans, 0 lookups
- Size: 63.39 MB

**SK_UserAccount** (NONCLUSTERED)
- Key columns: `AccountId, UserId`
- Usage: 38 seeks, 0 scans, 0 lookups
- Size: 77.33 MB

**SK_UAUseAllocations** (NONCLUSTERED)
- Key columns: `UseAllocations, UserAccountId`
- Usage: 0 seeks, 5 scans, 0 lookups
- Size: 36.97 MB

**SKI_UserBudgetActive_Account** (NONCLUSTERED)
- Key columns: `UserId, BudgetId, Active`
- Included: `AccountId`
- Usage: 495,752 seeks, 0 scans, 0 lookups
- Size: 141.32 MB


### dbo.UserAdminLog

*Table rows: 6,466*

****[PK]** PK_UserAdminLog** (CLUSTERED)
- Key columns: `logID`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 6.20 MB


### dbo.UserCategory

*Table rows: 0*

****[PK]** PK_UserCategory** (CLUSTERED)
- Key columns: `UserCategoryId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.Users

*Table rows: 338,327*

****[PK]** PK_Users** (CLUSTERED)
- Key columns: `UserId`
- Usage: 85,156,525 seeks, 10,139 scans, 73,329 lookups
- Size: 321.29 MB

**SK_CometId** (NONCLUSTERED)
- Key columns: `CometId`
- Usage: 49,614 seeks, 39 scans, 0 lookups
- Size: 6.96 MB

**SK_Approver** (NONCLUSTERED)
- Key columns: `ApproverId`
- Usage: 12,986 seeks, 0 scans, 0 lookups
- Size: 7.71 MB

**SKI_DistrictActive_UserSchoolApprovallevelCometApprover** (NONCLUSTERED)
- Key columns: `DistrictId, Active`
- Included: `UserId, SchoolId, ApprovalLevel, CometId, ApproverId`
- Usage: 281,508 seeks, 32 scans, 0 lookups
- Size: 15.80 MB

**SKI_SchoolUser_CometDistrictAcctCode** (NONCLUSTERED)
- Key columns: `SchoolId, UserId`
- Included: `CometId, DistrictAcctgCode`
- Usage: 2,637 seeks, 0 scans, 0 lookups
- Size: 11.39 MB

***[Unique]* SKI_User_SchoolCometAcctg** (NONCLUSTERED)
- Key columns: `UserId`
- Included: `SchoolId, CometId, DistrictAcctgCode`
- Usage: 218,496 seeks, 1 scans, 0 lookups
- Size: 7.59 MB

**_dta_index_Users_7_658802521__K1_10_12** (NONCLUSTERED)
- Key columns: `UserId`
- Included: `CometId, DistrictAcctgCode`
- Usage: 0 seeks, 190 scans, 0 lookups
- Size: 7.19 MB

**SKI_SchoolActive_AttentionLevelComet** (NONCLUSTERED)
- Key columns: `SchoolId, Active`
- Included: `Attention, ApprovalLevel, CometId`
- Usage: 6,169 seeks, 904 scans, 0 lookups
- Size: 21.60 MB


### dbo.UserTrees

*Table rows: 56,920*

****[PK]** PK_UserTrees** (CLUSTERED)
- Key columns: `utid`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 5.45 MB


### dbo.VendorCatalogNote

*Table rows: 11*

****[PK]** PK_VendorCatalogNote** (CLUSTERED)
- Key columns: `VendorCatalogNoteId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.02 MB


### dbo.VendorCategory

*Table rows: 6,785*

****[PK]** PK_VendorCategory** (CLUSTERED)
- Key columns: `VCId`
- Usage: 5 seeks, 0 scans, 4,846 lookups
- Size: 0.31 MB

**SK_Vendor** (NONCLUSTERED)
- Key columns: `VendorId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.13 MB

**SK_Category** (NONCLUSTERED)
- Key columns: `CategoryId`
- Usage: 4,767 seeks, 0 scans, 0 lookups
- Size: 0.14 MB

**SKI_VendorCategory_Name** (NONCLUSTERED)
- Key columns: `VendorId, CategoryId`
- Included: `VCId, VendorName, WebLink`
- Usage: 3,138,572 seeks, 478 scans, 0 lookups
- Size: 0.22 MB


### dbo.VendorCategoryPP

*Table rows: 17,675*

****[PK]** PK__VendorCategoryPP__2B8A53B1** (CLUSTERED)
- Key columns: `VCPId`
- Usage: 45 seeks, 2,584 scans, 1,864 lookups
- Size: 1.98 MB

**SK_VendorId** (NONCLUSTERED)
- Key columns: `VendorId`
- Usage: 1,864 seeks, 1 scans, 0 lookups
- Size: 0.67 MB


### dbo.VendorCertificates

*Table rows: 0*

****[PK]** PK__VendorCe__6273C2F02BF9F766** (CLUSTERED)
- Key columns: `VendorCertificateId`
- Usage: 1 seeks, 3 scans, 0 lookups
- Size: 0.00 MB


### dbo.VendorContacts

*Table rows: 23,291*

****[PK]** PK__VendorCo__A4D440DD7E883271** (CLUSTERED)
- Key columns: `VendorContactId`
- Usage: 62,391 seeks, 7,625 scans, 2,250 lookups
- Size: 7.80 MB

**SKI_Vendor_VendorcontactidActiveBidcontactPocontact** (NONCLUSTERED)
- Key columns: `VendorId, Active, POContact DESC, VendorContactId`
- Included: `BidContact`
- Usage: 175,325 seeks, 4 scans, 0 lookups
- Size: 0.79 MB

**SKI_Vendor_All** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `VendorContactId, Active, SalutationId, FirstName, LastName, Suffix, Address1, Address2, City, State, Zipcode, Phone, Fax, EMail, BidContact, POContact, FullName`
- Usage: 6,919,407 seeks, 5,725 scans, 0 lookups
- Size: 5.30 MB

**_dta_index_VendorContacts_7_183372118__K2_K1_8_9_10_11_12_13** (NONCLUSTERED)
- Key columns: `VendorId, VendorContactId`
- Included: `Address1, Address2, City, State, Zipcode, Phone`
- Usage: 3,046,675 seeks, 0 scans, 0 lookups
- Size: 2.98 MB

**_dta_index_VendorContacts_7_183372118__K3_K2_K1_K20** (NONCLUSTERED)
- Key columns: `Active, VendorId, VendorContactId, POContact`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.77 MB


### dbo.VendorDocRequest

*Table rows: 14*

****[PK]** PK_VendorDocRequest** (CLUSTERED)
- Key columns: `VendorDocRequestId`
- Usage: 6,081 seeks, 1,015 scans, 0 lookups
- Size: 0.95 MB


### dbo.VendorDocRequestDetail

*Table rows: 52*

****[PK]** PK_VendorDocRequestDetail** (CLUSTERED)
- Key columns: `VendorDocRequestDetailId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.VendorDocRequestStatus

*Table rows: 14*

****[PK]** PK_VendorDocRequestStatus** (NONCLUSTERED)
- Key columns: `VendorDocRequestStatusId`
- Usage: 3,040 seeks, 3,040 scans, 0 lookups
- Size: 0.02 MB


### dbo.VendorLocations

*Table rows: 0*

****[PK]** PK__VendorLocations__55F8BC25** (CLUSTERED)
- Key columns: `VendorLocationId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.VendorLogoDisplays

*Table rows: 0*

****[PK]** PK__VendorLo__68EBDD4F7211DF33** (CLUSTERED)
- Key columns: `VendorLogoDisplayID`
- Usage: 1 seeks, 65,111 scans, 0 lookups
- Size: 0.00 MB


### dbo.VendorOrders

*Table rows: 5,472*

****[PK]** PK__VendorOr__477DCB3BB41239CE** (CLUSTERED)
- Key columns: `VendorOrderId`
- Usage: 61 seeks, 991 scans, 0 lookups
- Size: 132.62 MB


### dbo.VendorOverrideMessages

*Table rows: 5*

****[PK]** PK__VendorOverrideMe__01D73E63** (CLUSTERED)
- Key columns: `VOMId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### dbo.VendorPOtags

*Table rows: 0*

***[Unique]* MSmerge_index_2044234733** (NONCLUSTERED)
- Key columns: `SysId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### dbo.VendorQuery

*Table rows: 11,553*

****[PK]** PK_VendorQuery** (CLUSTERED)
- Key columns: `VendorQueryId`
- Usage: 3 seeks, 3 scans, 0 lookups
- Size: 115.40 MB

**SKI_Bidheader_QueryVendor** (NONCLUSTERED)
- Key columns: `BidHeaderId`
- Included: `VendorQueryId, VendorId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 0.33 MB


### dbo.VendorQueryDetail

*Table rows: 130,112*

****[PK]** PK_VendorQueryDetail** (CLUSTERED)
- Key columns: `VendorQueryDetailId`
- Usage: 0 seeks, 2 scans, 0 lookups
- Size: 22.41 MB

**SK_VendorQueryId** (NONCLUSTERED)
- Key columns: `VendorQueryId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 2.73 MB


### dbo.VendorQueryMSRP

*Table rows: 140*

****[PK]** PK_VendorQueryMSRP** (CLUSTERED)
- Key columns: `VendorQueryMSRPId`
- Usage: 5 seeks, 3 scans, 0 lookups
- Size: 69.25 MB


### dbo.VendorQueryMSRPDetail

*Table rows: 2*

****[PK]** PK_VendorQueryMSRPDetail** (CLUSTERED)
- Key columns: `VendorQueryMSRPDetailId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.03 MB


### dbo.VendorQueryMSRPStatus

*Table rows: 2*

****[PK]** PK_VendorQueryMSRPStatus** (CLUSTERED)
- Key columns: `VendorQueryMSRPStatusId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.02 MB


### dbo.VendorQueryStatus

*Table rows: 30,222*

****[PK]** PK_VendorQueryStatus** (NONCLUSTERED)
- Key columns: `VendorQueryStatusId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.52 MB

**IX_VendorQueryStatus** (NONCLUSTERED)
- Key columns: `VendorQueryId`
- Usage: 1 seeks, 0 scans, 0 lookups
- Size: 0.71 MB


### dbo.VendorQueryTandM

*Table rows: 1,889*

****[PK]** PK_VendorQueryTandM** (CLUSTERED)
- Key columns: `VendorQueryTandMId`
- Usage: 21 seeks, 4 scans, 0 lookups
- Size: 933.88 MB


### dbo.VendorQueryTandMDetail

*Table rows: 1,142*

****[PK]** PK_VendorQueryTandMDetail** (CLUSTERED)
- Key columns: `VendorQueryTandMDetailId`
- Usage: 0 seeks, 14 scans, 0 lookups
- Size: 0.37 MB


### dbo.VendorQueryTandMStatus

*Table rows: 1,746*

****[PK]** PK_VendorQueryTandMStatus** (CLUSTERED)
- Key columns: `VendorQueryTandMStatusId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.13 MB


### dbo.Vendors

*Table rows: 18,900*

****[PK]** PK_Vendors** (CLUSTERED)
- Key columns: `VendorId`
- Usage: 4,230,695 seeks, 5,581 scans, 8,542 lookups
- Size: 3.66 MB

**_dta_index_Vendors_9_752057765__K1_K4** (NONCLUSTERED)
- Key columns: `VendorId, Name`
- Usage: 4,783,958 seeks, 414 scans, 0 lookups
- Size: 0.74 MB

**_dta_index_Vendors_7_1906157886__K1_3_4** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `Code, Name`
- Usage: 458,178 seeks, 2,382 scans, 0 lookups
- Size: 1.26 MB

**_dta_index_Vendors_7_1906157886__K1_4** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `Name`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 1.12 MB

**_dta_index_Vendors_7_1906157886__K1_3** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `Code`
- Usage: 0 seeks, 20 scans, 0 lookups
- Size: 0.45 MB

**SK_Code** (NONCLUSTERED)
- Key columns: `Code`
- Usage: 3 seeks, 3,359 scans, 0 lookups
- Size: 0.41 MB

**SK_ActiveName** (NONCLUSTERED)
- Key columns: `Active, Name`
- Usage: 10,150 seeks, 5 scans, 0 lookups
- Size: 1.24 MB

**SKI_ActiveCode_Vendor** (NONCLUSTERED)
- Key columns: `Active, Code`
- Included: `VendorId`
- Usage: 10,298 seeks, 5 scans, 0 lookups
- Size: 0.55 MB

**_dta_stat_279372460_18** (NONCLUSTERED)
- Key columns: `HostURL`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB

**_dta_index_Vendors_7_279372460__K1_3_4_5_6_7_8_9_10_11_15_24** (NONCLUSTERED)
- Key columns: `VendorId`
- Included: `Code, Name, Address1, Address2, Address3, City, State, ZipCode, Phone, ShippingPercentage, UploadType`
- Usage: 1,405 seeks, 38 scans, 0 lookups
- Size: 2.73 MB


### dbo.VendorSessions

*Table rows: 10,787*

****[PK]** PK_VendorSessions** (CLUSTERED)
- Key columns: `VendorSessionId`
- Usage: 2,413 seeks, 23 scans, 0 lookups
- Size: 1.02 MB

***[Unique]* SK_jSessionPK** (NONCLUSTERED)
- Key columns: `jSession, VendorSessionId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.13 MB


### dbo.VendorUploads

*Table rows: 1,533,266*

****[PK]** PK__VendorUploads__4C813328** (CLUSTERED)
- Key columns: `UploadId`
- Usage: 804 seeks, 0 scans, 145,291 lookups
- Size: 213.15 MB

**SK_PO** (NONCLUSTERED)
- Key columns: `poid`
- Usage: 145,291 seeks, 0 scans, 0 lookups
- Size: 23.86 MB


### dbo.VPOLoginAttempts

*Table rows: 0*

****[PK]** PK__VPOLogin__DE43609E57D879A4** (CLUSTERED)
- Key columns: `VPOLoginAttemptId`
- Usage: 1 seeks, 2 scans, 0 lookups
- Size: 0.00 MB


### dbo.VPORegistrations

*Table rows: 6*

****[PK]** PK__VPORegis__811068474D5AEB31** (CLUSTERED)
- Key columns: `VPORegistrationId`
- Usage: 2 seeks, 3 scans, 0 lookups
- Size: 0.02 MB


### dbo.VPOVendorLinks

*Table rows: 10*

****[PK]** PK__VPOVendo__8C21AD725313C487** (CLUSTERED)
- Key columns: `VPOVendorLinkId`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.02 MB

**IX_VPOVendorLinks** (NONCLUSTERED)
- Key columns: `VPORegistrationId, VendorId`
- Usage: 0 seeks, 3 scans, 0 lookups
- Size: 0.02 MB


### dbo.z4zbReqDetail

*Table rows: 0*

**SKI_Filtered_DetailPrice** (NONCLUSTERED)
- Key columns: `Filtered`
- Included: `DetailId, BidPrice`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB

**SKI_DetailFiltered_BidPrice** (NONCLUSTERED)
- Key columns: `DetailId, Filtered`
- Included: `BidPrice`
- Usage: 0 seeks, 1 scans, 0 lookups
- Size: 0.00 MB


### EDSIQWebUser.TableOfContents

*Table rows: 6,664*

****[PK]** PK_TableOfContents** (CLUSTERED)
- Key columns: `TCId`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.72 MB


### EDSIQWebUser.UnsubscriptionEmail

*Table rows: 0*

****[PK]** PK_UnsubscriptionEmail** (CLUSTERED)
- Key columns: `Id`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB

***[Unique]* UnsubscriptionEmail_uindex** (NONCLUSTERED)
- Key columns: `Email`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.00 MB


### EDSWebRpts.REPMAN_GROUPS

*Table rows: 1*

****[PK]** PK__REPMAN_GROUPS__2DFCAC08** (CLUSTERED)
- Key columns: `GROUP_CODE`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB


### EDSWebRpts.REPMAN_REPORTS

*Table rows: 1*

****[PK]** PK__REPMAN_REPORTS__2C146396** (CLUSTERED)
- Key columns: `REPORT_NAME`
- Usage: 0 seeks, 0 scans, 0 lookups
- Size: 0.02 MB

