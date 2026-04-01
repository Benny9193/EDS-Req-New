"""Tests for the memory layer: SessionManager and LearnedContextDB."""

import json
import pytest
from pathlib import Path

from agent.memory.session import Session, SessionManager, SessionMessage
from agent.memory.learned_context import LearnedContextDB


# ── SessionMessage ───────────────────────────────────────────────────


class TestSessionMessage:
    def test_defaults(self):
        msg = SessionMessage(role="user", content="hello")
        assert msg.role == "user"
        assert msg.content == "hello"
        assert msg.timestamp.endswith("Z")
        assert msg.tool_calls == []
        assert msg.tokens == 0

    def test_with_metadata(self):
        msg = SessionMessage(
            role="assistant", content="hi", tokens=50,
            metadata={"model": "test"},
        )
        assert msg.tokens == 50
        assert msg.metadata["model"] == "test"


# ── Session ──────────────────────────────────────────────────────────


class TestSession:
    def test_to_dict_roundtrip(self):
        session = Session(
            id="abc12345",
            mode="sql",
            provider="claude",
            messages=[
                SessionMessage(role="user", content="SELECT 1"),
                SessionMessage(role="assistant", content="Here's the result"),
            ],
        )
        d = session.to_dict()
        restored = Session.from_dict(d)
        assert restored.id == "abc12345"
        assert restored.mode == "sql"
        assert len(restored.messages) == 2
        assert restored.messages[0].content == "SELECT 1"

    def test_defaults(self):
        session = Session(id="test")
        assert session.mode == "chat"
        assert session.provider == "claude"
        assert session.total_tokens == 0
        assert session.summary is None


# ── SessionManager ───────────────────────────────────────────────────


@pytest.fixture
def sessions_dir(tmp_path):
    return tmp_path / "sessions"


@pytest.fixture
def manager(sessions_dir):
    return SessionManager(sessions_dir=str(sessions_dir), max_sessions=5)


class TestSessionManager:
    def test_create_session(self, manager):
        session = manager.create_session(mode="sql", provider="ollama")
        assert len(session.id) == 8
        assert session.mode == "sql"
        assert session.provider == "ollama"

    def test_create_session_persists(self, manager, sessions_dir):
        session = manager.create_session()
        path = sessions_dir / f"{session.id}.json"
        assert path.exists()

    def test_get_session(self, manager):
        session = manager.create_session()
        loaded = manager.get_session(session.id)
        assert loaded is not None
        assert loaded.id == session.id

    def test_get_session_from_disk(self, manager, sessions_dir):
        session = manager.create_session()
        sid = session.id
        # Clear cache to force disk read
        manager._cache.clear()
        loaded = manager.get_session(sid)
        assert loaded is not None
        assert loaded.id == sid

    def test_get_session_missing(self, manager):
        assert manager.get_session("nonexistent") is None

    def test_add_message(self, manager):
        session = manager.create_session()
        msg = manager.add_message(session.id, "user", "Hello!")
        assert msg is not None
        assert msg.role == "user"
        assert msg.content == "Hello!"

        loaded = manager.get_session(session.id)
        assert len(loaded.messages) == 1

    def test_add_message_missing_session(self, manager):
        assert manager.add_message("nonexistent", "user", "hi") is None

    def test_add_message_updates_timestamp(self, manager):
        session = manager.create_session()
        original = session.updated_at
        manager.add_message(session.id, "user", "hello")
        updated = manager.get_session(session.id)
        assert updated.updated_at >= original

    def test_add_message_accumulates_tokens(self, manager):
        session = manager.create_session()
        manager.add_message(session.id, "user", "hello", tokens=10)
        manager.add_message(session.id, "assistant", "hi", tokens=5)
        loaded = manager.get_session(session.id)
        assert loaded.total_tokens == 15

    def test_list_sessions(self, manager):
        s1 = manager.create_session()
        s2 = manager.create_session()
        sessions = manager.list_sessions()
        assert len(sessions) == 2
        # Most recent first
        assert sessions[0].updated_at >= sessions[1].updated_at

    def test_list_sessions_limit(self, manager):
        for _ in range(5):
            manager.create_session()
        sessions = manager.list_sessions(limit=2)
        assert len(sessions) == 2

    def test_delete_session(self, manager, sessions_dir):
        session = manager.create_session()
        sid = session.id
        path = sessions_dir / f"{sid}.json"
        assert path.exists()

        assert manager.delete_session(sid) is True
        assert not path.exists()
        assert manager.get_session(sid) is None

    def test_delete_session_missing(self, manager):
        assert manager.delete_session("nonexistent") is False

    def test_get_recent_context(self, manager):
        session = manager.create_session()
        for i in range(15):
            manager.add_message(session.id, "user", f"message {i}")
        recent = manager.get_recent_context(session.id, n_messages=5)
        assert len(recent) == 5
        assert recent[0].content == "message 10"
        assert recent[-1].content == "message 14"

    def test_get_recent_context_missing_session(self, manager):
        assert manager.get_recent_context("nonexistent") == []

    def test_eviction(self, sessions_dir):
        manager = SessionManager(sessions_dir=str(sessions_dir), max_sessions=3)
        ids = []
        for _ in range(5):
            s = manager.create_session()
            ids.append(s.id)

        # Should have at most 3 files
        files = list(sessions_dir.glob("*.json"))
        assert len(files) <= 3

    def test_save_session_explicit(self, manager, sessions_dir):
        mgr = SessionManager(sessions_dir=str(sessions_dir), auto_save=False)
        session = mgr.create_session()
        # Not auto-saved
        path = sessions_dir / f"{session.id}.json"
        assert not path.exists()

        mgr.save_session(session)
        assert path.exists()


