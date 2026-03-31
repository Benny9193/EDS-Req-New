"""
Elasticsearch integration for product search.

Provides a denormalized product index with bid/price plan associations,
enabling fast full-text search filtered by eligible bid IDs.

Index schema: Each document represents one product with nested bid_prices
containing per-bid pricing from CrossRefs.
"""

import os
import logging
from typing import Optional

from elasticsearch import AsyncElasticsearch

logger = logging.getLogger(__name__)

# Configuration from environment
# Default to the existing EDS-ES Azure VM (20.122.81.233)
ES_URL = os.getenv("ES_URL", "http://20.122.81.233:9200")
ES_ENABLED = os.getenv("ES_ENABLED", "true").lower() in ("true", "1", "yes")
ES_INDEX = os.getenv("ES_INDEX", "pricing_consolidated_active")

# Singleton client
_es_client: Optional[AsyncElasticsearch] = None


def get_es_client() -> Optional[AsyncElasticsearch]:
    """Get or create the async Elasticsearch client. Returns None if ES is disabled."""
    global _es_client
    if not ES_ENABLED:
        return None
    if _es_client is None:
        _es_client = AsyncElasticsearch(
            ES_URL,
            request_timeout=10,
            max_retries=2,
            retry_on_timeout=True,
        )
    return _es_client


async def close_es_client():
    """Close the ES client on app shutdown."""
    global _es_client
    if _es_client is not None:
        await _es_client.close()
        _es_client = None


async def es_healthy() -> bool:
    """Check if Elasticsearch is reachable."""
    client = get_es_client()
    if client is None:
        return False
    try:
        info = await client.info()
        return True
    except Exception as e:
        logger.warning(f"Elasticsearch health check failed: {e}")
        return False


# ===========================================
# INDEX MAPPING
# ===========================================

PRODUCT_INDEX_SETTINGS = {
    "settings": {
        "number_of_shards": 1,
        "number_of_replicas": 0,
        "analysis": {
            "analyzer": {
                "product_analyzer": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "asciifolding", "product_synonyms"]
                },
                "autocomplete_analyzer": {
                    "type": "custom",
                    "tokenizer": "autocomplete_tokenizer",
                    "filter": ["lowercase", "asciifolding"]
                },
                "autocomplete_search": {
                    "type": "custom",
                    "tokenizer": "standard",
                    "filter": ["lowercase", "asciifolding"]
                },
                "item_code_analyzer": {
                    "type": "custom",
                    "tokenizer": "keyword",
                    "filter": ["lowercase"]
                }
            },
            "tokenizer": {
                "autocomplete_tokenizer": {
                    "type": "edge_ngram",
                    "min_gram": 2,
                    "max_gram": 15,
                    "token_chars": ["letter", "digit"]
                }
            },
            "filter": {
                "product_synonyms": {
                    "type": "synonym",
                    "lenient": True,
                    "synonyms": [
                        "pencil,pencils",
                        "pen,pens",
                        "marker,markers",
                        "eraser,erasers",
                        "notebook,notebooks",
                        "folder,folders",
                        "binder,binders",
                        "paper,papers",
                        "crayon,crayons",
                        "scissors,shears",
                        "glue,adhesive",
                        "tape,adhesive tape",
                        "stapler,staple",
                        "calc,calculator",
                        "headset,headphone,headphones",
                    ]
                }
            }
        },
        "index": {
            "max_result_window": 50000
        }
    },
    "mappings": {
        "properties": {
            # Core product fields
            "item_id": {"type": "integer"},
            "item_code": {
                "type": "text",
                "analyzer": "item_code_analyzer",
                "fields": {
                    "raw": {"type": "keyword"}
                }
            },
            "name": {
                "type": "text",
                "analyzer": "product_analyzer",
                "fields": {
                    "autocomplete": {
                        "type": "text",
                        "analyzer": "autocomplete_analyzer",
                        "search_analyzer": "autocomplete_search"
                    },
                    "raw": {"type": "keyword"},
                    "sort": {"type": "keyword", "normalizer": "lowercase"}
                }
            },
            "description": {
                "type": "text",
                "analyzer": "product_analyzer"
            },
            "short_description": {
                "type": "text",
                "analyzer": "product_analyzer"
            },

            # Vendor info (from Items.VendorId -> Vendors)
            "vendor_id": {"type": "integer"},
            "vendor_name": {
                "type": "text",
                "fields": {
                    "raw": {"type": "keyword"},
                    "autocomplete": {
                        "type": "text",
                        "analyzer": "autocomplete_analyzer",
                        "search_analyzer": "autocomplete_search"
                    }
                }
            },
            "vendor_part_number": {"type": "keyword"},

            # Category
            "category_id": {"type": "integer"},
            "category_name": {
                "type": "keyword",
                "fields": {
                    "text": {"type": "text"}
                }
            },

            # Default pricing and unit
            "list_price": {"type": "float"},
            "unit_of_measure": {"type": "keyword"},
            "active": {"type": "boolean"},

            # Image URL (first active from CrossRefs)
            "image_url": {"type": "keyword", "index": False},

            # ===========================================
            # BID/PRICE PLAN ASSOCIATIONS
            # ===========================================
            # Nested array of bids this product is eligible for.
            # Each entry has the CatalogId (bid_id) and the
            # bid-specific price from CrossRefs.CatalogPrice.
            # This enables filtering: "show only products in bids [1,2,3]"
            # and sorting by bid-specific price.
            "bid_prices": {
                "type": "nested",
                "properties": {
                    "bid_id": {"type": "integer"},
                    "catalog_price": {"type": "float"},
                    "vendor_id": {"type": "integer"},
                }
            },
            # Flat list of bid IDs for fast terms filtering
            # (avoids nested query cost for simple eligibility checks)
            "bid_ids": {"type": "integer"},

            # Timestamp for incremental re-indexing
            "indexed_at": {"type": "date"}
        }
    }
}


async def ensure_index():
    """Create the product index if it doesn't exist."""
    client = get_es_client()
    if client is None:
        return
    try:
        exists = await client.indices.exists(index=ES_INDEX)
        if not exists:
            await client.indices.create(index=ES_INDEX, body=PRODUCT_INDEX_SETTINGS)
            logger.info(f"Created Elasticsearch index: {ES_INDEX}")
        else:
            logger.info(f"Elasticsearch index already exists: {ES_INDEX}")
    except Exception as e:
        logger.error(f"Failed to create ES index: {e}")


async def recreate_index():
    """Drop and recreate the product index (for full reindex)."""
    client = get_es_client()
    if client is None:
        return
    try:
        exists = await client.indices.exists(index=ES_INDEX)
        if exists:
            await client.indices.delete(index=ES_INDEX)
            logger.info(f"Deleted existing index: {ES_INDEX}")
        await client.indices.create(index=ES_INDEX, body=PRODUCT_INDEX_SETTINGS)
        logger.info(f"Recreated Elasticsearch index: {ES_INDEX}")
    except Exception as e:
        logger.error(f"Failed to recreate ES index: {e}")
