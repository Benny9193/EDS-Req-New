#!/bin/bash
# ============================================================
# EDS Universal Requisition - Application Launcher
# Starts the API server and opens the frontend in browser
# ============================================================

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

echo "============================================================"
echo "  EDS Universal Requisition - Starting Application"
echo "============================================================"
echo ""

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    log_error "Virtual environment not found!"
    echo ""
    echo "Please run the setup first:"
    echo "  1. cd $SCRIPT_DIR"
    echo "  2. python3 -m venv .venv"
    echo "  3. source .venv/bin/activate"
    echo "  4. pip install -e '.[dev,api]'"
    echo ""
    exit 1
fi

# Check if .env file exists
if [ ! -f ".env" ]; then
    log_warn ".env file not found - copying from template..."
    if [ -f "config/dev.env" ]; then
        cp "config/dev.env" ".env"
        log_info "Created .env file. Please edit with your database credentials."
    elif [ -f ".env.example" ]; then
        cp ".env.example" ".env"
        log_info "Created .env file. Please edit with your database credentials."
    fi
fi

# Activate virtual environment
log_info "Activating virtual environment..."
source .venv/bin/activate 2>/dev/null || source .venv/Scripts/activate 2>/dev/null

# Check if uvicorn is available
if ! command -v uvicorn &> /dev/null; then
    log_info "Installing dependencies..."
    pip install -e ".[dev,api]" -q
fi

log_info "Starting API server on http://localhost:8000"
log_info "API documentation available at http://localhost:8000/docs"
echo ""

# Function to open browser cross-platform
open_browser() {
    local url="$1"
    if command -v xdg-open &> /dev/null; then
        xdg-open "$url" 2>/dev/null &
    elif command -v open &> /dev/null; then
        open "$url" 2>/dev/null &
    elif command -v cmd.exe &> /dev/null; then
        # WSL
        cmd.exe /c start "" "$url" 2>/dev/null &
    else
        log_warn "Could not detect browser. Please open manually:"
        log_warn "  $url"
    fi
}

# Start API server in background
log_info "Starting API server..."
uvicorn api.main:app --reload --port 8000 &
API_PID=$!

# Wait for server to start
log_info "Waiting for server to start..."
sleep 3

# Check if server started successfully
if ! kill -0 $API_PID 2>/dev/null; then
    log_error "API server failed to start!"
    exit 1
fi

# Open the login page in browser
log_info "Opening login page in browser..."
open_browser "http://localhost:8000/login"

echo ""
echo "============================================================"
echo "  Application Started!"
echo "============================================================"
echo ""
echo "  API Server:  http://localhost:8000"
echo "  API Docs:    http://localhost:8000/docs"
echo "  Frontend:    $SCRIPT_DIR/frontend/index.html"
echo ""
echo "  Press Ctrl+C to stop the server"
echo "============================================================"
echo ""

# Wait for API server (trap Ctrl+C to clean up)
trap "log_info 'Stopping API server...'; kill $API_PID 2>/dev/null; exit 0" INT TERM
wait $API_PID