# ── LearnedContextDB ─────────────────────────────────────────────────


@pytest.fixture
def db(tmp_path):
    db_path = tmp_path / "knowledge.sqlite"
    db = LearnedContextDB(db_path=str(db_path))
    yield db
    db.close()


class TestLearnedContextDB:
    # Preferences
    def test_set_and_get_preference(self, db):
        db.set_preference("default_database", "EDS")
        assert db.get_preference("default_database") == "EDS"

    def test_get_preference_missing(self, db):
        assert db.get_preference("nonexistent") is None

    def test_set_preference_upserts(self, db):
        db.set_preference("theme", "dark")
        db.set_preference("theme", "light")
        assert db.get_preference("theme") == "light"

    def test_get_all_preferences(self, db):
        db.set_preference("a", "1")
        db.set_preference("b", "2")
        prefs = db.get_all_preferences()
        assert prefs == {"a": "1", "b": "2"}

    # Query patterns
    def test_record_and_get_patterns(self, db):
        db.record_query_pattern("vendor lookup", query_type="select", example="SELECT * FROM Vendors")
        db.record_query_pattern("vendor lookup")  # increment frequency
        patterns = db.get_frequent_patterns(limit=5)
        assert len(patterns) == 1
        assert patterns[0]["frequency"] == 2

    def test_patterns_ordered_by_frequency(self, db):
        db.record_query_pattern("rare")
        db.record_query_pattern("common")
        db.record_query_pattern("common")
        db.record_query_pattern("common")
        patterns = db.get_frequent_patterns()
        assert patterns[0]["pattern"] == "common"

    # Entity aliases
    def test_add_and_resolve_alias(self, db):
        db.add_entity_alias("SS", "School Specialty", entity_type="vendor")
        assert db.resolve_alias("SS") == "School Specialty"

    def test_resolve_alias_missing(self, db):
        assert db.resolve_alias("unknown") is None

    # Domain knowledge
    def test_add_and_get_knowledge(self, db):
        db.add_domain_knowledge(
            topic="budget_year",
            knowledge="Budget year runs Dec 1 - Nov 30",
            source="CLAUDE.md",
        )
        results = db.get_domain_knowledge("budget_year")
        assert len(results) == 1
        assert "Dec 1" in results[0]["knowledge"]

    def test_get_knowledge_empty(self, db):
        assert db.get_domain_knowledge("nonexistent") == []

    # Summaries
    def test_save_summary(self, db):
        db.save_summary("sess1", "Discussed vendor queries", message_count=10)
        # Verify it was stored (no get method in spec, check via raw SQL)
        row = db._conn.execute(
            "SELECT * FROM conversation_summaries WHERE session_id = ?", ("sess1",)
        ).fetchone()
        assert row is not None
        assert row["summary"] == "Discussed vendor queries"

    # Context for prompt
    def test_get_context_for_prompt_empty(self, db):
        assert db.get_context_for_prompt() == ""

    def test_get_context_for_prompt_with_data(self, db):
        db.set_preference("output_format", "table")
        db.record_query_pattern("vendor totals")
        db.add_entity_alias("WBM", "W.B. Mason")
        context = db.get_context_for_prompt()
        assert "output_format" in context
        assert "vendor totals" in context
        assert "WBM" in context
        assert "W.B. Mason" in context
