@echo off
REM ============================================================
REM EDS Diagnostic Script - Check API and Database Connection
REM ============================================================

echo ============================================================
echo   EDS Universal Requisition - Diagnostics
echo ============================================================
echo.

cd /d "%~dp0"

echo [TEST 1] Checking if API is running on port 8000...
powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://localhost:8000/api/status' -UseBasicParsing -TimeoutSec 5; Write-Host '[PASS] API is running' -ForegroundColor Green; Write-Host $response.Content } catch { Write-Host '[FAIL] API is not reachable' -ForegroundColor Red }"

echo.
echo [TEST 2] Checking API health endpoint...
powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://localhost:8000/api/health' -UseBasicParsing -TimeoutSec 5; Write-Host '[PASS] Health check passed' -ForegroundColor Green } catch { Write-Host '[FAIL] Health check failed' -ForegroundColor Red }"

echo.
echo [TEST 3] Testing products endpoint...
powershell -Command "try { $response = Invoke-WebRequest -Uri 'http://localhost:8000/api/products?page_size=1' -UseBasicParsing -TimeoutSec 10; Write-Host '[PASS] Products endpoint working' -ForegroundColor Green; Write-Host ('Response length: ' + $response.Content.Length + ' bytes') } catch { Write-Host '[FAIL] Products endpoint failed: ' $_.Exception.Message -ForegroundColor Red }"

echo.
echo [TEST 4] Checking .env file...
if exist ".env" (
    echo [PASS] .env file exists
    echo Contents (credentials hidden):
    powershell -Command "Get-Content '.env' | ForEach-Object { if ($_ -match '=') { $parts = $_ -split '=',2; Write-Host ($parts[0] + '=' + ('*' * [Math]::Min($parts[1].Length, 10))) } else { Write-Host $_ } }"
) else (
    echo [FAIL] .env file not found!
    echo Please create .env with your database credentials.
)

echo.
echo [TEST 5] Checking virtual environment...
if exist ".venv\Scripts\python.exe" (
    echo [PASS] Virtual environment exists
) else (
    echo [FAIL] Virtual environment not found
)

echo.
echo ============================================================
echo   Diagnostic Complete
echo ============================================================
echo.
echo If API is not running, start it with:
echo   start.bat
echo.
echo If database is not connected, check your .env credentials.
echo.
pause
