"""
Vendor API endpoints.
"""

from typing import List, Optional
from fastapi import APIRouter, HTTPException, Query

from ..database import execute_query, execute_single
from ..models import Vendor
from ..cache import get_cache, CACHE_TTL_MEDIUM

router = APIRouter(prefix="/vendors", tags=["Vendors"])

# Cache key for vendors list (no search filter)
VENDORS_CACHE_KEY = "vendors_list_{limit}"


@router.get("", response_model=List[Vendor])
async def get_vendors(
    search: Optional[str] = Query(None, description="Search vendor name"),
    limit: int = Query(100, ge=1, le=500, description="Max results")
):
    """
    Get all vendors with optional search filter.
    Vendors list (without search) is cached for 30 minutes.
    """
    try:
        # Filter out placeholder vendor names, junk data, and EDS default vendor
        exclude_names = """
            v.Name NOT IN ('Unknown', 'Unknown Vendor', 'UNKNOWN', 'TBD', 'N/A', '', '.')
            AND LTRIM(RTRIM(v.Name)) != ''
            AND LTRIM(RTRIM(v.Name)) != '.'
            AND LEN(LTRIM(RTRIM(v.Name))) > 2
            AND v.Name NOT LIKE '%NO BID%'
            AND v.Name NOT LIKE '%NOT BID%'
            AND v.Name NOT LIKE '%NO AWARD%'
            AND v.Name NOT LIKE '%DELETED%'
            AND v.Name NOT LIKE '**%'
        """
        exclude_eds = "v.VendorId != 7853"  # EDS default catalog vendor

        if search:
            # Searches are not cached - need fresh results
            query = f"""
                SELECT TOP (?)
                    v.VendorId as id,
                    LTRIM(RTRIM(v.Name)) as name,
                    v.Code as code,
                    COUNT(i.ItemId) as product_count
                FROM Vendors v
                LEFT JOIN Items i ON v.VendorId = i.VendorId AND i.Active = 1 AND i.ListPrice > 0
                    AND i.Description IS NOT NULL AND i.Description != ''
                WHERE v.Active = 1 AND v.Name LIKE ? AND {exclude_names} AND {exclude_eds}
                GROUP BY v.VendorId, v.Name, v.Code
                HAVING COUNT(i.ItemId) > 0
                ORDER BY LTRIM(RTRIM(v.Name))
            """
            rows = execute_query(query, (limit, f"%{search}%"))
        else:
            # Check cache for full vendor list
            cache = get_cache()
            cache_key = VENDORS_CACHE_KEY.format(limit=limit)
            cached_result = await cache.get(cache_key)
            if cached_result is not None:
                return cached_result

            # Cache miss - fetch from database
            query = f"""
                SELECT TOP (?)
                    v.VendorId as id,
                    LTRIM(RTRIM(v.Name)) as name,
                    v.Code as code,
                    COUNT(i.ItemId) as product_count
                FROM Vendors v
                LEFT JOIN Items i ON v.VendorId = i.VendorId AND i.Active = 1 AND i.ListPrice > 0
                    AND i.Description IS NOT NULL AND i.Description != ''
                WHERE v.Active = 1 AND {exclude_names} AND {exclude_eds}
                GROUP BY v.VendorId, v.Name, v.Code
                HAVING COUNT(i.ItemId) > 0
                ORDER BY LTRIM(RTRIM(v.Name))
            """
            rows = execute_query(query, (limit,))

            result = [
                Vendor(
                    id=row["id"],
                    name=row["name"] or "Unknown",
                    code=row.get("code"),
                    product_count=row.get("product_count", 0)
                )
                for row in rows
            ]

            # Cache for 30 minutes
            await cache.set(cache_key, result, CACHE_TTL_MEDIUM)

            return result

        return [
            Vendor(
                id=row["id"],
                name=row["name"] or "Unknown",
                code=row.get("code"),
                product_count=row.get("product_count", 0)
            )
            for row in rows
        ]

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")


@router.get("/{vendor_id}", response_model=Vendor)
async def get_vendor(vendor_id: int):
    """Get a single vendor by ID."""
    try:
        query = """
            SELECT
                v.VendorId as id,
                v.Name as name,
                v.Code as code,
                COUNT(i.ItemId) as product_count
            FROM Vendors v
            LEFT JOIN Items i ON v.VendorId = i.VendorId AND i.Active = 1 AND i.ListPrice > 0
            WHERE v.VendorId = ?
            GROUP BY v.VendorId, v.Name, v.Code
        """
        row = execute_single(query, (vendor_id,))

        if not row:
            raise HTTPException(status_code=404, detail="Vendor not found")

        return Vendor(
            id=row["id"],
            name=row["name"] or "Unknown",
            code=row.get("code"),
            product_count=row.get("product_count", 0)
        )

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
