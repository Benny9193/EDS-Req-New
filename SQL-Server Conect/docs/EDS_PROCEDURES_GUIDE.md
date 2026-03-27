# EDS Database - Stored Procedures Business Guide

Generated: 2026-01-15

This guide provides business context and usage guidance for the key stored procedures in the EDS database. For complete parameter documentation, see EDS_STORED_PROCEDURES.md.

---

## Overview

The EDS database contains 364 stored procedures organized into functional domains. This guide focuses on the most commonly used procedures and their business context.

### Naming Conventions

| Prefix | Purpose | Example |
|--------|---------|---------|
| `sp_` | Standard stored procedure | `sp_CreateNewRequisition` |
| `sp_FA_` | Front-end Application (web UI) | `sp_FA_ApproveReq` |
| `sp_CC_` | Control Center (admin) | `sp_CCAccountMaint` |
| `sp_PA_` | Processing Application | `sp_PARequisitions` |
| `sp_UA_` | User Account management | `sp_UAList` |
| `sp_BA_` | Budget Account management | `sp_BAList` |
| `usp_` | User-defined (newer) | `usp_GetPODetail` |

---

## Requisition Lifecycle Procedures

### Creating Requisitions

```sql
-- 1. Create new requisition
EXEC sp_CreateNewRequisition 
    @SchoolId = 123,
    @UserId = 456,
    @CategoryId = 1,
    @BudgetAccountId = 789;

-- 2. Add line items via Detail table

-- 3. Submit for approval
EXEC sp_SubmitRequisition @RequisitionId = @NewReqId;
```

**Key Procedures:**
- `sp_CreateNewRequisition` - Creates requisition header
- `sp_SubmitRequisition` - Submits for approval workflow
- `sp_UpdateReqDetail` - Updates line items
- `sp_HoldRequisition` - Places on hold

### Approval Workflow

```sql
-- Check pending approvals
EXEC sp_RefreshPendingApprovals @DistrictId = 1;

-- Approve requisition
EXEC sp_FA_ApproveReq 
    @RequisitionId = 123,
    @ApproverId = 456,
    @Decision = 3;  -- 3=Approved, 4=Rejected
```

### Requisition Status Flow

```
Draft (H) → sp_SubmitRequisition → Pending (P)
                                      ↓
         sp_FA_ApproveReq ← Approved (A) or Rejected (R)
                                      ↓
         sp_CreatePO ← Ready for PO
```

---

## Purchase Order Procedures

### Creating POs

```sql
-- Create PO from approved requisitions
EXEC sp_CreatePO 
    @RequisitionIdList = '123,124,125',
    @VendorId = 100;

-- Queue for transmission
EXEC usp_QueuePOsToSend @POIdList = '1001,1002';
```

**Key Procedures:**
- `sp_CreatePO` - Generates PO from requisitions
- `sp_FA_CreatePO` - Front-end PO creation
- `usp_QueuePOsToSend` - Queues for vendor transmission
- `sp_FA_UpdatePOStatus` - Updates PO status

### PO Transmission

```sql
-- Start PO send
EXEC usp_StartPOSend @POId = 1001;

-- After transmission complete
EXEC usp_EndPOSend @POId = 1001, @Status = 'Success';
```

---

## Bidding Procedures

### Creating Bids

```sql
-- Create new bid header
EXEC sp_CreateNewBidHeader
    @CategoryId = 1,
    @DueDate = '2026-03-01',
    @Description = 'Office Supplies FY2026';

-- Add items to bid
EXEC sp_CreateBidHeaderItems
    @BidHeaderId = 500,
    @ItemIdList = '1,2,3,4,5';
```

### Bid Evaluation

```sql
-- Compare vendor submissions
EXEC sp_BidCompare @BidHeaderId = 500;

-- View comparison with discounts
EXEC sp_BidCompareDiscount @BidHeaderId = 500;
```

### Awarding Bids

```sql
-- Award to winning vendor
EXEC sp_AwardBidHeader
    @BidHeaderId = 500,
    @VendorId = 100;

-- Award single item
EXEC sp_AwardBidHeaderSingleItem
    @BidHeaderId = 500,
    @ItemId = 123,
    @VendorId = 100;
```

---

## Batch Processing

Batch processing handles high-volume order processing.

