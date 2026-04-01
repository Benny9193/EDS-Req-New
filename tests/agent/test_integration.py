"""End-to-end integration tests for the agent wiring.

Tests the full flow: user context → chat → tool calls → audit logged → session persisted.
"""

import json
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from agent.core.agent import AgentMode, EDSAgent
from agent.llm.base import LLMResponse
from agent.security.roles import ApprovalLevel, Permission, UserContext
from agent.tools.registry import reset_registry


@pytest.fixture(autouse=True)
def clean_registry():
    reset_registry()
    yield
    reset_registry()


@pytest.fixture
def mock_llm():
    llm = MagicMock()
    llm.model_name = "test-model"
    llm.complete.return_value = LLMResponse(
        content="Here is your answer.",
        model="test-model",
        tool_calls=[],
        usage={"input_tokens": 100, "output_tokens": 50},
    )
    llm.stream.return_value = iter(["Here ", "is ", "your ", "answer."])
    return llm


@pytest.fixture
def agent(mock_llm, tmp_path):
    a = EDSAgent(config={
        "memory": {
            "sessions_dir": str(tmp_path / "sessions"),
            "learned_context_db": str(tmp_path / "knowledge.sqlite"),
        },
        "audit": {
            "log_dir": str(tmp_path / "audit"),
            "enabled": True,
        },
    })
    a._llm_provider = mock_llm
    a._provider_name = "test"
    return a


# ── Session persistence ──────────────────────────────────────────────


class TestSessionPersistence:
    def test_chat_persists_to_session(self, agent):
        session = agent.sessions.create_session()
        response = agent.chat("Hello", session_id=session.id)

        assert response.content == "Here is your answer."

        loaded = agent.sessions.get_session(session.id)
        assert len(loaded.messages) == 2
        assert loaded.messages[0].role == "user"
        assert loaded.messages[0].content == "Hello"
        assert loaded.messages[1].role == "assistant"

    def test_stream_persists_to_session(self, agent):
        session = agent.sessions.create_session()
        chunks = list(agent.chat_stream("Hi", session_id=session.id))

        assert "".join(chunks) == "Here is your answer."

        loaded = agent.sessions.get_session(session.id)
        assert len(loaded.messages) == 2

    def test_session_history_used_in_messages(self, agent, mock_llm):
        session = agent.sessions.create_session()

        # First turn
        agent.chat("What tables exist?", session_id=session.id)

        # Second turn — should include first turn in messages
        agent.chat("Tell me more about Vendors", session_id=session.id)

        # Verify the second call included history
        second_call_messages = mock_llm.complete.call_args_list[1][0][0]
        # Should have: system + user1 + assistant1 + user2
        roles = [m.role.value for m in second_call_messages]
        assert roles.count("user") >= 2


# ── User context ─────────────────────────────────────────────────────


class TestUserContextIntegration:
    def test_user_context_in_system_prompt(self, agent, mock_llm):
        agent.set_user_context(
            user_id=100, approval_level=0,
            user_name="Jane Teacher", school_id=42,
        )
        agent.chat("Hi")

        messages = mock_llm.complete.call_args[0][0]
        system_msg = messages[0].content
        assert "Jane Teacher" in system_msg
        assert "Requestor" in system_msg
        assert "Level 0" in system_msg

    def test_user_context_in_streamed_prompt(self, agent, mock_llm):
        agent.set_user_context(user_id=1, approval_level=9, user_name="Admin")
        list(agent.chat_stream("Hi"))

        messages = mock_llm.stream.call_args[0][0]
        system_msg = messages[0].content
        assert "System Administrator" in system_msg

    def test_status_includes_user_context(self, agent):
        agent.set_user_context(user_id=1, approval_level=5, user_name="Buyer")
        status = agent.get_status()
        assert status["user"]["level"] == 5
        assert status["user"]["role"] == "Customer Service Rep / Buyer"

    def test_no_user_context_no_crash(self, agent, mock_llm):
        response = agent.chat("Hi")
        assert response.content == "Here is your answer."
        messages = mock_llm.complete.call_args[0][0]
        system_msg = messages[0].content
        assert "Current user context" not in system_msg


# ── Audit logging ────────────────────────────────────────────────────


