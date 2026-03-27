# EDS Database - Tier 1 Tables (Enhanced Documentation)

Generated: 2026-01-15

This document provides enhanced business context documentation for the 25 most critical tables in the EDS database, identified by row count and business impact.

---

## Table of Contents

1. [CrossRefs (150.6M rows)](#1-crossrefs)
2. [Items (30.1M rows)](#2-items)
3. [Detail (30.8M rows)](#3-detail)
4. [Requisitions (2.1M rows)](#4-requisitions)
5. [Vendors (18.9K rows)](#5-vendors)
6. [Category (12.9K rows)](#6-category)
7. [District (3.5K rows)](#7-district)
8. [School (12.9K rows)](#8-school)
9. [Users (28.6K rows)](#9-users)
10. [PO (Purchase Orders)](#10-po)
11. [Awards](#11-awards)
12. [BidHeaders](#12-bidheaders)
13. [Catalogs](#13-catalogs)

---

## 1. CrossRefs

**Schema:** `dbo` | **Rows:** 150,631,334 | **Domain:** Inventory & Items

### Purpose

The CrossRefs table is the central item mapping hub that links internal EDS item codes to vendor-specific product codes, enabling multi-vendor pricing and catalog management across the entire procurement system.

### Business Context

CrossRefs serves as the translation layer between EDS's standardized product catalog (Items) and vendor-specific catalogs. When a school orders a product, the system uses CrossRefs to:
1. Find which vendors carry that item
2. Retrieve vendor-specific pricing
3. Obtain vendor's product code for ordering
4. Access product images and detailed descriptions

This is the largest table in the database because every product can have multiple vendor cross-references (one item might be available from 5+ vendors, each with their own code and price).

### Usage

- **Ordering System:** Maps Items to vendor-specific codes when generating purchase orders
- **Catalog Display:** Provides images, descriptions, and pricing for product browsing
- **Price Comparison:** Enables comparison shopping across multiple vendors
- **Bid Processing:** Links bid responses to standard items for evaluation

### Key Relationships

```
Parent Tables (CrossRefs references):
├── Items (ItemId) - The standardized product
├── Catalog (CatalogId) - Which vendor catalog this cross-ref belongs to
├── Manufacturers (ManufacturerId) - Product manufacturer
└── Images (ImageId) - Product image

Used By:
├── Detail - Order line items use CrossRefs for pricing
├── BidItems - Bid submissions reference CrossRefs
└── DistrictItems - District-specific item configurations
```

### Critical Columns

| Column | Business Purpose |
|--------|------------------|
| ItemId | Links to standardized EDS item |
| VendorItemCode | Vendor's product SKU/code |
| CatalogId | Which vendor catalog |
| CatalogPrice | Current catalog price from vendor |
| GrossPrice | Price before any discounts |
| ImageURL | Product image for display |
| ManufacturorPartNumber | Manufacturer's part number |
| UPC_ISBN | Universal product code |
| Active | Whether this cross-ref is currently valid |

### Common Query Patterns

```sql
-- Get all vendors for an item with pricing
SELECT cr.VendorItemCode, cr.CatalogPrice, c.VendorId, v.Name as VendorName
FROM CrossRefs cr
JOIN Catalog c ON cr.CatalogId = c.CatalogId
JOIN Vendors v ON c.VendorId = v.VendorId
WHERE cr.ItemId = @ItemId AND cr.Active = 1;

-- Find cross-ref by vendor item code
SELECT cr.*, i.Description
FROM CrossRefs cr
JOIN Items i ON cr.ItemId = i.ItemId
WHERE cr.VendorItemCode = @VendorCode AND cr.Active = 1;
```

### Data Quality Notes

- The `Manufacturor` column has a historical typo (should be "Manufacturer") - preserved for backwards compatibility
- Many cross-refs exist for discontinued products (Active=0) - these should not be purged as they're needed for historical order references
- Image URLs may be external (vendor-hosted) or internal - always validate before display

---

## 2. Items

**Schema:** `dbo` | **Rows:** 30,153,953 | **Domain:** Inventory & Items

### Purpose

The Items table is the master product catalog containing all standardized products available for ordering through the EDS system.

### Business Context

Items represents EDS's standardized product master, independent of any specific vendor. This abstraction allows:
1. **Product standardization** - Same product from different vendors mapped to one Item record
2. **Historical consistency** - Order history remains consistent even when vendors change
3. **Simplified ordering** - Users select from standardized list, system handles vendor routing

Items works together with CrossRefs (vendor-specific) and DistrictItems (district-specific configurations).

### Usage

- **Product Browsing:** Users browse Items when creating requisitions
- **Catalog Management:** EDS admin maintains the master product list
- **Reporting:** Standardized reporting across districts and vendors
- **Bid Specifications:** Bid requests specify items, vendors respond with cross-refs

### Key Relationships

```
Parent Tables:
├── Category (CategoryId) - Product category
├── Units (UnitId) - Unit of measure (Each, Box, etc.)
├── Headings (HeadingId) - Catalog section heading
├── Manufacturers (ManufacturerId) - Product manufacturer
└── Vendors (VendorId) - Primary/default vendor

Child Tables:
├── CrossRefs (ItemId) - Vendor-specific cross-references
├── Detail (ItemId) - Order line items
├── BidRequestItems (ItemId) - Bid specifications
├── DistrictItems (ItemId) - District configurations
└── Pricing (ItemId) - Price history
```

### Critical Columns

| Column | Business Purpose |
|--------|------------------|
| ItemCode | Primary item identifier/SKU |
| Description | Full product name/description |
| CategoryId | Product classification |
| UnitId | Standard unit of measure |
| ListPrice | MSRP/default price |
| RTK | Right-to-Know flag (hazmat) |
| Active | Is product currently available |
| StandardItem | Is this a standard catalog item |

### Product Lifecycle

```
New Product Added (Active=1)
        │
        ▼
Cross-refs created (vendor pricing)
        │
        ▼
Available for ordering
        │
        ├─── Product discontinued
        │           │
        │           ▼
        │    RedirectedItemId set (points to replacement)
        │           │
        │           ▼
        │    Active set to 0
        │    DateDeactivated set
        │
        └─── Item updated (new pricing, description, etc.)
```

---

## 3. Detail

**Schema:** `dbo` | **Rows:** 30,842,040 | **Domain:** Orders & Purchasing

### Purpose

The Detail table stores individual line items on requisitions and purchase orders - every product ordered through the system creates a Detail record.

### Business Context

Detail is the transactional heart of the ordering system. When a user adds a product to their order:
1. A Detail record is created linking the Requisition to the Item
2. Price is calculated based on CrossRefs, Awards, or manual entry
3. The Detail flows through approval, PO generation, and vendor transmission
4. Historical Detail records provide purchasing analytics and reorder history

This table has 30M+ rows because every single line item ever ordered is preserved for history and reporting.

### Usage

- **Order Creation:** Users add items which create Detail records
- **PO Generation:** Detail records grouped by vendor to create POs
- **Spending Reports:** Aggregate Detail for district spending analysis
- **Reorder Suggestions:** Analyze past Detail to suggest reorders

### Key Relationships

```
Parent Tables:
├── Requisitions (RequisitionId) - The parent order
├── Items (ItemId) - What product was ordered
├── Vendors (VendorId) - Which vendor supplies it
├── Awards (AwardId) - What bid award provides the pricing
├── PO (POId) - Which PO this line is on
└── Catalog (CatalogId) - Source catalog

Related Tables:
├── PODetailItems - Links Detail to PO line items
├── BatchDetail - Batch processing records
└── CrossRefs - May link to specific cross-ref
```

### Critical Columns

| Column | Business Purpose |
|--------|------------------|
| RequisitionId | Parent requisition |
| ItemId | Product ordered |
| Quantity | How many units |
| BidPrice | Price from awarded bid |
| CatalogPrice | List/catalog price |
| GrossPrice | Gross before discount |
| DiscountRate | Applied discount |
| VendorId | Vendor fulfilling order |
| POId | Resulting purchase order |
| StatusId | Current status |
| Active | Is line item still valid |

### Order Flow

```
User selects product
        │
        ▼
Detail created (StatusId = On Hold)
        │
        ▼
Requisition submitted for approval
        │
        ▼
Detail.StatusId = Pending Approval
        │
        ▼
Approved → Detail.StatusId = Approved
        │
        ▼
PO Generated → Detail.POId set, StatusId = PO Printed
        │
        ▼
PO transmitted to vendor
```

---

## 4. Requisitions

**Schema:** `dbo` | **Rows:** 2,078,481 | **Domain:** Orders & Purchasing

### Purpose

The Requisitions table stores header-level information for purchase requests before they become purchase orders.

### Business Context

A Requisition represents a user's intent to purchase items. It goes through the approval workflow before becoming a Purchase Order:

1. **User creates requisition** - Selects school, account code, adds items
2. **Submits for approval** - Routes to appropriate approvers
3. **Approved** - Moves to EDS for PO generation
4. **PO Created** - Requisition marked as complete

Districts typically have 1.4M+ completed requisitions representing years of purchasing history.

### Usage

- **Order Entry:** Starting point for all purchases
- **Approval Workflow:** Routes through approval hierarchy
- **Budget Control:** Validates against budget accounts
- **PO Generation:** Grouped by vendor for PO creation

### Key Relationships

```
Parent Tables:
├── School (SchoolId) - Ordering location
├── Users (UserId) - Who created the requisition
├── BudgetAccounts (BudgetAccountId) - Funding source
├── Category (CategoryId) - Primary product category
├── Budgets (BudgetId) - Budget period
└── StatusTable (StatusId) - Current status

Child Tables:
├── Detail - Line items on this requisition
├── Approvals - Approval records
├── PO - Generated purchase orders
└── RequisitionNotes - User notes
```

### Status Flow (See EDS_STATUS_CODES.md)

| StatusId | Code | Meaning | Requisition Count |
|----------|------|---------|-------------------|
| 1 | H | On Hold | 148,171 |
| 2 | P | Pending Approval | 77,525 |
| 3 | A | Approved | 72,264 |
| 6 | O | PO Printed | 1,474,907 |
| 4 | R | Rejected | 10,081 |

### Critical Columns

| Column | Business Purpose |
|--------|------------------|
| RequisitionNumber | Human-readable ID |
| SchoolId | Ordering school |
| UserId | Creator |
| BudgetAccountId | Funding account |
| StatusId | Workflow status |
| TotalRequisitionCost | Order total |
| ApprovalRequired | Does this need approval |
| DateEntered | When created |

---

## 5. Vendors

**Schema:** `dbo` | **Rows:** 18,900 | **Domain:** Vendors

### Purpose

The Vendors table is the master supplier database containing all vendors that supply products to school districts through the EDS system.

### Business Context

Vendors are central to the procurement process:
1. **Bid Participation:** Vendors submit pricing through the bid process
2. **Order Fulfillment:** POs are transmitted to vendors
3. **Catalog Management:** Vendors maintain product catalogs (CrossRefs)
4. **Contract Management:** Awards link vendors to bid contracts

Vendor types include:
- **Bid Vendors:** Participate in competitive bidding
- **Direct Vendors:** Supply specific products directly
- **District Vendors:** District-specific suppliers

### Usage

- **Bid Management:** Invite vendors to bid, receive responses
- **PO Transmission:** Send orders electronically via cXML, FTP, email
- **Catalog Updates:** Vendors upload price/product changes
- **Reporting:** Vendor spending analysis

### Key Relationships

```
Child Tables (Vendor referenced by):
├── Catalog - Vendor's product catalogs
├── CrossRefs - Via Catalog, vendor-specific items
├── Awards - Contract awards to vendor
├── BidResults - Vendor bid submissions
├── PO - Purchase orders sent to vendor
├── DistrictVendor - District-vendor relationships
└── VendorContacts - Contact persons
```

### Critical Columns

| Column | Business Purpose |
|--------|------------------|
| Code | Short vendor code |
| Name | Company name |
| Address1-3, City, State, ZipCode | Mailing address |
| Phone, Fax, EMail | Contact info |
| UseGrossPrices | Pricing method |
| ShippingPercentage | Default shipping % |
| AllowElectronicPOs | Can receive e-POs |
| cXML* columns | Electronic ordering config |
| Active | Is vendor active |

### Electronic PO Integration

Vendors can receive POs via:
- **cXML:** Standard procurement XML format (cXMLAddress, cXML* columns)
- **FTP:** File upload (HostURL, HostPort, HostDirectory)
- **Email:** Email notification with PDF attachment
- **Manual:** Download from vendor portal

---

## 6. Category

**Schema:** `dbo` | **Rows:** 12,919 | **Domain:** Inventory & Items

### Purpose

The Category table defines the product classification hierarchy used to organize items across the system.

### Business Context

Categories organize products for:
1. **Browsing:** Users navigate categories to find products
2. **Bidding:** Bids are organized by category
3. **Reporting:** Spending reports by category
4. **Permissions:** Users may be restricted to certain categories

Categories are hierarchical (though flat in this table - hierarchy via naming/numbering conventions).

### Key Columns

| Column | Business Purpose |
|--------|------------------|
| CategoryNumber | Category code |
| Name | Category name |
| Code | Short code |
| Type | Category type |
| Prefix | Item code prefix |
| OnSavingsReport | Include in savings reports |
| Grouping | Report grouping |

---

## 7. District

**Schema:** `dbo` | **Rows:** 3,503 | **Domain:** Users & Security

### Purpose

The District table represents school districts - the primary organizational unit in the EDS system.

### Business Context

Districts are the customer entities:
1. **Contract Holders:** Districts sign contracts with EDS
2. **Budget Owners:** Budgets belong to districts
3. **User Organizations:** Users belong to schools within districts
4. **Procurement Units:** Orders and bids organized by district

### Key Relationships

```
Child Tables:
├── School - Schools in this district
├── Users - Via School
├── Budgets - District budgets
├── DistrictVendor - Approved vendors
├── DistrictItems - Custom item configurations
└── DistrictCategory - Allowed categories
```

---

## 8. School

**Schema:** `dbo` | **Rows:** 12,862 | **Domain:** Users & Security

### Purpose

The School table represents individual schools, offices, and departments within districts.

### Business Context

Schools are where orders originate:
1. **Order Origin:** Requisitions are placed by school
2. **Shipping Destination:** Orders ship to school address
3. **User Assignment:** Users belong to specific schools
4. **Budget Allocation:** Some budgets are school-specific

### Key Relationships

```
Parent:
└── District (DistrictId)

Child Tables:
├── Users - Users at this school
├── Requisitions - Orders from this school
└── SchoolContacts - School contact persons
```

---

## 9. Users

**Schema:** `dbo` | **Rows:** 28,643 | **Domain:** Users & Security

### Purpose

The Users table stores all user accounts for the EDS system.

### Business Context

Users are individuals who:
1. **Create Orders:** Place requisitions for their school
2. **Approve Orders:** Review and approve requisitions
3. **Manage Bids:** Create and evaluate bids (EDS staff)
4. **Administer System:** Manage districts and configuration

### User Hierarchy

```
EDS Staff (Level 5+)
    │
    ├── System Administrators (Level 9)
    │
    └── Customer Service Reps (Level 5)

District Users (Level 1-3)
    │
    ├── Business Administrators (Level 2)
    │       │
    │       └── Can approve district-wide
    │
    └── Teachers/Staff (Level 1)
            │
            └── Can order, limited approval
```

### Key Columns

| Column | Business Purpose |
|--------|------------------|
| UserName | Login username |
| Email | User email |
| SchoolId | Primary school |
| ApprovalLevel | User's authority level |
| Active | Is account active |

---

## 10. PO

**Schema:** `dbo` | **Domain:** Orders & Purchasing

### Purpose

The PO (Purchase Order) table stores generated purchase orders that are transmitted to vendors.

### Business Context

POs are created from approved requisitions:
1. Requisitions grouped by vendor
2. PO generated with unique number
3. PO transmitted to vendor (electronically or printed)
4. Status tracked through fulfillment

### Flow

```
Approved Requisitions
        │
        ▼
Group by Vendor
        │
        ▼
Generate PO (one per vendor)
        │
        ▼
Transmit to Vendor
        │
        ▼
Track Receipt/Completion
```

---

## 11. Awards

**Schema:** `dbo` | **Domain:** Bidding

### Purpose

The Awards table records bid awards - contracts given to vendors based on winning bids.

### Business Context

Awards are the outcome of the bidding process:
1. District creates bid (BidHeaders)
2. Vendors respond (BidResults)
3. District evaluates and awards (Awards)
4. Award prices become available for ordering (via CrossRefs)

### Award Types

| Type | Description |
|------|-------------|
| Primary | First-choice vendor |
| Secondary | Backup if primary unavailable |

---

## 12. BidHeaders

**Schema:** `dbo` | **Domain:** Bidding

### Purpose

The BidHeaders table stores bid solicitation headers - the master record for competitive bids.

### Business Context

BidHeaders drives the competitive procurement process:
1. District/EDS creates bid
2. Items added (BidRequestItems)
3. Vendors invited (VendorQuery)
4. Vendors respond (BidResults)
5. Evaluated and awarded (Awards)

---

## 13. Catalogs

**Schema:** `dbo` | **Domain:** Inventory & Items

### Purpose

The Catalogs table represents vendor product catalogs - collections of products with pricing from a specific vendor.

### Business Context

Catalogs organize vendor products:
1. Each vendor can have multiple catalogs
2. Catalogs have effective/expiration dates
3. CrossRefs belong to catalogs
4. Pricing tied to catalog/award periods

---

## Summary: Table Relationships

```
                          ┌─────────────┐
                          │   District  │
                          └─────────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            ▼            ▼
              ┌─────────┐  ┌─────────┐  ┌─────────┐
              │  School │  │ Budgets │  │ Vendors │
              └─────────┘  └─────────┘  └─────────┘
                    │            │            │
                    ▼            │            ▼
              ┌─────────┐        │      ┌─────────┐
              │  Users  │        │      │ Catalog │
              └─────────┘        │      └─────────┘
                    │            │            │
                    ▼            ▼            ▼
              ┌─────────────────────────────────────┐
              │          Requisitions               │
              │ (User creates, Budget funds)        │
              └─────────────────────────────────────┘
                                 │
                                 ▼
              ┌─────────────────────────────────────┐
              │             Detail                  │
              │ (Line items - links to Items)       │
              └─────────────────────────────────────┘
                                 │
                    ┌────────────┼────────────┐
                    ▼            │            ▼
              ┌─────────┐        │      ┌─────────┐
              │  Items  │        │      │   PO    │
              └─────────┘        │      └─────────┘
                    │            │            │
                    ▼            │            ▼
              ┌─────────┐        │      ┌─────────┐
              │CrossRefs│◄───────┘      │ Vendor  │
              └─────────┘               └─────────┘

      ┌─────────┐     ┌─────────┐     ┌─────────┐
      │BidHeader│────►│BidResult│────►│ Awards  │
      └─────────┘     └─────────┘     └─────────┘
```

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial Tier 1 table documentation | Phase 1 Documentation |
