"""
EDS Universal Requisition API

FastAPI application for the Universal Requisition front-end.
Serves product catalog, categories, and vendors from SQL Server.

Usage:
    uvicorn api.main:app --reload --port 8000

Or run directly:
    python -m api.main
"""

import os
import logging
from contextlib import asynccontextmanager
from pathlib import Path
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse, RedirectResponse, Response

from . import __version__
from .database import test_connection, get_connection_info
from .models import APIStatus
from .middleware import RateLimitMiddleware, SecurityHeadersMiddleware
from .routes import products_router, categories_router, vendors_router
from .routes.auth import router as auth_router
from .routes.requisitions import router as requisitions_router
from .routes.ai_search import router as ai_search_router
from .routes.ai_chat import router as ai_chat_router
from .routes.admin import router as admin_router
from .routes.bids import router as bids_router
from .routes.cart import router as cart_router
from .routes.templates import router as templates_router
from .routes.search import router as search_router
from .routes.dashboard import router as dashboard_router
from .routes.reports import router as reports_router
from .routes.saved_lists import router as saved_lists_router
from .routes.agent_chat import router as agent_chat_router

_logger = logging.getLogger(__name__)

# Path to frontend directory
FRONTEND_DIR = Path(__file__).parent.parent / "frontend"


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application startup/shutdown lifecycle."""
    # Startup: start Ollama keepalive if using Ollama
    from .routes.ai_chat import start_ollama_keepalive, stop_ollama_keepalive
    from .search import get_es_client, close_es_client, ensure_index
    start_ollama_keepalive()
    # Initialize Elasticsearch index if enabled
    await ensure_index()
    yield
    # Shutdown: stop keepalive, close ES client
    stop_ollama_keepalive()
    await close_es_client()


# Create FastAPI app
app = FastAPI(
    title="EDS Universal Requisition API",
    description="Backend API for the Universal Requisition catalog and shopping system",
    version=__version__,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# Configure CORS - environment-aware
_cors_env = os.getenv("EDS_ENV", "development").lower()
_allowed_origins_env = os.getenv("EDS_CORS_ORIGINS", "")

if _allowed_origins_env:
    # Explicit origins from environment variable (comma-separated)
    _cors_origins = [o.strip() for o in _allowed_origins_env.split(",") if o.strip()]
elif _cors_env == "production":
    # Production: no wildcard, must set EDS_CORS_ORIGINS
    _cors_origins = []
    _logger.warning(
        "EDS_ENV=production but EDS_CORS_ORIGINS is not set. "
        "All cross-origin requests will be rejected. "
        "Set EDS_CORS_ORIGINS to a comma-separated list of allowed origins."
    )
else:
    # Development defaults
    _cors_origins = [
        "http://localhost:3000",
        "http://localhost:8000",
        "http://localhost:8080",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "http://127.0.0.1:8080",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=_cors_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Authorization"],
)

# Add security headers
app.add_middleware(SecurityHeadersMiddleware)

# Add rate limiting (configurable via environment)
_rate_limit = int(os.getenv("EDS_RATE_LIMIT", "120"))
app.add_middleware(RateLimitMiddleware, requests_per_minute=_rate_limit)

# Include routers
app.include_router(auth_router, prefix="/api")
app.include_router(products_router, prefix="/api")
app.include_router(categories_router, prefix="/api")
app.include_router(vendors_router, prefix="/api")
app.include_router(requisitions_router, prefix="/api")
app.include_router(ai_search_router, prefix="/api")
app.include_router(ai_chat_router, prefix="/api")
app.include_router(admin_router, prefix="/api")
app.include_router(bids_router, prefix="/api")
app.include_router(cart_router, prefix="/api")
app.include_router(templates_router, prefix="/api")
app.include_router(search_router, prefix="/api")
app.include_router(dashboard_router, prefix="/api")
app.include_router(reports_router, prefix="/api")
app.include_router(saved_lists_router, prefix="/api")
app.include_router(agent_chat_router, prefix="/api")

# Serve frontend static files (JS, CSS, images)
if FRONTEND_DIR.exists():
    app.mount("/js", StaticFiles(directory=FRONTEND_DIR / "js"), name="js")
    app.mount("/css", StaticFiles(directory=FRONTEND_DIR / "css"), name="css")
    if (FRONTEND_DIR / "images").exists():
        app.mount("/images", StaticFiles(directory=FRONTEND_DIR / "images"), name="images")
    if (FRONTEND_DIR / "assets").exists():
        app.mount("/assets", StaticFiles(directory=FRONTEND_DIR / "assets"), name="assets")

# ============================================
# Frontend Page Serving
# ============================================
#
# Instead of 30+ individual route handlers, pages are served by a
# generic handler. Clean URLs (e.g. /checkout) and .html URLs
# (e.g. /checkout.html) both resolve to the same HTML file.
#
# Special cases:
#   /          -> index.html (main SPA)
#   /login     -> login.html (falls back to index.html)
#   /search    -> search-results.html (extra alias)
#   /product   -> product-detail.html (extra alias)

# Route aliases: clean URL -> HTML filename (without .html)
_ROUTE_ALIASES = {
    "search": "search-results",
    "product": "product-detail",
    "agent-chat": "agent",
    "dba-agent": "agent",
}

# Default fallback page when a requested HTML file doesn't exist
_FALLBACK_PAGE = "index.html"


def _resolve_frontend_page(page_name: str) -> Path | None:
    """
    Resolve a page name to a safe frontend HTML file path.

    Returns the resolved Path if the file exists and is inside FRONTEND_DIR,
    or None if the page doesn't exist or the path escapes FRONTEND_DIR.
    """
    html_file = (FRONTEND_DIR / f"{page_name}.html").resolve()
    if html_file.is_relative_to(FRONTEND_DIR.resolve()) and html_file.is_file():
        return html_file
    return None


@app.get("/", tags=["Frontend"])
async def root():
    """Serve the main frontend application."""
    index = _resolve_frontend_page("index")
    if index:
        return FileResponse(index, headers={"Cache-Control": "no-cache"})
    return {"message": "EDS Universal Requisition API", "docs": "/docs"}


@app.get("/api/status", response_model=APIStatus, tags=["Health"])
async def get_status():
    """
    Get API status and health check.
    Tests database connectivity.
    """
    from .routes.ai_chat import AI_CHAT_ENABLED, _LLM_PROVIDER
    from .search import es_healthy, ES_ENABLED

    db_connected = test_connection()
    es_ok = await es_healthy() if ES_ENABLED else False
    return APIStatus(
        status="healthy" if db_connected else "degraded",
        database_connected=db_connected,
        version=__version__,
        ai_enabled=AI_CHAT_ENABLED,
        ai_provider=_LLM_PROVIDER if AI_CHAT_ENABLED else None,
        search_enabled=ES_ENABLED,
        search_connected=es_ok,
    )


@app.get("/api/health", tags=["Health"])
async def health_check():
    """Simple health check for load balancers."""
    return {"status": "ok"}


@app.get("/api/debug/connection", tags=["Health"])
async def debug_connection():
    """
    Debug endpoint to check database connection configuration.
    Only available when EDS_DEBUG=true environment variable is set.
    """
    if os.getenv("EDS_DEBUG", "").lower() not in ("true", "1", "yes"):
        return JSONResponse(
            status_code=404,
            content={"detail": "Page not found"},
        )

    from .database import execute_query

    conn_info = get_connection_info()
    db_connected = test_connection()

    result = {
        "database_connected": db_connected,
        "config": conn_info,
    }

    if db_connected:
        try:
            tables = execute_query("""
                SELECT TABLE_NAME
                FROM INFORMATION_SCHEMA.TABLES
                WHERE TABLE_TYPE = 'BASE TABLE'
                AND TABLE_NAME IN ('Items', 'Products', 'Category', 'Vendors', 'CrossRefs')
                ORDER BY TABLE_NAME
            """)
            result["tables"] = [t['TABLE_NAME'] for t in tables]
        except Exception as e:
            result["error"] = str(e)

    return result


@app.get("/favicon.ico", tags=["Frontend"])
async def favicon():
    """Serve favicon."""
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect fill="#1c1a83" width="32" height="32" rx="6"/><text x="16" y="22" text-anchor="middle" fill="white" font-family="Arial" font-weight="bold" font-size="16">E</text></svg>'''
    return Response(content=svg, media_type="image/svg+xml")


@app.get("/{full_path:path}", tags=["Frontend"])
async def catch_all(full_path: str):
    """
    Generic frontend page handler and 404 fallback.

    Resolves clean URLs (/checkout) and .html URLs (/checkout.html)
    to frontend HTML files. Returns 404 for unknown paths.
    Legacy versioned URLs (/v2, /v3, ..., /v7, /reimagined) redirect to root.
    """
    # Skip API-like paths (shouldn't reach here, but be safe)
    if full_path.startswith("api/"):
        return JSONResponse(
            status_code=404,
            content={"detail": "API endpoint not found", "path": full_path}
        )

    # Redirect legacy versioned frontend URLs to root
    stripped = full_path.rstrip("/")
    if stripped in ("v2", "v3", "v4", "v5", "v6", "v7", "reimagined") or \
       stripped.startswith(("v2/", "v3/", "v4/", "v5/", "v6/", "v7/", "reimagined/")):
        return RedirectResponse(url="/", status_code=301)

    # Strip trailing .html to normalize
    page_name = full_path.removesuffix(".html").rstrip("/")

    # Apply route aliases (e.g. "search" -> "search-results")
    page_name = _ROUTE_ALIASES.get(page_name, page_name)

    # Only serve known HTML files — _resolve_frontend_page handles
    # directory traversal prevention via resolve() + is_relative_to()
    html_file = _resolve_frontend_page(page_name)
    if html_file:
        return FileResponse(html_file, headers={"Cache-Control": "no-cache"})

    # 404 fallback
    not_found_file = FRONTEND_DIR / "404.html"
    if not_found_file.exists():
        return FileResponse(not_found_file, status_code=404)
    return JSONResponse(
        status_code=404,
        content={"detail": "Page not found", "path": full_path}
    )


# Run with uvicorn if executed directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "api.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
