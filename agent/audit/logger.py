"""Thread-safe JSONL audit logger with daily rotation and retention.

All agent actions (queries, tool calls, LLM calls, security events) are
logged as newline-delimited JSON to daily files in the audit log directory.
Rotated files are compressed with gzip.
"""

import gzip
import json
import logging
import os
import threading
from dataclasses import asdict, dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class AuditEventType(str, Enum):
    QUERY_EXECUTED = "query_executed"
    QUERY_BLOCKED = "query_blocked"
    QUERY_FAILED = "query_failed"
    TOOL_CALLED = "tool_called"
    TOOL_FAILED = "tool_failed"
    SESSION_STARTED = "session_started"
    SESSION_ENDED = "session_ended"
    CONFIG_CHANGED = "config_changed"
    ERROR = "error"
    SECURITY_ALERT = "security_alert"
    LLM_CALLED = "llm_called"
    LLM_FAILED = "llm_failed"
    REPORT_GENERATED = "report_generated"


@dataclass
class AuditEvent:
    event_type: AuditEventType
    timestamp: datetime = field(default_factory=datetime.utcnow)
    session_id: Optional[str] = None
    data: Dict = field(default_factory=dict)
    metadata: Dict = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        d["event_type"] = self.event_type.value
        d["timestamp"] = self.timestamp.isoformat() + "Z"
        return d

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), default=str)


