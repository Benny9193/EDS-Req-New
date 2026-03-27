"""
Configuration Management
Loads and validates configuration from config.yaml with environment overrides.

Usage:
    from config import config, get_threshold, get_database_config

    # Access config values
    db_name = config.database.name
    critical_threshold = config.thresholds.missing_index.critical

    # Or use convenience functions
    threshold = get_threshold('missing_index', 'critical')
    db_config = get_database_config()
"""

import os
from dataclasses import dataclass, field
from typing import Optional, Any, Dict
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


@dataclass
class MissingIndexThresholds:
    """Thresholds for missing index recommendations."""
    critical: int = 95
    high: int = 80
    medium: int = 50
    min_executions: int = 100


@dataclass
class BlockingThresholds:
    """Thresholds for blocking events."""
    critical_seconds: int = 3600
    high_seconds: int = 300
    medium_seconds: int = 60


@dataclass
class IOLatencyThresholds:
    """Thresholds for I/O latency."""
    critical_ms: int = 200
    high_ms: int = 100
    medium_ms: int = 50


@dataclass
class SlowQueryThresholds:
    """Thresholds for slow queries."""
    critical_buffer_gets: int = 10000000
    high_buffer_gets: int = 1000000
    min_buffer_gets: int = 100000


@dataclass
class Thresholds:
    """All threshold configurations."""
    missing_index: MissingIndexThresholds = field(default_factory=MissingIndexThresholds)
    blocking: BlockingThresholds = field(default_factory=BlockingThresholds)
    io_latency: IOLatencyThresholds = field(default_factory=IOLatencyThresholds)
    slow_query: SlowQueryThresholds = field(default_factory=SlowQueryThresholds)


@dataclass
class DatabaseConfig:
    """Database connection configuration."""
    name: str = "dpa_EDSAdmin"
    timeout: int = 30


@dataclass
class AnalysisConfig:
    """Analysis default settings."""
    missing_indexes_days: int = 30
    slow_queries_days: int = 7
    blocking_days: int = 30
    io_issues_hours: int = 24
    top_results: int = 50
    report_top: int = 10


@dataclass
class DashboardConfig:
    """Dashboard settings."""
    refresh_interval: int = 30

    @dataclass
    class HealthScore:
        critical_index_penalty: int = 20
        high_index_penalty: int = 10
        blocking_penalty: int = 15
        io_latency_penalty: int = 10
        slow_query_penalty: int = 5

    health_score: HealthScore = field(default_factory=HealthScore)


@dataclass
class OutputConfig:
    """Output directory settings."""
    directory: str = "output/performance"
    exports_directory: str = "output/exports"
    log_directory: str = "logs"


@dataclass
class AlertConfig:
    """Alert notification settings."""
    email: str = "dba-team@company.com"
    mail_profile: str = "Default"
    enabled: bool = True


@dataclass
class LoggingConfig:
    """Logging configuration."""
    level: str = "INFO"
    format: str = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    max_file_size_mb: int = 10
    backup_count: int = 5


@dataclass
class Config:
    """Main configuration container."""
    database: DatabaseConfig = field(default_factory=DatabaseConfig)
    thresholds: Thresholds = field(default_factory=Thresholds)
    analysis: AnalysisConfig = field(default_factory=AnalysisConfig)
    dashboard: DashboardConfig = field(default_factory=DashboardConfig)
    output: OutputConfig = field(default_factory=OutputConfig)
    alerts: AlertConfig = field(default_factory=AlertConfig)
    logging: LoggingConfig = field(default_factory=LoggingConfig)


def _find_config_file() -> Optional[Path]:
    """Find config.yaml in project root or current directory."""
    # Check project root (one level up from scripts/)
    project_root = Path(__file__).parent.parent
    config_path = project_root / "config.yaml"
    if config_path.exists():
        return config_path

    # Check current working directory
    cwd_config = Path.cwd() / "config.yaml"
    if cwd_config.exists():
        return cwd_config

    return None


def _load_yaml_config(path: Path) -> Dict[str, Any]:
    """Load configuration from YAML file."""
    if yaml is None:
        print("[WARNING] PyYAML not installed. Using default configuration.")
        print("         Install with: pip install pyyaml")
        return {}

    try:
        with open(path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f) or {}
    except Exception as e:
        print(f"[WARNING] Failed to load config from {path}: {e}")
        return {}


def _apply_dict_to_dataclass(obj: Any, data: Dict[str, Any]) -> None:
    """Recursively apply dictionary values to dataclass instance."""
    if not data:
        return

    for key, value in data.items():
        if hasattr(obj, key):
            attr = getattr(obj, key)
            if hasattr(attr, '__dataclass_fields__') and isinstance(value, dict):
                # Recursively apply to nested dataclass
                _apply_dict_to_dataclass(attr, value)
            else:
                # Set the value directly
                setattr(obj, key, value)


