"""
Category API endpoints.
"""

from typing import List
from fastapi import APIRouter, HTTPException

from ..database import execute_query, execute_single
from ..models import Category
from ..cache import get_cache, CACHE_TTL_LONG

router = APIRouter(prefix="/categories", tags=["Categories"])

# Cache key for categories list
CATEGORIES_CACHE_KEY = "categories_list"


@router.get("", response_model=List[Category])
async def get_categories():
    """
    Get all product categories with product counts.
    Categories are cached for 1 hour since they rarely change.
    """
    try:
        # Check cache first
        cache = get_cache()
        cached_result = await cache.get(CATEGORIES_CACHE_KEY)
        if cached_result is not None:
            return cached_result

        # Cache miss - fetch from database
        query = """
            SELECT
                c.CategoryId as id,
                c.Name as name,
                COUNT(i.ItemId) as product_count
            FROM Category c
            LEFT JOIN Items i ON c.CategoryId = i.CategoryId AND i.Active = 1 AND i.ListPrice > 0
            WHERE c.Active = 1
            GROUP BY c.CategoryId, c.Name
            ORDER BY c.Name
        """
        rows = execute_query(query)
        result = [
            Category(
                id=row["id"],
                name=row["name"] or "Unknown",
                product_count=row.get("product_count", 0)
            )
            for row in rows
        ]

        # Store in cache for 1 hour
        await cache.set(CATEGORIES_CACHE_KEY, result, CACHE_TTL_LONG)

        return result

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/{category_id}", response_model=Category)
async def get_category(category_id: int):
    """Get a single category by ID."""
    try:
        query = """
            SELECT
                c.CategoryId as id,
                c.Name as name,
                COUNT(i.ItemId) as product_count
            FROM Category c
            LEFT JOIN Items i ON c.CategoryId = i.CategoryId AND i.Active = 1 AND i.ListPrice > 0
            WHERE c.CategoryId = ?
            GROUP BY c.CategoryId, c.Name
        """
        row = execute_single(query, (category_id,))

        if not row:
            raise HTTPException(status_code=404, detail="Category not found")

        return Category(
            id=row["id"],
            name=row["name"] or "Unknown",
            product_count=row.get("product_count", 0)
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
