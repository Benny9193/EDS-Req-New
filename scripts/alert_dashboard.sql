/*
================================================================================
SQL Server Performance Monitoring Dashboard
================================================================================
Purpose: Daily summary of key performance metrics from dpa_EDSAdmin

Run this query each morning to get overnight performance summary.
Review all sections for potential issues requiring investigation.

Generated: 2025-12-04 17:27:48
================================================================================
*/

USE dpa_EDSAdmin;
GO

PRINT '================================================================================'
PRINT 'SQL SERVER PERFORMANCE DASHBOARD - 2025-12-04'
PRINT '================================================================================'
PRINT ''

/*
================================================================================
SECTION 1: NEW MISSING INDEXES (Last 24 Hours)
================================================================================
High-impact missing index recommendations identified since yesterday.
Action: Review indexes with EST_SAVING > 95% for immediate implementation.
*/

PRINT '1. NEW MISSING INDEXES (Last 24 Hours)'
PRINT '--------------------------------------'

SELECT TOP 20
    CONVERT(VARCHAR, w.D, 120) as DateIdentified,
    w.EST_SAVING as EstSavingPercent,
    w.SQL_EXECS as Executions,
    fq.ODATABASE as DatabaseName,
    fq.OSCHEMA + '.' + fq.ONAME as TableName,
    fq.OINDEX_COLUMNS as IndexColumns,
    CASE
        WHEN w.EST_SAVING > 95 THEN 'CRITICAL'
        WHEN w.EST_SAVING > 80 THEN 'HIGH'
        WHEN w.EST_SAVING > 50 THEN 'MEDIUM'
        ELSE 'LOW'
    END as Priority
FROM CON_WHATIF_SRC_1 w
LEFT JOIN CON_FQ_OBJECT_1 fq ON w.IDX_ID = fq.ID
WHERE w.D >= DATEADD(day, -1, GETDATE())
    AND w.EST_SAVING >= 50  -- Only show indexes with 50%+ improvement potential
ORDER BY w.EST_SAVING DESC, w.SQL_EXECS DESC;

DECLARE @NewHighImpactIndexes INT
SELECT @NewHighImpactIndexes = COUNT(*)
FROM CON_WHATIF_SRC_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND EST_SAVING > 95;

PRINT ''
PRINT 'Summary: ' + CAST(@NewHighImpactIndexes AS VARCHAR) + ' new high-impact indexes (>95% improvement) detected'
PRINT ''

/*
================================================================================
SECTION 2: BLOCKING EVENTS (Last 24 Hours)
================================================================================
Blocking events that caused significant wait time.
Action: Investigate events >5 minutes. Review query patterns causing blocks.
*/

PRINT '2. BLOCKING EVENTS (Last 24 Hours)'
PRINT '-----------------------------------'

SELECT TOP 15
    CONVERT(VARCHAR, bs.DATEHOUR, 120) as BlockingDateTime,
    CASE bs.DIMENSIONTYPE
        WHEN 'P' THEN 'Program'
        WHEN 'D' THEN 'Database'
        WHEN 'E' THEN 'Event'
        ELSE 'Unknown'
    END as BlockingType,
    m.NAME as BlockingEntity,
    CAST(bs.BLEETIMESECS / 60.0 AS DECIMAL(10,2)) as BlockeeMinutes,
    CAST(bs.BLERTIMESECS / 60.0 AS DECIMAL(10,2)) as BlockerMinutes,
    CASE
        WHEN bs.BLEETIMESECS > 3600 THEN 'CRITICAL'
        WHEN bs.BLEETIMESECS > 300 THEN 'HIGH'
        WHEN bs.BLEETIMESECS > 60 THEN 'MEDIUM'
        ELSE 'LOW'
    END as Severity
FROM CON_BLOCKING_SUM_1 bs
LEFT JOIN CONM_1 m ON bs.DIMENSIONID = m.ID
WHERE bs.DATEHOUR >= DATEADD(day, -1, GETDATE())
    AND bs.BLEETIMESECS > 60  -- Only show blocking >1 minute
ORDER BY bs.BLEETIMESECS DESC;

DECLARE @TotalBlockingHours DECIMAL(10,2)
DECLARE @BlockingEventCount INT

