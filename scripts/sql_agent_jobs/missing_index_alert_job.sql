/*
================================================================================
SQL Agent Job: Missing Index Alert
================================================================================
Purpose: Alert DBA team when new high-impact missing indexes are identified

Schedule: Daily at 8:00 AM
Threshold: EST_SAVING > 95%
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
IF EXISTS (SELECT 1 FROM msdb.dbo.sysjobs WHERE name = 'Alert - Missing Indexes')
BEGIN
    EXEC msdb.dbo.sp_delete_job @job_name = 'Alert - Missing Indexes';
    PRINT '[INFO] Existing job dropped';
END
GO

PRINT '================================================================================';
PRINT 'Creating SQL Agent Job: Missing Index Alert';
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
    @job_name = N'Alert - Missing Indexes',
    @enabled = 1,
    @description = N'Monitors dpa_EDSAdmin for new high-impact missing index recommendations (>95% estimated saving) and sends daily email alerts',
    @category_name = N'[Uncategorized (Local)]',
    @owner_login_name = N'sa';
GO

PRINT '[OK] Job created';
PRINT '';

-- Add job step
EXEC msdb.dbo.sp_add_jobstep
    @job_name = N'Alert - Missing Indexes',
    @step_name = N'Check for New Missing Indexes',
    @step_id = 1,
    @subsystem = N'TSQL',
    @command = N'
DECLARE @NewMissingIndexes INT;
DECLARE @EmailBody NVARCHAR(MAX);
DECLARE @EmailSubject NVARCHAR(255);

-- Check for new high-impact missing indexes (last 24 hours)
SELECT @NewMissingIndexes = COUNT(*)
FROM dpa_EDSAdmin.dbo.CON_WHATIF_SRC_1
WHERE D >= DATEADD(day, -1, GETDATE())
    AND EST_SAVING > 95;  -- Over 95% potential improvement

IF @NewMissingIndexes > 0
BEGIN
    -- Build alert email
    SET @EmailSubject = ''SQL Server Missing Index Alert: '' + CAST(@NewMissingIndexes AS VARCHAR) + '' high-impact recommendations'';

    SET @EmailBody = ''<html><body>'';
    SET @EmailBody = @EmailBody + ''<h2>Missing Index Recommendations Alert</h2>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Server:</strong> '' + @@SERVERNAME + ''</p>'';
    SET @EmailBody = @EmailBody + ''<p><strong>Report Date:</strong> '' + CONVERT(VARCHAR, GETDATE(), 120) + ''</p>'';
    SET @EmailBody = @EmailBody + ''<p><strong>New High-Impact Indexes:</strong> '' + CAST(@NewMissingIndexes AS VARCHAR) + '' (>95% estimated improvement)</p>'';
    SET @EmailBody = @EmailBody + ''<hr/>'';

    -- Get top 10 new missing indexes
    SET @EmailBody = @EmailBody + ''<h3>Top 10 New Missing Index Recommendations</h3>'';
    SET @EmailBody = @EmailBody + ''<table border="1" cellpadding="5" cellspacing="0">'';
    SET @EmailBody = @EmailBody + ''<tr><th>Date</th><th>Database</th><th>Table</th><th>Est. Saving %</th><th>Executions</th></tr>'';

    SELECT @EmailBody = @EmailBody + ''<tr>''
        + ''<td>'' + CONVERT(VARCHAR, w.D, 120) + ''</td>''
        + ''<td>'' + ISNULL(fq.ODATABASE, ''Unknown'') + ''</td>''
        + ''<td>'' + ISNULL(fq.OSCHEMA + ''.'' + fq.ONAME, ''Unknown'') + ''</td>''
        + ''<td>'' + CAST(w.EST_SAVING AS VARCHAR(20)) + ''</td>''
        + ''<td>'' + CAST(w.SQL_EXECS AS VARCHAR(20)) + ''</td>''
        + ''</tr>''
    FROM (
        SELECT TOP 10 *
        FROM dpa_EDSAdmin.dbo.CON_WHATIF_SRC_1
        WHERE D >= DATEADD(day, -1, GETDATE())
            AND EST_SAVING > 95
        ORDER BY EST_SAVING DESC, SQL_EXECS DESC
    ) w
    LEFT JOIN dpa_EDSAdmin.dbo.CON_FQ_OBJECT_1 fq ON w.IDX_ID = fq.ID;

    SET @EmailBody = @EmailBody + ''</table>'';
    SET @EmailBody = @EmailBody + ''<hr/>'';
    SET @EmailBody = @EmailBody + ''<h3>Recommended Actions</h3>'';
    SET @EmailBody = @EmailBody + ''<ol>'';
    SET @EmailBody = @EmailBody + ''<li>Run extract_missing_indexes.py to get full details</li>'';
    SET @EmailBody = @EmailBody + ''<li>Review execution plans for affected queries</li>'';
    SET @EmailBody = @EmailBody + ''<li>Generate CREATE INDEX scripts using generate_index_scripts.py</li>'';
    SET @EmailBody = @EmailBody + ''<li>Test in development environment</li>'';
    SET @EmailBody = @EmailBody + ''<li>Schedule deployment to production</li>'';
    SET @EmailBody = @EmailBody + ''</ol>'';
    SET @EmailBody = @EmailBody + ''<p><em>This is an automated alert from SQL Server Performance Monitoring</em></p>'';
    SET @EmailBody = @EmailBody + ''</body></html>'';

    -- Send email alert
    EXEC msdb.dbo.sp_send_dbmail
        @profile_name = ''Default'',  -- UPDATE THIS IF YOUR PROFILE NAME IS DIFFERENT
        @recipients = ''dba-team@company.com'',  -- UPDATE THIS EMAIL ADDRESS
        @subject = @EmailSubject,
        @body = @EmailBody,
        @body_format = ''HTML'';

    PRINT ''[ALERT] '' + CAST(@NewMissingIndexes AS VARCHAR) + '' new high-impact missing indexes detected'';
END
ELSE
BEGIN
    PRINT ''[OK] No new high-impact missing indexes detected in last 24 hours'';
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

-- Schedule job (daily at 8:00 AM)
EXEC msdb.dbo.sp_add_jobschedule
    @job_name = N'Alert - Missing Indexes',
    @name = N'Daily at 8 AM',
    @enabled = 1,
    @freq_type = 4,  -- Daily
    @freq_interval = 1,
    @freq_subday_type = 1,  -- At the specified time
    @freq_subday_interval = 0,
    @active_start_time = 080000;  -- 8:00 AM
GO

PRINT '[OK] Schedule created (daily at 8:00 AM)';
PRINT '';

-- Assign job to local server
EXEC msdb.dbo.sp_add_jobserver
    @job_name = N'Alert - Missing Indexes',
    @server_name = N'(local)';
GO

PRINT '[OK] Job assigned to local server';
PRINT '';

PRINT '================================================================================';
PRINT 'MISSING INDEX ALERT JOB CREATED SUCCESSFULLY';
PRINT '================================================================================';
PRINT '';
PRINT 'Job Name: Alert - Missing Indexes';
PRINT 'Schedule: Daily at 8:00 AM';
PRINT 'Threshold: EST_SAVING > 95%';
PRINT '';
PRINT 'NEXT STEPS:';
PRINT '  1. Update email addresses in job step (dba-team@company.com)';
PRINT '  2. Verify Database Mail profile name (currently: Default)';
PRINT '  3. Adjust threshold if needed (currently >95% improvement)';
PRINT '  4. Test job: EXEC msdb.dbo.sp_start_job @job_name = ''Alert - Missing Indexes''';
PRINT '';

GO
