"""
Database connection module for EDS API.
Uses pyodbc to connect to SQL Server with connection pooling.
"""

import os
import logging
from pathlib import Path
from contextlib import contextmanager
from typing import Generator, Any, List, Dict, Optional
import pyodbc
from dotenv import load_dotenv

# Load environment variables from project root .env file
PROJECT_ROOT = Path(__file__).parent.parent
ENV_FILE = PROJECT_ROOT / ".env"
load_dotenv(ENV_FILE)

# Set up logging
logger = logging.getLogger(__name__)

# Database configuration
# Note: Uses EDS database for product catalog (not dpa_EDSAdmin which is DPA monitoring)
DB_CONFIG = {
    "server": os.getenv("DB_SERVER", "localhost"),
    "database": os.getenv("DB_DATABASE_CATALOG", os.getenv("DB_DATABASE", "EDS")),
    "username": os.getenv("DB_USERNAME", ""),
    "password": os.getenv("DB_PASSWORD", ""),
    # Connection pool settings
    "pool_min_connections": int(os.getenv("DB_POOL_MIN", "2")),
    "pool_max_connections": int(os.getenv("DB_POOL_MAX", "10")),
    "connection_timeout": int(os.getenv("DB_CONNECTION_TIMEOUT", "30")),
}

# Enable connection pooling at the driver level
pyodbc.pooling = True


def get_connection_string() -> str:
    """Build the ODBC connection string with pooling optimizations."""
    return (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"UID={DB_CONFIG['username']};"
        f"PWD={DB_CONFIG['password']};"
        f"TrustServerCertificate=yes;"
        f"Connection Timeout={DB_CONFIG['connection_timeout']};"
        # Enable MARS for multiple result sets
        f"MultipleActiveResultSets=True;"
    )


# Cache the connection string
_connection_string: Optional[str] = None


def _get_cached_connection_string() -> str:
    """Get cached connection string to avoid rebuilding."""
    global _connection_string
    if _connection_string is None:
        _connection_string = get_connection_string()
    return _connection_string


@contextmanager
def get_db_connection() -> Generator[pyodbc.Connection, None, None]:
    """
    Context manager for database connections.
    Uses pyodbc's built-in connection pooling.
    """
    conn = None
    try:
        conn = pyodbc.connect(_get_cached_connection_string())
        yield conn
    except pyodbc.Error as e:
        logger.error(f"Database connection error: {e}")
        raise
    finally:
        if conn:
            conn.close()


@contextmanager
def get_db_cursor() -> Generator[pyodbc.Cursor, None, None]:
    """Context manager for database cursors."""
    with get_db_connection() as conn:
        cursor = conn.cursor()
        try:
            yield cursor
        finally:
            cursor.close()


@contextmanager
def transaction() -> Generator[tuple[pyodbc.Connection, pyodbc.Cursor], None, None]:
    """
    Context manager for database transactions with automatic commit/rollback.

    Usage:
        with transaction() as (conn, cursor):
            cursor.execute("INSERT ...")
            cursor.execute("INSERT ...")
            # Commits automatically if no exception
            # Rolls back automatically on exception

    Yields:
        Tuple of (connection, cursor) for executing queries
    """
    conn = None
    cursor = None
    try:
        conn = pyodbc.connect(_get_cached_connection_string())
        conn.autocommit = False  # Ensure we're in transaction mode
        cursor = conn.cursor()
        yield (conn, cursor)
        conn.commit()
        logger.debug("Transaction committed successfully")
    except Exception as e:
        if conn:
            try:
                conn.rollback()
                logger.warning(f"Transaction rolled back due to: {e}")
            except Exception as rollback_error:
                logger.error(f"Rollback failed: {rollback_error}")
        raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def execute_query(
    query: str,
    params: Optional[tuple] = None
) -> List[Dict[str, Any]]:
    """
    Execute a SELECT query and return results as list of dicts.

    Args:
        query: SQL query string
        params: Optional tuple of parameters for parameterized queries

    Returns:
        List of dictionaries with column names as keys
    """
    with get_db_cursor() as cursor:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)

        columns = [column[0] for column in cursor.description]
        results = []
        for row in cursor.fetchall():
            results.append(dict(zip(columns, row)))
        return results


def execute_single(
    query: str,
    params: Optional[tuple] = None
) -> Optional[Dict[str, Any]]:
    """
    Execute a SELECT query and return single result as dict.

    Args:
        query: SQL query string
        params: Optional tuple of parameters

    Returns:
        Dictionary with column names as keys, or None if no result
    """
    results = execute_query(query, params)
    return results[0] if results else None


def test_connection() -> bool:
    """Test the database connection."""
    try:
        with get_db_cursor() as cursor:
            cursor.execute("SELECT 1")
            return True
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
        return False


def get_connection_info() -> dict:
    """Get connection info for debugging (passwords hidden)."""
    return {
        "server": DB_CONFIG["server"],
        "database": DB_CONFIG["database"],
        "username": DB_CONFIG["username"],
        "password": "***" if DB_CONFIG["password"] else "(not set)",
        "env_file": str(ENV_FILE),
        "env_file_exists": ENV_FILE.exists(),
    }


# Log connection info at module load (for debugging)
_conn_info = get_connection_info()
logger.info(f"Database config: server={_conn_info['server']}, database={_conn_info['database']}, user={_conn_info['username']}")