SELECT
    @TotalBlockingHours = CAST(SUM(BLEETIMESECS) / 3600.0 AS DECIMAL(10,2)),
    @BlockingEventCount = COUNT(*)
FROM CON_BLOCKING_SUM_1
WHERE DATEHOUR >= DATEADD(day, -1, GETDATE())
    AND BLEETIMESECS > 60;

PRINT ''
PRINT 'Summary: ' + CAST(@BlockingEventCount AS VARCHAR) + ' blocking events, ' + CAST(@TotalBlockingHours AS VARCHAR) + ' hours total blockee time'
PRINT ''

/*
================================================================================
SECTION 3: I/O LATENCY SPIKES (Last 24 Hours)
================================================================================
Periods where disk I/O latency exceeded acceptable thresholds.
Action: Investigate spikes >100ms average. Check storage health.
*/

PRINT '3. I/O LATENCY SPIKES (Last 24 Hours)'
PRINT '--------------------------------------'

SELECT TOP 20
    CONVERT(VARCHAR, D, 120) as DateTime,
    CAST(READ_LATENCY AS DECIMAL(10,2)) as AvgReadLatencyMS,
    CAST(WRITE_LATENCY AS DECIMAL(10,2)) as AvgWriteLatencyMS,
    CAST(TOTAL_LATENCY AS DECIMAL(10,2)) as TotalLatencyMS,
    CASE
        WHEN READ_LATENCY > 200 OR WRITE_LATENCY > 200 THEN 'CRITICAL'
        WHEN READ_LATENCY > 100 OR WRITE_LATENCY > 100 THEN 'HIGH'
        WHEN READ_LATENCY > 50 OR WRITE_LATENCY > 50 THEN 'MEDIUM'
        ELSE 'LOW'
    END as Severity
FROM CON_IO_DETAIL_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND (READ_LATENCY > 50 OR WRITE_LATENCY > 50)  -- Only show problematic latency
ORDER BY TOTAL_LATENCY DESC;

DECLARE @MaxReadLatency DECIMAL(10,2)
DECLARE @AvgReadLatency DECIMAL(10,2)
DECLARE @HighLatencyCount INT

SELECT
    @MaxReadLatency = CAST(MAX(READ_LATENCY) AS DECIMAL(10,2)),
    @AvgReadLatency = CAST(AVG(READ_LATENCY) AS DECIMAL(10,2)),
    @HighLatencyCount = COUNT(*)
FROM CON_IO_DETAIL_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND READ_LATENCY > 100;

PRINT ''
PRINT 'Summary: ' + CAST(@HighLatencyCount AS VARCHAR) + ' high latency events (>100ms), Max: ' + CAST(@MaxReadLatency AS VARCHAR) + 'ms, Avg: ' + CAST(@AvgReadLatency AS VARCHAR) + 'ms'
PRINT ''

/*
================================================================================
SECTION 4: SLOW QUERIES (Last 24 Hours)
================================================================================
Queries with excessive buffer gets (logical reads), indicating potential issues.
Action: Review queries >10M buffer gets. Check for missing indexes or bad plans.
*/

PRINT '4. SLOW QUERIES (Last 24 Hours)'
PRINT '--------------------------------'

SELECT TOP 15
    CONVERT(VARCHAR, qp.D, 120) as DateTime,
    qp.SQL_HASH as QueryHash,
    CAST(qp.SQL_BUFFER_GETS / 1000000.0 AS DECIMAL(10,2)) as BufferGetsMillions,
    qp.SQL_EXECS as Executions,
    CAST(qp.SQL_BUFFER_GETS / NULLIF(qp.SQL_EXECS, 0) AS BIGINT) as AvgBufferGetsPerExec,
    CAST(qp.SQL_ELAPSED_TIME / 1000.0 AS DECIMAL(10,2)) as ElapsedTimeSeconds,
    CASE
        WHEN qp.SQL_BUFFER_GETS > 100000000 THEN 'CRITICAL'
        WHEN qp.SQL_BUFFER_GETS > 10000000 THEN 'HIGH'
        WHEN qp.SQL_BUFFER_GETS > 1000000 THEN 'MEDIUM'
        ELSE 'LOW'
    END as Severity
FROM CON_QUERY_PLAN_1 qp
WHERE qp.D >= DATEADD(day, -1, GETDATE())
    AND qp.SQL_BUFFER_GETS > 10000000  -- >10M buffer gets
