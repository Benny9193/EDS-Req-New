"""Tests for the agent chat API routes.

Uses a standalone FastAPI app to avoid importing the full api package
(which requires database dependencies not available in test env).
"""

import json
import pytest
from unittest.mock import MagicMock, patch

from agent.core.agent import AgentResponse


@pytest.fixture
def mock_agent():
    agent = MagicMock()
    agent.chat.return_value = AgentResponse(
        content="Hello! I'm the EDS DBA Agent.",
        tool_calls=[],
        metadata={"model": "test", "provider": "test"},
    )
    agent.chat_stream.return_value = iter(["Hello", "!", " I'm", " the agent."])
    agent.sessions.list_sessions.return_value = []
    agent.sessions.create_session.return_value = MagicMock(
        id="abc12345", mode="chat", provider="test", updated_at="2026-04-01T00:00:00Z",
    )
    agent.sessions.get_session.return_value = MagicMock(
        id="abc12345", mode="chat", provider="test", updated_at="2026-04-01T00:00:00Z",
        messages=[
            MagicMock(role="user", content="hi", timestamp="2026-04-01T00:00:00Z"),
            MagicMock(role="assistant", content="hello", timestamp="2026-04-01T00:00:01Z"),
        ],
    )
    agent.sessions.delete_session.return_value = True
    agent.get_status.return_value = {
        "provider": "test", "model": "test-model", "mode": "chat",
        "tools_loaded": 8, "tools": ["sql_executor"],
    }
    return agent


@pytest.fixture
def client(mock_agent):
    """Create a test client with a standalone FastAPI app + agent router."""
    import importlib.util
    import sys
    from pathlib import Path

    # Load agent_chat module directly to avoid api/routes/__init__.py imports
    mod_path = Path(__file__).parent.parent.parent / "api" / "routes" / "agent_chat.py"
    spec = importlib.util.spec_from_file_location("agent_chat_standalone", mod_path)
    agent_chat_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(agent_chat_module)

    # Inject mock agent
    agent_chat_module._agent = mock_agent
    agent_chat_module._get_agent = lambda: mock_agent

    from fastapi import FastAPI
    from fastapi.testclient import TestClient

    app = FastAPI()
    app.include_router(agent_chat_module.router, prefix="/api")

    yield TestClient(app)


class TestChatEndpoint:
    def test_chat_success(self, client):
        response = client.post("/api/agent/chat", json={
            "message": "Hello",
            "mode": "chat",
        })
        assert response.status_code == 200
        data = response.json()
        assert data["content"] == "Hello! I'm the EDS DBA Agent."

    def test_chat_with_session(self, client, mock_agent):
        response = client.post("/api/agent/chat", json={
            "message": "Hello",
            "session_id": "abc12345",
            "mode": "sql",
        })
        assert response.status_code == 200

    def test_chat_invalid_mode(self, client):
        response = client.post("/api/agent/chat", json={
            "message": "Hello",
            "mode": "invalid_mode",
        })
        assert response.status_code == 200


class TestStreamEndpoint:
    def test_stream_returns_sse(self, client):
        response = client.post("/api/agent/chat/stream", json={
            "message": "Hello",
        })
        assert response.status_code == 200
        assert "text/event-stream" in response.headers["content-type"]

        events = []
        for line in response.text.split("\n"):
            if line.startswith("data: "):
                events.append(json.loads(line[6:]))

        chunk_events = [e for e in events if e.get("type") == "chunk"]
        done_events = [e for e in events if e.get("type") == "done"]
        assert len(chunk_events) > 0
        assert len(done_events) == 1


class TestSessionEndpoints:
    def test_list_sessions(self, client):
        response = client.get("/api/agent/sessions")
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_create_session(self, client):
        response = client.post("/api/agent/sessions", json={"mode": "sql"})
        assert response.status_code == 200
        assert response.json()["id"] == "abc12345"

    def test_get_messages(self, client):
        response = client.get("/api/agent/sessions/abc12345/messages")
        assert response.status_code == 200
        data = response.json()
        assert len(data["messages"]) == 2

    def test_delete_session(self, client):
        response = client.delete("/api/agent/sessions/abc12345")
        assert response.status_code == 200
        assert response.json()["deleted"] is True


class TestStatusEndpoint:
    def test_status(self, client):
        response = client.get("/api/agent/status")
        assert response.status_code == 200
        assert response.json()["tools_loaded"] == 8
