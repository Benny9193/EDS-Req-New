"""Schema introspector tool — queries live database metadata.

Introspects tables, views, columns, stored procedures, and indexes
from the EDS and dpa_EDSAdmin databases via system catalog views.
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

# Pre-built introspection queries
_QUERIES = {
    "tables": """
        SELECT t.TABLE_SCHEMA, t.TABLE_NAME, t.TABLE_TYPE
        FROM INFORMATION_SCHEMA.TABLES t
        ORDER BY t.TABLE_SCHEMA, t.TABLE_NAME
    """,
    "columns": """
        SELECT c.TABLE_NAME, c.COLUMN_NAME, c.DATA_TYPE,
               c.CHARACTER_MAXIMUM_LENGTH, c.IS_NULLABLE, c.COLUMN_DEFAULT
        FROM INFORMATION_SCHEMA.COLUMNS c
        WHERE c.TABLE_NAME = ?
        ORDER BY c.ORDINAL_POSITION
    """,
    "procedures": """
        SELECT ROUTINE_SCHEMA, ROUTINE_NAME, ROUTINE_TYPE, CREATED, LAST_ALTERED
        FROM INFORMATION_SCHEMA.ROUTINES
        WHERE ROUTINE_TYPE = 'PROCEDURE'
        ORDER BY ROUTINE_SCHEMA, ROUTINE_NAME
    """,
    "views": """
        SELECT TABLE_SCHEMA, TABLE_NAME
        FROM INFORMATION_SCHEMA.VIEWS
        ORDER BY TABLE_SCHEMA, TABLE_NAME
    """,
    "indexes": """
        SELECT i.name AS IndexName, t.name AS TableName,
               i.type_desc AS IndexType, i.is_unique, i.is_primary_key
        FROM sys.indexes i
        JOIN sys.tables t ON i.object_id = t.object_id
        WHERE i.name IS NOT NULL AND t.name = ?
        ORDER BY t.name, i.name
    """,
    "table_row_counts": """
        SELECT t.name AS TableName,
               SUM(p.rows) AS RowCount
        FROM sys.tables t
        JOIN sys.partitions p ON t.object_id = p.object_id AND p.index_id IN (0, 1)
        GROUP BY t.name
        ORDER BY SUM(p.rows) DESC
    """,
}


class SchemaIntrospectorTool(BaseTool):
    """Introspect live database schema metadata."""

    name = "schema_introspector"
    category = ToolCategory.SQL

    def __init__(self):
        pass

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name=self.name,
            description=(
                "Query live database metadata: list tables, columns, stored procedures, "
                "views, indexes, and row counts from the EDS SQL Server database."
            ),
            parameters=[
                ToolParameter(
                    name="query_type",
                    type="string",
                    description="Type of schema query to run.",
                    enum=["tables", "columns", "procedures", "views", "indexes", "table_row_counts"],
                ),
                ToolParameter(
                    name="object_name",
                    type="string",
                    description="Table or object name (required for 'columns' and 'indexes' queries).",
                    required=False,
                    default="",
                ),
                ToolParameter(
                    name="database",
                    type="string",
                    description="Target database.",
                    required=False,
                    default="EDS",
                    enum=["EDS", "dpa_EDSAdmin"],
                ),
            ],
            category=self.category,
            returns="Schema metadata as a list of row dictionaries.",
        )

    def execute(self, **kwargs) -> ToolResult:
        query_type: str = kwargs.get("query_type", "")
        object_name: str = kwargs.get("object_name", "")
        database: str = kwargs.get("database", "EDS")

        if query_type not in _QUERIES:
            return ToolResult(
                success=False,
                error=f"Unknown query_type '{query_type}'. "
                      f"Valid: {list(_QUERIES.keys())}",
            )

        if query_type in ("columns", "indexes") and not object_name:
            return ToolResult(
                success=False,
                error=f"object_name is required for '{query_type}' query.",
            )

        sql = _QUERIES[query_type]
        params = [object_name] if "?" in sql else []

        try:
            rows, columns = self._run_query(sql, database, params)
            data = [dict(zip(columns, row)) for row in rows]
            return ToolResult(
                success=True,
                data=data,
                metadata={
                    "query_type": query_type,
                    "database": database,
                    "row_count": len(data),
                },
            )
        except Exception as e:
            logger.error("Schema introspection failed: %s", e)
            return ToolResult(success=False, error=f"Introspection error: {e}")

    def _run_query(self, sql: str, database: str, params: list) -> tuple:
        from agent.tools.db_connection import get_connection

        with get_connection(database, timeout=30) as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)

            if cursor.description is None:
                return [], []

            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchall()
            return rows, columns


def create_schema_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    return [SchemaIntrospectorTool()]
