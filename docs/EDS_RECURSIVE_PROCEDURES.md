# EDS Database - Recursive Procedure Documentation

Generated: 2026-01-09 12:16:42

This document explains the purpose of each self-calling (recursive) stored procedure.

---

## Summary

**Total Recursive Procedures:** 34

### By Category

| Category | Count | Description |
|----------|-------|-------------|
| Tree Traversal | 15 | Traverses hierarchical/tree data structure |
| Org Hierarchy | 8 | Navigates organizational hierarchy |
| Approval Chain | 5 | Processes approval workflow chain |
| Category Tree | 4 | Traverses category/catalog hierarchy |
| Bill Of Materials | 1 | Processes bill of materials/component hierarchy |
| Document Chain | 1 | Follows document/attachment chain |

---

## Tree Traversal (15 procedures)

*Traverses hierarchical/tree data structure*

### sp_AwardBidHeader

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-06-26 12:00:23.160000
- **Also calls:** Log_ProcedureCall
- **Termination:** Has explicit termination condition ✓

### sp_BidCopyWithIncrease

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-11-12 14:11:43.953000
- **Warning:** No obvious termination condition found ⚠️

### sp_CCUpdateUserAccounts_2

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2014-10-07 17:53:25.150000
- **Termination:** Has explicit termination condition ✓

### sp_CXmlLogin

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2024-10-18 06:40:48.047000
- **Also calls:** sp_NewRequisitionId
- **Termination:** Has explicit termination condition ✓

### usp_CopyRequisition

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-08-11 11:44:01.123000
- **Also calls:** sp_NewRequisitionId
- **Termination:** Has explicit termination condition ✓

### usp_GetPODetail

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-09-11 16:06:24.730000
- **Also calls:** usp_GetPODetail_Test
- **Termination:** Has explicit termination condition ✓

### usp_GetPODetail_Test

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-06-24 15:35:25.850000
- **Warning:** No obvious termination condition found ⚠️

### usp_OrderEZVendors

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-09-18 15:12:44.180000
- **Termination:** Has explicit termination condition ✓

### usp_SDSDocs

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-07-24 16:03:22.303000
- **Warning:** No obvious termination condition found ⚠️

### usp_SearchItemsByReqHKDS

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2022-12-22 15:00:36.410000
- **Parameters:** `@pRequisitionId int
	, @pVendorId int
	, @pHeadingId bigint
	, @pFilter varchar(4096)
	, @pDistr...`
- **Termination:** Has explicit termination condition ✓

### usp_SearchItemsByReqHKDSDavid

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2020-06-09 17:20:06.727000
- **Also calls:** usp_SearchItemsByReqHKDS
- **Parameters:** `@pRequisitionId int, @pVendorId int, @pHeadingId bigint, @pFilter varchar(4096), @pDistrictId int, @...`
- **Termination:** Has explicit termination condition ✓

### usp_SearchVendors

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-09-18 15:12:43.980000
- **Termination:** Has explicit termination condition ✓

### usp_TransactionLogMover

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-04-06 12:08:31.603000
- **Termination:** Has explicit termination condition ✓

### usp_VendorStatsCYvsLY

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2025-05-08 16:15:38.140000
- **Warning:** No obvious termination condition found ⚠️

### usp_WaitingTasks

- **Schema:** dbo
- **Purpose:** Traverses hierarchical/tree data structure
- **Modified:** 2019-08-16 12:13:35.210000
- **Warning:** No obvious termination condition found ⚠️

---

## Org Hierarchy (8 procedures)

*Navigates organizational hierarchy*

### sp_BringBillingForward

- **Schema:** dbo
- **Purpose:** Navigates organizational hierarchy
- **Modified:** 2025-12-08 11:57:53.300000
- **Warning:** No obvious termination condition found ⚠️

### sp_BringBillingForwardState

- **Schema:** dbo
- **Purpose:** Navigates organizational hierarchy
- **Modified:** 2024-11-11 11:57:58.070000
- **Warning:** No obvious termination condition found ⚠️

### sp_CopyBudgetAmounts

- **Schema:** dbo
- **Purpose:** Navigates organizational hierarchy
- **Modified:** 2013-12-05 09:17:04.373000
- **Warning:** No obvious termination condition found ⚠️

