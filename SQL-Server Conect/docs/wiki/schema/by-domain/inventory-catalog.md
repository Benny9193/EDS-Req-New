# Schema: Inventory & Catalog Domain

[Home](../../index.md) > [Schema](../index.md) > [By Domain](index.md) > Inventory & Catalog

---

## Overview

The inventory domain contains 28 tables managing product catalogs, vendor items, pricing, and inventory tracking.

---

## Table Count: 28

### Core Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| Items | Internal product master | ItemId, ItemCode, Description, Category |
| CrossRefs | Vendor catalog items | CrossRefId, ItemId, VendorId, VendorSKU, Price |
| Categories | Item categories | CategoryId, CategoryName, ParentId |
| UnitOfMeasures | UOM definitions | UOMId, UOMCode, Description |

### Inventory Tables

| Table | Purpose |
|-------|---------|
| Inventory | Stock levels |
| InventoryLocations | Warehouse locations |
| InventoryTransactions | Movement history |
| ReorderPoints | Auto-reorder settings |

### Pricing Tables

| Table | Purpose |
|-------|---------|
| PriceHistory | Historical prices |
| PromotionalPrices | Temporary discounts |
| ContractPrices | Award-linked prices |

---

## Key Relationships

```
Items (1) ──────► (N) CrossRefs ──────► (1) Vendors
     │                   │
     │                   └──────► (N) Detail (requisition lines)
     │
     ├──────► (1) Categories
     │
     └──────► (N) Inventory ──────► (1) InventoryLocations
```

---

## Critical Table: CrossRefs

The CrossRefs table links internal items to vendor-specific catalog entries.

### Schema
| Column | Type | Description |
|--------|------|-------------|
| CrossRefId | INT | Primary key |
| ItemId | INT | Internal item FK |
| VendorId | INT | Vendor FK |
| VendorSKU | VARCHAR(50) | Vendor's product code |
| VendorDescription | VARCHAR(500) | Vendor's description |
| CatalogPrice | DECIMAL | List price |
| ContractPrice | DECIMAL | Award price (if applicable) |
| UnitOfMeasure | VARCHAR(20) | Vendor's UOM |
| PackSize | INT | Qty per pack |
| PerishableItem | BIT | Is perishable |
| PrescriptionRequired | BIT | Requires Rx |
| DigitallyDelivered | BIT | Electronic delivery |
| MinimumOrderQuantity | INT | Min order qty |
| Active | BIT | Is available |
| Created | DATETIME | Create date |
| Modified | DATETIME | Last modified |

### Performance Impact

CrossRef lookups are frequently blocked during bulk operations:

```sql
-- Simple lookup that can be blocked
SELECT CrossRefId,
       COALESCE(PerishableItem, 0) as PerishableItem,
       COALESCE(PrescriptionRequired, 0) as PrescriptionRequired,
       COALESCE(DigitallyDelivered, 0) as DigitallyDelivered,
       COALESCE(MinimumOrderQuantity, 0) as MinimumOrderQuantity
FROM CrossRefs
WHERE CrossRefId = @P0
```

**Known Issue:** This query was blocked for 737 minutes on Jan 6, 2026. See [KI-004](../../performance/known-issues/crossref-blocking.md).

---

## Critical Table: Items

### Schema
| Column | Type | Description |
|--------|------|-------------|
| ItemId | INT | Primary key |
| ItemCode | VARCHAR(50) | Internal item number |
| Description | VARCHAR(500) | Item name |
| CategoryId | INT | Category FK |
| UOMId | INT | Default UOM FK |
| ManufacturerId | INT | Manufacturer FK |
| ManufacturerPartNo | VARCHAR(50) | MFG part number |
| ContractRequired | BIT | Must use awarded vendor |
| Active | BIT | Is available |
| Created | DATETIME | Create date |
| Modified | DATETIME | Last modified |

---

## Common Queries

### Search Items
```sql
SELECT i.ItemId, i.ItemCode, i.Description,
       c.CategoryName, i.Active
FROM Items i
LEFT JOIN Categories c ON i.CategoryId = c.CategoryId
WHERE i.Description LIKE '%' + @SearchTerm + '%'
   OR i.ItemCode LIKE '%' + @SearchTerm + '%'
ORDER BY i.Description
```

