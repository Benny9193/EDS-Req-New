# EDS Configuration Reference

Complete reference for all configuration options in the EDS Universal Requisition system.

---

## Configuration Files Overview

| File | Purpose | Format |
|------|---------|--------|
| `.env` | Environment-specific settings | KEY=value |
| `config.yaml` | Application settings and thresholds | YAML |
| `agent_config.yaml` | DBA Agent settings (LLM, RAG, security, tools) | YAML |
| `config/dev.env` | Development environment template | KEY=value |
| `config/prod.env.example` | Production environment template | KEY=value |

**Priority Order** (highest to lowest):
1. Environment variables
2. `.env` file
3. `config.yaml` file
4. Default values in code

---

## Environment Variables (.env)

Create a `.env` file in the project root with your settings.

### Database Connection

```env
# Required
DB_SERVER=your-server.database.windows.net
DB_DATABASE=EDS
DB_USERNAME=your_username
DB_PASSWORD=your_password

# Optional
DB_DRIVER=ODBC Driver 18 for SQL Server  # Default
DB_TRUST_CERT=yes                         # Use 'no' in production
```

| Variable | Required | Default | Description |
|----------|----------|---------|-------------|
| `DB_SERVER` | Yes | - | SQL Server hostname or IP |
| `DB_DATABASE` | Yes | - | Database name |
| `DB_USERNAME` | Yes | - | Database username |
| `DB_PASSWORD` | Yes | - | Database password |
| `DB_DRIVER` | No | `ODBC Driver 18 for SQL Server` | ODBC driver name |
| `DB_TRUST_CERT` | No | `no` | Trust self-signed certs (dev only) |

### Connection Pool

```env
DB_POOL_MIN=2
DB_POOL_MAX=10
DB_CONNECTION_TIMEOUT=30
```

| Variable | Default | Description |
|----------|---------|-------------|
| `DB_POOL_MIN` | `2` | Minimum pool connections |
| `DB_POOL_MAX` | `10` | Maximum pool connections |
| `DB_CONNECTION_TIMEOUT` | `30` | Connection timeout (seconds) |

### API Configuration

```env
API_PORT=8000
API_BASE_URL=/api
LOG_LEVEL=INFO
```

| Variable | Default | Description |
|----------|---------|-------------|
| `API_PORT` | `8000` | API server port |
| `API_BASE_URL` | `/api` | API URL prefix |
| `LOG_LEVEL` | `INFO` | Logging level (DEBUG, INFO, WARNING, ERROR) |

### Frontend Configuration

```env
FRONTEND_PORT=80
BUDGET_LIMIT=5000
```

| Variable | Default | Description |
|----------|---------|-------------|
| `FRONTEND_PORT` | `80` | Frontend server port (Docker) |
| `BUDGET_LIMIT` | `5000` | Default budget limit for requisitions |

### Elasticsearch

```env
ES_ENABLED=true
ES_URL=http://20.122.81.233:9200
ES_INDEX=pricing_consolidated_active
```

| Variable | Default | Description |
|----------|---------|-------------|
| `ES_ENABLED` | `true` | Enable/disable Elasticsearch integration |
| `ES_URL` | `http://20.122.81.233:9200` | Elasticsearch server URL |
| `ES_INDEX` | `pricing_consolidated_active` | Alias pointing to active pricing index |

> **Note:** Production runs ES 7.15.2. The `docker-compose.yml` local dev environment uses ES 8.17.0. Be aware of API differences between major versions.

### AI / LLM Provider

```env
LLM_PROVIDER=ollama
ANTHROPIC_API_KEY=your_key_here
OLLAMA_HOST=http://localhost:11434
```

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_PROVIDER` | (auto-detect) | AI backend: `claude`, `ollama`, or `openai` |
| `ANTHROPIC_API_KEY` | - | Claude API key (required when `LLM_PROVIDER=claude`) |
| `OLLAMA_HOST` | `http://localhost:11434` | Ollama server URL |

---

## Application Configuration (config.yaml)

The `config.yaml` file contains application-wide settings, thresholds, and defaults.

### Database Settings

```yaml
database:
  name: dpa_EDSAdmin      # Database name
  timeout: 30             # Query timeout in seconds
```

### Threshold Configuration

#### Missing Index Thresholds

```yaml
thresholds:
  missing_index:
    critical: 95          # >= 95% improvement = critical
    high: 80              # >= 80% improvement = high
    medium: 50            # >= 50% improvement = medium
    min_executions: 100   # Minimum executions to consider
```

