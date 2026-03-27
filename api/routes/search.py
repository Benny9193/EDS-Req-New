"""
Elasticsearch-powered product search endpoints.

Queries the existing EDS-ES pricing_consolidated index which contains
denormalized product+bid+pricing data. Falls back to SQL when ES
is unavailable.

Field mapping (existing ES index -> our API):
  shortDescription[0] -> name
  fullDescription     -> description
  vendorName          -> vendor
  vendorItemCode[0]   -> vendor_item_code
  itemCode[0]         -> item_code
  bidPrice            -> unit_price (when bid filtered)
  catalogPrice        -> unit_price (fallback)
  bidHeaderId         -> bid filter field
  imageURL            -> image
  thumbnailURL        -> image (fallback)
  unitCode            -> unit_of_measure
  categoryId          -> category (numeric)
"""

import logging
from typing import Optional, List

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from ..search import get_es_client, ES_INDEX, ES_ENABLED
from ..models import Product, ProductListResponse

router = APIRouter(prefix="/search", tags=["Search"])
logger = logging.getLogger(__name__)


# ===========================================
# RESPONSE MODELS
# ===========================================

class SearchFacets(BaseModel):
    """Aggregation facets returned with search results."""
    categories: List[dict] = Field(default_factory=list)
    vendors: List[dict] = Field(default_factory=list)
    price_range: dict = Field(default_factory=dict)


class SearchResponse(BaseModel):
    """Extended search response with facets and ES metadata."""
    products: List[Product]
    total: int
    page: int
    page_size: int
    total_pages: int
    facets: Optional[SearchFacets] = None
    source: str = "elasticsearch"  # "elasticsearch" or "sql_fallback"


class AutocompleteItem(BaseModel):
    """Lightweight autocomplete suggestion."""
    id: str
    name: str
    vendor: str = ""
    category: str = "General"
    unit_price: float = 0.0
    image: Optional[str] = None


# ===========================================
# FIELD MAPPING — existing ES index fields
# ===========================================
# The pricing_consolidated_60 index uses camelCase fields from the
# existing EDSIQ ColdFusion indexer. Map them to our API Product model.

def _hit_to_product(src: dict, bid_id_list: List[int] = None) -> Product:
    """Convert an ES hit _source to our Product model."""
    # Name: shortDescription is an array, take first element
    short_desc = src.get("shortDescription") or src.get("shortDescriptionNative", "")
    if isinstance(short_desc, list):
        short_desc = short_desc[0] if short_desc else ""

    # Full description
    full_desc = src.get("fullDescription") or src.get("fullDescriptionNative", "")
    if isinstance(full_desc, list):
        full_desc = full_desc[0] if full_desc else ""

    # Item code
    item_code = src.get("itemCode", "")
    if isinstance(item_code, list):
        item_code = item_code[0] if item_code else ""

    # Vendor item code
    vendor_item_code = src.get("vendorItemCode") or src.get("vendorItemCodeNative", "")
    if isinstance(vendor_item_code, list):
        vendor_item_code = vendor_item_code[0] if vendor_item_code else ""

    # Price: prefer bidPrice when filtering by bid, otherwise catalogPrice
    unit_price = 0.0
    if bid_id_list:
        unit_price = float(src.get("bidPrice", 0) or 0)
    if not unit_price:
        unit_price = float(src.get("catalogPrice", 0) or src.get("bidPrice", 0) or 0)

    # Image
    image = src.get("thumbnailURL") or src.get("imageURL")

    # Vendor name
    vendor_name = src.get("vendorName") or src.get("vendorNameNative", "Unknown Vendor")

    # Unit of measure
    uom = (src.get("unitCode") or "Each").strip()

    return Product(
        id=str(src.get("itemId") or src.get("pricingConsolidatedId", "")),
        name=short_desc,
        description=full_desc,
        vendor=vendor_name,
        vendor_item_code=vendor_item_code,
        category=str(src.get("categoryId", "General")),
        image=image,
        status="in-stock",
        unit_of_measure=uom,
        unit_price=unit_price,
    )


# ===========================================
# SEARCH ENDPOINT
# ===========================================

