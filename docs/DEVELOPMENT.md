# EDS Development Guide

Setting up a local development environment for the EDS Universal Requisition project.

---

## Prerequisites

| Requirement | Version | Purpose |
|-------------|---------|---------|
| Python | 3.11+ | API backend |
| ODBC Driver | 18 | SQL Server connectivity |
| Git | 2.x | Version control |
| Docker | 24+ | Containerization (optional) |
| Node.js | 20+ | Frontend tooling (optional) |

---

## Quick Setup

```bash
# 1. Clone repository
git clone <repository-url>
cd EDS

# 2. Configure environment
cp .env.example .env
# Edit .env with your database credentials

# 3. Start API server
source .venv/bin/activate
uvicorn api.main:app --reload --port 8000

# 4. Open frontend
# Open frontend/index.html in browser, or use Docker (see DEPLOYMENT.md)
```

---

## Detailed Setup

### 1. Python Environment

```bash
# Create virtual environment
python -m venv .venv

# Activate (Linux/Mac)
source .venv/bin/activate

# Activate (Windows)
.venv\Scripts\activate

# Install all dependencies
pip install -e ".[dev,api,scripts]"

# Or install specific extras
pip install -e ".[api]"      # API only
pip install -e ".[scripts]"  # Scripts only
pip install -e ".[dev]"      # Development tools
```

### 2. ODBC Driver Installation

**Ubuntu/Debian:**
```bash
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | sudo tee /etc/apt/sources.list.d/mssql-release.list
sudo apt-get update
sudo ACCEPT_EULA=Y apt-get install -y msodbcsql18 unixodbc-dev
```

**macOS:**
```bash
brew install unixodbc
brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
brew install msodbcsql18
```

**Windows:**
Download from [Microsoft ODBC Driver](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server)

### 3. Environment Configuration

Create `.env` in project root:

```env
# Database Connection
DB_SERVER=eds-sqlserver.eastus2.cloudapp.azure.com
DB_DATABASE=EDS
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_DRIVER=ODBC Driver 18 for SQL Server
DB_TRUST_CERT=yes

# Development Settings
LOG_LEVEL=DEBUG
API_PORT=8000
```

### 4. Verify Setup

```bash
# Test database connection
python test_db.py

# Expected output:
# Connection successful!
# Database: EDS
# Tables: 439
```

---

## Running the Application

### API Server

```bash
# Development mode (with auto-reload)
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000

# Production mode
uvicorn api.main:app --host 0.0.0.0 --port 8000 --workers 4
```

**API Endpoints:**
- http://localhost:8000 - Root
- http://localhost:8000/docs - Swagger UI
- http://localhost:8000/redoc - ReDoc
- http://localhost:8000/api/status - Health check

### Frontend

**Option 1: Direct file access**
```bash
# Open in browser
# Windows: file:///C:/EDS/frontend/index.html
# WSL: Configure API_CONFIG.baseUrl to WSL IP
```

**Option 2: Local server**
```bash
# Python HTTP server
python -m http.server 3000

# Access at http://localhost:3000/frontend/index.html
```

**Option 3: Docker**
```bash
docker-compose up frontend
# Access at http://localhost:80
```

---

## Project Structure

```
EDS/
├── api/                    # FastAPI backend
│   ├── __init__.py
│   ├── main.py            # Application entry point
│   ├── database.py        # Database connection
│   ├── models.py          # Pydantic models
│   └── routes/            # API endpoints
│       ├── products.py
│       ├── categories.py
│       └── vendors.py
│
├── scripts/               # Utility scripts
│   ├── README.md          # Script documentation
│   ├── config.py          # Shared configuration
│   ├── db_utils.py        # Database utilities
│   └── ...               # Analysis/doc scripts
│
├── docs/                  # Documentation
│   ├── wiki/             # Detailed wiki pages
│   ├── API_REFERENCE.md
│   ├── DEPLOYMENT.md
│   └── ...
│
├── tests/                 # Test suite
│   ├── api/              # API tests
│   ├── e2e/              # End-to-end tests
│   └── conftest.py       # Pytest fixtures
│
├── frontend/             # Alternative frontend files
├── docker/               # Docker configurations
├── config/               # Environment configs
│
├── frontend/index.html   # Main frontend entry point
├── docker-compose.yml    # Docker orchestration
├── pyproject.toml        # Python project config
└── .env                  # Environment variables
```

---

## Development Workflow

### Git Workflow

```bash
# Create feature branch
git checkout -b feature/your-feature

# Make changes and commit
git add .
git commit -m "feat: description of changes"

# Push and create PR
git push origin feature/your-feature
```

