"""Report generator tool — LLM-driven Excel report planning and building.

Two-phase process: the LLM generates a ReportPlan (SQL queries + sheet
definitions), then the ReportBuilder executes them into a formatted Excel file.
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

REPORT_PLAN_PROMPT = """Generate a JSON report plan for the following request.
The plan should have this structure:
{{
  "title": "Report Title",
  "description": "What this report shows",
  "queries": [
    {{
      "name": "query_name",
      "sql": "SELECT ... FROM ... WHERE ...",
      "description": "What this query returns"
    }}
  ],
  "sheets": [
    {{
      "name": "sheet_name",
      "title": "Sheet Display Title",
      "query": "query_name",
      "columns": [
        {{"name": "ColumnName", "type": "string", "header": "Display Header", "width": 15, "format": null}}
      ]
    }}
  ]
}}

Column types: string, number, currency, percentage, date
Format values: currency, percentage, integer, date, datetime (or null)

Use T-SQL compatible with SQL Server 2017. Use explicit column names.
Key tables: Vendors, Items, PurchaseOrders, PurchaseOrderDetails, Requisitions, BidHeaders, Districts, Schools.

Request: {description}

Return ONLY the JSON, no explanation."""


class ReportGeneratorTool(BaseTool):
    """Generate Excel reports via LLM-planned queries."""

    name = "report_generator"
    category = ToolCategory.ANALYSIS

    def __init__(
        self,
        provider_name: str = "ollama",
        output_dir: str = "output",
        max_rows: int = 50_000,
    ):
        self._provider_name = provider_name
        self._output_dir = output_dir
        self._max_rows = max_rows

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name=self.name,
            description=(
                "Generate an Excel report from a natural language description. "
                "The LLM creates a report plan (SQL queries + sheets), then "
                "the report builder executes it and produces an .xlsx file."
            ),
            parameters=[
                ToolParameter(
                    name="description",
                    type="string",
                    description="Natural language description of the desired report.",
                ),
                ToolParameter(
                    name="preview_only",
                    type="boolean",
                    description="If true, return the plan without executing it.",
                    required=False,
                    default=False,
                ),
            ],
            category=self.category,
            returns="Report file path or preview of the report plan.",
        )

    def execute(self, **kwargs) -> ToolResult:
        description: str = kwargs.get("description", "")
        preview_only: bool = kwargs.get("preview_only", False)

        if not description.strip():
            return ToolResult(success=False, error="Empty description")

        # Phase 1: Generate report plan via LLM
        try:
            plan_json = self._generate_plan(description)
        except Exception as e:
            return ToolResult(success=False, error=f"Plan generation failed: {e}")

        try:
            plan_dict = json.loads(plan_json)
        except json.JSONDecodeError as e:
            return ToolResult(
                success=False,
                error=f"Invalid plan JSON: {e}",
                metadata={"raw_plan": plan_json[:500]},
            )

        if preview_only:
            return ToolResult(
                success=True,
                data=plan_dict,
                metadata={"phase": "preview"},
            )

        # Phase 2: Build the report
        try:
            from agent.export.models import ColumnDef, QueryDef, ReportPlan, SheetDef
            from agent.export.report_builder import ReportBuilder

            queries = [
                QueryDef(sql=q["sql"], name=q["name"], description=q.get("description", ""))
                for q in plan_dict.get("queries", [])
            ]
            sheets = [
                SheetDef(
                    name=s["name"],
                    title=s["title"],
                    query=s["query"],
                    columns=[
                        ColumnDef(**c) for c in s.get("columns", [])
                    ],
                )
                for s in plan_dict.get("sheets", [])
            ]
            report_plan = ReportPlan(
                title=plan_dict.get("title", "Report"),
                description=plan_dict.get("description", ""),
                queries=queries,
                sheets=sheets,
            )

            builder = ReportBuilder(
                output_dir=self._output_dir,
                max_rows=self._max_rows,
            )
            result = builder.build(report_plan)

            return ToolResult(
                success=True,
                data=result,
                metadata={"phase": "complete", "plan": plan_dict},
            )

        except Exception as e:
            return ToolResult(success=False, error=f"Report build failed: {e}")

    def _generate_plan(self, description: str) -> str:
        from agent.llm.base import Message, MessageRole
        from agent.llm.registry import get_provider
        from agent.config import get_llm_config

        provider_config = get_llm_config(self._provider_name)
        provider = get_provider(self._provider_name, provider_config)

        prompt = REPORT_PLAN_PROMPT.format(description=description)
        messages = [Message(role=MessageRole.USER, content=prompt)]
        response = provider.complete(messages, temperature=0.0)

        text = response.content.strip()
        # Strip markdown fences
        if text.startswith("```"):
            lines = text.split("\n")
            lines = [l for l in lines if not l.strip().startswith("```")]
            text = "\n".join(lines).strip()

        return text


def create_report_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    config = config or {}
    llm_config = config.get("llm", {})
    reports_config = config.get("reports", {})
    return [
        ReportGeneratorTool(
            provider_name=llm_config.get("default_provider", "ollama"),
            output_dir=reports_config.get("output_dir", "output"),
            max_rows=reports_config.get("max_rows", 50_000),
        ),
    ]
