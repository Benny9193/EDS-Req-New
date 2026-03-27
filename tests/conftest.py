"""
Pytest configuration and fixtures.
"""

import sys
import os
from pathlib import Path

import pytest

# Disable rate limiting for tests — must be set before the app is imported
os.environ["EDS_RATE_LIMIT"] = "999999"

# Add scripts and api directories to path
project_root = Path(__file__).parent.parent
scripts_dir = project_root / 'scripts'
api_dir = project_root / 'api'
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(scripts_dir))


@pytest.fixture
def sample_config():
    """Sample configuration for testing."""
    return {
        'database': {
            'name': 'test_db',
            'timeout': 30
        },
        'thresholds': {
            'missing_index': {
                'critical': 95,
                'high': 80,
                'medium': 50
            },
            'blocking': {
                'critical_seconds': 3600,
                'high_seconds': 300
            }
        }
    }


@pytest.fixture
def mock_db_credentials(monkeypatch):
    """Mock database credentials."""
    monkeypatch.setenv('DB_SERVER', 'test-server.local')
    monkeypatch.setenv('DB_USERNAME', 'test_user')
    monkeypatch.setenv('DB_PASSWORD', 'test_pass')
    monkeypatch.setenv('DB_DATABASE', 'test_db')


@pytest.fixture
def temp_output_dir(tmp_path):
    """Create temporary output directory."""
    output_dir = tmp_path / 'output' / 'performance'
    output_dir.mkdir(parents=True)
    return output_dir
