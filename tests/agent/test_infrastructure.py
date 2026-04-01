"""Tests for infrastructure knowledge module and tool."""

import json
import pytest
from unittest.mock import MagicMock, patch

from agent.core.infrastructure import (
    CRITICAL_TABLES,
    DATABASES,
    DB_ACCOUNTS,
    KNOWN_ISSUES,
    K8S_CLUSTERS,
    PROD_SERVICES,
    SQLServerInfo,
    ElasticsearchInfo,
    get_database_info,
    get_infrastructure_prompt,
    get_known_issue,
)
from agent.tools.infrastructure import InfrastructureTool


# ── Infrastructure Data ──────────────────────────────────────────────


class TestInfrastructureData:
    def test_sql_server_info(self):
        sql = SQLServerInfo()
        assert sql.fqdn == "eds-sqlserver.eastus2.cloudapp.azure.com"
        assert sql.port == 1433
        assert "2017" in sql.version
        assert sql.vcpus == 16
        assert sql.memory_gb == 64

    def test_elasticsearch_info(self):
        es = ElasticsearchInfo()
        assert es.version == "7.15.2"
        assert es.active_index == "pricing_consolidated_60"
        assert "18.6M" in es.active_docs

    def test_databases_populated(self):
        assert len(DATABASES) >= 10
        eds = next(d for d in DATABASES if d.name == "EDS")
        assert eds.tables == 439
        assert "1.48 TB" in eds.size

    def test_critical_tables_populated(self):
        assert len(CRITICAL_TABLES) >= 10
        crossrefs = next(t for t in CRITICAL_TABLES if t.name == "CrossRefs")
        assert "150.6M" in crossrefs.rows

    def test_known_issues_populated(self):
        assert len(KNOWN_ISSUES) == 5
        ki001 = KNOWN_ISSUES[0]
        assert ki001.id == "KI-001"
        assert ki001.severity == "CRITICAL"

    def test_k8s_clusters(self):
        assert len(K8S_CLUSTERS) == 2
        prod = next(c for c in K8S_CLUSTERS if "prod" in c.name)
        assert prod.nodes == 13

    def test_prod_services(self):
        assert len(PROD_SERVICES) >= 10
        edsiq = next(s for s in PROD_SERVICES if s.name == "eds-edsiq")
        assert edsiq.ip == "52.251.10.10"

    def test_db_accounts(self):
        assert "EDSIQWebUser" in DB_ACCOUNTS
        assert "EDSAdmin" in DB_ACCOUNTS


# ── Lookup Functions ─────────────────────────────────────────────────


class TestLookups:
    def test_get_known_issue(self):
        ki = get_known_issue("KI-001")
        assert ki is not None
        assert ki.severity == "CRITICAL"

    def test_get_known_issue_case_insensitive(self):
        ki = get_known_issue("ki-003")
        assert ki is not None
        assert "trig_DetailUpdate" in ki.title

    def test_get_known_issue_missing(self):
        assert get_known_issue("KI-999") is None

    def test_get_database_info(self):
        db = get_database_info("EDS")
        assert db is not None
        assert db.tables == 439

    def test_get_database_info_case_insensitive(self):
        db = get_database_info("eds")
        assert db is not None

    def test_get_database_info_missing(self):
        assert get_database_info("nonexistent") is None


# ── Infrastructure Prompt ────────────────────────────────────────────


class TestInfrastructurePrompt:
    def test_prompt_generated(self):
        prompt = get_infrastructure_prompt()
        assert isinstance(prompt, str)
        assert len(prompt) > 500

    def test_prompt_contains_sql_server(self):
        prompt = get_infrastructure_prompt()
        assert "eds-sqlserver" in prompt
        assert "1433" in prompt
        assert "SQL Server 2017" in prompt

    def test_prompt_contains_databases(self):
        prompt = get_infrastructure_prompt()
        assert "EDS" in prompt
        assert "1.48 TB" in prompt

    def test_prompt_contains_known_issues(self):
        prompt = get_infrastructure_prompt()
        assert "KI-001" in prompt
        assert "CRITICAL" in prompt

    def test_prompt_contains_elasticsearch(self):
        prompt = get_infrastructure_prompt()
        assert "pricing_consolidated_60" in prompt

    def test_prompt_contains_usage_patterns(self):
        prompt = get_infrastructure_prompt()
        assert "Peak hours" in prompt or "8:00" in prompt
        assert "maintenance" in prompt.lower()


