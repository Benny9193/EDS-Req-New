#!/usr/bin/env python3
"""
EDS DBA MCP Server
==================

Model Context Protocol server for the EDS (Educational Data Services) database.
Exposes database tools directly to Claude Code for SQL execution, schema
introspection, documentation search, and report generation.

Uses FastMCP with stdio transport. All logging goes to stderr.

Tools:
  - execute_sql      — Run validated SQL queries (SELECT only by default)
  - explain_sql      — Get execution plans without running queries
  - search_docs      — Search database documentation via RAG
  - lookup_doc       — Look up a specific database object by name
  - introspect_schema — Get table/column/FK/index metadata
  - list_tables      — Quick list of all tables with row counts
  - test_connection   — Verify database connectivity
"""

import sys
import os
import json
import logging
from pathlib import Path
from datetime import datetime
from typing import Optional

# ── Ensure project root is importable ──────────────────────────────────
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

# ── Load .env before anything else ─────────────────────────────────────
from dotenv import load_dotenv

load_dotenv(PROJECT_ROOT / ".env")

# ── Logging to stderr only (MCP uses stdout for protocol) ─────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    stream=sys.stderr,
)
logger = logging.getLogger("eds-mcp")

# ── FastMCP import ─────────────────────────────────────────────────────
try:
    from mcp.server.fastmcp import FastMCP
except ImportError:
    logger.error(
        "MCP SDK not installed. Install with: pip install mcp\n"
        "  or: pip install 'mcp[cli]'"
    )
    sys.exit(1)

# ── EDS imports ────────────────────────────────────────────────────────
from scripts.db_utils import DatabaseConnection, DatabaseConnectionError, DatabaseQueryError
from agent.security.validator import QueryValidator, ValidationResult

# ── Server setup ───────────────────────────────────────────────────────
mcp = FastMCP(
    "EDS DBA Server",
    instructions="Database tools for the EDS procurement system. "
    "Execute SQL, inspect schemas, search documentation, and test connections.",
)

# ── Shared state ───────────────────────────────────────────────────────
validator = QueryValidator(
    read_only_mode=True,
    require_confirmation_for_writes=True,
    allowed_databases=["EDS", "dpa_EDSAdmin"],
)

ALLOWED_DATABASES = ["EDS", "dpa_EDSAdmin"]
MAX_ROWS = 500


# ═══════════════════════════════════════════════════════════════════════
# Helper Functions
# ═══════════════════════════════════════════════════════════════════════

def _serialize_value(value):
    """Convert a database value to JSON-safe format."""
    if value is None:
        return None
    if isinstance(value, datetime):
        return value.isoformat()
    if isinstance(value, bytes):
        return value.hex()
    if isinstance(value, (str, int, float, bool)):
        return value
    return str(value)


def _execute_read_query(
    query: str,
    database: str = "EDS",
    limit: int = 100,
) -> dict:
    """
    Execute a read-only query and return structured results.

    Returns dict with keys: columns, rows, row_count, truncated
    Raises on error.
    """
    # Validate
    result = validator.validate(query, database)
    if not result.is_valid:
        raise ValueError(f"Query blocked: {result.blocked_reason}")
    if not result.is_read_only:
        raise ValueError(
            "Only SELECT queries are allowed through the MCP server. "
            "Write operations must be done in SSMS."
        )

    # Add TOP if missing
    query_stripped = query.strip()
    query_upper = query_stripped.upper()
    if query_upper.startswith("SELECT") and "TOP" not in query_upper.split("FROM")[0]:
        select_end = query_upper.find("SELECT") + 6
        query_stripped = query_stripped[:select_end] + f" TOP {limit} " + query_stripped[select_end:]

    with DatabaseConnection(database=database) as db:
        cursor = db._conn.cursor()
        cursor.execute(query_stripped)

        columns = [desc[0] for desc in cursor.description] if cursor.description else []
        raw_rows = cursor.fetchall()
        cursor.close()

        rows = []
        for row in raw_rows[:limit]:
            rows.append({
                columns[i]: _serialize_value(row[i])
                for i in range(len(columns))
            })

        return {
            "columns": columns,
            "rows": rows,
            "row_count": len(rows),
            "truncated": len(raw_rows) > limit,
        }


