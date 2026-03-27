"""
Elasticsearch Product Indexer.

Reads products from SQL Server (Items + CrossRefs + Vendors + Categories)
and indexes denormalized documents into Elasticsearch with bid/price
plan associations for fast filtered search.

Usage:
    python -m scripts.index_elasticsearch              # Full reindex
    python -m scripts.index_elasticsearch --incremental # Only changed items
    python -m scripts.index_elasticsearch --batch-size 5000
"""

import os
import sys
import time
import argparse
import logging
from datetime import datetime, timezone
from typing import List, Dict, Any

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pyodbc
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk, BulkIndexError

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)

# ===========================================
# CONFIGURATION
# ===========================================

ES_URL = os.getenv("ES_URL", "http://localhost:9200")
ES_INDEX = "eds_products"

DB_SERVER = os.getenv("DB_SERVER", "eds-sqlserver.eastus2.cloudapp.azure.com")
DB_DATABASE = os.getenv("DB_DATABASE_CATALOG", os.getenv("DB_DATABASE", "EDS"))
DB_USERNAME = os.getenv("DB_USERNAME", "EDSAdmin")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_DRIVER = os.getenv("DB_DRIVER", "ODBC Driver 18 for SQL Server")

DEFAULT_BATCH_SIZE = 5000


def get_db_connection():
    """Create a direct pyodbc connection for batch reading."""
    conn_str = (
        f"DRIVER={{{DB_DRIVER}}};"
        f"SERVER={DB_SERVER};"
        f"DATABASE={DB_DATABASE};"
        f"UID={DB_USERNAME};"
        f"PWD={DB_PASSWORD};"
        f"TrustServerCertificate=yes;"
        f"Connection Timeout=30;"
    )
    return pyodbc.connect(conn_str)


def get_es_client():
    """Create a synchronous Elasticsearch client for indexing."""
    return Elasticsearch(ES_URL, request_timeout=30)


# ===========================================
# INDEX MANAGEMENT
# ===========================================

# Import settings from the api module
from api.search import PRODUCT_INDEX_SETTINGS


def recreate_index(es: Elasticsearch):
    """Drop and recreate the product index."""
    if es.indices.exists(index=ES_INDEX):
        es.indices.delete(index=ES_INDEX)
        logger.info(f"Deleted existing index: {ES_INDEX}")

    es.indices.create(index=ES_INDEX, body=PRODUCT_INDEX_SETTINGS)
    logger.info(f"Created index: {ES_INDEX}")


# ===========================================
# DATA EXTRACTION
# ===========================================

PRODUCTS_QUERY = """
SELECT
    i.ItemId,
    i.ItemCode,
    i.Description,
    ISNULL(i.ShortDescription, '') as ShortDescription,
    i.VendorId,
    ISNULL(v.Name, '') as VendorName,
    i.VendorPartNumber,
    i.CategoryId,
    ISNULL(c.Name, 'General') as CategoryName,
    ISNULL(i.ListPrice, 0) as ListPrice,
    ISNULL(u.Code, 'Each') as UnitOfMeasure,
    i.Active
FROM Items i
LEFT JOIN Vendors v ON i.VendorId = v.VendorId
LEFT JOIN Units u ON i.UnitId = u.UnitId
LEFT JOIN Category c ON i.CategoryId = c.CategoryId
WHERE i.Description IS NOT NULL
  AND i.Description != ''
  AND i.Active = 1
  AND i.ListPrice > 0
ORDER BY i.ItemId
OFFSET ? ROWS FETCH NEXT ? ROWS ONLY
"""

BID_PRICES_QUERY = """
SELECT
    cr.ItemId,
    cr.CatalogId as BidId,
    ISNULL(cr.CatalogPrice, 0) as CatalogPrice,
    cat.VendorId as BidVendorId
FROM CrossRefs cr
JOIN Catalog cat ON cr.CatalogId = cat.CatalogId
WHERE cr.Active = 1
  AND cat.Active = 1
  AND ISNULL(cat.VendorId, 0) != 7853
  AND cr.ItemId IN ({placeholders})
"""

