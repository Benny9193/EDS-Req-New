# Workflow: Requisition to Purchase Order

[Home](../../index.md) > [Business](../index.md) > [Workflows](index.md) > Requisition to PO

---

## Overview

This workflow covers the complete procurement cycle from creating a purchase request through issuing a purchase order to a vendor.

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         REQUISITION TO PO WORKFLOW                          │
│                                                                             │
│    ┌──────────┐                                                            │
│    │   User   │                                                            │
│    └────┬─────┘                                                            │
│         │                                                                   │
│         ▼                                                                   │
│    ┌──────────┐     ┌──────────┐     ┌──────────┐     ┌──────────┐        │
│    │  Create  │────▶│  Select  │────▶│  Assign  │────▶│  Submit  │        │
│    │  Request │     │  Items   │     │  Budget  │     │          │        │
│    └──────────┘     └──────────┘     └──────────┘     └────┬─────┘        │
│                                                             │              │
│    ┌────────────────────────────────────────────────────────┘              │
│    │                                                                       │
│    ▼                                                                       │
│    ┌──────────┐     ┌──────────┐     ┌──────────┐                         │
│    │  Route   │────▶│ Approver │────▶│ Decision │                         │
│    │  Approval│     │  Review  │     │          │                         │
│    └──────────┘     └──────────┘     └────┬─────┘                         │
│                                           │                                │
│                     ┌─────────────────────┼─────────────────────┐          │
│                     │                     │                     │          │
│                     ▼                     ▼                     ▼          │
│               ┌──────────┐         ┌──────────┐         ┌──────────┐      │
│               │ Approved │         │ Rejected │         │ Returned │      │
│               └────┬─────┘         └────┬─────┘         └────┬─────┘      │
│                    │                    │                    │            │
│                    ▼                    ▼                    ▼            │
│               ┌──────────┐         ┌──────────┐         ┌──────────┐      │
│               │ Generate │         │  Notify  │         │  Revise  │      │
│               │    PO    │         │   User   │         │  Request │      │
│               └────┬─────┘         └──────────┘         └──────────┘      │
│                    │                                                       │
│                    ▼                                                       │
│               ┌──────────┐     ┌──────────┐     ┌──────────┐             │
│               │  Send    │────▶│  Vendor  │────▶│  Track   │             │
│               │ to Vendor│     │   Acks   │     │ Delivery │             │
│               └──────────┘     └──────────┘     └──────────┘             │
│                                                                           │
└───────────────────────────────────────────────────────────────────────────┘
```

---

## Step 1: Create Requisition

### User Action
1. Log into EDS
2. Navigate to "New Requisition"
3. Select school/location
4. Enter delivery information
5. Set "Date Needed"

### System Actions
- Creates Requisition record (Status: Draft)
- Assigns RequisitionNumber
- Records UserId, SchoolId, DateCreated

### Database Impact
```sql
INSERT INTO Requisitions (UserId, SchoolId, DateCreated, Status, ...)
VALUES (@UserId, @SchoolId, GETDATE(), 'Draft', ...)
```

---

## Step 2: Select Items

### User Action
1. Search for items in catalog
2. Select vendor (or let system choose based on award)
3. Enter quantity
4. Add to requisition

### System Actions
- Creates Detail record for each line
- **Fires `trig_DetailUpdate`** (potential blocking)
- Looks up pricing from CrossRefs
- Calculates extended price

### Database Impact
```sql
INSERT INTO Detail (RequisitionId, ItemId, CrossRefId, Quantity, ...)
VALUES (@ReqId, @ItemId, @CrossRefId, @Qty, ...)

-- Trigger then fires and performs:
--   - Price lookup from CrossRefs
--   - Item remapping from BidMappedItems
--   - Vendor assignment
--   - Total calculation
```

### Performance Note
See [KI-003: trig_DetailUpdate Blocking](../../performance/known-issues/trigger-blocking.md) for trigger impact during bulk operations.

---

## Step 3: Assign Budget

### User Action
1. Select account code for each line
2. Or accept default account codes
3. System validates funds availability

### System Actions
- Validates account code exists and is active
- Checks available budget
- Warns if over budget (may still allow submission)

### Budget Validation
```sql
SELECT b.AccountCode, b.AvailableBalance,
       b.AvailableBalance - @LineAmount as Remaining
FROM Budgets b
WHERE b.AccountCode = @AccountCode
  AND b.FiscalYear = @CurrentFiscalYear