@router.get("", response_model=SearchResponse)
async def search_products(
    q: Optional[str] = Query(None, max_length=200, description="Search query"),
    query: Optional[str] = Query(None, max_length=200, description="Search query (alias for q)"),
    bid_ids: Optional[str] = Query(None, description="Comma-separated bid header IDs to filter by"),
    category: Optional[str] = Query(None, max_length=100, description="Filter by category ID"),
    vendor: Optional[str] = Query(None, max_length=100, description="Filter by vendor name"),
    min_price: Optional[float] = Query(None, ge=0, description="Minimum price"),
    max_price: Optional[float] = Query(None, ge=0, description="Maximum price"),
    sort_by: Optional[str] = Query("relevance", description="Sort: relevance, price, name"),
    sort_order: Optional[str] = Query("asc", description="Sort direction: asc, desc"),
    page: int = Query(1, ge=1, le=10000, description="Page number"),
    page_size: int = Query(20, ge=1, le=100, description="Items per page"),
    include_facets: bool = Query(False, description="Include category/vendor/price facets"),
):
    """
    Search products using Elasticsearch with optional bid filtering.

    - **q**: Full-text search across name, description, item code, vendor
    - **bid_ids**: Filter to products in specific bid headers (comma-separated BidHeaderIds)
    - **category/vendor**: Additional filters
    - **include_facets**: Return aggregation counts for filters
    """
    search_term = q or query

    client = get_es_client()
    if client is None:
        raise HTTPException(
            status_code=503,
            detail="Search service unavailable. Set ES_ENABLED=true to enable."
        )

    try:
        # Parse bid_ids
        bid_id_list = []
        if bid_ids:
            bid_id_list = [int(b.strip()) for b in bid_ids.split(",") if b.strip().isdigit()]

        body = _build_search_query(
            q=search_term,
            bid_id_list=bid_id_list,
            category=category,
            vendor=vendor,
            min_price=min_price,
            max_price=max_price,
            sort_by=sort_by,
            sort_order=sort_order,
            page=page,
            page_size=page_size,
            include_facets=include_facets,
        )

        result = await client.search(index=ES_INDEX, body=body)

        hits = result.get("hits", {})
        total = hits.get("total", {}).get("value", 0)
        total_pages = max(1, (total + page_size - 1) // page_size)

        products = [
            _hit_to_product(hit["_source"], bid_id_list)
            for hit in hits.get("hits", [])
        ]

        facets = None
        if include_facets and "aggregations" in result:
            facets = _parse_facets(result["aggregations"])

        return SearchResponse(
            products=products,
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
            facets=facets,
            source="elasticsearch",
        )

    except Exception as e:
        logger.error(f"ES search error: {e}")
        raise HTTPException(status_code=500, detail=f"Search failed: {str(e)}")


# ===========================================
# AUTOCOMPLETE
# ===========================================

@router.get("/autocomplete", response_model=List[AutocompleteItem])
async def autocomplete(
    q: str = Query(..., min_length=2, max_length=100, description="Search prefix"),
    bid_ids: Optional[str] = Query(None, description="Comma-separated bid header IDs"),
    limit: int = Query(10, ge=1, le=20, description="Max suggestions"),
):
    """
    Fast autocomplete suggestions using the existing ES index's
    combinedTypeAheads.suggestion field (search_as_you_type).
    Falls back to multi_match on product name fields.
    """
    client = get_es_client()
    if client is None:
        raise HTTPException(status_code=503, detail="Search service unavailable")

    try:
        bid_id_list = []
        if bid_ids:
            bid_id_list = [int(b.strip()) for b in bid_ids.split(",") if b.strip().isdigit()]

        # Use the search_as_you_type field + standard multi_match
        must = {
            "multi_match": {
                "query": q,
                "fields": [
                    "combinedTypeAheads.suggestion^3",
                    "combinedTypeAheads.suggestion._2gram^2",
                    "combinedTypeAheads.suggestion._3gram",
                    "shortDescription^2",
                    "itemCode^4",
                    "vendorName",
                    "productNames^2",
                ],
                "type": "best_fields",
            }
        }

        filters = []
        if bid_id_list:
            filters.append({"terms": {"bidHeaderId": bid_id_list}})

        bool_query = {"must": [must]}
        if filters:
            bool_query["filter"] = filters

        body = {
            "size": limit,
            "_source": [
                "itemId", "pricingConsolidatedId",
                "shortDescription", "shortDescriptionNative",
                "vendorName", "vendorNameNative",
                "categoryId", "bidPrice", "catalogPrice",
                "thumbnailURL", "imageURL",
            ],
            "query": {"bool": bool_query},
        }

        result = await client.search(index=ES_INDEX, body=body)

        items = []
        for hit in result.get("hits", {}).get("hits", []):
            src = hit["_source"]
            name = src.get("shortDescription") or src.get("shortDescriptionNative", "")
            if isinstance(name, list):
                name = name[0] if name else ""
            vendor = src.get("vendorName") or src.get("vendorNameNative", "")
            price = float(src.get("bidPrice", 0) or src.get("catalogPrice", 0) or 0)
            image = src.get("thumbnailURL") or src.get("imageURL")

            items.append(AutocompleteItem(
                id=str(src.get("itemId") or src.get("pricingConsolidatedId", hit["_id"])),
                name=name,
                vendor=vendor,
                category=str(src.get("categoryId", "General")),
                unit_price=price,
                image=image,
            ))
        return items

    except Exception as e:
        logger.error(f"ES autocomplete error: {e}")
        raise HTTPException(status_code=500, detail="Autocomplete failed")


# ===========================================
# QUERY BUILDER
# ===========================================

def _build_search_query(
    q: Optional[str],
    bid_id_list: List[int],
    category: Optional[str],
    vendor: Optional[str],
    min_price: Optional[float],
    max_price: Optional[float],
    sort_by: str,
    sort_order: str,
    page: int,
    page_size: int,
    include_facets: bool,
) -> dict:
    """Build the Elasticsearch query DSL for the pricing_consolidated index."""

    filters = []

    # Bid filtering — bidHeaderId is a long field in the existing index
    if bid_id_list:
        filters.append({"terms": {"bidHeaderId": bid_id_list}})

    # Category filter (categoryId is numeric in existing index)
    if category:
        if category.isdigit():
            filters.append({"term": {"categoryId": int(category)}})

    # Vendor filter — match against vendorName text field
    if vendor:
        filters.append({"match": {"vendorName": vendor}})

    # Price range — use bidPrice (the contract price)
    price_filter = {}
    if min_price is not None:
        price_filter["gte"] = min_price
    if max_price is not None:
        price_filter["lte"] = max_price
    if price_filter:
        filters.append({"range": {"bidPrice": price_filter}})

    # Build the bool query
    bool_query = {}
    if filters:
        bool_query["filter"] = filters

    if q and q.strip():
        bool_query["must"] = [
            {
                "multi_match": {
                    "query": q.strip(),
                    "fields": [
                        "shortDescription^3",
                        "productNames^2.5",
                        "allStringFields",
                        "fullDescription",
                        "itemCode^4",
                        "vendorName^1.5",
                        "vendorItemCode^2",
                        "manufacturer^1.5",
                        "manufacturerPartNumber^2",
                        "keywords^2",
                        "headings",
                    ],
                    "type": "best_fields",
                    "fuzziness": "AUTO",
                    "prefix_length": 2,
                }
            }
        ]
    else:
        bool_query["must"] = [{"match_all": {}}]

    # Sort
    sort_clause = []
    direction = "desc" if sort_order and sort_order.lower() == "desc" else "asc"

    if sort_by == "price":
        sort_clause.append({"bidPrice": {"order": direction, "missing": "_last"}})
    elif sort_by == "name":
        sort_clause.append({"sortSeq.keyword": {"order": direction}})
    else:
        # Relevance — _score desc, then by order popularity
        if q and q.strip():
            sort_clause.append({"_score": {"order": "desc"}})
        sort_clause.append({"orderCounts": {"order": "desc", "missing": "_last"}})

    # Pagination
    from_offset = (page - 1) * page_size

    body = {
        "query": {"bool": bool_query},
        "sort": sort_clause,
        "from": from_offset,
        "size": page_size,
        "_source": [
            "itemId", "pricingConsolidatedId", "crossRefId", "catalogId",
            "bidHeaderId", "bidPrice", "catalogPrice",
            "itemCode", "vendorItemCode", "vendorItemCodeNative",
            "shortDescription", "shortDescriptionNative",
            "fullDescription", "fullDescriptionNative",
            "vendorId", "vendorName", "vendorNameNative",
            "categoryId", "unitCode",
            "imageURL", "thumbnailURL",
            "manufacturer", "manufacturerNative",
            "manufacturerPartNumber", "manufacturerPartNumberNative",
            "orderCounts",
        ],
    }

    # Aggregations for facets
    if include_facets:
        body["aggs"] = {
            "categories": {
                "terms": {"field": "categoryId", "size": 50}
            },
            "vendors": {
                "terms": {"field": "vendorNameNative.keyword", "size": 50}
            },
            "price_stats": {
                "stats": {"field": "bidPrice"}
            },
        }

    return body


def _parse_facets(aggs: dict) -> SearchFacets:
    """Parse ES aggregation results into facet response."""
    categories = []
    if "categories" in aggs:
        categories = [
            {"name": str(b["key"]), "count": b["doc_count"]}
            for b in aggs["categories"].get("buckets", [])
        ]

    vendors = []
    if "vendors" in aggs:
        vendors = [
            {"name": b["key"], "count": b["doc_count"]}
            for b in aggs["vendors"].get("buckets", [])
        ]

    price_range = {}
    if "price_stats" in aggs:
        stats = aggs["price_stats"]
        price_range = {
            "min": stats.get("min", 0),
            "max": stats.get("max", 0),
            "avg": stats.get("avg", 0),
        }

    return SearchFacets(
        categories=categories,
        vendors=vendors,
        price_range=price_range,
    )
