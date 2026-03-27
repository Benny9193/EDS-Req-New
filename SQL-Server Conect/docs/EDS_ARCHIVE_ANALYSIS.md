# EDS Database - Archive Schema Analysis

Generated: 2026-01-09 09:49:29

This document analyzes the archive schema compared to the active dbo schema.

---

## Executive Summary

| Metric | dbo (Active) | archive | Ratio |
|--------|--------------|---------|-------|
| **Tables** | 382 | 51 | - |
| **Total Rows** | 1,236,300,093 | 129,549,402 | 10.5% |
| **Total Size (MB)** | 532,878 | 18,169 | 3.4% |
| **Total Size (GB)** | 520.4 | 17.7 | - |

### Key Findings

- **49** tables exist in both schemas (archived copies)
- **333** tables exist only in dbo (no archive)
- **2** tables exist only in archive (no active version)
- Archive schema holds **3%** of the data volume

---

## Tables in Both Schemas

These tables have both active (dbo) and archived copies.

| Table | dbo Rows | archive Rows | dbo Size (MB) | archive Size (MB) | Archive % |
|-------|----------|--------------|---------------|-------------------|----------|
| Detail | 30,841,298 | 25,480,018 | 19,418 | 7,578 | 83% |
| BidResults | 33,034,634 | 30,585,282 | 13,466 | 4,943 | 93% |
| PODetailItems | 24,327,506 | 22,905,929 | 2,585 | 2,090 | 94% |
| BidHeaderDetail | 123,789,710 | 26,252,593 | 7,976 | 1,146 | 21% |
| BatchDetail | 5,020,036 | 4,060,286 | 1,048 | 792 | 81% |
| Requisitions | 2,078,232 | 1,433,904 | 627 | 317 | 69% |
| BidRequestItems | 27,855,481 | 5,704,577 | 1,931 | 305 | 20% |
| RequisitionChangeLog | 1,938,491 | 1,936,897 | 332 | 297 | 100% |
| PO | 2,462,014 | 1,300,617 | 421 | 201 | 53% |
| Approvals | 7,824,818 | 3,517,361 | 485 | 185 | 45% |
| UserAccounts | 3,329,135 | 2,704,140 | 218 | 126 | 81% |
| Bids | 143,697 | 172,256 | 33 | 30 | 120% |
| VendorQuery | 11,553 | 4,057 | 119 | 30 | 35% |
| ApprovalsHistory | 332,112 | 447,389 | 22 | 24 | 135% |
| Awards | 135,686 | 143,977 | 20 | 18 | 106% |
| VendorQueryDetail | 130,112 | 39,321 | 24 | 8 | 30% |
| BidImports | 54,678 | 42,011 | 18 | 8 | 77% |
| VendorQueryTandM | 1,889 | 7 | 935 | 4 | 0% |
| TMAwards | 89,597 | 29,335 | 7 | 2 | 33% |
| BidMSRPResults | 40,980 | 10,848 | 7 | 1 | 26% |
| DMSBidDocuments | 29,032 | 0 | 10 | 1 | 0% |
| DetailMatch | 103,534 | 1,499 | 32 | 1 | 1% |
| Catalog | 3,897 | 2,422 | 3 | 1 | 62% |
| DMSVendorBidDocuments | 736,489 | 0 | 254 | 1 | 0% |
| BidHeaderDocument | 161,488 | 11,787 | 9 | 0 | 7% |
| BidTrades | 1,591 | 119 | 16 | 0 | 7% |
| VendorDocRequest | 14 | 0 | 1 | 0 | 0% |
| VendorQueryMSRP | 140 | 0 | 69 | 0 | 0% |
| VendorQueryMSRPDetail | 2 | 0 | 0 | 0 | 0% |
| BidHeaders | 9,548 | 3,395 | 8 | 0 | 36% |
| BidHeaderDocuments | 1 | 0 | 0 | 0 | 0% |
| BidHeaderCheckList | 110,423 | 4,521 | 10 | 0 | 4% |
| OrderBooks | 30,399 | 692 | 6 | 0 | 2% |
| BidMappedItems | 1,456,772 | 0 | 150 | 0 | 0% |
| BidReawards | 611 | 0 | 0 | 0 | 0% |
| BidRequestManufacturer | 104,823 | 0 | 6 | 0 | 0% |
| BidRequestOptions | 422,035 | 0 | 34 | 0 | 0% |
| BidRequestPriceRanges | 1,897,760 | 0 | 114 | 0 | 0% |
| DetailHold | 1 | 0 | 0 | 0 | 0% |
| FreezeItems | 15,435 | 0 | 2 | 0 | 0% |
| ItemContractPrices | 0 | 0 | 0 | 0 | 0% |
| POTempDetails | 4,014 | 0 | 0 | 0 | 0% |
| Prices | 0 | 0 | 0 | 0 | 0% |
| PricingConsolidatedOrderCounts | 401,387 | 0 | 11 | 0 | 0% |
| PricingMap | 0 | 0 | 0 | 0 | 0% |
| PricingUpdate | 59,384 | 0 | 4 | 0 | 0% |
| VendorDocRequestDetail | 52 | 0 | 0 | 0 | 0% |
| VendorQueryTandMDetail | 1,142 | 0 | 1 | 0 | 0% |
| allitems | 6,276,768 | 0 | 1,220 | 0 | 0% |

---

## Largest Archive Tables

Tables consuming the most archive storage.

