"""
Tests for configuration management.
"""

import pytest
from pathlib import Path


class TestConfig:
    """Tests for config module."""

    def test_config_loads_defaults(self):
        """Test that config loads with default values."""
        from config import Config

        config = Config()

        assert config.database.name == 'dpa_EDSAdmin'
        assert config.database.timeout == 30
        assert config.thresholds.missing_index.critical == 95
        assert config.thresholds.blocking.critical_seconds == 3600

    def test_validate_params_valid(self):
        """Test parameter validation with valid values."""
        from config import validate_params

        # Should not raise
        validate_params(days=30)
        validate_params(min_saving=50)
        validate_params(hours=24)
        validate_params(latency_ms=100)

    def test_validate_params_invalid_days(self):
        """Test parameter validation rejects invalid days."""
        from config import validate_params

        with pytest.raises(ValueError, match="days must be 1-365"):
            validate_params(days=0)

        with pytest.raises(ValueError, match="days must be 1-365"):
            validate_params(days=400)

    def test_validate_params_invalid_min_saving(self):
        """Test parameter validation rejects invalid min_saving."""
        from config import validate_params

        with pytest.raises(ValueError, match="min_saving must be 0-100"):
            validate_params(min_saving=-1)

        with pytest.raises(ValueError, match="min_saving must be 0-100"):
            validate_params(min_saving=101)

    def test_validate_params_invalid_hours(self):
        """Test parameter validation rejects invalid hours."""
        from config import validate_params

        with pytest.raises(ValueError, match="hours must be 1-8760"):
            validate_params(hours=0)

    def test_validate_params_invalid_latency(self):
        """Test parameter validation rejects invalid latency."""
        from config import validate_params

        with pytest.raises(ValueError, match="latency_ms must be 0-10000"):
            validate_params(latency_ms=-5)

    def test_get_threshold(self):
        """Test threshold retrieval."""
        from config import get_threshold, reload_config

        # Reload to ensure fresh state
        reload_config()

        critical = get_threshold('missing_index', 'critical')
        assert critical == 95

        high = get_threshold('blocking', 'high_seconds')
        assert high == 300

    def test_get_threshold_invalid_category(self):
        """Test threshold retrieval with invalid category."""
        from config import get_threshold

        with pytest.raises(ValueError, match="Unknown threshold category"):
            get_threshold('invalid_category', 'critical')

    def test_get_threshold_invalid_level(self):
        """Test threshold retrieval with invalid level."""
        from config import get_threshold

        with pytest.raises(ValueError, match="Unknown threshold level"):
            get_threshold('missing_index', 'invalid_level')

    def test_env_override(self, monkeypatch):
        """Test environment variable overrides."""
        from config import reload_config

        monkeypatch.setenv('DB_DATABASE', 'custom_db')

        config = reload_config()
        assert config.database.name == 'custom_db'


class TestThresholds:
    """Tests for threshold dataclasses."""

    def test_missing_index_thresholds_defaults(self):
        """Test missing index threshold defaults."""
        from config import MissingIndexThresholds

        thresholds = MissingIndexThresholds()
        assert thresholds.critical == 95
        assert thresholds.high == 80
        assert thresholds.medium == 50
        assert thresholds.min_executions == 100

    def test_blocking_thresholds_defaults(self):
        """Test blocking threshold defaults."""
        from config import BlockingThresholds

        thresholds = BlockingThresholds()
        assert thresholds.critical_seconds == 3600
        assert thresholds.high_seconds == 300
        assert thresholds.medium_seconds == 60

    def test_io_latency_thresholds_defaults(self):
        """Test I/O latency threshold defaults."""
        from config import IOLatencyThresholds

        thresholds = IOLatencyThresholds()
        assert thresholds.critical_ms == 200
        assert thresholds.high_ms == 100
        assert thresholds.medium_ms == 50
