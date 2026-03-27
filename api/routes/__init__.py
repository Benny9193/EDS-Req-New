"""API route modules."""

from .products import router as products_router
from .categories import router as categories_router
from .vendors import router as vendors_router

__all__ = ["products_router", "categories_router", "vendors_router"]
