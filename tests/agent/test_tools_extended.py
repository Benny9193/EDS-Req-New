"""Tests for extended tools: script_runner, schema_introspector, catalog_search, report_generator."""

import json
import sys
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from agent.tools.script_runner import ScriptRunnerTool, create_script_tools
from agent.tools.schema_introspector import SchemaIntrospectorTool, create_schema_tools
from agent.tools.catalog_search import CatalogSearchTool, create_catalog_tools
from agent.tools.report_generator import ReportGeneratorTool, create_report_tools
from agent.export.models import ColumnDef, QueryDef, ReportPlan, SheetDef
from agent.export.excel_formatter import EDSColors, FORMAT_MAP


# ── ScriptRunnerTool ─────────────────────────────────────────────────


class TestScriptRunnerTool:
    def test_definition(self):
        tool = ScriptRunnerTool()
        defn = tool.definition
        assert defn.name == "script_runner"
        assert any(p.name == "script_name" for p in defn.parameters)

    def test_empty_name_rejected(self):
        tool = ScriptRunnerTool()
        result = tool.execute(script_name="")
        assert not result.success

    def test_missing_script(self, tmp_path):
        tool = ScriptRunnerTool(scripts_dir=str(tmp_path))
        result = tool.execute(script_name="nonexistent")
        assert not result.success
        assert "not found" in result.error.lower()

    def test_run_simple_script(self, tmp_path):
        script = tmp_path / "hello.py"
        script.write_text('print("hello world")')
        tool = ScriptRunnerTool(scripts_dir=str(tmp_path))
        result = tool.execute(script_name="hello")
        assert result.success
        assert "hello world" in result.data

    def test_script_with_args(self, tmp_path):
        script = tmp_path / "echo.py"
        script.write_text('import sys; print(" ".join(sys.argv[1:]))')
        tool = ScriptRunnerTool(scripts_dir=str(tmp_path))
        result = tool.execute(script_name="echo", args="foo bar")
        assert result.success
        assert "foo bar" in result.data

    def test_script_failure(self, tmp_path):
        script = tmp_path / "fail.py"
        script.write_text('import sys; sys.exit(1)')
        tool = ScriptRunnerTool(scripts_dir=str(tmp_path))
        result = tool.execute(script_name="fail")
        assert not result.success
        assert result.metadata["exit_code"] == 1

    def test_script_timeout(self, tmp_path):
        script = tmp_path / "slow.py"
        script.write_text('import time; time.sleep(10)')
        tool = ScriptRunnerTool(scripts_dir=str(tmp_path), timeout=1)
        result = tool.execute(script_name="slow")
        assert not result.success
        assert "timed out" in result.error.lower()

    def test_path_traversal_blocked(self, tmp_path):
        tool = ScriptRunnerTool(scripts_dir=str(tmp_path))
        result = tool.execute(script_name="../../etc/passwd")
        assert not result.success

    def test_factory(self):
        tools = create_script_tools({"tools": {"scripts_dir": "scripts", "script_timeout": 60}})
        assert len(tools) == 1
        assert tools[0].name == "script_runner"


# ── SchemaIntrospectorTool ───────────────────────────────────────────


class TestSchemaIntrospectorTool:
    def test_definition(self):
        tool = SchemaIntrospectorTool()
        defn = tool.definition
        assert defn.name == "schema_introspector"
        assert any(p.name == "query_type" for p in defn.parameters)

    def test_unknown_query_type(self):
        tool = SchemaIntrospectorTool()
        result = tool.execute(query_type="bogus")
        assert not result.success
        assert "Unknown" in result.error

    def test_columns_requires_object_name(self):
        tool = SchemaIntrospectorTool()
        result = tool.execute(query_type="columns")
        assert not result.success
        assert "object_name" in result.error

    def test_indexes_requires_object_name(self):
        tool = SchemaIntrospectorTool()
        result = tool.execute(query_type="indexes")
        assert not result.success

    @patch.object(SchemaIntrospectorTool, "_run_query")
    def test_tables_query(self, mock_run):
        mock_run.return_value = (
            [("dbo", "Vendors", "BASE TABLE"), ("dbo", "Items", "BASE TABLE")],
            ["TABLE_SCHEMA", "TABLE_NAME", "TABLE_TYPE"],
        )
        tool = SchemaIntrospectorTool()
        result = tool.execute(query_type="tables")
        assert result.success
        assert len(result.data) == 2
        assert result.data[0]["TABLE_NAME"] == "Vendors"

    @patch.object(SchemaIntrospectorTool, "_run_query")
    def test_columns_query(self, mock_run):
        mock_run.return_value = (
            [("Vendors", "VendorId", "int", None, "NO", None)],
            ["TABLE_NAME", "COLUMN_NAME", "DATA_TYPE", "CHARACTER_MAXIMUM_LENGTH", "IS_NULLABLE", "COLUMN_DEFAULT"],
        )
        tool = SchemaIntrospectorTool()
        result = tool.execute(query_type="columns", object_name="Vendors")
        assert result.success
        assert result.data[0]["COLUMN_NAME"] == "VendorId"

    def test_factory(self):
        tools = create_schema_tools()
        assert len(tools) == 1


