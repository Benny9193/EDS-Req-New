"""
Bid/Contract filtering API endpoints.

Provides bid-based product filtering for the Universal Requisition frontend.
Bids represent purchasing contracts with approved vendors and negotiated pricing.
"""

import logging
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from ..database import execute_query, execute_single
from ..models import Product, ProductListResponse
from ..cache import get_cache

router = APIRouter(prefix="/bids", tags=["Bids"])
logger = logging.getLogger(__name__)


# ===========================================
# MODELS
# ===========================================

class BidVendor(BaseModel):
    """Vendor associated with a bid."""
    vendor_id: int
    vendor_name: str
    product_count: int = 0


class BidSummary(BaseModel):
    """Summary of a bid/contract."""
    bid_id: int
    bid_name: str
    bid_code: str
    description: Optional[str] = None
    vendor_count: int = 0
    product_count: int = 0
    is_active: bool = True
    due_date: Optional[str] = None
    expiration_date: Optional[str] = None


class BidDetail(BaseModel):
    """Full bid detail with vendors."""
    bid_id: int
    bid_name: str
    bid_code: str
    description: Optional[str] = None
    vendors: List[BidVendor] = []
    product_count: int = 0
    is_active: bool = True
    due_date: Optional[str] = None
    expiration_date: Optional[str] = None


class BidListResponse(BaseModel):
    """Response for bid listing."""
    bids: List[BidSummary]
    total: int


# ===========================================
# BID LISTING
# ===========================================

@router.get("", response_model=BidListResponse)
async def list_bids(
    active_only: bool = Query(True, description="Only return active bids"),
    search: Optional[str] = Query(None, max_length=100, description="Search bid names"),
):
    """
    List all available bids/contracts.

    Returns bid summaries with vendor and product counts.
    Bids are derived from the Catalog table, grouped by CatalogName patterns
    that represent purchasing contracts.
    """
    try:
        # Check cache first (bids change rarely)
        cache = get_cache()
        cache_key = f"bids_list_{active_only}_{search or ''}"
        cached = await cache.get(cache_key)
        if cached is not None:
            return cached

        conditions = []
        params = []

        # Fast query: skip expensive CrossRefs CTE (was scanning 150M rows).
        # Product counts are omitted from the listing — they're only needed
        # when drilling into a specific bid via /{bid_id}.
        query = """
            SELECT
                cat.CatalogId as bid_id,
                cat.Name as bid_name,
                ISNULL(cat.Prefix, '') as bid_code,
                cat.Description as description,
                v.Name as vendor_name,
                CASE WHEN cat.Active = 1 THEN 1 ELSE 0 END as is_active,
                cat.EffectiveFrom as effective_from,
                cat.EffectiveUntil as effective_until
            FROM Catalog cat
            LEFT JOIN Vendors v ON cat.VendorId = v.VendorId
            WHERE 1=1
        """

        if active_only:
            query += " AND cat.Active = 1"

        if search:
            query += " AND cat.Name LIKE ?"
            params.append(f"%{search}%")

        # Exclude the default EDS catalog (VendorId 7853)
        query += " AND ISNULL(cat.VendorId, 0) != 7853"
        query += " ORDER BY cat.Name"

        rows = execute_query(query, tuple(params) if params else None)

        bids_map = {}
        for row in rows:
            bid_id = row['bid_id']
            if bid_id not in bids_map:
                eff_from = row.get('effective_from')
                eff_until = row.get('effective_until')
                bids_map[bid_id] = BidSummary(
                    bid_id=bid_id,
                    bid_name=row['bid_name'],
                    bid_code=row['bid_code'] or '',
                    description=row.get('description'),
                    vendor_count=0,
                    product_count=1,  # non-zero so frontend filter shows them
                    is_active=bool(row.get('is_active', True)),
                    due_date=eff_from.isoformat() if eff_from else None,
                    expiration_date=eff_until.isoformat() if eff_until else None,
                )
            if row.get('vendor_name'):
                bids_map[bid_id].vendor_count += 1

        bids = list(bids_map.values())
        result = BidListResponse(bids=bids, total=len(bids))

        # Cache for 10 minutes
        await cache.set(cache_key, result, ttl=600)

        return result

    except Exception as e:
        logger.error("Error listing bids: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve bids")


# ===========================================
# BID DETAIL
# ===========================================