### sp_DSHeadings

- **Schema:** dbo
- **Purpose:** Navigates organizational hierarchy
- **Modified:** 2022-12-20 11:46:23.393000
- **Warning:** No obvious termination condition found ⚠️

### usp_BringAccountsForward

- **Schema:** dbo
- **Purpose:** Navigates organizational hierarchy
- **Modified:** 2022-05-04 15:44:34.360000
- **Termination:** Has explicit termination condition ✓

### usp_GetPOs

- **Schema:** dbo
- **Purpose:** Navigates organizational hierarchy
- **Modified:** 2025-10-13 23:47:07.697000
- **Termination:** Has explicit termination condition ✓

### usp_SetPricing

- **Schema:** dbo
- **Purpose:** Navigates organizational hierarchy
- **Modified:** 2025-11-30 16:55:35.343000
- **Also calls:** usp_SearchItemsByReqHKDS
- **Termination:** Has explicit termination condition ✓

### usp_getSDSDocsDistrict

- **Schema:** dbo
- **Purpose:** Navigates organizational hierarchy
- **Modified:** 2022-09-14 18:35:48.920000
- **Also calls:** usp_getSDSDocsSchool, usp_getSDSDocsUser
- **Termination:** Has explicit termination condition ✓

---

## Approval Chain (5 procedures)

*Processes approval workflow chain*

### bid2xls

- **Schema:** dbo
- **Purpose:** Processes approval workflow chain
- **Modified:** 2022-07-22 13:38:02.837000
- **Warning:** No obvious termination condition found ⚠️

### sp_FA_RequisitionsTotals

- **Schema:** dbo
- **Purpose:** Processes approval workflow chain
- **Modified:** 2022-05-19 15:15:12.133000
- **Warning:** No obvious termination condition found ⚠️

### sp_UpdatePricePlan

- **Schema:** dbo
- **Purpose:** Processes approval workflow chain
- **Modified:** 2009-03-25 06:55:28.397000
- **Warning:** No obvious termination condition found ⚠️

### usp_POStatusByState

- **Schema:** dbo
- **Purpose:** Processes approval workflow chain
- **Modified:** 2023-05-18 09:57:32.977000
- **Warning:** No obvious termination condition found ⚠️

### usp_getMyLastYearsReqs

- **Schema:** dbo
- **Purpose:** Processes approval workflow chain
- **Modified:** 2025-03-26 17:44:57.500000
- **Warning:** No obvious termination condition found ⚠️

---

## Document Chain (1 procedures)

*Follows document/attachment chain*

### usp_getSDSDocsUser

- **Schema:** dbo
- **Purpose:** Follows document/attachment chain
- **Modified:** 2022-09-14 18:36:11.577000
- **Termination:** Has explicit termination condition ✓

---

## Category Tree (4 procedures)

*Traverses category/catalog hierarchy*

### sp_BidCompareSummary

- **Schema:** dbo
- **Purpose:** Traverses category/catalog hierarchy
- **Modified:** 2022-10-14 16:48:05.437000
- **Warning:** No obvious termination condition found ⚠️

### sp_CatalogImporter

- **Schema:** dbo
- **Purpose:** Traverses category/catalog hierarchy
- **Modified:** 2012-11-14 20:04:32.920000
- **Warning:** No obvious termination condition found ⚠️

### usp_BidRanking

- **Schema:** dbo
- **Purpose:** Traverses category/catalog hierarchy
- **Modified:** 2015-03-24 13:07:04.690000
- **Warning:** No obvious termination condition found ⚠️

### usp_GetImageList

- **Schema:** dbo
- **Purpose:** Traverses category/catalog hierarchy
- **Modified:** 2025-03-21 09:02:46.013000
- **Termination:** Has explicit termination condition ✓

---

## Best Practices for Recursive Procedures

1. **Always include termination conditions** - Check for NULL, empty result, or max depth
2. **Use MAXRECURSION option** for CTEs (default is 100, max is 32767)
3. **Avoid deep recursion** - SQL Server has a max stack depth of 32
4. **Consider iterative alternatives** - WHILE loops may be more efficient
5. **Test with large datasets** - Recursion can cause stack overflow
6. **Add comments** explaining the recursion purpose and exit conditions
