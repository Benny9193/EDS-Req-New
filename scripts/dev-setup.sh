#!/bin/bash
# EDS Universal Requisition - Development Setup Script
# Sets up the development environment

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

cd "$PROJECT_ROOT"

log_info "=========================================="
log_info "EDS Universal Requisition - Dev Setup"
log_info "=========================================="

# Check Python
if command -v python3 &> /dev/null; then
    PYTHON=python3
elif command -v python &> /dev/null; then
    PYTHON=python
else
    log_warn "Python not found. Please install Python 3.9+"
    exit 1
fi

log_info "Using Python: $($PYTHON --version)"

# Create virtual environment
if [ ! -d ".venv" ]; then
    log_info "Creating virtual environment..."
    $PYTHON -m venv .venv
fi

# Activate virtual environment
log_info "Activating virtual environment..."
source .venv/bin/activate 2>/dev/null || source .venv/Scripts/activate 2>/dev/null

# Upgrade pip
log_info "Upgrading pip..."
pip install --upgrade pip

# Install dependencies
log_info "Installing dependencies..."
pip install -e ".[dev,api]"

# Copy environment file if not exists
if [ ! -f ".env" ]; then
    log_info "Creating .env file from template..."
    cp config/dev.env .env
    log_warn "Please edit .env with your database credentials"
fi

# Check for ODBC driver
log_info "Checking ODBC driver..."
if command -v odbcinst &> /dev/null; then
    odbcinst -q -d | grep -i "sql server" && log_info "SQL Server ODBC driver found" || log_warn "SQL Server ODBC driver not found"
else
    log_warn "odbcinst not found - cannot check ODBC drivers"
fi

log_info "=========================================="
log_info "Setup complete!"
log_info ""
log_info "To start development:"
log_info "  1. Edit .env with your database credentials"
log_info "  2. Activate the virtual environment:"
log_info "     source .venv/bin/activate"
log_info "  3. Start the API server:"
log_info "     uvicorn api.main:app --reload --port 8000"
log_info "  4. Open frontend/alpine-requisition.html in browser"
log_info ""
log_info "Or use Docker:"
log_info "  ./scripts/deploy.sh dev"
log_info "=========================================="
