# EDS Database Schema Guide

Comprehensive guide to the EDS (Enterprise Data System) SQL Server database schema.

---

## Overview

The EDS database is a large SQL Server 2017 database supporting K-12 school district procurement operations.

### Quick Statistics

| Object Type | Count | Description |
|-------------|-------|-------------|
| **Tables** | 438 | Data storage (including 50+ archive tables) |
| **Columns** | 4,638 | Across all tables |
| **Views** | 474 | Reporting and application views |
| **Stored Procedures** | 395 | Business logic implementation |
| **Triggers** | 52 | Data integrity and cascades |
| **Indexes** | 815+ | Performance optimization |
| **Functions** | 231 | Scalar and table-valued |
| **Foreign Keys** | 31 | Explicit relationships |

### Database Size

| Metric | Value |
|--------|-------|
| Total Size | ~1.2 TB |
| Largest Table | CrossRefs (150M+ rows) |
| Transaction Tables | 30M+ rows |
| Active Records | ~50M across core tables |

---

## Schema Diagrams

### Core Entity Relationships

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                            ORGANIZATIONAL HIERARCHY                          │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│   District (3.5K) ────┬──── School (12.9K) ────── Users (28.6K)            │
│         │             │                              │                      │
│         │             └──── Budgets ─────────────────┤                      │
│         │                                            │                      │
│         └──── Vendors (18.9K) ◄──────────────────────┘                      │
│                   │                                                         │
└───────────────────┼─────────────────────────────────────────────────────────┘
                    │
┌───────────────────┼─────────────────────────────────────────────────────────┐
│                   │           PRODUCT CATALOG                                │
├───────────────────┼─────────────────────────────────────────────────────────┤
│                   │                                                         │
│                   ▼                                                         │
│   Catalog ───── CrossRefs (150M) ───── Items (30M) ───── Category (12.9K)  │
│     │                │                     │                                │
│     │                │                     └──── Manufacturers              │
│     │                └──── Images                                           │
│     │                                                                       │
│     └──── Pricing                                                           │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                    │
┌───────────────────┼─────────────────────────────────────────────────────────┐
│                   │           PROCUREMENT WORKFLOW                           │
├───────────────────┼─────────────────────────────────────────────────────────┤
│                   ▼                                                         │
│                                                                             │
│   Requisitions (2.1M) ───── Detail (30.8M) ───── Items                     │
│         │                        │                                          │
│         │                        └──── CrossRefs (pricing lookup)           │
│         │                                                                   │
│         ▼                                                                   │
│   Approvals (7.8M) ───── PendingApprovals                                  │
│         │                                                                   │
│         ▼                                                                   │
│   PO (2.5M) ───── PODetailItems (24M) ───── Vendors                        │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
                    │
┌───────────────────┼─────────────────────────────────────────────────────────┐
│                   │           COMPETITIVE BIDDING                            │
├───────────────────┼─────────────────────────────────────────────────────────┤
│                   ▼                                                         │
│                                                                             │
│   BidHeaders ───── BidHeaderDetail (123M) ───── Detail                     │
│       │                                                                     │
│       ├──── BidRequestItems (27M) ───── Items                              │
│       │                                                                     │
│       ├──── Bids ───── Vendors                                             │
│       │         │                                                           │
│       │         └──── BidResults (33M)                                     │
│       │                                                                     │
│       └──── Awards ───── Items + Vendors                                   │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Procurement Data Flow

```
User creates order request
         │
         ▼
┌─────────────────┐
│  Requisitions   │ ◄──── School, Budget, User references
└────────┬────────┘
         │ (1:N)
         ▼
┌─────────────────┐
│     Detail      │ ◄──── Items, CrossRefs (pricing)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Approvals     │ ◄──── Approval workflow (multi-level)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│       PO        │ ◄──── Vendor, converted from requisition
└────────┬────────┘
         │ (1:N)
         ▼
┌─────────────────┐
│  PODetailItems  │ ◄──── Line items sent to vendor
└─────────────────┘
```

