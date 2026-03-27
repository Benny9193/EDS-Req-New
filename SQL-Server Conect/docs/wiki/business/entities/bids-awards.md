# Bids & Awards

[Home](../../index.md) > [Business](../index.md) > [Entities](index.md) > Bids & Awards

---

## Overview

The bidding system manages competitive procurement processes. Districts solicit bids from vendors, evaluate responses, and award contracts for goods and services.

---

## Bidding Lifecycle

```
Bid Created ──► Published ──► Vendors Respond ──► Bid Closes
      │             │              │                   │
      │             │              ▼                   ▼
      │             │      Questions &            Evaluation
      │             │      Amendments                  │
      │             │              │                   ▼
      │             └──────────────┘              Award Made
      │                                               │
      └───────────────────────────────────────────────┘
                                                      │
                                                      ▼
                                              Contract Active
```

---

## Key Tables

The bidding domain has **76 tables** - the largest domain in EDS:

### Core Tables

| Table | Purpose |
|-------|---------|
| BidHeaders | Bid/solicitation header |
| BidDetail | Line items in bid |
| BidVendors | Vendors invited to bid |
| BidResponses | Vendor responses |
| Awards | Winning vendor awards |
| AwardItems | Items in award |
| Contracts | Multi-year agreements |

### Supporting Tables

| Table | Purpose |
|-------|---------|
| BidCategories | Classification |
| BidStatuses | Status codes |
| BidTypes | Bid type (RFP, RFQ, etc.) |
| BidMappedItems | Item mapping for awards |
| EvaluationCriteria | Scoring criteria |
| EvaluationScores | Vendor scores |

---

## Bid Types

| Type | Description | Use Case |
|------|-------------|----------|
| IFB | Invitation for Bid | Standard lowest price |
| RFP | Request for Proposal | Complex services |
| RFQ | Request for Quote | Quick price check |
| Sole Source | Single vendor | Unique product/service |
| Piggyback | Use another entity's bid | Efficiency |

---

## Award Process

### Evaluation Methods

| Method | Description |
|--------|-------------|
| Lowest Price | Award to lowest responsive bidder |
| Best Value | Price plus quality factors |
| Technical Score | Weighted criteria evaluation |
| BAFO | Best and Final Offer |

### Award Workflow

```
Bid Closes
    │
    ▼
Responses Tabulated
    │
    ├── Price Comparison
    │
    ├── Compliance Check
    │       │
    │       ├── Responsive? (met requirements)
    │       └── Responsible? (can perform)
    │
    ├── Evaluation Scoring (if RFP)
    │
    └── Award Decision
            │
            ├── Board Approval (if required)
            │
            └── Award Notification
                    │
                    ├── To Winner(s)
                    └── To Non-winners
```

---

## Contract Management

### Contract Fields

| Field | Description |
|-------|-------------|
| ContractId | Primary key |
| ContractNumber | Display number |
| VendorId | Awarded vendor |
| BidHeaderId | Source bid |
| StartDate | Effective date |
| EndDate | Expiration date |
| TotalValue | Maximum value |
| RenewalOptions | Extension terms |

### Contract Types

| Type | Duration | Renewals |
|------|----------|----------|
| Annual | 1 year | Up to 4 renewals |
| Multi-Year | 2-5 years | Built-in |
| Indefinite | Until cancelled | None |
| Blanket | 1 year | As needed |

---

## BidMappedItems

When an award is made, items are mapped for automatic pricing:

```
Original Item: "Copy Paper, White, 8.5x11"
    │
    ├── Award A (Vendor: Staples)
    │       SKU: STP-12345
    │       Price: $42.99
    │
    └── Award B (Vendor: Office Depot)
            SKU: OD-67890
            Price: $43.50
```

The `trig_DetailUpdate` trigger uses BidMappedItems to:
1. Look up awarded vendor for item
2. Apply contract pricing
3. Update requisition line

---

## Common Queries

### Active Bids
```sql
SELECT bh.BidNumber, bh.BidTitle, bh.BidType,
       bh.OpenDate, bh.CloseDate, bh.Status
FROM BidHeaders bh
WHERE bh.Status IN ('Published', 'Open')
ORDER BY bh.CloseDate
```

### Awards by Vendor
```sql
SELECT v.VendorName, a.AwardNumber,
       bh.BidNumber, a.TotalAmount,
       a.StartDate, a.EndDate
FROM Awards a
JOIN Vendors v ON a.VendorId = v.VendorId
JOIN BidHeaders bh ON a.BidHeaderId = bh.BidHeaderId
WHERE a.Status = 'Active'
ORDER BY v.VendorName, a.StartDate
```

### Items on Award
```sql
SELECT ai.ItemDescription, ai.UnitPrice,
       ai.UOM, v.VendorName
FROM AwardItems ai
JOIN Awards a ON ai.AwardId = a.AwardId
JOIN Vendors v ON a.VendorId = v.VendorId
WHERE ai.ItemId = @ItemId
  AND a.Status = 'Active'
ORDER BY ai.UnitPrice
```

---

## Compliance Requirements

### Public Procurement Rules
- Open competitive bidding > $50,000 (varies by state)
- Public notice requirements
- Bid opening procedures
- Protest rights

### Documentation Required
- Bid specifications
- Vendor responses
- Evaluation worksheets
- Board approval minutes
- Award notification

---

## Performance Considerations

### Trigger Impact
The `trig_DetailUpdate` trigger queries BidMappedItems for every requisition line, which can cause blocking during bulk operations.

See [KI-003: Trigger Blocking](../../performance/known-issues/trigger-blocking.md).

### Index Recommendations
- BidMappedItems should have indexes on ItemId, VendorId
- AwardItems should have covering index for price lookups

---

## See Also

- [Vendors](vendors.md) - Supplier management
- [Catalogs & Items](catalogs-items.md) - Product catalog
- [Workflow: Vendor Bidding](../workflows/vendor-bidding.md)
- [Schema: Bidding](../../schema/by-domain/bidding.md)

