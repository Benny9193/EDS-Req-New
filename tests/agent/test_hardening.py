"""Tests for bug fixes and hardening: DB connection errors, config mismatches, SQL params."""

import pytest
from unittest.mock import MagicMock, patch

from agent.tools.db_connection import DatabaseConnectionError, get_connection, build_connection_string


# ── DB Connection Helper ─────────────────────────────────────────────


class TestDBConnection:
    def test_build_connection_string(self):
        with patch.dict("os.environ", {
            "DB_SERVER": "myserver",
            "DB_USERNAME": "user",
            "DB_PASSWORD": "pass",
        }):
            cs = build_connection_string("EDS", timeout=15)
            assert "myserver" in cs
            assert "EDS" in cs
            assert "user" in cs
            assert "Connection Timeout=15" in cs

    def test_build_connection_string_defaults(self):
        with patch.dict("os.environ", {}, clear=True):
            cs = build_connection_string()
            assert "localhost" in cs
            assert "EDS" in cs

    @patch("agent.tools.db_connection.pyodbc")
    def test_get_connection_success(self, mock_pyodbc):
        mock_conn = MagicMock()
        mock_pyodbc.connect.return_value = mock_conn

        with get_connection("EDS") as conn:
            assert conn is mock_conn

    @patch("agent.tools.db_connection.pyodbc")
    def test_get_connection_login_failed(self, mock_pyodbc):
        mock_pyodbc.OperationalError = type("OperationalError", (Exception,), {})
        mock_pyodbc.InterfaceError = type("InterfaceError", (Exception,), {})
        mock_pyodbc.connect.side_effect = mock_pyodbc.OperationalError(
            "Login failed for user 'bad'"
        )

        with pytest.raises(DatabaseConnectionError, match="authentication failed"):
            with get_connection("EDS"):
                pass

    @patch("agent.tools.db_connection.pyodbc")
    def test_get_connection_server_unreachable(self, mock_pyodbc):
        mock_pyodbc.OperationalError = type("OperationalError", (Exception,), {})
        mock_pyodbc.InterfaceError = type("InterfaceError", (Exception,), {})
        mock_pyodbc.connect.side_effect = mock_pyodbc.OperationalError(
            "TCP Provider: server was not found"
        )

        with pytest.raises(DatabaseConnectionError, match="Cannot reach"):
            with get_connection("EDS"):
                pass

    @patch("agent.tools.db_connection.pyodbc")
    def test_get_connection_driver_missing(self, mock_pyodbc):
        mock_pyodbc.OperationalError = type("OperationalError", (Exception,), {})
        mock_pyodbc.InterfaceError = type("InterfaceError", (Exception,), {})
        mock_pyodbc.connect.side_effect = mock_pyodbc.OperationalError(
            "ODBC Driver 17 not found"
        )

        with pytest.raises(DatabaseConnectionError, match="ODBC Driver"):
            with get_connection("EDS"):
                pass


# ── SQL Executor config fix ──────────────────────────────────────────


class TestSQLExecutorConfig:
    def test_default_allows_writes(self):
        """Default config (no explicit read_only_mode) should allow writes."""
        from agent.tools.sql_executor import create_sql_tools
        tools = create_sql_tools({})
        tool = tools[0]
        # With default read_only_mode=false, writes should be allowed
        assert tool._validator.allow_writes is True

    def test_read_only_mode_true_blocks_writes(self):
        from agent.tools.sql_executor import create_sql_tools
        tools = create_sql_tools({"security": {"read_only_mode": True}})
        tool = tools[0]
        assert tool._validator.allow_writes is False

    def test_read_only_mode_false_allows_writes(self):
        from agent.tools.sql_executor import create_sql_tools
        tools = create_sql_tools({"security": {"read_only_mode": False}})
        tool = tools[0]
        assert tool._validator.allow_writes is True


# ── Catalog Search params fix ────────────────────────────────────────


class TestCatalogSearchParams:
    def test_queries_use_positional_params(self):
        from agent.tools.catalog_search import _SEARCH_QUERIES
        for name, sql in _SEARCH_QUERIES.items():
            assert "@" not in sql, f"{name} query still uses named params"
            assert "?" in sql, f"{name} query missing ? placeholders"

    def test_param_count_matches_placeholders(self):
        from agent.tools.catalog_search import _SEARCH_QUERIES, _SEARCH_PARAM_COUNTS
        for name, sql in _SEARCH_QUERIES.items():
            n_placeholders = sql.count("?")
            expected = 1 + _SEARCH_PARAM_COUNTS[name]  # limit + search terms
            assert n_placeholders == expected, (
                f"{name}: {n_placeholders} placeholders but expected {expected}"
            )

    @patch("agent.tools.catalog_search.CatalogSearchTool._run_search")
    def test_vendor_search_passes_params(self, mock_run):
        mock_run.return_value = (
            [(9, "0009", "School Specialty")],
            ["VendorId", "VendorCode", "VendorName"],
        )
        from agent.tools.catalog_search import CatalogSearchTool
        tool = CatalogSearchTool()
        result = tool.execute(search_term="School", catalog="vendors", limit=5)
        assert result.success
        # Verify params passed correctly
        mock_run.assert_called_once_with("vendors", "School", 5)


# ── Error message quality ────────────────────────────────────────────


class TestErrorMessages:
    def test_sql_executor_db_error_friendly(self):
        from agent.tools.sql_executor import SQLExecutorTool

        tool = SQLExecutorTool()
        with patch.object(tool, "_run_query", side_effect=DatabaseConnectionError(
            "Cannot reach database server 'myserver'"
        )):
            result = tool.execute(query="SELECT 1")
            assert not result.success
            assert "Cannot reach" in result.error

    def test_schema_introspector_db_error_friendly(self):
        from agent.tools.schema_introspector import SchemaIntrospectorTool

        tool = SchemaIntrospectorTool()
        with patch.object(tool, "_run_query", side_effect=DatabaseConnectionError(
            "Database authentication failed"
        )):
            result = tool.execute(query_type="tables")
            assert not result.success
            assert "authentication" in result.error.lower()