---

## Tables by Business Domain

### Procurement (45 tables)

Core tables for the requisition-to-purchase-order workflow.

| Table | Rows | Purpose |
|-------|------|---------|
| **Requisitions** | 2.1M | Purchase requests from users |
| **Detail** | 30.8M | Line items on requisitions |
| **PO** | 2.5M | Purchase orders sent to vendors |
| **PODetailItems** | 24.3M | PO line items |
| **Approvals** | 7.8M | Approval history |
| **PendingApprovals** | 567K | Awaiting approval |

**Key Relationships:**
- Requisitions → Detail (1:N)
- Requisitions → PO (1:1 after conversion)
- Detail → Items (N:1)
- PO → Vendor (N:1)

**See:** [Orders & Purchasing Domain](wiki/schema/by-domain/orders-purchasing.md)

---

### Product Catalog (28 tables)

Product master data and vendor cross-references.

| Table | Rows | Purpose |
|-------|------|---------|
| **Items** | 30.1M | Master product catalog |
| **CrossRefs** | 150.6M | Vendor-item mappings |
| **Category** | 12.9K | Product categories |
| **Catalog** | 2.6K | Vendor catalogs |
| **Images** | 1.7M | Product images |

**Key Relationships:**
- Items → CrossRefs (1:N per vendor)
- Items → Category (N:1)
- CrossRefs → Catalog (N:1)
- CrossRefs → Images (N:1)

**See:** [Inventory & Catalog Domain](wiki/schema/by-domain/inventory-catalog.md)

---

### Vendors (32 tables)

Vendor management and contacts.

| Table | Rows | Purpose |
|-------|------|---------|
| **Vendors** | 18.9K | Vendor master |
| **VendorContacts** | 25K | Vendor contact people |
| **VendorUploads** | 1.5M | Catalog upload history |
| **VendorShipCodes** | 5K | Shipping methods |

**Key Relationships:**
- Vendors → Catalog (1:N)
- Vendors → VendorContacts (1:N)
- Vendors → PO (1:N)

**See:** [Vendors Domain](wiki/schema/by-domain/vendors.md)

---

### Competitive Bidding (76 tables)

RFP/RFQ management and bid evaluation.

| Table | Rows | Purpose |
|-------|------|---------|
| **BidHeaders** | 8.4K | Bid solicitations |
| **BidHeaderDetail** | 123.8M | Items in bids |
| **BidRequestItems** | 27.9M | Items requested in RFPs |
| **Bids** | 185K | Vendor bid submissions |
| **BidResults** | 33M | Bid response details |
| **Awards** | 450K | Award decisions |

**Key Relationships:**
- BidHeaders → BidHeaderDetail (1:N)
- BidHeaders → Bids (1:N per vendor)
- Bids → BidResults (1:N)
- Awards → Items + Vendors

**See:** [Bidding Domain](wiki/schema/by-domain/bidding.md)

---

### Users & Security (24 tables)

User accounts, schools, and districts.

| Table | Rows | Purpose |
|-------|------|---------|
| **District** | 3.5K | School districts |
| **School** | 12.9K | Individual schools |
| **Users** | 28.6K | User accounts |
| **UserAccounts** | 3.3M | Account details |
| **UserRoles** | 50K | Role assignments |

**Key Relationships:**
- District → School (1:N)
- School → Users (1:N)
- Users → Requisitions (1:N)

**See:** [Users & Security Domain](wiki/schema/by-domain/users-security.md)

---

### Finance & Budgets (18 tables)

Budget tracking and accounting.

| Table | Rows | Purpose |
|-------|------|---------|
| **Budgets** | 250K | Budget definitions |
| **BudgetAccounts** | 1.4M | Account balances |
| **Accounts** | 500K | Chart of accounts |

**Key Relationships:**
- District → Budgets (1:N)
- Budgets → BudgetAccounts (1:N)
- Requisitions → Budgets (N:1)