class TestAuditIntegration:
    def test_llm_call_audited(self, agent, tmp_path):
        from agent.audit.logger import reset_audit_logger
        reset_audit_logger()
        # Force agent to use fresh audit logger pointing at tmp_path
        agent._audit_logger = None

        agent.chat("Hello")
        agent.audit.close()

        audit_files = list((tmp_path / "audit").glob("audit_*.jsonl"))
        assert len(audit_files) >= 1

        all_lines = []
        for f in audit_files:
            all_lines.extend(f.read_text().strip().split("\n"))
        events = [json.loads(l) for l in all_lines if l]
        llm_events = [e for e in events if e["event_type"] == "llm_called"]
        assert len(llm_events) >= 1
        assert llm_events[0]["data"]["provider"] == "test"
        reset_audit_logger()

    def test_blocked_query_audited(self, agent, tmp_path):
        from agent.tools.sql_executor import SQLExecutorTool
        from agent.audit.logger import reset_audit_logger, get_audit_logger

        # Reset to use the test audit dir
        reset_audit_logger()
        audit = get_audit_logger({
            "audit": {"log_dir": str(tmp_path / "audit"), "enabled": True}
        })

        tool = SQLExecutorTool()
        tool.execute(query="EXEC xp_cmdshell 'whoami'")

        audit.close()

        audit_files = list((tmp_path / "audit").glob("audit_*.jsonl"))
        assert len(audit_files) >= 1

        all_lines = []
        for f in audit_files:
            all_lines.extend(f.read_text().strip().split("\n"))

        events = [json.loads(l) for l in all_lines if l]
        blocked = [e for e in events if e["event_type"] == "query_blocked"]
        assert len(blocked) >= 1
        assert "xp_cmdshell" in blocked[0]["data"]["sql"]

        security = [e for e in events if e["event_type"] == "security_alert"]
        assert len(security) >= 1

        reset_audit_logger()


# ── Tool calling with session ────────────────────────────────────────


class TestToolCallingWithSession:
    def test_tool_results_in_session(self, agent, mock_llm):
        from agent.tools.base import BaseTool, ToolCategory, ToolDefinition, ToolParameter, ToolResult
        from agent.tools.registry import get_registry

        class EchoTool(BaseTool):
            name = "echo"
            category = ToolCategory.UTILITY
            @property
            def definition(self):
                return ToolDefinition(
                    name="echo", description="Echo input",
                    parameters=[ToolParameter(name="text", type="string", description="Text")],
                    category=ToolCategory.UTILITY,
                )
            def execute(self, **kwargs):
                return ToolResult(success=True, data=f"echo: {kwargs.get('text', '')}")

        registry = get_registry()
        registry.register(EchoTool())
        agent._tool_registry = registry

        mock_llm.complete.side_effect = [
            LLMResponse(
                content="", model="test",
                tool_calls=[{"id": "tc1", "name": "echo", "input": {"text": "hello"}}],
                usage={"input_tokens": 10, "output_tokens": 5},
            ),
            LLMResponse(
                content="The echo tool said: hello",
                model="test", tool_calls=[],
                usage={"input_tokens": 20, "output_tokens": 10},
            ),
        ]

        session = agent.sessions.create_session()
        response = agent.chat("Echo hello", session_id=session.id)

        assert "hello" in response.content
        assert len(response.tool_calls) == 1

        # Session should have the user message and final response
        loaded = agent.sessions.get_session(session.id)
        assert len(loaded.messages) == 2


# ── CLI commands verification ────────────────────────────────────────


class TestCLICommands:
    def test_cli_has_all_commands(self):
        from agent.cli.app import cli
        command_names = list(cli.commands.keys())
        expected = ["chat", "ask", "sql", "docs", "run", "report",
                    "sessions", "status", "index-docs"]
        for cmd in expected:
            assert cmd in command_names, f"Missing CLI command: {cmd}"

    def test_status_command(self):
        from click.testing import CliRunner
        from agent.cli.app import cli

        runner = CliRunner()
        result = runner.invoke(cli, ["status"])
        assert result.exit_code == 0
        assert "EDS DBA Agent" in result.output
        assert "Provider" in result.output

    def test_sessions_command_empty(self):
        from click.testing import CliRunner
        from agent.cli.app import cli

        runner = CliRunner()
        result = runner.invoke(cli, ["sessions"])
        assert result.exit_code == 0
