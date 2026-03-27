/*
================================================================================
Enable READ_COMMITTED_SNAPSHOT Isolation
================================================================================
Purpose: Enable snapshot isolation to reduce blocking from read queries

Benefits:
- Reduces blocking for SELECT queries
- Read queries see consistent snapshot without locking writers
- Improves concurrency for mixed OLTP workloads

Considerations:
- Requires tempdb space for row versions (monitor growth)
- May cause increased I/O on tempdb
- Readers see slightly older data (by design)
- Test in development environment first

Prerequisites:
- Adequate tempdb space (recommend 50GB+ free)
- Approval from DBA team
- Application team notification
- Test environment validation complete

Rollback: See ROLLBACK section at end of file
================================================================================
*/

-- Set database context
USE [master];
GO

/*
================================================================================
PRE-IMPLEMENTATION CHECKS
================================================================================
*/

PRINT '================================================================================';
PRINT 'READ_COMMITTED_SNAPSHOT ISOLATION - PRE-IMPLEMENTATION CHECKS';
PRINT '================================================================================';
PRINT '';

-- Check tempdb size and free space
PRINT 'Checking tempdb space...';
SELECT
    'tempdb' as DatabaseName,
    SUM(size) * 8 / 1024.0 as CurrentSizeMB,
    SUM(CASE WHEN max_size = -1 THEN 1000000 ELSE max_size END) * 8 / 1024.0 as MaxSizeMB,
    (SUM(CASE WHEN max_size = -1 THEN 1000000 ELSE max_size END) - SUM(size)) * 8 / 1024.0 as AvailableMB
FROM tempdb.sys.database_files;

PRINT '';
PRINT 'tempdb should have at least 50 GB available space';
PRINT 'If insufficient space, abort and expand tempdb first';
PRINT '';

-- Check current snapshot isolation status
PRINT 'Current snapshot isolation status for user databases:';
SELECT
    name as DatabaseName,
    is_read_committed_snapshot_on as SnapshotEnabled,
    snapshot_isolation_state_desc as SnapshotState
FROM sys.databases
WHERE name NOT IN ('master', 'tempdb', 'model', 'msdb')
    AND state_desc = 'ONLINE'
ORDER BY name;

PRINT '';
PRINT 'Press Ctrl+C to abort if any checks failed';
PRINT 'Otherwise, continue to enable snapshot isolation...';
PRINT '';

GO

/*
================================================================================
ENABLE SNAPSHOT ISOLATION ON USER DATABASES
================================================================================
*/

PRINT '================================================================================';
PRINT 'ENABLING SNAPSHOT ISOLATION';
PRINT '================================================================================';
PRINT '';

-- EDS Database
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'EDS' AND is_read_committed_snapshot_on = 0)
BEGIN
    PRINT 'Enabling snapshot isolation on EDS...';

    ALTER DATABASE [EDS]
    SET READ_COMMITTED_SNAPSHOT ON
    WITH ROLLBACK IMMEDIATE;

    PRINT '[OK] EDS: Snapshot isolation enabled';
    PRINT '';
END
ELSE
BEGIN
    PRINT '[INFO] EDS: Snapshot isolation already enabled or database not found';
    PRINT '';
END
GO

-- Catalogs Database
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'Catalogs' AND is_read_committed_snapshot_on = 0)
BEGIN
    PRINT 'Enabling snapshot isolation on Catalogs...';

    ALTER DATABASE [Catalogs]
    SET READ_COMMITTED_SNAPSHOT ON
    WITH ROLLBACK IMMEDIATE;

    PRINT '[OK] Catalogs: Snapshot isolation enabled';
    PRINT '';
END
ELSE
BEGIN
    PRINT '[INFO] Catalogs: Snapshot isolation already enabled or database not found';
    PRINT '';
END
GO

-- VendorBids Database
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'VendorBids' AND is_read_committed_snapshot_on = 0)
BEGIN
    PRINT 'Enabling snapshot isolation on VendorBids...';

    ALTER DATABASE [VendorBids]
    SET READ_COMMITTED_SNAPSHOT ON
    WITH ROLLBACK IMMEDIATE;

    PRINT '[OK] VendorBids: Snapshot isolation enabled';
    PRINT '';
END
ELSE
BEGIN
    PRINT '[INFO] VendorBids: Snapshot isolation already enabled or database not found';
    PRINT '';
END
GO

