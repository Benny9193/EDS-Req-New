# EDS Database - Executive Summary

Generated: 2026-01-09 12:05:00

---

## Database Overview

| Property | Value |
|----------|-------|
| Database Name | EDS |
| Owner | repl |
| Created | 2023-02-25 23:10:10.290000 |
| Collation | SQL_Latin1_General_CP1_CI_AS |
| Data Size | 1,222,486.4 MB |
| Log Size | 53,403.8 MB |

---

## Object Inventory

| Object Type | Count |
|-------------|-------|
| Tables | 439 |
| Table Columns | 4,638 |
| Views | 475 |
| View Columns | 6,847 |
| Stored Procedures | 396 |
| SP Parameters | 1,308 |
| Functions | 231 |
| Triggers | 59 |
| Indexes | 1,115 |
| Foreign Keys | 31 |
| Check Constraints | 1 |
| Default Constraints | 133 |

---

## Documentation Coverage

| Object Type | Documented | Total | Coverage |
|-------------|------------|-------|----------|
| Tables | 439 | 439 | 100.0% |
| Table Columns | 4,638 | 4,638 | 100.0% |
| Views | 475 | 475 | 100.0% |
| View Columns | 6,847 | 6,847 | 100.0% |
| Stored Procedures | 396 | 396 | 100.0% |
| SP Parameters | 1,308 | 1,308 | 100.0% |
| **TOTAL** | **14,103** | **14,103** | **100.0%** |

---

## Schema Breakdown

| Schema | Tables | Views | Procedures |
|--------|--------|-------|------------|
| archive | 51 | 0 | 0 |
| dbo | 382 | 460 | 375 |
| EDSIQEndUser | 0 | 1 | 0 |
| EDSIQWebUser | 3 | 11 | 19 |
| EDSWebRpts | 2 | 0 | 0 |
| utility | 0 | 0 | 1 |
| VMS | 0 | 2 | 0 |

---

## Largest Tables (Top 20)

| Schema | Table | Rows | Size (MB) |
|--------|-------|------|----------|
| dbo | OrderBookDetailOld | 187,630,151 | 3,446.95 |
| dbo | CrossRefs | 150,631,340 | 111,821.64 |
| dbo | BidHeaderDetail | 123,789,710 | 7,973.59 |
| dbo | BidHeaderDetail_Orig | 102,658,927 | 6,095.11 |
| dbo | TransactionLog_HISTORY | 99,019,937 | 173,804.37 |
| dbo | BidResults_Orig | 55,592,743 | 10,119.73 |
| dbo | ReportSessionLinks | 51,991,267 | 2,280.69 |
| dbo | OrderBookDetail | 37,804,007 | 4,212.03 |
| dbo | TransactionLogCF | 33,704,754 | 119,610.20 |
| dbo | BidResults | 33,034,634 | 13,462.04 |
| dbo | Detail | 30,842,313 | 19,390.42 |
| archive | BidResults | 30,585,282 | 4,942.67 |
| dbo | Items | 30,153,956 | 8,107.64 |
| dbo | BidRequestItems | 27,855,481 | 1,929.58 |
| dbo | BidItems | 26,906,489 | 3,989.91 |
| dbo | DetailChanges | 26,502,061 | 1,955.76 |
| archive | BidHeaderDetail | 26,252,593 | 1,145.89 |
| dbo | BidRequestItems_Orig | 25,521,585 | 1,757.88 |
| archive | Detail | 25,480,018 | 7,578.16 |
| dbo | PODetailItems | 24,327,549 | 2,580.59 |

---

## Key Metrics

- **Average columns per table:** 10.6
- **Average parameters per stored procedure:** 3.3
- **Views to tables ratio:** 1.08:1
- **Indexes per table:** 2.5
- **Foreign keys per table:** 0.07

---

## Documentation Files

- `EDS_TABLES.md` - Complete table documentation
- `EDS_VIEWS.md` - View documentation
- `EDS_STORED_PROCEDURES.md` - Stored procedure documentation
- `EDS_INDEXES.md` - Index documentation
- `EDS_ERD.md` - Entity relationship diagram
