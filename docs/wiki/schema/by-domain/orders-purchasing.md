# Schema: Orders & Purchasing Domain

[Home](../../index.md) > [Schema](../index.md) > [By Domain](index.md) > Orders & Purchasing

---

## Overview

The orders domain contains 45 tables managing the complete procurement lifecycle from requisitions through purchase orders.

---

## Table Count: 45

### Requisition Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| Requisitions | Purchase request header | RequisitionId, RequisitionNumber, UserId, Status |
| Detail | Requisition line items | DetailId, RequisitionId, ItemId, Quantity, UnitPrice |
| RequisitionApprovals | Approval history | ApprovalId, RequisitionId, ApproverId, Action |
| RequisitionNotes | Comments/notes | NoteId, RequisitionId, NoteText |
| RequisitionAttachments | File uploads | AttachmentId, RequisitionId, FilePath |

### Purchase Order Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| PurchaseOrders | PO header | POId, PONumber, VendorId, Status |
| PODetail | PO line items | PODetailId, POId, DetailId, Quantity |
| POShipments | Shipping info | ShipmentId, POId, ShipDate |
| POReceipts | Receiving records | ReceiptId, PODetailId, QuantityReceived |
| POInvoices | Invoice header | InvoiceId, POId, InvoiceNumber, Amount |
| POPayments | Payment records | PaymentId, InvoiceId, PaymentDate |

### Supporting Tables

| Table | Purpose |
|-------|---------|
| RequisitionStatuses | Status lookup |
| POStatuses | PO status lookup |
| ShippingMethods | Ship via options |
| PaymentTerms | Net 30, etc. |

---

## Key Relationships

```
Requisitions (1) ──────► (N) Detail ──────► (1) CrossRefs
     │                        │
     │                        └──────► (1) Items
     │
     ├──────► (N) RequisitionApprovals
     │
     └──────► (N) PurchaseOrders (1) ──────► (N) PODetail
                       │                         │
                       │                         └──► POReceipts
                       │
                       └──────► (N) POInvoices ──► POPayments
```

---

## Critical Table: Detail

The Detail table is central to requisition processing and is involved in critical blocking issues.

### Schema
| Column | Type | Description |
|--------|------|-------------|
| DetailId | INT | Primary key |
| RequisitionId | INT | Parent requisition |
| ItemId | INT | Internal item reference |
| CrossRefId | INT | Vendor catalog item |
| Quantity | DECIMAL | Requested quantity |
| UnitPrice | DECIMAL | Price per unit |
| ExtendedPrice | DECIMAL | Qty × Price |
| AccountCode | VARCHAR | Budget account |
| Description | VARCHAR | Item description |
| VendorId | INT | Assigned vendor |
| OriginalItemId | INT | If item was remapped |

### Critical Trigger: trig_DetailUpdate

This trigger fires on every INSERT/UPDATE to Detail:

```sql
CREATE TRIGGER [dbo].[trig_DetailUpdate] ON [dbo].[Detail]
AFTER INSERT, UPDATE NOT FOR REPLICATION
AS
SET NOCOUNT ON

-- Remap items based on awards
UPDATE Detail
SET ItemId = BidMappedItems.NewItemId,
    OriginalItemId = COALESCE(Detail.OriginalItemId, BidMappedItems.OrigItemId)
FROM inserted
JOIN BidMappedItems ON ...

-- Update pricing from CrossRefs
UPDATE Detail
SET BidPrice = CrossRefs.CatalogPrice,
    CatalogPage = CrossRefs.Page
FROM inserted
JOIN CrossRefs ON ...
```

**Known Issue:** This trigger causes blocking. See [KI-003](../../performance/known-issues/trigger-blocking.md).

---

## Common Queries

### Requisitions by Status
```sql
SELECT Status, COUNT(*) as ReqCount,
       SUM(TotalAmount) as TotalValue
FROM Requisitions
WHERE DateCreated > DATEADD(month, -3, GETDATE())
GROUP BY Status
ORDER BY ReqCount DESC
```