class AuditLogger:
    """Thread-safe JSONL audit logger with daily rotation and gzip compression."""

    def __init__(
        self,
        log_dir: str = "data/audit",
        retention_days: int = 90,
        enabled: bool = True,
    ):
        self._log_dir = Path(log_dir)
        self._retention_days = retention_days
        self._enabled = enabled
        self._lock = threading.Lock()
        self._current_date: Optional[str] = None
        self._file = None

        if self._enabled:
            self._log_dir.mkdir(parents=True, exist_ok=True)

    @property
    def enabled(self) -> bool:
        return self._enabled

    @enabled.setter
    def enabled(self, value: bool) -> None:
        self._enabled = value
        if not value:
            self._close_file()

    def _get_log_filename(self, date_str: str) -> Path:
        return self._log_dir / f"audit_{date_str}.jsonl"

    def _ensure_file(self) -> None:
        """Open or rotate the log file for today's date."""
        today = datetime.utcnow().strftime("%Y-%m-%d")
        if self._current_date != today:
            self._close_file()
            self._compress_old_file()
            self._current_date = today
            filepath = self._get_log_filename(today)
            self._file = open(filepath, "a", encoding="utf-8")

    def _close_file(self) -> None:
        if self._file:
            self._file.close()
            self._file = None

    def _compress_old_file(self) -> None:
        """Compress yesterday's log file if it exists and isn't compressed."""
        if not self._current_date:
            return
        old_path = self._get_log_filename(self._current_date)
        gz_path = old_path.with_suffix(".jsonl.gz")
        if old_path.exists() and not gz_path.exists():
            try:
                with open(old_path, "rb") as f_in:
                    with gzip.open(gz_path, "wb") as f_out:
                        f_out.write(f_in.read())
                old_path.unlink()
                logger.debug("Compressed audit log: %s", gz_path)
            except Exception as e:
                logger.warning("Failed to compress audit log: %s", e)

    def log_event(self, event: AuditEvent) -> None:
        """Write an audit event to the log file."""
        if not self._enabled:
            return

        with self._lock:
            try:
                self._ensure_file()
                self._file.write(event.to_json() + "\n")
                self._file.flush()
            except Exception as e:
                logger.error("Failed to write audit event: %s", e)

    def cleanup_old_logs(self) -> int:
        """Delete log files older than retention_days. Returns count of deleted files."""
        if not self._enabled:
            return 0

        cutoff = datetime.utcnow() - timedelta(days=self._retention_days)
        deleted = 0

        for path in self._log_dir.glob("audit_*"):
            try:
                # Extract date from filename: audit_YYYY-MM-DD.jsonl[.gz]
                name = path.stem
                if name.endswith(".jsonl"):
                    name = name[:-6]  # strip .jsonl from .jsonl.gz case
                date_str = name.replace("audit_", "")
                file_date = datetime.strptime(date_str, "%Y-%m-%d")
                if file_date < cutoff:
                    path.unlink()
                    deleted += 1
                    logger.debug("Deleted old audit log: %s", path)
            except (ValueError, OSError) as e:
                logger.debug("Skipping file %s: %s", path, e)

        return deleted

    def close(self) -> None:
        """Close the logger and release resources."""
        with self._lock:
            self._close_file()

    # ── Convenience methods ──────────────────────────────────────────

    def log_query(
        self,
        sql: str,
        session_id: Optional[str] = None,
        result_count: Optional[int] = None,
        duration_ms: Optional[float] = None,
    ) -> None:
        data = {"sql": sql}
        metadata = {}
        if result_count is not None:
            metadata["result_count"] = result_count
        if duration_ms is not None:
            metadata["duration_ms"] = duration_ms
        self.log_event(AuditEvent(
            event_type=AuditEventType.QUERY_EXECUTED,
            session_id=session_id,
            data=data,
            metadata=metadata,
        ))

    def log_blocked_query(
        self,
        sql: str,
        reason: str,
        session_id: Optional[str] = None,
    ) -> None:
        self.log_event(AuditEvent(
            event_type=AuditEventType.QUERY_BLOCKED,
            session_id=session_id,
            data={"sql": sql, "reason": reason},
        ))

    def log_tool_call(
        self,
        tool_name: str,
        params: Dict,
        session_id: Optional[str] = None,
        success: bool = True,
        error: Optional[str] = None,
        duration_ms: Optional[float] = None,
    ) -> None:
        event_type = AuditEventType.TOOL_CALLED if success else AuditEventType.TOOL_FAILED
        data = {"tool_name": tool_name, "params": params}
        metadata = {}
        if error:
            data["error"] = error
        if duration_ms is not None:
            metadata["duration_ms"] = duration_ms
        self.log_event(AuditEvent(
            event_type=event_type,
            session_id=session_id,
            data=data,
            metadata=metadata,
        ))

    def log_session_start(
        self,
        session_id: str,
        provider: str,
        mode: str,
    ) -> None:
        self.log_event(AuditEvent(
            event_type=AuditEventType.SESSION_STARTED,
            session_id=session_id,
            data={"provider": provider, "mode": mode},
        ))

    def log_session_end(
        self,
        session_id: str,
        message_count: int,
        total_tokens: int,
    ) -> None:
        self.log_event(AuditEvent(
            event_type=AuditEventType.SESSION_ENDED,
            session_id=session_id,
            data={"message_count": message_count, "total_tokens": total_tokens},
        ))

    def log_llm_call(
        self,
        provider: str,
        model: str,
        tokens_in: int,
        tokens_out: int,
        duration_ms: float,
        session_id: Optional[str] = None,
    ) -> None:
        self.log_event(AuditEvent(
            event_type=AuditEventType.LLM_CALLED,
            session_id=session_id,
            data={
                "provider": provider,
                "model": model,
                "tokens_in": tokens_in,
                "tokens_out": tokens_out,
            },
            metadata={"duration_ms": duration_ms},
        ))

    def log_error(
        self,
        error: str,
        context: Optional[Dict] = None,
        session_id: Optional[str] = None,
    ) -> None:
        self.log_event(AuditEvent(
            event_type=AuditEventType.ERROR,
            session_id=session_id,
            data={"error": error, "context": context or {}},
        ))

    def log_security_alert(
        self,
        alert_type: str,
        details: Dict,
        session_id: Optional[str] = None,
    ) -> None:
        self.log_event(AuditEvent(
            event_type=AuditEventType.SECURITY_ALERT,
            session_id=session_id,
            data={"alert_type": alert_type, "details": details},
        ))


# ── Module-level singleton ───────────────────────────────────────────

_global_logger: Optional[AuditLogger] = None


def get_audit_logger(config: Optional[Dict[str, Any]] = None) -> AuditLogger:
    """Get or create the global audit logger."""
    global _global_logger
    if _global_logger is None:
        config = config or {}
        audit_config = config.get("audit", {})
        _global_logger = AuditLogger(
            log_dir=audit_config.get("log_dir", "data/audit"),
            retention_days=audit_config.get("retention_days", 90),
            enabled=audit_config.get("enabled", True),
        )
    return _global_logger


def reset_audit_logger() -> None:
    """Reset the global logger (for testing)."""
    global _global_logger
    if _global_logger:
        _global_logger.close()
    _global_logger = None
