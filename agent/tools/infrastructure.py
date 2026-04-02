"""Infrastructure lookup tool — queries the agent's infrastructure knowledge.

Provides the LLM with detailed information about the EDS Azure infrastructure,
SQL Server, Kubernetes clusters, known issues, and monitoring thresholds.
"""

import json
import logging
from typing import Any, Dict, List, Optional

from agent.tools.base import (
    BaseTool,
    ToolCategory,
    ToolDefinition,
    ToolParameter,
    ToolResult,
)

logger = logging.getLogger(__name__)


class InfrastructureTool(BaseTool):
    """Look up EDS infrastructure details: servers, databases, issues, services."""

    name = "infrastructure_lookup"
    category = ToolCategory.MONITORING

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name=self.name,
            description=(
                "Look up EDS infrastructure details: SQL Server config, database inventory, "
                "known performance issues, Kubernetes services, Elasticsearch status, "
                "monitoring thresholds, and usage patterns."
            ),
            parameters=[
                ToolParameter(
                    name="query_type",
                    type="string",
                    description="What to look up.",
                    enum=[
                        "sql_server", "databases", "critical_tables",
                        "known_issues", "kubernetes", "elasticsearch",
                        "services", "accounts", "usage_patterns",
                        "monitoring_thresholds", "issue_detail",
                    ],
                ),
                ToolParameter(
                    name="detail_id",
                    type="string",
                    description="Specific ID for detail lookups (e.g. 'KI-001' for issue_detail, 'EDS' for databases).",
                    required=False,
                    default="",
                ),
            ],
            category=self.category,
            returns="Infrastructure information as JSON.",
        )

    def execute(self, **kwargs) -> ToolResult:
        query_type = kwargs.get("query_type", "")
        detail_id = kwargs.get("detail_id", "")

        from agent.core.infrastructure import (
            CRITICAL_TABLES, DATABASES, DB_ACCOUNTS, KNOWN_ISSUES,
            K8S_CLUSTERS, PROD_SERVICES, PEAK_HOURS, ANNUAL_CYCLE,
            HEALTH_THRESHOLDS, SQLServerInfo, ElasticsearchInfo,
            get_known_issue, get_database_info,
        )
        from dataclasses import asdict

        if query_type == "sql_server":
            data = asdict(SQLServerInfo())
        elif query_type == "databases":
            if detail_id:
                db = get_database_info(detail_id)
                data = asdict(db) if db else {"error": f"Database '{detail_id}' not found"}
            else:
                data = [asdict(d) for d in DATABASES]
        elif query_type == "critical_tables":
            data = [asdict(t) for t in CRITICAL_TABLES]
        elif query_type == "known_issues":
            data = [asdict(ki) for ki in KNOWN_ISSUES]
        elif query_type == "issue_detail":
            if not detail_id:
                return ToolResult(success=False, error="detail_id required for issue_detail (e.g. 'KI-001')")
            ki = get_known_issue(detail_id)
            data = asdict(ki) if ki else {"error": f"Issue '{detail_id}' not found"}
        elif query_type == "kubernetes":
            data = [asdict(c) for c in K8S_CLUSTERS]
        elif query_type == "elasticsearch":
            data = asdict(ElasticsearchInfo())
        elif query_type == "services":
            data = [asdict(s) for s in PROD_SERVICES]
        elif query_type == "accounts":
            data = DB_ACCOUNTS
        elif query_type == "usage_patterns":
            data = {"peak_hours": PEAK_HOURS, "annual_cycle": ANNUAL_CYCLE}
        elif query_type == "monitoring_thresholds":
            data = HEALTH_THRESHOLDS
        else:
            return ToolResult(
                success=False,
                error=f"Unknown query_type '{query_type}'.",
            )

        return ToolResult(success=True, data=data)


def create_infrastructure_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    return [InfrastructureTool()]
