"""Tests for the agent tools layer: base classes, registry, sql_executor, query_generator."""

import json
import pytest
from unittest.mock import MagicMock, patch

from agent.tools.base import (
    BaseTool,
    ToolCall,
    ToolCallResult,
    ToolCategory,
    ToolDefinition,
    ToolParameter,
    ToolResult,
)
from agent.tools.registry import ToolRegistry, reset_registry
from agent.tools.sql_executor import SQLExecutorTool, create_sql_tools
from agent.tools.query_generator import QueryGeneratorTool, create_query_tools
from agent.security.validator import QueryValidator


# ── Fixtures ─────────────────────────────────────────────────────────


class DummyTool(BaseTool):
    name = "dummy"
    category = ToolCategory.UTILITY

    @property
    def definition(self):
        return ToolDefinition(
            name=self.name,
            description="A dummy tool for testing.",
            parameters=[
                ToolParameter(name="input", type="string", description="Input text."),
            ],
            category=self.category,
        )

    def execute(self, **kwargs):
        return ToolResult(success=True, data=f"echo: {kwargs.get('input', '')}")


class AnotherTool(BaseTool):
    name = "another"
    category = ToolCategory.SQL

    @property
    def definition(self):
        return ToolDefinition(
            name=self.name,
            description="Another tool.",
            parameters=[],
            category=self.category,
        )

    def execute(self, **kwargs):
        return ToolResult(success=True, data="ok")


@pytest.fixture
def registry():
    return ToolRegistry()


@pytest.fixture(autouse=True)
def clean_global_registry():
    """Reset the global registry between tests."""
    reset_registry()
    yield
    reset_registry()


# ── ToolParameter / ToolDefinition ───────────────────────────────────


class TestToolDefinition:
    def test_to_json_schema(self):
        defn = ToolDefinition(
            name="test",
            description="Test tool",
            parameters=[
                ToolParameter(name="query", type="string", description="SQL query"),
                ToolParameter(name="limit", type="integer", description="Max rows",
                              required=False, default=100),
            ],
            category=ToolCategory.SQL,
        )
        schema = defn.to_json_schema()
        assert schema["type"] == "object"
        assert "query" in schema["properties"]
        assert "limit" in schema["properties"]
        assert schema["required"] == ["query"]
        assert schema["properties"]["limit"]["default"] == 100

    def test_to_anthropic_format(self):
        defn = DummyTool().definition
        fmt = defn.to_anthropic_format()
        assert fmt["name"] == "dummy"
        assert "description" in fmt
        assert "input_schema" in fmt

    def test_to_openai_format(self):
        defn = DummyTool().definition
        fmt = defn.to_openai_format()
        assert fmt["type"] == "function"
        assert fmt["function"]["name"] == "dummy"
        assert "parameters" in fmt["function"]

    def test_enum_parameter(self):
        param = ToolParameter(
            name="db", type="string", description="Database",
            enum=["EDS", "dpa_EDSAdmin"],
        )
        schema = param.to_json_schema()
        assert schema["enum"] == ["EDS", "dpa_EDSAdmin"]


# ── ToolRegistry ─────────────────────────────────────────────────────


