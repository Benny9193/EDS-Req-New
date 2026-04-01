"""MCP server exposing the EDS DBA Agent as a tool provider.

Enables Claude Desktop, Claude Code, and other MCP clients to use
the agent's tools: SQL execution, query generation, documentation
search, schema introspection, catalog search, and report generation.

Usage:
  python -m agent.mcp.server              # stdio transport (for Claude Desktop)
  python -m agent.mcp.server --sse        # SSE transport (for web clients)
"""

import json
import logging
from typing import Optional

from mcp.server.fastmcp import FastMCP

logger = logging.getLogger(__name__)

mcp = FastMCP(
    name="eds-dba-agent",
    instructions=(
        "EDS DBA Agent — AI-powered database assistant for the EDS "
        "(Educational Data Services) K-12 e-procurement system. "
        "Provides SQL execution, query generation, documentation search, "
        "schema introspection, catalog search, and report generation."
    ),
)

# Lazy-loaded agent instance
_agent = None


def _get_agent():
    global _agent
    if _agent is None:
        from agent.core.agent import EDSAgent
        _agent = EDSAgent()
    return _agent


# ── Tools ────────────────────────────────────────────────────────────


@mcp.tool()
def execute_sql(query: str, database: str = "EDS", max_rows: int = 100) -> str:
    """Execute a validated SQL query against the EDS database.

    The query is checked for safety (blocked patterns, write protection)
    before execution. Returns results as JSON.

    Args:
        query: SQL query to execute
        database: Target database (EDS or dpa_EDSAdmin)
        max_rows: Maximum rows to return
    """
    from agent.tools.sql_executor import SQLExecutorTool
    tool = SQLExecutorTool()
    result = tool.execute(query=query, database=database, max_rows=max_rows)

    if result.success:
        return json.dumps({
            "data": result.data,
            "metadata": result.metadata,
        }, default=str, indent=2)
    else:
        return f"Error: {result.error}"


@mcp.tool()
def generate_sql(description: str, context: str = "") -> str:
    """Generate a SQL Server query from a natural language description.

    Uses the LLM with EDS schema context to produce correct T-SQL.

    Args:
        description: What you want to query in plain English
        context: Additional context about specific tables or columns
    """
    from agent.tools.query_generator import QueryGeneratorTool
    from agent.config import get_default_provider

    tool = QueryGeneratorTool(provider_name=get_default_provider())
    result = tool.execute(description=description, context=context)

    if result.success:
        return result.data
    else:
        return f"Error: {result.error}"


@mcp.tool()
def search_docs(query: str, query_type: str = "general", n_results: int = 5) -> str:
    """Search EDS documentation using RAG-powered hybrid retrieval.

    Searches schema docs, stored procedures, views, business workflows,
    and other documentation.

    Args:
        query: Search query in natural language
        query_type: Type hint for search optimization (general/sql/schema/procedure)
        n_results: Number of results to return
    """
    from agent.tools.doc_retriever import DocRetrieverTool
    from agent.config import load_config

    tool = DocRetrieverTool(config=load_config())
    result = tool.execute(query=query, query_type=query_type, n_results=n_results)

    if result.success:
        return json.dumps(result.data, default=str, indent=2)
    else:
        return f"Error: {result.error}"


@mcp.tool()
def introspect_schema(
    query_type: str, object_name: str = "", database: str = "EDS",
) -> str:
    """Query live database schema metadata.

    Args:
        query_type: One of: tables, columns, procedures, views, indexes, table_row_counts
        object_name: Table/object name (required for columns and indexes)
        database: Target database (EDS or dpa_EDSAdmin)
    """
    from agent.tools.schema_introspector import SchemaIntrospectorTool

    tool = SchemaIntrospectorTool()
    result = tool.execute(
        query_type=query_type, object_name=object_name, database=database,
    )

    if result.success:
        return json.dumps(result.data, default=str, indent=2)
    else:
        return f"Error: {result.error}"


