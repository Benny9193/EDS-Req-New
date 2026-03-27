# EDS Universal Requisition API

FastAPI backend for the Universal Requisition front-end.

## Setup

### 1. Install dependencies

```bash
cd /mnt/c/EDS
pip install -e ".[api]"
```

Or install directly:
```bash
pip install fastapi uvicorn[standard] pydantic
```

### 2. Configure database connection

The API uses the same `.env` file as the rest of the project:

```env
DB_SERVER=eds-sqlserver.eastus2.cloudapp.azure.com
DB_DATABASE=dpa_EDSAdmin
DB_USERNAME=EDSAdmin
DB_PASSWORD=your_password
```

### 3. Run the API server

```bash
# From project root
uvicorn api.main:app --reload --port 8000

# Or run directly
python -m api.main
```

The API will be available at `http://localhost:8000`

## API Documentation

Once running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Endpoints

### Health
- `GET /` - Root endpoint
- `GET /api/status` - API status and DB health check
- `GET /api/health` - Simple health check

### Products
- `GET /api/products` - List products (paginated, with filters)
- `GET /api/products/{id}` - Get single product
- `GET /api/products/search/autocomplete?q=query` - Quick search

Query parameters for `/api/products`:
- `query` - Search text
- `category` - Filter by category
- `vendor` - Filter by vendor name
- `status` - Filter by stock status
- `min_price` / `max_price` - Price range
- `page` / `page_size` - Pagination

### Categories
- `GET /api/categories` - List all categories
- `GET /api/categories/{id}` - Get single category

### Vendors
- `GET /api/vendors` - List vendors
- `GET /api/vendors/{id}` - Get single vendor

## Database Schema Notes

The API expects the following tables in your SQL Server database:
- `Catalog` - Product catalog items
- `CatalogPricing` - Product pricing
- `CatalogText` - Product descriptions
- `Categories` - Product categories
- `Vendors` - Vendor information

If your schema differs, update the SQL queries in `api/routes/products.py`.

## Front-End Integration

The Universal Requisition HTML file (`universal-requisition.html`) is already configured to:

1. Try to connect to the API on page load
2. Fall back to static data if API is unavailable
3. Use API for search autocomplete when available

To disable API integration, set in the HTML:
```javascript
API_CONFIG.enabled = false;
```

## Development

### Running with hot reload
```bash
uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
```

### Testing the connection
```bash
curl http://localhost:8000/api/status
```

Expected response:
```json
{
  "status": "healthy",
  "database_connected": true,
  "version": "1.0.0"
}
```
