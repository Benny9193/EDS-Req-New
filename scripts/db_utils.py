"""
Shared Database Utilities
Provides secure, reusable database connection and query execution.

Usage:
    from db_utils import DatabaseConnection, execute_query

    # Context manager usage (recommended)
    with DatabaseConnection() as db:
        results = db.execute_query(
            "SELECT * FROM table WHERE id = ?",
            params=(123,)
        )

    # Or use the convenience function
    results = execute_query("SELECT * FROM table WHERE status = ?", ("active",))
"""

import os
import pyodbc
from typing import Optional, List, Tuple, Any, Dict
from contextlib import contextmanager
from dotenv import load_dotenv

# Load environment variables from project root
_env_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), '.env')
load_dotenv(_env_path)


class DatabaseConnectionError(Exception):
    """Raised when database connection fails."""
    pass


class DatabaseQueryError(Exception):
    """Raised when query execution fails."""
    pass


class DatabaseConnection:
    """
    Secure database connection manager with context manager support.

    Features:
    - Automatic ODBC driver detection
    - Parameterized query execution (prevents SQL injection)
    - Proper resource cleanup with context managers
    - Connection timeout handling

    Example:
        with DatabaseConnection() as db:
            rows = db.execute_query(
                "SELECT * FROM users WHERE status = ?",
                params=("active",)
            )
            for row in rows:
                print(row)
    """

    def __init__(
        self,
        database: str = None,
        server: str = None,
        username: str = None,
        password: str = None,
        timeout: int = 30
    ):
        """
        Initialize database connection parameters.

        Args:
            database: Database name (default: from config or 'dpa_EDSAdmin')
            server: Server address (default: from DB_SERVER env var)
            username: Username (default: from DB_USERNAME env var)
            password: Password (default: from DB_PASSWORD env var)
            timeout: Connection timeout in seconds (default: 30)
        """
        self.database = database or os.getenv('DB_DATABASE', 'dpa_EDSAdmin')
        self.server = server or os.getenv('DB_SERVER')
        self.username = username or os.getenv('DB_USERNAME')
        self.password = password or os.getenv('DB_PASSWORD')
        self.timeout = timeout
        self._conn: Optional[pyodbc.Connection] = None
        self._driver: Optional[str] = None

    def __enter__(self) -> 'DatabaseConnection':
        """Enter context manager - establish connection."""
        self.connect()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """Exit context manager - close connection."""
        self.disconnect()

    def _detect_odbc_driver(self) -> str:
        """Detect available SQL Server ODBC driver."""
        drivers = [d for d in pyodbc.drivers() if 'SQL Server' in d]
        if not drivers:
            raise DatabaseConnectionError(
                "No SQL Server ODBC driver found. "
                "Install 'ODBC Driver 17 for SQL Server' or similar."
            )
        # Prefer newer drivers
        preferred_order = [
            'ODBC Driver 18 for SQL Server',
            'ODBC Driver 17 for SQL Server',
            'SQL Server Native Client 11.0',
            'SQL Server'
        ]
        for preferred in preferred_order:
            if preferred in drivers:
                return preferred
        return drivers[0]

    def _validate_credentials(self) -> None:
        """Validate that all required credentials are present."""
        missing = []
        if not self.server:
            missing.append('DB_SERVER')
        if not self.username:
            missing.append('DB_USERNAME')
        if not self.password:
            missing.append('DB_PASSWORD')

        if missing:
            raise DatabaseConnectionError(
                f"Missing database credentials: {', '.join(missing)}. "
                "Set these in your .env file or pass them directly."
            )

    def connect(self) -> None:
        """
        Establish database connection.

        Raises:
            DatabaseConnectionError: If connection fails
        """
        if self._conn is not None:
            return  # Already connected

        self._validate_credentials()
        self._driver = self._detect_odbc_driver()

        conn_str = (
            f"DRIVER={{{self._driver}}};"
            f"SERVER={self.server};"
            f"DATABASE={self.database};"
            f"UID={self.username};"
            f"PWD={self.password};"
            f"Encrypt=yes;"
            f"TrustServerCertificate=yes;"
            f"Connection Timeout={self.timeout}"
        )

        try:
            self._conn = pyodbc.connect(conn_str, timeout=self.timeout)
        except pyodbc.Error as e:
            raise DatabaseConnectionError(
                f"Failed to connect to {self.database} on {self.server}: {e}"
            ) from e

    def disconnect(self) -> None:
        """Close database connection and release resources."""
        if self._conn is not None:
            try:
                self._conn.close()
            except pyodbc.Error:
                pass  # Ignore errors on close
            finally:
                self._conn = None

    @property
    def is_connected(self) -> bool:
        """Check if connection is established."""
        return self._conn is not None

    def execute_query(
        self,
        query: str,
        params: Tuple = None,
        fetch_all: bool = True
    ) -> List[Tuple]:
        """
        Execute a parameterized query safely.

        Args:
            query: SQL query with ? placeholders for parameters
            params: Tuple of parameter values (prevents SQL injection)
            fetch_all: If True, fetch all results; if False, return cursor

        Returns:
            List of result tuples

        Raises:
            DatabaseQueryError: If query execution fails

        Example:
            # Safe parameterized query
            rows = db.execute_query(
                "SELECT * FROM users WHERE age > ? AND status = ?",
                params=(21, "active")
            )
        """
        if not self.is_connected:
            raise DatabaseQueryError("Not connected to database. Call connect() first.")

        cursor = None
        try:
            cursor = self._conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            if fetch_all:
                return cursor.fetchall()
            return cursor
        except pyodbc.Error as e:
            raise DatabaseQueryError(f"Query execution failed: {e}") from e
        finally:
            if cursor is not None and fetch_all:
                cursor.close()

    def execute_non_query(
        self,
        query: str,
        params: Tuple = None,
        commit: bool = True
    ) -> int:
        """
        Execute a non-query statement (INSERT, UPDATE, DELETE, DDL).

        Args:
            query: SQL statement with ? placeholders
            params: Tuple of parameter values
            commit: Whether to commit the transaction

        Returns:
            Number of rows affected

        Raises:
            DatabaseQueryError: If execution fails
        """
        if not self.is_connected:
            raise DatabaseQueryError("Not connected to database. Call connect() first.")

        cursor = None
        try:
            cursor = self._conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)

            rows_affected = cursor.rowcount
            if commit:
                self._conn.commit()
            return rows_affected
        except pyodbc.Error as e:
            if commit:
                self._conn.rollback()
            raise DatabaseQueryError(f"Statement execution failed: {e}") from e
        finally:
            if cursor is not None:
                cursor.close()

    def execute_many(
        self,
        query: str,
        params_list: List[Tuple],
        commit: bool = True
    ) -> int:
        """
        Execute a statement multiple times with different parameters.

        Args:
            query: SQL statement with ? placeholders
            params_list: List of parameter tuples
            commit: Whether to commit the transaction

        Returns:
            Total rows affected
        """
        if not self.is_connected:
            raise DatabaseQueryError("Not connected to database. Call connect() first.")

        cursor = None
        try:
            cursor = self._conn.cursor()
            cursor.executemany(query, params_list)
            rows_affected = cursor.rowcount
            if commit:
                self._conn.commit()
            return rows_affected
        except pyodbc.Error as e:
            if commit:
                self._conn.rollback()
            raise DatabaseQueryError(f"Batch execution failed: {e}") from e
        finally:
            if cursor is not None:
                cursor.close()

    def fetch_one(self, query: str, params: Tuple = None) -> Optional[Tuple]:
        """
        Execute query and fetch single row.

        Args:
            query: SQL query with ? placeholders
            params: Parameter tuple

        Returns:
            Single row tuple or None if no results
        """
        if not self.is_connected:
            raise DatabaseQueryError("Not connected to database. Call connect() first.")

        cursor = None
        try:
            cursor = self._conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            return cursor.fetchone()
        except pyodbc.Error as e:
            raise DatabaseQueryError(f"Query execution failed: {e}") from e
        finally:
            if cursor is not None:
                cursor.close()

    def fetch_scalar(self, query: str, params: Tuple = None) -> Any:
        """
        Execute query and fetch single value.

        Args:
            query: SQL query returning single value
            params: Parameter tuple

        Returns:
            Single value or None
        """
        row = self.fetch_one(query, params)
        return row[0] if row else None


# Convenience functions for simple operations

def execute_query(
    query: str,
    params: Tuple = None,
    database: str = None
) -> List[Tuple]:
    """
    Execute a query using a temporary connection.

    Convenience function for one-off queries.

    Args:
        query: SQL query with ? placeholders
        params: Parameter tuple
        database: Database name (optional)

    Returns:
        List of result tuples
    """
    with DatabaseConnection(database=database) as db:
        return db.execute_query(query, params)


def execute_non_query(
    query: str,
    params: Tuple = None,
    database: str = None
) -> int:
    """
    Execute a non-query statement using a temporary connection.

    Args:
        query: SQL statement with ? placeholders
        params: Parameter tuple
        database: Database name (optional)

    Returns:
        Number of rows affected
    """
    with DatabaseConnection(database=database) as db:
        return db.execute_non_query(query, params)


@contextmanager
def get_connection(database: str = None) -> DatabaseConnection:
    """
    Get a database connection as a context manager.

    Alternative syntax for connection management.

    Example:
        with get_connection() as db:
            results = db.execute_query("SELECT 1")
    """
    db = DatabaseConnection(database=database)
    try:
        db.connect()
        yield db
    finally:
        db.disconnect()
