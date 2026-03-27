/*
================================================================================
SQL Agent Job: I/O Latency Alert
================================================================================
Purpose: Alert on-call DBA when I/O latency exceeds critical thresholds

Schedule: Every 5 minutes
Threshold: Avg latency >100ms OR Max latency >500ms
Alert Method: Database Mail (High Priority)

Prerequisites:
- Database Mail configured
- On-call operator created
- Access to dpa_EDSAdmin database

Installation: Execute this script on SQL Server to create the job
================================================================================
*/

USE [msdb];
GO

-- Drop job if exists (for re-deployment)
IF EXISTS (SELECT 1 FROM msdb.dbo.sysjobs WHERE name = 'Alert - I/O Latency')
BEGIN
    EXEC msdb.dbo.sp_delete_job @job_name = 'Alert - I/O Latency';
    PRINT '[INFO] Existing job dropped';
END
GO

PRINT '================================================================================';
PRINT 'Creating SQL Agent Job: I/O Latency Alert';
PRINT '================================================================================';
PRINT '';

-- Create on-call operator (if not exists)
IF NOT EXISTS (SELECT 1 FROM msdb.dbo.sysoperators WHERE name = 'DBAOnCall')
BEGIN
    PRINT 'Creating operator: DBAOnCall';

    EXEC msdb.dbo.sp_add_operator
        @name = N'DBAOnCall',
        @enabled = 1,
        @email_address = N'dba-oncall@company.com',  -- UPDATE THIS EMAIL ADDRESS
        @pager_address = N'dba-oncall@company.com';  -- UPDATE FOR PAGER/SMS

    PRINT '[OK] Operator created';
END
ELSE
BEGIN
    PRINT '[INFO] Operator DBAOnCall already exists';
END
PRINT '';
GO

-- Create job
EXEC msdb.dbo.sp_add_job
    @job_name = N'Alert - I/O Latency',
    @enabled = 1,
    @description = N'Monitors dpa_EDSAdmin for high I/O latency (>100ms avg or >500ms max) and sends critical alerts',
    @category_name = N'[Uncategorized (Local)]',
    @owner_login_name = N'sa';
GO

PRINT '[OK] Job created';
PRINT '';

-- Add job step
EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'Alert - I/O Latency',
    @step_name = N'Check I/O Latency',
    @step_id = 1,
    @subsystem = N'TSQL',
    @command = N'
DECLARE @AvgReadLatency FLOAT;
DECLARE @AvgWriteLatency FLOAT;
DECLARE @MaxReadLatency FLOAT;
DECLARE @MaxWriteLatency FLOAT;
DECLARE @EmailBody NVARCHAR(MAX);
DECLARE @EmailSubject NVARCHAR(255);
DECLARE @AlertLevel VARCHAR(20);

-- Check I/O latency for last 10 minutes
SELECT
    @AvgReadLatency = AVG(READ_LATENCY),
    @AvgWriteLatency = AVG(WRITE_LATENCY),
    @MaxReadLatency = MAX(READ_LATENCY),
    @MaxWriteLatency = MAX(WRITE_LATENCY)
FROM dpa_EDSAdmin.dbo.CON_IO_DETAIL_1
WHERE D >= DATEADD(minute, -10, GETDATE());