# ═══════════════════════════════════════════════════════════════════════
# MCP Tools
# ═══════════════════════════════════════════════════════════════════════

@mcp.tool()
def execute_sql(
    query: str,
    database: str = "EDS",
    limit: int = 100,
) -> str:
    """
    Execute a read-only SQL query against the EDS database.

    Returns results as a formatted table. Only SELECT queries are allowed.
    Write operations (INSERT, UPDATE, DELETE, DROP) are blocked.

    Args:
        query: SQL SELECT query to execute
        database: Target database — "EDS" (catalog) or "dpa_EDSAdmin" (monitoring)
        limit: Maximum rows to return (default 100, max 500)

    Example queries:
        - SELECT TOP 10 * FROM BidHeaders ORDER BY CloseDate DESC
        - SELECT COUNT(*) FROM RequisitionItems WHERE YEAR(DateCreated) = 2024
        - SELECT v.VendorName, COUNT(*) as BidCount FROM BidImports bi JOIN Vendors v ON bi.VendorID = v.VendorID GROUP BY v.VendorName ORDER BY BidCount DESC
    """
    if database not in ALLOWED_DATABASES:
        return f"Error: Database '{database}' not allowed. Use: {ALLOWED_DATABASES}"

    limit = min(limit, MAX_ROWS)

    try:
        results = _execute_read_query(query, database, limit)
    except (ValueError, DatabaseConnectionError, DatabaseQueryError) as e:
        return f"Error: {e}"
    except Exception as e:
        logger.exception("execute_sql failed")
        return f"Error: {e}"

    # Format as markdown table
    if not results["rows"]:
        return "Query returned no results."

    columns = results["columns"]
    rows = results["rows"]

    lines = []
    lines.append("| " + " | ".join(columns) + " |")
    lines.append("| " + " | ".join(["---"] * len(columns)) + " |")
    for row in rows:
        values = []
        for col in columns:
            v = str(row.get(col, ""))
            if len(v) > 60:
                v = v[:57] + "..."
            values.append(v)
        lines.append("| " + " | ".join(values) + " |")

    footer = f"\n{results['row_count']} row(s) returned"
    if results["truncated"]:
        footer += f" (truncated to {limit})"

    return "\n".join(lines) + footer


@mcp.tool()
def explain_sql(
    query: str,
    database: str = "EDS",
) -> str:
    """
    Get the execution plan for a SQL query without running it.

    Use this to understand query performance and identify missing indexes
    before executing a potentially expensive query.

    Args:
        query: SQL query to analyze
        database: Target database — "EDS" or "dpa_EDSAdmin"
    """
    if database not in ALLOWED_DATABASES:
        return f"Error: Database '{database}' not allowed. Use: {ALLOWED_DATABASES}"

    result = validator.validate(query, database)
    if not result.is_valid:
        return f"Error: Query blocked — {result.blocked_reason}"

    try:
        with DatabaseConnection(database=database) as db:
            cursor = db._conn.cursor()
            cursor.execute("SET SHOWPLAN_TEXT ON")
            cursor.execute(query)

            plan_lines = []
            while True:
                row = cursor.fetchone()
                if not row:
                    break
                plan_lines.append(str(row[0]))

            cursor.execute("SET SHOWPLAN_TEXT OFF")
            cursor.close()

            if not plan_lines:
                return "No execution plan generated."

            return "Execution Plan:\n\n" + "\n".join(plan_lines)

    except Exception as e:
        logger.exception("explain_sql failed")
        return f"Error getting execution plan: {e}"


