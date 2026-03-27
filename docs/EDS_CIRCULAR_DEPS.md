# EDS Database - Circular Dependency Analysis

Generated: 2026-01-09 12:13:40

---

## Summary

| Metric | Count |
|--------|-------|
| Total Procedures | 395 |
| Procedures with calls | 127 |
| Self-calling procedures | 34 |
| Circular dependency chains | 0 |
| Max call depth | 4 |

---

## Self-Calling Procedures (Recursive)

These procedures call themselves, which may be intentional recursion:

- `bid2xls`
- `sp_AwardBidHeader`
- `sp_BidCompareSummary`
- `sp_BidCopyWithIncrease`
- `sp_BringBillingForward`
- `sp_BringBillingForwardState`
- `sp_CCUpdateUserAccounts_2`
- `sp_CXmlLogin`
- `sp_CatalogImporter`
- `sp_CopyBudgetAmounts`
- `sp_DSHeadings`
- `sp_FA_RequisitionsTotals`
- `sp_UpdatePricePlan`
- `usp_BidMatchRefs`
- `usp_BidRanking`
- `usp_BringAccountsForward`
- `usp_CopyRequisition`
- `usp_GetImageList`
- `usp_GetPODetail`
- `usp_GetPODetail_Test`
- `usp_GetPOs`
- `usp_OrderEZVendors`
- `usp_POStatusByState`
- `usp_SDSDocs`
- `usp_SearchItemsByReqHKDS`
- `usp_SearchItemsByReqHKDSDavid`
- `usp_SearchVendors`
- `usp_SetPricing`
- `usp_TransactionLogMover`
- `usp_VendorStatsCYvsLY`
- `usp_WaitingTasks`
- `usp_getMyLastYearsReqs`
- `usp_getSDSDocsDistrict`
- `usp_getSDSDocsUser`

**Note:** Self-recursion can be intentional (tree traversal, hierarchical data) or a bug. Review each case.

---

## Circular Dependency Chains

*No circular dependency chains found (good!)*

---

## Deepest Call Chains

Procedures with the deepest call hierarchies:

| Procedure | Max Depth |
|-----------|----------|
| sp_ProcessCopyRequests | 4 |
| usp_getSDSDocsAll | 4 |
| sp_AddISBN | 4 |
| sp_CopyReqs | 3 |
| sp_easyadd | 3 |
| sp_CombineReqs | 3 |
| usp_SetPricing_SearchDataDB | 3 |
| usp_getSDSDocsDistrict | 3 |
| usp_GetVendorPricing | 3 |
| sp_DeleteEmptyReqs | 3 |
| usp_SearchItemsByReqHKDSError | 3 |
| usp_SearchItemsByReqHKDS_David | 3 |
| sp_ISBNAdd | 3 |
| sp_ConvertReadyBatches | 3 |
| sp_ConvertReqs | 2 |
| sp_CopyReqsBulk | 2 |
| sp_CreateOrderBook03 | 2 |
| sp_UpdateReqDetailItem | 2 |
| sp_UpdateReqDetailPricePlan | 2 |
| sp_UpdateReqHeader | 2 |
| dt_addtosourcecontrol_u | 2 |
| dt_checkinobject_u | 2 |
| dt_checkoutobject_u | 2 |
| usp_GetPODetail | 2 |
| dt_isundersourcecontrol_u | 2 |

**Note:** Deep call chains (>5 levels) may indicate complex business logic that could benefit from refactoring.

---

## Recommendations

### Self-Calling Procedures
1. Verify each self-calling procedure has proper termination conditions
2. Check for maximum recursion depth limits (SQL Server default: 32)
3. Consider using CTEs for recursive operations instead

