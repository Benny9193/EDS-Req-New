"""
Tests for database utilities.
"""

import pytest
from unittest.mock import Mock, patch, MagicMock


class TestDatabaseConnection:
    """Tests for DatabaseConnection class."""

    def test_init_defaults(self, mock_db_credentials):
        """Test initialization with default values."""
        from db_utils import DatabaseConnection

        db = DatabaseConnection()

        # Fixture sets DB_DATABASE='test_db', so that's expected
        assert db.database == 'test_db'
        assert db.server == 'test-server.local'
        assert db.username == 'test_user'
        assert db.timeout == 30

    def test_init_custom_values(self, mock_db_credentials):
        """Test initialization with custom values."""
        from db_utils import DatabaseConnection

        db = DatabaseConnection(
            database='custom_db',
            timeout=60
        )

        assert db.database == 'custom_db'
        assert db.timeout == 60

    def test_is_connected_false_initially(self, mock_db_credentials):
        """Test is_connected returns False before connect."""
        from db_utils import DatabaseConnection

        db = DatabaseConnection()
        assert db.is_connected is False

    def test_validate_credentials_missing_server(self, monkeypatch):
        """Test validation fails with missing server."""
        from db_utils import DatabaseConnection, DatabaseConnectionError

        monkeypatch.delenv('DB_SERVER', raising=False)
        monkeypatch.setenv('DB_USERNAME', 'user')
        monkeypatch.setenv('DB_PASSWORD', 'pass')

        db = DatabaseConnection()

        with pytest.raises(DatabaseConnectionError, match="Missing database credentials"):
            db._validate_credentials()

    def test_validate_credentials_missing_username(self, monkeypatch):
        """Test validation fails with missing username."""
        from db_utils import DatabaseConnection, DatabaseConnectionError

        monkeypatch.setenv('DB_SERVER', 'server')
        monkeypatch.delenv('DB_USERNAME', raising=False)
        monkeypatch.setenv('DB_PASSWORD', 'pass')

        db = DatabaseConnection()

        with pytest.raises(DatabaseConnectionError, match="Missing database credentials"):
            db._validate_credentials()

    def test_context_manager(self, mock_db_credentials):
        """Test context manager enters and exits properly."""
        from db_utils import DatabaseConnection

        with patch('db_utils.pyodbc') as mock_pyodbc:
            mock_pyodbc.drivers.return_value = ['ODBC Driver 17 for SQL Server']
            mock_conn = MagicMock()
            mock_pyodbc.connect.return_value = mock_conn

            with DatabaseConnection() as db:
                assert db.is_connected is True

            mock_conn.close.assert_called_once()

    def test_execute_query_not_connected(self, mock_db_credentials):
        """Test execute_query raises when not connected."""
        from db_utils import DatabaseConnection, DatabaseQueryError

        db = DatabaseConnection()

        with pytest.raises(DatabaseQueryError, match="Not connected"):
            db.execute_query("SELECT 1")

    @patch('db_utils.pyodbc')
    def test_execute_query_with_params(self, mock_pyodbc, mock_db_credentials):
        """Test execute_query with parameters."""
        from db_utils import DatabaseConnection

        mock_pyodbc.drivers.return_value = ['ODBC Driver 17 for SQL Server']
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1, 'test')]
        mock_conn.cursor.return_value = mock_cursor
        mock_pyodbc.connect.return_value = mock_conn

        with DatabaseConnection() as db:
            results = db.execute_query(
                "SELECT * FROM table WHERE id = ?",
                params=(123,)
            )

        mock_cursor.execute.assert_called_once_with(
            "SELECT * FROM table WHERE id = ?",
            (123,)
        )
        assert results == [(1, 'test')]

    @patch('db_utils.pyodbc')
    def test_fetch_one(self, mock_pyodbc, mock_db_credentials):
        """Test fetch_one returns single row."""
        from db_utils import DatabaseConnection

        mock_pyodbc.drivers.return_value = ['ODBC Driver 17 for SQL Server']
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (1, 'test')
        mock_conn.cursor.return_value = mock_cursor
        mock_pyodbc.connect.return_value = mock_conn

        with DatabaseConnection() as db:
            result = db.fetch_one("SELECT TOP 1 * FROM table")

        assert result == (1, 'test')
        mock_cursor.close.assert_called_once()

    @patch('db_utils.pyodbc')
    def test_fetch_scalar(self, mock_pyodbc, mock_db_credentials):
        """Test fetch_scalar returns single value."""
        from db_utils import DatabaseConnection

        mock_pyodbc.drivers.return_value = ['ODBC Driver 17 for SQL Server']
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = (42,)
        mock_conn.cursor.return_value = mock_cursor
        mock_pyodbc.connect.return_value = mock_conn

        with DatabaseConnection() as db:
            result = db.fetch_scalar("SELECT COUNT(*) FROM table")

        assert result == 42

    @patch('db_utils.pyodbc')
    def test_fetch_scalar_returns_none(self, mock_pyodbc, mock_db_credentials):
        """Test fetch_scalar returns None when no results."""
        from db_utils import DatabaseConnection

        mock_pyodbc.drivers.return_value = ['ODBC Driver 17 for SQL Server']
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchone.return_value = None
        mock_conn.cursor.return_value = mock_cursor
        mock_pyodbc.connect.return_value = mock_conn

        with DatabaseConnection() as db:
            result = db.fetch_scalar("SELECT id FROM table WHERE 1=0")

        assert result is None


class TestConvenienceFunctions:
    """Tests for convenience functions."""

    @patch('db_utils.pyodbc')
    def test_execute_query_function(self, mock_pyodbc, mock_db_credentials):
        """Test execute_query convenience function."""
        from db_utils import execute_query

        mock_pyodbc.drivers.return_value = ['ODBC Driver 17 for SQL Server']
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [(1,)]
        mock_conn.cursor.return_value = mock_cursor
        mock_pyodbc.connect.return_value = mock_conn

        results = execute_query("SELECT 1")

        assert results == [(1,)]
        mock_conn.close.assert_called_once()


class TestDatabaseErrors:
    """Tests for database error handling."""

    def test_database_connection_error_message(self):
        """Test DatabaseConnectionError has proper message."""
        from db_utils import DatabaseConnectionError

        error = DatabaseConnectionError("Connection failed")
        assert str(error) == "Connection failed"

    def test_database_query_error_message(self):
        """Test DatabaseQueryError has proper message."""
        from db_utils import DatabaseQueryError

        error = DatabaseQueryError("Query failed")
        assert str(error) == "Query failed"