@mcp.tool()
def list_tables(
    database: str = "EDS",
    schema_filter: str = "dbo",
) -> str:
    """
    List all tables in the database with row counts and column counts.

    Quick overview tool — use introspect_schema for detailed column info.

    Args:
        database: Target database — "EDS" or "dpa_EDSAdmin"
        schema_filter: Schema to filter (default "dbo")
    """
    if database not in ALLOWED_DATABASES:
        return f"Error: Database '{database}' not allowed."

    query = """
    SELECT
        s.name AS [Schema],
        t.name AS [Table],
        p.rows AS [Rows],
        (SELECT COUNT(*) FROM sys.columns c WHERE c.object_id = t.object_id) AS [Columns]
    FROM sys.tables t
    INNER JOIN sys.schemas s ON t.schema_id = s.schema_id
    LEFT JOIN sys.partitions p ON t.object_id = p.object_id AND p.index_id IN (0, 1)
    WHERE t.is_ms_shipped = 0
    """
    if schema_filter:
        query += f" AND s.name = '{schema_filter}'"
    query += " ORDER BY p.rows DESC"

    try:
        results = _execute_read_query(query, database, 200)
    except Exception as e:
        return f"Error: {e}"

    if not results["rows"]:
        return "No tables found."

    lines = ["| Schema | Table | Rows | Columns |", "| --- | --- | --- | --- |"]
    for row in results["rows"]:
        rows_fmt = f"{row.get('Rows', 0):,}" if row.get("Rows") else "0"
        lines.append(f"| {row.get('Schema', '')} | {row.get('Table', '')} | {rows_fmt} | {row.get('Columns', '')} |")

    return "\n".join(lines) + f"\n\n{len(results['rows'])} table(s) in {database}"


