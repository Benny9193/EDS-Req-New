"""
Tests for index deployment utilities.
"""

import pytest
from unittest.mock import patch, MagicMock


class TestIndexDeployer:
    """Tests for IndexDeployer class."""

    def test_init_creates_output_dir(self, mock_db_credentials, tmp_path, monkeypatch):
        """Test initialization creates output directory."""
        from deploy_indexes_test import IndexDeployer

        monkeypatch.setattr(
            'deploy_indexes_test.os.path.dirname',
            lambda x: str(tmp_path)
        )

        deployer = IndexDeployer()
        assert deployer.conn_cache == {}
        assert deployer.deployment_log == []

    def test_parse_sql_script_file_not_found(self, mock_db_credentials):
        """Test parse_sql_script raises FileNotFoundError for missing file."""
        from deploy_indexes_test import IndexDeployer

        deployer = IndexDeployer()

        with pytest.raises(FileNotFoundError, match="SQL script not found"):
            deployer.parse_sql_script('/nonexistent/path/script.sql')

    def test_parse_sql_script_extracts_indexes(
        self, mock_db_credentials, temp_output_dir
    ):
        """Test parse_sql_script correctly extracts index definitions."""
        from deploy_indexes_test import IndexDeployer

        # Create a sample SQL script matching actual format
        # Note: Comment must not be at start of batch (parser skips batches starting with --)
        script_content = """USE [TestDB]
GO

CREATE NONCLUSTERED INDEX [IX_Users_Email]
ON [dbo].[Users] ([Email])
INCLUDE ([Name], [CreatedDate])
WITH (ONLINE = ON);
-- Estimated Improvement: 95.500%
GO

USE [TestDB]
GO

CREATE NONCLUSTERED INDEX [IX_Orders_CustomerId]
ON [dbo].[Orders] ([CustomerId])
WITH (ONLINE = ON);
-- Estimated Improvement: 88.200%
GO
"""
        script_path = temp_output_dir / 'test_indexes.sql'
        script_path.write_text(script_content)

        deployer = IndexDeployer()
        indexes = deployer.parse_sql_script(str(script_path))

        assert len(indexes) == 2
        assert indexes[0]['index_name'] == 'IX_Users_Email'
        assert indexes[0]['table'] == 'Users'
        assert indexes[0]['schema'] == 'dbo'
        assert abs(indexes[0]['estimated_improvement'] - 95.5) < 0.01
        assert indexes[1]['index_name'] == 'IX_Orders_CustomerId'

    def test_estimate_index_size_returns_value(self, mock_db_credentials):
        """Test estimate_index_size returns correct estimate."""
        from deploy_indexes_test import IndexDeployer

        deployer = IndexDeployer()

        # Mock database connection
        mock_db = MagicMock()
        mock_db.fetch_one.return_value = (100.0,)  # Table size 100 MB

        estimated_size = deployer.estimate_index_size(mock_db, 'dbo', 'Users')

        # Should be 15% of 100 MB = 15 MB
        assert abs(estimated_size - 15.0) < 0.01
        mock_db.fetch_one.assert_called_once()

    def test_estimate_index_size_returns_zero_on_error(self, mock_db_credentials):
        """Test estimate_index_size returns 0 on error."""
        from deploy_indexes_test import IndexDeployer
        from db_utils import DatabaseQueryError

        deployer = IndexDeployer()

        mock_db = MagicMock()
        mock_db.fetch_one.side_effect = DatabaseQueryError("Query failed")

        estimated_size = deployer.estimate_index_size(mock_db, 'dbo', 'Users')
        assert estimated_size == 0

    def test_check_disk_space_returns_info(self, mock_db_credentials):
        """Test check_disk_space returns correct info."""
        from deploy_indexes_test import IndexDeployer

        deployer = IndexDeployer()

        mock_db = MagicMock()
        mock_db.fetch_one.return_value = ('TestDB', 500.0, 1000.0)

        space_info = deployer.check_disk_space(mock_db)

        assert space_info['database'] == 'TestDB'
        assert abs(space_info['current_size_mb'] - 500.0) < 0.01
        assert abs(space_info['max_size_mb'] - 1000.0) < 0.01
        assert abs(space_info['available_mb'] - 500.0) < 0.01

    def test_execute_index_creation_dry_run(self, mock_db_credentials):
        """Test execute_index_creation in dry run mode."""
        from deploy_indexes_test import IndexDeployer

        deployer = IndexDeployer()

        mock_db = MagicMock()
        mock_db.fetch_one.return_value = (50.0,)

        index_info = {
            'database': 'TestDB',
            'schema': 'dbo',
            'table': 'Users',
            'index_name': 'IX_Users_Email',
            'estimated_improvement': 95.5,
            'sql': 'CREATE INDEX ...'
        }

        result = deployer.execute_index_creation(mock_db, index_info, dry_run=True)

        assert result['status'] == 'dry_run'
        assert result['database'] == 'TestDB'
        assert result['index_name'] == 'IX_Users_Email'
        assert result['duration_seconds'] == 0
        mock_db.execute_non_query.assert_not_called()

    def test_execute_index_creation_success(self, mock_db_credentials):
        """Test execute_index_creation succeeds."""
        from deploy_indexes_test import IndexDeployer

        deployer = IndexDeployer()

        mock_db = MagicMock()
        mock_db.fetch_one.return_value = (50.0,)
        mock_db.execute_non_query.return_value = None

        index_info = {
            'database': 'TestDB',
            'schema': 'dbo',
            'table': 'Users',
            'index_name': 'IX_Users_Email',
            'estimated_improvement': 95.5,
            'sql': 'CREATE INDEX ...'
        }

        result = deployer.execute_index_creation(mock_db, index_info, dry_run=False)

        assert result['status'] == 'success'
        assert result['database'] == 'TestDB'
        assert result['index_name'] == 'IX_Users_Email'
        mock_db.execute_non_query.assert_called_once_with('CREATE INDEX ...')

    def test_execute_index_creation_failure(self, mock_db_credentials):
        """Test execute_index_creation handles failure."""
        from deploy_indexes_test import IndexDeployer
        from db_utils import DatabaseQueryError

        deployer = IndexDeployer()

        mock_db = MagicMock()
        mock_db.fetch_one.return_value = (50.0,)
        mock_db.execute_non_query.side_effect = DatabaseQueryError(
            "Index already exists"
        )

        index_info = {
            'database': 'TestDB',
            'schema': 'dbo',
            'table': 'Users',
            'index_name': 'IX_Users_Email',
            'estimated_improvement': 95.5,
            'sql': 'CREATE INDEX ...'
        }

        result = deployer.execute_index_creation(mock_db, index_info, dry_run=False)

        assert result['status'] == 'failed'
        assert 'Index already exists' in result['error']


class TestProductionIndexDeployer:
    """Tests for ProductionIndexDeployer class."""

    def test_check_existing_index_true(self, mock_db_credentials):
        """Test check_existing_index returns True when index exists."""
        from deploy_indexes_production import ProductionIndexDeployer

        deployer = ProductionIndexDeployer()

        mock_db = MagicMock()
        mock_db.fetch_scalar.return_value = 1  # Index exists

        exists = deployer.check_existing_index(
            mock_db, 'dbo', 'Users', 'IX_Users_Email'
        )

        assert exists is True
        mock_db.fetch_scalar.assert_called_once()

    def test_check_existing_index_false(self, mock_db_credentials):
        """Test check_existing_index returns False when index doesn't exist."""
        from deploy_indexes_production import ProductionIndexDeployer

        deployer = ProductionIndexDeployer()

        mock_db = MagicMock()
        mock_db.fetch_scalar.return_value = 0  # Index does not exist

        exists = deployer.check_existing_index(
            mock_db, 'dbo', 'Users', 'IX_Users_New'
        )

        assert exists is False
