"""Tests for the MCP server."""

import json
import pytest
from unittest.mock import MagicMock, patch


class TestMCPServerDefinition:
    def test_mcp_server_imports(self):
        from agent.mcp.server import mcp
        assert mcp.name == "eds-dba-agent"

    def test_mcp_has_tools(self):
        from agent.mcp.server import mcp
        # FastMCP registers tools via decorators
        # Verify our tools are registered by checking the module functions exist
        from agent.mcp import server
        assert hasattr(server, "execute_sql")
        assert hasattr(server, "generate_sql")
        assert hasattr(server, "search_docs")
        assert hasattr(server, "introspect_schema")
        assert hasattr(server, "search_catalog")
        assert hasattr(server, "run_script")
        assert hasattr(server, "chat_with_agent")

    def test_mcp_has_resources(self):
        from agent.mcp import server
        assert hasattr(server, "agent_status")
        assert hasattr(server, "approval_levels")

    def test_mcp_has_prompts(self):
        from agent.mcp import server
        assert hasattr(server, "sql_query")
        assert hasattr(server, "investigate_table")
        assert hasattr(server, "vendor_report")


class TestMCPToolFunctions:
    """Test the MCP tool functions directly (without MCP transport)."""

    def test_execute_sql_blocked(self):
        from agent.mcp.server import execute_sql
        result = execute_sql("EXEC xp_cmdshell 'whoami'")
        assert "Error" in result

    def test_execute_sql_empty(self):
        from agent.mcp.server import execute_sql
        result = execute_sql("")
        assert "Error" in result

    @patch("agent.tools.sql_executor.SQLExecutorTool._run_query")
    def test_execute_sql_success(self, mock_run):
        mock_run.return_value = ([("Vendors", 100)], ["TableName", "Count"])
        from agent.mcp.server import execute_sql
        result = execute_sql("SELECT 'Vendors' AS TableName, 100 AS Count")
        parsed = json.loads(result)
        assert "data" in parsed
        assert len(parsed["data"]) == 1

    def test_search_catalog_empty(self):
        from agent.mcp.server import search_catalog
        result = search_catalog("")
        assert "Error" in result

    def test_introspect_schema_bad_type(self):
        from agent.mcp.server import introspect_schema
        result = introspect_schema("bogus")
        assert "Error" in result

    def test_run_script_missing(self):
        from agent.mcp.server import run_script
        result = run_script("nonexistent_script_xyz")
        assert "Error" in result

    @patch("agent.core.agent.get_provider")
    def test_chat_with_agent(self, mock_provider):
        from agent.llm.base import LLMResponse

        mock_llm = MagicMock()
        mock_llm.model_name = "test"
        mock_llm.complete.return_value = LLMResponse(
            content="The Vendors table has VendorId, VendorName...",
            model="test", tool_calls=[],
            usage={"input_tokens": 10, "output_tokens": 20},
        )
        mock_provider.return_value = mock_llm

        # Reset the cached agent
        import agent.mcp.server as srv
        srv._agent = None

        from agent.mcp.server import chat_with_agent
        result = chat_with_agent("What tables exist?")
        assert "Vendors" in result

        srv._agent = None  # cleanup


class TestMCPResources:
    def test_approval_levels_resource(self):
        from agent.mcp.server import approval_levels
        result = approval_levels()
        parsed = json.loads(result)
        assert "0" in parsed
        assert "9" in parsed
        assert parsed["0"]["label"] == "Requestor (Teacher/Staff)"
        assert "permissions" in parsed["0"]


class TestMCPCLICommand:
    def test_cli_has_mcp_command(self):
        from agent.cli.app import cli
        assert "mcp" in cli.commands