@mcp.tool()
def introspect_schema(
    object_name: str,
    database: str = "EDS",
) -> str:
    """
    Get detailed schema for a table, view, or procedure.

    Returns columns with types, primary keys, foreign keys, indexes,
    and a sample of data. Use list_tables first to find table names.

    Args:
        object_name: Name of the table, view, or procedure (e.g., "BidHeaders", "Items")
        database: Target database — "EDS" or "dpa_EDSAdmin"
    """
    if database not in ALLOWED_DATABASES:
        return f"Error: Database '{database}' not allowed."

    output_parts = []

    try:
        with DatabaseConnection(database=database) as db:
            cursor = db._conn.cursor()

            # ── Columns ──
            cursor.execute("""
                SELECT
                    c.name AS column_name,
                    t.name AS data_type,
                    c.max_length,
                    c.is_nullable,
                    CASE WHEN pk.column_id IS NOT NULL THEN 1 ELSE 0 END AS is_pk,
                    CASE WHEN fkc.parent_column_id IS NOT NULL THEN 1 ELSE 0 END AS is_fk,
                    dc.definition AS default_value
                FROM sys.columns c
                INNER JOIN sys.types t ON c.user_type_id = t.user_type_id
                LEFT JOIN sys.default_constraints dc ON c.default_object_id = dc.object_id
                LEFT JOIN (
                    SELECT ic.object_id, ic.column_id
                    FROM sys.index_columns ic
                    INNER JOIN sys.indexes i ON ic.object_id = i.object_id AND ic.index_id = i.index_id
                    WHERE i.is_primary_key = 1
                ) pk ON c.object_id = pk.object_id AND c.column_id = pk.column_id
                LEFT JOIN sys.foreign_key_columns fkc ON c.object_id = fkc.parent_object_id
                    AND c.column_id = fkc.parent_column_id
                WHERE c.object_id = OBJECT_ID(?)
                ORDER BY c.column_id
            """, (object_name,))

            columns = cursor.fetchall()

            if not columns:
                return f"Object '{object_name}' not found in {database}. Use list_tables to see available tables."

            output_parts.append(f"## {object_name} ({database})\n")
            output_parts.append("### Columns\n")
            output_parts.append("| Column | Type | Nullable | PK | FK | Default |")
            output_parts.append("| --- | --- | --- | --- | --- | --- |")

            for col in columns:
                name, dtype, max_len, nullable, is_pk, is_fk, default = col
                type_str = dtype
                if max_len and max_len > 0 and dtype in ("varchar", "nvarchar", "char", "nchar", "binary", "varbinary"):
                    type_str += f"({max_len})" if max_len != -1 else "(max)"
                output_parts.append(
                    f"| {name} | {type_str} | {'Yes' if nullable else 'No'} "
                    f"| {'PK' if is_pk else ''} | {'FK' if is_fk else ''} "
                    f"| {default or ''} |"
                )

            # ── Foreign Keys ──
            cursor.execute("""
                SELECT
                    fk.name AS fk_name,
                    COL_NAME(fkc.parent_object_id, fkc.parent_column_id) AS fk_column,
                    OBJECT_NAME(fk.referenced_object_id) AS ref_table,
                    COL_NAME(fkc.referenced_object_id, fkc.referenced_column_id) AS ref_column
                FROM sys.foreign_keys fk
                INNER JOIN sys.foreign_key_columns fkc ON fk.object_id = fkc.constraint_object_id
                WHERE fk.parent_object_id = OBJECT_ID(?)
            """, (object_name,))

            fks = cursor.fetchall()
            if fks:
                output_parts.append("\n### Foreign Keys\n")
                for fk_name, fk_col, ref_table, ref_col in fks:
                    output_parts.append(f"- **{fk_col}** → {ref_table}.{ref_col} ({fk_name})")

            # ── Indexes ──
            cursor.execute("""
                SELECT
                    i.name AS index_name,
                    i.type_desc,
                    i.is_unique,
                    i.is_primary_key,
                    STRING_AGG(c.name, ', ') WITHIN GROUP (ORDER BY ic.key_ordinal) AS columns
                FROM sys.indexes i
                INNER JOIN sys.index_columns ic ON i.object_id = ic.object_id AND i.index_id = ic.index_id
                INNER JOIN sys.columns c ON ic.object_id = c.object_id AND ic.column_id = c.column_id
                WHERE i.object_id = OBJECT_ID(?) AND i.name IS NOT NULL
                GROUP BY i.name, i.type_desc, i.is_unique, i.is_primary_key
            """, (object_name,))

            indexes = cursor.fetchall()
            if indexes:
                output_parts.append("\n### Indexes\n")
                for idx_name, idx_type, is_unique, is_pk, idx_cols in indexes:
                    flags = []
                    if is_pk:
                        flags.append("PRIMARY KEY")
                    if is_unique:
                        flags.append("UNIQUE")
                    flags.append(idx_type)
                    output_parts.append(f"- **{idx_name}** ({', '.join(flags)}): {idx_cols}")

            # ── Row Count ──
            cursor.execute("""
                SELECT SUM(p.rows)
                FROM sys.partitions p
                WHERE p.object_id = OBJECT_ID(?) AND p.index_id IN (0, 1)
            """, (object_name,))

            row_count = cursor.fetchone()
            if row_count and row_count[0]:
                output_parts.append(f"\n**Row count:** {row_count[0]:,}")

            cursor.close()

    except Exception as e:
        logger.exception("introspect_schema failed")
        return f"Error introspecting '{object_name}': {e}"

    return "\n".join(output_parts)


@mcp.tool()
def search_docs(
    query: str,
    doc_type: str = "all",
    num_results: int = 5,
) -> str:
    """
    Search EDS database documentation using semantic search (RAG).

    Searches over table schemas, stored procedures, views, indexes, and
    business domain documentation. Requires the documentation index to be built.

    Args:
        query: Natural language search query (e.g., "vendor bid pricing", "purchase order workflow")
        doc_type: Filter by type — "all", "table", "procedure", "view", "index", "business"
        num_results: Number of results to return (default 5, max 20)
    """
    num_results = min(num_results, 20)

    try:
        from agent.rag.retriever import create_retriever

        retriever = create_retriever()

        if retriever.vector_store.count() == 0:
            return (
                "Documentation index is empty. "
                "Run: python -m agent.rag.indexer  to build the index."
            )

        if doc_type and doc_type != "all":
            results = retriever.retrieve_for_query_type(
                query=query,
                query_type=doc_type,
                n_results=num_results,
            )
        else:
            results = retriever.retrieve(
                query=query,
                n_results=num_results,
            )

        if not results:
            return f"No documentation found for: '{query}'"

        output = []
        for i, r in enumerate(results, 1):
            obj_name = (
                r.metadata.get("table_name")
                or r.metadata.get("procedure_name")
                or r.metadata.get("view_name")
                or r.metadata.get("domain_name")
                or "unknown"
            )
            chunk_type = r.metadata.get("chunk_type", "")
            source = r.metadata.get("source_file", "")
            score = round(r.score, 3)

            output.append(f"### {i}. {obj_name} ({chunk_type})")
            output.append(f"*Source: {source} | Relevance: {score}*\n")
            output.append(r.content)
            output.append("\n---\n")

        return "\n".join(output)

    except ImportError as e:
        return f"RAG dependencies not installed: {e}. Install with: pip install chromadb sentence-transformers"
    except Exception as e:
        logger.exception("search_docs failed")
        return f"Error searching documentation: {e}"