-- Determine alert level and check if alert needed
IF @AvgReadLatency > 100 OR @MaxReadLatency > 500
BEGIN
    -- Determine severity
    IF @MaxReadLatency > 500
        SET @AlertLevel = ''CRITICAL'';
    ELSE IF @AvgReadLatency > 200
        SET @AlertLevel = ''HIGH'';
    ELSE
        SET @AlertLevel = ''WARNING'';

    -- Build alert email
    SET @EmailSubject = ''['' + @AlertLevel + ''] SQL Server I/O Latency Alert'';

    SET @EmailBody = ''<html><body>'';
    SET @EmailBody = @EmailBody + ''<h2 style="color: red;">I/O Latency Alert - '' + @AlertLevel + ''</h2>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Server:</strong> '' + @@SERVERNAME + ''</p>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Alert Time:</strong> '' + CONVERT(VARCHAR, GETDATE(), 120) + ''</p>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Severity:</strong> <span style="color: red;">'' + @AlertLevel + ''</span></p>'';
    SET @EmailBody = @EmailBody + ''<hr/>'';

    -- Metrics table
    SET @EmailBody = @EmailBody + ''<h3>I/O Latency Metrics (Last 10 Minutes)</h3>'';
    SET @EmailBody = @EmailBody + ''<table border="1" cellpadding="5" cellspacing="0">'';
    SET @EmailBody = @EmailBody + ''<tr><th>Metric</th><th>Read (ms)</th><th>Write (ms)</th><th>Status</th></tr>'';

    -- Average latency row
    SET @EmailBody = @EmailBody + ''<tr>''
        + ''<td><strong>Average Latency</strong></td>''
        + ''<td>'' + CAST(ROUND(@AvgReadLatency, 2) AS VARCHAR(20)) + ''</td>''
        + ''<td>'' + CAST(ROUND(@AvgWriteLatency, 2) AS VARCHAR(20)) + ''</td>''
        + ''<td>'' + CASE
            WHEN @AvgReadLatency > 200 THEN ''<span style="color: red;">CRITICAL</span>''
            WHEN @AvgReadLatency > 100 THEN ''<span style="color: orange;">HIGH</span>''
            ELSE ''<span style="color: green;">OK</span>''
        END + ''</td>''
        + ''</tr>'';

    -- Max latency row
    SET @EmailBody = @EmailBody + ''<tr>''
        + ''<td><strong>Maximum Latency</strong></td>''
        + ''<td>'' + CAST(ROUND(@MaxReadLatency, 2) AS VARCHAR(20)) + ''</td>''
        + ''<td>'' + CAST(ROUND(@MaxWriteLatency, 2) AS VARCHAR(20)) + ''</td>''
        + ''<td>'' + CASE
            WHEN @MaxReadLatency > 500 THEN ''<span style="color: red;">CRITICAL</span>''
            WHEN @MaxReadLatency > 200 THEN ''<span style="color: orange;">HIGH</span>''
            ELSE ''<span style="color: green;">OK</span>''
        END + ''</td>''
        + ''</tr>'';

    SET @EmailBody = @EmailBody + ''</table>'';
    SET @EmailBody = @EmailBody + ''<hr/>'';

    -- Interpretation
    SET @EmailBody = @EmailBody + ''<h3>Interpretation</h3>'';
    SET @EmailBody = @EmailBody + ''<ul>'';
    SET @EmailBody = @EmailBody + ''<li><strong>< 10ms:</strong> Excellent (SSD performance)</li>'';
    SET @EmailBody = @EmailBody + ''<li><strong>10-50ms:</strong> Acceptable (standard SSD)</li>'';
    SET @EmailBody = @EmailBody + ''<li><strong>50-100ms:</strong> Concerning (investigate)</li>'';
    SET @EmailBody = @EmailBody + ''<li><strong>> 100ms:</strong> Critical (urgent action required)</li>'';
    SET @EmailBody = @EmailBody + ''</ul>'';

    -- Recommended actions
    SET @EmailBody = @EmailBody + ''<h3>Recommended Actions</h3>'';
    SET @EmailBody = @EmailBody + ''<ol>'';
    SET @EmailBody = @EmailBody + ''<li>Check SAN/storage array health</li>'';
    SET @EmailBody = @EmailBody + ''<li>Review disk queue lengths (Performance Monitor)</li>'';
    SET @EmailBody = @EmailBody + ''<li>Check for blocking or long-running queries</li>'';
    SET @EmailBody = @EmailBody + ''<li>Review tempdb configuration and usage</li>'';
    SET @EmailBody = @EmailBody + ''<li>Check RAID controller cache status</li>'';
    SET @EmailBody = @EmailBody + ''<li>Monitor continuously for next 30 minutes</li>'';
    SET @EmailBody = @EmailBody + ''</ol>'';

    -- Query to run
    SET @EmailBody = @EmailBody + ''<h3>Diagnostic Query</h3>'';
    SET @EmailBody = @EmailBody + ''<pre style="background-color: #f0f0f0; padding: 10px;">'';
    SET @EmailBody = @EmailBody + ''SELECT TOP 20 * FROM dpa_EDSAdmin.dbo.CON_IO_DETAIL_1'';
    SET @EmailBody = @EmailBody + '' WHERE D >= DATEADD(minute, -10, GETDATE())'';
    SET @EmailBody = @EmailBody + '' ORDER BY READ_LATENCY DESC;'';
    SET @EmailBody = @EmailBody + ''</pre>'';

    SET @EmailBody = @EmailBody + ''<hr/>'';
    SET @EmailBody = @EmailBody + ''<p><em>This is an automated CRITICAL alert from SQL Server Performance Monitoring</em></p>'';
    SET @EmailBody = @EmailBody + ''</body></html>'';

    -- Send email alert (HIGH PRIORITY)
    EXEC msdb.dbo.sp_send_dbmail
        @profile_name = ''Default'',  -- UPDATE THIS IF YOUR PROFILE NAME IS DIFFERENT
        @recipients = ''dba-oncall@company.com'',  -- UPDATE THIS EMAIL ADDRESS
        @copy_recipients = ''dba-team@company.com'',  -- CC to team
        @subject = @EmailSubject,
        @body = @EmailBody,
        @body_format = ''HTML'',
        @importance = ''High'';

    PRINT ''[ALERT] '' + @AlertLevel + '': Avg Read Latency: '' + CAST(@AvgReadLatency AS VARCHAR) + ''ms, Max: '' + CAST(@MaxReadLatency AS VARCHAR) + ''ms'';