class TestToolRegistry:
    def test_register_and_get(self, registry):
        tool = DummyTool()
        registry.register(tool)
        assert registry.get("dummy") is tool
        assert registry.tool_count == 1

    def test_register_duplicate_raises(self, registry):
        registry.register(DummyTool())
        with pytest.raises(ValueError, match="already registered"):
            registry.register(DummyTool())

    def test_register_many(self, registry):
        registry.register_many([DummyTool(), AnotherTool()])
        assert registry.tool_count == 2

    def test_unregister(self, registry):
        registry.register(DummyTool())
        removed = registry.unregister("dummy")
        assert removed is not None
        assert registry.tool_count == 0

    def test_unregister_missing_returns_none(self, registry):
        assert registry.unregister("nonexistent") is None

    def test_list_tools(self, registry):
        registry.register_many([DummyTool(), AnotherTool()])
        names = registry.list_tools()
        assert names == ["another", "dummy"]

    def test_list_tools_by_category(self, registry):
        registry.register_many([DummyTool(), AnotherTool()])
        assert registry.list_tools(category=ToolCategory.UTILITY) == ["dummy"]
        assert registry.list_tools(category=ToolCategory.SQL) == ["another"]

    def test_list_tools_enabled_only(self, registry):
        tool = DummyTool()
        tool.enabled = False
        registry.register(tool)
        assert registry.list_tools(enabled_only=True) == []
        assert registry.list_tools(enabled_only=False) == ["dummy"]

    def test_execute(self, registry):
        registry.register(DummyTool())
        result = registry.execute("dummy", input="hello")
        assert result.success
        assert result.data == "echo: hello"

    def test_execute_missing_raises(self, registry):
        with pytest.raises(ValueError, match="not found"):
            registry.execute("nonexistent")

    def test_execute_disabled_raises(self, registry):
        tool = DummyTool()
        tool.enabled = False
        registry.register(tool)
        with pytest.raises(ValueError, match="disabled"):
            registry.execute("dummy")

    def test_execute_call(self, registry):
        registry.register(DummyTool())
        call = ToolCall(tool_name="dummy", parameters={"input": "test"}, call_id="c1")
        result = registry.execute_call(call)
        assert isinstance(result, ToolCallResult)
        assert result.result.success
        assert result.duration_ms >= 0
        assert result.tool_call.call_id == "c1"

    def test_get_tools_for_llm_anthropic(self, registry):
        registry.register(DummyTool())
        tools = registry.get_tools_for_llm(format="anthropic")
        assert len(tools) == 1
        assert "input_schema" in tools[0]

    def test_get_tools_for_llm_openai(self, registry):
        registry.register(DummyTool())
        tools = registry.get_tools_for_llm(format="openai")
        assert len(tools) == 1
        assert tools[0]["type"] == "function"

    def test_enable_disable_category(self, registry):
        registry.register_many([DummyTool(), AnotherTool()])
        registry.disable_category(ToolCategory.UTILITY)
        assert registry.list_tools(enabled_only=True) == ["another"]
        registry.enable_category(ToolCategory.UTILITY)
        assert "dummy" in registry.list_tools(enabled_only=True)

    def test_contains(self, registry):
        registry.register(DummyTool())
        assert "dummy" in registry
        assert "nonexistent" not in registry

    def test_iter(self, registry):
        registry.register_many([DummyTool(), AnotherTool()])
        assert list(registry) == ["another", "dummy"]

    def test_get_definition(self, registry):
        registry.register(DummyTool())
        defn = registry.get_definition("dummy")
        assert defn is not None
        assert defn.name == "dummy"

    def test_get_definition_missing(self, registry):
        assert registry.get_definition("nope") is None


# ── SQLExecutorTool ──────────────────────────────────────────────────


