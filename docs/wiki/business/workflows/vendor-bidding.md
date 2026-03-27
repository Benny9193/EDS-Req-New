# Workflow: Vendor Bidding

[Home](../../index.md) > [Business](../index.md) > [Workflows](index.md) > Vendor Bidding

---

## Overview

The vendor bidding workflow manages competitive procurement processes where multiple vendors compete to supply goods or services. This ensures compliance with public procurement regulations and obtains best value for the district.

---

## Workflow Diagram

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         VENDOR BIDDING WORKFLOW                             │
│                                                                             │
│    ┌──────────────────────────────────────────────────────────────────┐    │
│    │                    BID CREATION PHASE                            │    │
│    │                                                                  │    │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │    │
│    │   │ Identify │───▶│  Draft   │───▶│ Internal │───▶│ Publish  │  │    │
│    │   │   Need   │    │   Bid    │    │  Review  │    │    Bid   │  │    │
│    │   └──────────┘    └──────────┘    └──────────┘    └──────────┘  │    │
│    └────────────────────────────────────────┬─────────────────────────┘    │
│                                             │                              │
│    ┌────────────────────────────────────────▼─────────────────────────┐    │
│    │                    SOLICITATION PHASE                            │    │
│    │                                                                  │    │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │    │
│    │   │  Notify  │───▶│ Vendor   │───▶│ Q&A /    │───▶│   Bid    │  │    │
│    │   │ Vendors  │    │ Response │    │ Addenda  │    │  Closes  │  │    │
│    │   └──────────┘    └──────────┘    └──────────┘    └──────────┘  │    │
│    └────────────────────────────────────────┬─────────────────────────┘    │
│                                             │                              │
│    ┌────────────────────────────────────────▼─────────────────────────┐    │
│    │                    EVALUATION PHASE                              │    │
│    │                                                                  │    │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │    │
│    │   │   Open   │───▶│ Evaluate │───▶│  Score   │───▶│  Select  │  │    │
│    │   │   Bids   │    │ Responses│    │ Vendors  │    │  Winner  │  │    │
│    │   └──────────┘    └──────────┘    └──────────┘    └──────────┘  │    │
│    └────────────────────────────────────────┬─────────────────────────┘    │
│                                             │                              │
│    ┌────────────────────────────────────────▼─────────────────────────┐    │
│    │                    AWARD PHASE                                   │    │
│    │                                                                  │    │
│    │   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐  │    │
│    │   │  Board   │───▶│  Award   │───▶│ Execute  │───▶│ Contract │  │    │
│    │   │ Approval │    │  Notice  │    │ Contract │    │  Active  │  │    │
│    │   └──────────┘    └──────────┘    └──────────┘    └──────────┘  │    │
│    └──────────────────────────────────────────────────────────────────┘    │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Phase 1: Bid Creation

### Step 1: Identify Need
- Department requests formal bid
- Purchasing reviews requirement
- Determine bid type (IFB, RFP, RFQ)
- Estimate total value

### Step 2: Draft Bid
1. Create bid header
2. Define specifications
3. List items/services needed
4. Set evaluation criteria (if RFP)
5. Establish timeline

### Bid Header Information

| Field | Description |
|-------|-------------|
| BidNumber | Unique identifier |
| BidTitle | Descriptive name |
| BidType | IFB, RFP, RFQ, etc. |
| OpenDate | When responses accepted |
| CloseDate | Submission deadline |
| PreBidMeeting | Optional meeting date |
| ContactPerson | Purchasing contact |

### Step 3: Internal Review
- Legal review (if required)
- Finance review (budget confirmation)
- Technical review (specifications)
- Final approval to publish

### Step 4: Publish Bid
- Post to public bid portal
- Notify registered vendors
- Start public notice period
- Update status to "Published"

---

## Phase 2: Solicitation

### Step 5: Notify Vendors
- Email to vendors in category
- Post on district website
- Required public notice (newspaper, etc.)
- Update vendor portal

### Step 6: Vendor Questions
Vendors submit questions during Q&A period:
1. Questions collected
2. Answers compiled
3. Addendum issued (if needed)
4. All vendors receive same information

### Question Management
```
Question: "Can you clarify the delivery schedule?"
    │
    ▼
Answer prepared by Purchasing
    │
    ▼
Addendum #1 issued to all vendors
    │
    ▼
Close date may be extended
```

### Step 7: Receive Responses
- Vendors submit sealed bids
- System records submission time
- No responses accepted after deadline
- Late submissions rejected

---

## Phase 3: Evaluation

