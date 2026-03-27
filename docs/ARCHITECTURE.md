# EDS Architecture Overview

High-level architecture of the EDS Universal Requisition system.

---

## System Architecture

```
┌────────────────────────────────────────────────────────────────────────────┐
│                               CLIENT LAYER                                  │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│   ┌──────────────────────────────────────────────────────────────────┐    │
│   │              Universal Requisition Frontend                       │    │
│   │              (universal-requisition.html)                         │    │
│   │  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐            │    │
│   │  │ Product  │ │  Search  │ │  Cart    │ │ Filters  │            │    │
│   │  │  Grid    │ │Component │ │ Drawer   │ │Component │            │    │
│   │  └──────────┘ └──────────┘ └──────────┘ └──────────┘            │    │
│   │                                                                  │    │
│   │  Tech: HTML5, Tailwind CSS, Alpine.js, Vanilla JavaScript       │    │
│   │  Storage: localStorage (cart, favorites, settings)               │    │
│   └──────────────────────────────────────────────────────────────────┘    │
│                                    │                                       │
│                                    │ HTTP/JSON (REST API)                  │
│                                    ▼                                       │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                               API LAYER                                     │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│   ┌──────────────────────────────────────────────────────────────────┐    │
│   │                    FastAPI Application                            │    │
│   │                    (api/main.py)                                  │    │
│   │                                                                   │    │
│   │   Routes:                                                         │    │
│   │   ┌────────────────┐ ┌────────────────┐ ┌────────────────┐       │    │
│   │   │ /api/products  │ │/api/categories │ │ /api/vendors   │       │    │
│   │   │  - GET list    │ │  - GET list    │ │  - GET list    │       │    │
│   │   │  - GET by ID   │ │                │ │  - Search      │       │    │
│   │   │  - Autocomplete│ │                │ │                │       │    │
│   │   └────────────────┘ └────────────────┘ └────────────────┘       │    │
│   │   ┌────────────────┐                                              │    │
│   │   │ /api/health    │  Middleware: CORS, Logging, Error Handling  │    │
│   │   │ /api/status    │                                              │    │
│   │   └────────────────┘                                              │    │
│   │                                                                   │    │
│   │   Tech: FastAPI, Pydantic, Uvicorn                               │    │
│   └──────────────────────────────────────────────────────────────────┘    │
│                                    │                                       │
│                                    │ pyodbc (ODBC Driver 18)               │
│                                    ▼                                       │
└────────────────────────────────────────────────────────────────────────────┘

┌────────────────────────────────────────────────────────────────────────────┐
│                             DATABASE LAYER                                  │
├────────────────────────────────────────────────────────────────────────────┤
│                                                                            │
│   ┌──────────────────────────────────────────────────────────────────┐    │
│   │               SQL Server 2017 (Azure VM)                          │    │
│   │               eds-sqlserver.eastus2.cloudapp.azure.com           │    │
│   │                                                                   │    │
│   │   ┌─────────────────────┐    ┌─────────────────────┐             │    │
│   │   │         EDS         │    │     dpa_EDSAdmin    │             │    │
│   │   │  (Production DB)    │    │   (Monitoring DB)   │             │    │
│   │   │                     │    │                     │             │    │
│   │   │  Tables: 439        │    │  Tables: 207        │             │    │
│   │   │  Size: ~1.4 TB      │    │  DPA metrics        │             │    │
│   │   │  Stored Procs: 396  │    │  Performance data   │             │    │
│   │   │  Views: 475         │    │                     │             │    │
│   │   └─────────────────────┘    └─────────────────────┘             │    │
│   │                                                                   │    │
│   │   Key Tables: Catalog, Items, Vendors, Categories, Orders        │    │
│   └──────────────────────────────────────────────────────────────────┘    │
│                                                                            │
└────────────────────────────────────────────────────────────────────────────┘
```

---

## Component Details

### Frontend (Client Layer)

**File:** `universal-requisition.html`

