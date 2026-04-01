"""Catalog search tool — searches EDS product/vendor/school catalogs.

Provides keyword search against the product catalog, vendor list,
and school/district directory in the EDS database.
"""

import logging
import os
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
        SELECT TOP(@limit) i.ItemId, i.ItemNumber, i.Description,
               i.UnitOfMeasure, v.VendorName
        FROM Items i
        JOIN Vendors v ON i.VendorId = v.VendorId
        WHERE i.Description LIKE '%' + @search + '%'
           OR i.ItemNumber LIKE '%' + @search + '%'
        ORDER BY i.Description
    """,
    "vendors": """
        SELECT TOP(@limit) v.VendorId, v.VendorCode, v.VendorName
        FROM Vendors v
        WHERE v.VendorName LIKE '%' + @search + '%'
           OR v.VendorCode LIKE '%' + @search + '%'
        ORDER BY v.VendorName
    """,
    "schools": """
        SELECT TOP(@limit) s.SchoolId, s.SchoolName, d.DistrictName
        FROM Schools s
        JOIN Districts d ON s.DistrictId = d.DistrictId
        WHERE s.SchoolName LIKE '%' + @search + '%'
           OR d.DistrictName LIKE '%' + @search + '%'
        ORDER BY d.DistrictName, s.SchoolName
    """,
}


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
        import pyodbc

        server = os.environ.get("DB_SERVER", "localhost")
        username = os.environ.get("DB_USERNAME", "")
        password = os.environ.get("DB_PASSWORD", "")

        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};DATABASE=EDS;"
            f"UID={username};PWD={password};"
        )

        sql = _SEARCH_QUERIES[catalog]

        with pyodbc.connect(conn_str, timeout=30) as conn:
            cursor = conn.cursor()
            cursor.execute(sql, {"search": search_term, "limit": limit})

            if cursor.description is None:
                return [], []

            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            return rows, columns


def create_catalog_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    return [CatalogSearchTool()]