### Requisition with Details
```sql
SELECT r.RequisitionNumber, r.Status, r.TotalAmount,
       u.FirstName + ' ' + u.LastName as Requestor,
       d.Description, d.Quantity, d.UnitPrice, d.ExtendedPrice,
       v.VendorName
FROM Requisitions r
JOIN Users u ON r.UserId = u.UserId
JOIN Detail d ON r.RequisitionId = d.RequisitionId
LEFT JOIN Vendors v ON d.VendorId = v.VendorId
WHERE r.RequisitionId = @RequisitionId
```

### Open POs by Vendor
```sql
SELECT v.VendorName, COUNT(po.POId) as OpenPOs,
       SUM(po.TotalAmount) as TotalValue
FROM PurchaseOrders po
JOIN Vendors v ON po.VendorId = v.VendorId
WHERE po.Status NOT IN ('Closed', 'Cancelled')
GROUP BY v.VendorId, v.VendorName
ORDER BY TotalValue DESC
```

### Unreceived Items
```sql
SELECT po.PONumber, d.Description,
       pod.Quantity, pod.QuantityReceived,
       pod.Quantity - pod.QuantityReceived as Outstanding
FROM PurchaseOrders po
JOIN PODetail pod ON po.POId = pod.POId
JOIN Detail d ON pod.DetailId = d.DetailId
WHERE pod.QuantityReceived < pod.Quantity
  AND po.Status NOT IN ('Cancelled', 'Closed')
```

---

## Index Recommendations

### Detail Table
```sql
-- For requisition lookups
CREATE INDEX IX_Detail_RequisitionId
ON Detail (RequisitionId)
INCLUDE (ItemId, CrossRefId, Quantity, UnitPrice, ExtendedPrice)

-- For item lookups
CREATE INDEX IX_Detail_ItemId
ON Detail (ItemId)

-- For vendor reports
CREATE INDEX IX_Detail_VendorId
ON Detail (VendorId)
```

### Requisitions Table
```sql
-- For status queries
CREATE INDEX IX_Requisitions_Status_Date
ON Requisitions (Status, DateCreated)
INCLUDE (RequisitionNumber, TotalAmount, UserId)

-- For user queries
CREATE INDEX IX_Requisitions_UserId
ON Requisitions (UserId)
```

---

## Views

### vw_ReqDetail
Combined view of requisitions and detail lines:

```sql
SELECT r.*, d.*,
       v.VendorName,
       cr.CatalogPrice
FROM Requisitions r
JOIN Detail d ON r.RequisitionId = d.RequisitionId
LEFT JOIN Vendors v ON d.VendorId = v.VendorId
LEFT JOIN CrossRefs cr ON d.CrossRefId = cr.CrossRefId
```

### vw_ExistingRequisitions
User-facing view with permission filtering:

```sql
-- Uses uf_RequisitionIsVisible function
-- Can be slow during high blocking
```

---

## Performance Considerations

### High-Impact Operations
| Operation | Impact | Mitigation |
|-----------|--------|------------|
| Bulk Detail INSERT | Trigger fires per row | Batch in groups of 100 |
| DELETE vw_ReqDetail | Cascading deletes | Process during low usage |
| Large requisitions | Many Detail records | Split into multiple reqs |

### Known Issues
- [KI-003: trig_DetailUpdate](../../performance/known-issues/trigger-blocking.md) - Trigger blocking
- [KI-004: CrossRef Blocking](../../performance/known-issues/crossref-blocking.md) - Lookup blocking

---

## See Also

- [Business: Requisitions](../../business/entities/requisitions.md)
- [Business: Purchase Orders](../../business/entities/purchase-orders.md)
- [Workflow: Requisition to PO](../../business/workflows/requisition-to-po.md)

