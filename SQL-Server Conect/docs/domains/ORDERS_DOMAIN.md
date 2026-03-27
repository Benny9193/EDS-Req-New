# EDS Database - Orders & Purchasing Domain

Generated: 2026-01-15

This document provides comprehensive documentation for all tables in the Orders & Purchasing domain, which manages requisitions, approvals, purchase orders, and order fulfillment.

**Total Tables:** 47 | **Total Rows:** ~395 million

---

## Table of Contents

1. [Domain Overview](#domain-overview)
2. [Requisition Tables](#requisition-tables)
3. [Order Detail Tables](#order-detail-tables)
4. [Approval Tables](#approval-tables)
5. [Purchase Order Tables](#purchase-order-tables)
6. [Batch Processing Tables](#batch-processing-tables)
7. [Order Book Tables](#order-book-tables)
8. [Supporting Tables](#supporting-tables)

---

## Domain Overview

The Orders & Purchasing domain handles the complete order lifecycle from requisition to fulfillment:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ORDER PROCESSING LIFECYCLE                           │
└─────────────────────────────────────────────────────────────────────────────┘

  CREATE             APPROVE            GENERATE           TRANSMIT
 ┌──────────┐       ┌──────────┐       ┌──────────┐       ┌──────────┐
 │Requisition│─────►│ Approvals │─────►│    PO    │─────►│ POQueue  │
 │          │       │          │       │          │       │          │
 └──────────┘       └──────────┘       └──────────┘       └──────────┘
      │                  │                  │                  │
      ▼                  ▼                  ▼                  ▼
   Detail           ApprovalLevels    PODetailItems      TransmitLog
   ReqNotes         ApprovalsHistory  POStatus           VendorOrders
   ReqChangeLog     PendingApprovals  POQueue

  BATCH              ORDER BOOK         FULFILL
 ┌──────────┐       ┌──────────┐       ┌──────────┐
 │ Batches  │─────►│OrderBooks │─────►│ Detail   │
 │          │       │          │       │(updated) │
 └──────────┘       └──────────┘       └──────────┘
      │                  │                  │
      ▼                  ▼                  ▼
 BatchDetail        OrderBookDetail   DetailChanges
 BatchBook          OrderBookLog      DetailMatch
```

### Key Business Processes

| Process | Tables Involved | Description |
|---------|-----------------|-------------|
| Create Requisition | Requisitions, Detail | User creates purchase request |
| Approval Workflow | Approvals, ApprovalLevels | Route through approval chain |
| Generate PO | PO, PODetailItems | Convert approved reqs to POs |
| Transmit Order | POQueue, POStatus | Send to vendors |
| Batch Processing | Batches, BatchDetail | Process orders in batches |
| Order Books | OrderBooks, OrderBookDetail | Organize by vendor/period |

---

## Requisition Tables

### Requisitions

**Rows:** ~3,516,113 | **Purpose:** Purchase request headers

The Requisitions table is the starting point for all purchases. Users create requisitions which flow through approval and become purchase orders.

| Column | Type | Description |
|--------|------|-------------|
| RequisitionId | int PK | Unique requisition ID |
| RequisitionNumber | varchar | Human-readable number |
| SchoolId | int FK | Ordering school |
| UserId | int FK | Creator |
| BudgetAccountId | int FK | Funding source |
| CategoryId | int FK | Product category |
| StatusId | int FK | Workflow status |
| TotalRequisitionCost | money | Order total |
| DateEntered | datetime | Creation date |
| ApprovalRequired | tinyint | Needs approval? |
| ApprovalLevel | tinyint | Current approval level |

**Status Distribution (from live data):**

| Status | Code | Count | Description |
|--------|------|-------|-------------|
| PO Printed | O | 1,474,907 | Complete - PO generated |
| On Hold | H | 148,171 | User holding/editing |
| Pending Approval | P | 77,525 | Awaiting approver |
| Approved | A | 72,264 | Ready for PO |
| Downloaded | D | 24,457 | Offline processing |
| Rejected | R | 10,081 | Returned to user |

**Relationships:**
- Parent of: Detail, Approvals, RequisitionNotes
- References: School, Users, BudgetAccounts, Category, StatusTable

---

### RequisitionChangeLog

**Rows:** ~3,875,388 | **Purpose:** Requisition audit trail

Tracks all changes to requisitions for compliance and troubleshooting.

| Column | Type | Description |
|--------|------|-------------|
| ChangeLogId | int PK | Unique log entry |
| RequisitionId | int FK | Affected requisition |
| ChangeType | varchar | Type of change |
| OldValue | varchar | Previous value |
| NewValue | varchar | New value |
| ChangeDate | datetime | When changed |
| ChangedBy | int FK | User who changed |

---

### RequisitionNotes

**Rows:** ~24,775 | **Purpose:** Notes attached to requisitions

User-added notes for communication and documentation.

| Column | Type | Description |
|--------|------|-------------|
| RequisitionNoteId | int PK | Unique note ID |
| RequisitionId | int FK | Parent requisition |
| NoteText | varchar | Note content |
| NoteDate | datetime | When added |
| UserId | int FK | Note author |

---

### RequisitionNoteEmails

**Rows:** ~16,173 | **Purpose:** Email notifications for notes

Tracks emails sent for requisition notes.

---

## Order Detail Tables

### Detail

**Rows:** ~56,357,661 | **Purpose:** Line items on requisitions/POs

The Detail table stores every product ordered - the transactional heart of the ordering system.

| Column | Type | Description |
|--------|------|-------------|
| DetailId | int PK | Unique line item ID |
| RequisitionId | int FK | Parent requisition |
| ItemId | int FK | Product ordered |
| Quantity | int | Quantity ordered |
| BidPrice | money | Award/bid price |
| CatalogPrice | money | List price |
| GrossPrice | money | Gross before discount |
| DiscountRate | decimal | Applied discount |
| VendorId | int FK | Fulfilling vendor |
| POId | int FK | Generated PO |
| Active | tinyint | 1=Valid line item |

**Relationships:**
- Parent: Requisitions
- References: Items, Vendors, PO, Awards, Catalog
- Child: PODetailItems, DetailChanges

**Key Business Rules:**
- Detail.BidPrice comes from active Awards/CrossRefs
- One Detail can appear on one PO (POId)
- StatusId mirrors parent Requisition status

---

### DetailChanges

**Rows:** ~26,502,061 | **Purpose:** Line item change history

Audit trail for all detail line modifications.

| Column | Type | Description |
|--------|------|-------------|
| DetailChangeId | int PK | Unique change ID |
| DetailId | int FK | Affected line item |
| ChangeType | varchar | Type of change |
| FieldChanged | varchar | Which field |
| OldValue | varchar | Previous value |
| NewValue | varchar | New value |
| ChangeDate | datetime | When changed |

---

### DetailChangeLog

**Rows:** ~2,924,942 | **Purpose:** Summary change log

Higher-level detail change tracking.

---

### DetailNotifications

**Rows:** ~2,779,173 | **Purpose:** Notification tracking

Tracks notifications sent for detail changes.

---

### DetailMatch

**Rows:** ~105,033 | **Purpose:** Item matching records

Records item matching/substitution decisions.

---

### DetailHold

**Rows:** 1 | **Purpose:** Hold configuration

System configuration for detail holds.

---

## Approval Tables

### Approvals

**Rows:** ~11,345,955 | **Purpose:** Approval records

Records every approval decision in the workflow.

| Column | Type | Description |
|--------|------|-------------|
| ApprovalId | int PK | Unique approval ID |
| RequisitionId | int FK | Approved requisition |
| ApprovalById | int FK | Approving user |
| StatusId | int FK | Decision (Approved/Rejected) |
| ApprovalDate | datetime | When decided |
| Comments | varchar | Approver comments |
| ApprovalLevel | tinyint | Which level |

**Status Values:**
| StatusId | Meaning |
|----------|---------|
| 3 | Approved |
| 4 | Rejected |

---

### ApprovalLevels

**Rows:** 9 | **Purpose:** Approval hierarchy definition

Defines the approval levels and who can approve at each level.

| ApprovalLevelId | Description | Level |
|-----------------|-------------|-------|
| 1 | None | 0 |
| 2 | Principal/Director/Supervisor | 1 |
| 3 | Business Administrator | 2 |
| 9 | Accounting | 3 |
| 4 | Customer Service Rep | 5 |
| 7 | Support Personnel | 7 |
| 8 | EDS Administration | 8 |
| 5 | System Administrator | 9 |
| 6 | Tab House | 11 |

---

### ApprovalsHistory

**Rows:** ~779,612 | **Purpose:** Archived approvals

Historical approval records for completed requisitions.

---

### PendingApprovals

**Purpose:** Queue of items awaiting approval

Real-time queue for approvers to process.

---

## Purchase Order Tables

### PO

**Rows:** ~3,762,924 | **Purpose:** Purchase order headers

Generated purchase orders sent to vendors.

| Column | Type | Description |
|--------|------|-------------|
| POId | int PK | Unique PO ID |
| PONumber | varchar | Human-readable PO number |
| VendorId | int FK | Vendor receiving order |
| DistrictId | int FK | Ordering district |
| PODate | datetime | Order date |
| TotalAmount | money | Order total |
| StatusId | int FK | PO status |
| TransmitDate | datetime | When sent to vendor |

**Relationships:**
- Parent of: PODetailItems, POStatus
- References: Vendors, District

---

### PODetailItems

**Rows:** ~47,234,474 | **Purpose:** PO line items

Links Detail records to POs - the bridge between requisitions and orders.

| Column | Type | Description |
|--------|------|-------------|
| PODetailItemId | int PK | Unique ID |
| POId | int FK | Parent PO |
| DetailId | int FK | Source detail line |
| Quantity | int | Quantity on PO |
| UnitPrice | money | Price per unit |
| ExtendedPrice | money | Quantity × Price |

**Relationships:**
- Parent: PO
- References: Detail

---

### POStatus

**Rows:** ~406,281 | **Purpose:** PO status history

Tracks PO status changes through fulfillment.

| Column | Type | Description |
|--------|------|-------------|
| POStatusId | int PK | Unique status ID |
| POId | int FK | Affected PO |
| StatusId | int FK | New status |
| StatusDate | datetime | When changed |
| UserId | int FK | Who changed |

---

### POQueue

**Rows:** ~26,783 | **Purpose:** PO transmission queue

POs waiting to be transmitted to vendors.

---

### POQueueItems

**Rows:** ~398,187 | **Purpose:** Queue item details

Individual items in the PO queue.

---

### POLayouts

**Rows:** ~632 | **Purpose:** PO print layouts

Print format definitions for POs.

---

### POLayoutDetail

**Rows:** ~6,841 | **Purpose:** Layout field details

Field definitions for PO layouts.

---

### POLayoutFields

**Rows:** 56 | **Purpose:** Layout field types

Types of fields available in layouts.

---

### POPageSummary

**Rows:** ~73,456 | **Purpose:** PO page summaries

Page-level summaries for multi-page POs.

---

### POTemp / POTempDetails

**Rows:** ~37 / ~4,014 | **Purpose:** Temporary PO data

Staging tables for PO generation.

---

### POPrintTaggedPOFile

**Rows:** ~120,948 | **Purpose:** Print job tracking

Tracks printed PO files.

---

### POStatusTable

**Rows:** 0 | **Purpose:** PO status definitions

Status lookup (currently empty - uses StatusTable).

---

## Batch Processing Tables

### Batches

**Rows:** ~14,507 | **Purpose:** Batch job headers

Defines batch processing runs.

| Column | Type | Description |
|--------|------|-------------|
| BatchId | int PK | Unique batch ID |
| BatchDate | datetime | Processing date |
| DistrictId | int FK | Target district |
| BatchType | int | Type of batch |
| Status | varchar | Batch status |

---

### BatchDetail

**Rows:** ~9,080,322 | **Purpose:** Batch line items

Items included in batch processing.

| Column | Type | Description |
|--------|------|-------------|
| BatchDetailId | int PK | Unique ID |
| BatchId | int FK | Parent batch |
| DetailId | int FK | Source detail |
| ProcessedDate | datetime | When processed |

---

### BatchBook

**Rows:** ~217,611 | **Purpose:** Batch book records

Books generated from batch processing.

---

### BatchDetailInserts

**Rows:** ~1,176 | **Purpose:** Batch insert tracking

Tracks items inserted during batch.

---

## Order Book Tables

### OrderBooks

**Rows:** ~31,091 | **Purpose:** Order book headers

Order books organize orders by vendor/period.

| Column | Type | Description |
|--------|------|-------------|
| OrderBookId | int PK | Unique book ID |
| VendorId | int FK | Target vendor |
| DistrictId | int FK | District |
| BookDate | datetime | Book date |
| Status | varchar | Book status |
| OrderBookTypeId | int FK | Book type |

---

### OrderBookDetail

**Rows:** ~225,434,158 | **Purpose:** Order book line items

Individual items in order books - the largest Orders domain table.

| Column | Type | Description |
|--------|------|-------------|
| OrderBookDetailId | int PK | Unique ID |
| OrderBookId | int FK | Parent book |
| ItemId | int FK | Product |
| Quantity | int | Quantity |
| Price | money | Unit price |
| ExtendedAmount | money | Total |

---

### OrderBookLog

**Rows:** ~474,300 | **Purpose:** Order book activity log

Audit trail for order book operations.

---

### OrderBookTypes

**Rows:** 12 | **Purpose:** Book type definitions

Types of order books.

---

### OrderBookAlwaysAdd

**Rows:** 9 | **Purpose:** Auto-add configuration

Items automatically added to order books.

---

## Supporting Tables

### PostCatalogHeader / PostCatalogDetail

**Rows:** ~3,328 / ~39,111 | **Purpose:** Post-catalog processing

Handles catalog updates after orders.

---

## Entity Relationship Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         ORDERS DOMAIN RELATIONSHIPS                          │
└─────────────────────────────────────────────────────────────────────────────┘

                    ┌──────────────┐
                    │    Users     │
                    └──────────────┘
                           │
              ┌────────────┼────────────┐
              ▼            ▼            ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐
        │  School  │  │Approvals │  │ Budgets  │
        └──────────┘  └──────────┘  └──────────┘
              │            │            │
              └────────────┼────────────┘
                           ▼
                    ┌──────────────┐
                    │ Requisitions │──────────────┐
                    └──────────────┘              │
                           │                      │
              ┌────────────┼────────────┐         │
              ▼            ▼            ▼         ▼
        ┌──────────┐  ┌──────────┐  ┌──────────┐ ┌──────────┐
        │  Detail  │  │ ReqNotes │  │ ReqChange│ │  Batch   │
        └──────────┘  └──────────┘  │   Log    │ │ Detail   │
              │                     └──────────┘ └──────────┘
              │
              ├─────────────────────────────┐
              ▼                             ▼
        ┌──────────┐                  ┌──────────┐
        │   PO     │◄─────────────────│PODetail  │
        └──────────┘                  │  Items   │
              │                       └──────────┘
              ▼
        ┌──────────┐
        │ POStatus │
        └──────────┘
              │
              ▼
        ┌──────────┐
        │ Vendors  │
        └──────────┘
```

---

## Common Queries

### Get requisitions pending approval
```sql
SELECT r.RequisitionId, r.RequisitionNumber,
       u.UserName AS Creator, r.TotalRequisitionCost,
       s.Name AS Status
FROM Requisitions r
JOIN Users u ON r.UserId = u.UserId
JOIN StatusTable s ON r.StatusId = s.StatusId
WHERE r.StatusId = 2 -- Pending Approval
  AND r.Active = 1
ORDER BY r.DateEntered;
```

### Get PO with line items
```sql
SELECT po.PONumber, v.Name AS Vendor,
       po.PODate, po.TotalAmount,
       d.Description, pdi.Quantity, pdi.UnitPrice
FROM PO po
JOIN Vendors v ON po.VendorId = v.VendorId
JOIN PODetailItems pdi ON po.POId = pdi.POId
JOIN Detail d ON pdi.DetailId = d.DetailId
WHERE po.POId = @POId;
```

### Approval history for requisition
```sql
SELECT a.ApprovalDate, u.UserName AS Approver,
       s.Name AS Decision, al.Description AS Level,
       a.Comments
FROM Approvals a
JOIN Users u ON a.ApprovalById = u.UserId
JOIN StatusTable s ON a.StatusId = s.StatusId
JOIN ApprovalLevels al ON a.ApprovalLevel = al.ApprovalLevel
WHERE a.RequisitionId = @RequisitionId
ORDER BY a.ApprovalDate;
```

---

## Data Flow Summary

```
User creates Requisition
        │
        ▼
Detail records created (line items)
        │
        ▼
Status = "On Hold" (H)
        │
        ▼
User submits ──► Status = "Pending Approval" (P)
        │
        ▼
Approval created in Approvals table
        │
        ├── Approved ──► Status = "Approved" (A)
        │                     │
        │                     ▼
        │              PO generated
        │                     │
        │                     ▼
        │              PODetailItems link Detail to PO
        │                     │
        │                     ▼
        │              Status = "PO Printed" (O)
        │                     │
        │                     ▼
        │              PO transmitted to Vendor
        │
        └── Rejected ──► Status = "Rejected" (R)
                              │
                              ▼
                        Returns to user
```

---

## Performance Considerations

| Table | Size | Index Strategy |
|-------|------|----------------|
| Detail | 56M | Clustered on DetailId, NC on RequisitionId, ItemId, VendorId |
| OrderBookDetail | 225M | Partition by OrderBookId or date, NC on ItemId |
| PODetailItems | 47M | NC on POId, DetailId |
| Approvals | 11M | NC on RequisitionId, StatusId |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial Orders domain documentation | Phase 2 Documentation |
