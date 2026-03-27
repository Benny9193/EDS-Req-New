# EDS Database - Infinite Loop Analysis

Generated: 2026-01-09 12:29:51

This report identifies stored procedures with patterns that could cause infinite loops.

---

## Summary

**Total Procedures Analyzed:** 395
**Procedures with Issues:** 78

| Severity | Count |
|----------|-------|
| HIGH | 1 |
| MEDIUM | 0 |
| LOW | 78 |

---

## HIGH Severity Issues

**These require immediate attention:**

### dbo.usp_SearchItemsByReqHKDS

*Last modified: 2022-12-22 15:00:36.410000*

**Issue:** Infinite WHILE loop
- WHILE 1=1 loop without visible BREAK condition
- **Recommendation:** Add explicit BREAK condition or refactor to bounded loop

**Code snippet:**
```sql



--USE [EDS]
--GO
--/****** Object:  StoredProcedure [dbo].[usp_SearchItemsByReqHKDS]    Script Date: 7/31/2020 7:45:40 AM ******/
--SET ANSI_NULLS ON
--GO
--SET QUOTED_IDENTIFIER ON
--GO

--exec dbo.usp_SearchItemsByReqHKDS 58609170, 9, 0, 'blue red colors', 400, 0, 'and'
--exec dbo.u
```

---

## LOW Severity Issues

**Informational - may be false positives:**

