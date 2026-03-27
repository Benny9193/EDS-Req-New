/*
===============================================================================
  PO Splitting SP Patch — Configurable MaxPODetailItems
===============================================================================
  Purpose:  Allow arbitrary PO item limits (e.g., 25) instead of hardcoded 99
  Request:  East Brunswick Public Schools (DistrictId=28)
  Contact:  Lori Tagerty, Senior Manager AP/Purchasing
  Date:     2026-03-24

  PROBLEM:
  sp_CreatePO checks: IF @MaxPODetailItems = 99
  This only activates splitting when the value is exactly 99.
  The else branch inserts ALL items without any limit.

  FIX:
  Change the condition to: IF @MaxPODetailItems > 0 AND @MaxPODetailItems < 999999999
  And use @MaxPODetailItems dynamically in the TOP clause.

  IMPACT:
  - Districts with MaxPODetailItems = 999999999 (current default): NO CHANGE
  - Districts with MaxPODetailItems = 99: SAME BEHAVIOR (99 items per PO)
  - East Brunswick after setting to 25: POs split at 25 items

  ROLLBACK:
  Run the rollback section at the bottom to restore original behavior.
===============================================================================
*/

-- ============================================================================
-- STEP 1: Backup current procedure
-- ============================================================================
-- The backup already exists as sp_CreatePO_Saved062724
-- Creating a fresh backup before this change:

IF OBJECT_ID('sp_CreatePO_PreSplitPatch', 'P') IS NOT NULL
    DROP PROCEDURE sp_CreatePO_PreSplitPatch;
GO

-- Copy current definition
EXEC sp_rename 'sp_CreatePO', 'sp_CreatePO_PreSplitPatch';
GO

-- ============================================================================
-- STEP 2: Create patched procedure
-- ============================================================================
-- NOTE: This is a TEMPLATE showing the key change.
-- The full procedure body should be copied from sp_CreatePO_PreSplitPatch
-- with ONLY the following section replaced.
--
-- FIND (around line 239):
--
--     if @MaxPODetailItems = 99
--     begin
--       -- Assign Detail to PO
--       insert PODetailItems (...)
--         select top 99 @POId, Detail.DetailId, ...
--           from Detail
--           ...
--           and Detail.DetailId > @MaxDetailId
--         order by Detail.DetailId
--     end
--     else
--     begin
--       -- Assign Detail to PO
--       insert PODetailItems (...)
--         select @POId, Detail.DetailId, ...
--           from Detail
--           ...
--     end
--
-- REPLACE WITH:
--
--     if @MaxPODetailItems > 0 AND @MaxPODetailItems < 999999999
--     begin
--       -- Assign Detail to PO (with configurable item limit)
--       insert PODetailItems (POId, DetailId, ItemId, Quantity, BidItemId,
--                             BidPrice, GrossPrice, DiscountRate, AwardId,
--                             VendorId, VendorItemCode, Alternate, ContractNumber)
--         select top (@MaxPODetailItems) @POId, Detail.DetailId, Detail.ItemId,
--                Detail.Quantity, Detail.BidItemId, Detail.BidPrice,
--                Detail.GrossPrice, Detail.DiscountRate, Detail.AwardId,
--                Detail.VendorId, Detail.VendorItemCode, Detail.Alternate,
--                bi.ContractNumber
--           from Detail
--           join Requisitions on Requisitions.RequisitionId = Detail.RequisitionId
--           join School on School.SchoolId = Requisitions.SchoolId
--           outer apply (Select top 1 Bids.BidHeaderId, BidItems.ContractNumber
--                          from BidItems
--                          join Bids on Bids.BidId = BidItems.BidId
--                         where BidItems.BidItemId = Detail.BidItemId) bi
--          where School.DistrictId = @DistrictId
--            and Detail.VendorId = @VendorId
--            and Detail.RequisitionId = @pRequisitionId
--            and Detail.ItemId is not null
--            and coalesce(bi.BidHeaderId,
--                         case when Detail.BidHeaderId = 0
--                              then null
--                              else Detail.BidHeaderId end,
--                         Requisitions.BidHeaderId) = @BidHeaderId
--            and Detail.DetailId > @MaxDetailId
--          order by Detail.DetailId
--     end
--     else
--     begin
--       -- Assign ALL Detail to PO (no limit — default behavior)
--       insert PODetailItems (POId, DetailId, ItemId, Quantity, BidItemId,
--                             BidPrice, GrossPrice, DiscountRate, AwardId,
--                             VendorId, VendorItemCode, Alternate, ContractNumber)
--         select @POId, Detail.DetailId, Detail.ItemId, Detail.Quantity,
--                Detail.BidItemId, Detail.BidPrice, Detail.GrossPrice,
--                Detail.DiscountRate, Detail.AwardId, Detail.VendorId,
--                Detail.VendorItemCode, Detail.Alternate, bi.ContractNumber
--           from Detail
--           join Requisitions on Requisitions.RequisitionId = Detail.RequisitionId
--           join School on School.SchoolId = Requisitions.SchoolId
--           outer apply (Select top 1 Bids.BidHeaderId, BidItems.ContractNumber
--                          from BidItems
--                          join Bids on Bids.BidId = BidItems.BidId
--                         where BidItems.BidItemId = Detail.BidItemId) bi
--          where School.DistrictId = @DistrictId
--            and Detail.VendorId = @VendorId
--            and Detail.RequisitionId = @pRequisitionId
--            and Detail.ItemId is not null
--            and coalesce(bi.BidHeaderId,
--                         case when Detail.BidHeaderId = 0
--                              then null
--                              else Detail.BidHeaderId end,
--                         Requisitions.BidHeaderId) = @BidHeaderId
--     end

-- ============================================================================
-- STEP 3: Configure East Brunswick (after SP is deployed)
-- ============================================================================

-- Check current value
SELECT af.AccountingFormatId, af.Description, af.MaxPODetailItems
  FROM District d
  JOIN AccountingFormats af ON af.AccountingFormatId = d.AccountingFormatId
 WHERE d.DistrictId = 28;

-- Set to 25 items per PO
-- UPDATE AccountingFormats
--    SET MaxPODetailItems = 25
--  WHERE AccountingFormatId = 33;

-- ============================================================================
-- STEP 4: Verify (dry run query)
-- ============================================================================

-- Preview: Which POs from last budget year would have been split?
SELECT
    ph.PONumber,
    ph.VendorName,
    ph.SchoolName,
    ph.ItemCount AS OriginalItems,
    CEILING(CAST(ph.ItemCount AS FLOAT) / 25) AS WouldBecomeNPOs,
    CEILING(CAST(ph.ItemCount AS FLOAT) / 25) - 1 AS ExtraPOsCreated,
    ph.Amount
FROM POHeader ph
WHERE ph.DistrictId = 28
  AND ph.PODate >= '2024-12-01' AND ph.PODate < '2025-12-01'
  AND ph.ItemCount > 25
ORDER BY ph.ItemCount DESC;

-- ============================================================================
-- ROLLBACK (if needed)
-- ============================================================================
-- To restore original behavior:
--
-- 1. Restore the original stored procedure:
--    DROP PROCEDURE sp_CreatePO;
--    EXEC sp_rename 'sp_CreatePO_PreSplitPatch', 'sp_CreatePO';
--
-- 2. Reset MaxPODetailItems:
--    UPDATE AccountingFormats
--       SET MaxPODetailItems = 999999999
--     WHERE AccountingFormatId = 33;