| Threshold | Default | Description |
|-----------|---------|-------------|
| `critical` | `95` | Critical priority threshold (%) |
| `high` | `80` | High priority threshold (%) |
| `medium` | `50` | Medium priority threshold (%) |
| `min_executions` | `100` | Minimum query executions |

#### Blocking Event Thresholds

```yaml
thresholds:
  blocking:
    critical_seconds: 3600    # >= 1 hour = critical
    high_seconds: 300         # >= 5 minutes = high
    medium_seconds: 60        # >= 1 minute = medium
```

| Threshold | Default | Description |
|-----------|---------|-------------|
| `critical_seconds` | `3600` | Critical blocking threshold |
| `high_seconds` | `300` | High blocking threshold |
| `medium_seconds` | `60` | Medium blocking threshold |

#### I/O Latency Thresholds

```yaml
thresholds:
  io_latency:
    critical_ms: 200      # >= 200ms = critical
    high_ms: 100          # >= 100ms = high
    medium_ms: 50         # >= 50ms = medium
```

#### Slow Query Thresholds

```yaml
thresholds:
  slow_query:
    critical_buffer_gets: 10000000   # 10M+ = critical
    high_buffer_gets: 1000000        # 1M+ = high
    min_buffer_gets: 100000          # Minimum to report
```

### Analysis Settings

```yaml
analysis:
  missing_indexes_days: 30    # Lookback for missing indexes
  slow_queries_days: 7        # Lookback for slow queries
  blocking_days: 30           # Lookback for blocking events
  io_issues_hours: 24         # Lookback for I/O issues
  top_results: 50             # Max results per analysis
  report_top: 10              # Items in summary reports
```

### Dashboard Settings

```yaml
dashboard:
  refresh_interval: 30        # Auto-refresh in seconds
  health_score:
    critical_index_penalty: 20
    high_index_penalty: 10
    blocking_penalty: 15
    io_latency_penalty: 10
    slow_query_penalty: 5
```

### Output Settings

```yaml
output:
  directory: output/performance
  exports_directory: output/exports
  log_directory: logs
```

### Alert Settings

```yaml
alerts:
  email: dba-team@company.com
  mail_profile: Default
  enabled: true
```

### Logging Settings

```yaml
logging:
  level: INFO
  format: "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
  max_file_size_mb: 10
  backup_count: 5
```

---

## Frontend Configuration

The frontend configuration lives in `frontend/js/config.js` (generated at container startup from `config.template.js` via environment variable substitution).

### API Configuration Object

```javascript
const API_CONFIG = {
    baseUrl: 'http://localhost:8000/api',
    enabled: true,          // Set false for static demo mode
    timeout: 15000,         // Request timeout (ms)
    retryAttempts: 2,       // Retry failed requests
    retryDelay: 1000,       // Delay between retries (ms)
};
```

### Storage Keys

```javascript
const STORAGE_KEYS = {
    cart: 'eds-cart',
    favorites: 'eds-favorites',
    recentlyViewed: 'eds-recently-viewed',
    savedCarts: 'eds-saved-carts',
};
```

### Feature Settings

| Setting | Default | Description |
|---------|---------|-------------|
| `ProductGrid.pageSize` | `20` | Products per page |
| `SavedCarts.maxCarts` | `10` | Maximum saved carts |
| `ProductComparison.maxItems` | `3` | Max comparison items |
| `RecentlyViewed.maxItems` | `5` | Max recently viewed |
| `cart.budgetLimit` | `5000` | Default budget limit |

---

## Environment-Specific Templates

### Development (`config/dev.env`)

```env
# Development settings
FRONTEND_PORT=3000
API_BASE_URL=http://localhost:8000/api
BUDGET_LIMIT=5000
API_PORT=8000
LOG_LEVEL=DEBUG

# Local database
DB_SERVER=localhost
DB_DATABASE=EDS
DB_USERNAME=sa
DB_PASSWORD=your_dev_password
DB_TRUST_CERT=yes

# Smaller pool for dev
DB_POOL_MIN=2
DB_POOL_MAX=10
```

### Production (`config/prod.env.example`)

```env
# Production settings - DO NOT COMMIT WITH REAL VALUES
FRONTEND_PORT=80
API_BASE_URL=/api
BUDGET_LIMIT=5000
API_PORT=8000
LOG_LEVEL=WARNING

# Production database
DB_SERVER=your-sql-server.database.windows.net
DB_DATABASE=EDS_Production
DB_USERNAME=eds_app_user
DB_PASSWORD=<SET_SECURE_PASSWORD>
DB_TRUST_CERT=no

# Larger pool for production
DB_POOL_MIN=5
DB_POOL_MAX=20
DB_CONNECTION_TIMEOUT=30
```

