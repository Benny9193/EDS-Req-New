# EDS Troubleshooting Guide

Common issues and solutions for the EDS Universal Requisition application.

---

## Quick Diagnosis

| Symptom | Likely Cause | Quick Fix |
|---------|--------------|-----------|
| Products not loading | API not running | Start API server |
| 422 errors in console | Invalid request params | Check filter values |
| Cart not saving | localStorage disabled | Enable browser storage |
| Filters not working | JavaScript error | Check browser console |
| CORS errors | API misconfigured | Check CORS settings |
| Connection refused | Wrong port/host | Verify API_CONFIG |

---

## Frontend Issues

### Products Not Loading

**Symptoms:**
- Empty product grid
- "Loading..." indicator stuck
- Network errors in console

**Diagnosis:**
```javascript
// Open browser console (F12) and run:
console.log(API_CONFIG);
console.log('API enabled:', API_CONFIG.enabled);

// Test API directly
fetch(API_CONFIG.baseUrl + '/status')
    .then(r => r.json())
    .then(console.log)
    .catch(console.error);
```

**Solutions:**

1. **API not running:**
   ```bash
   # Start the API server
   cd /mnt/c/EDS
   source .venv/bin/activate
   uvicorn api.main:app --reload --host 0.0.0.0 --port 8000
   ```

2. **Wrong API URL:**
   ```javascript
   // In universal-requisition.html, check API_CONFIG:
   const API_CONFIG = {
       baseUrl: 'http://localhost:8000/api',  // Verify this URL
       enabled: true,
   };
   ```

3. **WSL networking issue:**
   ```bash
   # Find WSL IP
   hostname -I

   # Update API_CONFIG.baseUrl to use WSL IP
   # baseUrl: 'http://172.23.x.x:8000/api'
   ```

### Filters Not Working

**Symptoms:**
- Category selection has no effect
- Vendor filter doesn't filter products
- Price range slider doesn't update

**Diagnosis:**
```javascript
// Check current filters in console
console.log(ProductGrid.currentFilters);

// Check if filter components exist
console.log(typeof CategoryFilter);
console.log(typeof VendorFilter);
```

**Solutions:**

1. **JavaScript error blocking execution:**
   - Check console for red error messages
   - Fix any syntax errors or undefined references

2. **Filters being overwritten:**
   - Ensure `loadProducts()` isn't resetting filters
   - Check filter event handlers are attached

3. **API not supporting filters:**
   ```bash
   # Test filter support
   curl "http://localhost:8000/api/products?category=Writing"
   ```

### Cart Not Persisting

**Symptoms:**
- Cart empties on page refresh
- Saved carts disappear
- Favorites not saving

**Diagnosis:**
```javascript
// Check localStorage
console.log(localStorage.getItem('eds-cart'));
console.log(localStorage.getItem('eds-saved-carts'));

// Check if localStorage is available
console.log('localStorage available:', typeof Storage !== 'undefined');
```

**Solutions:**

1. **localStorage disabled:**
   - Enable cookies/storage in browser settings
   - Check if private/incognito mode is blocking storage

2. **Storage quota exceeded:**
   ```javascript
   // Clear old data
   localStorage.clear();
   // Or selectively remove
   localStorage.removeItem('eds-recently-viewed');
   ```

3. **JSON parsing error:**
   ```javascript
   // Reset cart data
   localStorage.setItem('eds-cart', '[]');
   localStorage.setItem('eds-saved-carts', '[]');
   ```

### Search/Autocomplete Not Working

**Symptoms:**
- No autocomplete suggestions
- Search returns no results
- Search triggers errors

**Solutions:**

1. **Minimum query length:**
   - Autocomplete requires 2+ characters
   - Type more characters to trigger

2. **API endpoint issue:**
   ```bash
   curl "http://localhost:8000/api/products/search/autocomplete?q=pen"
   ```

3. **Debounce delay:**
   - Wait 300ms after typing
   - Check SearchComponent settings

---

## API Issues

### Connection Refused

**Symptoms:**
- `ERR_CONNECTION_REFUSED` in browser
- API health check fails

