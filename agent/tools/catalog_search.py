"""Catalog search tool — searches EDS product/vendor/school catalogs.

Provides keyword search against the product catalog, vendor list,
and school/district directory in the EDS database.
"""

import logging
from typing import Any, Dict, List, Optional

from agent.tools.base import (
    BaseTool,
    ToolCategory,
    ToolDefinition,
    ToolParameter,
    ToolResult,
)

logger = logging.getLogger(__name__)

_SEARCH_QUERIES = {
    "products": """
        SELECT TOP(?) i.ItemId, i.ItemNumber, i.Description,
               i.UnitOfMeasure, v.VendorName
        FROM Items i
        JOIN Vendors v ON i.VendorId = v.VendorId
        WHERE i.Description LIKE '%' + ? + '%'
           OR i.ItemNumber LIKE '%' + ? + '%'
        ORDER BY i.Description
    """,
    "vendors": """
        SELECT TOP(?) v.VendorId, v.VendorCode, v.VendorName
        FROM Vendors v
        WHERE v.VendorName LIKE '%' + ? + '%'
           OR v.VendorCode LIKE '%' + ? + '%'
        ORDER BY v.VendorName
    """,
    "schools": """
        SELECT TOP(?) s.SchoolId, s.SchoolName, d.DistrictName
        FROM Schools s
        JOIN Districts d ON s.DistrictId = d.DistrictId
        WHERE s.SchoolName LIKE '%' + ? + '%'
           OR d.DistrictName LIKE '%' + ? + '%'
        ORDER BY d.DistrictName, s.SchoolName
    """,
}

# Number of search_term params per query (limit is always first)
_SEARCH_PARAM_COUNTS = {"products": 2, "vendors": 2, "schools": 2}


class CatalogSearchTool(BaseTool):
    """Search the EDS product, vendor, and school catalogs."""

    name = "catalog_search"
    category = ToolCategory.SQL

    def __init__(self):
        pass

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name=self.name,
            description=(
                "Search the EDS catalogs for products, vendors, or schools. "
                "Returns matching records from the EDS database."
            ),
            parameters=[
                ToolParameter(
                    name="search_term",
                    type="string",
                    description="Text to search for.",
                ),
                ToolParameter(
                    name="catalog",
                    type="string",
                    description="Which catalog to search.",
                    required=False,
                    default="products",
                    enum=["products", "vendors", "schools"],
                ),
                ToolParameter(
                    name="limit",
                    type="integer",
                    description="Maximum results to return.",
                    required=False,
                    default=20,
                ),
            ],
            category=self.category,
            returns="List of matching catalog records.",
        )

    def execute(self, **kwargs) -> ToolResult:
        search_term: str = kwargs.get("search_term", "")
        catalog: str = kwargs.get("catalog", "products")
        limit: int = kwargs.get("limit", 20)

        if not search_term.strip():
            return ToolResult(success=False, error="Empty search term")

        if catalog not in _SEARCH_QUERIES:
            return ToolResult(
                success=False,
                error=f"Unknown catalog '{catalog}'. Valid: {list(_SEARCH_QUERIES.keys())}",
            )

        try:
            rows, columns = self._run_search(catalog, search_term, limit)
            data = [dict(zip(columns, row)) for row in rows]

            return ToolResult(
                success=True,
                data=data,
                metadata={
                    "catalog": catalog,
                    "search_term": search_term,
                    "result_count": len(data),
                },
            )
        except Exception as e:
            logger.error("Catalog search failed: %s", e)
            return ToolResult(success=False, error=f"Search error: {e}")

    def _run_search(self, catalog: str, search_term: str, limit: int) -> tuple:
        from agent.tools.db_connection import get_connection

        sql = _SEARCH_QUERIES[catalog]
        n_search_params = _SEARCH_PARAM_COUNTS.get(catalog, 2)
        params = [limit] + [search_term] * n_search_params

        with get_connection("EDS", timeout=30) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, params)

            if cursor.description is None:
                return [], []

            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            return rows, columns


def create_catalog_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    return [CatalogSearchTool()]