### Commit Message Format

```
type(scope): description

Types:
  feat     - New feature
  fix      - Bug fix
  docs     - Documentation
  style    - Formatting
  refactor - Code restructuring
  test     - Adding tests
  chore    - Maintenance
```

### Code Style

**Python:**
- Follow PEP 8
- Use type hints
- Max line length: 100 characters

```python
# Example
def get_products(
    page: int = 1,
    page_size: int = 20,
    category: Optional[str] = None
) -> ProductListResponse:
    """Retrieve paginated product list."""
    ...
```

**JavaScript:**
- Use ES6+ syntax
- Const/let (no var)
- Single quotes for strings

```javascript
// Example
const loadProducts = async (page = 1) => {
    const response = await api.getProducts({ page });
    return response.products;
};
```

---

## Testing

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=api --cov-report=html

# Run specific test file
pytest tests/api/test_products.py

# Run with verbose output
pytest -v

# Run only failing tests
pytest --lf
```

### Test Structure

```
tests/
├── api/
│   ├── test_products.py     # Product endpoint tests
│   ├── test_categories.py   # Category endpoint tests
│   └── test_vendors.py      # Vendor endpoint tests
├── e2e/
│   └── test_requisition.py  # End-to-end tests
└── conftest.py              # Shared fixtures
```

### Writing Tests

```python
# tests/api/test_products.py
import pytest
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)

def test_get_products():
    response = client.get("/api/products")
    assert response.status_code == 200
    assert "products" in response.json()

def test_get_product_by_id():
    response = client.get("/api/products/ABC123")
    assert response.status_code in [200, 404]
```

---

## Debugging

### API Debugging

```python
# Add to api/main.py for debug logging
import logging
logging.basicConfig(level=logging.DEBUG)

# Or set environment variable
# LOG_LEVEL=DEBUG uvicorn api.main:app --reload
```

### Frontend Debugging

1. Open browser DevTools (F12)
2. Check Console for errors
3. Network tab for API requests
4. Set breakpoints in Sources tab

### Database Debugging

```python
# Interactive query testing
python scripts/schema_explorer.py

# Or use Python REPL
python
>>> from scripts.db_utils import get_connection
>>> conn = get_connection()
>>> cursor = conn.cursor()
>>> cursor.execute("SELECT TOP 5 * FROM Catalog")
>>> for row in cursor.fetchall():
...     print(row)
```

---

## Common Tasks

### Add New API Endpoint

1. Create route in `api/routes/`
2. Add models in `api/models.py`
3. Register in `api/main.py`
4. Add tests in `tests/api/`
5. Update `docs/API_REFERENCE.md`

### Add New Frontend Feature

1. Add JavaScript module in `frontend/js/`
2. Initialize in `DOMContentLoaded`
3. Add CSS styles if needed
4. Update `docs/UNIVERSAL_REQUISITION.md`

### Update Database Documentation

```bash
# Regenerate all documentation
python scripts/refresh_documentation.py

# Or specific docs
python scripts/generate_data_dictionary.py
python scripts/generate_sp_dependencies.py
```

---

## Troubleshooting

### "ODBC Driver not found"

```bash
# Check installed drivers
odbcinst -q -d

# Reinstall driver
sudo ACCEPT_EULA=Y apt-get install --reinstall msodbcsql18
```

### "Connection refused" to API

```bash
# Check if API is running
curl http://localhost:8000/api/health

# Check port availability
lsof -i :8000
```

### "CORS error" in browser

API already has CORS configured. If issues persist:
```python
# api/main.py
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Development only
    allow_methods=["*"],
    allow_headers=["*"],
)
```

### Tests failing with database errors

```bash
# Run tests with mock database
pytest --no-db

# Or set up test database
export DB_DATABASE=EDS_Test
pytest
```

---

## IDE Setup

### VS Code

Recommended extensions:
- Python (Microsoft)
- Pylance
- SQLTools + SQL Server driver
- REST Client
- CSS Variable Autocomplete

**settings.json:**
```json
{
    "python.defaultInterpreterPath": ".venv/bin/python",
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

### PyCharm

1. Open project folder
2. Configure interpreter: `.venv/bin/python`
3. Mark `api/` as Sources Root
4. Mark `tests/` as Test Sources Root

---

## See Also

- [Deployment Guide](DEPLOYMENT.md) - Production deployment
- [API Reference](API_REFERENCE.md) - API documentation
- [Scripts README](../scripts/README.md) - Utility scripts
- [Database Architecture](wiki/architecture/database-architecture.md) - Database details
