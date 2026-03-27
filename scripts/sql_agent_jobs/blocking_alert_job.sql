/*
================================================================================
SQL Agent Job: Blocking Event Alert
================================================================================
Purpose: Alert DBA team when blocking events exceed threshold

Schedule: Every 15 minutes
Threshold: Blocking > 5 minutes
Alert Method: Database Mail

Prerequisites:
- Database Mail configured
- DBA operator created
- Access to dpa_EDSAdmin database

Installation: Execute this script on SQL Server to create the job
================================================================================
*/

USE [msdb];
GO

-- Drop job if exists (for re-deployment)
IF EXISTS (SELECT 1 FROM msdb.dbo.sysjobs WHERE name = 'Alert - Blocking Events')
BEGIN
    EXEC msdb.dbo.sp_delete_job @job_name = 'Alert - Blocking Events';
    PRINT '[INFO] Existing job dropped';
END
GO

PRINT '================================================================================';
PRINT 'Creating SQL Agent Job: Blocking Event Alert';
PRINT '================================================================================';
PRINT '';

-- Create operator (if not exists)
IF NOT EXISTS (SELECT 1 FROM msdb.dbo.sysoperators WHERE name = 'DBATeam')
BEGIN
    PRINT 'Creating operator: DBATeam';

    EXEC msdb.dbo.sp_add_operator
        @name = N'DBATeam',
        @enabled = 1,
        @email_address = N'dba-team@company.com';  -- UPDATE THIS EMAIL ADDRESS

    PRINT '[OK] Operator created';
END
ELSE
BEGIN
    PRINT '[INFO] Operator DBATeam already exists';
END
PRINT '';
GO

-- Create job
EXEC msdb.dbo.sp_add_job
    @job_name = N'Alert - Blocking Events',
    @enabled = 1,
    @description = N'Monitors dpa_EDSAdmin for blocking events >5 minutes and sends email alerts',
    @category_name = N'[Uncategorized (Local)]',
    @owner_login_name = N'sa';
GO

PRINT '[OK] Job created';
PRINT '';

-- Add job step
EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'Alert - Blocking Events',
    @step_name = N'Check for Blocking',
    @step_id = 1,
    @subsystem = N'TSQL',
    @command = N'
DECLARE @BlockingCount INT;
DECLARE @TotalBlockingMinutes FLOAT;
DECLARE @EmailBody NVARCHAR(MAX);
DECLARE @EmailSubject NVARCHAR(255);

-- Check dpa_EDSAdmin for recent blocking (last 15 minutes)
SELECT
    @BlockingCount = COUNT(*),
    @TotalBlockingMinutes = SUM(BLEETIMESECS) / 60.0
FROM dpa_EDSAdmin.dbo.CON_BLOCKING_SUM_1
WHERE DATEHOUR >= DATEADD(minute, -15, GETDATE())
    AND BLEETIMESECS > 300;  -- Over 5 minutes

