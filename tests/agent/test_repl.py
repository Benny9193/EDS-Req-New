"""Tests for REPL slash commands via the extracted handle_command function."""

import pytest
from unittest.mock import MagicMock, patch

from agent.cli.repl import CommandResult, handle_command
from agent.core.agent import AgentMode, EDSAgent


@pytest.fixture
def agent(tmp_path):
    a = EDSAgent(config={
        "memory": {"sessions_dir": str(tmp_path / "sessions")},
    })
    a._llm_provider = MagicMock()
    a._llm_provider.model_name = "test"
    a._provider_name = "test"
    return a


@pytest.fixture
def session_id(agent):
    s = agent.sessions.create_session(mode="chat", provider="test")
    return s.id


class TestExitCommands:
    def test_exit(self, agent, session_id):
        r = handle_command("/exit", agent, session_id)
        assert r.action == "exit"

    def test_quit(self, agent, session_id):
        r = handle_command("/quit", agent, session_id)
        assert r.action == "exit"

    def test_q(self, agent, session_id):
        r = handle_command("/q", agent, session_id)
        assert r.action == "exit"


class TestModeCommands:
    def test_sql(self, agent, session_id):
        r = handle_command("/sql", agent, session_id)
        assert r.action == "continue"
        assert agent.mode == AgentMode.SQL

    def test_docs(self, agent, session_id):
        r = handle_command("/docs", agent, session_id)
        assert agent.mode == AgentMode.DOCS

    def test_analyze(self, agent, session_id):
        r = handle_command("/analyze", agent, session_id)
        assert agent.mode == AgentMode.ANALYZE

    def test_chat(self, agent, session_id):
        agent.mode = AgentMode.SQL
        r = handle_command("/chat", agent, session_id)
        assert agent.mode == AgentMode.CHAT


class TestHelp:
    def test_help(self, agent, session_id):
        r = handle_command("/help", agent, session_id)
        assert r.action == "info"
        assert "/exit" in r.message


class TestSessionCommands:
    def test_new(self, agent, session_id):
        r = handle_command("/new", agent, session_id)
        assert r.action == "continue"
        assert r.new_session_id is not None
        assert r.new_session_id != session_id

    def test_clear(self, agent, session_id):
        agent.sessions.add_message(session_id, "user", "hello")
        r = handle_command("/clear", agent, session_id)
        assert r.action == "continue"
        assert r.new_session_id is not None

    def test_sessions_list(self, agent, session_id):
        r = handle_command("/sessions", agent, session_id)
        assert r.action == "info"
        assert len(r.output_lines) >= 1
        # Current session should be marked with *
        assert any("*" in line for line in r.output_lines)

    def test_sessions_empty(self, tmp_path):
        a = EDSAgent(config={
            "memory": {"sessions_dir": str(tmp_path / "empty_sessions")},
        })
        a._llm_provider = MagicMock()
        a._provider_name = "test"
        r = handle_command("/sessions", a, "nonexistent")
        assert "No sessions" in r.message

    def test_load_existing(self, agent, session_id):
        # Create a second session to load
        s2 = agent.sessions.create_session()
        agent.sessions.add_message(s2.id, "user", "old message")

        r = handle_command(f"/load {s2.id}", agent, session_id)
        assert r.action == "continue"
        assert r.new_session_id == s2.id
        assert "1 messages" in r.message

    def test_load_missing(self, agent, session_id):
        r = handle_command("/load nonexistent", agent, session_id)
        assert r.action == "error"
        assert "not found" in r.message

    def test_load_no_arg(self, agent, session_id):
        r = handle_command("/load", agent, session_id)
        assert r.action == "error"
        assert "Usage" in r.message


class TestHistoryCommand:
    def test_history_empty(self, agent, session_id):
        r = handle_command("/history", agent, session_id)
        assert "No messages" in r.message

    def test_history_with_messages(self, agent, session_id):
        agent.sessions.add_message(session_id, "user", "What is EDS?")
        agent.sessions.add_message(session_id, "assistant", "EDS is a procurement system.")
        r = handle_command("/history", agent, session_id)
        assert r.action == "info"
        assert len(r.output_lines) == 2
        assert "[USER]" in r.output_lines[0]
        assert "[ASSISTANT]" in r.output_lines[1]

    def test_history_with_limit(self, agent, session_id):
        for i in range(10):
            agent.sessions.add_message(session_id, "user", f"msg {i}")
        r = handle_command("/history 3", agent, session_id)
        assert len(r.output_lines) == 3

    def test_history_truncates_long_messages(self, agent, session_id):
        agent.sessions.add_message(session_id, "user", "x" * 200)
        r = handle_command("/history", agent, session_id)
        assert "..." in r.output_lines[0]


class TestStatusCommand:
    def test_status(self, agent, session_id):
        r = handle_command("/status", agent, session_id)
        assert r.action == "info"
        assert any("provider" in line for line in r.output_lines)
        assert any("session" in line for line in r.output_lines)


class TestProviderCommand:
    def test_provider_no_arg(self, agent, session_id):
        r = handle_command("/provider", agent, session_id)
        assert r.action == "error"
        assert "Usage" in r.message

    @patch("agent.core.agent.get_provider")
    def test_provider_switch(self, mock_get, agent, session_id):
        mock_llm = MagicMock()
        mock_llm.model_name = "new-model"
        mock_get.return_value = mock_llm

        r = handle_command("/provider claude", agent, session_id)
        assert r.action == "continue"
        assert "claude" in r.message

    def test_provider_switch_failure(self, agent, session_id):
        with patch.object(agent, "set_provider", side_effect=ValueError("No API key")):
            r = handle_command("/provider claude", agent, session_id)
            assert r.action == "error"
            assert "Failed" in r.message


class TestUnknownCommand:
    def test_unknown(self, agent, session_id):
        r = handle_command("/bogus", agent, session_id)
        assert r.action == "error"
        assert "Unknown" in r.message


class TestCommandResult:
    def test_defaults(self):
        r = CommandResult(action="continue")
        assert r.message == ""
        assert r.new_session_id is None
        assert r.output_lines == []
