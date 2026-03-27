# EDS Database - Business Workflows

Generated: 2026-01-15

This document describes the key business processes and how data flows through the EDS database tables. Use this guide to understand how tables relate to each other in the context of real business operations.

---

## Table of Contents

1. [Bidding & Procurement Workflow](#1-bidding--procurement-workflow)
2. [Order Processing Workflow](#2-order-processing-workflow)
3. [Vendor Management Workflow](#3-vendor-management-workflow)
4. [Product Catalog Workflow](#4-product-catalog-workflow)
5. [User & Approval Workflow](#5-user--approval-workflow)
6. [Budget Management Workflow](#6-budget-management-workflow)

---

## 1. Bidding & Procurement Workflow

### Overview
The bidding system manages competitive procurement for school districts. Districts create bid solicitations, vendors submit pricing, and awards are made to winning vendors.

### Process Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           BIDDING LIFECYCLE                                  │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  1. CREATE   │────►│  2. SOLICIT  │────►│  3. RECEIVE  │────►│  4. EVALUATE │
  │  BID REQUEST │     │   VENDORS    │     │   RESPONSES  │     │    BIDS      │
  └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
         │                    │                    │                    │
         ▼                    ▼                    ▼                    ▼
    BidHeaders           VendorQuery          BidResults          BidResults
    BidRequestItems      BidImports           BidItems            (evaluation)
                                              BidAnswers

                    ┌──────────────┐     ┌──────────────┐
              ─────►│   5. AWARD   │────►│  6. CATALOG  │
                    │   CONTRACT   │     │   PRICING    │
                    └──────────────┘     └──────────────┘
                           │                    │
                           ▼                    ▼
                        Awards              CrossRefs
                        Awardings           Items (pricing)
                        BidItems            Catalog
```

### Step-by-Step Table Flow

#### Step 1: Create Bid Request
| Table | Action | Description |
|-------|--------|-------------|
| **BidHeaders** | INSERT | Master bid record with bid number, dates, category |
| **BidRequestItems** | INSERT | Line items being bid (linked to Items table) |
| **BidRequestOptions** | INSERT | Optional specifications for items |
| **BidHeaderDocument** | INSERT | Attached bid documents/specs |

**Key Fields:**
- `BidHeaders.BidHeaderId` - Primary identifier for the bid
- `BidHeaders.BidDate` - When bid opens
- `BidHeaders.DueDate` - When responses are due
- `BidHeaders.CategoryId` - Product category being bid

#### Step 2: Solicit Vendors
| Table | Action | Description |
|-------|--------|-------------|
| **VendorQuery** | INSERT | Track which vendors are invited |
| **BidImports** | INSERT | Import vendor catalog data |
| **DMSVendorBidDocuments** | INSERT | Vendor-specific bid documents |

#### Step 3: Receive Vendor Responses
| Table | Action | Description |
|-------|--------|-------------|
| **BidResults** | INSERT | Vendor's submitted bid pricing |
| **BidItems** | INSERT | Line-item pricing from vendor |
| **BidAnswers** | INSERT | Vendor responses to questions |
| **BidResultChanges** | INSERT | Track changes to submitted bids |

**Key Fields:**
- `BidResults.BidResultsId` - Unique submission identifier
- `BidResults.VendorId` - Which vendor submitted
- `BidResults.BidPrice` - Submitted price
- `BidResults.Active` - Is this the current/valid submission

#### Step 4: Evaluate Bids
| Table | Action | Description |
|-------|--------|-------------|
| **BidResults** | UPDATE | Mark evaluation status |
| **BidResultsChangeLog** | INSERT | Audit trail of evaluation |
| **BidHeaderCheckList** | UPDATE | Track evaluation checklist |

#### Step 5: Award Contract
| Table | Action | Description |
|-------|--------|-------------|
| **Awards** | INSERT | Create award record |
| **Awardings** | INSERT | Link award to specific items |
| **BidItems** | UPDATE | Mark winning items |
| **AwardsCatalogList** | INSERT | Which catalogs are included |

**Key Fields:**
- `Awards.AwardId` - Award identifier
- `Awards.VendorId` - Winning vendor
- `Awards.EffectiveDate` / `ExpirationDate` - Contract period
- `Awards.AwardTypeId` - Type of award (1=Primary, 2=Secondary?)

#### Step 6: Update Catalog Pricing
| Table | Action | Description |
|-------|--------|-------------|
| **CrossRefs** | UPDATE | Update item pricing from award |
| **Items** | UPDATE | Update list prices |
| **Catalog** | UPDATE | Refresh vendor catalog |

### Status Values

| Status | Meaning | Table |
|--------|---------|-------|
| Open | Bid accepting submissions | BidHeaders |
| Closed | Submissions closed, under review | BidHeaders |
| Awarded | Contract awarded | BidHeaders |
| Cancelled | Bid cancelled | BidHeaders |

### Key Relationships

```
BidHeaders (1) ────< BidRequestItems (n)
     │                     │
     │                     └──── Items
     │
     ├────< BidResults (n) ────< BidItems (n)
     │           │
     │           └──── Vendors
     │
     └────< Awards (n) ────< Awardings (n)
```

---

## 2. Order Processing Workflow

### Overview
The ordering system manages requisitions from schools, approval workflows, and purchase order generation for awarded vendors.

### Process Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ORDER PROCESSING LIFECYCLE                           │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  1. CREATE   │────►│  2. SUBMIT   │────►│  3. APPROVE  │────►│  4. GENERATE │
  │ REQUISITION  │     │   FOR REVIEW │     │  REQUISITION │     │      PO      │
  └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
         │                    │                    │                    │
         ▼                    ▼                    ▼                    ▼
   Requisitions          Requisitions          Approvals               PO
   Detail                (status change)        (insert)           PODetailItems
   UserAccounts                                                    POStatus

                    ┌──────────────┐     ┌──────────────┐
              ─────►│  5. TRANSMIT │────►│  6. RECEIVE  │
                    │   TO VENDOR  │     │    GOODS     │
                    └──────────────┘     └──────────────┘
                           │                    │
                           ▼                    ▼
                     TransmitLog            (external)
                     VendorOrders
```

### Step-by-Step Table Flow

#### Step 1: Create Requisition
| Table | Action | Description |
|-------|--------|-------------|
| **Requisitions** | INSERT | Header record for the requisition |
| **Detail** | INSERT | Line items being ordered |
| **UserAccounts** | SELECT | Validate user's budget account |
| **BudgetAccounts** | SELECT | Check available budget |

**Key Fields:**
- `Requisitions.RequisitionId` - Unique requisition number
- `Requisitions.UserId` - Who created it
- `Requisitions.SchoolId` - Ordering school
- `Requisitions.StatusId` - Current status
- `Detail.DetailId` - Line item identifier
- `Detail.Quantity` - Quantity ordered
- `Detail.ItemId` - Product being ordered

#### Step 2: Submit for Review
| Table | Action | Description |
|-------|--------|-------------|
| **Requisitions** | UPDATE | Change status to "Submitted" |
| **RequisitionChangeLog** | INSERT | Audit trail |
| **PendingApprovals** | INSERT | Queue for approver |

#### Step 3: Approve Requisition
| Table | Action | Description |
|-------|--------|-------------|
| **Approvals** | INSERT | Record approval decision |
| **Requisitions** | UPDATE | Update status to "Approved" |
| **ApprovalsHistory** | INSERT | Archive approval record |
| **Detail** | UPDATE | Mark lines as approved |

**Key Fields:**
- `Approvals.ApprovalId` - Approval record ID
- `Approvals.ApprovalById` - Who approved
- `Approvals.StatusId` - Approval status (Approved/Rejected)
- `Approvals.RequisitionId` - Which requisition

#### Step 4: Generate Purchase Order
| Table | Action | Description |
|-------|--------|-------------|
| **PO** | INSERT | Create purchase order header |
| **PODetailItems** | INSERT | Line items on PO |
| **POStatus** | INSERT | Track PO status changes |
| **OrderBookDetail** | INSERT | Add to order book for vendor |

**Key Fields:**
- `PO.POId` - Purchase order number
- `PO.VendorId` - Vendor receiving order
- `PO.PODate` - Order date
- `PODetailItems.DetailId` - Links back to original requisition line

#### Step 5: Transmit to Vendor
| Table | Action | Description |
|-------|--------|-------------|
| **TransmitLog** | INSERT | Record transmission |
| **VendorOrders** | INSERT | Vendor order tracking |
| **POQueue** | UPDATE | Mark as transmitted |

#### Step 6: Receive Goods
| Table | Action | Description |
|-------|--------|-------------|
| **Detail** | UPDATE | Mark as received |
| **POStatus** | INSERT | Update PO status |

### Requisition Status Values

| StatusId | Meaning | Next States |
|----------|---------|-------------|
| 1 | Draft | Submit (2) |
| 2 | Submitted | Approved (3), Rejected (5) |
| 3 | Approved | PO Generated (4) |
| 4 | PO Generated | Transmitted (6) |
| 5 | Rejected | Draft (1) |
| 6 | Transmitted | Received (7) |
| 7 | Received | Complete (8) |
| 8 | Complete | - |

### Key Relationships

```
Users ────< Requisitions (n) ────< Detail (n) ────< Items
  │              │                     │
  │              │                     └──── CrossRefs (pricing)
  │              │
  │              └────< Approvals (n)
  │                          │
  │                          └──── Users (ApprovalById)
  │
  └────< UserAccounts ────< BudgetAccounts ────< Budgets

Requisitions ────< PO (via Detail/PODetailItems)
                    │
                    ├────< PODetailItems (n)
                    │           │
                    │           └──── Detail (link)
                    │
                    └────< POStatus (n)
```

---

## 3. Vendor Management Workflow

### Overview
Manages vendor registration, qualification, and ongoing relationship for procurement.

### Process Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        VENDOR MANAGEMENT LIFECYCLE                           │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │ 1. REGISTER  │────►│ 2. QUALIFY   │────►│ 3. MAINTAIN  │────►│ 4. DEACTIVATE│
  │    VENDOR    │     │    VENDOR    │     │   CATALOGS   │     │   (if needed)│
  └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
         │                    │                    │                    │
         ▼                    ▼                    ▼                    ▼
      Vendors            VendorQuery           Catalog              Vendors
    VendorContacts      DistrictVendor        CrossRefs           (Active=0)
                        VendorCategory         Items
```

### Step-by-Step Table Flow

#### Step 1: Register Vendor
| Table | Action | Description |
|-------|--------|-------------|
| **Vendors** | INSERT | Master vendor record |
| **VendorContacts** | INSERT | Contact persons |
| **VendorSessions** | INSERT | Login credentials (for portal) |

**Key Fields:**
- `Vendors.VendorId` - Unique vendor ID
- `Vendors.Name` - Company name
- `Vendors.Code` - Short vendor code
- `Vendors.Active` - Is vendor active

#### Step 2: Qualify Vendor
| Table | Action | Description |
|-------|--------|-------------|
| **DistrictVendor** | INSERT | Link vendor to districts |
| **VendorCategory** | INSERT | Categories vendor can supply |
| **VendorQuery** | INSERT | Track vendor communications |

#### Step 3: Maintain Catalogs
| Table | Action | Description |
|-------|--------|-------------|
| **Catalog** | INSERT/UPDATE | Vendor's product catalog |
| **CrossRefs** | INSERT/UPDATE | Item cross-references and pricing |
| **Items** | INSERT/UPDATE | Product master data |
| **VendorUploads** | INSERT | Track catalog uploads |

#### Step 4: Deactivate Vendor
| Table | Action | Description |
|-------|--------|-------------|
| **Vendors** | UPDATE | Set Active = 0 |
| **CrossRefs** | UPDATE | Deactivate pricing |
| **Awards** | UPDATE | Expire active awards |

### Key Tables

| Table | Purpose | Key Fields |
|-------|---------|------------|
| **Vendors** | Master vendor data | VendorId, Name, Code, Active |
| **VendorContacts** | Contact persons | VendorContactId, VendorId, Name, Email |
| **DistrictVendor** | Vendor-District relationships | DistrictVendorId, DistrictId, VendorId |
| **VendorCategory** | Product categories vendor supplies | VCId, VendorId, CategoryId |
| **VendorUploads** | Catalog upload tracking | UploadId, VendorId, UploadDate |

---

## 4. Product Catalog Workflow

### Overview
Manages the product catalog including items, pricing, cross-references, and vendor catalogs.

### Process Flow

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         CATALOG MANAGEMENT LIFECYCLE                         │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
  │  1. CREATE   │────►│ 2. CROSS-REF │────►│  3. PRICE    │────►│  4. PUBLISH  │
  │    ITEM      │     │   TO VENDOR  │     │    UPDATE    │     │  TO CATALOG  │
  └──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
         │                    │                    │                    │
         ▼                    ▼                    ▼                    ▼
      Items              CrossRefs            CrossRefs            Catalog
     Category            Catalog              (pricing)           DistrictItems
      Units                                   Awards
```

### Key Tables and Relationships

#### Items (Product Master)
| Field | Description |
|-------|-------------|
| ItemId | Primary key - system product ID |
| ItemCode | Short SKU code |
| Description | Product name |
| ShortDescription | Brief description |
| CategoryId | FK to Category |
| UnitId | FK to Units (unit of measure) |
| VendorId | Primary vendor |
| ListPrice | Default list price |
| Active | Is product available |

#### CrossRefs (Vendor Cross-References)
| Field | Description |
|-------|-------------|
| CrossRefId | Primary key |
| ItemId | FK to Items - which product |
| CatalogId | FK to Catalog - which vendor catalog |
| VendorItemCode | Vendor's product code |
| ImageURL | Product image |
| Active | Is this cross-ref active |

**Note:** CrossRefs links internal Items to vendor Catalogs. One Item can have multiple CrossRefs (different vendors).

#### Catalog (Vendor Catalogs)
| Field | Description |
|-------|-------------|
| CatalogId | Primary key |
| VendorId | FK to Vendors |
| Name | Catalog name |
| EffectiveDate | When pricing is valid |
| ExpirationDate | When pricing expires |

### Item-to-Order Flow

```
Items ────< CrossRefs (n) ────< Catalog ────< Vendors
  │              │
  │              └──── ImageURL, VendorItemCode, Pricing
  │
  ├──── Category (classification)
  │
  ├──── Units (unit of measure)
  │
  └────< Detail (orders) ────< Requisitions
```

---

## 5. User & Approval Workflow

### Overview
Manages user accounts, school assignments, and approval hierarchies.

### Key Tables

| Table | Purpose |
|-------|---------|
| **Users** | User accounts |
| **District** | School districts |
| **School** | Individual schools |
| **UserAccounts** | User-to-budget-account links |
| **Approvals** | Approval workflow records |
| **ApprovalLevels** | Approval thresholds by amount |
| **SecurityRoles** | Role definitions |
| **SecurityRoleUsers** | User role assignments |

### Approval Flow

```
User submits Requisition
         │
         ▼
┌─────────────────────┐
│ Check ApprovalLevels│──── Is amount within user's authority?
└─────────────────────┘
         │
    ┌────┴────┐
    │ Yes     │ No
    ▼         ▼
Auto-approve  Route to approver
    │              │
    ▼              ▼
Approvals     PendingApprovals
(insert)      (queue for approver)
                   │
                   ▼
              Approver reviews
                   │
              ┌────┴────┐
              │ Approve │ Reject
              ▼         ▼
          Approvals  Approvals
          (Approved) (Rejected)
```

### Organizational Hierarchy

```
District (1)
    │
    ├──── School (n)
    │         │
    │         └──── Users (n)
    │                   │
    │                   └──── UserAccounts (n)
    │                              │
    │                              └──── BudgetAccounts
    │                                        │
    │                                        └──── Budgets
    │
    └──── DistrictCategories (allowed categories)
```

---

## 6. Budget Management Workflow

### Overview
Tracks budget allocations, encumbrances, and spending by account.

### Key Tables

| Table | Purpose |
|-------|---------|
| **Budgets** | Budget period definitions |
| **BudgetAccounts** | Individual budget line items |
| **UserAccounts** | Links users to their budget accounts |
| **Accounts** | Chart of accounts |

### Budget Flow

```
Budget (fiscal year)
    │
    └──── BudgetAccounts (line items)
              │
              └──── UserAccounts (user access)
                        │
                        └──── Detail (encumbrances when ordered)
                                  │
                                  └──── PODetailItems (actual spending)
```

### Budget Validation

When a requisition is created:
1. Check `UserAccounts` - does user have access to this budget?
2. Check `BudgetAccounts` - is there sufficient balance?
3. Check `ApprovalLevels` - does amount require approval?

---

## Quick Reference: Table Domains

| Domain | Key Tables | Primary Flow |
|--------|------------|--------------|
| **Bidding** | BidHeaders → BidResults → Awards | Solicitation → Response → Award |
| **Orders** | Requisitions → Detail → PO → PODetailItems | Request → Approve → Order |
| **Vendors** | Vendors → DistrictVendor → Catalog | Register → Qualify → Maintain |
| **Catalog** | Items → CrossRefs → Catalog | Create → Cross-ref → Price |
| **Users** | Users → UserAccounts → BudgetAccounts | Assign → Budget → Approve |
| **Budget** | Budgets → BudgetAccounts → Detail | Allocate → Encumber → Spend |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial workflow documentation | Phase 1 Documentation |
