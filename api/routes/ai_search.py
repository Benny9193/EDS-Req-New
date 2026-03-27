"""
AI-powered product search endpoint.

Uses the DBA Agent's query generator to convert natural language
queries into SQL against the Items/Products catalog.
"""

import os
import re
import logging
from typing import Optional
from pydantic import BaseModel, Field
from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse

from ..database import execute_query
from ..models import Product, ProductListResponse
from .products import map_row_to_product, clean_string

router = APIRouter(prefix="/products", tags=["AI Search"])
logger = logging.getLogger(__name__)

# Provider configuration: use LLM_PROVIDER env var, or auto-detect
_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
_LLM_PROVIDER = os.getenv("LLM_PROVIDER", "claude" if _API_KEY else "ollama")

# Feature flag: enabled when any provider is configured
AI_SEARCH_ENABLED = bool(_API_KEY) or _LLM_PROVIDER == "ollama"

# Maximum query length for AI search
MAX_AI_QUERY_LENGTH = 300

# SQL patterns that are NOT allowed in generated queries
_BLOCKED_SQL_PATTERNS = re.compile(
    r"\b(DROP|DELETE|UPDATE|INSERT|ALTER|CREATE|TRUNCATE|EXEC|EXECUTE|"
    r"xp_|sp_configure|OPENROWSET|BULK|UNION|INTO|GRANT|REVOKE|SHUTDOWN)\b",
    re.IGNORECASE,
)


class AISearchRequest(BaseModel):
    """Request body for AI-powered search."""
    query: str = Field(
        ...,
        min_length=3,
        max_length=MAX_AI_QUERY_LENGTH,
        description="Natural language search query",
    )
    page: int = Field(1, ge=1, le=1000, description="Page number")
    page_size: int = Field(20, ge=1, le=100, description="Items per page")


class AISearchResponse(BaseModel):
    """Extended product list response with AI metadata."""
    products: list[Product]
    total: int
    page: int
    page_size: int
    total_pages: int
    ai_explanation: str = Field("", description="AI explanation of the search interpretation")
    generated_sql: str = Field("", description="The SQL query that was generated")


def _validate_generated_sql(sql: str) -> None:
    """
    Validate that generated SQL is safe to execute.
    Raises HTTPException if unsafe patterns detected.
    """
    if not sql:
        raise HTTPException(status_code=500, detail="AI failed to generate a SQL query")

    # Must be a SELECT statement
    stripped = sql.strip().upper()
    if not stripped.startswith("SELECT"):
        raise HTTPException(
            status_code=400,
            detail="AI generated a non-SELECT query. Only search queries are allowed.",
        )

    # Block dangerous patterns
    if _BLOCKED_SQL_PATTERNS.search(sql):
        raise HTTPException(
            status_code=400,
            detail="AI generated query contains blocked SQL operations",
        )

    # Must reference Items table
    if "items" not in sql.lower():
        raise HTTPException(
            status_code=400,
            detail="AI generated query does not reference the Items table",
        )


def _generate_product_sql(natural_language: str, page: int, page_size: int) -> dict:
    """
    Use the agent's query generator to convert natural language to SQL.

    Returns dict with 'sql' and 'explanation' keys.
    """
    from agent.tools.query_generator import QueryGeneratorTool, PRODUCT_SCHEMA_CONTEXT

    config = {
        "provider": _LLM_PROVIDER,
        "schema_context": PRODUCT_SCHEMA_CONTEXT,
    }
    tool = QueryGeneratorTool(config=config)

    # Add pagination context to the question
    offset = (page - 1) * page_size
    question = (
        f"{natural_language}\n\n"
        f"Return {page_size} results starting at offset {offset} "
        f"(page {page}, page_size {page_size}). "
        f"Use OFFSET/FETCH NEXT for pagination."
    )

    result = tool.execute(question=question, database="EDS", include_explanation=True)

    if not result.success:
        raise HTTPException(
            status_code=500,
            detail="AI query generation failed",
        )

    return result.data


@router.post("/ai-search", response_model=AISearchResponse)
async def ai_search(request: AISearchRequest):
    """
    AI-powered product search using natural language.

    Accepts natural language queries like:
    - "red pencils under $5"
    - "paper products from Staples sorted by price"
    - "cheapest notebooks in Writing Supplies category"

    Converts the query to SQL using an LLM, validates it for safety,
    executes it, and returns results in the standard Product format.
    """
    if not AI_SEARCH_ENABLED:
        raise HTTPException(
            status_code=503,
            detail="AI search is not available. Configure ANTHROPIC_API_KEY or set LLM_PROVIDER=ollama.",
        )

    try:
        # Generate SQL from natural language
        ai_result = _generate_product_sql(
            request.query, request.page, request.page_size,
        )

        sql = ai_result.get("sql", "")
        explanation = ai_result.get("explanation", "")

        # Validate the generated SQL
        _validate_generated_sql(sql)

        # Execute the query
        rows = execute_query(sql)

        # Map rows to Product models
        products = []
        for row in rows:
            try:
                products.append(map_row_to_product(row))
            except Exception as e:
                logger.warning("Failed to map AI search row: %s", e)
                continue

        # Estimate total (AI queries don't always include COUNT)
        total = len(products)
        if total == request.page_size:
            # Likely more results; estimate higher
            total = request.page_size * (request.page + 1)
        total_pages = max(1, -(-total // request.page_size))  # ceil division

        return AISearchResponse(
            products=products,
            total=total,
            page=request.page,
            page_size=request.page_size,
            total_pages=total_pages,
            ai_explanation=explanation,
            generated_sql=sql,
        )

    except HTTPException:
        raise
    except Exception as e:
        logger.error("AI search failed: %s", e, exc_info=True)
        raise HTTPException(
            status_code=500,
            detail="AI search encountered an error",
        )
