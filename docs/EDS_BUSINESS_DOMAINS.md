# EDS Database - Business Domain Guide

Generated: 2026-01-09 09:49:19

This document organizes database tables by functional business domain to help understand the database structure and relationships.

---

## Domain Summary

| Domain | Tables | Total Rows | Description |
|--------|--------|------------|-------------|
| [Bidding](#bidding) | 60 | 444,609,260 | Bid management, awards, and bid request processing |
| [Orders & Purchasing](#orders--purchasing) | 80 | 386,395,378 | Purchase orders, requisitions, and order details |
| [Vendors](#vendors) | 31 | 2,033,657 | Vendor registration, profiles, and management |
| [Inventory & Items](#inventory--items) | 30 | 205,568,313 | Product catalog, items, and pricing |
| [Users & Security](#users--security) | 22 | 27,392,709 | User accounts, sessions, and approvals |
| [Reporting](#reporting) | 12 | 164,672,295 | Reports, alerts, audit logs, and analytics |
| [Documents](#documents) | 11 | 1,784,388 | Document management and file storage |
| [Finance & Budgets](#finance--budgets) | 5 | 16,376 | Budget tracking and financial data |
| [Configuration](#configuration) | 3 | 4 | System settings and parameters |
| [Communication](#communication) | 11 | 39,259 | Email, notifications, and messaging |
| [Other](#other) | 117 | 3,788,405 | Miscellaneous tables |

---

## Bidding {bidding}

Bid management, awards, and bid request processing

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| BidHeaderDetail | 123,789,710 | 9 | BidHeaderDetailId | BidHeaderId, DetailId, BidRequestItemId (+2) |
| BidHeaderDetail_Orig | 102,658,927 | 7 | BidHeaderDetailId | BidHeaderId, DetailId, BidRequestItemId |
| BidResults_Orig | 55,592,743 | 46 | BidResultsId | BidImportId, BidHeaderId, BidRequestItemId (+11) |
| BidResults | 33,034,634 | 58 | BidResultsId | BidImportId, BidHeaderId, BidRequestItemId (+11) |
| BidRequestItems | 27,855,481 | 15 | BidRequestItemId | BidHeaderId, ItemId |
| BidItems | 26,906,489 | 20 | BidItemId | BidId, ItemId, AwardId (+3) |
| BidRequestItems_Orig | 25,521,585 | 15 | BidRequestItemId | BidHeaderId, ItemId |
| BidResultChanges | 18,229,521 | 10 | BRChangeId | BidResultsId |
| BidItems_Old | 16,238,384 | 19 | BidItemId | BidId, ItemId, AwardId (+3) |
| BidMgrTagFile | 4,335,799 | 6 | BidMgrTagFileId |  |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| BidHeaderDetail | 123,789,710 | 2024-10-28 05:02:15.220000 |
| BidHeaderDetail_Orig | 102,658,927 | 2021-09-11 19:40:09.687000 |
| BidResults_Orig | 55,592,743 | 2021-09-11 18:58:41.837000 |
| BidResults | 33,034,634 | 2025-07-10 09:54:37.057000 |
| BidRequestItems | 27,855,481 | 2024-10-28 05:04:42.273000 |
| BidItems | 26,906,489 | 2024-10-28 05:03:25.067000 |
| BidRequestItems_Orig | 25,521,585 | 2021-09-11 18:50:17.617000 |
| BidResultChanges | 18,229,521 | 2024-06-21 21:52:24.963000 |
| BidItems_Old | 16,238,384 | 2021-03-17 23:18:57.703000 |
| BidMgrTagFile | 4,335,799 | 2024-06-21 21:31:28.480000 |
| BidRequestPriceRanges | 1,897,760 | 2024-06-21 21:52:12.693000 |
| BidMappedItems | 1,456,772 | 2025-06-24 05:14:58.113000 |
| BidProductLinePrices | 1,323,391 | 2024-06-21 21:30:58.943000 |
| BidAnswersJournal | 1,250,977 | 2024-06-21 22:41:18.687000 |
| DMSVendorBidDocuments | 736,489 | 2026-01-09 09:19:46.823000 |
| BidAnswers | 545,208 | 2024-06-21 21:31:31.293000 |
| BidMSRPResultPrices | 422,692 | 2024-06-21 21:35:33.737000 |
| BidRequestOptions | 422,035 | 2024-06-21 21:52:09.563000 |
| BidProductLines | 286,318 | 2024-06-21 21:31:14.497000 |
| BidManufacturers | 252,521 | 2024-06-21 21:35:29.893000 |
| BidResultsChangeLog | 238,978 | 2024-06-21 21:54:25.560000 |
| BidRequestProductLines | 175,875 | 2024-06-21 21:52:13.287000 |
| BidHeaderDocument | 161,488 | 2024-06-21 21:34:11.400000 |
| Bids | 143,697 | 2024-06-21 21:54:27.443000 |
| Awards | 135,686 | 2024-06-21 21:31:12.267000 |
| BidMSRPResultsProductLines | 110,442 | 2024-06-21 21:35:35.020000 |
| BidHeaderCheckList | 110,423 | 2024-06-21 21:31:37.127000 |
| BidRequestManufacturer | 104,823 | 2024-06-21 22:41:19.933000 |
| TMAwards | 89,597 | 2025-02-18 05:15:33.940000 |
| BidsCatalogList | 82,649 | 2024-06-21 21:54:27.997000 |
| AwardsCatalogList | 82,484 | 2024-06-21 21:31:15.513000 |
| BidImportCounties | 64,134 | 2024-06-21 21:34:14.710000 |
| BidImports | 54,678 | 2024-06-21 21:34:16.523000 |
| BidTradeCounties | 42,912 | 2024-06-21 21:54:28.323000 |
| BidMSRPResults | 40,980 | 2024-06-21 21:35:34.323000 |
| BidRequestItemMergeActions | 36,542 | 2024-06-21 21:51:29.793000 |
| BidImportCatalogList | 32,921 | 2025-01-27 16:03:22.757000 |
| DMSBidDocuments | 29,032 | 2024-11-21 05:09:26.193000 |
| BidRequestItemMergeActions_Saved_101521 | 27,298 | 2021-10-15 12:51:08.043000 |
| BidRequestItemMergeActions_Orig | 27,168 | 2021-09-11 20:01:13.797000 |
| BidQuestions | 23,509 | 2024-06-21 22:41:19.313000 |
| Awardings | 11,023 | 2024-06-21 21:31:09.540000 |
| BidDocument | 10,558 | 2024-06-21 21:31:35.053000 |
| BidHeaders | 9,548 | 2025-07-01 21:57:21.167000 |
| BidTrades | 1,591 | 2024-06-21 21:54:29.210000 |
| BidPackageDocument | 1,430 | 2024-06-21 21:35:36.553000 |
| BidderCheckListPkgDetail | 1,195 | 2024-06-21 21:31:32.560000 |
| BidReawards | 611 | 2024-06-21 21:51:29.437000 |
| BidDocumentTypes | 298 | 2024-06-21 21:31:35.543000 |
| BidderCheckList | 140 | 2024-06-21 21:31:32.130000 |
| BidderCheckListPkgHeader | 56 | 2024-06-21 21:31:32.943000 |
| BidPackage | 50 | 2024-06-21 21:35:36.153000 |
| AwardTypes | 2 | 2024-06-21 21:31:12.833000 |
| BidTypes | 2 | 2024-06-21 21:54:29.420000 |
| BidCalendar | 1 | 2024-06-21 21:31:31.703000 |
| BidHeaderDocuments | 1 | 2024-06-21 21:34:11.780000 |
| BidMgrConfiguration | 1 | 2024-06-21 21:35:31.720000 |
| BidResponses | 1 | 2024-06-21 21:52:13.560000 |
| BidManagers | 0 | 2024-06-21 21:35:28.127000 |
| z4zbBidFix | 0 | 2018-03-19 17:18:50.693000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **BidHeader** (referenced by 24 tables)
- **BidImport** (referenced by 10 tables)
- **Item** (referenced by 8 tables)
- **BidRequestItem** (referenced by 7 tables)
- **Category** (referenced by 6 tables)

---

## Orders & Purchasing {orders--purchasing}

Purchase orders, requisitions, and order details

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| OrderBookDetailOld | 187,630,151 | 22 | OrderBookDetailId | OrderBookId, ItemId, BidItemId (+5) |
| ReportSessionLinks | 51,989,978 | 4 | RSLId | RSId, IntId, AuxId |
| OrderBookDetail | 37,804,007 | 22 | OrderBookDetailId | OrderBookId, ItemId, BidItemId (+5) |
| Detail | 30,841,291 | 61 | DetailId | RequisitionId, CatalogId, ItemId (+20) |
| DetailChanges | 26,502,061 | 9 | DetailChangeId | DetailId, RequisitionId, ItemId (+1) |
| PODetailItems | 24,327,506 | 14 | PODetailItemId | POId, DetailId, ItemId (+3) |
| ReportSession | 5,282,298 | 11 | RSId | ReportProcessorId |
| BatchDetail | 5,020,036 | 37 | BatchDetailId | BatchBookId, BatchId, CometId (+7) |
| DetailChangeLog | 2,924,942 | 16 | DetailChangeId | DetailId, RequisitionId, ItemId (+7) |
| DetailNotifications | 2,779,169 | 10 | DetailNotificationId | DetailId, NotificationId, OrigItemId (+3) |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| OrderBookDetailOld | 187,630,151 | 2021-11-08 21:29:55.377000 |
| ReportSessionLinks | 51,989,978 | 2024-06-21 21:57:15.410000 |
| OrderBookDetail | 37,804,007 | 2024-06-21 22:33:09.703000 |
| Detail | 30,841,291 | 2025-06-26 11:42:17.350000 |
| DetailChanges | 26,502,061 | 2024-06-21 21:58:39.760000 |
| PODetailItems | 24,327,506 | 2024-06-21 22:48:37.943000 |
| ReportSession | 5,282,298 | 2024-06-21 22:34:54.313000 |
| BatchDetail | 5,020,036 | 2024-06-21 21:59:55.823000 |
| DetailChangeLog | 2,924,942 | 2024-06-21 21:57:59.453000 |
| DetailNotifications | 2,779,169 | 2025-02-06 06:07:58.753000 |
| PO | 2,462,014 | 2025-06-13 16:45:21.827000 |
| Requisitions | 2,078,232 | 2025-06-26 11:40:37.293000 |
| RequisitionChangeLog | 1,938,491 | 2024-06-21 22:02:01.147000 |
| RTK_ReportItems | 1,006,140 | 2025-06-12 05:20:21.173000 |
| ImportDetail | 882,935 | 2024-06-21 22:03:05.827000 |
| OrderBookLog | 474,297 | 2024-06-21 22:33:10.603000 |
| POStatus | 406,158 | 2024-06-21 22:33:44.833000 |
| PricingConsolidatedOrderCounts | 401,387 | 2021-11-09 18:46:47.393000 |
| POQueueItems | 398,104 | 2024-07-03 05:07:46.387000 |
| BatchBook | 217,611 | 2021-11-08 21:28:07.370000 |
| RTK_MSDSDetail | 151,665 | 2024-06-21 22:35:07.547000 |
| MSDSDetail | 138,516 | 2024-06-21 22:41:21.630000 |
| VendorQueryDetail | 130,112 | 2024-06-21 22:40:48.167000 |
| POPrintTaggedPOFile | 120,948 | 2022-05-18 22:44:42.647000 |
| DetailMatch | 103,534 | 2024-06-21 21:58:41.857000 |
| MSRPExcelImport | 76,315 | 2024-06-21 22:32:29.693000 |
| POPageSummary | 73,456 | 2024-06-21 22:33:13.507000 |
| PostCatalogDetail | 39,099 | 2024-06-21 22:33:45.510000 |
| OrderBooks | 30,399 | 2024-06-21 22:33:11.107000 |
| POQueue | 26,748 | 2024-06-21 22:33:15.643000 |
| RequisitionNotes | 24,752 | 2025-04-06 21:19:41.813000 |
| ImportCatalogDetail | 17,646 | 2024-06-21 22:03:03.357000 |
| RequisitionNoteEmails | 16,161 | 2024-06-21 22:34:57.953000 |
| Batches | 14,507 | 2021-11-08 21:28:19.310000 |
| DistrictProposedCharges | 11,997 | 2024-06-21 21:59:11.270000 |
| POLayoutDetail | 6,841 | 2024-06-21 22:33:12.930000 |
| SulphiteDetail | 6,280 | 2021-11-08 21:29:55.727000 |
| ImportMessages | 5,500 | 2024-06-21 22:03:09.097000 |
| VendorOrders | 5,467 | 2025-06-12 12:21:45.440000 |
| POTempDetails | 4,014 | 2021-11-08 21:29:55.490000 |
| PostCatalogHeader | 3,327 | 2024-06-21 22:33:45.753000 |
| TMImport | 3,114 | 2024-06-21 21:57:25.300000 |
| TMImport5 | 2,889 | 2018-03-19 17:18:48.417000 |
| ImportCatalogHeader | 2,822 | 2024-06-21 22:03:03.850000 |
| TagFilePos_ | 2,259 | 2020-11-17 18:15:57.450000 |
| TMImport6 | 2,134 | 2018-03-19 17:18:48.457000 |
| TMImport1 | 1,885 | 2018-03-19 17:18:48.310000 |
| BatchDetailInserts | 1,176 | 2021-11-08 21:28:19.267000 |
| VendorQueryTandMDetail | 1,142 | 2024-06-21 22:41:22.737000 |
| TMImport3 | 833 | 2018-03-19 17:18:48.383000 |
| ImportProcesses | 754 | 2024-06-21 22:03:09.333000 |
| POLayouts | 632 | 2024-06-21 22:33:13.363000 |
| MSRPExcelExport | 563 | 2024-06-21 21:59:56.757000 |
| UserImports | 328 | 2022-02-07 15:51:38.530000 |
| Imports | 301 | 2024-06-21 22:03:09.817000 |
| TMImport2 | 147 | 2018-03-19 17:18:48.350000 |
| POLayoutFields | 56 | 2024-06-21 22:33:13.053000 |
| VendorDocRequestDetail | 52 | 2024-06-21 22:40:43.327000 |
| SulphiteImport | 49 | 2021-11-08 21:29:55.753000 |
| POTemp | 37 | 2021-11-08 21:29:55.467000 |
| RTK_Purposes | 35 | 2024-06-21 22:35:07.730000 |
| CatalogImportFields | 15 | 2024-06-21 21:57:15.667000 |
| MSRPOptions | 12 | 2024-06-21 22:32:30.153000 |
| OrderBookTypes | 12 | 2024-06-21 22:33:11.303000 |
| DistrictReports | 11 | 2024-06-21 21:59:11.437000 |
| VPOVendorLinks | 10 | 2024-06-21 22:41:16.060000 |
| OrderBookAlwaysAdd | 9 | 2024-06-21 22:32:37.067000 |
| VPORegistrations | 6 | 2024-06-21 22:41:15.683000 |
| VendorQueryMSRPDetail | 2 | 2024-06-21 22:41:22.427000 |
| DetailHold | 1 | 2024-06-21 21:58:41.590000 |
| AccountingDetail | 0 | 2024-06-21 21:30:30.927000 |
| CatalogImportMap | 0 | 2024-06-21 21:57:15.913000 |
| CatalogRequestDetail | 0 | 2024-06-21 22:41:20.740000 |
| DetailUploads | 0 | 2024-06-21 21:59:06.090000 |
| POIDTable | 0 | 2024-06-21 22:33:12.657000 |
| POStatusTable | 0 | 2024-06-21 22:33:44.967000 |
| QuestionnaireResponses | 0 | 2024-06-21 22:33:54.317000 |
| VendorPOtags | 0 | 2024-06-21 22:40:44.227000 |
| VPOLoginAttempts | 0 | 2024-06-21 22:41:15.377000 |
| z4zbReqDetail | 0 | 2018-03-19 17:18:50.720000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **Vendor** (referenced by 15 tables)
- **Item** (referenced by 14 tables)
- **Detail** (referenced by 12 tables)
- **Requisition** (referenced by 11 tables)
- **BidHeader** (referenced by 11 tables)

---

## Vendors {vendors}

Vendor registration, profiles, and management

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| VendorUploads | 1,533,264 | 8 | UploadId | cxmlsessionid, poid, PayloadID |
| DistrictVendor | 315,684 | 6 | DistrictVendorId | DistrictId, VendorId |
| ShippingVendor | 38,754 | 5 | ShippingVendorId | VendorId, ShippingId |
| VendorQueryStatus | 30,222 | 5 | VendorQueryStatusId | VendorQueryId, StatusId |
| VendorContacts | 23,291 | 24 | VendorContactId | VendorId, SalutationId |
| Vendors | 18,900 | 42 | VendorId | DistrictId, VendorDeliveryRuleId |
| VendorCategoryPP | 17,675 | 5 | VCPId | VendorId, CategoryId, DistrictId (+1) |
| TMVendors | 16,173 | 8 | TMVendorId | VendorId, TradeId, CountyId (+1) |
| VendorQuery | 11,553 | 14 | VendorQueryId | BidHeaderId, VendorId, BidImportId |
| VendorSessions | 10,787 | 8 | VendorSessionId | VendorId, VPORegistrationId |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| VendorUploads | 1,533,264 | 2024-06-21 22:41:14.743000 |
| DistrictVendor | 315,684 | 2025-02-19 05:14:02.093000 |
| ShippingVendor | 38,754 | 2024-06-21 22:39:16.673000 |
| VendorQueryStatus | 30,222 | 2024-06-21 22:40:51.010000 |
| VendorContacts | 23,291 | 2024-06-21 22:40:42.193000 |
| Vendors | 18,900 | 2026-01-02 15:49:14.360000 |
| VendorCategoryPP | 17,675 | 2024-06-21 22:40:40.997000 |
| TMVendors | 16,173 | 2024-06-21 21:57:38.230000 |
| VendorQuery | 11,553 | 2024-06-21 22:40:45.597000 |
| VendorSessions | 10,787 | 2024-06-21 22:40:53.983000 |
| VendorCategory | 6,785 | 2024-06-21 22:40:40.703000 |
| DMSVendorDocuments | 6,485 | 2026-01-09 09:19:47.890000 |
| VendorQueryTandM | 1,889 | 2024-06-21 22:40:51.180000 |
| VendorQueryTandMStatus | 1,746 | 2024-06-21 22:41:23.030000 |
| TMSurveyNewVendors | 186 | 2024-06-21 22:39:21.437000 |
| VendorQueryMSRP | 140 | 2024-06-21 22:40:48.967000 |
| CommonVendorQuery | 43 | 2024-06-21 21:57:24.033000 |
| CommonTandMVendorQuery | 22 | 2024-06-21 21:57:23.583000 |
| VendorDocRequest | 14 | 2024-06-21 22:40:42.833000 |
| VendorDocRequestStatus | 14 | 2024-06-21 22:40:43.460000 |
| VendorCatalogNote | 11 | 2024-06-21 22:40:40.253000 |
| HolidayCalendarVendor | 7 | 2024-02-06 15:19:21.277000 |
| VendorOverrideMessages | 5 | 2024-06-21 22:40:44.157000 |
| CommonMSRPVendorQuery | 4 | 2024-06-21 21:57:23.310000 |
| VendorQueryMSRPStatus | 2 | 2024-06-21 22:41:22.547000 |
| VendorDeliveryRule | 1 | 2024-02-06 15:19:21.480000 |
| CommonVendorQueryAnswer | 0 | 2024-06-21 21:57:24.400000 |
| RTK_VendorLinks | 0 | 2024-06-21 22:35:14.010000 |
| VendorCertificates | 0 | 2024-06-21 22:40:41.113000 |
| VendorLocations | 0 | 2024-06-21 22:40:43.650000 |
| VendorLogoDisplays | 0 | 2024-06-21 22:40:43.767000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **Vendor** (referenced by 15 tables)
- **Status** (referenced by 4 tables)
- **BidHeader** (referenced by 4 tables)
- **BidImport** (referenced by 4 tables)
- **District** (referenced by 3 tables)

---

## Inventory & Items {inventory--items}

Product catalog, items, and pricing

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| CrossRefs | 150,631,265 | 49 | CrossRefId | ItemId, CatalogId, RTK_MSDSId (+4) |
| Items | 30,153,920 | 38 | ItemId | CategoryId, UnitId, ParentCatalogId (+10) |
| CatalogTextParts | 17,179,537 | 4 | CatalogTextPartId | CatalogTextId |
| allitems | 6,276,768 | 19 | *None* | BidHeaderId, ItemId, VendorId (+7) |
| HeaderWorkItems | 491,824 | 2 | *None* | OBDWorkId, ItemId |
| ItemUpdates | 198,886 | 5 | ItemUpdateId | ItemId |
| ProductVerificationResults | 197,830 | 7 | VerificationId | EntryId |
| PriceRanges | 120,619 | 8 | PriceRangeId | CategoryId, ManufacturerId, ManufacturerProductLineId (+1) |
| CatalogText | 112,799 | 5 | CatalogTextId | CatalogId |
| FreezeItems2015 | 102,339 | 28 | *None* | CometId, DetailId, RequisitionId (+6) |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| CrossRefs | 150,631,265 | 2025-08-26 15:37:33.967000 |
| Items | 30,153,920 | 2025-03-05 16:04:08.417000 |
| CatalogTextParts | 17,179,537 | 2021-11-08 21:28:47.520000 |
| allitems | 6,276,768 | 2021-11-08 21:28:06.850000 |
| HeaderWorkItems | 491,824 | 2021-11-08 21:28:49.343000 |
| ItemUpdates | 198,886 | 2021-11-08 21:28:49.407000 |
| ProductVerificationResults | 197,830 | 2025-10-31 17:14:38.067000 |
| PriceRanges | 120,619 | 2024-06-21 22:33:47.393000 |
| CatalogText | 112,799 | 2021-11-08 21:28:22.250000 |
| FreezeItems2015 | 102,339 | 2024-06-21 21:57:16.640000 |
| RTK_Items | 64,627 | 2024-06-21 22:35:04.177000 |
| FreezeItems | 15,435 | 2024-06-21 22:01:53.743000 |
| ManufacturerProductLines | 14,298 | 2024-06-21 22:32:27.570000 |
| Catalog | 3,897 | 2025-05-19 14:49:17.810000 |
| Carolina Living Items | 2,017 | 2023-06-14 15:01:10.960000 |
| PPCatalogs | 1,664 | 2024-06-21 22:33:45.993000 |
| PricePlans | 584 | 2024-06-21 22:33:47.093000 |
| MappedItems | 2 | 2024-06-21 22:32:28.220000 |
| PriceListTypes | 2 | 2024-06-21 22:33:46.907000 |
| AddendumItems | 0 | 2024-06-21 21:30:47.287000 |
| additems | 0 | 2024-06-21 21:30:49.150000 |
| CalendarItems | 0 | 2024-06-21 21:54:31.027000 |
| CatalogPricing | 0 | 2024-06-21 21:57:16.123000 |
| CatalogRequest | 0 | 2024-06-21 21:57:16.320000 |
| CatalogRequestStatus | 0 | 2024-06-21 22:41:20.853000 |
| ItemContractPrices | 0 | 2021-11-08 21:28:49.373000 |
| ItemDocuments | 0 | 2024-06-21 22:27:30.200000 |
| OBPrices | 0 | 2021-11-08 21:28:49.433000 |
| PriceHolds | 0 | 2024-06-21 22:33:46.537000 |
| Prices | 0 | 2024-06-21 22:41:21.730000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **Item** (referenced by 10 tables)
- **Category** (referenced by 9 tables)
- **Vendor** (referenced by 9 tables)
- **Catalog** (referenced by 8 tables)
- **CrossRef** (referenced by 6 tables)

---

## Users & Security {users--security}

User accounts, sessions, and approvals

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| SessionTable | 12,395,179 | 27 | SessionId | DistrictId, SchoolId, UserId (+10) |
| Approvals | 7,824,818 | 7 | ApprovalId | ApprovalById, StatusId, RequisitionId (+1) |
| UserAccounts | 3,329,135 | 9 | UserAccountId | AccountId, BudgetId, BudgetAccountId (+1) |
| BudgetAccounts | 1,399,984 | 7 | BudgetAccountId | BudgetId, AccountId |
| PendingApprovals | 567,122 | 15 | SysId | SessionId, SchoolId, UserId (+8) |
| IPQueueUsers | 489,217 | 7 | IPQueueUserId | IPQueueId, UserId |
| SecurityRoleUsers | 355,335 | 3 | SecurityRoleUserId | SecurityRoleId, UserId |
| Users | 338,299 | 41 | UserId | DistrictId, SchoolId, ShippingId (+5) |
| ApprovalsHistory | 332,112 | 7 | ApprovalId | ApprovalById, StatusId, RequisitionId (+1) |
| SSOLoginTracking | 123,234 | 6 | *None* |  |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| SessionTable | 12,395,179 | 2025-04-16 02:54:40.350000 |
| Approvals | 7,824,818 | 2024-06-21 22:45:16.390000 |
| UserAccounts | 3,329,135 | 2025-06-26 11:38:44.770000 |
| BudgetAccounts | 1,399,984 | 2025-06-26 11:42:47.357000 |
| PendingApprovals | 567,122 | 2021-11-08 21:29:55.440000 |
| IPQueueUsers | 489,217 | 2024-06-21 22:03:28.930000 |
| SecurityRoleUsers | 355,335 | 2024-06-21 22:36:30.163000 |
| Users | 338,299 | 2025-06-25 11:22:01.827000 |
| ApprovalsHistory | 332,112 | 2024-06-21 22:45:17.703000 |
| SSOLoginTracking | 123,234 | 2025-06-28 07:07:31.850000 |
| Accounts | 108,696 | 2024-06-21 22:41:30.240000 |
| CXmlSession | 64,845 | 2024-06-21 21:57:46.850000 |
| UserTrees | 56,920 | 2024-06-21 22:40:40.043000 |
| UserAdminLog | 6,466 | 2024-06-21 22:39:24.347000 |
| SulphiteUsers | 1,209 | 2021-11-08 21:29:55.783000 |
| AccountingUserFields | 80 | 2024-06-21 21:30:35.157000 |
| AccountingFormats | 49 | 2024-06-21 21:30:33.807000 |
| ApprovalLevels | 9 | 2024-06-21 21:31:02.580000 |
| AccountSeparators | 0 | 2024-06-21 21:30:42.023000 |
| jSessions | 0 | 2021-11-08 06:59:30.497000 |
| SessionCmds | 0 | 2024-06-21 22:36:30.727000 |
| UserCategory | 0 | 2024-06-21 22:39:24.977000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **User** (referenced by 8 tables)
- **District** (referenced by 5 tables)
- **Requisition** (referenced by 5 tables)
- **Budget** (referenced by 5 tables)
- **School** (referenced by 4 tables)

---

## Reporting {reporting}

Reports, alerts, audit logs, and analytics

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| TransactionLog_HISTORY | 99,019,937 | 10 | SysId | SessionId |
| TransactionLogCF | 33,662,296 | 10 | SysId | SessionId |
| DebugMsgs | 20,840,159 | 3 | SysId |  |
| DebugMsgs_Orig | 5,211,696 | 3 | sysid |  |
| Audit | 2,568,656 | 7 | AuditId |  |
| ImageLog | 1,788,706 | 11 | imageLogId | imageId |
| EmailBlastLog | 1,437,241 | 12 | EmailBlastLogId | EmailBlastId, PrimaryRecipientId |
| TransmitLog | 143,139 | 5 | TransmitId |  |
| TmpLog | 461 | 2 | *None* |  |
| Alerts | 4 | 5 | AlertID | DistrictID |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| TransactionLog_HISTORY | 99,019,937 | 2025-04-07 06:01:32.303000 |
| TransactionLogCF | 33,662,296 | 2025-05-02 05:23:25.183000 |
| DebugMsgs | 20,840,159 | 2021-11-08 21:28:49.047000 |
| DebugMsgs_Orig | 5,211,696 | 2016-03-01 19:50:07.903000 |
| Audit | 2,568,656 | 2024-06-21 21:31:08.253000 |
| ImageLog | 1,788,706 | 2025-03-21 09:18:57.293000 |
| EmailBlastLog | 1,437,241 | 2024-06-21 22:01:52.413000 |
| TransmitLog | 143,139 | 2024-08-08 06:08:04.230000 |
| TmpLog | 461 | 2021-08-14 09:42:05.557000 |
| Alerts | 4 | 2024-06-21 21:30:51.453000 |
| ReqAudit | 0 | 2024-06-21 22:34:54.877000 |
| SDSLog | 0 | 2024-06-21 22:36:14.577000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **Session** (referenced by 2 tables)
- **image** (referenced by 1 tables)
- **EmailBlast** (referenced by 1 tables)
- **PrimaryRecipient** (referenced by 1 tables)
- **Requisition** (referenced by 1 tables)

---

## Documents {documents}

Document management and file storage

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| Images | 1,736,177 | 19 | imageId |  |
| ImageErrors | 26,727 | 4 | imageErrorId |  |
| RTK_CASFile | 7,881 | 19 | RTK_CASFileId | DOT_Id |
| RTK_LegacySchoolFile | 6,766 | 10 | LegacySchoolFileId | DistrictId, RTK_SitesId |
| TagFile_ | 6,235 | 4 | *None* |  |
| DMSSDSDocuments | 602 | 5 | Id | MSDSId, DocId |
| CSMessageFiles | 0 | 4 | CSMessageFileID | CSMessageID |
| PrintDocuments | 0 | 12 | PrintDocumentId | DistrictId, SchoolId, UserId |
| RTK_Documents | 0 | 12 | RTKDocumentId | DistrictId, FacilityId, SchoolId (+2) |
| TAGFILEP | 0 | 4 | USR, TBL, POS |  |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| Images | 1,736,177 | 2025-03-22 05:15:23.670000 |
| ImageErrors | 26,727 | 2025-03-21 09:44:35.430000 |
| RTK_CASFile | 7,881 | 2024-06-21 22:35:01.910000 |
| RTK_LegacySchoolFile | 6,766 | 2024-06-21 22:35:05.013000 |
| TagFile_ | 6,235 | 2020-11-17 18:15:56.337000 |
| DMSSDSDocuments | 602 | 2024-06-21 21:59:12.140000 |
| CSMessageFiles | 0 | 2024-06-21 21:57:38.727000 |
| PrintDocuments | 0 | 2024-06-21 22:33:50.923000 |
| RTK_Documents | 0 | 2024-06-21 22:35:02.343000 |
| TAGFILEP | 0 | 2020-11-17 18:15:57.263000 |
| WizHelpFile | 0 | 2021-11-08 07:01:38.257000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **District** (referenced by 3 tables)
- **School** (referenced by 2 tables)
- **User** (referenced by 2 tables)
- **DOT_** (referenced by 1 tables)
- **RTK_Sites** (referenced by 1 tables)

---

## Finance & Budgets {finance--budgets}

Budget tracking and financial data

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| Budgets | 16,376 | 12 | BudgetId | DistrictId |
| Invoices | 0 | 7 | InvoiceId | DistrictId, InvoiceTypeId |
| InvoiceTypes | 0 | 4 | InvoiceTypeId |  |
| Payments | 0 | 7 | PaymentId | DistrictId, InvoiceId, PaymentTypeId |
| PaymentTypes | 0 | 2 | PaymentTypeId |  |

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **District** (referenced by 3 tables)
- **InvoiceType** (referenced by 1 tables)
- **Invoice** (referenced by 1 tables)
- **PaymentType** (referenced by 1 tables)

---

## Configuration {configuration}

System settings and parameters

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| NotificationOptions | 4 | 2 | NotificationOptionId |  |
| Options | 0 | 4 | OptionId |  |
| OptionsLink | 0 | 4 | OptionLinkId | OptionId, LinkId |

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **Option** (referenced by 1 tables)
- **Link** (referenced by 1 tables)

---

## Communication {communication}

Email, notifications, and messaging

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| EmailBlast | 16,701 | 22 | EmailBlastId | Reference1Id, Reference2Id |
| CSMessages | 11,621 | 3 | CSMessageID | UserID |
| DistrictNotifications | 6,043 | 9 | DistrictNotificationId | DistrictId, CategoryId, UserId |
| DistrictContacts | 3,815 | 18 | DistrictContactId | DistrictId, DistrictContactTypeId, SalutationId (+1) |
| Notifications | 720 | 7 | *None* | NotificationId, UserId, EmailBlastId |
| EmailBlastAddresses08132012 | 271 | 1 | *None* |  |
| SaxNotifications | 78 | 16 | *None* | CometId, UserId |
| DistrictContactTypes | 7 | 2 | DistrictContactTypeId |  |
| EmailBlastCopy | 3 | 17 | EmailBlastId |  |
| Messages | 0 | 4 | MessageId |  |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| EmailBlast | 16,701 | 2024-06-21 21:59:35.907000 |
| CSMessages | 11,621 | 2024-06-21 21:57:39.920000 |
| DistrictNotifications | 6,043 | 2024-06-21 21:59:10.690000 |
| DistrictContacts | 3,815 | 2024-06-21 21:59:09.850000 |
| Notifications | 720 | 2024-06-21 21:54:28.740000 |
| EmailBlastAddresses08132012 | 271 | 2021-11-08 21:28:49.073000 |
| SaxNotifications | 78 | 2021-11-08 21:29:55.657000 |
| DistrictContactTypes | 7 | 2024-06-21 21:59:10.013000 |
| EmailBlastCopy | 3 | 2021-11-08 21:28:49.097000 |
| Messages | 0 | 2024-06-21 22:32:28.687000 |
| UnsubscriptionEmail | 0 | 2024-08-01 03:14:55.203000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **User** (referenced by 3 tables)
- **District** (referenced by 2 tables)
- **Reference1** (referenced by 1 tables)
- **Reference2** (referenced by 1 tables)
- **Category** (referenced by 1 tables)

---

## Other {other}

Miscellaneous and utility tables

### Key Tables

| Table | Rows | Columns | Primary Key | Potential FKs |
|-------|------|---------|-------------|---------------|
| TaskSchedule | 1,544,400 | 15 | TaskScheduleId | ProjectTasksId, DistrictId, CategoryId (+3) |
| ScanEvents | 389,487 | 6 | ScanEventId | ScanJobId |
| PricingAddenda | 205,624 | 29 | PricingAddendaId | CrossRefId, CatalogId, HeadingId (+8) |
| Headings | 166,699 | 10 | HeadingId | CategoryId, DistrictId |
| SDSDocs | 161,387 | 12 | Id | ItemId, CrossRefId, MSDSId |
| CatList | 155,059 | 10 | *None* |  |
| SafetyDataSheets | 154,540 | 6 | SafetyDataSheetId |  |
| DistrictCategories | 125,118 | 16 | DistrictCategoryId | CategoryId, DistrictId, OrderBookTypeId |
| TaskEvent | 122,103 | 8 | TaskEventId | ProjectTaskId, DistrictId, CategoryId (+1) |
| SDSResults | 116,893 | 14 | SDSResultsId | SafetyDataSheetId |

### All Tables

<details>
<summary>Click to expand all tables</summary>

| Table | Rows | Modified |
|-------|------|----------|
| TaskSchedule | 1,544,400 | 2024-06-21 21:57:49.723000 |
| ScanEvents | 389,487 | 2024-06-21 22:36:09.003000 |
| PricingAddenda | 205,624 | 2025-05-15 05:14:46.313000 |
| Headings | 166,699 | 2025-02-01 08:05:25.357000 |
| SDSDocs | 161,387 | 2024-06-21 22:36:11.233000 |
| CatList | 155,059 | 2021-11-08 21:28:47.603000 |
| SafetyDataSheets | 154,540 | 2025-03-23 05:10:58.330000 |
| DistrictCategories | 125,118 | 2025-01-12 19:21:30.263000 |
| TaskEvent | 122,103 | 2024-06-21 22:39:20.327000 |
| SDSResults | 116,893 | 2025-05-02 13:47:54.090000 |
| TMSurveyResults | 89,650 | 2024-06-21 21:57:34.887000 |
| ResetPasswordTracking | 86,852 | 2025-06-25 07:50:36.310000 |
| PricingUpdate | 59,384 | 2024-06-21 22:33:50.790000 |
| MSDS | 58,726 | 2024-06-21 22:32:29.283000 |
| UNSPSCs | 50,317 | 2021-11-08 21:29:55.830000 |
| SearchSets | 43,911 | 2021-11-08 21:29:55.680000 |
| SaxDups | 31,171 | 2021-11-08 21:29:55.637000 |
| SDSSyncStatus | 26,483 | 2024-12-16 23:12:04.147000 |
| Keywords | 25,261 | 2024-06-21 22:32:26.780000 |
| NextNumber | 24,263 | 2025-04-16 02:54:31.280000 |
| CopyRequests | 23,572 | 2024-06-21 21:57:32.900000 |
| DistrictCharges | 22,477 | 2024-06-21 21:59:09.300000 |
| DistrictContinuances | 14,395 | 2024-06-21 21:59:10.237000 |
| Units | 11,218 | 2024-06-21 22:39:23.587000 |
| YearlyTotals | 10,161 | 2024-06-21 21:57:17.913000 |
| DistrictPP | 9,242 | 2024-06-21 22:41:21.153000 |
| Manufacturers | 9,007 | 2024-06-21 22:32:27.767000 |
| ShipLocations | 6,868 | 2024-06-21 22:39:14.830000 |
| School | 6,582 | 2024-06-21 22:41:22.077000 |
| IPQueue | 5,038 | 2024-06-21 22:03:11.750000 |
| TmpTaskSchedule | 4,884 | 2021-11-08 07:01:25.447000 |
| TopUOM | 4,579 | 2024-06-21 22:39:21.933000 |
| Suppression | 4,364 | 2024-08-10 03:07:42.990000 |
| RTK_2010NJHSL | 3,322 | 2021-11-08 21:29:55.617000 |
| RTK_FactSheets | 2,459 | 2024-06-21 22:35:02.810000 |
| CalendarDates | 2,261 | 2024-06-21 21:54:29.997000 |
| PPCategory | 1,457 | 2024-06-21 22:33:46.337000 |
| dchtest | 1,192 | 2021-11-08 06:55:55.540000 |
| District | 968 | 2025-10-08 12:40:34.070000 |
| ShippingCosts | 954 | 2024-06-21 21:35:32.707000 |
| TempIrvingtonWincap | 860 | 2024-06-21 22:39:20.483000 |
| RTK_Sites | 823 | 2024-06-21 22:35:13.220000 |
| TMSurvey | 796 | 2024-06-21 22:39:20.873000 |
| CalendarIB | 684 | 2024-06-21 21:54:30.760000 |
| RTK_Inventories | 658 | 2024-06-21 22:35:03.080000 |
| ShippingRequests | 635 | 2024-06-21 21:35:38.097000 |
| Calendars | 300 | 2024-06-21 21:54:31.700000 |
| Category | 134 | 2025-01-12 19:21:30.217000 |
| Trades | 107 | 2024-06-21 22:39:22.087000 |
| SDS_Rpt_Bridge | 99 | 2022-02-22 07:59:18.443000 |
| TMSurveyNewTrades | 89 | 2024-06-21 22:39:21.100000 |
| Counties | 78 | 2024-06-21 21:57:33.313000 |
| RTK_LegacyDistrictCodesMap | 78 | 2024-06-21 22:35:04.500000 |
| TM_UOM | 77 | 2024-06-21 22:39:20.720000 |
| DistrictNotes | 75 | 2024-06-21 21:59:10.483000 |
| SecurityRoleKeys | 65 | 2024-06-21 22:36:15.947000 |
| StatusTable | 53 | 2024-06-21 22:39:17.897000 |
| Sulphite | 49 | 2021-11-08 21:29:55.707000 |
| CSRep | 45 | 2024-06-21 21:57:40.263000 |
| dtproperties | 42 | 2001-08-27 16:22:54.930000 |
| InstructionBookContents | 31 | 2024-06-21 22:03:09.953000 |
| HolidayCalendar | 29 | 2024-02-06 15:19:21.127000 |
| RTK_ContainerCodes | 21 | 2024-06-21 22:35:02.230000 |
| Coops | 20 | 2024-06-21 21:57:28.827000 |
| Printers | 18 | 2025-11-26 20:55:58.167000 |
| Sections | 18 | 2024-06-21 22:36:15.470000 |
| CSCommands | 16 | 2024-06-21 21:57:38.540000 |
| ChargeTypes | 14 | 2026-01-06 15:57:06.727000 |
| ProjectTasks | 14 | 2024-06-21 22:33:53.837000 |
| SecurityKeys | 14 | 2024-06-21 22:36:15.773000 |
| Months | 12 | 2024-06-21 22:32:28.857000 |
| RTK_InventoryRangeCodes | 12 | 2024-06-21 22:35:03.227000 |
| ScheduledTask | 12 | 2024-12-10 22:48:48.540000 |
| RTK_MixtureCodes | 11 | 2024-06-21 22:35:05.523000 |
| ScannerZones | 10 | 2021-11-08 07:01:01.577000 |
| ScheduleTypes | 10 | 2024-06-21 22:36:10.853000 |
| RTK_HealthHazardCodes | 9 | 2024-06-21 22:35:02.943000 |
| sysdiagrams | 9 | 2021-11-08 07:01:22.873000 |
| Instructions | 7 | 2024-06-21 22:03:10.390000 |
| DistrictTypes | 6 | 2024-06-21 21:59:11.837000 |
| InstructionBookTypes | 6 | 2024-06-21 22:03:10.127000 |
| Salutations | 5 | 2024-06-21 22:35:14.137000 |
| SecurityRoles | 5 | 2024-06-21 22:36:16.167000 |
| BookTypes | 4 | 2024-06-21 21:54:29.557000 |
| Menus | 4 | 2024-06-21 22:32:28.447000 |
| RTK_UOMCodes | 3 | 2024-06-21 22:35:13.873000 |
| ScanJobs | 3 | 2021-11-08 07:01:01.550000 |
| States | 3 | 2024-06-21 22:39:17.680000 |
| CalendarTypes | 2 | 2024-06-21 21:54:31.960000 |
| CertificateAuthority | 1 | 2024-06-21 21:57:22.430000 |
| Control | 1 | 2024-06-21 21:57:27.870000 |
| AnswerTypes | 0 | 2024-06-21 21:31:01.317000 |
| CalDistricts | 0 | 2024-06-21 21:54:29.783000 |
| ContractTypes | 0 | 2021-11-08 21:28:47.630000 |
| CoverView | 0 | 2021-11-08 21:28:47.640000 |
| DistrictCategoryTitles | 0 | 2024-06-21 21:59:08.403000 |
| DistrictChargesNotes | 0 | 2024-06-21 21:59:09.463000 |
| Ledger | 0 | 2024-06-21 22:32:26.983000 |
| LL_RepArea | 0 | 2019-10-18 12:35:42.940000 |
| LL_RepLay | 0 | 2019-10-18 12:37:23.583000 |
| OBView | 0 | 2021-11-08 21:28:49.460000 |
| PricingMap | 0 | 2024-06-21 22:33:50.157000 |
| Rates | 0 | 2024-06-21 22:33:55.123000 |
| RateTypes | 0 | 2024-06-21 22:33:56.660000 |
| RateUnits | 0 | 2024-06-21 22:33:56.957000 |
| Receiving | 0 | 2024-06-21 22:33:57.067000 |
| Rights | 0 | 2024-06-21 22:35:00.920000 |
| RightsLink | 0 | 2024-06-21 22:35:01.773000 |
| RTK_Surveys | 0 | 2024-06-21 22:35:13.527000 |
| RTK_Training | 0 | 2024-06-21 22:35:13.687000 |
| SDSErrors | 0 | 2024-06-21 22:36:12.560000 |
| SDSs | 0 | 2024-06-21 22:36:14.817000 |
| SearchKeywords | 0 | 2024-06-21 22:36:15.370000 |
| Services | 0 | 2024-06-21 22:36:30.393000 |
| TableOfContents | 0 | 2024-06-21 22:39:18.417000 |
| TagSet_ | 0 | 2020-11-17 18:15:57.607000 |
| TransactionTypes | 0 | 2024-06-21 22:39:22.177000 |

</details>

### Common Relationships

Based on naming conventions, tables in this domain commonly reference:

- **District** (referenced by 27 tables)
- **Category** (referenced by 14 tables)
- **Item** (referenced by 8 tables)
- **User** (referenced by 6 tables)
- **School** (referenced by 6 tables)

---

## Cross-Domain Relationships

Key tables that are referenced across multiple domains:

| Table Pattern | Referenced By Domains |
|---------------|----------------------|
| DistrictId | Bidding, Communication, Documents, Finance & Budgets, Inventory & Items, Orders & Purchasing, Other, Users & Security, Vendors |
| CategoryId | Bidding, Communication, Inventory & Items, Orders & Purchasing, Other, Users & Security, Vendors |
| RequisitionId | Bidding, Inventory & Items, Orders & Purchasing, Other, Reporting, Users & Security |
| UserId | Bidding, Communication, Documents, Orders & Purchasing, Other, Users & Security |
| CatalogId | Bidding, Inventory & Items, Orders & Purchasing, Other, Users & Security, Vendors |
| VendorId | Bidding, Inventory & Items, Orders & Purchasing, Other, Users & Security, Vendors |
| DetailId | Bidding, Inventory & Items, Orders & Purchasing, Other, Reporting |
| CometId | Communication, Inventory & Items, Orders & Purchasing, Other, Users & Security |
| ItemId | Bidding, Inventory & Items, Orders & Purchasing, Other, Reporting |
| BidHeaderId | Bidding, Inventory & Items, Orders & Purchasing, Other, Vendors |
| PricePlanId | Bidding, Inventory & Items, Orders & Purchasing, Other, Vendors |
| SessionId | Bidding, Orders & Purchasing, Other, Reporting, Users & Security |
| ShippingId | Communication, Orders & Purchasing, Other, Users & Security, Vendors |
| UnitId | Bidding, Inventory & Items, Orders & Purchasing, Other |
| AwardId | Bidding, Inventory & Items, Orders & Purchasing, Other |