END
ELSE
BEGIN
    PRINT ''[OK] I/O latency within acceptable range (Avg: '' + CAST(@AvgReadLatency AS VARCHAR) + ''ms, Max: '' + CAST(@MaxReadLatency AS VARCHAR) + ''ms)'';
END
',
    @database_name = N'master',
    @on_success_action = 1,  -- Quit with success
    @on_fail_action = 2,  -- Quit with failure
    @retry_attempts = 0,
    @retry_interval = 0;
GO

PRINT '[OK] Job step created';
PRINT '';

-- Schedule job (every 5 minutes)
EXEC msdb.dbo.sp_add_jobschedule
    @job_name = N'Alert - I/O Latency',
    @name = N'Every 5 minutes',
    @enabled = 1,
    @freq_type = 4,  -- Daily
    @freq_interval = 1,
    @freq_subday_type = 4,  -- Minutes
    @freq_subday_interval = 5,
    @active_start_time = 000000,  -- Midnight
    @active_end_time = 235959;  -- 11:59:59 PM
GO

PRINT '[OK] Schedule created (every 5 minutes)';
PRINT '';

-- Assign job to local server
EXEC msdb.dbo.sp_add_jobserver
    @job_name = N'Alert - I/O Latency',
    @server_name = N'(local)';
GO

PRINT '[OK] Job assigned to local server';
PRINT '';

PRINT '================================================================================';
PRINT 'I/O LATENCY ALERT JOB CREATED SUCCESSFULLY';
PRINT '================================================================================';
PRINT '';
PRINT 'Job Name: Alert - I/O Latency';
PRINT 'Schedule: Every 5 minutes';
PRINT 'Thresholds: Avg >100ms OR Max >500ms';
PRINT 'Priority: HIGH';
PRINT '';
PRINT 'NEXT STEPS:';
PRINT '  1. Update email addresses (dba-oncall@company.com, dba-team@company.com)';
PRINT '  2. Verify Database Mail profile name (currently: Default)';
PRINT '  3. Adjust thresholds if needed (currently: 100ms avg, 500ms max)';
PRINT '  4. Configure pager/SMS for critical alerts';
PRINT '  5. Test job: EXEC msdb.dbo.sp_start_job @job_name = ''Alert - I/O Latency''';
PRINT '';
PRINT 'WARNING: This job runs frequently (every 5 minutes)';
PRINT '         Consider alert suppression if latency issues persist >30 minutes';
PRINT '';

GO