-- ContentCentral Database
IF EXISTS (SELECT 1 FROM sys.databases WHERE name = 'ContentCentral' AND is_read_committed_snapshot_on = 0)
BEGIN
    PRINT 'Enabling snapshot isolation on ContentCentral...';

    ALTER DATABASE [ContentCentral]
    SET READ_COMMITTED_SNAPSHOT ON
    WITH ROLLBACK IMMEDIATE;

    PRINT '[OK] ContentCentral: Snapshot isolation enabled';
    PRINT '';
END
ELSE
BEGIN
    PRINT '[INFO] ContentCentral: Snapshot isolation already enabled or database not found';
    PRINT '';
END
GO

/*
================================================================================
POST-IMPLEMENTATION VERIFICATION
================================================================================
*/

PRINT '================================================================================';
PRINT 'POST-IMPLEMENTATION VERIFICATION';
PRINT '================================================================================';
PRINT '';

-- Verify snapshot isolation enabled
PRINT 'Verifying snapshot isolation status:';
SELECT
    name as DatabaseName,
    is_read_committed_snapshot_on as SnapshotEnabled,
    snapshot_isolation_state_desc as SnapshotState,
    CASE WHEN is_read_committed_snapshot_on = 1 THEN 'OK' ELSE 'NOT ENABLED' END as Status
FROM sys.databases
WHERE name IN ('EDS', 'Catalogs', 'VendorBids', 'ContentCentral')
ORDER BY name;

PRINT '';
PRINT '================================================================================';
PRINT 'SNAPSHOT ISOLATION ENABLED SUCCESSFULLY';
PRINT '================================================================================';
PRINT '';
PRINT 'NEXT STEPS:';
PRINT '  1. Monitor tempdb growth for next 48 hours';
PRINT '  2. Monitor blocking events (should decrease)';
PRINT '  3. Check application behavior for any issues';
PRINT '  4. Document implementation in change log';
PRINT '';
PRINT 'MONITORING QUERIES:';
PRINT '  - tempdb size: SELECT * FROM tempdb.sys.database_files';
PRINT '  - Version store usage: SELECT * FROM sys.dm_tran_version_store_space_usage';
PRINT '  - Active snapshots: SELECT * FROM sys.dm_tran_active_snapshot_database_transactions';
PRINT '';

GO

/*
================================================================================
ROLLBACK INSTRUCTIONS (IF NEEDED)
================================================================================

IMPORTANT: Only disable snapshot isolation if critical issues occur

Issues that might require rollback:
- tempdb growth causing disk space issues
- Severe performance degradation
- Application compatibility issues

ROLLBACK SCRIPT:
--------------------------------------------------------------------------------

-- Disable snapshot isolation on EDS
ALTER DATABASE [EDS]
SET READ_COMMITTED_SNAPSHOT OFF;

-- Disable snapshot isolation on Catalogs
ALTER DATABASE [Catalogs]
SET READ_COMMITTED_SNAPSHOT OFF;

-- Disable snapshot isolation on VendorBids
ALTER DATABASE [VendorBids]
SET READ_COMMITTED_SNAPSHOT OFF;

-- Disable snapshot isolation on ContentCentral
ALTER DATABASE [ContentCentral]
SET READ_COMMITTED_SNAPSHOT OFF;

-- Verify disabled
SELECT
    name,
    is_read_committed_snapshot_on
FROM sys.databases
WHERE name IN ('EDS', 'Catalogs', 'VendorBids', 'ContentCentral');

--------------------------------------------------------------------------------

After rollback, investigate root cause and consider alternative solutions:
- Query hints (NOLOCK, READPAST)
- Transaction optimization
- Index improvements
- Application-level retry logic

================================================================================
*/

/*
================================================================================
MONITORING QUERIES FOR ONGOING USE
================================================================================

-- Monitor tempdb version store space usage
SELECT
    DB_NAME(database_id) as DatabaseName,
    reserved_page_count * 8 / 1024.0 as ReservedSpaceMB,
    version_store_reserved_page_count * 8 / 1024.0 as VersionStoreMB
FROM sys.dm_tran_version_store_space_usage
ORDER BY version_store_reserved_page_count DESC;

-- Check for long-running snapshot transactions
SELECT
    transaction_id,
    transaction_sequence_num,
    commit_sequence_num,
    session_id,
    elapsed_time_seconds
FROM sys.dm_tran_active_snapshot_database_transactions
ORDER BY elapsed_time_seconds DESC;

-- Monitor tempdb growth over time
SELECT
    name,
    size * 8 / 1024.0 as CurrentSizeMB,
    max_size * 8 / 1024.0 as MaxSizeMB,
    growth,
    is_percent_growth
FROM tempdb.sys.database_files;

================================================================================
*/

PRINT 'Script execution complete.';
PRINT 'Review output above for any errors.';
PRINT '';