**See:** [Finance & Budgets Domain](wiki/schema/by-domain/finance-budgets.md)

---

## Critical Tables Reference

### Tier 1 - Highest Impact (13 tables)

These tables are critical for core operations and contain the most data.

| Table | Rows | Description |
|-------|------|-------------|
| CrossRefs | 150.6M | Item-vendor mappings |
| BidHeaderDetail | 123.8M | Bid line items |
| Items | 30.1M | Product catalog |
| Detail | 30.8M | Requisition line items |
| BidRequestItems | 27.9M | Bid specifications |
| PODetailItems | 24.3M | PO line items |
| Approvals | 7.8M | Approval records |
| Requisitions | 2.1M | Purchase requests |
| PO | 2.5M | Purchase orders |
| Vendors | 18.9K | Vendor master |
| Category | 12.9K | Product categories |
| School | 12.9K | Schools |
| District | 3.5K | Districts |

**Full Documentation:** [Tier 1 Tables](tables/TIER1_TABLES.md)

---

## Common Query Patterns

### Find Products by Category

```sql
SELECT i.ItemId, i.Description, c.CategoryName, cr.CatalogPrice
FROM Items i
JOIN Category c ON i.CategoryId = c.CategoryId
LEFT JOIN CrossRefs cr ON i.ItemId = cr.ItemId AND cr.Active = 1
WHERE c.CategoryName LIKE '%Writing%'
ORDER BY i.Description;
```

### Get Vendor Pricing for an Item

```sql
SELECT
    v.Name AS VendorName,
    cr.VendorItemCode,
    cr.CatalogPrice,
    cr.GrossPrice
FROM CrossRefs cr
JOIN Catalog cat ON cr.CatalogId = cat.CatalogId
JOIN Vendors v ON cat.VendorId = v.VendorId
WHERE cr.ItemId = @ItemId
  AND cr.Active = 1
ORDER BY cr.CatalogPrice;
```

### Requisition with Line Items

```sql
SELECT
    r.RequisitionId,
    r.DateCreated,
    u.UserName,
    d.DetailId,
    i.Description,
    d.Quantity,
    d.UnitPrice,
    d.ExtendedPrice
FROM Requisitions r
JOIN Users u ON r.UserId = u.UserId
JOIN Detail d ON r.RequisitionId = d.RequisitionId
JOIN Items i ON d.ItemId = i.ItemId
WHERE r.RequisitionId = @RequisitionId;
```

### Pending Approvals by Approver

```sql
SELECT
    pa.SysId,
    r.RequisitionId,
    r.DateCreated,
    u.UserName AS Requestor,
    SUM(d.ExtendedPrice) AS TotalAmount
FROM PendingApprovals pa
JOIN Requisitions r ON pa.RequisitionId = r.RequisitionId
JOIN Users u ON r.UserId = u.UserId
JOIN Detail d ON r.RequisitionId = d.RequisitionId
WHERE pa.ApproverId = @ApproverId
GROUP BY pa.SysId, r.RequisitionId, r.DateCreated, u.UserName;
```

---

## Naming Conventions

### Tables

| Pattern | Example | Description |
|---------|---------|-------------|
| Singular noun | `Vendor` | Entity tables |
| Plural noun | `Approvals` | Transaction/history tables |
| `archive.` prefix | `archive.Detail` | Archived data |
| `vw_` prefix | `vw_ReqDetail` | Views (older convention) |

### Columns

| Pattern | Example | Description |
|---------|---------|-------------|
| `{Table}Id` | `VendorId` | Primary key |
| `{Related}Id` | `CategoryId` | Foreign key |
| `Date{Action}` | `DateCreated` | Timestamps |
| `Is{State}` | `IsActive` | Boolean flags |
| `{Entity}Name` | `VendorName` | Display names |

### Known Inconsistencies

- `Manufacturor` (typo, kept for compatibility)
- Mixed use of `Active` (bit) vs `IsActive`
- Some PKs don't follow `{Table}Id` pattern

