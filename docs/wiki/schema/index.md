# Schema Reference

[Home](../index.md) > Schema

---

## Database Overview

The EDS database is a large SQL Server 2017 database containing all procurement data for K-12 school districts.

---

## Quick Statistics

| Object Type | Count | Notes |
|-------------|-------|-------|
| **Tables** | 439 | Including archive tables |
| **Columns** | 4,638 | Across all tables |
| **Views** | 475 | Reporting and application views |
| **Stored Procedures** | 396 | Business logic |
| **Triggers** | 52 | Data integrity and cascades |
| **Indexes** | 815+ | Performance optimization |
| **Functions** | 231 | Scalar and table-valued |
| **Foreign Keys** | 31 | Explicit relationships |

---

## Tables by Business Domain

| Domain | Tables | Key Tables | Description |
|--------|--------|------------|-------------|
| [Bidding](by-domain/bidding.md) | 76 | BidHeaders, Bids, Awards | Competitive bidding |
| [Orders & Purchasing](by-domain/orders-purchasing.md) | 45 | Requisitions, Detail, PO | Purchase workflow |
| [Vendors](by-domain/vendors.md) | 32 | Vendors, VendorContacts | Vendor management |
| [Inventory & Catalog](by-domain/inventory-catalog.md) | 28 | Items, Catalog, CrossRefs | Product catalog |
| [Users & Security](by-domain/users-security.md) | 24 | Users, School, District | User management |
| [Finance & Budgets](by-domain/finance-budgets.md) | 18 | Budgets, Accounts | Budget tracking |
| [Documents](by-domain/documents.md) | 15 | Various doc tables | Document management |

---

## Largest Tables (by row count)

| Table | Rows | Description |
|-------|------|-------------|
| Detail | 30.8M | Requisition line items |
| CrossRefs | 20M+ | Item cross-references |
| Requisitions | 2.08M | Purchase requests |
| Approvals | 7.8M | Approval records |
| Items | 1.5M+ | Product catalog |
| PO | 1M+ | Purchase orders |

---

## Key Schema Objects

### Critical Stored Procedures
| Procedure | Purpose | Notes |
|-----------|---------|-------|
| sp_CreateNewRequisition | Create requisition | Entry point |
| sp_SubmitRequisition | Submit for approval | Workflow |
| sp_ApproveReq | Process approval | Workflow |
| sp_ConvertReqs | Convert to PO | Workflow |
| usp_GetIndexData | Bid pricing lookup | Performance issue |

### Critical Triggers
| Trigger | Table | Impact |
|---------|-------|--------|
| trig_DetailUpdate | Detail | High - causes blocking |
| trig_CrossRefs | CrossRefs | Medium |
| trig_RequisitionsUpdate | Requisitions | Medium |

### Critical Views
| View | Purpose |
|------|---------|
| vw_ReqDetail | Requisition details |
| vw_ExistingRequisitions | Active requisitions |
| vw_VendorsTable | Vendor lookup |

---

## Schema Documentation

### Detailed References
- [Stored Procedures](stored-procedures.md) - All 396 procedures
- [Views](views.md) - All 475 views
- [Triggers](triggers.md) - 59 triggers with impact analysis
- [Indexes](indexes.md) - Index recommendations

### Full Documentation
> **Complete Reference:** See [EDS_DATA_DICTIONARY.md](../../EDS_DATA_DICTIONARY.md) for full table/column details

---

## Entity Relationships

### Primary Relationships
```
District (1) ──── (*) School ──── (*) Users
    │                                  │
    └──────── (*) Budgets ────── (*) Requisitions
                                       │
                                  (*) Detail ──── Items
                                       │
                                  (*) PO ──── Vendors
```

### Bidding Relationships
```
BidHeaders (1) ──── (*) Bids ──── Vendors
     │                  │
     └──── (*) BidItems │
                        │
              (*) Awards ────── Items
```

> **Full ERD:** See [EDS_ERD.md](../../EDS_ERD.md) for complete diagrams

---

## Related Documentation

- [Business Entities](../business/entities/index.md) - Business context
- [Performance](../performance/index.md) - Performance issues
- [Troubleshooting](../troubleshooting/index.md) - Common problems
