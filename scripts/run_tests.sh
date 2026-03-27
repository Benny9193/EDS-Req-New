#!/bin/bash
# EDS Test Runner Script
# Usage:
#   ./scripts/run_tests.sh          # Run all tests
#   ./scripts/run_tests.sh unit     # Run unit tests only
#   ./scripts/run_tests.sh api      # Run API tests only
#   ./scripts/run_tests.sh e2e      # Run E2E tests only
#   ./scripts/run_tests.sh coverage # Run with coverage report

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_ROOT"

# Ensure virtual environment is activated if it exists
if [ -d ".venv" ] && [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    source .venv/bin/activate 2>/dev/null || source .venv/Scripts/activate 2>/dev/null || true
fi

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

case "${1:-all}" in
    unit)
        echo -e "${GREEN}Running unit tests...${NC}"
        pytest tests/ -m "not integration and not e2e" -v
        ;;
    api)
        echo -e "${GREEN}Running API tests...${NC}"
        pytest tests/api/ -v
        ;;
    e2e)
        echo -e "${GREEN}Running E2E tests...${NC}"
        echo -e "${YELLOW}Note: Requires playwright install: playwright install chromium${NC}"
        pytest tests/e2e/ -v -m e2e
        ;;
    coverage)
        echo -e "${GREEN}Running tests with coverage...${NC}"
        pytest tests/ -m "not e2e" --cov=api --cov=scripts --cov-report=term-missing --cov-report=html
        echo -e "${GREEN}Coverage report generated: htmlcov/index.html${NC}"
        ;;
    all)
        echo -e "${GREEN}Running all tests (excluding E2E)...${NC}"
        pytest tests/ -m "not e2e" -v
        ;;
    *)
        echo "Usage: $0 {unit|api|e2e|coverage|all}"
        exit 1
        ;;
esac

echo -e "${GREEN}Tests completed!${NC}"
