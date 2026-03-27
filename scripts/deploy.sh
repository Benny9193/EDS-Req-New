#!/bin/bash
# EDS Universal Requisition - Deployment Script
# Usage:
#   ./scripts/deploy.sh dev      # Deploy to development
#   ./scripts/deploy.sh staging  # Deploy to staging
#   ./scripts/deploy.sh prod     # Deploy to production

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

log_warn() {
    echo -e "${YELLOW}[WARN]${NC} $1"
}

log_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check prerequisites
check_prerequisites() {
    log_info "Checking prerequisites..."

    if ! command -v docker &> /dev/null; then
        log_error "Docker is not installed"
        exit 1
    fi

    if ! command -v docker-compose &> /dev/null && ! docker compose version &> /dev/null; then
        log_error "Docker Compose is not installed"
        exit 1
    fi

    log_info "Prerequisites OK"
}

# Load environment file
load_env() {
    local env_file="$1"
    if [ -f "$env_file" ]; then
        log_info "Loading environment from $env_file"
        export $(grep -v '^#' "$env_file" | xargs)
    else
        log_warn "Environment file not found: $env_file"
    fi
}

# Build images
build_images() {
    log_info "Building Docker images..."
    cd "$PROJECT_ROOT"
    docker-compose build --no-cache
    log_info "Build complete"
}

# Deploy services
deploy_services() {
    log_info "Deploying services..."
    cd "$PROJECT_ROOT"
    docker-compose up -d
    log_info "Deployment complete"
}

# Health check
health_check() {
    log_info "Running health checks..."

    local max_attempts=30
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        if curl -s http://localhost:${API_PORT:-8000}/api/health > /dev/null 2>&1; then
            log_info "API is healthy"
            break
        fi
        log_warn "Waiting for API to be ready... (attempt $attempt/$max_attempts)"
        sleep 2
        ((attempt++))
    done

    if [ $attempt -gt $max_attempts ]; then
        log_error "API health check failed after $max_attempts attempts"
        exit 1
    fi

    if curl -s http://localhost:${FRONTEND_PORT:-80}/health > /dev/null 2>&1; then
        log_info "Frontend is healthy"
    else
        log_warn "Frontend health check returned non-200"
    fi

    log_info "All health checks passed"
}

# Show status
show_status() {
    log_info "Service status:"
    docker-compose ps
    echo ""
    log_info "Logs (last 20 lines):"
    docker-compose logs --tail=20
}

# Main
main() {
    local environment="${1:-dev}"

    log_info "=========================================="
    log_info "EDS Universal Requisition Deployment"
    log_info "Environment: $environment"
    log_info "=========================================="

    check_prerequisites

    case "$environment" in
        dev|development)
            load_env "$PROJECT_ROOT/config/dev.env"
            load_env "$PROJECT_ROOT/.env"
            ;;
        staging)
            load_env "$PROJECT_ROOT/config/staging.env"
            ;;
        prod|production)
            load_env "$PROJECT_ROOT/config/prod.env"
            log_warn "Deploying to PRODUCTION environment!"
            read -p "Are you sure? (yes/no): " confirm
            if [ "$confirm" != "yes" ]; then
                log_info "Deployment cancelled"
                exit 0
            fi
            ;;
        *)
            log_error "Unknown environment: $environment"
            echo "Usage: $0 {dev|staging|prod}"
            exit 1
            ;;
    esac

    build_images
    deploy_services
    health_check
    show_status

    log_info "=========================================="
    log_info "Deployment complete!"
    log_info "Frontend: http://localhost:${FRONTEND_PORT:-80}"
    log_info "API Docs: http://localhost:${API_PORT:-8000}/docs"
    log_info "=========================================="
}

main "$@"