class TestSQLExecutorTool:
    def test_definition(self):
        tool = SQLExecutorTool()
        defn = tool.definition
        assert defn.name == "sql_executor"
        assert defn.category == ToolCategory.SQL
        param_names = [p.name for p in defn.parameters]
        assert "query" in param_names
        assert "database" in param_names

    def test_empty_query_rejected(self):
        tool = SQLExecutorTool()
        result = tool.execute(query="")
        assert not result.success
        assert "Empty" in result.error

    def test_blocked_query_rejected(self):
        tool = SQLExecutorTool()
        result = tool.execute(query="EXEC xp_cmdshell 'whoami'")
        assert not result.success
        assert "rejected" in result.error.lower()

    def test_write_query_rejected_in_readonly(self):
        tool = SQLExecutorTool()
        result = tool.execute(query="INSERT INTO Foo VALUES (1)")
        assert not result.success

    def test_disallowed_database_rejected(self):
        tool = SQLExecutorTool()
        result = tool.execute(query="SELECT 1", database="master")
        assert not result.success
        assert "master" in result.error

    @patch("agent.tools.sql_executor.SQLExecutorTool._run_query")
    def test_successful_execution(self, mock_run):
        mock_run.return_value = (
            [("School Specialty", 205723), ("Staples", 55509)],
            ["VendorName", "POCount"],
        )
        tool = SQLExecutorTool()
        result = tool.execute(query="SELECT VendorName, POCount FROM Vendors")
        assert result.success
        assert len(result.data) == 2
        assert result.data[0]["VendorName"] == "School Specialty"
        assert result.metadata["row_count"] == 2
        assert result.metadata["columns"] == ["VendorName", "POCount"]

    @patch("agent.tools.sql_executor.SQLExecutorTool._run_query")
    def test_execution_error(self, mock_run):
        mock_run.side_effect = Exception("Connection failed")
        tool = SQLExecutorTool()
        result = tool.execute(query="SELECT 1")
        assert not result.success
        assert "Connection failed" in result.error

    @patch("agent.tools.sql_executor.SQLExecutorTool._run_query")
    def test_truncated_flag(self, mock_run):
        rows = [(i,) for i in range(100)]
        mock_run.return_value = (rows, ["Id"])
        tool = SQLExecutorTool(max_results=100)
        result = tool.execute(query="SELECT Id FROM Foo")
        assert result.metadata["truncated"] is True

    @patch("agent.tools.sql_executor.SQLExecutorTool._run_query")
    def test_no_result_set(self, mock_run):
        mock_run.return_value = ([], [])
        tool = SQLExecutorTool()
        result = tool.execute(query="EXEC sp_GetVendors")
        assert result.success
        assert result.data == []

    def test_callable(self):
        tool = SQLExecutorTool()
        result = tool(query="")
        assert not result.success

    def test_create_sql_tools_factory(self):
        tools = create_sql_tools({
            "security": {
                "max_query_results": 50,
                "query_timeout": 15,
                "read_only_mode": True,
            }
        })
        assert len(tools) == 1
        assert tools[0].name == "sql_executor"
        assert tools[0]._max_results == 50


# ── QueryGeneratorTool ───────────────────────────────────────────────


class TestQueryGeneratorTool:
    def test_definition(self):
        tool = QueryGeneratorTool()
        defn = tool.definition
        assert defn.name == "query_generator"
        assert defn.category == ToolCategory.SQL
        param_names = [p.name for p in defn.parameters]
        assert "description" in param_names

    def test_empty_description_rejected(self):
        tool = QueryGeneratorTool()
        result = tool.execute(description="")
        assert not result.success
        assert "Empty" in result.error

    @patch("agent.llm.registry.get_provider")
    @patch("agent.config.get_llm_config")
    def test_successful_generation(self, mock_config, mock_provider):
        from agent.llm.base import LLMResponse

        mock_config.return_value = {}
        mock_llm = MagicMock()
        mock_llm.complete.return_value = LLMResponse(
            content="SELECT TOP 10 v.VendorName FROM Vendors v ORDER BY v.VendorName",
            model="test-model",
        )
        mock_provider.return_value = mock_llm

        tool = QueryGeneratorTool(provider_name="claude")
        result = tool.execute(description="List top 10 vendors")
        assert result.success
        assert "SELECT" in result.data
        assert "Vendors" in result.data

    @patch("agent.llm.registry.get_provider")
    @patch("agent.config.get_llm_config")
    def test_strips_markdown_fences(self, mock_config, mock_provider):
        from agent.llm.base import LLMResponse

        mock_config.return_value = {}
        mock_llm = MagicMock()
        mock_llm.complete.return_value = LLMResponse(
            content="```sql\nSELECT 1\n```",
            model="test-model",
        )
        mock_provider.return_value = mock_llm

        tool = QueryGeneratorTool(provider_name="claude")
        result = tool.execute(description="Select one")
        assert result.success
        assert result.data == "SELECT 1"
        assert "```" not in result.data

    @patch("agent.llm.registry.get_provider")
    @patch("agent.config.get_llm_config")
    def test_generation_error(self, mock_config, mock_provider):
        mock_config.return_value = {}
        mock_provider.side_effect = ValueError("No API key")

        tool = QueryGeneratorTool(provider_name="claude")
        result = tool.execute(description="Generate something")
        assert not result.success
        assert "No API key" in result.error

    def test_create_query_tools_factory(self):
        tools = create_query_tools({"llm": {"default_provider": "ollama"}})
        assert len(tools) == 1
        assert tools[0].name == "query_generator"
        assert tools[0]._provider_name == "ollama"


