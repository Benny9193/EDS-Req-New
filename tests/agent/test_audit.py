"""Tests for the JSONL audit logger."""

import gzip
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch

import pytest

from agent.audit.logger import (
    AuditEvent,
    AuditEventType,
    AuditLogger,
    get_audit_logger,
    reset_audit_logger,
)


@pytest.fixture
def log_dir(tmp_path):
    return tmp_path / "audit"


@pytest.fixture
def audit_logger(log_dir):
    logger = AuditLogger(log_dir=str(log_dir), retention_days=30, enabled=True)
    yield logger
    logger.close()


@pytest.fixture(autouse=True)
def clean_global():
    reset_audit_logger()
    yield
    reset_audit_logger()


# ── AuditEvent ───────────────────────────────────────────────────────


class TestAuditEvent:
    def test_to_dict(self):
        event = AuditEvent(
            event_type=AuditEventType.QUERY_EXECUTED,
            session_id="abc123",
            data={"sql": "SELECT 1"},
        )
        d = event.to_dict()
        assert d["event_type"] == "query_executed"
        assert d["session_id"] == "abc123"
        assert d["data"]["sql"] == "SELECT 1"
        assert d["timestamp"].endswith("Z")

    def test_to_json(self):
        event = AuditEvent(
            event_type=AuditEventType.TOOL_CALLED,
            data={"tool_name": "sql_executor"},
        )
        j = event.to_json()
        parsed = json.loads(j)
        assert parsed["event_type"] == "tool_called"

    def test_default_timestamp(self):
        event = AuditEvent(event_type=AuditEventType.ERROR)
        assert isinstance(event.timestamp, datetime)

    def test_all_event_types_have_values(self):
        assert len(AuditEventType) == 13


# ── AuditLogger basics ──────────────────────────────────────────────


class TestAuditLoggerBasics:
    def test_creates_log_dir(self, log_dir):
        AuditLogger(log_dir=str(log_dir), enabled=True)
        assert log_dir.exists()

    def test_disabled_logger_does_nothing(self, log_dir):
        logger = AuditLogger(log_dir=str(log_dir), enabled=False)
        logger.log_event(AuditEvent(event_type=AuditEventType.ERROR))
        # No files should be created
        assert not log_dir.exists()

    def test_enable_disable(self, audit_logger):
        assert audit_logger.enabled is True
        audit_logger.enabled = False
        assert audit_logger.enabled is False

    def test_log_event_writes_jsonl(self, audit_logger, log_dir):
        audit_logger.log_event(AuditEvent(
            event_type=AuditEventType.QUERY_EXECUTED,
            data={"sql": "SELECT 1"},
        ))
        files = list(log_dir.glob("audit_*.jsonl"))
        assert len(files) == 1
        content = files[0].read_text()
        lines = content.strip().split("\n")
        assert len(lines) == 1
        parsed = json.loads(lines[0])
        assert parsed["event_type"] == "query_executed"
        assert parsed["data"]["sql"] == "SELECT 1"

    def test_multiple_events_append(self, audit_logger, log_dir):
        for i in range(5):
            audit_logger.log_event(AuditEvent(
                event_type=AuditEventType.TOOL_CALLED,
                data={"tool_name": f"tool_{i}"},
            ))
        files = list(log_dir.glob("audit_*.jsonl"))
        assert len(files) == 1
        lines = files[0].read_text().strip().split("\n")
        assert len(lines) == 5


# ── Convenience methods ──────────────────────────────────────────────


class TestConvenienceMethods:
    def _read_last_event(self, log_dir):
        files = list(log_dir.glob("audit_*.jsonl"))
        assert len(files) >= 1
        lines = files[0].read_text().strip().split("\n")
        return json.loads(lines[-1])

    def test_log_query(self, audit_logger, log_dir):
        audit_logger.log_query(
            sql="SELECT VendorName FROM Vendors",
            session_id="s1",
            result_count=10,
            duration_ms=42.5,
        )
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "query_executed"
        assert event["session_id"] == "s1"
        assert event["data"]["sql"] == "SELECT VendorName FROM Vendors"
        assert event["metadata"]["result_count"] == 10
        assert event["metadata"]["duration_ms"] == 42.5

    def test_log_blocked_query(self, audit_logger, log_dir):
        audit_logger.log_blocked_query(
            sql="DROP TABLE Vendors",
            reason="Write operation blocked",
            session_id="s2",
        )
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "query_blocked"
        assert "DROP TABLE" in event["data"]["sql"]

    def test_log_tool_call_success(self, audit_logger, log_dir):
        audit_logger.log_tool_call(
            tool_name="sql_executor",
            params={"query": "SELECT 1"},
            success=True,
            duration_ms=15.0,
        )
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "tool_called"

    def test_log_tool_call_failure(self, audit_logger, log_dir):
        audit_logger.log_tool_call(
            tool_name="sql_executor",
            params={"query": "BAD SQL"},
            success=False,
            error="Syntax error",
        )
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "tool_failed"
        assert event["data"]["error"] == "Syntax error"

    def test_log_session_start(self, audit_logger, log_dir):
        audit_logger.log_session_start("s3", "claude", "chat")
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "session_started"
        assert event["data"]["provider"] == "claude"

    def test_log_session_end(self, audit_logger, log_dir):
        audit_logger.log_session_end("s3", message_count=20, total_tokens=5000)
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "session_ended"
        assert event["data"]["message_count"] == 20

    def test_log_llm_call(self, audit_logger, log_dir):
        audit_logger.log_llm_call(
            provider="claude",
            model="claude-sonnet-4-20250514",
            tokens_in=500,
            tokens_out=200,
            duration_ms=1234.5,
        )
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "llm_called"
        assert event["data"]["tokens_in"] == 500
        assert event["metadata"]["duration_ms"] == 1234.5

    def test_log_error(self, audit_logger, log_dir):
        audit_logger.log_error("Connection timeout", context={"host": "db-server"})
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "error"
        assert event["data"]["context"]["host"] == "db-server"

    def test_log_security_alert(self, audit_logger, log_dir):
        audit_logger.log_security_alert(
            alert_type="blocked_pattern",
            details={"pattern": "xp_cmdshell", "query": "EXEC xp_cmdshell 'dir'"},
        )
        event = self._read_last_event(log_dir)
        assert event["event_type"] == "security_alert"
        assert event["data"]["alert_type"] == "blocked_pattern"