def _apply_env_overrides(config: Config) -> None:
    """Apply environment variable overrides."""
    # Database overrides
    if os.getenv('DB_DATABASE'):
        config.database.name = os.getenv('DB_DATABASE')
    if os.getenv('DB_TIMEOUT'):
        config.database.timeout = int(os.getenv('DB_TIMEOUT'))

    # Threshold overrides (format: THRESHOLD_CATEGORY_NAME)
    if os.getenv('THRESHOLD_MISSING_INDEX_CRITICAL'):
        config.thresholds.missing_index.critical = int(os.getenv('THRESHOLD_MISSING_INDEX_CRITICAL'))
    if os.getenv('THRESHOLD_BLOCKING_CRITICAL_SECONDS'):
        config.thresholds.blocking.critical_seconds = int(os.getenv('THRESHOLD_BLOCKING_CRITICAL_SECONDS'))

    # Alert overrides
    if os.getenv('ALERT_EMAIL'):
        config.alerts.email = os.getenv('ALERT_EMAIL')

    # Logging overrides
    if os.getenv('LOG_LEVEL'):
        config.logging.level = os.getenv('LOG_LEVEL')


def load_config() -> Config:
    """
    Load configuration from config.yaml with environment overrides.

    Priority:
    1. Environment variables (highest)
    2. config.yaml file
    3. Default values (lowest)

    Returns:
        Config instance with all settings
    """
    config = Config()

    # Load from YAML file if available
    config_path = _find_config_file()
    if config_path:
        yaml_data = _load_yaml_config(config_path)
        _apply_dict_to_dataclass(config, yaml_data)

    # Apply environment variable overrides
    _apply_env_overrides(config)

    return config


# Global config instance (lazy loaded)
_config: Optional[Config] = None


def get_config() -> Config:
    """Get the global configuration instance."""
    global _config
    if _config is None:
        _config = load_config()
    return _config


def reload_config() -> Config:
    """Force reload of configuration."""
    global _config
    _config = load_config()
    return _config


# Convenience property for direct access
config = property(lambda self: get_config())


# Convenience functions

def get_threshold(category: str, level: str) -> int:
    """
    Get a threshold value by category and level.

    Args:
        category: 'missing_index', 'blocking', 'io_latency', 'slow_query'
        level: 'critical', 'high', 'medium', or threshold-specific name

    Returns:
        Threshold value

    Example:
        critical = get_threshold('missing_index', 'critical')  # Returns 95
    """
    cfg = get_config()
    category_obj = getattr(cfg.thresholds, category, None)
    if category_obj is None:
        raise ValueError(f"Unknown threshold category: {category}")

    value = getattr(category_obj, level, None)
    if value is None:
        raise ValueError(f"Unknown threshold level '{level}' in category '{category}'")

    return value


def get_database_config() -> Dict[str, Any]:
    """
    Get database configuration as a dictionary.

    Returns:
        Dict with 'name' and 'timeout' keys
    """
    cfg = get_config()
    return {
        'name': cfg.database.name,
        'timeout': cfg.database.timeout
    }


def get_output_path(subdir: str = None) -> Path:
    """
    Get output directory path.

    Args:
        subdir: Optional subdirectory ('exports', 'logs')

    Returns:
        Path to output directory
    """
    cfg = get_config()
    project_root = Path(__file__).parent.parent

    if subdir == 'exports':
        base = cfg.output.exports_directory
    elif subdir == 'logs':
        base = cfg.output.log_directory
    else:
        base = cfg.output.directory

    path = project_root / base
    path.mkdir(parents=True, exist_ok=True)
    return path


def validate_params(
    days: int = None,
    min_saving: int = None,
    hours: int = None,
    latency_ms: int = None
) -> None:
    """
    Validate common parameters.

    Raises:
        ValueError: If any parameter is out of valid range
    """
    if days is not None:
        if not 1 <= days <= 365:
            raise ValueError(f"days must be 1-365, got {days}")

    if min_saving is not None:
        if not 0 <= min_saving <= 100:
            raise ValueError(f"min_saving must be 0-100, got {min_saving}")

    if hours is not None:
        if not 1 <= hours <= 8760:  # Max 1 year
            raise ValueError(f"hours must be 1-8760, got {hours}")

    if latency_ms is not None:
        if not 0 <= latency_ms <= 10000:
            raise ValueError(f"latency_ms must be 0-10000, got {latency_ms}")


# Make config accessible as module-level variable
def __getattr__(name: str) -> Any:
    """Allow accessing config as module attribute."""
    if name == 'config':
        return get_config()
    raise AttributeError(f"module '{__name__}' has no attribute '{name}'")
