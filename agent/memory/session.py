"""Session management with JSON file persistence.

Each session is stored as an individual JSON file in the sessions directory.
Session IDs are 8-character UUID4 hex strings.
"""

import json
import logging
import os
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from uuid import uuid4

logger = logging.getLogger(__name__)


@dataclass
class SessionMessage:
    """A single message in a session conversation."""

    role: str
    content: str
    timestamp: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    tool_calls: List[Dict] = field(default_factory=list)
    tool_results: List[Dict] = field(default_factory=list)
    tokens: int = 0
    metadata: Dict = field(default_factory=dict)


@dataclass
class Session:
    """A conversation session."""

    id: str
    created_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    updated_at: str = field(default_factory=lambda: datetime.utcnow().isoformat() + "Z")
    messages: List[SessionMessage] = field(default_factory=list)
    metadata: Dict = field(default_factory=dict)
    mode: str = "chat"
    provider: str = "claude"
    model: Optional[str] = None
    total_tokens: int = 0
    summary: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        return d

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Session":
        messages = [SessionMessage(**m) for m in data.pop("messages", [])]
        return cls(messages=messages, **data)


class SessionManager:
    """Manages conversation sessions with JSON file persistence."""

    def __init__(
        self,
        sessions_dir: str = "data/sessions",
        max_sessions: int = 100,
        auto_save: bool = True,
    ):
        self._sessions_dir = Path(sessions_dir)
        self._max_sessions = max_sessions
        self._auto_save = auto_save
        self._cache: Dict[str, Session] = {}

        self._sessions_dir.mkdir(parents=True, exist_ok=True)

    def _session_path(self, session_id: str) -> Path:
        return self._sessions_dir / f"{session_id}.json"

    def create_session(
        self,
        mode: str = "chat",
        provider: str = "claude",
        model: Optional[str] = None,
    ) -> Session:
        """Create a new session with an 8-char UUID hex ID."""
        session_id = uuid4().hex[:8]
        session = Session(
            id=session_id,
            mode=mode,
            provider=provider,
            model=model,
        )
        self._cache[session_id] = session

        if self._auto_save:
            self.save_session(session)

        self._evict_if_needed()
        return session

    def get_session(self, session_id: str) -> Optional[Session]:
        """Load a session from cache or disk."""
        if session_id in self._cache:
            return self._cache[session_id]

        path = self._session_path(session_id)
        if not path.exists():
            return None

        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            session = Session.from_dict(data)
            self._cache[session_id] = session
            return session
        except (json.JSONDecodeError, KeyError, TypeError) as e:
            logger.warning("Failed to load session %s: %s", session_id, e)
            return None

    def add_message(
        self,
        session_id: str,
        role: str,
        content: str,
        **kwargs,
    ) -> Optional[SessionMessage]:
        """Add a message to a session. Returns the message or None if session not found."""
        session = self.get_session(session_id)
        if session is None:
            return None

        msg = SessionMessage(role=role, content=content, **kwargs)
        session.messages.append(msg)
        session.updated_at = datetime.utcnow().isoformat() + "Z"
        session.total_tokens += msg.tokens

        if self._auto_save:
            self.save_session(session)

        return msg

    def save_session(self, session: Session) -> None:
        """Persist a session to disk."""
        path = self._session_path(session.id)
        try:
            with open(path, "w", encoding="utf-8") as f:
                json.dump(session.to_dict(), f, indent=2, default=str)
        except OSError as e:
            logger.error("Failed to save session %s: %s", session.id, e)

    def list_sessions(self, limit: int = 20) -> List[Session]:
        """List sessions sorted by updated_at (most recent first)."""
        sessions = []
        for path in self._sessions_dir.glob("*.json"):
            session_id = path.stem
            session = self.get_session(session_id)
            if session:
                sessions.append(session)

        sessions.sort(key=lambda s: s.updated_at, reverse=True)
        return sessions[:limit]

    def delete_session(self, session_id: str) -> bool:
        """Delete a session from cache and disk."""
        self._cache.pop(session_id, None)
        path = self._session_path(session_id)
        if path.exists():
            try:
                path.unlink()
                return True
            except OSError as e:
                logger.error("Failed to delete session %s: %s", session_id, e)
                return False
        return False

    def get_recent_context(
        self,
        session_id: str,
        n_messages: int = 10,
    ) -> List[SessionMessage]:
        """Get the most recent n messages from a session."""
        session = self.get_session(session_id)
        if session is None:
            return []
        return session.messages[-n_messages:]

    def _evict_if_needed(self) -> None:
        """Evict oldest sessions when max_sessions is exceeded."""
        files = sorted(
            self._sessions_dir.glob("*.json"),
            key=lambda p: p.stat().st_mtime,
        )
        while len(files) > self._max_sessions:
            oldest = files.pop(0)
            session_id = oldest.stem
            self._cache.pop(session_id, None)
            try:
                oldest.unlink()
                logger.debug("Evicted session: %s", session_id)
            except OSError:
                pass