# ── Retention cleanup ────────────────────────────────────────────────


class TestRetention:
    def test_cleanup_deletes_old_files(self, log_dir):
        log_dir.mkdir(parents=True, exist_ok=True)
        # Create a file "from 100 days ago"
        old_date = (datetime.utcnow() - timedelta(days=100)).strftime("%Y-%m-%d")
        old_file = log_dir / f"audit_{old_date}.jsonl"
        old_file.write_text('{"event": "old"}\n')

        # Create a file "from today"
        today = datetime.utcnow().strftime("%Y-%m-%d")
        new_file = log_dir / f"audit_{today}.jsonl"
        new_file.write_text('{"event": "new"}\n')

        logger = AuditLogger(log_dir=str(log_dir), retention_days=30)
        deleted = logger.cleanup_old_logs()

        assert deleted == 1
        assert not old_file.exists()
        assert new_file.exists()

    def test_cleanup_deletes_old_gz_files(self, log_dir):
        log_dir.mkdir(parents=True, exist_ok=True)
        old_date = (datetime.utcnow() - timedelta(days=100)).strftime("%Y-%m-%d")
        old_gz = log_dir / f"audit_{old_date}.jsonl.gz"
        with gzip.open(old_gz, "wb") as f:
            f.write(b'{"event": "old"}\n')

        logger = AuditLogger(log_dir=str(log_dir), retention_days=30)
        deleted = logger.cleanup_old_logs()
        assert deleted == 1
        assert not old_gz.exists()

    def test_cleanup_keeps_recent_files(self, log_dir):
        log_dir.mkdir(parents=True, exist_ok=True)
        recent_date = (datetime.utcnow() - timedelta(days=5)).strftime("%Y-%m-%d")
        recent_file = log_dir / f"audit_{recent_date}.jsonl"
        recent_file.write_text('{"event": "recent"}\n')

        logger = AuditLogger(log_dir=str(log_dir), retention_days=30)
        deleted = logger.cleanup_old_logs()
        assert deleted == 0
        assert recent_file.exists()


# ── Rotation / compression ───────────────────────────────────────────


class TestRotation:
    def test_rotation_compresses_previous_day(self, log_dir):
        log_dir.mkdir(parents=True, exist_ok=True)

        # Simulate logging on "yesterday"
        yesterday = (datetime.utcnow() - timedelta(days=1)).strftime("%Y-%m-%d")
        logger = AuditLogger(log_dir=str(log_dir))
        logger._current_date = yesterday
        yesterday_file = log_dir / f"audit_{yesterday}.jsonl"
        yesterday_file.write_text('{"event": "yesterday"}\n')

        # Open a new file for today — should trigger compression of yesterday
        logger._ensure_file()
        logger.close()

        gz_file = log_dir / f"audit_{yesterday}.jsonl.gz"
        assert gz_file.exists()
        assert not yesterday_file.exists()

        # Verify compressed content
        with gzip.open(gz_file, "rt") as f:
            content = f.read()
        assert "yesterday" in content


# ── Global singleton ─────────────────────────────────────────────────


class TestGlobalLogger:
    def test_get_audit_logger_default(self):
        logger = get_audit_logger()
        assert isinstance(logger, AuditLogger)
        assert logger.enabled is True

    def test_get_audit_logger_with_config(self):
        logger = get_audit_logger({
            "audit": {
                "enabled": False,
                "retention_days": 60,
            }
        })
        assert logger.enabled is False

    def test_get_audit_logger_singleton(self):
        l1 = get_audit_logger()
        l2 = get_audit_logger()
        assert l1 is l2

    def test_reset_audit_logger(self):
        l1 = get_audit_logger()
        reset_audit_logger()
        l2 = get_audit_logger()
        assert l1 is not l2
