# Requisitions

[Home](../../index.md) > [Business](../index.md) > [Entities](index.md) > Requisitions

---

## Overview

A Requisition is a formal request to purchase goods or services. It's the starting point of the procurement process and must be approved before becoming a Purchase Order.

---

## Requisition Lifecycle

```
Draft → Submitted → Pending Approval → Approved → Converted to PO
  │         │              │              │
  │         │              ▼              ▼
  │         │          Rejected       Partially
  │         │              │          Converted
  │         ▼              │              │
  └──► Cancelled ◄─────────┴──────────────┘
```

---

## Key Tables

### Requisitions Table

| Field | Description |
|-------|-------------|
| RequisitionId | Primary key |
| RequisitionNumber | Display number |
| UserId | Requestor |
| SchoolId | Originating school |
| DateCreated | Creation timestamp |
| DateNeeded | Required by date |
| Status | Current status |
| TotalAmount | Sum of line items |
| ApprovalLevel | Current approval stage |
| Notes | Comments |

### Detail Table (Line Items)

| Field | Description |
|-------|-------------|
| DetailId | Primary key |
| RequisitionId | Parent requisition |
| ItemId | Item reference |
| CrossRefId | Vendor catalog item |
| Quantity | Amount requested |
| UnitPrice | Price per unit |
| ExtendedPrice | Quantity × Price |
| AccountCode | Budget code |
| Description | Item description |

---

## Status Values

| Status | Description |
|--------|-------------|
| Draft | Being edited, not submitted |
| Submitted | Sent for approval |
| Pending | Awaiting approver action |
| Approved | Ready for PO generation |
| Partially Approved | Some lines approved |
| Rejected | Denied by approver |
| Cancelled | Withdrawn by requestor |
| Converted | Became Purchase Order |

---

## Detail Line Processing

### The Detail Trigger Issue

When Detail lines are inserted or updated, `trig_DetailUpdate` fires and performs extensive operations:

```
INSERT/UPDATE Detail
    │
    ▼
trig_DetailUpdate fires
    │
    ├── Look up CrossRef pricing
    ├── Remap items via BidMappedItems
    ├── Update vendor information
    ├── Calculate extended prices
    └── Update requisition totals
```

**Known Issue:** This trigger can cause significant blocking during bulk operations. See [KI-003: Trigger Blocking](../../performance/known-issues/trigger-blocking.md).

---

## Approval Workflow

### Approval Levels

| Level | Approver | Threshold |
|-------|----------|-----------|
| 1 | Department Head | Any amount |
| 2 | Principal | > $500 |
| 3 | Purchasing | > $2,500 |
| 4 | Finance Director | > $10,000 |
| 5 | Superintendent | > $50,000 |

### Approval Routing

```
Requestor creates requisition
    │
    ▼
Amount ≤ $500? ─────────────► Level 1 Approver
    │                               │
    No                              │ Approve
    │                               │
    ▼                               ▼
Amount ≤ $2,500? ──────────► Level 2 Approver
    │                               │
    ...continues up chain...        │
    │                               ▼
    └──────────────────────► Final Approval
                                    │
                                    ▼
                            Convert to PO
```

---

## Common Queries

### Find Pending Requisitions
```sql
SELECT r.RequisitionNumber, r.DateCreated, r.TotalAmount,
       u.FirstName + ' ' + u.LastName as Requestor,
       s.SchoolName
FROM Requisitions r
JOIN Users u ON r.UserId = u.UserId
JOIN Schools s ON r.SchoolId = s.SchoolId
WHERE r.Status = 'Pending'
ORDER BY r.DateCreated
```

### Get Requisition with Details
```sql
SELECT d.DetailId, d.Description, d.Quantity,
       d.UnitPrice, d.ExtendedPrice, d.AccountCode,
       cr.VendorSKU, v.VendorName
FROM Detail d
LEFT JOIN CrossRefs cr ON d.CrossRefId = cr.CrossRefId
LEFT JOIN Vendors v ON cr.VendorId = v.VendorId
WHERE d.RequisitionId = @RequisitionId
ORDER BY d.DetailId
```

### Requisition Visibility
```sql
-- User-facing query that checks permissions
SELECT r.*
FROM Requisitions r
WHERE uf_RequisitionIsVisible(r.RequisitionId, @UserId) = 1
```

**Note:** `uf_RequisitionIsVisible` is a UDF that can become a blocking victim during high load.

---

## Performance Considerations

### High-Volume Periods
- **Back-to-School (Aug-Sep):** Highest requisition volume
- **Month-End:** Budget reconciliation activity
- **Year-End:** Fiscal year closing

### Blocking Hotspots

| Operation | Risk Level | Mitigation |
|-----------|------------|------------|
| Bulk Detail INSERT | High | Process in batches |
| CrossRef lookup | Medium | Use NOLOCK hints |
| uf_RequisitionIsVisible | Medium | Optimize indexes |

---

## Integration Points

| System | Integration |
|--------|-------------|
| Budgeting | Account code validation |
| Inventory | Item availability check |
| Bidding | Award price lookup |
| Vendors | Catalog pricing |

---

## See Also

- [Purchase Orders](purchase-orders.md) - Next step after approval
- [Catalogs & Items](catalogs-items.md) - Item selection
- [Workflow: Requisition to PO](../workflows/requisition-to-po.md)
- [Trigger Blocking Issue](../../performance/known-issues/trigger-blocking.md)
- [Schema: Orders & Purchasing](../../schema/by-domain/orders-purchasing.md)

