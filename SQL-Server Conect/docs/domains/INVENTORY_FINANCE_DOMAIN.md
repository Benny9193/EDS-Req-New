# EDS Database - Inventory, Finance & System Domain

Generated: 2026-01-15

This document provides comprehensive documentation for the remaining domains: Inventory & Catalog, Finance & Budgets, and System Configuration.

**Total Tables:** ~40 | **Total Rows:** ~260 million

---

## Table of Contents

1. [Inventory & Catalog Domain](#inventory--catalog-domain)
2. [Finance & Budget Domain](#finance--budget-domain)
3. [System & Configuration Domain](#system--configuration-domain)
4. [Reporting Domain](#reporting-domain)

---

## Inventory & Catalog Domain

This domain manages the product catalog, vendor cross-references, pricing, and item classifications.

**Total Rows:** ~199 million

### Core Catalog Tables

#### CrossRefs

**Rows:** ~150,632,769 | **Purpose:** Vendor item cross-references

The largest table in the entire database. Links EDS standard items to vendor-specific product codes and pricing.

| Column | Type | Description |
|--------|------|-------------|
| CrossRefId | int PK | Unique cross-reference ID |
| ItemId | int FK | EDS standard item |
| CatalogId | int FK | Vendor catalog |
| VendorItemCode | varchar | Vendor's SKU |
| CatalogPrice | money | Vendor's price |
| GrossPrice | money | Before discounts |
| ImageURL | varchar | Product image |
| ManufacturerId | int FK | Manufacturer |
| UPC_ISBN | varchar | Universal product code |
| Active | tinyint | 1=Current |

**Key Relationships:**
- References: Items, Catalog, Manufacturers
- Used by: Detail (for pricing), BidItems

---

#### Items

**Rows:** ~30,154,516 | **Purpose:** Master product catalog

The standardized product master - independent of vendors.

| Column | Type | Description |
|--------|------|-------------|
| ItemId | int PK | Unique item ID |
| ItemCode | varchar | EDS item code |
| Description | varchar | Product name |
| CategoryId | int FK | Product category |
| UnitId | int FK | Unit of measure |
| HeadingId | int FK | Catalog heading |
| ListPrice | money | Default price |
| RTK | tinyint | Hazmat flag |
| Active | tinyint | 1=Available |

---

#### Catalog

**Rows:** ~6,322 | **Purpose:** Vendor catalog definitions

Represents vendor product catalogs with effective dates.

| Column | Type | Description |
|--------|------|-------------|
| CatalogId | int PK | Unique catalog ID |
| VendorId | int FK | Owning vendor |
| Name | varchar | Catalog name |
| EffectiveDate | datetime | Valid from |
| ExpirationDate | datetime | Valid until |
| Active | tinyint | 1=Current |

---

#### Category

**Rows:** 134 | **Purpose:** Product category hierarchy

Top-level product classifications.

| Column | Type | Description |
|--------|------|-------------|
| CategoryId | int PK | Unique category ID |
| CategoryNumber | varchar | Category code |
| Name | varchar | Category name |
| Code | varchar | Short code |
| Active | tinyint | 1=Active |

---

### Classification Tables

#### Headings

**Rows:** ~166,699 | **Purpose:** Catalog section headings

Organizes items within categories.

---

#### Keywords

**Rows:** ~25,261 | **Purpose:** Search keywords

Keywords for product search.

---

#### Manufacturers

**Rows:** ~9,007 | **Purpose:** Product manufacturers

Manufacturer master list.

| Column | Type | Description |
|--------|------|-------------|
| ManufacturerId | int PK | Unique ID |
| Name | varchar | Manufacturer name |
| Code | varchar | Short code |
| Active | tinyint | 1=Active |

---

#### ManufacturerProductLines

**Rows:** ~14,298 | **Purpose:** Product line definitions

Product lines within manufacturers.

---

#### Units

**Rows:** ~11,229 | **Purpose:** Units of measure

Standard units (Each, Box, Case, etc.).

| Column | Type | Description |
|--------|------|-------------|
| UnitId | int PK | Unique unit ID |
| Code | varchar | Unit code (EA, BX, CS) |
| Active | tinyint | 1=Active |

---

### Pricing Tables

#### PricePlans

**Rows:** 584 | **Purpose:** Pricing plan definitions

Different pricing structures.

---

#### PriceRanges

**Rows:** ~120,619 | **Purpose:** Quantity price breaks

Volume discount tiers.

---

#### PricingAddenda

**Rows:** ~206,078 | **Purpose:** Price adjustments

Add-on pricing modifications.

---

#### PricingUpdate

**Rows:** ~59,390 | **Purpose:** Price change records

Price update history.

---

#### PricingConsolidatedOrderCounts

**Rows:** ~401,387 | **Purpose:** Order volume for pricing

Volume data for pricing decisions.

---

### Catalog Content Tables

#### CatalogText

**Rows:** ~112,799 | **Purpose:** Extended product descriptions

Detailed product text.

---

#### CatalogTextParts

**Rows:** ~17,179,537 | **Purpose:** Text segments

Segmented text for large descriptions.

---

#### CatalogImportFields

**Rows:** 15 | **Purpose:** Import field mapping

Field definitions for catalog imports.

---

#### ItemUpdates

**Rows:** ~198,886 | **Purpose:** Item change tracking

History of item modifications.

---

### Inventory Domain Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         INVENTORY & CATALOG STRUCTURE                        │
└─────────────────────────────────────────────────────────────────────────────┘

                         ┌──────────────┐
                         │   Category   │
                         └──────────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
              ┌──────────┐          ┌──────────┐
              │ Headings │          │   Items  │◄────────────┐
              └──────────┘          └──────────┘             │
                    │                     │                  │
                    │              ┌──────┴──────┐           │
                    │              ▼             ▼           │
                    │        ┌──────────┐  ┌──────────┐      │
                    │        │CrossRefs │  │ Keywords │      │
                    │        └──────────┘  └──────────┘      │
                    │              │                         │
                    │              ▼                         │
                    │        ┌──────────┐                    │
                    │        │ Catalog  │                    │
                    │        └──────────┘                    │
                    │              │                         │
                    │              ▼                         │
                    │        ┌──────────┐                    │
                    └───────►│ Vendors  │────────────────────┘
                             └──────────┘
```

---

## Finance & Budget Domain

This domain manages budget accounts, funding allocations, and financial tracking.

**Total Rows:** ~1.5 million

### Budget Tables

#### Budgets

**Rows:** ~16,381 | **Purpose:** Budget period definitions

Fiscal year budget definitions per district.

| Column | Type | Description |
|--------|------|-------------|
| BudgetId | int PK | Unique budget ID |
| DistrictId | int FK | Owning district |
| FiscalYear | int | Budget year |
| Name | varchar | Budget name |
| StartDate | datetime | Period start |
| EndDate | datetime | Period end |
| Active | tinyint | 1=Current |

---

#### BudgetAccounts

**Rows:** ~1,402,229 | **Purpose:** Budget line items

Individual budget allocations within a budget period.

| Column | Type | Description |
|--------|------|-------------|
| BudgetAccountId | int PK | Unique account ID |
| BudgetId | int FK | Parent budget |
| AccountId | int FK | Chart of accounts |
| BudgetAmount | money | Allocated amount |
| AmountAvailable | money | Remaining balance |
| Active | tinyint | 1=Active |

**Key Relationships:**
- Parent: Budgets
- References: Accounts
- Used by: UserAccounts, Requisitions

---

#### Accounts

**Rows:** ~108,773 | **Purpose:** Chart of accounts

Account code definitions.

| Column | Type | Description |
|--------|------|-------------|
| AccountId | int PK | Unique account ID |
| AccountCode | varchar | Account code |
| Description | varchar | Account name |
| Active | tinyint | 1=Active |

---

### Accounting Integration

#### AccountingFormats

**Rows:** 49 | **Purpose:** Export format definitions

Formats for accounting system exports.

---

#### AccountingUserFields

**Rows:** 80 | **Purpose:** Custom field mappings

User-defined field configurations.

---

### Billing Tables

#### ChargeTypes

**Rows:** 14 | **Purpose:** Charge type definitions

Types of charges billed to districts.

| ChargeTypeId | Description |
|--------------|-------------|
| 1 | Annual EDSIQ Licence |
| 2 | Annual EDSIQ Licence with Right to Know |
| 3 | Right to Know |
| 4 | Accounting System Interface |
| 5 | Training |
| 6 | Time and Materials |
| 7 | Generic PO's |
| 8 | e-PO Module |

---

### Budget Flow

```
District creates Budget (fiscal year)
        │
        ▼
BudgetAccounts created (line items)
        │
        ▼
UserAccounts link users to BudgetAccounts
        │
        ▼
User creates Requisition against BudgetAccount
        │
        ▼
AmountAvailable reduced (encumbrance)
        │
        ▼
PO created ──► Actual spending recorded
```

---

## System & Configuration Domain

This domain manages system settings, logging, and communications.

### Email & Communication

#### EmailBlast

**Rows:** ~16,750 | **Purpose:** Email campaign definitions

Mass email configurations.

| Column | Type | Description |
|--------|------|-------------|
| EmailBlastId | int PK | Unique blast ID |
| Subject | varchar | Email subject |
| Body | text | Email content |
| SendDate | datetime | When sent |
| Status | varchar | Delivery status |

---

#### EmailBlastLog

**Rows:** ~1,441,683 | **Purpose:** Email delivery log

Individual email delivery records.

---

### System Logging

*(Various logging tables exist in the archive schema for historical data)*

---

## Reporting Domain

This domain manages report generation and session tracking.

### ReportSession

**Rows:** ~5,288,858 | **Purpose:** Report generation sessions

Tracks report generation requests.

| Column | Type | Description |
|--------|------|-------------|
| ReportSessionId | int PK | Unique session ID |
| UserId | int FK | Requesting user |
| ReportType | varchar | Type of report |
| GeneratedDate | datetime | When generated |
| Status | varchar | Completion status |

---

### ReportSessionLinks

**Rows:** ~52,007,161 | **Purpose:** Report data links

Links report sessions to source data records.

**Note:** This is the second largest table in the database. Consider archiving old report sessions.

---

## Domain Summary

| Domain | Tables | Rows | Key Tables |
|--------|--------|------|------------|
| Inventory & Catalog | 20 | ~199M | CrossRefs, Items, Catalog |
| Finance & Budget | 6 | ~1.5M | BudgetAccounts, Accounts |
| System & Config | 5 | ~1.5M | EmailBlast, EmailBlastLog |
| Reporting | 2 | ~57M | ReportSession, ReportSessionLinks |

---

## Cross-Domain Relationships

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CROSS-DOMAIN FLOW                                    │
└─────────────────────────────────────────────────────────────────────────────┘

INVENTORY                    ORDERS                      FINANCE
┌──────────┐               ┌──────────┐               ┌──────────┐
│  Items   │──────────────►│  Detail  │◄──────────────│ Budget   │
└──────────┘               └──────────┘               │ Accounts │
     │                          │                     └──────────┘
     ▼                          │                          ▲
┌──────────┐                    │                          │
│CrossRefs │                    │                          │
└──────────┘                    │                          │
     │                          ▼                          │
     ▼                    ┌──────────┐                     │
┌──────────┐              │Requisition│─────────────────────┘
│ Catalog  │              └──────────┘
└──────────┘                    │
     │                          ▼
     ▼                    ┌──────────┐
┌──────────┐              │    PO    │
│ Vendors  │◄─────────────┴──────────┘
└──────────┘

USERS & SECURITY ────────► SessionTable ────────► REPORTING
                                                 ┌──────────┐
                                                 │ Report   │
                                                 │ Session  │
                                                 └──────────┘
```

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial Inventory/Finance/System documentation | Phase 2 Documentation |