@mcp.tool()
def lookup_doc(
    object_name: str,
    object_type: str = "any",
) -> str:
    """
    Look up documentation for a specific database object by name.

    Use when you know the exact table, procedure, or view name.

    Args:
        object_name: Name of the database object (e.g., "BidHeaders", "sp_FA_AttemptLogin")
        object_type: Type filter — "table", "procedure", "view", "index", or "any"
    """
    try:
        from agent.rag.retriever import create_retriever

        retriever = create_retriever()
        query = f"{object_name} {object_type if object_type != 'any' else ''}"

        results = retriever.retrieve(query=query, n_results=3)

        # Find best match
        matching = []
        for r in results:
            obj = (
                r.metadata.get("table_name", "").lower()
                or r.metadata.get("procedure_name", "").lower()
                or r.metadata.get("view_name", "").lower()
                or ""
            )
            if object_name.lower() in obj or obj in object_name.lower():
                matching.append(r)

        if not matching and results:
            matching = results[:1]

        if not matching:
            return f"No documentation found for '{object_name}'"

        best = matching[0]
        chunk_type = best.metadata.get("chunk_type", "unknown")
        source = best.metadata.get("source_file", "")

        return (
            f"## {object_name} ({chunk_type})\n"
            f"*Source: {source}*\n\n"
            f"{best.content}"
        )

    except ImportError as e:
        return f"RAG dependencies not installed: {e}"
    except Exception as e:
        logger.exception("lookup_doc failed")
        return f"Error looking up '{object_name}': {e}"


@mcp.tool()
def test_connection(
    database: str = "EDS",
) -> str:
    """
    Test database connectivity and return server info.

    Use this to verify the database connection is working before running queries.

    Args:
        database: Target database — "EDS" or "dpa_EDSAdmin"
    """
    if database not in ALLOWED_DATABASES:
        return f"Error: Database '{database}' not allowed."

    try:
        with DatabaseConnection(database=database) as db:
            cursor = db._conn.cursor()

            # Server version
            cursor.execute("SELECT @@VERSION")
            version = cursor.fetchone()[0]

            # Server name
            cursor.execute("SELECT @@SERVERNAME")
            server_name = cursor.fetchone()[0]

            # Current database
            cursor.execute("SELECT DB_NAME()")
            current_db = cursor.fetchone()[0]

            # Table count
            cursor.execute(
                "SELECT COUNT(*) FROM sys.tables WHERE is_ms_shipped = 0"
            )
            table_count = cursor.fetchone()[0]

            cursor.close()

            return (
                f"**Connection OK**\n\n"
                f"- **Server:** {server_name}\n"
                f"- **Database:** {current_db}\n"
                f"- **Tables:** {table_count}\n"
                f"- **Version:** {version.split(chr(10))[0]}\n"
            )

    except DatabaseConnectionError as e:
        return f"Connection FAILED: {e}"
    except Exception as e:
        logger.exception("test_connection failed")
        return f"Connection error: {e}"


# ═══════════════════════════════════════════════════════════════════════
# Entry point
# ═══════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    logger.info("Starting EDS DBA MCP Server...")
    mcp.run()