IMAGE_QUERY = """
SELECT cr.ItemId, cr.ImageURL
FROM CrossRefs cr
WHERE cr.ItemId IN ({placeholders})
  AND cr.Active = 1
  AND cr.ImageURL IS NOT NULL
  AND cr.ImageURL != ''
"""


def fetch_products_batch(conn, offset: int, batch_size: int) -> List[Dict]:
    """Fetch a batch of products from SQL Server."""
    cursor = conn.cursor()
    cursor.execute(PRODUCTS_QUERY, (offset, batch_size))
    columns = [desc[0] for desc in cursor.description]
    rows = []
    for row in cursor.fetchall():
        rows.append(dict(zip(columns, row)))
    cursor.close()
    return rows


def fetch_bid_prices(conn, item_ids: List[int]) -> Dict[int, List[Dict]]:
    """Fetch bid/price plan associations for a batch of items."""
    if not item_ids:
        return {}

    placeholders = ",".join(["?" for _ in item_ids])
    query = BID_PRICES_QUERY.format(placeholders=placeholders)

    cursor = conn.cursor()
    cursor.execute(query, item_ids)

    result: Dict[int, List[Dict]] = {}
    for row in cursor.fetchall():
        item_id = row[0]
        if item_id not in result:
            result[item_id] = []
        result[item_id].append({
            "bid_id": row[1],
            "catalog_price": float(row[2]) if row[2] else 0.0,
            "vendor_id": row[3],
        })
    cursor.close()
    return result


def fetch_images(conn, item_ids: List[int]) -> Dict[int, str]:
    """Fetch first image URL for a batch of items."""
    if not item_ids:
        return {}

    placeholders = ",".join(["?" for _ in item_ids])
    query = IMAGE_QUERY.format(placeholders=placeholders)

    cursor = conn.cursor()
    cursor.execute(query, item_ids)

    result: Dict[int, str] = {}
    for row in cursor.fetchall():
        item_id = row[0]
        if item_id not in result:  # First image wins
            result[item_id] = row[1]
    cursor.close()
    return result


# ===========================================
# DOCUMENT BUILDER
# ===========================================

def build_es_document(product: Dict, bid_prices: List[Dict], image_url: str = None) -> Dict[str, Any]:
    """Build a denormalized ES document from product + bid data."""
    now = datetime.now(timezone.utc).isoformat()

    doc = {
        "_index": ES_INDEX,
        "_id": str(product["ItemId"]),
        "_source": {
            "item_id": product["ItemId"],
            "item_code": (product.get("ItemCode") or "").strip(),
            "name": (product.get("Description") or "").strip(),
            "description": (product.get("Description") or "").strip(),
            "short_description": (product.get("ShortDescription") or "").strip(),
            "vendor_id": product.get("VendorId"),
            "vendor_name": (product.get("VendorName") or "").strip(),
            "vendor_part_number": (product.get("VendorPartNumber") or "").strip() or None,
            "category_id": product.get("CategoryId"),
            "category_name": (product.get("CategoryName") or "General").strip(),
            "list_price": float(product.get("ListPrice") or 0),
            "unit_of_measure": (product.get("UnitOfMeasure") or "Each").strip(),
            "active": bool(product.get("Active", True)),
            "image_url": image_url,
            "bid_prices": bid_prices,
            "bid_ids": list(set(bp["bid_id"] for bp in bid_prices)),
            "indexed_at": now,
        }
    }
    return doc


# ===========================================
# INDEXING PIPELINE
# ===========================================