**Diagnosis:**
```bash
# Check if API is listening
lsof -i :8000

# Or on Windows
netstat -ano | findstr 8000
```

**Solutions:**

1. **API not started:**
   ```bash
   uvicorn api.main:app --host 0.0.0.0 --port 8000
   ```

2. **Wrong port:**
   - Check `API_PORT` in `.env`
   - Update `API_CONFIG.baseUrl` in frontend

3. **Firewall blocking:**
   ```bash
   # Linux: Allow port
   sudo ufw allow 8000

   # Windows: Check Windows Firewall settings
   ```

### 422 Unprocessable Entity

**Symptoms:**
- API returns 422 errors
- Validation error messages

**Common Causes:**

1. **Invalid pagination:**
   ```bash
   # Wrong: page=true
   # Correct: page=1
   curl "http://localhost:8000/api/products?page=1&page_size=20"
   ```

2. **Invalid price range:**
   ```bash
   # Wrong: min > max
   # Correct:
   curl "http://localhost:8000/api/products?min_price=0&max_price=100"
   ```

3. **Query too short:**
   ```bash
   # Autocomplete requires min 2 characters
   curl "http://localhost:8000/api/products/search/autocomplete?q=pe"
   ```

### 500 Internal Server Error

**Symptoms:**
- API returns 500 errors
- "Internal Server Error" message

**Diagnosis:**
```bash
# Check API logs
docker-compose logs api

# Or if running locally
# Check terminal where uvicorn is running
```

**Solutions:**

1. **Database connection failed:**
   ```bash
   # Test database connection
   python test_db.py

   # Check .env variables
   cat .env | grep DB_
   ```

2. **Missing ODBC driver:**
   ```bash
   # List installed drivers
   odbcinst -q -d

   # Install if missing
   sudo ACCEPT_EULA=Y apt-get install msodbcsql18
   ```

3. **Query error:**
   - Check API logs for SQL errors
   - Verify table/column names exist

### CORS Errors

**Symptoms:**
- "CORS policy" error in console
- Blocked by CORS

**Solutions:**

1. **Check CORS configuration:**
   ```python
   # api/main.py should have:
   from fastapi.middleware.cors import CORSMiddleware

   app.add_middleware(
       CORSMiddleware,
       allow_origins=["*"],  # Or specific origins
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```

2. **Use same origin:**
   - Serve frontend from same host as API
   - Use Docker Compose setup

---

## Database Issues

### Connection Timeout

**Symptoms:**
- "Login timeout expired"
- Connection takes too long

**Solutions:**

1. **Check server accessibility:**
   ```bash
   # Test network connectivity
   ping eds-sqlserver.eastus2.cloudapp.azure.com

   # Test port
   nc -zv eds-sqlserver.eastus2.cloudapp.azure.com 1433
   ```

2. **Increase timeout:**
   ```env
   DB_CONNECTION_TIMEOUT=60
   ```

3. **Check credentials:**
   ```bash
   # Verify .env values
   cat .env | grep -E "^DB_"
   ```

### "ODBC Driver not found"

**Symptoms:**
- "Data source name not found"
- ODBC driver error

**Solutions:**

1. **Check installed drivers:**
   ```bash
   odbcinst -q -d
   ```

2. **Install ODBC Driver 18:**

   **Ubuntu/Debian:**
   ```bash
   curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
   curl https://packages.microsoft.com/config/ubuntu/$(lsb_release -rs)/prod.list | \
       sudo tee /etc/apt/sources.list.d/mssql-release.list
   sudo apt-get update
   sudo ACCEPT_EULA=Y apt-get install msodbcsql18 unixodbc-dev
   ```

   **macOS:**
   ```bash
   brew install unixodbc
   brew tap microsoft/mssql-release https://github.com/Microsoft/homebrew-mssql-release
   brew install msodbcsql18
   ```

3. **Verify driver name:**
   ```env
   # Match exactly what's installed
   DB_DRIVER=ODBC Driver 18 for SQL Server
   ```

### Query Performance

**Symptoms:**
- Slow product loading
- Timeouts on search