# ── CatalogSearchTool ────────────────────────────────────────────────


class TestCatalogSearchTool:
    def test_definition(self):
        tool = CatalogSearchTool()
        defn = tool.definition
        assert defn.name == "catalog_search"

    def test_empty_search_rejected(self):
        tool = CatalogSearchTool()
        result = tool.execute(search_term="")
        assert not result.success

    def test_unknown_catalog(self):
        tool = CatalogSearchTool()
        result = tool.execute(search_term="test", catalog="bogus")
        assert not result.success
        assert "Unknown" in result.error

    @patch.object(CatalogSearchTool, "_run_search")
    def test_vendor_search(self, mock_run):
        mock_run.return_value = (
            [(9, "0009", "School Specialty, LLC")],
            ["VendorId", "VendorCode", "VendorName"],
        )
        tool = CatalogSearchTool()
        result = tool.execute(search_term="School Specialty", catalog="vendors")
        assert result.success
        assert result.data[0]["VendorName"] == "School Specialty, LLC"
        assert result.metadata["catalog"] == "vendors"

    def test_factory(self):
        tools = create_catalog_tools()
        assert len(tools) == 1


# ── ReportGeneratorTool ──────────────────────────────────────────────


class TestReportGeneratorTool:
    def test_definition(self):
        tool = ReportGeneratorTool()
        defn = tool.definition
        assert defn.name == "report_generator"
        assert any(p.name == "description" for p in defn.parameters)

    def test_empty_description_rejected(self):
        tool = ReportGeneratorTool()
        result = tool.execute(description="")
        assert not result.success

    @patch.object(ReportGeneratorTool, "_generate_plan")
    def test_preview_mode(self, mock_plan):
        mock_plan.return_value = json.dumps({
            "title": "Test Report",
            "description": "A test",
            "queries": [{"name": "q1", "sql": "SELECT 1", "description": "test"}],
            "sheets": [{"name": "s1", "title": "Sheet 1", "query": "q1"}],
        })
        tool = ReportGeneratorTool()
        result = tool.execute(description="Test report", preview_only=True)
        assert result.success
        assert result.data["title"] == "Test Report"
        assert result.metadata["phase"] == "preview"

    @patch.object(ReportGeneratorTool, "_generate_plan")
    def test_invalid_json_plan(self, mock_plan):
        mock_plan.return_value = "not valid json {"
        tool = ReportGeneratorTool()
        result = tool.execute(description="Bad report")
        assert not result.success
        assert "Invalid plan JSON" in result.error

    def test_factory(self):
        tools = create_report_tools({"llm": {"default_provider": "ollama"}})
        assert len(tools) == 1


# ── Export Models ────────────────────────────────────────────────────


class TestExportModels:
    def test_column_def(self):
        col = ColumnDef(name="Amount", type="currency", header="Total Amount", width=20)
        assert col.format is None

    def test_query_def(self):
        q = QueryDef(sql="SELECT 1", name="test_query")
        assert q.description == ""

    def test_report_plan(self):
        plan = ReportPlan(
            title="Test",
            description="Test report",
            queries=[QueryDef(sql="SELECT 1", name="q1")],
            sheets=[SheetDef(name="s1", title="Sheet 1", query="q1")],
        )
        assert len(plan.queries) == 1
        assert len(plan.sheets) == 1


# ── Excel Formatter ──────────────────────────────────────────────────


class TestExcelFormatter:
    def test_eds_colors(self):
        assert EDSColors.PRIMARY == "1C1A83"
        assert EDSColors.ACCENT == "B70C0D"

    def test_format_map(self):
        assert FORMAT_MAP["currency"] == "$#,##0.00"
        assert FORMAT_MAP["percentage"] == "0.00%"
        assert "date" in FORMAT_MAP


# ── GUI State ────────────────────────────────────────────────────────


class TestGUIState:
    def test_app_state_defaults(self):
        from agent.gui.state import AppState, Theme
        state = AppState()
        assert state.theme == Theme.SYSTEM
        assert state.messages == []
        assert state.is_loading is False
        assert state.current_session_id is None

    def test_alert(self):
        from agent.gui.state import Alert
        alert = Alert(type="error", message="Something broke")
        assert alert.timeout == 5

    def test_theme_enum(self):
        from agent.gui.state import Theme
        assert Theme.LIGHT.value == "light"
        assert Theme.DARK.value == "dark"