# ── Infrastructure Tool ──────────────────────────────────────────────


class TestInfrastructureTool:
    @pytest.fixture
    def tool(self):
        return InfrastructureTool()

    def test_definition(self, tool):
        defn = tool.definition
        assert defn.name == "infrastructure_lookup"
        assert any(p.name == "query_type" for p in defn.parameters)

    def test_sql_server(self, tool):
        result = tool.execute(query_type="sql_server")
        assert result.success
        assert result.data["fqdn"] == "eds-sqlserver.eastus2.cloudapp.azure.com"

    def test_databases_list(self, tool):
        result = tool.execute(query_type="databases")
        assert result.success
        assert isinstance(result.data, list)
        assert len(result.data) >= 10

    def test_databases_detail(self, tool):
        result = tool.execute(query_type="databases", detail_id="EDS")
        assert result.success
        assert result.data["name"] == "EDS"

    def test_databases_not_found(self, tool):
        result = tool.execute(query_type="databases", detail_id="bogus")
        assert result.success
        assert "error" in result.data

    def test_critical_tables(self, tool):
        result = tool.execute(query_type="critical_tables")
        assert result.success
        assert len(result.data) >= 10

    def test_known_issues(self, tool):
        result = tool.execute(query_type="known_issues")
        assert result.success
        assert len(result.data) == 5

    def test_issue_detail(self, tool):
        result = tool.execute(query_type="issue_detail", detail_id="KI-001")
        assert result.success
        assert result.data["severity"] == "CRITICAL"

    def test_issue_detail_missing_id(self, tool):
        result = tool.execute(query_type="issue_detail")
        assert not result.success

    def test_kubernetes(self, tool):
        result = tool.execute(query_type="kubernetes")
        assert result.success
        assert len(result.data) == 2

    def test_elasticsearch(self, tool):
        result = tool.execute(query_type="elasticsearch")
        assert result.success
        assert result.data["version"] == "7.15.2"

    def test_services(self, tool):
        result = tool.execute(query_type="services")
        assert result.success
        assert len(result.data) >= 10

    def test_accounts(self, tool):
        result = tool.execute(query_type="accounts")
        assert result.success
        assert "EDSIQWebUser" in result.data

    def test_usage_patterns(self, tool):
        result = tool.execute(query_type="usage_patterns")
        assert result.success
        assert "peak_hours" in result.data

    def test_monitoring_thresholds(self, tool):
        result = tool.execute(query_type="monitoring_thresholds")
        assert result.success
        assert "blocking_critical_minutes" in result.data

    def test_unknown_query_type(self, tool):
        result = tool.execute(query_type="bogus")
        assert not result.success


# ── Agent Integration ────────────────────────────────────────────────


class TestAgentInfraIntegration:
    @patch("agent.core.agent.get_provider")
    def test_infra_context_in_system_prompt(self, mock_provider):
        from agent.core.agent import EDSAgent
        from agent.llm.base import LLMResponse

        mock_llm = MagicMock()
        mock_llm.model_name = "test"
        mock_llm.complete.return_value = LLMResponse(
            content="response", model="test", tool_calls=[],
            usage={"input_tokens": 10, "output_tokens": 5},
        )
        mock_provider.return_value = mock_llm

        agent = EDSAgent()
        agent._llm_provider = mock_llm
        agent._provider_name = "test"
        agent.chat("What SQL Server version do we run?")

        messages = mock_llm.complete.call_args[0][0]
        system_msg = messages[0].content
        assert "eds-sqlserver" in system_msg
        assert "KI-001" in system_msg
        assert "pricing_consolidated_60" in system_msg