```

---

## Step 4: Submit Requisition

### User Action
1. Review requisition summary
2. Add notes/justification if needed
3. Click "Submit"

### System Actions
- Updates Status to 'Submitted'
- Calculates TotalAmount
- Determines approval routing
- Sends notification to first approver

### Database Impact
```sql
UPDATE Requisitions
SET Status = 'Submitted',
    TotalAmount = (SELECT SUM(ExtendedPrice) FROM Detail WHERE RequisitionId = @ReqId),
    DateSubmitted = GETDATE()
WHERE RequisitionId = @ReqId
```

---

## Step 5: Approval Routing

### Routing Logic
System determines approvers based on:
1. Total amount (threshold-based)
2. School/department
3. Item category (some require special approval)
4. Account code

### Approval Levels

| Level | Approver | Threshold |
|-------|----------|-----------|
| 1 | Department Head | Any |
| 2 | Principal | > $500 |
| 3 | Purchasing | > $2,500 |
| 4 | Finance Director | > $10,000 |
| 5 | Superintendent | > $50,000 |
| 6 | Board | > $100,000 |

### Notification
Email sent to approver with:
- Requisition summary
- Line items
- Total amount
- Link to approve/reject

---

## Step 6: Approver Review

### Approver Actions
1. Review requisition details
2. Check budget impact
3. Verify business need
4. Approve, Reject, or Return for modification

### Decision Options

| Action | Result |
|--------|--------|
| **Approve** | Routes to next level or final |
| **Reject** | Ends workflow, notifies requestor |
| **Return** | Sends back for revision |
| **Request Info** | Pauses for additional details |

### Approval Query
```sql
-- Check if user can approve this requisition
SELECT 1
FROM ApprovalRules ar
WHERE ar.RoleId IN (SELECT RoleId FROM UserRoles WHERE UserId = @ApproverId)
  AND ar.MinAmount <= @RequisitionAmount
  AND ar.MaxAmount >= @RequisitionAmount
  AND ar.SchoolId IN (@SchoolId, NULL)  -- NULL = all schools
```

---

## Step 7: Generate PO

### Trigger
- Final approval received
- Or auto-generation for approved requisitions

### System Actions
1. Creates PurchaseOrder record
2. Groups lines by vendor (may create multiple POs)
3. Copies Detail to PODetail
4. Encumbers budget
5. Assigns PONumber

### PO Generation
```sql
-- Create PO for each vendor
INSERT INTO PurchaseOrders (RequisitionId, VendorId, PODate, TotalAmount, ...)
SELECT @ReqId, VendorId, GETDATE(), SUM(ExtendedPrice), ...
FROM Detail d
JOIN CrossRefs cr ON d.CrossRefId = cr.CrossRefId
WHERE d.RequisitionId = @ReqId
GROUP BY cr.VendorId

-- Copy line items
INSERT INTO PODetail (POId, DetailId, Quantity, UnitPrice, ...)
SELECT @POId, DetailId, Quantity, UnitPrice, ...
FROM Detail
WHERE RequisitionId = @ReqId
  AND VendorId = @POVendorId
```

---

## Step 8: Send to Vendor

### Transmission Methods
- **Email:** PDF attachment
- **EDI:** Electronic data interchange
- **Punch-out:** Return to vendor system
- **Fax:** Automated fax

### System Actions
1. Generates PO document
2. Transmits to vendor
3. Updates Status to 'Sent'
4. Logs transmission

---

## Step 9: Track Delivery

### Subsequent Steps
After PO is sent:
1. Vendor acknowledges receipt
2. Vendor ships items
3. School receives delivery
4. Invoice received
5. Three-way match
6. Payment processed

See [Purchase Orders](../entities/purchase-orders.md) for detailed receiving workflow.

---

## Exception Handling

| Exception | Resolution |
|-----------|------------|
| Over budget | Request budget transfer or exception approval |
| Item unavailable | Substitute or wait |
| Vendor inactive | Select alternate vendor |
| Approval timeout | Escalate or reassign |
| Price changed | Update PO or negotiate |

---

## Performance Considerations

### High-Volume Scenarios

| Scenario | Risk | Mitigation |
|----------|------|------------|
| Back-to-school bulk orders | Trigger blocking | Batch in smaller groups |
| Month-end rush | Approval queue delays | Expedite review |
| Year-end closing | System load | Schedule off-hours |

### Known Issues
- [trig_DetailUpdate](../../performance/known-issues/trigger-blocking.md) - can block during bulk saves
- [CrossRef lookups](../../performance/known-issues/crossref-blocking.md) - blocked during catalog operations

---

## See Also

- [Requisitions](../entities/requisitions.md) - Entity details
- [Purchase Orders](../entities/purchase-orders.md) - PO entity
- [Budget & Approval](budget-approval.md) - Approval workflow
- [Trigger Blocking](../../performance/known-issues/trigger-blocking.md)

