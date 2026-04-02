"""Query generator tool — converts natural language to SQL using the LLM.

Uses the configured LLM provider to translate a natural language description
into a SQL Server query, given schema context about the EDS database.
"""

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

# Schema context injected into the LLM prompt for SQL generation
EDS_SCHEMA_CONTEXT = """Key EDS database tables and relationships:

-- Vendors & Products
Vendors(VendorId PK, VendorCode, VendorName, VendorAddress, ...)
Items(ItemId PK, VendorId FK, ItemNumber, Description, UnitOfMeasure, ...)
Category(CategoryId PK, CategoryName, ParentCategoryId, ...)

-- Bidding & Pricing
BidHeaders(BidHeaderId PK, BidNumber, BidName, BidYear, StartDate, EndDate, StatusId, ...)
BidTrades(BidTradeId PK, BidHeaderId FK, TradeName, ...)
BidImports(BidImportId PK, BidHeaderId FK, VendorId FK, ...)
Awards(AwardId PK, BidHeaderId FK, VendorId FK, AwardDate, ...)

-- Orders & Purchasing
Requisitions(RequisitionId PK, DistrictId FK, SchoolId FK, UserId FK, StatusId, CreatedDate, ...)
RequisitionItems(RequisitionItemId PK, RequisitionId FK, ItemId FK, Quantity, UnitPrice, ...)
PurchaseOrders(PurchaseOrderId PK, PONumber, VendorId FK, DistrictId FK, OrderDate, ...)
PurchaseOrderDetails(DetailId PK, PurchaseOrderId FK, ItemId FK, Quantity, UnitPrice, ExtendedPrice, ...)

-- Organization
Districts(DistrictId PK, DistrictName, DistrictCode, StateCode, ...)
Schools(SchoolId PK, DistrictId FK, SchoolName, ...)
Users(UserId PK, DistrictId FK, UserNumber, FirstName, LastName, RoleId, ...)

-- Reference
StatusTable(StatusId PK, StatusName, StatusDescription)

Key conventions:
- Use BidHeaderId (not BidHeaderKey) for bid references
- Budget year runs Dec 1 – Nov 30
- Most recent completed budget year: Dec 1, 2024 – Nov 30, 2025
"""

SQL_GENERATION_PROMPT = """You are a SQL Server expert. Generate a SQL query based on the user's description.

{schema_context}

Rules:
- Write T-SQL compatible with SQL Server 2017
- Use explicit column names (never SELECT *)
- Use table aliases for readability
- Include appropriate JOINs based on the schema
- Add ORDER BY for deterministic results where applicable
- Use TOP or pagination for large result sets
- Do NOT include any explanation, only the SQL query
- Do NOT wrap the query in markdown code fences

User request: {description}

Additional context: {context}

SQL query:"""


class QueryGeneratorTool(BaseTool):
    """Generate SQL queries from natural language using the LLM."""

    name = "query_generator"
    category = ToolCategory.SQL

    def __init__(self, provider_name: str = "ollama"):
        self._provider_name = provider_name

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name=self.name,
            description=(
                "Generate a SQL Server query from a natural language description. "
                "Uses the LLM with EDS schema context to produce correct T-SQL."
            ),
            parameters=[
                ToolParameter(
                    name="description",
                    type="string",
                    description="Natural language description of the desired query.",
                ),
                ToolParameter(
                    name="context",
                    type="string",
                    description="Additional context about tables or columns to use.",
                    required=False,
                    default="",
                ),
            ],
            category=self.category,
            returns="Generated SQL query string.",
        )

    def execute(self, **kwargs) -> ToolResult:
        description: str = kwargs.get("description", "")
        context: str = kwargs.get("context", "")

        if not description.strip():
            return ToolResult(success=False, error="Empty description")

        try:
            from agent.llm.base import Message, MessageRole
            from agent.llm.registry import get_provider
            from agent.config import get_llm_config

            provider_config = get_llm_config(self._provider_name)
            provider = get_provider(self._provider_name, provider_config)

            prompt = SQL_GENERATION_PROMPT.format(
                schema_context=EDS_SCHEMA_CONTEXT,
                description=description,
                context=context or "None",
            )

            messages = [
                Message(role=MessageRole.USER, content=prompt),
            ]

            response = provider.complete(messages, temperature=0.0)
            sql = response.content.strip()

            # Strip markdown code fences if the LLM included them anyway
            if sql.startswith("```"):
                lines = sql.split("\n")
                # Remove first and last fence lines
                lines = [l for l in lines if not l.strip().startswith("```")]
                sql = "\n".join(lines).strip()

            return ToolResult(
                success=True,
                data=sql,
                metadata={
                    "provider": self._provider_name,
                    "model": response.model,
                    "usage": response.usage,
                },
            )

        except Exception as e:
            logger.error("Query generation failed: %s", e)
            return ToolResult(
                success=False,
                error=f"Generation error: {e}",
            )


def create_query_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    """Factory function to create query generator tools from config."""
    config = config or {}
    provider_name = config.get("llm", {}).get("default_provider", "ollama")

    return [
        QueryGeneratorTool(provider_name=provider_name),
    ]
