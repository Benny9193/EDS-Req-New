/*
================================================================================
  UNDO DOWNLOADED REQUISITION - Change status back to "On Hold"
================================================================================

  PURPOSE:
    Changes a requisition from "Requisition Downloaded" (StatusId=35, Code='D')
    back to "On Hold" (StatusId=1, Code='H') by inserting a new Approvals row.

  HOW IT WORKS:
    The EDS requisition system determines current status by looking at the
    latest (MAX ApprovalId) row in the Approvals table. By inserting a new
    row with StatusId=1 (On Hold), the requisition's status changes back.

  VERIFIED AGAINST LIVE DATABASE (2026-03-04):
    - StatusTable: StatusId=1 (Code='H', Name='On Hold')
    - StatusTable: StatusId=35 (Code='D', Name='Requisition Downloaded')
    - Approvals columns: RequisitionId, StatusId, ApprovalById, ApproverId, Level, ApprovalDate
    - vw_RequisitionStatus: Downloaded shows as "Requisition Downloaded by [NAME]"
    - vw_RequisitionStatus: On Hold shows as "On Hold by [NAME]"
    - PO records: Not always present for downloaded reqs (no PO cleanup needed)

  USAGE:
    1. Replace @RequisitionId with the actual RequisitionId (NOT RequisitionNumber!)
       - To find the RequisitionId, use the lookup query in Step 0 below
    2. Run Step 1 (PREVIEW) to verify the requisition is currently downloaded
    3. Run Step 2 (EXECUTE) to perform the change
    4. Run Step 3 (VERIFY) to confirm the status changed

  ALTERNATIVE - USE STORED PROC:
    If you have a valid SessionID, you can use the same stored proc the UI uses:
       EXEC sp_FA_UpdateRequisitionStatus @pSessionId=<SessionId>, @pRequisitionId=<ReqId>, @pStatusCode='H'
    or EXEC sp_FA_ApproveReq @pSessionId=<SessionId>, @pRequisitionId=<ReqId>, @pStatusCode='H'

================================================================================
*/

-- ============================================
-- STEP 0: FIND THE REQUISITION ID
-- ============================================
-- Replace the WHERE clause to match your requisition(s).
-- RequisitionNumber is NOT the same as RequisitionId!

SELECT
    R.RequisitionId,
    R.RequisitionNumber,
    ST.StatusCode,
    ST.Name AS CurrentStatus,
    vwRS.StatusDesc AS DisplayStatus,
    A.ApprovalById,
    A.ApprovalDate
FROM Requisitions R
JOIN Approvals A ON A.RequisitionId = R.RequisitionId
    AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
JOIN StatusTable ST ON ST.StatusId = A.StatusId
LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
WHERE vwRS.StatusDesc LIKE '%Downloaded%'
    -- Narrow down by district/budget or requisition numbers:
    -- AND R.RequisitionNumber IN (5, 26, 36, 41, 42, 45)
ORDER BY R.RequisitionNumber;
GO


-- ============================================
-- STEP 1: PREVIEW - Confirm the requisition is downloaded
-- ============================================
-- SET THIS to the RequisitionId from Step 0
DECLARE @RequisitionId INT = 0;  -- <-- REPLACE WITH ACTUAL RequisitionId

SELECT
    R.RequisitionId,
    R.RequisitionNumber,
    ST.StatusId,
    ST.StatusCode,
    ST.Name AS CurrentApprovalStatus,
    A.ApprovalById,
    A.ApproverId,
    A.Level,
    A.ApprovalDate
FROM Requisitions R
JOIN Approvals A ON A.RequisitionId = R.RequisitionId
    AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
JOIN StatusTable ST ON ST.StatusId = A.StatusId
WHERE R.RequisitionId = @RequisitionId;

-- Expected: StatusCode='D', StatusId=35, Name='Requisition Downloaded'
-- If you see something else, STOP - the requisition is not in Downloaded status.
GO


-- ============================================
-- STEP 2: EXECUTE - Insert new "On Hold" approval row
-- ============================================
-- This changes the requisition status from "Downloaded" to "On Hold"
-- by inserting a new approval record (the system reads the latest one).

DECLARE @RequisitionId INT = 0;  -- <-- REPLACE WITH ACTUAL RequisitionId

