# EDS Deployment Guide

Instructions for deploying the EDS Universal Requisition application.

---

## Deployment Options

| Method | Use Case | Complexity |
|--------|----------|------------|
| Docker Compose | Production/Staging | Low |
| Manual | Development/Testing | Medium |
| Kubernetes | Enterprise/Scaling | High |

---

## Quick Start (Docker)

```bash
# Clone and navigate to project
cd /mnt/c/EDS

# Copy environment configuration
cp config/prod.env.example .env

# Edit .env with your settings
nano .env

# Build and start services
docker-compose up -d --build

# Verify services are running
docker-compose ps

# View logs
docker-compose logs -f
```

**Access Points:**
- Frontend: http://localhost:80
- API: http://localhost:8000
- API Docs: http://localhost:8000/docs

---

## Docker Compose Configuration

### Services

```yaml
# docker-compose.yml
services:
  frontend:    # Nginx serving static files
    port: 80

  api:         # FastAPI backend
    port: 8000
```

### Environment Variables

Create `.env` in project root:

```env
# Database Connection
DB_SERVER=eds-sqlserver.eastus2.cloudapp.azure.com
DB_DATABASE=EDS
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_DRIVER=ODBC Driver 18 for SQL Server
DB_TRUST_CERT=yes

# Connection Pool
DB_POOL_MIN=2
DB_POOL_MAX=10
DB_CONNECTION_TIMEOUT=30

# Ports
FRONTEND_PORT=80
API_PORT=8000

# Application
API_BASE_URL=/api
BUDGET_LIMIT=5000
LOG_LEVEL=INFO
```

### Docker Commands

```bash
# Start services
docker-compose up -d

# Rebuild after code changes
docker-compose up -d --build

# Stop services
docker-compose down

# View logs (all services)
docker-compose logs -f

# View logs (specific service)
docker-compose logs -f api

# Restart a service
docker-compose restart api

# Shell into container
docker-compose exec api bash

# Remove all containers and volumes
docker-compose down -v
```

---

## Dockerfiles

### API Dockerfile (`docker/Dockerfile.api`)

```dockerfile
FROM python:3.12-slim

# Install ODBC drivers for SQL Server
RUN apt-get update && apt-get install -y \
    curl gnupg2 unixodbc-dev \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18

WORKDIR /app
COPY api/ ./api/
COPY pyproject.toml .
RUN pip install -e ".[api]"

EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Frontend Dockerfile (`docker/Dockerfile.frontend`)

```dockerfile
FROM nginx:alpine

COPY universal-requisition.html /usr/share/nginx/html/index.html
COPY frontend/assets/ /usr/share/nginx/html/assets/
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## Manual Deployment

### Prerequisites

- Python 3.12+
- ODBC Driver 18 for SQL Server
- Node.js (optional, for frontend dev)

### Backend Setup

```bash
# Create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -e ".[api]"

# Configure environment
cp .env.example .env
# Edit .env with credentials

# Run API server
uvicorn api.main:app --host 0.0.0.0 --port 8000
```

### Frontend Setup

For development, open `universal-requisition.html` directly in browser.

For production, serve via nginx or any static file server:

```bash
# Example with Python
cd /mnt/c/EDS
python -m http.server 80
```

---

## Production Considerations

### Security

1. **SSL/TLS** - Use HTTPS in production
   ```nginx
   server {
       listen 443 ssl;
       ssl_certificate /path/to/cert.pem;
       ssl_certificate_key /path/to/key.pem;
   }
   ```

2. **Environment Variables** - Never commit `.env` files
   ```bash
   # Use secrets management
   docker secret create db_password /path/to/password.txt
   ```

3. **Network Isolation** - Use Docker networks
   ```yaml
   networks:
     eds-internal:
       internal: true  # No external access
   ```

### Performance

1. **API Workers** - Scale uvicorn workers
   ```bash
   uvicorn api.main:app --workers 4
   ```

2. **Connection Pooling** - Configure pool size
   ```env
   DB_POOL_MIN=5
   DB_POOL_MAX=20
   ```

3. **Caching** - Add Redis for session/cache (optional)
   ```yaml
   services:
     redis:
       image: redis:alpine
   ```

### Monitoring

1. **Health Checks** - Already configured in docker-compose
   ```bash
   curl http://localhost:8000/api/health
   ```

2. **Logging** - Configure log levels
   ```env
   LOG_LEVEL=WARNING  # Production
   LOG_LEVEL=DEBUG    # Development
   ```

3. **Metrics** - Add Prometheus endpoint (optional)

---

## CI/CD Pipeline

### GitHub Actions (`.github/workflows/`)

```yaml
# Example: deploy.yml
name: Deploy

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build and push
        run: |
          docker-compose build
          docker-compose push

      - name: Deploy to server
        run: |
          ssh user@server 'cd /app && docker-compose pull && docker-compose up -d'
```

---

## Deployment Script

Use the provided deployment script:

```bash
# Development deployment
./scripts/dev-setup.sh

# Production deployment
./scripts/deploy.sh
```

### deploy.sh

```bash
#!/bin/bash
set -e

echo "=== EDS Deployment ==="

# Pull latest code
git pull origin main

# Build containers
docker-compose build

# Run database migrations (if any)
# docker-compose run --rm api python manage.py migrate

# Restart services with zero downtime
docker-compose up -d --no-deps --build api
docker-compose up -d --no-deps --build frontend

# Cleanup old images
docker image prune -f

echo "=== Deployment Complete ==="
```

---

## Rollback

```bash
# List recent images
docker images | grep eds

# Rollback to previous version
docker-compose down
docker tag eds-api:previous eds-api:latest
docker-compose up -d

# Or use specific version
docker-compose up -d api:v1.2.3
```

---

## Troubleshooting

### Container Won't Start

```bash
# Check logs
docker-compose logs api

# Common issues:
# - Database connection failed → Check DB_SERVER, credentials
# - Port already in use → Change FRONTEND_PORT/API_PORT
# - Missing ODBC driver → Rebuild container
```

### Database Connection Issues

```bash
# Test from container
docker-compose exec api python -c "
from api.database import test_connection
print(test_connection())
"
```

### Health Check Failing

```bash
# Check endpoint manually
curl -v http://localhost:8000/api/health

# Check container health
docker inspect eds-api | grep -A 10 Health
```

---

## See Also

- [Development Setup](DEVELOPMENT.md) - Local development
- [API Reference](API_REFERENCE.md) - API documentation
- [Universal Requisition](UNIVERSAL_REQUISITION.md) - Frontend guide
