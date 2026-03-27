# ============================================================
# EDS Universal Requisition - Application Launcher (PowerShell)
# Starts the API server and opens the frontend in browser
# ============================================================

$ErrorActionPreference = "Stop"

Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  EDS Universal Requisition - Starting Application" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""

# Get the directory where this script is located
$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $ScriptDir

# Check if virtual environment exists
if (-not (Test-Path ".venv\Scripts\Activate.ps1")) {
    Write-Host "[ERROR] Virtual environment not found!" -ForegroundColor Red
    Write-Host ""
    Write-Host "Please run the setup first:" -ForegroundColor Yellow
    Write-Host "  1. cd $ScriptDir"
    Write-Host "  2. python -m venv .venv"
    Write-Host "  3. .\.venv\Scripts\Activate.ps1"
    Write-Host "  4. pip install -e '.[dev,api]'"
    Write-Host ""
    Read-Host "Press Enter to exit"
    exit 1
}

# Check if .env file exists
if (-not (Test-Path ".env")) {
    Write-Host "[WARN] .env file not found - copying from template..." -ForegroundColor Yellow
    if (Test-Path "config\dev.env") {
        Copy-Item "config\dev.env" ".env"
        Write-Host "[INFO] Created .env file. Please edit with your database credentials." -ForegroundColor Green
    } elseif (Test-Path ".env.example") {
        Copy-Item ".env.example" ".env"
        Write-Host "[INFO] Created .env file. Please edit with your database credentials." -ForegroundColor Green
    }
}

# Activate virtual environment
Write-Host "[INFO] Activating virtual environment..." -ForegroundColor Green
& ".\.venv\Scripts\Activate.ps1"

# Check if uvicorn is available
$uvicornPath = Get-Command uvicorn -ErrorAction SilentlyContinue
if (-not $uvicornPath) {
    Write-Host "[INFO] Installing dependencies..." -ForegroundColor Green
    pip install -e ".[dev,api]" -q
}

Write-Host "[INFO] Starting API server on http://localhost:8000" -ForegroundColor Green
Write-Host "[INFO] API documentation available at http://localhost:8000/docs" -ForegroundColor Green
Write-Host ""

# Start the API server in a new window
$apiProcess = Start-Process -FilePath "powershell" -ArgumentList "-NoExit", "-Command", "cd '$ScriptDir'; .\.venv\Scripts\Activate.ps1; uvicorn api.main:app --reload --port 8000" -PassThru

# Wait for server to start
Write-Host "[INFO] Waiting for server to start..." -ForegroundColor Green
Start-Sleep -Seconds 3

# Open the login page in default browser
Write-Host "[INFO] Opening login page in browser..." -ForegroundColor Green
Start-Process "http://localhost:8000/login"

Write-Host ""
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host "  Application Started!" -ForegroundColor Cyan
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "  API Server:  http://localhost:8000" -ForegroundColor White
Write-Host "  API Docs:    http://localhost:8000/docs" -ForegroundColor White
Write-Host "  Frontend:    $ScriptDir\frontend\index.html" -ForegroundColor White
Write-Host ""
Write-Host "  To stop: Close the API server PowerShell window" -ForegroundColor Yellow
Write-Host "============================================================" -ForegroundColor Cyan
Write-Host ""
Read-Host "Press Enter to exit this window"
