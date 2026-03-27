# Database Inventory

> **Last updated**: 2026-03-27 (infrastructure audit)
>
> The SQL Server instance (`eds-sqlserver.eastus2.cloudapp.azure.com`) hosts **22 user databases** plus 4 system databases.
> CLAUDE.md documents EDS and dpa_EDSAdmin. This file covers the full inventory.

## Server Details

| Property | Value |
|----------|-------|
| Edition | SQL Server 2017 Developer Edition (64-bit) |
| Version | 14.0.3520.4 (RTM-CU31-GDR, Feb 2026 patch) |
| OS | Windows Server 2022 Datacenter (Hypervisor) |
| Machine Name | SQL-Server |

---

## Production / Business Databases

| Database | Size | Tables | Views | Procs | Purpose |
|----------|------|--------|-------|-------|---------|
| **EDS** | 1.48 TB | 439 | 475 | 396 | Primary production database — products, vendors, categories, users, sessions, requisitions, orders, bids |
| **dpa_EDSAdmin** | ~50 GB | 207 | — | — | SolarWinds DPA monitoring — performance metrics, blocking events, wait stats |
| **Catalogs** | 224 GB | 25 | 0 | 45 | Production catalog data |
| **VendorBids** | 109 GB | 41 | 23 | 72 | Vendor bidding system (EDSIQ connects to this) |
| **SearchData** | 92 GB | 9 | 0 | 1 | Search index data |
| **ContentCentral** | 56 GB | 134 | 7 | 0 | Content/document management |
| **WorkTables** | 31 GB | 264 | 0 | 0 | Work/staging data |
| **Documents** | 6.8 GB | 39 | 15 | 12 | Document storage |
| **NJ_RTK** | 256 MB | 9 | 6 | 3 | NJ Right to Know data |
| **ProcurementAnalytics** | 144 MB | 13 | 0 | 0 | New analytics DB (created 2026-03-13) |
| **IDIQ_Platform** | 80 MB | 0 | 0 | 0 | IDIQ platform (empty, created 2026-02-26) |
| **IDIQ_Platform_UAT** | 144 MB | 98 | 0 | 0 | IDIQ UAT environment (created 2026-02-26) |

---

## Test / Dev Databases

| Database | Size | Notes |
|----------|------|-------|
| **EDS_Test** | 1.22 TB | Full test copy of EDS |
| **EDS_TEST_Old** | 1.12 TB | Older test copy — candidate for cleanup |
| **VendorBids_TEST** | 99 GB | VendorBids test copy |
| **SearchData_Test** | 92 GB | SearchData test copy |
| **test** | 80 MB | Empty test database |
| **work** | 16 MB | Single-table workspace |
| **DeletedPOs** | 16 MB | Deleted PO archive |

---

## Infrastructure Databases

| Database | Size | Notes |
|----------|------|-------|
| **SolarWindsOrion** | 346 MB | SolarWinds monitoring agent data |
| **hMailServer** | 16 MB | Mail system |
| **hMailServerNew** | 16 MB | Updated mail system |

---

## Total Disk Usage

| Category | Count | Size |
|----------|-------|------|
| Production/Business | 12 | ~2.0 TB |
| Test/Dev | 7 | ~2.5 TB |
| Infrastructure | 3 | ~378 MB |
| **Total** | **22** | **~4.5 TB** |

> **Note**: Test databases (EDS_Test, EDS_TEST_Old, VendorBids_TEST, SearchData_Test) account for ~2.5 TB. Consider whether EDS_TEST_Old is still needed.

---

## Cross-Database Connections

| Source | Target DB | Connection Type |
|--------|-----------|-----------------|
| EDSIQ (ColdFusion app) | EDS | Primary data |
| EDSIQ (ColdFusion app) | VendorBids | Bidding operations |
| EDSIQ (ColdFusion app) | Documents | Document management |
| Universal Requisition API | EDS | Product catalog, requisitions |
| DPA monitoring agent | dpa_EDSAdmin | Performance data collection |
| SolarWinds agent | SolarWindsOrion | Infrastructure monitoring |
