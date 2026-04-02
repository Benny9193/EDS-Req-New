"""Shared database connection helper for agent tools.

Provides a connection context manager with friendly error messages
for common failure modes (unreachable server, auth failure, etc.).
"""

import logging
import os
from contextlib import contextmanager
from typing import Optional

try:
    import pyodbc
except ImportError:
    pyodbc = None  # type: ignore

logger = logging.getLogger(__name__)


class DatabaseConnectionError(Exception):
    """Raised when the database is unreachable or credentials are wrong."""
    pass


def build_connection_string(database: str = "EDS", timeout: int = 30) -> str:
    server = os.environ.get("DB_SERVER", "localhost")
    username = os.environ.get("DB_USERNAME", "")
    password = os.environ.get("DB_PASSWORD", "")

    if not server or server == "localhost":
        logger.warning("DB_SERVER not set or is localhost — connection may fail")

    return (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password};"
        f"Connection Timeout={timeout};"
    )


@contextmanager
def get_connection(database: str = "EDS", timeout: int = 30):
    """Context manager that yields a pyodbc connection with friendly errors."""
    if pyodbc is None:
        raise DatabaseConnectionError(
            "pyodbc is not installed. Install it with: pip install pyodbc"
        )

    conn_str = build_connection_string(database, timeout)

    try:
        conn = pyodbc.connect(conn_str, timeout=timeout)
    except pyodbc.OperationalError as e:
        msg = str(e)
        if "Login failed" in msg:
            raise DatabaseConnectionError(
                f"Database authentication failed for '{database}'. "
                "Check DB_USERNAME and DB_PASSWORD environment variables."
            ) from e
        elif "server was not found" in msg or "Cannot open" in msg or "TCP Provider" in msg:
            server = os.environ.get("DB_SERVER", "localhost")
            raise DatabaseConnectionError(
                f"Cannot reach database server '{server}'. "
                "Check DB_SERVER environment variable and network connectivity."
            ) from e
        elif "ODBC Driver" in msg:
            raise DatabaseConnectionError(
                "ODBC Driver 17 for SQL Server is not installed. "
                "Install it from: https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server"
            ) from e
        else:
            raise DatabaseConnectionError(f"Database connection failed: {msg}") from e
    except pyodbc.InterfaceError as e:
        raise DatabaseConnectionError(
            f"Database interface error: {e}. Check ODBC driver installation."
        ) from e
    except Exception as e:
        raise DatabaseConnectionError(f"Unexpected connection error: {e}") from e

    try:
        yield conn
    finally:
        conn.close()
