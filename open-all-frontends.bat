@echo off
REM ============================================================
REM  EDS Frontend Demo Launcher
REM  Starts the API server and opens all 7 frontends in browser
REM ============================================================
SET PORT=8000
SET BASE=http://localhost:%PORT%

cd /d "%~dp0"

REM --- Check if server is already running ---
curl -s -o nul -w "" "%BASE%/api/health" >nul 2>&1
if %ERRORLEVEL%==0 (
    echo API server already running on port %PORT%.
    goto :open_tabs
)

REM --- Start the API server in a new window ---
echo Starting API server on port %PORT%...
start "EDS API Server" cmd /k "cd /d %~dp0 && uvicorn api.main:app --port %PORT% --log-level info"

REM --- Wait for server to be ready (up to 15 seconds) ---
echo Waiting for server to start...
set /a tries=0
:wait_loop
if %tries% GEQ 15 (
    echo ERROR: Server failed to start after 15 seconds.
    echo Check the "EDS API Server" window for errors.
    pause
    exit /b 1
)
timeout /t 1 /nobreak >nul
curl -s -o nul -w "" "%BASE%/api/health" >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    set /a tries+=1
    goto :wait_loop
)
echo Server is ready!
echo.

:open_tabs
echo Opening all 7 EDS frontend concepts...
echo.

start "" "%BASE%/v6/"
timeout /t 1 /nobreak >nul
start "" "%BASE%/"
timeout /t 1 /nobreak >nul
start "" "%BASE%/v5/"
timeout /t 1 /nobreak >nul
start "" "%BASE%/v2/"
timeout /t 1 /nobreak >nul
start "" "%BASE%/v3/"
timeout /t 1 /nobreak >nul
start "" "%BASE%/v4/"
timeout /t 1 /nobreak >nul
start "" "%BASE%/reimagined/"

echo.
echo ============================================================
echo  All 7 tabs opened in demo order:
echo    1. v6  (Procurement Hub - lead demo)
echo    2. /   (Original - full feature depth)
echo    3. v5  (Multi-Theme - theme switching)
echo    4. v2  (Dark SaaS)
echo    5. v3  (Warm Dashboard)
echo    6. v4  (School Theme)
echo    7. reimagined (Bold Modern)
echo.
echo  API server running in separate window.
echo  Close that window when done to stop the server.
echo ============================================================
pause