| Table | Rows | Size (MB) | Size (GB) | % of Archive |
|-------|------|-----------|-----------|-------------|
| Detail | 25,480,018 | 7,578 | 7.40 | 41.7% |
| BidResults | 30,585,282 | 4,943 | 4.83 | 27.2% |
| PODetailItems | 22,905,929 | 2,090 | 2.04 | 11.5% |
| BidHeaderDetail | 26,252,593 | 1,146 | 1.12 | 6.3% |
| BatchDetail | 4,060,286 | 792 | 0.77 | 4.4% |
| Requisitions | 1,433,904 | 317 | 0.31 | 1.7% |
| BidRequestItems | 5,704,577 | 305 | 0.30 | 1.7% |
| RequisitionChangeLog | 1,936,897 | 297 | 0.29 | 1.6% |
| PO | 1,300,617 | 201 | 0.20 | 1.1% |
| Approvals | 3,517,361 | 185 | 0.18 | 1.0% |
| UserAccounts | 2,704,140 | 126 | 0.12 | 0.7% |
| UserAccountsUserAccountId_CrossMapping | 2,704,140 | 44 | 0.04 | 0.2% |
| Bids | 172,256 | 30 | 0.03 | 0.2% |
| VendorQuery | 4,057 | 30 | 0.03 | 0.2% |
| ApprovalsHistory | 447,389 | 24 | 0.02 | 0.1% |
| Awards | 143,977 | 18 | 0.02 | 0.1% |
| cxmlSession | 50,022 | 13 | 0.01 | 0.1% |
| VendorQueryDetail | 39,321 | 8 | 0.01 | 0.0% |
| BidImports | 42,011 | 8 | 0.01 | 0.0% |
| VendorQueryTandM | 7 | 4 | 0.00 | 0.0% |

---

## Tables Without Archive (dbo only)

These tables exist only in dbo with no archived copy.

### Large Tables (>10K rows) Without Archive

| Table | Rows | Size (MB) | Consider Archiving? |
|-------|------|-----------|--------------------|
| OrderBookDetailOld | 187,630,151 | 3,454 | Yes |
| CrossRefs | 150,631,265 | 111,809 | Yes |
| BidHeaderDetail_Orig | 102,658,927 | 6,095 | Yes |
| TransactionLog_HISTORY | 99,019,937 | 177,658 | Yes |
| BidResults_Orig | 55,592,743 | 10,120 | Yes |
| ReportSessionLinks | 51,989,978 | 2,282 | Yes |
| OrderBookDetail | 37,804,007 | 4,248 | Yes |
| TransactionLogCF | 33,662,338 | 119,431 | Yes |
| Items | 30,153,920 | 8,112 | Yes |
| BidItems | 26,906,489 | 3,994 | Yes |
| DetailChanges | 26,502,061 | 1,956 | Yes |
| BidRequestItems_Orig | 25,521,585 | 1,758 | Yes |
| DebugMsgs | 20,840,159 | 7,368 | Yes |
| BidResultChanges | 18,229,521 | 1,334 | Yes |
| CatalogTextParts | 17,179,537 | 1,048 | Yes |
| BidItems_Old | 16,238,384 | 2,271 | Yes |
| SessionTable | 12,395,179 | 1,956 | Yes |
| ReportSession | 5,282,298 | 394 | Yes |
| DebugMsgs_Orig | 5,211,696 | 1,830 | Yes |
| BidMgrTagFile | 4,335,799 | 288 | Yes |
| DetailChangeLog | 2,924,942 | 338 | Yes |
| DetailNotifications | 2,779,169 | 301 | Yes |
| Audit | 2,568,656 | 172 | Yes |
| ImageLog | 1,788,706 | 2,160 | Yes |
| Images | 1,736,177 | 972 | Yes |
| TaskSchedule | 1,544,400 | 191 | Yes |
| VendorUploads | 1,533,264 | 214 | Yes |
| EmailBlastLog | 1,437,241 | 3,802 | Yes |
| BudgetAccounts | 1,399,984 | 84 | Maybe |
| BidProductLinePrices | 1,323,391 | 72 | Maybe |

*Total dbo-only tables: 333*

---

## Orphaned Archive Tables

These tables exist only in archive with no active dbo version.
Consider whether these can be dropped or if the dbo table was renamed.

| Table | Rows | Size (MB) | Created | Modified |
|-------|------|-----------|---------|----------|
| UserAccountsUserAccountId_CrossMapping | 2,704,140 | 44 | 2022-12-16 23:40:45.687000 | 2022-12-16 23:40:45.687000 |
| cxmlSession | 50,022 | 13 | 2022-12-16 23:40:40.747000 | 2022-12-16 23:40:40.747000 |

---

## Recommendations

### Storage Optimization

**Large archive tables (>1 GB) to review:**

- `archive.Detail` - 7.4 GB, 25,480,018 rows
- `archive.BidResults` - 4.8 GB, 30,585,282 rows
- `archive.PODetailItems` - 2.0 GB, 22,905,929 rows
- `archive.BidHeaderDetail` - 1.1 GB, 26,252,593 rows

### Archive Strategy

**Tables that should be considered for archiving:**

- `dbo.OrderBookDetailOld` - 3,454 MB, 187,630,151 rows
- `dbo.CrossRefs` - 111,809 MB, 150,631,265 rows
- `dbo.BidHeaderDetail_Orig` - 6,095 MB, 102,658,927 rows
- `dbo.TransactionLog_HISTORY` - 177,658 MB, 99,019,937 rows
- `dbo.BidResults_Orig` - 10,120 MB, 55,592,743 rows

### Data Retention

Consider implementing:

1. **Retention Policy**: Define how long archived data should be kept
2. **Purge Schedule**: Regular cleanup of old archive data
3. **Compression**: Enable page/row compression on archive tables
4. **Partitioning**: Consider partitioning large tables by date