| Component | Purpose |
|-----------|---------|
| `ProductGrid` | Product listing with pagination |
| `SearchComponent` | Search bar with autocomplete |
| `CartDrawer` | Shopping cart slide-out panel |
| `CategoryFilter` | Category sidebar filter |
| `VendorFilter` | Vendor search/filter |
| `FilterChips` | Active filter display |
| `PriceSlider` | Price range filter |
| `QuickViewModal` | Product detail modal |
| `ProductComparison` | Compare up to 3 products |
| `SavedCarts` | Save/load cart drafts |
| `RecentlyViewed` | Track recent products |
| `Favorites` | Save favorite products |

**Technologies:**
- HTML5 single-page application
- Tailwind CSS (via CDN)
- Alpine.js for reactivity
- Vanilla JavaScript components
- localStorage for state persistence

### API Layer

**Directory:** `api/`

```
api/
├── __init__.py
├── main.py          # FastAPI application entry
├── database.py      # Database connection management
├── models.py        # Pydantic request/response models
└── routes/
    ├── products.py  # Product endpoints
    ├── categories.py # Category endpoints
    └── vendors.py   # Vendor endpoints
```

**Endpoints:**

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/health` | GET | Health check |
| `/api/status` | GET | Detailed status |
| `/api/products` | GET | List products (paginated) |
| `/api/products/{id}` | GET | Single product |
| `/api/products/search/autocomplete` | GET | Search autocomplete |
| `/api/categories` | GET | List categories |
| `/api/vendors` | GET | List vendors |
| `/api/vendors/search` | GET | Search vendors |

**Technologies:**
- FastAPI framework
- Pydantic for validation
- Uvicorn ASGI server
- pyodbc for SQL Server

### Database Layer

**Server:** SQL Server 2017 on Azure VM

**Primary Tables:**

| Table | Purpose |
|-------|---------|
| `Catalog` | Product catalog items |
| `Items` | Item details and pricing |
| `Vendors` | Vendor information |
| `Categories` | Product categories |
| `Orders` | Order headers |
| `OrderDetails` | Order line items |

**Key Relationships:**
```
Catalog ──┬── Items (1:N)
          └── Categories (N:1)

Items ────┬── Vendors (N:1)
          └── OrderDetails (1:N)

Orders ───── OrderDetails (1:N)
```

---

## Data Flow

### Product Browsing Flow

```
1. User loads page
   │
2. Frontend initializes
   │ GET /api/categories
   │ GET /api/vendors
   │ GET /api/products?page=1
   ▼
3. API receives request
   │
4. Database query executed
   │ SELECT FROM Catalog JOIN Items JOIN Vendors...
   ▼
5. Results returned to API
   │
6. API transforms to JSON
   │
7. Frontend renders products
   │
8. User sees product grid
```

### Add to Cart Flow

```
1. User clicks "Add to Cart"
   │
2. CartDrawer.addItem(product, quantity)
   │
3. Cart state updated
   │
4. localStorage.setItem('eds-cart', JSON.stringify(items))
   │
5. Cart drawer UI updates
   │
6. Budget indicator updates
```

### Search Flow

```
1. User types in search box
   │
2. Debounce (300ms)
   │
3. GET /api/products/search/autocomplete?q=...
   │
4. API searches: Description LIKE '%query%' OR VendorItemNumber LIKE '%query%'
   │
5. Results returned (max 10)
   │
6. Autocomplete dropdown shows results
```

---

## Deployment Architecture

### Docker Compose Deployment

```
┌──────────────────────────────────────────────────────────────┐
│                    Docker Host                                │
│                                                              │
│   ┌─────────────────┐      ┌─────────────────────────────┐  │
│   │    Frontend     │      │           API               │  │
│   │    (nginx)      │      │      (uvicorn/FastAPI)      │  │
│   │                 │      │                             │  │
│   │  Port: 80       │ ───▶ │       Port: 8000           │  │
│   │                 │      │                             │  │
│   │  Serves:        │      │  Connects to:               │  │
│   │  - HTML         │      │  - SQL Server (ext)        │  │
│   │  - Assets       │      │                             │  │
│   └─────────────────┘      └─────────────────────────────┘  │
│                                       │                      │
└───────────────────────────────────────┼──────────────────────┘
                                        │
                                        ▼ TCP 1433
                              ┌─────────────────────┐
                              │    SQL Server       │
                              │    (External)       │
                              └─────────────────────┘
