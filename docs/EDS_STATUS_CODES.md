# EDS Database - Status Codes & Lookup Tables Reference

Generated: 2026-01-15

This document provides a comprehensive reference for all status codes, lookup values, and type definitions used throughout the EDS database.

---

## Table of Contents

1. [Master Status Table](#master-status-table)
2. [Requisition Status Workflow](#requisition-status-workflow)
3. [Approval System](#approval-system)
4. [Award & Bidding Types](#award--bidding-types)
5. [District & Organization Types](#district--organization-types)
6. [Product & Catalog Types](#product--catalog-types)
7. [Charge & Billing Types](#charge--billing-types)
8. [Vendor Query Status Usage](#vendor-query-status-usage)

---

## Master Status Table

The `StatusTable` is the central status lookup used across multiple entities (requisitions, vendor queries, approvals, etc.).

**Table:** `dbo.StatusTable` | **Rows:** 53

### Workflow Statuses (OptionValue > 0)

These statuses represent actual workflow states for requisitions and related entities.

| StatusId | Code | Name | Required Level | Option | Description |
|----------|------|------|----------------|--------|-------------|
| 1 | H | On Hold | 1 | 1 | Requisition is on hold, pending user action |
| 2 | P | Pending Approval | 1 | 2 | Awaiting approver review |
| 3 | A | Approved | 1 | 3 | Approved by all required approvers |
| 4 | R | Rejected | 1 | 4 | Rejected by approver |
| 5 | I | At EDS | 5 | 5 | Sent to EDS for processing |
| 6 | O | PO Printed | 9 | 6 | Purchase order has been printed |
| 23 | S | SBS Printed | 10 | 8 | School-based summary printed |
| 24 | 1 | SBS Pending | 10 | 7 | Awaiting SBS processing |
| 25 | J | Just Converted | 9 | 9 | Recently converted/imported |
| 27 | B | Ready to Bid | 9 | 10 | Ready for bid solicitation |
| 28 | C | On Hold - Bid Completed | 5 | 11 | Bid complete, on hold for review |
| 29 | W | Out to Bid - Waiting Response | 9 | 12 | Bid sent to vendors, awaiting responses |
| 32 | E | Changes at EDS | 5 | 13 | EDS made changes, needs review |
| 35 | D | Requisition Downloaded | 9 | 14 | Downloaded for offline processing |
| 45 | M | Manually Processed PO | 1 | 15 | PO processed manually (not system-generated) |
| 48 | 3 | PO Sent | 9 | 17 | PO transmitted to vendor |
| 49 | 2 | Requisition Printed for POs | 9 | 16 | Printed for PO generation |

### Action/Menu Options (OptionValue < 0)

These entries represent system actions/menu options, not workflow statuses.

| StatusId | Name | Required Level | Option | Purpose |
|----------|------|----------------|--------|---------|
| 7 | Export To Comet | 99 | -2 | Export to Comet accounting system |
| 8 | Print Screen Summary | 1 | -1 | Generate summary report |
| 9 | Create PO | 5 | -3 | Generate purchase orders |
| 10 | Update Next PO Number | 5 | -4 | Increment PO number sequence |
| 11 | District Summary | 5 | -5 | District-level summary report |
| 12 | Textbook Bid Report | 5 | -6 | Textbook bidding report |
| 13 | Delete Requisition | 5 | -12 | Remove requisition |
| 14 | Textbook Savings Report | 5 | -7 | Savings analysis for textbooks |
| 15 | Textbook Distribution Report | 5 | -8 | Distribution report |
| 16 | Create Textbook POs | 5 | -9 | Generate textbook purchase orders |
| 17 | Textbook Usage Report | 5 | -10 | Usage statistics |
| 18 | Copy Requisitions Forward | 10 | -11 | Roll forward to next year |
| 19 | Print Requisition(s) | 1 | -13 | Print requisition forms |
| 20 | Combine Requisitions | 5 | -14 | Merge multiple requisitions |
| 21 | School Summary | 10 | -15 | School-level summary |
| 22 | Schedule SBS | 10 | -16 | Schedule school-based summary |
| 26 | Create Acct File | 9 | -17 | Create accounting export file |
| 30 | Item Distribution Report | 1 | -18 | Item distribution analysis |
| 31 | Download Requisition(s) | 1 | -19 | Download for offline |
| 33 | Reprocess Requisition(s) | 5 | -20 | Re-run processing |
| 34 | No Bid Report | 5 | -21 | Items with no bids |
| 36 | Queued Copy Forward | 5 | -22 | Queue for rollover |
| 37 | Print Selective Screen Summary | 1 | -23 | Selective summary |
| 38 | Audit Report | 1 | -24 | Audit trail report |
| 39 | Print Award Letter | 1 | -25 | Generate award letters |
| 40 | Vendor Summary | 1 | -26 | Vendor activity summary |
| 41 | Bid Analysis | 5 | -27 | Analyze bid responses |
| 42 | Print My Users | 9 | -28 | User list report |
| 43 | Combine Reqs by Vendor | 5 | -29 | Consolidate by vendor |
| 46 | E-Mail to Vendor | 9 | -30 | Send email notification |
| 54 | Pre PO Verification | 5 | -31 | Verify before PO generation |
| 55 | Print Requisition(s) Bid Tab | 1 | -32 | Print bid tabulation |
| 56 | Export Spend Summary | 1 | -33 | Export spending data |
| 57 | Export Vendor Summary | 5 | -34 | Export vendor data |
| 58 | Delete Purchase Order(s) | 10 | -35 | Remove POs |
| 59 | Export Tagged Incidental Orders | 5 | -36 | Export incidental orders |

---

## Requisition Status Workflow

Based on actual usage data from 1.8M+ requisitions:

### Status Distribution

| Status | Code | Count | % of Total | Typical Flow |
|--------|------|-------|-----------|--------------|
| PO Printed | O | 1,474,907 | 81.5% | Final state for most orders |
| On Hold | H | 148,171 | 8.2% | Initial/paused state |
| Pending Approval | P | 77,525 | 4.3% | Awaiting approval |
| Approved | A | 72,264 | 4.0% | Ready for PO generation |
| Requisition Downloaded | D | 24,457 | 1.4% | Offline processing |
| Rejected | R | 10,081 | 0.6% | Returned to user |

### Standard Requisition Flow

```
┌──────────┐     ┌──────────────────┐     ┌──────────┐     ┌──────────┐
│ On Hold  │────►│ Pending Approval │────►│ Approved │────►│ At EDS   │
│   (H)    │     │       (P)        │     │    (A)   │     │   (I)    │
└──────────┘     └──────────────────┘     └──────────┘     └──────────┘
     │                   │                                       │
     │                   ▼                                       ▼
     │            ┌──────────┐                           ┌──────────────┐
     │            │ Rejected │                           │  PO Printed  │
     │            │    (R)   │                           │     (O)      │
     │            └──────────┘                           └──────────────┘
     │                   │                                       │
     └───────────────────┘                                       ▼
          (Return to On Hold)                           ┌──────────────┐
                                                        │   PO Sent    │
                                                        │     (3)      │
                                                        └──────────────┘
```

### Bidding-Related Flow

```
┌──────────┐     ┌───────────────────────────┐     ┌────────────────────┐
│ Approved │────►│ Ready to Bid              │────►│ Out to Bid -       │
│   (A)    │     │        (B)                │     │ Waiting Response   │
└──────────┘     └───────────────────────────┘     │        (W)         │
                                                   └────────────────────┘
                                                            │
                                                            ▼
                                                   ┌────────────────────┐
                                                   │ On Hold -          │
                                                   │ Bid Completed (C)  │
                                                   └────────────────────┘
```

---

## Approval System

### Approval Levels

**Table:** `dbo.ApprovalLevels` | **Rows:** 9

| LevelId | Level | Description | Typical Use |
|---------|-------|-------------|-------------|
| 1 | 0 | None | No approval required |
| 2 | 1 | Principal / Director / Supervisor | School-level approval |
| 3 | 2 | Business Administrator | District business office |
| 9 | 3 | Accounting | Financial verification |
| 4 | 5 | Customer Service Rep | EDS support staff |
| 7 | 7 | Support Personnel | Technical support |
| 8 | 8 | EDS Administration | EDS admin functions |
| 5 | 9 | System Administrator | Full system access |
| 6 | 11 | Tab House | Highest level (obsolete?) |

### Approval Workflow

1. **User submits requisition** → Status changes to "Pending Approval" (P)
2. **System checks ApprovalLevels** → Routes to appropriate approver based on amount/rules
3. **Approver reviews:**
   - **Approve** → Status changes to "Approved" (A)
   - **Reject** → Status changes to "Rejected" (R), returns to user
4. **Approved requisitions** → Move to "At EDS" (I) for processing

---

## Award & Bidding Types

### Award Types

**Table:** `dbo.AwardTypes` | **Rows:** 2

| AwardTypeId | Description | Usage |
|-------------|-------------|-------|
| 1 | Primary | Main award - first choice vendor |
| 2 | Secondary | Backup award - alternate vendor if primary unavailable |

### Book Types (Textbooks)

**Table:** `dbo.BookTypes` | **Rows:** 4

| BookTypeId | BookType | Description |
|------------|----------|-------------|
| 1 | Student Edition | Standard student textbook |
| 2 | Teacher Edition | Instructor version with answers |
| 3 | Workbook | Consumable student workbook |
| 4 | Dictionary | Reference dictionaries |

### Calendar Types (Bid Scheduling)

**Table:** `dbo.CalendarTypes` | **Rows:** 2

| CalendarTypeId | Description | DateCount | Notes |
|----------------|-------------|-----------|-------|
| 1 | Pre-Bid Calendar | 1 | Single date for pre-bid activities |
| 2 | Supplement Bids Calendar | 4 | Multiple dates (75→14→7 day spacing) |

### Price List Types

**Table:** `dbo.PriceListTypes` | **Rows:** 2

| PriceListTypeId | Name | Active | Description |
|-----------------|------|--------|-------------|
| 1 | Published MSRP | Yes | Manufacturer's suggested retail price |
| 2 | Vendor Price List | Yes | Vendor's custom pricing |

---

## District & Organization Types

### District Types

**Table:** `dbo.DistrictTypes` | **Rows:** 6

| TypeId | Description | Uses Online | Uses Booklet | Prior Year Reqs | Verify SBS |
|--------|-------------|-------------|--------------|-----------------|------------|
| 1 | Booklet Only | No | Yes | - | - |
| 2 | Online Only | Yes | No | Yes | - |
| 3 | Booklet & Online | Yes | Yes | Yes | - |
| 4 | Online without Prior Year Reqs | Yes | No | No | - |
| 5 | Verify SBS Online | Yes | Yes | No | Yes |
| 6 | T&M Only | - | - | - | - |

### District Contact Types

**Table:** `dbo.DistrictContactTypes` | **Rows:** 7

| TypeId | Description | Purpose |
|--------|-------------|---------|
| 1 | Business Administrator | Primary business contact |
| 2 | Primary Contact | Main EDS system contact |
| 3 | Athletic Director | Athletics procurement |
| 4 | Buildings and Grounds | Facilities/maintenance |
| 5 | Accounts Payable | Invoice/payment contact |
| 6 | RTK Contact | Right-to-Know compliance |
| 8 | Additional Renewal Contact | License renewal notices |

### Instruction Book Types

**Table:** `dbo.InstructionBookTypes` | **Rows:** 6

| IBTypeId | Description | Show In All Books | Purpose |
|----------|-------------|-------------------|---------|
| 1 | User | Yes | General user instructions |
| 2 | Administrator | No | Admin-specific instructions |
| 3 | Athletic | No | Athletic department |
| 4 | Custodial | No | Custodial/facilities |
| 5 | Vo-Tech | No | Vocational-technical |
| 6 | Business Office | No | Business office procedures |

---

## Product & Catalog Types

### Units of Measure

**Table:** `dbo.Units` | **Rows:** ~1,500 (Active)

Common unit codes include:
- EA (Each)
- DZ (Dozen)
- CS (Case)
- PK (Pack)
- BX (Box)
- CT (Carton)
- RM (Ream)
- GL (Gallon)

*Note: Full list available via database query*

### Category Structure

**Table:** `dbo.Category` | **Rows:** ~12,900

Categories are organized hierarchically with:
- `CategoryNumber` - Category identifier
- `Name` - Display name
- `Type` - Category type classification
- `Grouping` - Grouping for reports

---

## Charge & Billing Types

### Charge Types

**Table:** `dbo.ChargeTypes` | **Rows:** 14 (Active)

| ChargeTypeId | Description | Notes |
|--------------|-------------|-------|
| 1 | Annual EDSIQ Licence | Base license |
| 2 | Annual EDSIQ Licence with Right to Know | License + RTK |
| 3 | Right to Know | RTK add-on only |
| 4 | Accounting System Interface | Accounting integration |
| 5 | Training | Training services |
| 6 | Time and Materials | T&M billing |
| 7 | Generic PO's | Generic PO feature |
| 8 | e-PO Module | Electronic PO module |
| 9 | Annual EDSIQ Licencse with T&M | License + T&M |
| 10 | Annual EDSIQ Licencse with RTK and T&M | Full package |
| 11 | Right to Know Annual State Filing Preparation | RTK filing service |
| 13 | Apple Computer Products Bid Access and Support | Apple products access |
| 90008 | License and Maintenance with e-PO | L&M + e-PO |
| 90009 | License and Maintenance with T&M and e-PO | Full package + e-PO |

---

## Vendor Query Status Usage

Vendor queries use the same StatusTable but primarily these statuses:

| StatusId | Code | Name | Query Count | Description |
|----------|------|------|-------------|-------------|
| 1 | H | On Hold | 15,640 | Query on hold/pending |
| 5 | I | At EDS | 7,589 | Being processed at EDS |
| 4 | R | Rejected | 5,826 | Query rejected |
| 2 | P | Pending Approval | 905 | Awaiting approval |
| 3 | A | Approved | 172 | Query approved |
| 6 | O | PO Printed | 90 | Completed |

---

## Quick Reference

### Common Status Codes

| Code | Meaning | Where Used |
|------|---------|------------|
| H | On Hold | Requisitions, Vendor Queries |
| P | Pending Approval | Requisitions, Approvals |
| A | Approved | Requisitions, Vendor Queries |
| R | Rejected | Requisitions, Vendor Queries |
| I | At EDS | Requisitions processing |
| O | PO Printed | Completed requisitions |
| B | Ready to Bid | Bid processing |
| W | Waiting Response | Out for bid |
| S | SBS Printed | School-based summary |
| D | Downloaded | Offline processing |

### Required Level Reference

| Level | Access Type |
|-------|-------------|
| 1 | Basic User |
| 5 | EDS Staff |
| 9 | System Admin |
| 10 | District Admin |
| 99 | Super Admin |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial status codes documentation | Phase 1 Documentation |