---

## Archive Schema

The `archive` schema contains historical data moved from production tables.

| Archive Table | Source | Purpose |
|---------------|--------|---------|
| `archive.Detail` | `dbo.Detail` | Old order lines |
| `archive.Approvals` | `dbo.Approvals` | Old approvals |
| `archive.BidResults` | `dbo.BidResults` | Old bid data |

**Note:** Archive tables often lack primary keys and indexes for storage efficiency.

**See:** [Archive Analysis](EDS_ARCHIVE_ANALYSIS.md)

---

## Performance Considerations

### High-Volume Tables

| Table | Volume | Impact |
|-------|--------|--------|
| CrossRefs | 150M+ | Core lookups - ensure indexed |
| BidHeaderDetail | 123M+ | Bid queries can be slow |
| Detail | 30M+ | Requisition line items |

### Critical Indexes

| Table | Index | Purpose |
|-------|-------|---------|
| CrossRefs | `IX_CrossRefs_ItemId` | Product lookup |
| Detail | `IX_Detail_RequisitionId` | Order detail fetch |
| Items | `IX_Items_CategoryId` | Category filtering |

**See:** [Index Documentation](EDS_INDEXES.md)

### Known Performance Issues

| Issue | Table(s) | Mitigation |
|-------|----------|------------|
| Blocking on updates | Detail, CrossRefs | Use NOLOCK where safe |
| Slow bid lookups | BidHeaderDetail | Add filtered indexes |
| Large scans | Items | Use category filters |

**See:** [Troubleshooting - Slow Queries](wiki/troubleshooting/slow-queries.md)

---

## Related Documentation

### Detailed References

| Document | Description |
|----------|-------------|
| [EDS_DATA_DICTIONARY.md](EDS_DATA_DICTIONARY.md) | Complete table/column reference (1.3MB) |
| [EDS_ERD.md](EDS_ERD.md) | Entity relationship diagrams |
| [EDS_DATA_DICTIONARY.xlsx](EDS_DATA_DICTIONARY.xlsx) | Excel version |
| [Tier 1 Tables](tables/TIER1_TABLES.md) | Critical tables with business context |

### By Domain

| Domain | Document |
|--------|----------|
| Bidding | [wiki/schema/by-domain/bidding.md](wiki/schema/by-domain/bidding.md) |
| Orders | [wiki/schema/by-domain/orders-purchasing.md](wiki/schema/by-domain/orders-purchasing.md) |
| Vendors | [wiki/schema/by-domain/vendors.md](wiki/schema/by-domain/vendors.md) |
| Inventory | [wiki/schema/by-domain/inventory-catalog.md](wiki/schema/by-domain/inventory-catalog.md) |
| Users | [wiki/schema/by-domain/users-security.md](wiki/schema/by-domain/users-security.md) |
| Finance | [wiki/schema/by-domain/finance-budgets.md](wiki/schema/by-domain/finance-budgets.md) |

### Other Resources

| Document | Description |
|----------|-------------|
| [EDS_STORED_PROCEDURES.md](EDS_STORED_PROCEDURES.md) | Stored procedure documentation |
| [EDS_VIEWS.md](EDS_VIEWS.md) | View documentation |
| [EDS_TRIGGERS.md](EDS_TRIGGERS.md) | Trigger documentation |
| [EDS_INDEXES.md](EDS_INDEXES.md) | Index documentation |
| [EDS_BUSINESS_DOMAINS.md](EDS_BUSINESS_DOMAINS.md) | Business domain analysis |

---

## Generating Documentation

The schema documentation can be regenerated using the provided scripts:

```bash
# Generate full data dictionary
python scripts/generate_data_dictionary.py

# Generate ERD documentation
python scripts/generate_erd.py

# Refresh all documentation
python scripts/refresh_documentation.py
```

**See:** [Scripts README](../scripts/README.md) for all documentation scripts.
