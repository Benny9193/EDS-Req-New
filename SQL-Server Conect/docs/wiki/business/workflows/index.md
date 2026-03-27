# Business Workflows

[Home](../../index.md) > [Business](../index.md) > Workflows

---

## Overview

EDS supports several core business workflows that manage the procurement lifecycle from initial request through payment.

---

## Core Workflows

| Workflow | Description | Key Steps |
|----------|-------------|-----------|
| [Requisition to PO](requisition-to-po.md) | End-to-end procurement | Request → Approve → Order |
| [Vendor Bidding](vendor-bidding.md) | Competitive bidding | Solicit → Evaluate → Award |
| [Budget & Approval](budget-approval.md) | Financial controls | Validate → Route → Approve |

---

## Workflow Overview Diagram

```
                     ┌─────────────────────────────────────────────┐
                     │            VENDOR BIDDING                   │
                     │  Create Bid → Publish → Evaluate → Award    │
                     └────────────────────┬────────────────────────┘
                                          │
                                          ▼
┌──────────────────────────────────────────────────────────────────────────┐
│                       REQUISITION TO PO                                   │
│                                                                          │
│  ┌─────────┐    ┌──────────┐    ┌──────────┐    ┌────────┐    ┌───────┐ │
│  │ Create  │───▶│  Submit  │───▶│ Approve  │───▶│Generate│───▶│ Send  │ │
│  │   Req   │    │   Req    │    │   Req    │    │   PO   │    │  PO   │ │
│  └─────────┘    └──────────┘    └──────────┘    └────────┘    └───────┘ │
│       │                              │                             │     │
│       │                              ▼                             │     │
│       │         ┌─────────────────────────────────┐                │     │
│       └────────▶│     BUDGET & APPROVAL           │◀───────────────┘     │
│                 │  Check Funds → Route → Approve  │                      │
│                 └─────────────────────────────────┘                      │
└──────────────────────────────────────────────────────────────────────────┘
                                          │
                                          ▼
                     ┌─────────────────────────────────────────────┐
                     │            RECEIVING & PAYMENT              │
                     │    Receive → Invoice → 3-Way Match → Pay    │
                     └─────────────────────────────────────────────┘
```

---

## Workflow Participants

### By Role

| Role | Workflows |
|------|-----------|
| Requestor | Creates requisitions |
| Approver | Reviews and approves |
| Buyer | Generates POs, manages bids |
| Receiver | Confirms receipt |
| Finance | Manages budgets, payments |
| Vendor | Responds to bids, fulfills orders |

### System Interactions

| System | Workflow Step |
|--------|---------------|
| Budgeting | Validates funds at request |
| Bidding | Provides contract pricing |
| Catalog | Item selection and pricing |
| Notifications | Email alerts at each step |

---

## Workflow Timing

### Typical Processing Times

| Step | Target Time |
|------|-------------|
| Create requisition | Same day |
| First approval | 1 business day |
| Full approval | 3 business days |
| Generate PO | Same day after approval |
| Vendor acknowledgment | 1-2 business days |
| Delivery | Per contract terms |

### Peak Periods

| Period | Activity |
|--------|----------|
| August-September | Back-to-school ordering |
| December | Holiday break prep |
| May-June | End of fiscal year |
| Month-end | Budget reconciliation |

---

## Workflow Status Tracking

### Requisition States

```
Draft ──► Submitted ──► Pending ──► Approved ──► Converted
                           │
                           └──► Rejected ──► Cancelled
```

### PO States

```
Generated ──► Sent ──► Acknowledged ──► Shipped ──► Received ──► Paid
                                           │
                                           └──► Partial ──► Backordered
```

---

## Notifications

### Email Triggers

| Event | Recipient |
|-------|-----------|
| Requisition submitted | Approver |
| Requisition approved | Requestor, Buyer |
| Requisition rejected | Requestor |
| PO generated | Buyer, Vendor |
| PO acknowledged | Buyer |
| Items shipped | Receiver |
| Invoice received | Finance |

---

## Exception Handling

### Common Exceptions

| Exception | Resolution Path |
|-----------|-----------------|
| Over budget | Modify request or request exception |
| Vendor unavailable | Select alternate vendor |
| Item discontinued | Substitute item |
| Price changed | Update PO or cancel |
| Partial shipment | Accept partial or reorder |

---

## Performance Impact

Certain workflow steps can cause database blocking:

| Step | Potential Issue |
|------|-----------------|
| Save requisition lines | [trig_DetailUpdate blocking](../../performance/known-issues/trigger-blocking.md) |
| Lookup item prices | [CrossRef blocking](../../performance/known-issues/crossref-blocking.md) |
| Bulk imports | Cascading blocks |

---

## See Also

- [Business Entities](../entities/index.md) - Data structures
- [Performance Overview](../../performance/index.md) - System performance
- [Troubleshooting](../../troubleshooting/index.md) - Problem resolution