BEGIN TRANSACTION;

    -- Safety check: Only proceed if current status is 'D' (Downloaded)
    IF EXISTS (
        SELECT 1
        FROM Approvals A
        JOIN StatusTable ST ON ST.StatusId = A.StatusId
        WHERE A.RequisitionId = @RequisitionId
          AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = @RequisitionId)
          AND ST.StatusCode = 'D'
    )
    BEGIN
        INSERT INTO Approvals (RequisitionId, StatusId, ApprovalById, ApproverId, Level, ApprovalDate)
        SELECT
            A.RequisitionId,
            1,              -- StatusId=1 = "On Hold" (Code='H')
            A.ApprovalById, -- Keep same user
            A.ApproverId,   -- Keep same approver (usually NULL for downloaded)
            A.Level,        -- Keep same level
            GETDATE()       -- New timestamp
        FROM Approvals A
        WHERE A.RequisitionId = @RequisitionId
          AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = @RequisitionId);

        PRINT 'SUCCESS: Requisition ' + CAST(@RequisitionId AS VARCHAR) + ' changed to On Hold.';
    END
    ELSE
    BEGIN
        PRINT 'SKIPPED: Requisition ' + CAST(@RequisitionId AS VARCHAR) + ' is NOT currently in Downloaded status.';
    END

COMMIT TRANSACTION;
GO


-- ============================================
-- STEP 3: VERIFY - Confirm the change took effect
-- ============================================
DECLARE @RequisitionId INT = 0;  -- <-- REPLACE WITH ACTUAL RequisitionId

-- Check latest approval status
SELECT
    R.RequisitionId,
    R.RequisitionNumber,
    ST.StatusId,
    ST.StatusCode,
    ST.Name AS NewApprovalStatus,
    A.ApprovalDate
FROM Requisitions R
JOIN Approvals A ON A.RequisitionId = R.RequisitionId
    AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
JOIN StatusTable ST ON ST.StatusId = A.StatusId
WHERE R.RequisitionId = @RequisitionId;

-- Expected: StatusCode='H', StatusId=1, Name='On Hold'

-- Check what vw_RequisitionStatus shows
SELECT StatusId, StatusCode, StatusDesc, BaseStatus
FROM vw_RequisitionStatus
WHERE RequisitionId = @RequisitionId;

-- Expected: StatusDesc='On Hold by [NAME]', BaseStatus='On Hold'
GO


-- ============================================
-- BULK VERSION: Undo multiple downloaded requisitions at once
-- ============================================
-- Uncomment and customize the WHERE clause to match your requisitions.
-- ALWAYS preview first, then execute!

/*
-- PREVIEW: See which reqs will be affected
SELECT
    R.RequisitionId,
    R.RequisitionNumber,
    vwRS.StatusDesc
FROM Requisitions R
JOIN Approvals A ON A.RequisitionId = R.RequisitionId
    AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = R.RequisitionId)
JOIN StatusTable ST ON ST.StatusId = A.StatusId
LEFT JOIN vw_RequisitionStatus vwRS ON vwRS.RequisitionId = R.RequisitionId
WHERE ST.StatusCode = 'D'
    AND R.RequisitionId IN (
        -- List your RequisitionIds here:
        12345, 67890
    );

-- EXECUTE: Bulk undo
BEGIN TRANSACTION;

    INSERT INTO Approvals (RequisitionId, StatusId, ApprovalById, ApproverId, Level, ApprovalDate)
    SELECT
        A.RequisitionId,
        1,              -- On Hold
        A.ApprovalById,
        A.ApproverId,
        A.Level,
        GETDATE()
    FROM Approvals A
    JOIN StatusTable ST ON ST.StatusId = A.StatusId
    WHERE A.RequisitionId IN (
            -- Same list of RequisitionIds:
            12345, 67890
          )
      AND A.ApprovalId = (SELECT MAX(ApprovalId) FROM Approvals WHERE RequisitionId = A.RequisitionId)
      AND ST.StatusCode = 'D';

    PRINT 'Bulk undo complete. Rows inserted: ' + CAST(@@ROWCOUNT AS VARCHAR);

COMMIT TRANSACTION;
*/
