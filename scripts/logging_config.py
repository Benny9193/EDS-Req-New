"""
Structured Logging Configuration
Provides consistent logging across all scripts with file and console output.

Usage:
    from logging_config import setup_logging, get_logger

    # Setup logging for a script
    logger = setup_logging('analyze_performance')

    # Use the logger
    logger.info("Starting analysis")
    logger.warning("Found %d issues", count)
    logger.error("Operation failed: %s", error)

    # Or get logger for a specific module
    logger = get_logger(__name__)
"""

import os
import sys
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pathlib import Path
from typing import Optional

# Try to import config, fall back to defaults
try:
    from config import get_config
    _HAS_CONFIG = True
except ImportError:
    _HAS_CONFIG = False


# Default settings (used if config unavailable)
_DEFAULT_LOG_LEVEL = "INFO"
_DEFAULT_LOG_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
_DEFAULT_MAX_FILE_SIZE_MB = 10
_DEFAULT_BACKUP_COUNT = 5


def _get_log_directory() -> Path:
    """Get the log directory path, creating it if needed."""
    if _HAS_CONFIG:
        cfg = get_config()
        log_dir = cfg.output.log_directory
    else:
        log_dir = "logs"

    # Resolve relative to project root
    project_root = Path(__file__).parent.parent
    log_path = project_root / log_dir
    log_path.mkdir(parents=True, exist_ok=True)
    return log_path


def _get_log_settings() -> dict:
    """Get logging settings from config or defaults."""
    if _HAS_CONFIG:
        cfg = get_config()
        return {
            'level': cfg.logging.level,
            'format': cfg.logging.format,
            'max_size_mb': cfg.logging.max_file_size_mb,
            'backup_count': cfg.logging.backup_count
        }
    return {
        'level': _DEFAULT_LOG_LEVEL,
        'format': _DEFAULT_LOG_FORMAT,
        'max_size_mb': _DEFAULT_MAX_FILE_SIZE_MB,
        'backup_count': _DEFAULT_BACKUP_COUNT
    }


def _parse_log_level(level: str) -> int:
    """Convert string log level to logging constant."""
    level_map = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'WARN': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    return level_map.get(level.upper(), logging.INFO)


def setup_logging(
    script_name: str,
    log_level: str = None,
    console_output: bool = True,
    file_output: bool = True
) -> logging.Logger:
    """
    Set up logging for a script with file and console handlers.

    Args:
        script_name: Name of the script (used for log file name)
        log_level: Override log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        console_output: Enable console logging (default: True)
        file_output: Enable file logging (default: True)

    Returns:
        Configured logger instance

    Example:
        logger = setup_logging('analyze_performance')
        logger.info("Starting analysis...")
        logger.error("Failed: %s", error_msg)
    """
    settings = _get_log_settings()

    # Determine log level
    if log_level:
        level = _parse_log_level(log_level)
    else:
        # Check environment variable override
        env_level = os.getenv('LOG_LEVEL')
        if env_level:
            level = _parse_log_level(env_level)
        else:
            level = _parse_log_level(settings['level'])

    # Create logger
    logger = logging.getLogger(script_name)
    logger.setLevel(level)

    # Clear any existing handlers
    logger.handlers.clear()

    # Create formatter
    formatter = logging.Formatter(settings['format'])

    # Console handler
    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        logger.addHandler(console_handler)

    # File handler with rotation
    if file_output:
        log_dir = _get_log_directory()
        log_file = log_dir / f"{script_name}.log"

        max_bytes = settings['max_size_mb'] * 1024 * 1024
        file_handler = RotatingFileHandler(
            log_file,
            maxBytes=max_bytes,
            backupCount=settings['backup_count'],
            encoding='utf-8'
        )
        file_handler.setLevel(level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # Prevent propagation to root logger
    logger.propagate = False

    return logger


def get_logger(name: str) -> logging.Logger:
    """
    Get a logger by name.

    If logging hasn't been set up, creates a basic console logger.

    Args:
        name: Logger name (typically __name__)

    Returns:
        Logger instance
    """
    logger = logging.getLogger(name)

    # If no handlers, add a basic console handler
    if not logger.handlers and not logger.parent.handlers:
        settings = _get_log_settings()
        level = _parse_log_level(settings['level'])

        logger.setLevel(level)
        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(level)
        handler.setFormatter(logging.Formatter(settings['format']))
        logger.addHandler(handler)
        logger.propagate = False

    return logger


class LogContext:
    """
    Context manager for logging operation start/end.

    Usage:
        with LogContext(logger, "Processing data"):
            # ... processing code ...
        # Logs: "Starting: Processing data" and "Completed: Processing data (1.23s)"
    """

    def __init__(self, logger: logging.Logger, operation: str, level: int = logging.INFO):
        self.logger = logger
        self.operation = operation
        self.level = level
        self.start_time = None

    def __enter__(self):
        self.start_time = datetime.now()
        self.logger.log(self.level, "Starting: %s", self.operation)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        elapsed = (datetime.now() - self.start_time).total_seconds()
        if exc_type is None:
            self.logger.log(self.level, "Completed: %s (%.2fs)", self.operation, elapsed)
        else:
            self.logger.error("Failed: %s (%.2fs) - %s", self.operation, elapsed, exc_val)
        return False  # Don't suppress exceptions


def log_execution(logger: logging.Logger, operation: str):
    """
    Decorator to log function execution.

    Usage:
        @log_execution(logger, "Processing items")
        def process_items(items):
            ...
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            with LogContext(logger, operation):
                return func(*args, **kwargs)
        wrapper.__name__ = func.__name__
        wrapper.__doc__ = func.__doc__
        return wrapper
    return decorator


def configure_root_logger(level: str = None) -> None:
    """
    Configure the root logger for library compatibility.

    Use this when integrating with libraries that use the root logger.
    """
    settings = _get_log_settings()
    log_level = _parse_log_level(level or settings['level'])

    logging.basicConfig(
        level=log_level,
        format=settings['format'],
        handlers=[logging.StreamHandler(sys.stdout)]
    )


# Convenience function to suppress noisy loggers
def silence_logger(name: str, level: int = logging.WARNING) -> None:
    """
    Silence a noisy logger by raising its level.

    Args:
        name: Logger name (e.g., 'urllib3', 'pyodbc')
        level: Minimum level to log (default: WARNING)
    """
    logging.getLogger(name).setLevel(level)