# ── Agent Tool-Calling Integration ───────────────────────────────────


class TestAgentToolCalling:
    """Test that EDSAgent correctly wires the tool-calling loop."""

    @patch("agent.core.agent.get_provider")
    def test_chat_without_tools(self, mock_get_provider):
        """Agent should work fine when no tools request tool calls."""
        from agent.llm.base import LLMResponse
        from agent.core.agent import EDSAgent

        mock_llm = MagicMock()
        mock_llm.complete.return_value = LLMResponse(
            content="Hello! I'm the EDS DBA Agent.",
            model="test",
            tool_calls=[],
        )
        mock_llm.model_name = "test"
        mock_get_provider.return_value = mock_llm

        agent = EDSAgent()
        agent._llm_provider = mock_llm
        agent._provider_name = "claude"

        response = agent.chat("Hello")
        assert response.content == "Hello! I'm the EDS DBA Agent."
        assert response.tool_calls == []
        assert response.error is None

    @patch("agent.core.agent.get_provider")
    def test_chat_with_tool_call(self, mock_get_provider):
        """Agent should execute tool calls and feed results back to LLM."""
        from agent.llm.base import LLMResponse
        from agent.core.agent import EDSAgent
        from agent.tools.registry import get_registry

        # Register a mock tool
        registry = get_registry()
        dummy = DummyTool()
        registry.register(dummy)

        # First call: LLM requests tool use
        # Second call: LLM gives final response
        mock_llm = MagicMock()
        mock_llm.complete.side_effect = [
            LLMResponse(
                content="",
                model="test",
                tool_calls=[{"id": "tc1", "name": "dummy", "input": {"input": "test"}}],
            ),
            LLMResponse(
                content="The tool returned: echo: test",
                model="test",
                tool_calls=[],
            ),
        ]
        mock_llm.model_name = "test"
        mock_get_provider.return_value = mock_llm

        agent = EDSAgent()
        agent._llm_provider = mock_llm
        agent._provider_name = "claude"
        agent._tool_registry = registry

        response = agent.chat("Use the dummy tool with 'test'")
        assert response.content == "The tool returned: echo: test"
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0]["tool_name"] == "dummy"
        assert response.tool_calls[0]["success"] is True

    @patch("agent.core.agent.get_provider")
    def test_tool_call_error_handled(self, mock_get_provider):
        """Agent should handle tool execution errors gracefully."""
        from agent.llm.base import LLMResponse
        from agent.core.agent import EDSAgent
        from agent.tools.registry import get_registry

        registry = get_registry()
        # Register a tool that will fail (nonexistent tool name in the call)

        mock_llm = MagicMock()
        mock_llm.complete.side_effect = [
            LLMResponse(
                content="",
                model="test",
                tool_calls=[{"id": "tc1", "name": "nonexistent", "input": {}}],
            ),
            LLMResponse(
                content="Sorry, that tool failed.",
                model="test",
                tool_calls=[],
            ),
        ]
        mock_llm.model_name = "test"
        mock_get_provider.return_value = mock_llm

        agent = EDSAgent()
        agent._llm_provider = mock_llm
        agent._provider_name = "claude"
        agent._tool_registry = registry

        response = agent.chat("Run nonexistent tool")
        assert response.content == "Sorry, that tool failed."
        assert len(response.tool_calls) == 1
        assert response.tool_calls[0]["success"] is False