def index_products(es: Elasticsearch, conn, batch_size: int = DEFAULT_BATCH_SIZE):
    """Full reindex: stream all products from SQL Server into ES."""
    offset = 0
    total_indexed = 0
    total_errors = 0
    start_time = time.time()

    logger.info(f"Starting full product index (batch_size={batch_size})...")

    while True:
        # 1. Fetch product batch
        products = fetch_products_batch(conn, offset, batch_size)
        if not products:
            break

        item_ids = [p["ItemId"] for p in products]
        batch_start = time.time()

        # 2. Fetch bid prices and images for this batch
        bid_prices_map = fetch_bid_prices(conn, item_ids)
        images_map = fetch_images(conn, item_ids)

        # 3. Build ES documents
        actions = []
        for product in products:
            item_id = product["ItemId"]
            bid_prices = bid_prices_map.get(item_id, [])
            image_url = images_map.get(item_id)
            actions.append(build_es_document(product, bid_prices, image_url))

        # 4. Bulk index
        try:
            success, errors = bulk(es, actions, raise_on_error=False, stats_only=False)
            if isinstance(errors, list):
                total_errors += len(errors)
                if errors:
                    logger.warning(f"  Batch errors: {len(errors)} (first: {errors[0]})")
            total_indexed += success if isinstance(success, int) else len(products)
        except BulkIndexError as e:
            total_errors += len(e.errors)
            logger.error(f"  Bulk index error: {len(e.errors)} failures")

        batch_time = time.time() - batch_start
        logger.info(
            f"  Batch {offset // batch_size + 1}: "
            f"{len(products)} products, "
            f"{sum(len(v) for v in bid_prices_map.values())} bid prices, "
            f"{len(images_map)} images | "
            f"{batch_time:.1f}s"
        )

        offset += batch_size

        # If we got fewer than batch_size, we're done
        if len(products) < batch_size:
            break

    elapsed = time.time() - start_time
    logger.info(
        f"Indexing complete: {total_indexed} products indexed, "
        f"{total_errors} errors, {elapsed:.1f}s total"
    )

    # Refresh index to make all documents searchable
    es.indices.refresh(index=ES_INDEX)
    logger.info("Index refreshed.")

    return total_indexed, total_errors


# ===========================================
# COUNT QUERY (for progress reporting)
# ===========================================

def count_products(conn) -> int:
    """Count total eligible products."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT COUNT(*) FROM Items
        WHERE Description IS NOT NULL AND Description != ''
        AND Active = 1 AND ListPrice > 0
    """)
    count = cursor.fetchone()[0]
    cursor.close()
    return count


# ===========================================
# MAIN
# ===========================================

def main():
    parser = argparse.ArgumentParser(description="Index EDS products into Elasticsearch")
    parser.add_argument("--batch-size", type=int, default=DEFAULT_BATCH_SIZE,
                        help=f"Batch size for indexing (default: {DEFAULT_BATCH_SIZE})")
    parser.add_argument("--es-url", type=str, default=ES_URL,
                        help="Elasticsearch URL")
    parser.add_argument("--no-recreate", action="store_true",
                        help="Don't recreate index (append to existing)")
    args = parser.parse_args()

    # Connect to Elasticsearch
    es = Elasticsearch(args.es_url, request_timeout=60)
    try:
        info = es.info()
        logger.info(f"Connected to Elasticsearch: {info['version']['number']}")
    except Exception as e:
        logger.error(f"Cannot connect to Elasticsearch at {args.es_url}: {e}")
        sys.exit(1)

    # Connect to SQL Server
    logger.info(f"Connecting to SQL Server: {DB_SERVER}/{DB_DATABASE}")
    conn = get_db_connection()

    total = count_products(conn)
    logger.info(f"Total eligible products: {total:,}")

    # Recreate index (unless --no-recreate)
    if not args.no_recreate:
        recreate_index(es)

    # Run indexing
    indexed, errors = index_products(es, conn, batch_size=args.batch_size)

    # Print stats
    doc_count = es.count(index=ES_INDEX)["count"]
    logger.info(f"Final index document count: {doc_count:,}")

    conn.close()
    es.close()


if __name__ == "__main__":
    main()
