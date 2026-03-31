"""
Product API endpoints.

Connects to the Items table in the EDS database.
"""

import re
import logging
from typing import Optional, List
from fastapi import APIRouter, HTTPException, Query
from ..database import execute_query, execute_single
from ..models import Product, ProductListResponse, ProductStatus
from ..cache import get_cache, CACHE_TTL_SHORT
from ..search import get_es_client, ES_ENABLED, ES_INDEX

router = APIRouter(prefix="/products", tags=["Products"])
logger = logging.getLogger(__name__)

# Input validation constants
MAX_QUERY_LENGTH = 100
MAX_CATEGORY_LENGTH = 50
MAX_VENDOR_LENGTH = 100
VALID_STATUS_VALUES = {'in-stock', 'low-stock', 'out-of-stock', 'discontinued'}


def sanitize_search_input(value: str) -> str:
    """Sanitize search input to prevent SQL injection patterns."""
    if not value:
        return value
    # Remove potentially dangerous characters while keeping search-friendly ones
    # Allow alphanumeric, spaces, hyphens, and basic punctuation
    sanitized = re.sub(r'[^\w\s\-.,\'\"()]', '', value)
    return sanitized.strip()[:MAX_QUERY_LENGTH]


def validate_status_filter(status: str) -> List[str]:
    """Validate and parse status filter values."""
    if not status:
        return []
    status_list = [s.strip().lower() for s in status.split(',') if s.strip()]
    return [s for s in status_list if s in VALID_STATUS_VALUES]


# SQL query to get products from Items table
# Optimized: Removed expensive CrossRefs CTE that was scanning 150M rows
# Vendor lookup: First tries Items.VendorId, then falls back to CrossRefs->Catalog->Vendors
PRODUCT_BASE_QUERY = """
SELECT
    i.ItemId as id,
    i.ItemCode as item_code,
    i.Description as name,
    ISNULL(i.ShortDescription, '') as description,
    ISNULL(v.Name, 'Unknown Vendor') as vendor,
    i.VendorPartNumber as vendor_item_code,
    ISNULL(c.Name, 'General') as category,
    NULL as image,
    CASE
        WHEN i.Active = 0 THEN 'discontinued'
        ELSE 'in-stock'
    END as status,
    ISNULL(u.Code, 'Each') as unit_of_measure,
    ISNULL(i.ListPrice, 0) as unit_price
FROM Items i
LEFT JOIN Vendors v ON i.VendorId = v.VendorId
LEFT JOIN Units u ON i.UnitId = u.UnitId
LEFT JOIN Category c ON i.CategoryId = c.CategoryId
WHERE i.Active = 1
AND i.Description IS NOT NULL AND i.Description != ''
"""

# Lightweight count query — no JOINs needed for unfiltered counts
PRODUCT_COUNT_QUERY = """
SELECT COUNT(*) as total FROM Items i
WHERE i.Active = 1 AND i.Description IS NOT NULL AND i.Description != ''
AND i.ListPrice > 0
"""


def clean_string(value: str) -> str:
    """Clean string by removing control characters and extra whitespace."""
    if not value:
        return value
    # Remove control characters and normalize whitespace
    return ' '.join(value.split()).strip()


def map_row_to_product(row: dict) -> Product:
    """Convert database row to Product model."""
    return Product(
        id=str(row.get("id", "")),
        name=clean_string(row.get("name", "")) or "Unknown Product",
        description=clean_string(row.get("description", "")) or "",
        vendor=clean_string(row.get("vendor", "")) or "Unknown Vendor",
        vendor_item_code=clean_string(row.get("vendor_item_code") or row.get("item_code", "")),
        category=clean_string(row.get("category", "")) or "General",
        image=row.get("image"),
        status=row.get("status") or "in-stock",
        unit_of_measure=clean_string(row.get("unit_of_measure", "")) or "Each",
        unit_price=float(row.get("unit_price", 0) or 0),
        tags=[]
    )