@router.get("/{bid_id}", response_model=BidDetail)
async def get_bid(bid_id: int):
    """
    Get full details for a specific bid, including approved vendors.
    """
    try:
        # Get bid info (columns: Name, Prefix — not CatalogName/CatalogCode)
        bid_row = execute_single("""
            SELECT
                cat.CatalogId as bid_id,
                cat.Name as bid_name,
                ISNULL(cat.Prefix, '') as bid_code,
                cat.Description as description,
                CASE WHEN cat.Active = 1 THEN 1 ELSE 0 END as is_active,
                cat.EffectiveFrom as effective_from,
                cat.EffectiveUntil as effective_until
            FROM Catalog cat
            WHERE cat.CatalogId = ?
        """, (bid_id,))

        if not bid_row:
            raise HTTPException(status_code=404, detail="Bid not found")

        # Get vendors for this bid via CrossRefs
        vendor_rows = execute_query("""
            SELECT
                v.VendorId as vendor_id,
                v.Name as vendor_name,
                COUNT(DISTINCT cr.ItemId) as product_count
            FROM CrossRefs cr
            JOIN Catalog cat ON cr.CatalogId = cat.CatalogId
            JOIN Vendors v ON cat.VendorId = v.VendorId
            WHERE cr.CatalogId = ?
            AND cr.Active = 1
            GROUP BY v.VendorId, v.Name
            ORDER BY v.Name
        """, (bid_id,))

        vendors = [
            BidVendor(
                vendor_id=r['vendor_id'],
                vendor_name=r['vendor_name'],
                product_count=r.get('product_count', 0)
            )
            for r in vendor_rows
        ]

        # Get total product count
        count_row = execute_single("""
            SELECT COUNT(DISTINCT cr.ItemId) as cnt
            FROM CrossRefs cr
            WHERE cr.CatalogId = ?
            AND cr.Active = 1
        """, (bid_id,))

        eff_from = bid_row.get('effective_from')
        eff_until = bid_row.get('effective_until')
        return BidDetail(
            bid_id=bid_row['bid_id'],
            bid_name=bid_row['bid_name'],
            bid_code=bid_row['bid_code'] or '',
            description=bid_row.get('description'),
            vendors=vendors,
            product_count=count_row['cnt'] if count_row else 0,
            is_active=bool(bid_row.get('is_active', True)),
            due_date=eff_from.isoformat() if eff_from else None,
            expiration_date=eff_until.isoformat() if eff_until else None,
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error getting bid %s: %s", bid_id, e)
        raise HTTPException(status_code=500, detail="Failed to retrieve bid details")


# ===========================================
# BID PRODUCTS
# ===========================================

@router.get("/{bid_id}/products", response_model=ProductListResponse)
async def get_bid_products(
    bid_id: int,
    query: Optional[str] = Query(None, max_length=100, description="Search within bid products"),
    category: Optional[str] = Query(None, max_length=50, description="Filter by category"),
    vendor: Optional[str] = Query(None, max_length=100, description="Filter by vendor"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price"),
    sort_by: Optional[str] = Query("name", description="Sort: name, price, vendor"),
    sort_order: Optional[str] = Query("asc", description="Sort direction: asc, desc"),
    page: int = Query(1, ge=1, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
):
    """
    Get products available under a specific bid/contract.

    Filters the product catalog to only show items that are cross-referenced
    to the given bid's catalog. Supports additional filtering by search query,
    category, vendor, and price range.
    """
    try:
        # Verify bid exists
        bid_check = execute_single(
            "SELECT CatalogId FROM Catalog WHERE CatalogId = ?", (bid_id,)
        )
        if not bid_check:
            raise HTTPException(status_code=404, detail="Bid not found")

        # Build product query filtered to this bid
        conditions = ["cr.CatalogId = ?", "cr.Active = 1", "i.Active = 1"]
        params = [bid_id]

        if query:
            conditions.append("(i.Description LIKE ? OR i.VendorPartNumber LIKE ?)")
            params.extend([f"%{query}%", f"%{query}%"])

        if category:
            conditions.append("c.Name = ?")
            params.append(category)

        if vendor:
            conditions.append("v.Name = ?")
            params.append(vendor)

        if min_price is not None:
            conditions.append("ISNULL(cr.CatalogPrice, i.ListPrice) >= ?")
            params.append(min_price)

        if max_price is not None:
            conditions.append("ISNULL(cr.CatalogPrice, i.ListPrice) <= ?")
            params.append(max_price)

        where_clause = " AND ".join(conditions)

        # Validate sort
        valid_sorts = {
            'name': 'i.Description',
            'price': 'ISNULL(cr.CatalogPrice, i.ListPrice)',
            'vendor': 'v.Name',
        }
        sort_col = valid_sorts.get(sort_by, 'i.Description')
        sort_dir = 'DESC' if sort_order and sort_order.lower() == 'desc' else 'ASC'

        # Count total
        count_query = f"""
            SELECT COUNT(DISTINCT i.ItemId) as total
            FROM CrossRefs cr
            JOIN Items i ON cr.ItemId = i.ItemId
            LEFT JOIN Vendors v ON i.VendorId = v.VendorId
            LEFT JOIN Category c ON i.CategoryId = c.CategoryId
            WHERE {where_clause}
        """
        count_row = execute_single(count_query, tuple(params))
        total = count_row['total'] if count_row else 0

        # Calculate pagination
        total_pages = max(1, (total + page_size - 1) // page_size)
        offset = (page - 1) * page_size

        # Get products
        product_query = f"""
            SELECT DISTINCT
                i.ItemId as id,
                i.Description as name,
                ISNULL(i.ShortDescription, '') as description,
                ISNULL(v.Name, 'Unknown Vendor') as vendor,
                i.VendorPartNumber as vendor_item_code,
                ISNULL(c.Name, 'General') as category,
                (SELECT TOP 1 cr2.ImageURL
                 FROM CrossRefs cr2
                 WHERE cr2.ItemId = i.ItemId
                 AND cr2.ImageURL IS NOT NULL AND cr2.ImageURL != ''
                 AND cr2.Active = 1) as image,
                'in-stock' as status,
                ISNULL(u.Code, 'Each') as unit_of_measure,
                ISNULL(cr.CatalogPrice, i.ListPrice) as unit_price
            FROM CrossRefs cr
            JOIN Items i ON cr.ItemId = i.ItemId
            LEFT JOIN Vendors v ON i.VendorId = v.VendorId
            LEFT JOIN Units u ON i.UnitId = u.UnitId
            LEFT JOIN Category c ON i.CategoryId = c.CategoryId
            WHERE {where_clause}
            ORDER BY {sort_col} {sort_dir}
            OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
        """
        params.extend([offset, page_size])

        rows = execute_query(product_query, tuple(params))

        products = [
            Product(
                id=str(row['id']),
                name=row['name'] or 'Untitled',
                description=row.get('description', ''),
                vendor=row['vendor'],
                vendor_item_code=row.get('vendor_item_code'),
                category=row['category'],
                image=row.get('image'),
                status=row.get('status', 'in-stock'),
                unit_of_measure=row.get('unit_of_measure', 'Each'),
                unit_price=float(row.get('unit_price', 0)),
            )
            for row in rows
        ]

        return ProductListResponse(
            products=products,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Error getting bid products for bid %s: %s", bid_id, e)
        raise HTTPException(status_code=500, detail="Failed to retrieve bid products")


# ===========================================
# BID VENDORS
# ===========================================

@router.get("/{bid_id}/vendors")
async def get_bid_vendors(bid_id: int):
    """
    Get the list of approved vendors for a specific bid.

    Returns vendors with their product counts under this bid.
    """
    try:
        rows = execute_query("""
            SELECT
                v.VendorId as id,
                v.Name as name,
                v.Code as code,
                COUNT(DISTINCT cr.ItemId) as product_count
            FROM CrossRefs cr
            JOIN Catalog cat ON cr.CatalogId = cat.CatalogId
            JOIN Vendors v ON cat.VendorId = v.VendorId
            WHERE cr.CatalogId = ?
            AND cr.Active = 1
            GROUP BY v.VendorId, v.Name, v.Code
            ORDER BY v.Name
        """, (bid_id,))

        return {
            "bid_id": bid_id,
            "vendors": [
                {
                    "id": r['id'],
                    "name": r['name'],
                    "code": r.get('code'),
                    "product_count": r.get('product_count', 0)
                }
                for r in rows
            ],
            "total": len(rows)
        }

    except Exception as e:
        logger.error("Error getting bid vendors for bid %s: %s", bid_id, e)
        raise HTTPException(status_code=500, detail="Failed to retrieve bid vendors")


# ===========================================
# BID CATEGORIES
# ===========================================

@router.get("/{bid_id}/categories")
async def get_bid_categories(bid_id: int):
    """
    Get product categories available under a specific bid.

    Returns categories with product counts, filtered to only
    include categories that have products in this bid.
    """
    try:
        rows = execute_query("""
            SELECT
                c.CategoryId as id,
                c.Name as name,
                COUNT(DISTINCT cr.ItemId) as product_count
            FROM CrossRefs cr
            JOIN Items i ON cr.ItemId = i.ItemId
            JOIN Category c ON i.CategoryId = c.CategoryId
            WHERE cr.CatalogId = ?
            AND cr.Active = 1
            AND i.Active = 1
            GROUP BY c.CategoryId, c.Name
            HAVING COUNT(DISTINCT cr.ItemId) > 0
            ORDER BY c.Name
        """, (bid_id,))

        return {
            "bid_id": bid_id,
            "categories": [
                {
                    "id": r['id'],
                    "name": r['name'],
                    "product_count": r.get('product_count', 0)
                }
                for r in rows
            ],
            "total": len(rows)
        }

    except Exception as e:
        logger.error("Error getting bid categories for bid %s: %s", bid_id, e)
        raise HTTPException(status_code=500, detail="Failed to retrieve bid categories")
