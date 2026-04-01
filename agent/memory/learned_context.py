"""Learned context database — SQLite-backed storage for accumulated knowledge.

Stores user preferences, query patterns, entity aliases, domain knowledge,
and conversation summaries that persist across sessions.
"""

import json
import logging
import sqlite3
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)

_SCHEMA_SQL = """
CREATE TABLE IF NOT EXISTS user_preferences (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    key         TEXT NOT NULL UNIQUE,
    value       TEXT NOT NULL,
    confidence  REAL DEFAULT 1.0,
    source      TEXT DEFAULT 'explicit',
    created_at  TEXT DEFAULT (datetime('now')),
    updated_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS query_patterns (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern     TEXT NOT NULL,
    query_type  TEXT,
    frequency   INTEGER DEFAULT 1,
    last_used   TEXT DEFAULT (datetime('now')),
    example     TEXT,
    metadata    TEXT DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS entity_aliases (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    alias       TEXT NOT NULL,
    canonical   TEXT NOT NULL,
    entity_type TEXT,
    confidence  REAL DEFAULT 1.0,
    created_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS domain_knowledge (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    topic       TEXT NOT NULL,
    knowledge   TEXT NOT NULL,
    source      TEXT,
    confidence  REAL DEFAULT 1.0,
    created_at  TEXT DEFAULT (datetime('now')),
    updated_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS conversation_summaries (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id   TEXT NOT NULL,
    summary      TEXT NOT NULL,
    message_count INTEGER DEFAULT 0,
    created_at   TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_preferences_key ON user_preferences(key);
CREATE INDEX IF NOT EXISTS idx_patterns_type   ON query_patterns(query_type);
CREATE INDEX IF NOT EXISTS idx_aliases_alias   ON entity_aliases(alias);
CREATE INDEX IF NOT EXISTS idx_knowledge_topic ON domain_knowledge(topic);
"""


class LearnedContextDB:
    """SQLite-backed learned context that accumulates over time."""

    def __init__(self, db_path: str = "data/memory/knowledge.sqlite"):
        self._db_path = Path(db_path)
        self._db_path.parent.mkdir(parents=True, exist_ok=True)
        self._conn = sqlite3.connect(str(self._db_path))
        self._conn.row_factory = sqlite3.Row
        self._init_schema()

    def _init_schema(self) -> None:
        self._conn.executescript(_SCHEMA_SQL)
        self._conn.commit()

    def close(self) -> None:
        self._conn.close()

    # ── User Preferences ─────────────────────────────────────────────

    def set_preference(
        self,
        key: str,
        value: str,
        confidence: float = 1.0,
        source: str = "explicit",
    ) -> None:
        self._conn.execute(
            """INSERT INTO user_preferences (key, value, confidence, source)
               VALUES (?, ?, ?, ?)
               ON CONFLICT(key) DO UPDATE SET
                   value = excluded.value,
                   confidence = excluded.confidence,
                   source = excluded.source,
                   updated_at = datetime('now')""",
            (key, value, confidence, source),
        )
        self._conn.commit()

    def get_preference(self, key: str) -> Optional[str]:
        row = self._conn.execute(
            "SELECT value FROM user_preferences WHERE key = ?", (key,)
        ).fetchone()
        return row["value"] if row else None

    def get_all_preferences(self) -> Dict[str, str]:
        rows = self._conn.execute(
            "SELECT key, value FROM user_preferences ORDER BY key"
        ).fetchall()
        return {row["key"]: row["value"] for row in rows}

    # ── Query Patterns ───────────────────────────────────────────────

    def record_query_pattern(
        self,
        pattern: str,
        query_type: Optional[str] = None,
        example: Optional[str] = None,
    ) -> None:
        existing = self._conn.execute(
            "SELECT id, frequency FROM query_patterns WHERE pattern = ?",
            (pattern,),
        ).fetchone()

        if existing:
            self._conn.execute(
                """UPDATE query_patterns
                   SET frequency = frequency + 1,
                       last_used = datetime('now'),
                       example = COALESCE(?, example)
                   WHERE id = ?""",
                (example, existing["id"]),
            )
        else:
            self._conn.execute(
                """INSERT INTO query_patterns (pattern, query_type, example)
                   VALUES (?, ?, ?)""",
                (pattern, query_type, example),
            )
        self._conn.commit()

    def get_frequent_patterns(self, limit: int = 10) -> List[Dict]:
        rows = self._conn.execute(
            """SELECT pattern, query_type, frequency, last_used, example
               FROM query_patterns ORDER BY frequency DESC LIMIT ?""",
            (limit,),
        ).fetchall()
        return [dict(row) for row in rows]

    # ── Entity Aliases ───────────────────────────────────────────────

    def add_entity_alias(
        self,
        alias: str,
        canonical: str,
        entity_type: Optional[str] = None,
    ) -> None:
        self._conn.execute(
            """INSERT OR REPLACE INTO entity_aliases (alias, canonical, entity_type)
               VALUES (?, ?, ?)""",
            (alias, canonical, entity_type),
        )
        self._conn.commit()

    def resolve_alias(self, alias: str) -> Optional[str]:
        row = self._conn.execute(
            "SELECT canonical FROM entity_aliases WHERE alias = ? ORDER BY confidence DESC LIMIT 1",
            (alias,),
        ).fetchone()
        return row["canonical"] if row else None

    # ── Domain Knowledge ─────────────────────────────────────────────

    def add_domain_knowledge(
        self,
        topic: str,
        knowledge: str,
        source: Optional[str] = None,
    ) -> None:
        self._conn.execute(
            """INSERT INTO domain_knowledge (topic, knowledge, source)
               VALUES (?, ?, ?)""",
            (topic, knowledge, source),
        )
        self._conn.commit()

    def get_domain_knowledge(self, topic: str) -> List[Dict]:
        rows = self._conn.execute(
            """SELECT topic, knowledge, source, confidence, created_at
               FROM domain_knowledge WHERE topic = ? ORDER BY confidence DESC""",
            (topic,),
        ).fetchall()
        return [dict(row) for row in rows]

    # ── Conversation Summaries ───────────────────────────────────────

    def save_summary(
        self,
        session_id: str,
        summary: str,
        message_count: int = 0,
    ) -> None:
        self._conn.execute(
            """INSERT INTO conversation_summaries (session_id, summary, message_count)
               VALUES (?, ?, ?)""",
            (session_id, summary, message_count),
        )
        self._conn.commit()

    # ── Context for Prompt ───────────────────────────────────────────

    def get_context_for_prompt(self) -> str:
        """Build a context string from learned knowledge for injection into prompts."""
        parts = []

        # User preferences
        prefs = self.get_all_preferences()
        if prefs:
            pref_lines = [f"- {k}: {v}" for k, v in prefs.items()]
            parts.append("User preferences:\n" + "\n".join(pref_lines))

        # Frequent patterns
        patterns = self.get_frequent_patterns(limit=5)
        if patterns:
            pattern_lines = [
                f"- {p['pattern']} (used {p['frequency']}x)"
                for p in patterns
            ]
            parts.append("Frequent query patterns:\n" + "\n".join(pattern_lines))

        # Entity aliases
        rows = self._conn.execute(
            "SELECT alias, canonical FROM entity_aliases ORDER BY confidence DESC LIMIT 10"
        ).fetchall()
        if rows:
            alias_lines = [f"- {r['alias']} → {r['canonical']}" for r in rows]
            parts.append("Known aliases:\n" + "\n".join(alias_lines))

        return "\n\n".join(parts) if parts else ""