**Solutions:**

1. **Add appropriate indexes:**
   ```bash
   python scripts/extract_missing_indexes.py
   ```

2. **Check query plans:**
   - Use SQL Server Management Studio
   - Look for table scans

3. **Increase connection pool:**
   ```env
   DB_POOL_MIN=5
   DB_POOL_MAX=20
   ```

**See Also:** [Database Troubleshooting](wiki/troubleshooting/index.md)

---

## Docker Issues

### Container Won't Start

**Diagnosis:**
```bash
# Check container status
docker-compose ps

# View logs
docker-compose logs api
docker-compose logs frontend
```

**Solutions:**

1. **Port conflict:**
   ```bash
   # Check what's using the port
   lsof -i :8000
   lsof -i :80

   # Change ports in .env
   API_PORT=8001
   FRONTEND_PORT=8080
   ```

2. **Missing environment file:**
   ```bash
   cp .env.example .env
   # Edit with your values
   ```

3. **Build errors:**
   ```bash
   # Rebuild from scratch
   docker-compose down
   docker-compose build --no-cache
   docker-compose up -d
   ```

### Health Check Failing

**Diagnosis:**
```bash
# Check health endpoint
curl -v http://localhost:8000/api/health

# View container health
docker inspect eds-api | grep -A 10 Health
```

**Solutions:**

1. **Database not accessible from container:**
   ```bash
   # Test from inside container
   docker-compose exec api python -c "
   from api.database import test_connection
   print(test_connection())
   "
   ```

2. **Increase health check timeout:**
   ```yaml
   # docker-compose.yml
   healthcheck:
     interval: 30s
     timeout: 10s
     retries: 5
   ```

---

## Development Issues

### Virtual Environment Problems

**Symptoms:**
- "Module not found" errors
- Wrong Python version

**Solutions:**

1. **Recreate venv:**
   ```bash
   rm -rf .venv
   python3.12 -m venv .venv
   source .venv/bin/activate
   pip install -e ".[dev,api]"
   ```

2. **Verify activation:**
   ```bash
   which python
   # Should show: /path/to/EDS/.venv/bin/python
   ```

### Test Failures

**Solutions:**

1. **Missing dependencies:**
   ```bash
   pip install -e ".[dev]"
   ```

2. **Database required:**
   ```bash
   # Run without database tests
   pytest -m "not integration"
   ```

3. **E2E browser missing:**
   ```bash
   pip install -e ".[e2e]"
   playwright install chromium
   ```

---

## Common Error Messages

| Error | Meaning | Solution |
|-------|---------|----------|
| `ModuleNotFoundError: api` | Package not installed | `pip install -e .` |
| `pyodbc.InterfaceError` | ODBC driver issue | Reinstall ODBC driver |
| `ERR_CONNECTION_REFUSED` | API not running | Start uvicorn |
| `CORS policy blocked` | Missing CORS headers | Check API CORS config |
| `422 Unprocessable Entity` | Invalid request data | Check request params |
| `localStorage is null` | Storage disabled | Enable browser storage |

---

## Getting Help

### Information to Gather

Before asking for help, collect:

1. **Error messages** - Full text from console/logs
2. **Steps to reproduce** - Exact sequence of actions
3. **Environment** - OS, browser, Python version
4. **Recent changes** - What changed before issue started

### Log Locations

| Log | Location |
|-----|----------|
| API logs | Terminal or `docker-compose logs api` |
| Browser console | DevTools (F12) → Console |
| Application logs | `/logs/` directory |
| Test output | pytest terminal output |

### Diagnostic Commands

```bash
# System info
python --version
node --version
docker --version

# Check services
curl http://localhost:8000/api/status
docker-compose ps

# Database test
python test_db.py

# Check configuration
cat .env
cat config.yaml
```

---

## See Also

- [Development Guide](DEVELOPMENT.md) - Setup instructions
- [API Reference](API_REFERENCE.md) - Endpoint documentation
- [Database Troubleshooting](wiki/troubleshooting/index.md) - SQL Server issues
- [Deployment Guide](DEPLOYMENT.md) - Docker deployment