IF @BlockingCount > 0
BEGIN
    -- Build alert email
    SET @EmailSubject = ''SQL Server Blocking Alert: '' + CAST(@BlockingCount AS VARCHAR) + '' events detected'';

    SET @EmailBody = ''<html><body>'';
    SET @EmailBody = @EmailBody + ''<h2>SQL Server Blocking Alert</h2>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Server:</strong> '' + @@SERVERNAME + ''</p>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Time:</strong> '' + CONVERT(VARCHAR, GETDATE(), 120) + ''</p>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Blocking Events:</strong> '' + CAST(@BlockingCount AS VARCHAR) + ''</p>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Total Blocking Time:</strong> '' + CAST(@TotalBlockingMinutes AS VARCHAR(20)) + '' minutes</p>'';
    SET @EmailBody = @EmailBody + ''<hr/>'';

    -- Get top 5 blocking events
    SET @EmailBody = @EmailBody + ''<h3>Top 5 Blocking Events</h3>'';
    SET @EmailBody = @EmailBody + ''<table border="1" cellpadding="5" cellspacing="0">'';
    SET @EmailBody = @EmailBody + ''<tr><th>Time</th><th>Type</th><th>Name</th><th>Blockee Hours</th></tr>'';

    SELECT @EmailBody = @EmailBody + ''<tr>''
        + ''<td>'' + CONVERT(VARCHAR, bs.DATEHOUR, 120) + ''</td>''
        + ''<td>'' + CASE bs.DIMENSIONTYPE WHEN ''P'' THEN ''Program'' WHEN ''D'' THEN ''Database'' WHEN ''E'' THEN ''Event'' ELSE ''Unknown'' END + ''</td>''
        + ''<td>'' + ISNULL(m.NAME, ''Unknown'') + ''</td>''
        + ''<td>'' + CAST(bs.BLEETIMESECS / 3600.0 AS VARCHAR(20)) + ''</td>''
        + ''</tr>''
    FROM (
        SELECT TOP 5 *
        FROM dpa_EDSAdmin.dbo.CON_BLOCKING_SUM_1
        WHERE DATEHOUR >= DATEADD(minute, -15, GETDATE())
            AND BLEETIMESECS > 300
        ORDER BY BLEETIMESECS DESC
    ) bs
    LEFT JOIN dpa_EDSAdmin.dbo.CONM_1 m ON bs.DIMENSIONID = m.ID;

    SET @EmailBody = @EmailBody + ''</table>'';
    SET @EmailBody = @EmailBody + ''<hr/>'';
    SET @EmailBody = @EmailBody + ''<p><em>This is an automated alert from SQL Server Performance Monitoring</em></p>'';
    SET @EmailBody = @EmailBody + ''</body></html>'';

    -- Send email alert
    EXEC msdb.dbo.sp_send_dbmail
        @profile_name = ''Default'',  -- UPDATE THIS IF YOUR PROFILE NAME IS DIFFERENT
        @recipients = ''dba-team@company.com'',  -- UPDATE THIS EMAIL ADDRESS
        @subject = @EmailSubject,
        @body = @EmailBody,
        @body_format = ''HTML'';

    PRINT ''[ALERT] Blocking detected: '' + CAST(@BlockingCount AS VARCHAR) + '' events, '' + CAST(@TotalBlockingMinutes AS VARCHAR) + '' minutes total'';
END
ELSE
BEGIN
    PRINT ''[OK] No blocking events detected'';
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

-- Schedule job (every 15 minutes)
EXEC msdb.dbo.sp_add_jobschedule
    @job_name = N'Alert - Blocking Events',
    @name = N'Every 15 minutes',
    @enabled = 1,
    @freq_type = 4,  -- Daily
    @freq_interval = 1,
    @freq_subday_type = 4,  -- Minutes
    @freq_subday_interval = 15,
    @active_start_time = 000000,  -- Midnight
    @active_end_time = 235959;  -- 11:59:59 PM
GO

PRINT '[OK] Schedule created (every 15 minutes)';
PRINT '';

-- Assign job to local server
EXEC msdb.dbo.sp_add_jobserver
    @job_name = N'Alert - Blocking Events',
    @server_name = N'(local)';
GO

PRINT '[OK] Job assigned to local server';
PRINT '';

PRINT '================================================================================';
PRINT 'BLOCKING ALERT JOB CREATED SUCCESSFULLY';
PRINT '================================================================================';
PRINT '';
PRINT 'Job Name: Alert - Blocking Events';
PRINT 'Schedule: Every 15 minutes';
PRINT 'Threshold: Blocking >5 minutes';
PRINT '';
PRINT 'NEXT STEPS:';
PRINT '  1. Update email addresses in job step (dba-team@company.com)';
PRINT '  2. Verify Database Mail profile name (currently: Default)';
PRINT '  3. Test job: EXEC msdb.dbo.sp_start_job @job_name = ''Alert - Blocking Events''';
PRINT '  4. Check job history: EXEC msdb.dbo.sp_help_jobhistory @job_name = ''Alert - Blocking Events''';
PRINT '';

GO
