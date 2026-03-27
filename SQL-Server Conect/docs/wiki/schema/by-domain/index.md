# Schema by Domain

[Home](../../index.md) > [Schema](../index.md) > By Domain

---

## Overview

The EDS database contains **438 tables** organized into functional domains. This section provides domain-specific schema documentation.

---

## Domain Summary

| Domain | Tables | Description | Documentation |
|--------|--------|-------------|---------------|
| [Bidding](bidding.md) | 76 | Competitive procurement | Bids, Awards, Contracts |
| [Orders & Purchasing](orders-purchasing.md) | 45 | Requisitions and POs | Req, Detail, PO tables |
| [Vendors](vendors.md) | 32 | Supplier management | Vendor, Contact tables |
| [Inventory & Catalog](inventory-catalog.md) | 28 | Products and pricing | Items, CrossRefs |
| [Users & Security](users-security.md) | 24 | Authentication/authorization | Users, Roles, Permissions |
| [Finance & Budgets](finance-budgets.md) | 18 | Budget management | Budgets, Accounts |
| [Documents](documents.md) | 15 | File attachments | Documents, Attachments |

---

## Table Distribution

```
Bidding        ████████████████████████████████████ 76 (17%)
Orders         ██████████████████████ 45 (10%)
Vendors        ████████████████ 32 (7%)
Inventory      ██████████████ 28 (6%)
Users          ████████████ 24 (5%)
Finance        █████████ 18 (4%)
Documents      ███████ 15 (3%)
Other/System   ████████████████████████████████████████████████ 200 (48%)
```

---

## Key Relationships

### Cross-Domain Relationships

```
Users ──────────┬──────────► Requisitions ──────► Detail ──────► PO
                │                   │                 │
                │                   ▼                 ▼
Schools ────────┘               Budgets          CrossRefs
                                                     │
                                                     ▼
                                                 Vendors
                                                     │
                                                     ▼
                                              Bids/Awards
```

---

## Naming Conventions

### Table Names
- Singular nouns preferred (User, not Users) - though EDS uses plural
- Descriptive prefixes for domain (Bid*, PO*, etc.)
- Join tables: EntityA_EntityB or EntityAEntityB

### Column Names
| Pattern | Meaning | Example |
|---------|---------|---------|
| *Id | Primary/Foreign Key | RequisitionId |
| Is* | Boolean flag | IsActive |
| Date* | Date/time | DateCreated |
| *Code | Short identifier | AccountCode |
| *Name | Display name | VendorName |

---

## Common Patterns

### Soft Delete
Many tables use Active flag instead of DELETE:
```sql
-- Preferred: Soft delete
UPDATE Entity SET Active = 0 WHERE Id = @Id

-- Actual delete only for logs/temp data
```

### Audit Columns
Standard audit columns:
| Column | Purpose |
|--------|---------|
| CreatedBy | User who created |
| CreatedDate | Creation timestamp |
| ModifiedBy | Last modifier |
| ModifiedDate | Last change time |

### Status Pattern
Status as string or FK to status table:
```sql
-- String status
Status VARCHAR(50)  -- 'Draft', 'Submitted', etc.

-- FK to status table
StatusId INT FOREIGN KEY REFERENCES Statuses(StatusId)
```

---

## Index Strategy

### Primary Keys
- All tables have clustered PK on Id column
- Usually IDENTITY(1,1)

### Foreign Keys
- Most FKs have non-clustered index
- Composite FKs where needed

### Covering Indexes
Recommended for high-volume queries:
```sql
CREATE INDEX IX_Table_Covering
ON Table (FilterColumn)
INCLUDE (SelectColumn1, SelectColumn2)
```

---

## See Also

- [Schema Overview](../index.md) - Summary statistics
- [Stored Procedures](../stored-procedures.md) - SP documentation
- [Views](../views.md) - View documentation
- [Triggers](../triggers.md) - Trigger documentation

