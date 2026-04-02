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
  frontend:        # Nginx serving static files
    port: 80

  api:             # FastAPI backend
    port: 8000

  elasticsearch:   # Search engine (ES 8.17.0 local; production runs ES 7.15.2)
    port: 9200
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

# Elasticsearch
ES_ENABLED=true
ES_URL=http://localhost:9200
ES_INDEX=pricing_consolidated_active

# AI/LLM (optional)
LLM_PROVIDER=ollama
OLLAMA_HOST=http://localhost:11434
# ANTHROPIC_API_KEY=your_key_here
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

Uses a multi-stage build for a smaller production image. Runs as a non-root `appuser` for security.

```dockerfile
# Stage 1: Builder — install Python dependencies
FROM python:3.11-slim as builder
WORKDIR /build
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl unixodbc-dev && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml ./
RUN pip install --no-cache-dir ".[api]"

# Stage 2: Production — copy packages, install ODBC driver
FROM python:3.11-slim as production
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl gnupg2 unixodbc \
    && curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/11/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y --no-install-recommends msodbcsql18 \
    && rm -rf /var/lib/apt/lists/*
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY api/ ./api/
RUN groupadd --gid 1000 appuser && useradd --uid 1000 --gid appuser appuser && chown -R appuser:appuser /app
USER appuser
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:8000/api/health || exit 1
EXPOSE 8000
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Frontend Dockerfile (`docker/Dockerfile.frontend`)

Copies the entire `frontend/` directory and supports runtime configuration via environment variable substitution into `config.js`.

```dockerfile
FROM nginx:alpine
RUN rm /etc/nginx/conf.d/default.conf
COPY docker/nginx.conf /etc/nginx/conf.d/default.conf
COPY frontend/ /usr/share/nginx/html/
# Runtime config: envsubst replaces variables in config.template.js → config.js
RUN echo '#!/bin/sh' > /docker-entrypoint.d/40-envsubst-config.sh && \
    echo 'envsubst < /usr/share/nginx/html/js/config.template.js > /usr/share/nginx/html/js/config.js' >> /docker-entrypoint.d/40-envsubst-config.sh && \
    chmod +x /docker-entrypoint.d/40-envsubst-config.sh
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD wget --spider http://localhost:80/ || exit 1
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

---

## Manual Deployment

### Prerequisites

- Python 3.11+
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

For development, open `index.html` directly in browser.

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

3. **Caching** - Redis is deployed in the `idiq-uat` K8s namespace (`uat-idiq-redis`) as the IDIQ backing store. For the Universal Requisition API, Redis can be added as a session/cache layer:
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

> **Note:** The `deploy.sh` and `dev-setup.sh` scripts referenced below are not yet implemented. Use the Docker Compose commands from [Quick Start](#quick-start-docker) directly.

```bash
# Build and deploy
docker-compose build
docker-compose up -d --no-deps --build api
docker-compose up -d --no-deps --build frontend

# Cleanup old images
docker image prune -f
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