---

## Using Configuration in Code

### Python Scripts

```python
from scripts.config import config, get_threshold, get_database_config

# Access config values directly
db_name = config.database.name
critical = config.thresholds.missing_index.critical

# Use convenience functions
threshold = get_threshold('missing_index', 'critical')  # 95
db_config = get_database_config()  # {'name': 'EDS', 'timeout': 30}

# Get output paths
from scripts.config import get_output_path
output_dir = get_output_path()          # /path/to/output/performance
exports_dir = get_output_path('exports') # /path/to/output/exports
logs_dir = get_output_path('logs')       # /path/to/logs
```

### Database Utilities

```python
from scripts.db_utils import get_connection

# Connection uses .env variables automatically
conn = get_connection()
cursor = conn.cursor()
cursor.execute("SELECT TOP 10 * FROM Catalog")
```

### API (FastAPI)

```python
from api.database import get_db_connection

# Uses environment variables
with get_db_connection() as conn:
    cursor = conn.cursor()
    # Execute queries
```

---

## Environment Variable Overrides

Environment variables override `config.yaml` settings:

| Config Path | Environment Variable |
|-------------|---------------------|
| `database.name` | `DB_DATABASE` |
| `database.timeout` | `DB_TIMEOUT` |
| `thresholds.missing_index.critical` | `THRESHOLD_MISSING_INDEX_CRITICAL` |
| `thresholds.blocking.critical_seconds` | `THRESHOLD_BLOCKING_CRITICAL_SECONDS` |
| `alerts.email` | `ALERT_EMAIL` |
| `logging.level` | `LOG_LEVEL` |

---

## Docker Configuration

### docker-compose.yml Environment

```yaml
services:
  api:
    environment:
      - DB_SERVER=${DB_SERVER}
      - DB_DATABASE=${DB_DATABASE}
      - DB_USERNAME=${DB_USERNAME}
      - DB_PASSWORD=${DB_PASSWORD}
      - LOG_LEVEL=${LOG_LEVEL:-INFO}
    env_file:
      - .env
```

### Using Secrets (Production)

```yaml
services:
  api:
    secrets:
      - db_password
    environment:
      - DB_PASSWORD_FILE=/run/secrets/db_password

secrets:
  db_password:
    external: true
```

---

## Validation

### Validate Configuration

```python
from scripts.config import validate_params

# Validates parameters are within acceptable ranges
validate_params(
    days=30,          # 1-365
    min_saving=80,    # 0-100
    hours=24,         # 1-8760
    latency_ms=100    # 0-10000
)
```

### Reload Configuration

```python
from scripts.config import reload_config

# Force reload after changing config files
config = reload_config()
```

---

## Troubleshooting

### Missing Environment Variables

```bash
# Check if variables are set
echo $DB_SERVER
echo $DB_DATABASE

# Load from .env manually
source .env
# or
export $(cat .env | xargs)
```

### YAML Parsing Errors

```bash
# Validate YAML syntax
python -c "import yaml; yaml.safe_load(open('config.yaml'))"
```

### Configuration Not Loading

```python
# Debug configuration loading
from scripts.config import _find_config_file
print(_find_config_file())  # Should print path or None

# Check loaded values
from scripts.config import get_config
cfg = get_config()
print(cfg.database.name)
print(cfg.thresholds.missing_index.critical)
```

---

## DBA Agent Configuration (agent_config.yaml)

The `agent_config.yaml` file at the repository root configures the DBA Agent. Key sections:

| Section | Purpose |
|---------|---------|
| `llm` | Provider settings for Claude (Sonnet 4), OpenAI (GPT-4o), and Ollama (Qwen 2.5) |
| `rag` | Vector store (ChromaDB), embedding model, chunking, and retrieval settings |
| `memory` | Session management, context window, and conversation history limits |
| `security` | Read-only mode toggle, allowed databases, blocked SQL operations |
| `tools` | Script execution, timeouts, and available tool configuration |
| `audit` | Audit logging (JSONL format to `data/audit/`) |
| `cli` | CLI interface settings (history, colors, prompt) |

See [AGENT_TECHNICAL_REFERENCE.md](AGENT_TECHNICAL_REFERENCE.md) for full details.

---

## See Also

- [Development Guide](DEVELOPMENT.md) - Local development setup
- [Deployment Guide](DEPLOYMENT.md) - Production deployment
- [Testing Guide](TESTING.md) - Test configuration