```

### Development Setup

```
┌──────────────────────────────────────────────────────────────┐
│                    Development Machine                        │
│                                                              │
│   ┌─────────────────┐      ┌─────────────────────────────┐  │
│   │    Browser      │      │       uvicorn               │  │
│   │                 │      │       (--reload)            │  │
│   │  file://...html │ ───▶ │                             │  │
│   │  or localhost   │      │  http://localhost:8000/api  │  │
│   └─────────────────┘      └─────────────────────────────┘  │
│                                       │                      │
└───────────────────────────────────────┼──────────────────────┘
                                        │
                                        ▼
                              ┌─────────────────────┐
                              │    SQL Server       │
                              │  (Azure/Local)      │
                              └─────────────────────┘
```

---

## Security Considerations

### Authentication Flow

Currently the Universal Requisition frontend does not implement user authentication. For production:

1. **API Authentication** - Add JWT or API key authentication
2. **User Sessions** - Implement login/logout
3. **Role-Based Access** - Control access by user role

### Data Security

| Layer | Security Measure |
|-------|------------------|
| Frontend | Input sanitization, XSS prevention |
| API | SQL injection prevention, input validation |
| Database | Parameterized queries, connection encryption |
| Network | HTTPS, firewall rules |

### Input Sanitization

```python
# api/routes/products.py
def sanitize_search_input(query: str) -> str:
    """Remove dangerous characters from search input."""
    # Remove SQL injection patterns
    # Remove XSS patterns
    # Enforce max length
    return sanitized_query
```

---

## Performance Architecture

### Caching Strategy

| Cache | Location | TTL | Purpose |
|-------|----------|-----|---------|
| Category list | Frontend (memory) | Session | Reduce API calls |
| Vendor list | Frontend (memory) | Session | Reduce API calls |
| Product images | Browser cache | Long | Reduce bandwidth |

### Connection Pooling

```python
# api/database.py
POOL_CONFIG = {
    'min_connections': 2,   # Minimum pool size
    'max_connections': 10,  # Maximum pool size
    'timeout': 30,          # Connection timeout
}
```

### Query Optimization

- Pagination with `OFFSET/FETCH`
- Indexed columns for WHERE clauses
- Lazy loading for images
- Debounced search requests

---

## Integration Points

### External Systems

| System | Integration | Protocol |
|--------|-------------|----------|
| SQL Server | Direct connection | ODBC/TDS |
| DPA (SolarWinds) | Monitoring | Agent |
| Legacy EDS Apps | Shared database | SQL |

### API Extensions

Future integrations could include:

- **Order submission** - POST /api/orders
- **User preferences** - GET/PUT /api/users/{id}/preferences
- **Approval workflow** - POST /api/orders/{id}/approve

---

## Scalability

### Horizontal Scaling

```
                    Load Balancer
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼
     ┌─────────┐   ┌─────────┐   ┌─────────┐
     │ API-1   │   │ API-2   │   │ API-3   │
     │(uvicorn)│   │(uvicorn)│   │(uvicorn)│
     └─────────┘   └─────────┘   └─────────┘
          │              │              │
          └──────────────┼──────────────┘
                         │
                    SQL Server
                   (with replicas)
```

### Vertical Scaling

- Increase uvicorn workers: `--workers 4`
- Increase connection pool: `DB_POOL_MAX=20`
- Add Redis for session caching (Redis is already deployed in K8s for IDIQ — `uat-idiq-redis`)

---

## Monitoring

### Health Endpoints

```bash
# Basic health check
curl http://localhost:8000/api/health

# Detailed status
curl http://localhost:8000/api/status
```

### Metrics to Monitor

| Metric | Source | Alert Threshold |
|--------|--------|-----------------|
| API response time | API logs | > 2 seconds |
| Error rate | API logs | > 1% |
| Database connections | Connection pool | > 80% capacity |
| Memory usage | System metrics | > 80% |

---

## Related Documentation

- [Development Guide](DEVELOPMENT.md) - Local setup
- [Deployment Guide](DEPLOYMENT.md) - Docker deployment
- [API Reference](API_REFERENCE.md) - Endpoint details
- [Database Architecture](wiki/architecture/database-architecture.md) - SQL Server details
- [System Overview](wiki/architecture/system-overview.md) - Full infrastructure
