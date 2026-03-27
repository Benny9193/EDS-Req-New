# Vendors

[Home](../../index.md) > [Business](../index.md) > [Entities](index.md) > Vendors

---

## Overview

Vendors are suppliers who provide goods and services to schools. EDS maintains vendor information, contracts, catalogs, and performance history.

---

## Vendor Lifecycle

```
Registration → Approval → Catalog Upload → Active → Performance Review
      │                         │              │
      │                         ▼              ▼
      │                    Bid Awards     Order History
      │                         │              │
      └────────────────────────►└──────────────┘
                                       │
                                       ▼
                              Renewal / Deactivation
```

---

## Key Tables

### Vendors Table

| Field | Description |
|-------|-------------|
| VendorId | Primary key |
| VendorName | Business name |
| VendorCode | Short identifier |
| Address, City, State, Zip | Primary address |
| Phone, Fax, Email | Contact info |
| TaxId | Federal tax ID |
| Active | Vendor status |
| MinimumOrder | Minimum order amount |

### VendorContacts Table

| Field | Description |
|-------|-------------|
| ContactId | Primary key |
| VendorId | Parent vendor |
| ContactName | Person name |
| Title | Job title |
| Email | Email address |
| Phone | Direct phone |
| IsPrimary | Primary contact flag |

---

## Vendor Categories

| Category | Description | Examples |
|----------|-------------|----------|
| Office Supplies | General supplies | Paper, pens, folders |
| Technology | IT equipment | Computers, software |
| Furniture | School furniture | Desks, chairs |
| Food Service | Cafeteria supplies | Food, equipment |
| Maintenance | Facility supplies | Cleaning, repairs |
| Curriculum | Educational materials | Books, workbooks |
| Athletic | Sports equipment | Uniforms, gear |

---

## Vendor Data Sync

### Vendor Sync Job
A scheduled job synchronizes vendor data between systems.

**Known Issue:** The sync job runs every hour, 24/7, even when unnecessary. See [KI-002: Vendor Sync Job](../../performance/known-issues/vendor-sync-job.md).

```sql
-- Sync job query pattern
SELECT v.VendorId, v.VendorName, v.VendorCode, ...
FROM Vendors v
LEFT JOIN VendorContacts vc ON v.VendorId = vc.VendorId
WHERE v.Modified > @LastSyncTime
```

---

## Vendor Performance

### Metrics Tracked

| Metric | Description |
|--------|-------------|
| Fill Rate | % of orders shipped complete |
| On-Time Delivery | % delivered by promised date |
| Return Rate | % of items returned |
| Price Compliance | % matching contracted price |
| Response Time | Average quote response time |

### Performance Scoring
Vendors are scored quarterly and annually:
- **A:** Excellent (90%+ on all metrics)
- **B:** Good (80-89%)
- **C:** Acceptable (70-79%)
- **D:** Needs Improvement (<70%)

---

## Vendor-Item Relationship

Vendors provide items through the **CrossRefs** table:

```
Vendor: Office Depot
    │
    └── CrossRefs (Catalog Items)
            ├── Item: Pencils #2 (SKU: 12345)
            ├── Item: Copy Paper (SKU: 67890)
            └── Item: Stapler (SKU: 11111)
```

### CrossRef Fields

| Field | Description |
|-------|-------------|
| CrossRefId | Primary key |
| VendorId | Vendor reference |
| ItemId | Internal item reference |
| VendorSKU | Vendor's product code |
| CatalogPrice | Current price |
| ContractPrice | Bid/contract price |
| UnitOfMeasure | Pack, Each, Box, etc. |

---

## Common Queries

### List Active Vendors
```sql
SELECT VendorId, VendorName, VendorCode,
       City, State, Phone, Email
FROM Vendors
WHERE Active = 1
ORDER BY VendorName
```

### Vendor with Item Count
```sql
SELECT v.VendorName, COUNT(cr.CrossRefId) as ItemCount
FROM Vendors v
LEFT JOIN CrossRefs cr ON v.VendorId = cr.VendorId
WHERE v.Active = 1
GROUP BY v.VendorId, v.VendorName
ORDER BY ItemCount DESC
```

### Find Vendor by Item
```sql
SELECT v.VendorName, cr.VendorSKU, cr.CatalogPrice
FROM CrossRefs cr
JOIN Vendors v ON cr.VendorId = v.VendorId
WHERE cr.ItemId = @ItemId
  AND v.Active = 1
ORDER BY cr.CatalogPrice
```

---

## Vendor Registration Process

### Steps
1. Vendor submits registration request
2. Purchasing reviews and approves
3. W-9 and insurance documents collected
4. Vendor account activated
5. Catalog data uploaded

### Required Documents

| Document | Purpose |
|----------|---------|
| W-9 | Tax identification |
| Certificate of Insurance | Liability coverage |
| Business License | Legal operation |
| References | Performance history |

---

## Cooperative Purchasing

Many districts use **cooperative purchasing agreements** to leverage buying power:

| Cooperative | Description |
|-------------|-------------|
| E&I Cooperative | National education cooperative |
| US Communities | Local government purchasing |
| State Contracts | State-negotiated contracts |
| Regional Co-ops | Multi-district agreements |

---

## See Also

- [Catalogs & Items](catalogs-items.md) - Product catalog
- [Bids & Awards](bids-awards.md) - Competitive bidding
- [Vendor Sync Job Issue](../../performance/known-issues/vendor-sync-job.md)
- [Schema: Vendors](../../schema/by-domain/vendors.md)

