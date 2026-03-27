@echo off
REM ============================================================
REM EDS Universal Requisition - Application Launcher
REM Starts the API server and opens the frontend in browser
REM ============================================================

setlocal EnableDelayedExpansion

echo ============================================================
echo   EDS Universal Requisition - Starting Application
echo ============================================================
echo.

REM Get the directory where this script is located
set "SCRIPT_DIR=%~dp0"
cd /d "%SCRIPT_DIR%"

REM Check if virtual environment exists
if not exist ".venv\Scripts\activate.bat" (
    echo [ERROR] Virtual environment not found!
    echo.
    echo Please run the setup first:
    echo   1. Open PowerShell or Command Prompt
    echo   2. cd %SCRIPT_DIR%
    echo   3. python -m venv .venv
    echo   4. .venv\Scripts\activate
    echo   5. pip install -e ".[dev,api]"
    echo.
    pause
    exit /b 1
)

REM Check if .env file exists
if not exist ".env" (
    echo [WARN] .env file not found - copying from template...
    if exist "config\dev.env" (
        copy "config\dev.env" ".env" >nul
        echo [INFO] Created .env file. Please edit with your database credentials.
    ) else if exist ".env.example" (
        copy ".env.example" ".env" >nul
        echo [INFO] Created .env file. Please edit with your database credentials.
    )
)

echo [INFO] Activating virtual environment...
call .venv\Scripts\activate.bat

REM Check if uvicorn is available
where uvicorn >nul 2>&1
if errorlevel 1 (
    echo [INFO] Installing dependencies...
    pip install -e ".[dev,api]" -q
)

echo [INFO] Starting API server on http://localhost:8000
echo [INFO] API documentation available at http://localhost:8000/docs
echo.

REM Start the API server in a new window
start "EDS API Server" cmd /k "cd /d %SCRIPT_DIR% && .venv\Scripts\activate.bat && uvicorn api.main:app --reload --port 8000"

REM Wait for server to start
echo [INFO] Waiting for server to start...
timeout /t 3 /nobreak >nul

REM Open the login page in default browser
echo [INFO] Opening login page in browser...
start "" "http://localhost:8000/login"

echo.
echo ============================================================
echo   Application Started!
echo ============================================================
echo.
echo   Login Page:  http://localhost:8000/login
echo   Application: http://localhost:8000
echo   API Docs:    http://localhost:8000/docs
echo.
echo   To stop: Close the "EDS API Server" command window
echo ============================================================
echo.
pause
