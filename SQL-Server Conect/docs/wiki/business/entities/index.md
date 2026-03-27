# Business Entities

[Home](../../index.md) > [Business](../index.md) > Entities

---

## Overview

EDS manages the complete lifecycle of K-12 school procurement through interconnected business entities. Understanding these entities and their relationships is essential for working with the system.

---

## Entity Hierarchy

```
Districts (Organization Level)
    │
    ├── Schools (Individual Campuses)
    │       │
    │       └── Users (Staff & Administrators)
    │               │
    │               └── Requisitions (Purchase Requests)
    │                       │
    │                       └── Detail Lines (Items)
    │                               │
    │                               └── Purchase Orders
    │
    ├── Vendors (Suppliers)
    │       │
    │       ├── CrossRefs (Catalog Items)
    │       │
    │       └── Bids & Awards
    │
    └── Budgets (Account Codes)
```

---

## Core Entities

| Entity | Description | Key Table | Records |
|--------|-------------|-----------|---------|
| [Districts & Schools](districts-schools.md) | Organization hierarchy | Districts, Schools | ~500 districts |
| [Users & Roles](users-roles.md) | People and permissions | Users, UserRoles | Thousands |
| [Vendors](vendors.md) | Suppliers and contacts | Vendors, VendorContacts | ~10,000+ |
| [Requisitions](requisitions.md) | Purchase requests | Requisitions, Detail | Millions |
| [Purchase Orders](purchase-orders.md) | Official orders | PurchaseOrders | Millions |
| [Bids & Awards](bids-awards.md) | Competitive bidding | BidHeaders, Awards | ~76 tables |
| [Catalogs & Items](catalogs-items.md) | Product catalog | Items, CrossRefs | Millions |

---

## Entity Relationships Diagram

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  District   │────▶│   School    │────▶│    User     │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                                               ▼
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Vendor    │────▶│   CrossRef  │────▶│ Requisition │
└─────────────┘     │   (Items)   │     └─────────────┘
      │             └─────────────┘            │
      │                                        ▼
      │             ┌─────────────┐     ┌─────────────┐
      └────────────▶│  Bid/Award  │────▶│   Detail    │
                    └─────────────┘     │   (Lines)   │
                                        └─────────────┘
                                               │
                                               ▼
                                        ┌─────────────┐
                                        │     PO      │
                                        └─────────────┘
```

---

## Data Flow

### 1. Setup Phase
1. Districts configure their organization structure
2. Schools are linked to districts
3. Users are created with appropriate roles
4. Vendors are onboarded and catalogs loaded

### 2. Procurement Phase
1. User creates a **Requisition**
2. **Detail** lines specify items and quantities
3. Items linked to **CrossRefs** (vendor catalog)
4. Requisition goes through **Approval** workflow

### 3. Ordering Phase
1. Approved requisition becomes **Purchase Order**
2. PO sent to **Vendor**
3. Items received and invoiced
4. Budget accounts updated

---

## Key Relationships

| Parent | Child | Relationship |
|--------|-------|--------------|
| District | School | One-to-Many |
| School | User | Many-to-Many (UserSchools) |
| User | Requisition | One-to-Many |
| Requisition | Detail | One-to-Many |
| Detail | CrossRef | Many-to-One |
| Vendor | CrossRef | One-to-Many |
| BidHeader | Award | One-to-Many |
| Award | CrossRef | One-to-Many |

---

## Table Count by Domain

| Domain | Tables | Description |
|--------|--------|-------------|
| Bidding | 76 | Competitive bidding process |
| Orders | 45 | Requisitions and POs |
| Vendors | 32 | Vendor management |
| Inventory | 28 | Items and catalogs |
| Users | 24 | Security and permissions |
| Finance | 18 | Budgets and accounting |
| Documents | 15 | Attachments and files |

---

## Next Steps

- Explore each entity in detail using the links above
- See [Workflows](../workflows/index.md) for process documentation
- See [Schema Reference](../../schema/index.md) for technical details