```sql
-- Load batch
EXEC sp_BatchLoad @BatchId = 1;

-- Verify batch
EXEC sp_BatchVerify @BatchId = 1;

-- Process batch
EXEC sp_BatchProcess @BatchId = 1;

-- Convert to POs
EXEC sp_BatchConvert @BatchId = 1;
```

**Batch Flow:**
```
sp_BatchLoad → sp_BatchVerify → sp_BatchProcess → sp_BatchConvert
```

---

## Catalog Management

### Importing Catalogs

```sql
-- Import vendor catalog
EXEC sp_CatalogImport
    @VendorId = 100,
    @FileName = 'catalog_2026.xlsx';

-- XML import
EXEC sp_CatalogImporterXML @XMLData = @CatalogXML;
```

### Price Updates

```sql
-- Update list prices for category
EXEC sp_UpdateAllListPrices @CategoryId = 1;

-- Update specific items
EXEC sp_UpdateListPrices @ItemIdList = '1,2,3';
```

---

## User Management

### Authentication

```sql
-- Attempt login
EXEC sp_FA_AttemptLogin
    @UserName = 'jdoe',
    @Password = 'hashed_password';

-- Logout
EXEC sp_Logout @SessionId = 12345;
```

### User Account Management

```sql
-- List user's budget accounts
EXEC sp_UAList @UserId = 456;

-- Set user's budget account
EXEC sp_FA_SetUserAccount
    @UserId = 456,
    @AccountId = 789;
```

---

## Budget & Account Procedures

```sql
-- List budget accounts for district
EXEC sp_BAList @DistrictId = 1;

-- Copy budget to new year
EXEC sp_CopyBudgetAmounts
    @SourceBudgetId = 2025,
    @TargetBudgetId = 2026;

-- Bring accounts forward to new year
EXEC usp_BringAccountsForward @DistrictId = 1;
```

---

## Reporting Procedures

```sql
-- Create report session
EXEC sp_FA_CreateReportSession
    @UserId = 456,
    @ReportType = 'RequisitionSummary';

-- Get requisition report data
EXEC sp_ReportReqData
    @DistrictId = 1,
    @StartDate = '2026-01-01',
    @EndDate = '2026-01-31';
```

---

## Maintenance Procedures

### Index Maintenance

```sql
-- Defrag all indexes
EXEC sp_DefragAll;

-- Reindex all tables
EXEC sp_ReindexAll;
```

### Process Monitoring

```sql
-- Monitor active processes
EXEC sp_processMonitor;

-- Check process status
EXEC sp_processStatus;

-- Kill process if needed
EXEC sp_processKill @ProcessId = 123;
```

### Data Cleanup

```sql
-- Nightly cleanup
EXEC sp_NightlyGarbageCollection;

-- Delete empty requisitions
EXEC sp_DeleteEmptyReqs;

-- Delete zero quantities
EXEC sp_DeleteZeros @RequisitionId = 123;
```

---

## Common Procedure Chains

### Order Processing Flow
```
sp_CreateNewRequisition
    ↓
sp_UpdateReqDetail (add items)
    ↓
sp_SubmitRequisition
    ↓
sp_RefreshPendingApprovals
    ↓
sp_FA_ApproveReq
    ↓
sp_CreatePO
    ↓
usp_QueuePOsToSend
    ↓
usp_StartPOSend → usp_EndPOSend
```

### Bid Award Flow
```
sp_CreateNewBidHeader
    ↓
sp_CreateBidHeaderItems
    ↓
sp_ImportVendorsBid (collect responses)
    ↓
sp_BidCompare
    ↓
sp_AwardBidHeader
    ↓
CrossRefs updated with award pricing
```

### Year-End Processing
```
sp_PrepareNextYear
    ↓
sp_CopyBudgetAmounts
    ↓
usp_BringAccountsForward
    ↓
sp_CopyReqs (if carrying forward)
```

---

## Error Handling

Most procedures return status codes:
- `0` = Success
- `-1` = General error
- `-2` = Validation error
- Specific negative codes for specific errors

Always check return values and handle errors appropriately.

---

## Performance Considerations

| Procedure | Notes |
|-----------|-------|
| `sp_BatchProcess` | Can be long-running, monitor progress |
| `sp_CatalogImport` | Large imports should run off-hours |
| `sp_DefragAll` | Resource intensive, schedule during maintenance |
| `sp_ReindexAll` | Locks tables, run during off-hours |

---

## Change History

| Date | Change | Author |
|------|--------|--------|
| 2026-01-15 | Initial procedures business guide | Phase 3 Documentation |
