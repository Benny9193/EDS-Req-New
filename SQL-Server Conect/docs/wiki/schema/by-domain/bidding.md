# Schema: Bidding Domain

[Home](../../index.md) > [Schema](../index.md) > [By Domain](index.md) > Bidding

---

## Overview

The bidding domain is the **largest in EDS** with 76 tables supporting competitive procurement processes including bids, awards, contracts, and vendor responses.

---

## Table Count: 76

### Core Tables

| Table | Purpose | Key Columns |
|-------|---------|-------------|
| BidHeaders | Bid/solicitation master | BidHeaderId, BidNumber, BidTitle, BidType |
| BidDetail | Line items in bid | BidDetailId, BidHeaderId, ItemId, Quantity |
| BidVendors | Vendors invited to bid | BidVendorId, BidHeaderId, VendorId |
| BidResponses | Vendor bid submissions | BidResponseId, BidHeaderId, VendorId |
| BidResponseDetail | Response line items | BidResponseDetailId, BidResponseId |
| Awards | Winning vendor awards | AwardId, BidHeaderId, VendorId |
| AwardItems | Items in award | AwardItemId, AwardId, ItemId, Price |
| Contracts | Multi-year agreements | ContractId, VendorId, StartDate, EndDate |

### Supporting Tables

| Table | Purpose |
|-------|---------|
| BidCategories | Bid classification |
| BidStatuses | Status lookup |
| BidTypes | IFB, RFP, RFQ, etc. |
| BidQuestions | Vendor Q&A |
| BidAddenda | Specification changes |
| BidAttachments | File uploads |
| BidMappedItems | Item mapping for awards |

### Evaluation Tables

| Table | Purpose |
|-------|---------|
| EvaluationCriteria | Scoring criteria |
| EvaluationScores | Vendor scores |
| EvaluationComments | Evaluator notes |
| EvaluationTeam | Evaluation committee |

---

## Key Relationships

```
BidHeaders (1) ────────► (N) BidDetail
     │
     ├────────► (N) BidVendors ────► Vendors
     │
     ├────────► (N) BidResponses ────► BidResponseDetail
     │
     ├────────► (N) BidQuestions
     │
     ├────────► (N) BidAddenda
     │
     └────────► (N) Awards ────► AwardItems ────► BidMappedItems
```

---

## Critical Table: BidMappedItems

This table links award pricing to requisition items:

### Schema
| Column | Type | Description |
|--------|------|-------------|
| MappedItemId | INT | Primary key |
| AwardId | INT | Source award |
| OrigItemId | INT | Original item requested |
| NewItemId | INT | Awarded item (may differ) |
| VendorId | INT | Awarded vendor |
| ContractPrice | DECIMAL | Award price |
| UOM | VARCHAR | Unit of measure |

### Usage in Trigger
The `trig_DetailUpdate` trigger queries this table:

```sql
-- When user adds item to requisition
-- Trigger looks up awarded price
SELECT bmi.NewItemId, bmi.VendorId, bmi.ContractPrice
FROM BidMappedItems bmi
JOIN Awards a ON bmi.AwardId = a.AwardId
WHERE bmi.OrigItemId = @RequestedItemId
  AND a.Status = 'Active'
```

---

## Common Queries

### Active Bids
```sql
SELECT bh.BidNumber, bh.BidTitle, bh.BidType,
       bt.TypeDescription,
       bh.OpenDate, bh.CloseDate
FROM BidHeaders bh
JOIN BidTypes bt ON bh.BidTypeId = bt.BidTypeId
WHERE bh.Status IN ('Open', 'Published')
ORDER BY bh.CloseDate
```

### Award Summary
```sql
SELECT a.AwardNumber, v.VendorName,
       bh.BidNumber, a.TotalAmount,
       a.StartDate, a.EndDate,
       COUNT(ai.AwardItemId) as ItemCount
FROM Awards a
JOIN Vendors v ON a.VendorId = v.VendorId
JOIN BidHeaders bh ON a.BidHeaderId = bh.BidHeaderId
LEFT JOIN AwardItems ai ON a.AwardId = ai.AwardId
WHERE a.Status = 'Active'
GROUP BY a.AwardId, a.AwardNumber, v.VendorName,
         bh.BidNumber, a.TotalAmount, a.StartDate, a.EndDate
```

### Bid Response Comparison
```sql
SELECT v.VendorName,
       SUM(brd.UnitPrice * brd.Quantity) as TotalBid
FROM BidResponses br
JOIN Vendors v ON br.VendorId = v.VendorId
JOIN BidResponseDetail brd ON br.BidResponseId = brd.BidResponseId
WHERE br.BidHeaderId = @BidHeaderId
GROUP BY br.BidResponseId, v.VendorName
ORDER BY TotalBid
```

---

## Index Recommendations

### BidMappedItems
```sql
-- For trigger lookups
CREATE INDEX IX_BidMappedItems_OrigItemId
ON BidMappedItems (OrigItemId)
INCLUDE (NewItemId, VendorId, ContractPrice, AwardId)

-- For award filtering
CREATE INDEX IX_BidMappedItems_AwardId
ON BidMappedItems (AwardId)
```

### BidHeaders
```sql
-- For status queries
CREATE INDEX IX_BidHeaders_Status
ON BidHeaders (Status)
INCLUDE (BidNumber, BidTitle, CloseDate)
```

---

## Related Triggers

| Trigger | Table | Impact |
|---------|-------|--------|
| trig_BidHeaders | BidHeaders | Audit logging |
| trig_Awards | Awards | Status updates |
| trig_BidMappedItems | BidMappedItems | Price sync |

---

## Performance Considerations

### High-Impact Operations
| Operation | Impact | Mitigation |
|-----------|--------|------------|
| Award creation | Creates many BidMappedItems | Batch in smaller groups |
| Item remapping | Full table scan possible | Add covering indexes |
| Bid response import | Bulk inserts | Use staged loading |

### Known Issues
The bidding tables are involved in [KI-003: Trigger Blocking](../../performance/known-issues/trigger-blocking.md) through BidMappedItems lookups.

---

## See Also

- [Business: Bids & Awards](../../business/entities/bids-awards.md)
- [Workflow: Vendor Bidding](../../business/workflows/vendor-bidding.md)
- [Trigger Blocking](../../performance/known-issues/trigger-blocking.md)