@router.get("", response_model=ProductListResponse)
async def get_products(
    query: Optional[str] = Query(None, max_length=MAX_QUERY_LENGTH, description="Search query"),
    category: Optional[str] = Query(None, max_length=MAX_CATEGORY_LENGTH, description="Filter by category"),
    vendor: Optional[str] = Query(None, max_length=MAX_VENDOR_LENGTH, description="Filter by vendor"),
    status: Optional[str] = Query(None, description="Filter by status (comma-separated: in-stock,low-stock,out-of-stock,discontinued)"),
    min_price: Optional[float] = Query(None, ge=0, le=1000000, description="Minimum price"),
    max_price: Optional[float] = Query(None, ge=0, le=1000000, description="Maximum price"),
    sort_by: Optional[str] = Query(None, description="Sort field: price, name"),
    sort_order: Optional[str] = Query("asc", description="Sort order: asc, desc"),
    page: int = Query(1, ge=1, le=10000, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page")
):
    """
    Get paginated list of products with optional filters.

    - **query**: Search in product name and description (max 100 chars)
    - **category**: Filter by exact category name
    - **vendor**: Filter by vendor name (partial match)
    - **status**: Filter by stock status
    - **min_price/max_price**: Price range filter (0-1,000,000)
    - **page/page_size**: Pagination
    """
    try:
        # Validate price range
        if min_price is not None and max_price is not None and min_price > max_price:
            raise HTTPException(status_code=400, detail="min_price cannot be greater than max_price")

        # Try Elasticsearch first when enabled (for search queries and default browse)
        if ES_ENABLED:
            es_result = await _try_es_search(
                query, category, vendor, min_price, max_price,
                sort_by, sort_order, page, page_size
            )
            if es_result is not None:
                return es_result

        # SQL fallback: Build dynamic WHERE clause
        conditions = []
        params = []

        if query:
            # Sanitize search input
            safe_query = sanitize_search_input(query)
            if safe_query:
                # Optimized search: prefix-first strategy for better index usage
                # Prefix matches (e.g., "pencil%") can use indexes
                # Word boundary matches (e.g., "% pencil%") catch mid-string terms
                conditions.append("""(
                    i.Description LIKE ? OR i.Description LIKE ?
                    OR i.ItemCode LIKE ?
                    OR i.ShortDescription LIKE ? OR i.ShortDescription LIKE ?
                )""")
                params.extend([
                    f"{safe_query}%",      # Description prefix match (index-friendly)
                    f"% {safe_query}%",    # Description word boundary match
                    f"{safe_query}%",      # ItemCode prefix match
                    f"{safe_query}%",      # ShortDescription prefix
                    f"% {safe_query}%"     # ShortDescription word boundary
                ])

        if category and category != "All":
            # Support both category ID (numeric) and category name
            if category.isdigit():
                conditions.append("i.CategoryId = ?")
                params.append(int(category))
            else:
                conditions.append("c.Name = ?")
                params.append(category)

        if vendor:
            # Sanitize vendor input
            safe_vendor = sanitize_search_input(vendor)
            if safe_vendor:
                conditions.append("v.Name LIKE ?")
                params.append(f"%{safe_vendor}%")

        if min_price is not None:
            conditions.append("i.ListPrice >= ?")
            params.append(min_price)

        if max_price is not None:
            conditions.append("i.ListPrice <= ?")
            params.append(max_price)

        # Status filter (supports comma-separated values, validated)
        if status:
            valid_statuses = validate_status_filter(status)
            if valid_statuses:
                status_conditions = []
                for s in valid_statuses:
                    if s == 'in-stock':
                        status_conditions.append("i.Active = 1")
                    elif s in ('discontinued', 'out-of-stock'):
                        status_conditions.append("i.Active = 0")
                if status_conditions:
                    conditions.append(f"({' OR '.join(status_conditions)})")

        # Only items with prices and descriptions by default
        conditions.append("i.ListPrice > 0")
        conditions.append("i.Description IS NOT NULL AND i.Description != ''")

        # Build full query with conditions
        where_clause = ""
        if conditions:
            where_clause = " AND " + " AND ".join(conditions)

        # Count total — use cached lightweight count when no filters active
        needs_join = category or vendor
        if not conditions or (len(conditions) == 2 and not needs_join):
            # No filters beyond the default price/description — use fast count
            cache = get_cache()
            total = await cache.get("product_total_count")
            if total is None:
                count_result = execute_single(PRODUCT_COUNT_QUERY)
                total = count_result["total"] if count_result else 0
                await cache.set("product_total_count", total, ttl=300)  # cache 5 min
        else:
            count_query = f"""
                SELECT COUNT(*) as total
                FROM Items i
                {'LEFT JOIN Vendors v ON i.VendorId = v.VendorId' if vendor else ''}
                {'LEFT JOIN Category c ON i.CategoryId = c.CategoryId' if category else ''}
                WHERE i.Active = 1 {where_clause}
            """
            count_result = execute_single(count_query, tuple(params) if params else None)
            total = count_result["total"] if count_result else 0

        # Calculate pagination
        offset = (page - 1) * page_size
        total_pages = (total + page_size - 1) // page_size if total > 0 else 1

        # Build ORDER BY clause based on sort parameters
        order_clause = "i.Description"  # default
        if sort_by == "price":
            order_clause = "i.ListPrice"
        elif sort_by == "name":
            order_clause = "i.Description"

        # Validate and apply sort order
        order_direction = "ASC"
        if sort_order and sort_order.lower() == "desc":
            order_direction = "DESC"

        # Get paginated results
        data_query = f"""
            {PRODUCT_BASE_QUERY} {where_clause}
            ORDER BY {order_clause} {order_direction}
            OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
        """
        params.extend([offset, page_size])

        rows = execute_query(data_query, tuple(params))
        products = [map_row_to_product(row) for row in rows]

        return ProductListResponse(
            products=products,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Failed to fetch products: %s", e)
        raise HTTPException(status_code=500, detail="Failed to fetch products")


@router.get("/search/autocomplete")
async def autocomplete_search(
    q: str = Query(..., min_length=2, max_length=MAX_QUERY_LENGTH, description="Search query"),
    limit: int = Query(10, ge=1, le=20, description="Max results"),
    vendor: Optional[str] = Query(None, description="Filter by vendor name"),
    category: Optional[str] = Query(None, description="Filter by category name or ID")
) -> List[Product]:
    """
    Quick autocomplete search for products.
    Returns top matches for the search input.
    """
    try:
        # Sanitize search input
        safe_q = sanitize_search_input(q)
        if not safe_q or len(safe_q) < 2:
            return []
        safe_vendor = sanitize_search_input(vendor) if vendor else None
        safe_category = sanitize_search_input(category) if category else None

        # Try ES autocomplete first
        if ES_ENABLED:
            es_result = await _try_es_autocomplete(safe_q, limit, vendor_filter=safe_vendor, category_filter=safe_category)
            if es_result is not None:
                return es_result

        # SQL fallback: Check cache first
        cache = get_cache()
        vendor_key = safe_vendor.lower() if safe_vendor else "all"
        category_key = safe_category.lower() if safe_category else "all"
        cache_key = f"autocomplete_{safe_q.lower()}_{vendor_key}_{category_key}_{limit}"
        cached_result = await cache.get(cache_key)
        if cached_result is not None:
            return cached_result

        query = """
            SELECT TOP (?)
                i.ItemId as id,
                i.ItemCode as item_code,
                i.Description as name,
                ISNULL(i.ShortDescription, '') as description,
                ISNULL(v.Name, 'Unknown Vendor') as vendor,
                i.VendorPartNumber as vendor_item_code,
                ISNULL(c.Name, 'General') as category,
                NULL as image,
                'in-stock' as status,
                ISNULL(u.Code, 'Each') as unit_of_measure,
                ISNULL(i.ListPrice, 0) as unit_price
            FROM Items i
            LEFT JOIN Vendors v ON i.VendorId = v.VendorId
            LEFT JOIN Units u ON i.UnitId = u.UnitId
            LEFT JOIN Category c ON i.CategoryId = c.CategoryId
            WHERE i.Active = 1
            AND i.ListPrice > 0
            AND i.Description LIKE ?
        """
        params = [limit, f"%{safe_q}%"]
        if safe_vendor:
            query += "    AND v.Name LIKE ?\n"
            params.append(f"%{safe_vendor}%")
        if safe_category:
            if safe_category.isdigit():
                query += "    AND i.CategoryId = ?\n"
                params.append(int(safe_category))
            else:
                query += "    AND c.Name LIKE ?\n"
                params.append(f"%{safe_category}%")
        query += "    ORDER BY i.Description"
        params = tuple(params)
        rows = execute_query(query, params)
        result = [map_row_to_product(row) for row in rows]

        # Cache for 5 minutes
        await cache.set(cache_key, result, CACHE_TTL_SHORT)
        return result

    except Exception as e:
        logger.error("Autocomplete search error: %s", e)
        raise HTTPException(status_code=500, detail="Search failed")


@router.get("/{product_id}", response_model=Product)
async def get_product(product_id: str):
    """Get a single product by ID."""
    try:
        # Validate product_id is numeric (ItemId is an integer)
        if not product_id.isdigit():
            raise HTTPException(status_code=400, detail="Invalid product ID format")

        # Optimized: Get product details with vendor fallback through CrossRefs->Catalog
        query = """
            SELECT
                i.ItemId as id,
                i.ItemCode as item_code,
                i.Description as name,
                ISNULL(i.ShortDescription, ISNULL(i.FullDescription, '')) as description,
                COALESCE(
                    v.Name,
                    (SELECT TOP 1 v2.Name
                     FROM CrossRefs cr
                     JOIN Catalog cat ON cr.CatalogId = cat.CatalogId
                     JOIN Vendors v2 ON cat.VendorId = v2.VendorId
                     WHERE cr.ItemId = i.ItemId AND cr.Active = 1
                     AND cat.VendorId != 7853),  -- Exclude EDS default catalog
                    'Unknown Vendor'
                ) as vendor,
                i.VendorPartNumber as vendor_item_code,
                ISNULL(c.Name, 'General') as category,
                (SELECT TOP 1 cr.ImageURL FROM CrossRefs cr
                 WHERE cr.ItemId = i.ItemId AND cr.ImageURL IS NOT NULL AND cr.ImageURL <> '' AND cr.Active = 1) as image,
                CASE WHEN i.Active = 0 THEN 'discontinued' ELSE 'in-stock' END as status,
                ISNULL(u.Code, 'Each') as unit_of_measure,
                ISNULL(i.ListPrice, 0) as unit_price
            FROM Items i
            LEFT JOIN Vendors v ON i.VendorId = v.VendorId
            LEFT JOIN Units u ON i.UnitId = u.UnitId
            LEFT JOIN Category c ON i.CategoryId = c.CategoryId
            WHERE i.ItemId = ?
        """
        row = execute_single(query, (int(product_id),))

        if not row:
            raise HTTPException(status_code=404, detail="Product not found")

        return map_row_to_product(row)

    except HTTPException:
        raise
    except Exception as e:
        logger.error("Get product error: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve product")


@router.get("/{product_id}/related", response_model=List[Product])
async def get_related_products(
    product_id: str,
    limit: int = Query(default=8, ge=1, le=20)
):
    """
    Get related products (same vendor or category).
    Returns products from the same vendor first, then same category.
    """
    try:
        # Validate product_id
        if not product_id.isdigit():
            return []

        # Get the current product's vendor and category
        product_query = """
            SELECT VendorId, CategoryId FROM Items
            WHERE ItemId = ? AND Active = 1
        """
        product = execute_single(product_query, [int(product_id)])

        if not product:
            return []

        vendor_id = product.get('VendorId')
        category_id = product.get('CategoryId')

        if not vendor_id and not category_id:
            return []

        # Build conditions based on available IDs
        conditions = ["i.ItemId != ?", "i.Active = 1", "i.ListPrice > 0"]
        params = [int(product_id)]

        if vendor_id and category_id:
            conditions.append("(i.VendorId = ? OR i.CategoryId = ?)")
            params.extend([vendor_id, category_id])
            order_clause = f"CASE WHEN i.VendorId = {vendor_id} THEN 0 ELSE 1 END, i.Description"
        elif vendor_id:
            conditions.append("i.VendorId = ?")
            params.append(vendor_id)
            order_clause = "i.Description"
        else:
            conditions.append("i.CategoryId = ?")
            params.append(category_id)
            order_clause = "i.Description"

        # Get related products
        related_query = f"""
            SELECT TOP (?)
                CAST(i.ItemId AS VARCHAR(20)) as id,
                i.Description as name,
                ISNULL(i.ShortDescription, '') as description,
                ISNULL(v.Name, 'Unknown') as vendor,
                ISNULL(i.VendorPartNumber, '') as vendor_item_code,
                ISNULL(c.Name, 'Uncategorized') as category,
                (SELECT TOP 1 cr.ImageURL FROM CrossRefs cr
                 WHERE cr.ItemId = i.ItemId AND cr.ImageURL IS NOT NULL
                 AND cr.ImageURL != '' AND cr.Active = 1) as image,
                CASE WHEN i.Active = 1 THEN 'in-stock' ELSE 'out-of-stock' END as status,
                ISNULL(u.Code, 'Each') as unit_of_measure,
                ISNULL(i.ListPrice, 0) as unit_price
            FROM Items i
            LEFT JOIN Vendors v ON i.VendorId = v.VendorId
            LEFT JOIN Units u ON i.UnitId = u.UnitId
            LEFT JOIN Category c ON i.CategoryId = c.CategoryId
            WHERE {' AND '.join(conditions)}
            ORDER BY {order_clause}
        """

        rows = execute_query(related_query, [limit] + params)
        return [map_row_to_product(row) for row in rows]

    except Exception as e:
        logger.error("Get related products error: %s", e)
        return []


@router.post("/images")
async def get_product_images(product_ids: List[str]) -> dict:
    """
    Batch fetch images for multiple products.
    Returns a dict mapping product_id -> image_url.
    Use this to lazy-load images after fetching the product list.
    """
    try:
        if not product_ids:
            return {}

        # Limit to 50 products per request
        product_ids = product_ids[:50]

        # Validate all IDs are numeric
        valid_ids = [int(pid) for pid in product_ids if pid.isdigit()]
        if not valid_ids:
            return {}

        # Build query with placeholders
        placeholders = ','.join(['?' for _ in valid_ids])
        query = f"""
            SELECT
                cr.ItemId as id,
                cr.ImageURL as image
            FROM CrossRefs cr
            WHERE cr.ItemId IN ({placeholders})
            AND cr.Active = 1
            AND cr.ImageURL IS NOT NULL
            AND cr.ImageURL != ''
        """

        rows = execute_query(query, tuple(valid_ids))

        # Return first image found for each product
        images = {}
        for row in rows:
            item_id = str(row["id"])
            if item_id not in images:
                images[item_id] = row["image"]

        return images

    except Exception as e:
        logger.error("Get product images error: %s", e)
        raise HTTPException(status_code=500, detail="Failed to retrieve images")


# ===========================================
# ELASTICSEARCH HELPERS (transparent fallback)
# ===========================================

def _pick_es_title(src: dict) -> str:
    """Pick the best product title from ES source fields.
    Prefers combinedTypeAheads (clean title-cased names) over raw descriptions."""
    # combinedTypeAheads has clean, title-cased product names
    type_aheads = src.get("combinedTypeAheads", [])
    if isinstance(type_aheads, list) and type_aheads:
        return type_aheads[0]
    # productNames is a fallback (lowercase but still a proper name)
    product_names = src.get("productNames", [])
    if isinstance(product_names, list) and product_names:
        return product_names[0].title()
    # shortDescriptionNative has proper case
    native = src.get("shortDescriptionNative", "")
    if native:
        return native
    # Last resort: shortDescription (may be lowercase)
    short = src.get("shortDescription", "")
    if isinstance(short, list):
        short = short[0] if short else ""
    return short


async def _try_es_search(
    query, category, vendor, min_price, max_price,
    sort_by, sort_order, page, page_size
):
    """Try ES search against existing pricing_consolidated index, return ProductListResponse or None."""
    client = get_es_client()
    if client is None:
        return None

    try:
        filters = []

        if category and category != "All":
            if category.isdigit():
                filters.append({"term": {"categoryId": int(category)}})

        if vendor:
            filters.append({"match": {"vendorName": vendor}})

        price_filter = {}
        if min_price is not None:
            price_filter["gte"] = min_price
        if max_price is not None:
            price_filter["lte"] = max_price
        if price_filter:
            filters.append({"range": {"bidPrice": price_filter}})

        if query and query.strip():
            q = query.strip()
            # For multi-word queries, require all terms to match (AND) to avoid
            # "Dixon pencil" returning everything with just "pencil"
            word_count = len(q.split())
            must_clause = [{
                "multi_match": {
                    "query": q,
                    "fields": [
                        "shortDescription^3", "productNames^2.5",
                        "combinedTypeAheads^2",
                        "itemCode^4", "vendorItemCode^2",
                        "fullDescription",
                    ],
                    "type": "best_fields",
                    "operator": "and" if word_count > 1 else "or",
                    "fuzziness": "AUTO" if word_count == 1 else "0",
                    "prefix_length": 2,
                }
            }]
            # Boost exact/phrase matches for better relevance ordering
            should_clause = [
                {"match_phrase": {"shortDescription": {"query": q, "boost": 10}}},
                {"match_phrase": {"productNames": {"query": q, "boost": 8}}},
                {"match_phrase": {"combinedTypeAheads": {"query": q, "boost": 8}}},
            ]
            # For single-word queries that look like item codes, boost prefix match
            if word_count == 1:
                should_clause.append({"prefix": {"itemCode": {"value": q.lower(), "boost": 15}}})
        else:
            must_clause = [{"match_all": {}}]
            should_clause = []

        bool_query = {"must": must_clause}
        if should_clause:
            bool_query["should"] = should_clause
        if filters:
            bool_query["filter"] = filters

        body = {
            "query": {"bool": bool_query},
            "from": (page - 1) * page_size,
            "size": page_size,
            # Collapse by itemId to deduplicate the same product across bids
            "collapse": {"field": "itemId"},
            # Get accurate unique product count after collapse
            "aggs": {"unique_products": {"cardinality": {"field": "itemId"}}},
        }

        # Sort
        direction = "desc" if sort_order and sort_order.lower() == "desc" else "asc"
        if sort_by == "price":
            body["sort"] = [{"bidPrice": {"order": direction, "missing": "_last"}}]
        elif sort_by == "name":
            body["sort"] = [{"sortSeq.keyword": {"order": direction}}]
        else:
            body["sort"] = [{"_score": {"order": "desc"}}, {"orderCounts": {"order": "desc", "missing": "_last"}}]

        result = await client.search(index=ES_INDEX, body=body)
        hits = result.get("hits", {})
        # Use cardinality aggregation for accurate unique count after collapse
        aggs = result.get("aggregations", {})
        total = aggs.get("unique_products", {}).get("value", hits.get("total", {}).get("value", 0))
        total_pages = max(1, (total + page_size - 1) // page_size)

        products = []
        for hit in hits.get("hits", []):
            src = hit["_source"]
            # Product name: prefer combinedTypeAheads (clean title-cased name),
            # fall back to shortDescriptionNative (proper case), then shortDescription
            title = _pick_es_title(src)
            desc = src.get("shortDescriptionNative") or ""
            if not desc:
                desc = src.get("shortDescription") or src.get("fullDescriptionNative", "")
                if isinstance(desc, list):
                    desc = desc[0] if desc else ""
            # Truncate description to keep cards clean
            desc = desc[:120].rstrip() + ("..." if len(desc) > 120 else "")
            item_code = src.get("itemCode", "")
            if isinstance(item_code, list):
                item_code = item_code[0] if item_code else ""
            vendor_code = src.get("vendorItemCode") or src.get("vendorItemCodeNative", "")
            if isinstance(vendor_code, list):
                vendor_code = vendor_code[0] if vendor_code else ""
            vendor_name = src.get("vendorName") or src.get("vendorNameNative", "Unknown Vendor")
            uom = (src.get("unitCode") or "Each").strip()
            price = float(src.get("bidPrice", 0) or src.get("catalogPrice", 0) or 0)
            image = src.get("thumbnailURL") or src.get("imageURL")

            products.append(Product(
                id=str(src.get("itemId") or src.get("pricingConsolidatedId", hit["_id"])),
                name=clean_string(title),
                description=clean_string(desc),
                vendor=clean_string(vendor_name),
                vendor_item_code=vendor_code or item_code,
                category=str(src.get("categoryId", "General")),
                image=image,
                status="in-stock",
                unit_of_measure=uom,
                unit_price=price,
                tags=[],
            ))

        # Post-query dedup: same product can have different itemIds across catalogs.
        # Keep the lowest-priced entry per name+vendor_item_code combo.
        seen = {}
        deduped = []
        for p in products:
            key = (p.name.lower().strip(), p.vendor_item_code.lower().strip()) if p.vendor_item_code else (p.name.lower().strip(), p.vendor.lower().strip())
            if key not in seen:
                seen[key] = p
                deduped.append(p)
            elif p.unit_price > 0 and (seen[key].unit_price == 0 or p.unit_price < seen[key].unit_price):
                idx = deduped.index(seen[key])
                deduped[idx] = p
                seen[key] = p
        products = deduped

        return ProductListResponse(
            products=products,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
        )

    except Exception as e:
        logger.warning("ES search failed, falling back to SQL: %s", e)
        return None


async def _try_es_autocomplete(q: str, limit: int, vendor_filter: str = None, category_filter: str = None):
    """Try ES autocomplete against existing pricing_consolidated index, return list of Products or None."""
    client = get_es_client()
    if client is None:
        return None

    try:
        must_clauses = [{
            "multi_match": {
                "query": q,
                "fields": [
                    "combinedTypeAheads.suggestion^3",
                    "combinedTypeAheads.suggestion._2gram^2",
                    "shortDescription^2",
                    "itemCode^4",
                    "vendorName",
                    "productNames^2",
                ],
                "type": "best_fields",
            }
        }]
        if vendor_filter:
            must_clauses.append({"match_phrase": {"vendorName": vendor_filter}})
        if category_filter:
            if category_filter.isdigit():
                must_clauses.append({"term": {"categoryId": int(category_filter)}})
            else:
                must_clauses.append({"match_phrase": {"categoryName": category_filter}})

        body = {
            "size": limit * 3,  # fetch extra for dedup
            "_source": [
                "itemId", "pricingConsolidatedId",
                "combinedTypeAheads", "productNames",
                "shortDescription", "shortDescriptionNative",
                "vendorName", "vendorNameNative",
                "vendorItemCode", "vendorItemCodeNative",
                "itemCode", "categoryId",
                "thumbnailURL", "imageURL",
                "unitCode", "bidPrice", "catalogPrice",
            ],
            "query": {
                "bool": {
                    "must": must_clauses,
                    "should": [
                        # Boost products where the query matches as a whole word in the name
                        {"match_phrase": {"shortDescription": {"query": q, "boost": 10}}},
                        {"match_phrase": {"productNames": {"query": q, "boost": 8}}},
                        # Boost exact item code prefix matches
                        {"prefix": {"itemCode": {"value": q.lower(), "boost": 15}}},
                    ],
                }
            },
        }

        result = await client.search(index=ES_INDEX, body=body)

        products = []
        for hit in result.get("hits", {}).get("hits", []):
            src = hit["_source"]
            title = _pick_es_title(src)
            vendor_name = src.get("vendorName") or src.get("vendorNameNative", "Unknown Vendor")
            vendor_code = src.get("vendorItemCode") or src.get("vendorItemCodeNative", "")
            if isinstance(vendor_code, list):
                vendor_code = vendor_code[0] if vendor_code else ""
            item_code = src.get("itemCode", "")
            if isinstance(item_code, list):
                item_code = item_code[0] if item_code else ""
            uom = (src.get("unitCode") or "Each").strip()
            price = float(src.get("bidPrice", 0) or src.get("catalogPrice", 0) or 0)
            image = src.get("thumbnailURL") or src.get("imageURL")

            products.append(Product(
                id=str(src.get("itemId") or src.get("pricingConsolidatedId", hit["_id"])),
                name=clean_string(title),
                description="",
                vendor=clean_string(vendor_name),
                vendor_item_code=vendor_code or item_code,
                category=str(src.get("categoryId", "General")),
                image=image,
                status="in-stock",
                unit_of_measure=uom,
                unit_price=price,
                tags=[],
            ))

        # Deduplicate by name+vendor (same product in different bids), keep highest-scored hit
        seen = set()
        deduped = []
        for p in products:
            dedup_key = (p.name.lower().strip(), p.vendor.lower().strip())
            if dedup_key not in seen:
                seen.add(dedup_key)
                deduped.append(p)
                if len(deduped) >= limit:
                    break

        return deduped

    except Exception as e:
        logger.warning("ES autocomplete failed, falling back to SQL: %s", e)
        return None