### Item with Vendor Prices
```sql
SELECT i.ItemCode, i.Description,
       v.VendorName, cr.VendorSKU,
       cr.CatalogPrice, cr.ContractPrice,
       COALESCE(cr.ContractPrice, cr.CatalogPrice) as EffectivePrice
FROM Items i
JOIN CrossRefs cr ON i.ItemId = cr.ItemId
JOIN Vendors v ON cr.VendorId = v.VendorId
WHERE i.ItemId = @ItemId
  AND cr.Active = 1
ORDER BY EffectivePrice
```

### Lowest Price by Item
```sql
SELECT i.ItemId, i.Description,
       MIN(COALESCE(cr.ContractPrice, cr.CatalogPrice)) as BestPrice,
       COUNT(DISTINCT cr.VendorId) as VendorCount
FROM Items i
JOIN CrossRefs cr ON i.ItemId = cr.ItemId
JOIN Vendors v ON cr.VendorId = v.VendorId
WHERE i.Active = 1
  AND cr.Active = 1
  AND v.Active = 1
GROUP BY i.ItemId, i.Description
HAVING COUNT(DISTINCT cr.VendorId) > 0
```

### Items Needing Reorder
```sql
SELECT i.ItemCode, i.Description,
       inv.QuantityOnHand, rp.ReorderPoint,
       rp.ReorderQuantity,
       v.VendorName as PreferredVendor
FROM Items i
JOIN Inventory inv ON i.ItemId = inv.ItemId
JOIN ReorderPoints rp ON i.ItemId = rp.ItemId
LEFT JOIN Vendors v ON rp.PreferredVendorId = v.VendorId
WHERE inv.QuantityOnHand <= rp.ReorderPoint
ORDER BY (inv.QuantityOnHand * 1.0 / NULLIF(rp.ReorderPoint, 0))
```

---

## Index Recommendations

### CrossRefs Table
```sql
-- For lookup queries (most critical)
CREATE INDEX IX_CrossRefs_Lookup
ON CrossRefs (CrossRefId)
INCLUDE (PerishableItem, PrescriptionRequired,
         DigitallyDelivered, MinimumOrderQuantity)

-- For item-based queries
CREATE INDEX IX_CrossRefs_ItemId
ON CrossRefs (ItemId)
INCLUDE (VendorId, VendorSKU, CatalogPrice, ContractPrice, Active)

-- For vendor catalog queries
CREATE INDEX IX_CrossRefs_VendorId
ON CrossRefs (VendorId)
INCLUDE (ItemId, VendorSKU, Active)
```

### Items Table
```sql
-- For description searches
CREATE INDEX IX_Items_Description
ON Items (Description)
INCLUDE (ItemCode, CategoryId, Active)

-- For code lookups
CREATE UNIQUE INDEX IX_Items_Code
ON Items (ItemCode)
```

---

## Catalog Management

### Catalog Upload Process
1. Vendor provides catalog file (CSV/Excel)
2. System validates format
3. Items matched or created
4. CrossRefs created/updated
5. Prices set

### Price Update Patterns

| Pattern | Description |
|---------|-------------|
| Full Catalog | Replace all vendor prices |
| Delta Update | Only changed items |
| Contract Update | Award prices only |
| Promotional | Temporary discounts |

---

## Triggers

### trig_CrossRefs
Fires on CrossRef changes:
- Logs price changes
- Updates related records
- Can cause blocking during catalog imports

### trig_Items
Fires on Item changes:
- Audit logging
- Category sync

---

## Performance Considerations

### High-Impact Operations
| Operation | Impact | Mitigation |
|-----------|--------|------------|
| Catalog import | Many CrossRef inserts | Batch in groups |
| Price lookup | Blocked by triggers | Use NOLOCK for display |
| Full catalog refresh | Table locks | Off-hours only |

### Known Issues
- [KI-004: CrossRef Blocking](../../performance/known-issues/crossref-blocking.md) - Lookup blocking

---

## See Also

- [Business: Catalogs & Items](../../business/entities/catalogs-items.md)
- [Vendors](vendors.md) - Vendor management
- [CrossRef Blocking Issue](../../performance/known-issues/crossref-blocking.md)