@mcp.tool()
def search_catalog(
    search_term: str, catalog: str = "products", limit: int = 20,
) -> str:
    """Search EDS product, vendor, or school catalogs.

    Args:
        search_term: Text to search for
        catalog: Which catalog (products/vendors/schools)
        limit: Maximum results
    """
    from agent.tools.catalog_search import CatalogSearchTool

    tool = CatalogSearchTool()
    result = tool.execute(
        search_term=search_term, catalog=catalog, limit=limit,
    )

    if result.success:
        return json.dumps(result.data, default=str, indent=2)
    else:
        return f"Error: {result.error}"


@mcp.tool()
def run_script(script_name: str, args: str = "") -> str:
    """Execute a Python analysis script from the scripts directory.

    Available scripts include performance analysis, index extraction,
    blocking investigation, and documentation generation.

    Args:
        script_name: Script name (without .py extension)
        args: Command-line arguments to pass
    """
    from agent.tools.script_runner import ScriptRunnerTool
    from agent.config import load_config

    config = load_config()
    scripts_dir = config.get("tools", {}).get("scripts_dir", "scripts")
    tool = ScriptRunnerTool(scripts_dir=scripts_dir)
    result = tool.execute(script_name=script_name, args=args)

    if result.success:
        return result.data
    else:
        return f"Error: {result.error}"


@mcp.tool()
def chat_with_agent(message: str, mode: str = "chat") -> str:
    """Send a message to the EDS DBA Agent and get a response.

    The agent has full context about the EDS database schema and can
    use tools to answer questions.

    Args:
        message: Your question or request
        mode: Agent mode (chat/sql/docs/analyze)
    """
    from agent.core.agent import AgentMode

    agent = _get_agent()
    response = agent.chat(message, mode=AgentMode(mode))

    if response.error:
        return f"Error: {response.error}"

    result = response.content
    if response.tool_calls:
        result += f"\n\n[{len(response.tool_calls)} tool(s) used]"
    if response.sql_generated:
        result += f"\n\nGenerated SQL:\n{response.sql_generated}"

    return result


# ── Resources ────────────────────────────────────────────────────────


@mcp.resource("eds://status")
def agent_status() -> str:
    """Current agent status including provider, tools, and configuration."""
    agent = _get_agent()
    return json.dumps(agent.get_status(), default=str, indent=2)


@mcp.resource("eds://approval-levels")
def approval_levels() -> str:
    """EDS approval level hierarchy and permission definitions."""
    from agent.security.roles import LEVEL_LABELS, get_permissions_for_level

    levels = {}
    for level_val, label in sorted(LEVEL_LABELS.items()):
        perms = get_permissions_for_level(level_val)
        levels[str(level_val)] = {
            "label": label,
            "permissions": sorted(perms),
        }
    return json.dumps(levels, indent=2)


# ── Prompts ──────────────────────────────────────────────────────────


@mcp.prompt()
def sql_query(description: str) -> str:
    """Generate a SQL query for the EDS database."""
    return (
        f"Generate a T-SQL query for the EDS database: {description}\n\n"
        "Use the generate_sql tool, then optionally execute_sql to run it."
    )


@mcp.prompt()
def investigate_table(table_name: str) -> str:
    """Investigate a database table's structure and data."""
    return (
        f"Investigate the {table_name} table:\n"
        f"1. Use introspect_schema to get its columns\n"
        f"2. Use introspect_schema to get its indexes\n"
        f"3. Use execute_sql to get a sample of 5 rows\n"
        f"4. Summarize the table's purpose and structure"
    )


@mcp.prompt()
def vendor_report(vendor_name: str) -> str:
    """Generate a report about a specific vendor."""
    return (
        f"Find information about vendor '{vendor_name}':\n"
        f"1. Search the catalog for the vendor\n"
        f"2. Execute SQL to get their order history\n"
        f"3. Summarize their total spend, PO count, and key products"
    )


# ── Entry point ──────────────────────────────────────────────────────


def main():
    """Run the MCP server."""
    import sys

    if "--sse" in sys.argv:
        mcp.run(transport="sse")
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