### Step 8: Open Bids
- Public bid opening (if required)
- Record all submitted prices
- Check for responsiveness
- Verify required documents

### Responsiveness Check

| Requirement | Check |
|-------------|-------|
| Submitted on time | Yes/No |
| All forms complete | Yes/No |
| Signature present | Yes/No |
| Bond included (if req) | Yes/No |
| References provided | Yes/No |

### Step 9: Evaluate Responses

#### For IFB (Lowest Price)
Simple price comparison for responsive bidders.

#### For RFP (Best Value)
Score against criteria:

| Criteria | Weight | Vendor A | Vendor B |
|----------|--------|----------|----------|
| Price | 40% | 35/40 | 38/40 |
| Experience | 25% | 22/25 | 20/25 |
| References | 20% | 18/20 | 17/20 |
| Timeline | 15% | 12/15 | 13/15 |
| **Total** | **100%** | **87** | **88** |

### Step 10: Select Winner
- Rank vendors by score
- Verify vendor responsibility
- Check for conflicts of interest
- Document selection rationale

---

## Phase 4: Award

### Step 11: Board Approval
For awards above threshold:
1. Prepare board agenda item
2. Present recommendation
3. Board votes to approve
4. Record in meeting minutes

### Step 12: Award Notice
- Notify winning vendor
- Notify non-winning vendors
- Post award results
- Start protest period

### Protest Period
- Usually 5-10 business days
- Losing vendors may protest
- Must respond to protests
- Document resolution

### Step 13: Execute Contract
1. Finalize terms and conditions
2. Obtain vendor signature
3. Obtain district signature
4. Record insurance certificates
5. Set up in system

### Step 14: Contract Active
- Load pricing into system
- Map items to award (BidMappedItems)
- Activate for requisitions
- Set contract dates

---

## Award Integration with Requisitions

Once an award is active, it integrates with requisitions:

```
Requisition Created
    │
    ▼
User selects item
    │
    ▼
System checks for active award
    │
    ├── Award found → Apply contract price
    │                 Assign awarded vendor
    │
    └── No award → Use catalog price
                   User selects vendor
```

### BidMappedItems Table
Maps original items to awarded items/prices:

```sql
-- When trig_DetailUpdate fires, it uses this mapping
SELECT bmi.NewItemId, bmi.VendorId, bmi.ContractPrice
FROM BidMappedItems bmi
JOIN Awards a ON bmi.AwardId = a.AwardId
WHERE bmi.OrigItemId = @RequestedItemId
  AND a.Status = 'Active'
  AND a.StartDate <= GETDATE()
  AND a.EndDate >= GETDATE()
```

---

## Bid Types

### IFB - Invitation for Bid
- Lowest responsive bidder wins
- Clear specifications required
- Used for commodities

### RFP - Request for Proposal
- Best value evaluation
- Weighted criteria scoring
- Used for complex services

### RFQ - Request for Quote
- Quick price comparison
- Informal process
- Lower dollar thresholds

### Sole Source
- Only one vendor can provide
- Justification required
- Board approval usually needed

### Piggyback
- Use another entity's bid
- Verify terms allow it
- Common with cooperatives

---

## Compliance Requirements

### Public Notice
| Threshold | Notice Required |
|-----------|-----------------|
| < $50,000 | 3 vendors quoted |
| $50,000+ | Public advertisement |
| $100,000+ | Board approval |

### Required Documentation
- Bid specifications
- All vendor responses
- Evaluation worksheets
- Award justification
- Board minutes (if applicable)
- Contract signed

### Retention
- Bid documents: 7 years
- Contract: Life + 7 years
- Unsuccessful bids: 3 years

---

## Common Queries

### Open Bids
```sql
SELECT BidNumber, BidTitle, CloseDate,
       DATEDIFF(day, GETDATE(), CloseDate) as DaysRemaining
FROM BidHeaders
WHERE Status = 'Open'
ORDER BY CloseDate
```

### Bid Responses
```sql
SELECT v.VendorName, br.SubmissionDate, br.TotalBidAmount
FROM BidResponses br
JOIN Vendors v ON br.VendorId = v.VendorId
WHERE br.BidHeaderId = @BidId
ORDER BY br.TotalBidAmount
```

---

## See Also

- [Bids & Awards](../entities/bids-awards.md) - Entity details
- [Vendors](../entities/vendors.md) - Vendor management
- [Requisition to PO](requisition-to-po.md) - How awards are used
- [Schema: Bidding](../../schema/by-domain/bidding.md)