- `bid2xls`: Missing BREAK in WHILE
- `bid2xlsTest`: Missing BREAK in WHILE
- `dt_checkinobject`: Missing BREAK in WHILE
- `dt_checkoutobject`: Missing BREAK in WHILE
- `dt_generateansiname`: Missing BREAK in WHILE
- `dt_isundersourcecontrol`: Missing BREAK in WHILE
- `sp_BatchConvert`: Missing BREAK in WHILE
- `sp_BatchConvertNew`: Missing BREAK in WHILE
- `sp_BatchProcess`: Missing BREAK in WHILE
- `sp_BatchQueue`: Missing BREAK in WHILE
- `sp_BatchVerify`: Missing BREAK in WHILE
- `sp_BatchVerifyBook`: Missing BREAK in WHILE
- `sp_BatchVerifyForce`: Missing BREAK in WHILE
- `sp_BidCopy`: Missing BREAK in WHILE
- `sp_BidCopyChangePP`: Missing BREAK in WHILE
- `sp_BidCopyWithIncrease`: Missing BREAK in WHILE
- `sp_BuildTopOrdered`: Missing BREAK in WHILE
- `sp_CombineReqs`: Missing BREAK in WHILE
- `sp_CombineReqsByVendorNoDelete`: Missing BREAK in WHILE
- `sp_ConvertReqs`: Missing BREAK in WHILE
- `sp_ConvertTextbookReqs`: Missing BREAK in WHILE
- `sp_CopyMSRPVers2BidUsingCursorSave`: Missing BREAK in WHILE
- `sp_CopyMSRPVers2BidUsingCursorSave2`: Missing BREAK in WHILE
- `sp_CopyReqsBulk`: Missing BREAK in WHILE
- `sp_CreatePO`: Missing BREAK in WHILE
- `sp_CreatePO_Saved062724`: Missing BREAK in WHILE
- `sp_CreatePOTest`: Missing BREAK in WHILE
- `sp_DefragAll`: Missing BREAK in WHILE
- `sp_DeleteDistrictPOs`: Missing BREAK in WHILE
- `sp_DeleteRequisitionRestricted`: Missing BREAK in WHILE
- `sp_DistrictRequisitionDetail`: Missing BREAK in WHILE
- `sp_EnhancedSearchItem`: Missing BREAK in WHILE
- `sp_FA_CreatePO`: Missing BREAK in WHILE
- `sp_MasterBudgetBook`: Missing BREAK in WHILE
- `sp_MoveIndexes`: Missing BREAK in WHILE
- `sp_MPIHeadings`: Missing BREAK in WHILE
- `sp_ProcessCopyRequests`: Missing BREAK in WHILE
- `sp_processMonitorOrig`: Missing BREAK in WHILE
- `sp_processStatus`: Missing BREAK in WHILE
- `sp_Reaward_script`: Missing BREAK in WHILE
- `sp_ReindexAll`: Missing BREAK in WHILE
- `sp_RTK_Build_MSDS_and_MSDSDetail`: Missing BREAK in WHILE
- `sp_SearchItemsByReqHK`: Missing BREAK in WHILE
- `sp_ShowAllDefrag`: Missing BREAK in WHILE
- `sp_ShowDistribution`: Missing BREAK in WHILE
- `sp_ShowTextbookSavings`: Missing BREAK in WHILE
- `sp_UpdateAllListPrices`: Missing BREAK in WHILE
- `sp_UpdateAllReqs`: Missing BREAK in WHILE
- `sp_UpdatePOAmounts`: Missing BREAK in WHILE
- `sp_UpdatePricePlan`: Missing BREAK in WHILE
- `sp_UpdateReq`: Missing BREAK in WHILE
- `sp_UpdateReqDetail`: Missing BREAK in WHILE
- `sp_UpdateReqDetailItem`: Missing BREAK in WHILE
- `sp_UpdateReqDetailPricePlan`: Missing BREAK in WHILE
- `usp_GeneratePassword`: Missing BREAK in WHILE
- `usp_GeneratePassword_Print`: Missing BREAK in WHILE
- `usp_GetMSDSSheets`: Missing BREAK in WHILE
- `usp_MakeZ$`: Missing BREAK in WHILE
- `usp_MakeZC`: Missing BREAK in WHILE
- `usp_OrderEZVendors`: Missing BREAK in WHILE
- `usp_SDSDocs`: Missing BREAK in WHILE
- `usp_SearchItems_SearchDataDB`: Missing BREAK in WHILE
- `usp_SearchItemsByReqHKDS`: Missing BREAK in WHILE
- `usp_SearchItemsByReqHKDS_David`: Missing BREAK in WHILE
- `usp_SearchItemsByReqHKDSDavid`: Missing BREAK in WHILE
- `usp_SearchItemsByReqHKDSError`: Missing BREAK in WHILE
- `usp_SearchItemsByReqHKDSTest`: Missing BREAK in WHILE
- `usp_SearchVendors`: Missing BREAK in WHILE
- `usp_VendorStatsCYvsLY`: Missing BREAK in WHILE
- `sp_CombineReqs`: Missing BREAK in WHILE
- `sp_CombineReqsNoDelete`: Missing BREAK in WHILE
- `sp_ConvertReadyBatches`: Missing BREAK in WHILE
- `sp_CopyReqs`: Missing BREAK in WHILE
- `sp_DeleteDistrictBudgetPOs`: Missing BREAK in WHILE
- `sp_DeleteEmptyReqs`: Missing BREAK in WHILE
- `sp_DeletePOList`: Missing BREAK in WHILE
- `sp_MultiBatchLoad`: Missing BREAK in WHILE
- `sp_SavingsLetter`: Missing BREAK in WHILE

---

## Best Practices to Prevent Infinite Loops

1. **Always include explicit exit conditions:**
   ```sql
   WHILE @counter < @maxIterations
   BEGIN
       -- Process
       SET @counter = @counter + 1
   END
   ```

2. **Use BREAK with WHILE 1=1:**
   ```sql
   WHILE 1=1
   BEGIN
       -- Process
       IF @condition BREAK  -- Explicit exit
   END
   ```

3. **Add depth parameter to recursive calls:**
   ```sql
   CREATE PROCEDURE sp_Recursive @id INT, @depth INT = 0
   AS BEGIN
       IF @depth > 100 RETURN  -- Max depth
       EXEC sp_Recursive @next_id, @depth + 1
   END
   ```

4. **Use TRY/CATCH with timeout:**
   ```sql
   SET LOCK_TIMEOUT 30000  -- 30 second timeout
   ```
