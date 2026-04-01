"""SQL executor tool — validates and runs SQL queries against the EDS database.

Queries pass through the security validator before execution. Results are
truncated to max_results rows and formatted as a list of dicts.
"""

import logging
import os
from typing import Any, Dict, List, Optional

from agent.security.validator import QueryValidator, ValidationResult
from agent.tools.base import (
    BaseTool,
    ToolCategory,
    ToolDefinition,
    ToolParameter,
    ToolResult,
)

logger = logging.getLogger(__name__)


class SQLExecutorTool(BaseTool):
    """Execute validated SQL queries against the EDS SQL Server database."""

    name = "sql_executor"
    category = ToolCategory.SQL

    def __init__(
        self,
        validator: Optional[QueryValidator] = None,
        max_results: int = 100,
        query_timeout: int = 30,
    ):
        self._validator = validator or QueryValidator()
        self._max_results = max_results
        self._query_timeout = query_timeout

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name=self.name,
            description=(
                "Execute a SQL query against the EDS SQL Server database. "
                "The query is validated for safety before execution. "
                "Returns results as a list of row dictionaries."
            ),
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="The SQL query to execute.",
                ),
                ToolParameter(
                    name="database",
                    type="string",
                    description="Target database name.",
                    required=False,
                    default="EDS",
                    enum=["EDS", "dpa_EDSAdmin"],
                ),
                ToolParameter(
                    name="max_rows",
                    type="integer",
                    description="Maximum number of rows to return.",
                    required=False,
                    default=100,
                ),
            ],
            category=self.category,
            returns="List of row dictionaries with column names as keys.",
        )

    def execute(self, **kwargs) -> ToolResult:
        query: str = kwargs.get("query", "")
        database: str = kwargs.get("database", "EDS")
        max_rows: int = kwargs.get("max_rows", self._max_results)

        if not query.strip():
            return ToolResult(success=False, error="Empty query")

        # Validate the query
        validation = self._validator.validate(query, target_database=database)
        if not validation.is_valid:
            return ToolResult(
                success=False,
                error=f"Query rejected: {'; '.join(validation.errors)}",
                metadata={
                    "query_type": validation.query_type.value,
                    "risk_level": validation.risk_level,
                },
            )

        # Execute against the database
        try:
            rows, columns = self._run_query(
                validation.sanitized or query,
                database,
                max_rows,
            )
            result_data = [dict(zip(columns, row)) for row in rows]

            metadata = {
                "row_count": len(result_data),
                "columns": columns,
                "query_type": validation.query_type.value,
                "database": database,
                "truncated": len(rows) >= max_rows,
            }
            if validation.warnings:
                metadata["warnings"] = validation.warnings

            return ToolResult(
                success=True,
                data=result_data,
                metadata=metadata,
            )

        except Exception as e:
            logger.error("SQL execution failed: %s", e)
            return ToolResult(
                success=False,
                error=f"Execution error: {e}",
                metadata={"query_type": validation.query_type.value},
            )

    def _run_query(
        self,
        query: str,
        database: str,
        max_rows: int,
    ) -> tuple:
        """Execute the query via pyodbc and return (rows, column_names)."""
        import pyodbc

        server = os.environ.get("DB_SERVER", "localhost")
        username = os.environ.get("DB_USERNAME", "")
        password = os.environ.get("DB_PASSWORD", "")

        conn_str = (
            f"DRIVER={{ODBC Driver 17 for SQL Server}};"
            f"SERVER={server};"
            f"DATABASE={database};"
            f"UID={username};"
            f"PWD={password};"
            f"Connection Timeout={self._query_timeout};"
        )

        with pyodbc.connect(conn_str, timeout=self._query_timeout) as conn:
            cursor = conn.cursor()
            cursor.execute(query)

            if cursor.description is None:
                # Non-SELECT statement (e.g. EXEC that returns no rows)
                return [], []

            columns = [col[0] for col in cursor.description]
            rows = cursor.fetchmany(max_rows)
            return rows, columns


def create_sql_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    """Factory function to create SQL tools from config."""
    config = config or {}
    security_config = config.get("security", {})
    max_results = security_config.get("max_query_results", 100)
    query_timeout = security_config.get("query_timeout", 30)

    allow_writes = not security_config.get("read_only_mode", True)
    allowed_databases = security_config.get("allowed_databases", ["EDS", "dpa_EDSAdmin"])

    validator = QueryValidator(
        allow_writes=allow_writes,
        allowed_databases=allowed_databases,
    )

    return [
        SQLExecutorTool(
            validator=validator,
            max_results=max_results,
            query_timeout=query_timeout,
        ),
    ]
