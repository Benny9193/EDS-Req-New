# Purchase Orders

[Home](../../index.md) > [Business](../index.md) > [Entities](index.md) > Purchase Orders

---

## Overview

A Purchase Order (PO) is an official document authorizing a vendor to supply goods or services. POs are generated from approved requisitions and represent a legal commitment to pay.

---

## PO Lifecycle

```
Approved Requisition
    │
    ▼
PO Generated ──► Sent to Vendor ──► Acknowledged
    │                                    │
    │                                    ▼
    │                              Shipped/Partial
    │                                    │
    │                                    ▼
    │                               Received
    │                                    │
    │                                    ▼
    └────────────────────────────► Invoiced ──► Paid ──► Closed
```

---

## Key Tables

### PurchaseOrders Table

| Field | Description |
|-------|-------------|
| POId | Primary key |
| PONumber | Display number |
| RequisitionId | Source requisition |
| VendorId | Supplier |
| ShipToSchoolId | Delivery location |
| PODate | Issue date |
| TotalAmount | Order total |
| Status | Current status |
| ShipVia | Shipping method |
| Terms | Payment terms |

### PODetail Table

| Field | Description |
|-------|-------------|
| PODetailId | Primary key |
| POId | Parent PO |
| DetailId | Source requisition line |
| Quantity | Order quantity |
| UnitPrice | Agreed price |
| QuantityReceived | Received amount |
| QuantityInvoiced | Invoiced amount |

---

## Status Values

| Status | Description |
|--------|-------------|
| Generated | Created, not sent |
| Sent | Transmitted to vendor |
| Acknowledged | Vendor confirmed |
| Partial Shipment | Some items shipped |
| Fully Shipped | All items shipped |
| Partial Receipt | Some items received |
| Received | All items received |
| Invoiced | Invoice received |
| Paid | Payment processed |
| Closed | Complete and archived |
| Cancelled | Order cancelled |

---

## PO Generation

### From Single Requisition
One requisition with one vendor → One PO

### From Multiple Requisitions
Multiple requisitions to same vendor can be consolidated:

```
Requisition A (Vendor: Staples)
    │
    ├── Line 1: Paper
    └── Line 2: Pens
                            ┌─────────────────┐
Requisition B (Staples)     │                 │
    │                   ────┼──► PO to Staples│
    └── Line 1: Folders     │                 │
                            └─────────────────┘
```

### Split PO (Multiple Vendors)
One requisition with multiple vendors → Multiple POs:

```
Requisition C
    │
    ├── Line 1 (Vendor: Staples) ──► PO-001 to Staples
    └── Line 2 (Vendor: Dell)    ──► PO-002 to Dell
```

---

## Common Queries

### Open POs by Vendor
```sql
SELECT po.PONumber, po.PODate, po.TotalAmount,
       v.VendorName, po.Status
FROM PurchaseOrders po
JOIN Vendors v ON po.VendorId = v.VendorId
WHERE po.Status NOT IN ('Closed', 'Cancelled')
ORDER BY v.VendorName, po.PODate
```

### PO with Line Items
```sql
SELECT pod.LineNumber, pod.Description,
       pod.Quantity, pod.UnitPrice,
       pod.QuantityReceived,
       (pod.Quantity - pod.QuantityReceived) as Outstanding
FROM PODetail pod
WHERE pod.POId = @POId
ORDER BY pod.LineNumber
```

### Unshipped Items
```sql
SELECT po.PONumber, v.VendorName,
       pod.Description, pod.Quantity,
       pod.QuantityReceived
FROM PurchaseOrders po
JOIN PODetail pod ON po.POId = pod.POId
JOIN Vendors v ON po.VendorId = v.VendorId
WHERE pod.QuantityReceived < pod.Quantity
  AND po.Status NOT IN ('Cancelled', 'Closed')
ORDER BY po.PODate
```

---

## Receiving Process

### Three-Way Match
1. **PO** - What was ordered
2. **Packing Slip** - What was shipped
3. **Invoice** - What vendor bills

All three must match before payment.

### Partial Receipt
When not all items arrive:
1. Record received quantities
2. Status changes to "Partial Receipt"
3. Backorder created for remaining items
4. Or, short-ship accepted and PO closed

### Over-Shipment
If more items arrive than ordered:
1. Accept and adjust PO quantity
2. Or refuse overage and return to vendor

---

## Budget Impact

### Encumbrance
When PO is generated:
- Budget is **encumbered** (reserved)
- Reduces available balance
- Does not reduce actual balance

### Expenditure
When invoice is paid:
- Encumbrance is released
- **Expenditure** recorded
- Actual balance reduced

```
Budget: $10,000
    │
    ├── PO Generated ($500) ──► Encumbered: $500
    │                           Available: $9,500
    │
    └── Invoice Paid ($500) ──► Encumbered: $0
                                Expenditure: $500
                                Available: $9,500
```

---

## Transmission Methods

| Method | Description |
|--------|-------------|
| Email | PDF sent to vendor email |
| EDI | Electronic Data Interchange |
| Fax | Fax to vendor number |
| Punch-out | Direct vendor integration |
| Manual | Print and mail |

---

## PO Amendments

### Change Order
When modifying an existing PO:
1. Add or remove lines
2. Change quantities
3. Update pricing
4. Modify shipping

Each amendment is tracked with version number.

### Cancellation
Entire PO can be cancelled if:
- Items no longer needed
- Vendor cannot fulfill
- Budget issue discovered

---

## See Also

- [Requisitions](requisitions.md) - Source documents
- [Vendors](vendors.md) - Suppliers
- [Workflow: Requisition to PO](../workflows/requisition-to-po.md)
- [Schema: Orders & Purchasing](../../schema/by-domain/orders-purchasing.md)