ORDER BY qp.SQL_BUFFER_GETS DESC;

DECLARE @SlowQueryCount INT
SELECT @SlowQueryCount = COUNT(DISTINCT SQL_HASH)
FROM CON_QUERY_PLAN_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND SQL_BUFFER_GETS > 10000000;

PRINT ''
PRINT 'Summary: ' + CAST(@SlowQueryCount AS VARCHAR) + ' distinct slow queries detected (>10M buffer gets)'
PRINT ''

/*
================================================================================
SECTION 5: DATABASE HEALTH SUMMARY
================================================================================
Overall health indicators for the past 24 hours.
*/

PRINT '5. DATABASE HEALTH SUMMARY (Last 24 Hours)'
PRINT '-------------------------------------------'

DECLARE @HealthScore INT = 100

-- Deduct points for issues
IF @NewHighImpactIndexes > 10 SET @HealthScore = @HealthScore - 20
IF @NewHighImpactIndexes > 5 SET @HealthScore = @HealthScore - 10

IF @TotalBlockingHours > 5 SET @HealthScore = @HealthScore - 25
IF @TotalBlockingHours > 1 SET @HealthScore = @HealthScore - 10

IF @HighLatencyCount > 100 SET @HealthScore = @HealthScore - 25
IF @HighLatencyCount > 50 SET @HealthScore = @HealthScore - 15

IF @SlowQueryCount > 20 SET @HealthScore = @HealthScore - 20
IF @SlowQueryCount > 10 SET @HealthScore = @HealthScore - 10

SELECT
    'Database Health Score' as Metric,
    CAST(@HealthScore AS VARCHAR) + '/100' as Value,
    CASE
        WHEN @HealthScore >= 90 THEN 'EXCELLENT'
        WHEN @HealthScore >= 75 THEN 'GOOD'
        WHEN @HealthScore >= 60 THEN 'FAIR'
        WHEN @HealthScore >= 40 THEN 'POOR'
        ELSE 'CRITICAL'
    END as Status

UNION ALL

SELECT
    'New High-Impact Indexes',
    CAST(@NewHighImpactIndexes AS VARCHAR),
    CASE
        WHEN @NewHighImpactIndexes = 0 THEN 'GOOD'
        WHEN @NewHighImpactIndexes < 5 THEN 'FAIR'
        WHEN @NewHighImpactIndexes < 10 THEN 'POOR'
        ELSE 'CRITICAL'
    END

UNION ALL

SELECT
    'Blocking Events (Hours)',
    CAST(@TotalBlockingHours AS VARCHAR),
    CASE
        WHEN @TotalBlockingHours = 0 THEN 'GOOD'
        WHEN @TotalBlockingHours < 1 THEN 'FAIR'
        WHEN @TotalBlockingHours < 5 THEN 'POOR'
        ELSE 'CRITICAL'
    END

UNION ALL

SELECT
    'High I/O Latency Events',
    CAST(@HighLatencyCount AS VARCHAR),
    CASE
        WHEN @HighLatencyCount = 0 THEN 'GOOD'
        WHEN @HighLatencyCount < 50 THEN 'FAIR'
        WHEN @HighLatencyCount < 100 THEN 'POOR'
        ELSE 'CRITICAL'
    END

UNION ALL

SELECT
    'Slow Queries',
    CAST(@SlowQueryCount AS VARCHAR),
    CASE
        WHEN @SlowQueryCount = 0 THEN 'GOOD'
        WHEN @SlowQueryCount < 10 THEN 'FAIR'
        WHEN @SlowQueryCount < 20 THEN 'POOR'
        ELSE 'CRITICAL'
    END;

PRINT ''
PRINT '================================================================================'
PRINT 'END OF DASHBOARD - ' + CONVERT(VARCHAR, GETDATE(), 120)
PRINT '================================================================================'
PRINT ''
PRINT 'RECOMMENDED ACTIONS:'
PRINT '  1. Review all CRITICAL and HIGH severity items'
PRINT '  2. Implement high-impact missing indexes (>95% improvement)'
PRINT '  3. Investigate blocking events >5 minutes'
PRINT '  4. Check storage health if I/O latency >100ms'
PRINT '  5. Analyze slow queries for optimization opportunities'
PRINT ''

GO
