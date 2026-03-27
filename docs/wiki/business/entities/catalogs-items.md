# Catalogs & Items

[Home](../../index.md) > [Business](../index.md) > [Entities](index.md) > Catalogs & Items

---

## Overview

The catalog system manages products available for purchase. Items are the internal product definitions, while CrossRefs link items to vendor-specific catalog entries with pricing.

---

## Catalog Structure

```
Items (Internal Product Master)
    │
    ├── ItemId: 1001
    │   Name: "Copy Paper, White, 8.5x11, 500 sheets"
    │   Category: Office Supplies
    │       │
    │       └── CrossRefs (Vendor Catalog Links)
    │               │
    │               ├── Vendor: Staples
    │               │   SKU: STP-12345
    │               │   Price: $42.99
    │               │
    │               └── Vendor: Office Depot
    │                   SKU: OD-67890
    │                   Price: $43.50
    │
    └── ItemId: 1002
        Name: "Pencils #2, Yellow, 12/pkg"
        ...
```

---

## Key Tables

### Items Table (Internal Master)

| Field | Description |
|-------|-------------|
| ItemId | Primary key |
| ItemCode | Internal item number |
| Description | Item name |
| Category | Classification |
| UnitOfMeasure | Default UOM |
| Active | Is available |
| ContractRequired | Must use awarded vendor |

### CrossRefs Table (Vendor Catalog)

| Field | Description |
|-------|-------------|
| CrossRefId | Primary key |
| ItemId | Internal item link |
| VendorId | Supplier |
| VendorSKU | Vendor's product code |
| VendorDescription | Vendor's description |
| CatalogPrice | List price |
| ContractPrice | Awarded price |
| UnitOfMeasure | Vendor's UOM |
| PackSize | Quantity per pack |
| PerishableItem | Is perishable |
| PrescriptionRequired | Requires Rx |
| DigitallyDelivered | Electronic delivery |
| MinimumOrderQuantity | Min order qty |

---

## CrossRef Blocking Issue

The CrossRef table is frequently accessed but can become blocked during bulk operations.

### Known Issue: KI-004
Simple CrossRef lookups can be blocked for extended periods (12+ hours accumulated) during bulk Detail table operations.

See [KI-004: CrossRef Blocking](../../performance/known-issues/crossref-blocking.md).

### Typical Lookup Query
```sql
SELECT CrossRefId,
       COALESCE(PerishableItem, 0) as PerishableItem,
       COALESCE(PrescriptionRequired, 0) as PrescriptionRequired,
       COALESCE(DigitallyDelivered, 0) as DigitallyDelivered,
       COALESCE(MinimumOrderQuantity, 0) as MinimumOrderQuantity
FROM CrossRefs
WHERE CrossRefId = @P0
```

---

## Item Categories

### Standard Categories

| Category | Description |
|----------|-------------|
| Office Supplies | Paper, pens, folders |
| Technology | Computers, software, peripherals |
| Furniture | Desks, chairs, storage |
| Curriculum | Textbooks, workbooks |
| Art Supplies | Paints, paper, materials |
| Science | Lab equipment, chemicals |
| Sports/PE | Equipment, uniforms |
| Maintenance | Cleaning, repairs |
| Food Service | Cafeteria supplies |
| Special Ed | Adaptive equipment |

### Category Hierarchy

```
Office Supplies
    ├── Paper Products
    │       ├── Copy Paper
    │       ├── Specialty Paper
    │       └── Notebooks
    ├── Writing Instruments
    │       ├── Pens
    │       ├── Pencils
    │       └── Markers
    └── Filing
            ├── Folders
            └── Binders
```

---

## Catalog Management

### Catalog Upload Process
1. Vendor provides catalog file (CSV/Excel)
2. System maps to standard categories
3. Items matched to existing or created new
4. Prices updated in CrossRefs
5. Availability set

### Price Updates
- **Catalog Price:** List price, updated by vendor
- **Contract Price:** Award price, locked during contract
- **Promotional Price:** Temporary discounts

### UOM Conversion
Different vendors may use different units:

| Item | Vendor A | Vendor B |
|------|----------|----------|
| Paper | Case (10 reams) | Ream |
| Pens | Box (12) | Each |
| Folders | Pack (100) | Pack (25) |

System handles conversions for price comparison.

---

## Common Queries

### Search Items by Description
```sql
SELECT i.ItemId, i.ItemCode, i.Description,
       i.Category, i.UnitOfMeasure
FROM Items i
WHERE i.Description LIKE '%' + @SearchTerm + '%'
  AND i.Active = 1
ORDER BY i.Description
```

### Item with Vendor Prices
```sql
SELECT i.Description, v.VendorName,
       cr.VendorSKU, cr.CatalogPrice, cr.ContractPrice
FROM Items i
JOIN CrossRefs cr ON i.ItemId = cr.ItemId
JOIN Vendors v ON cr.VendorId = v.VendorId
WHERE i.ItemId = @ItemId
ORDER BY COALESCE(cr.ContractPrice, cr.CatalogPrice)
```

### Lowest Price by Item
```sql
SELECT i.ItemId, i.Description,
       MIN(COALESCE(cr.ContractPrice, cr.CatalogPrice)) as BestPrice,
       COUNT(DISTINCT cr.VendorId) as VendorCount
FROM Items i
JOIN CrossRefs cr ON i.ItemId = cr.ItemId
JOIN Vendors v ON cr.VendorId = v.VendorId
WHERE v.Active = 1
GROUP BY i.ItemId, i.Description
```

### Items Needing Reorder
```sql
SELECT i.ItemCode, i.Description,
       inv.QuantityOnHand, inv.ReorderPoint,
       inv.ReorderQuantity
FROM Items i
JOIN Inventory inv ON i.ItemId = inv.ItemId
WHERE inv.QuantityOnHand <= inv.ReorderPoint
ORDER BY i.Description
```

---

## Punch-Out Catalogs

Some vendors provide **punch-out** catalogs where users shop directly on vendor's website:

1. User clicks "Shop at [Vendor]" in EDS
2. Redirected to vendor's site (authenticated)
3. User selects items, adds to cart
4. Cart contents returned to EDS requisition
5. Items appear as requisition lines

### Punch-Out Vendors
Common punch-out integrations:
- Amazon Business
- Staples
- Office Depot
- Dell
- CDW

---

## Catalog Triggers

### trig_CrossRefs
Fires on CrossRef changes to:
- Update item pricing
- Log price changes
- Sync to related tables

This trigger can cause blocking during catalog imports.

---

## Performance Recommendations

### For CrossRef Lookups
1. Use NOLOCK hint for display queries
2. Add covering index for common lookups
3. Cache frequently accessed items

### Index Recommendation
```sql
CREATE INDEX IX_CrossRefs_Lookup
ON CrossRefs (CrossRefId)
INCLUDE (PerishableItem, PrescriptionRequired,
         DigitallyDelivered, MinimumOrderQuantity)
```

---

## See Also

- [Vendors](vendors.md) - Supplier information
- [Requisitions](requisitions.md) - Using catalog items
- [CrossRef Blocking Issue](../../performance/known-issues/crossref-blocking.md)
- [Schema: Inventory & Catalog](../../schema/by-domain/inventory-catalog.md)

