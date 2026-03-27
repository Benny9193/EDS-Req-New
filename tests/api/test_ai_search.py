"""
Tests for AI-powered product search endpoint.

Mocks _generate_product_sql so no real LLM calls are made.
"""

import pytest
from unittest.mock import patch, MagicMock
from fastapi import HTTPException


# ============================================
# Mock helpers
# ============================================

SAMPLE_SQL = """
SELECT
    i.ItemId as id,
    i.ItemCode as item_code,
    i.Description as name,
    ISNULL(i.ShortDescription, '') as description,
    COALESCE(v.Name, 'Unknown Vendor') as vendor,
    i.VendorPartNumber as vendor_item_code,
    ISNULL(c.Name, 'General') as category,
    NULL as image,
    CASE WHEN i.Active = 0 THEN 'discontinued' ELSE 'in-stock' END as status,
    ISNULL(u.Code, 'Each') as unit_of_measure,
    ISNULL(i.ListPrice, 0) as unit_price
FROM Items i
LEFT JOIN Vendors v ON i.VendorId = v.VendorId
LEFT JOIN Units u ON i.UnitId = u.UnitId
LEFT JOIN Category c ON i.CategoryId = c.CategoryId
WHERE i.Active = 1 AND i.Description LIKE '%pencil%'
ORDER BY i.Description ASC
OFFSET 0 ROWS FETCH NEXT 20 ROWS ONLY
""".strip()

SAMPLE_ROWS = [
    {
        "id": 100,
        "item_code": "PEN-001",
        "name": "Yellow Pencil #2",
        "description": "Standard school pencil",
        "vendor": "Staples",
        "vendor_item_code": "STP-PEN-2",
        "category": "Writing Supplies",
        "image": None,
        "status": "in-stock",
        "unit_of_measure": "Each",
        "unit_price": 0.50,
    },
    {
        "id": 101,
        "item_code": "PEN-002",
        "name": "Mechanical Pencil",
        "description": "0.7mm mechanical pencil",
        "vendor": "Office Depot",
        "vendor_item_code": "OD-MP-07",
        "category": "Writing Supplies",
        "image": "https://example.com/pencil.jpg",
        "status": "in-stock",
        "unit_of_measure": "Each",
        "unit_price": 2.99,
    },
]


def _mock_generate_result(sql=SAMPLE_SQL, explanation="Searches for pencil products"):
    """Return dict matching _generate_product_sql output."""
    return {"sql": sql, "explanation": explanation}


# ============================================
# AI Search Endpoint Tests
# ============================================

class TestAISearchEndpoint:
    """Test POST /api/products/ai-search."""

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search.execute_query")
    @patch("api.routes.ai_search._generate_product_sql")
    def test_successful_search(self, mock_gen, mock_exec_query, test_client):
        """Valid query returns products with AI metadata."""
        mock_gen.return_value = _mock_generate_result()
        mock_exec_query.return_value = SAMPLE_ROWS

        response = test_client.post("/api/products/ai-search", json={
            "query": "pencils for school",
        })
        assert response.status_code == 200
        data = response.json()
        assert len(data["products"]) == 2
        assert data["products"][0]["name"] == "Yellow Pencil #2"
        assert data["products"][1]["vendor"] == "Office Depot"
        assert data["ai_explanation"] == "Searches for pencil products"
        assert "Items" in data["generated_sql"]
        assert data["page"] == 1
        assert data["page_size"] == 20

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search.execute_query")
    @patch("api.routes.ai_search._generate_product_sql")
    def test_search_with_pagination(self, mock_gen, mock_exec_query, test_client):
        """Custom page and page_size are passed through."""
        mock_gen.return_value = _mock_generate_result()
        mock_exec_query.return_value = SAMPLE_ROWS[:1]

        response = test_client.post("/api/products/ai-search", json={
            "query": "cheap pens",
            "page": 3,
            "page_size": 10,
        })
        assert response.status_code == 200
        data = response.json()
        assert data["page"] == 3
        assert data["page_size"] == 10

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search.execute_query")
    @patch("api.routes.ai_search._generate_product_sql")
    def test_empty_results(self, mock_gen, mock_exec_query, test_client):
        """No matching products returns empty list."""
        mock_gen.return_value = _mock_generate_result()
        mock_exec_query.return_value = []

        response = test_client.post("/api/products/ai-search", json={
            "query": "unicorn glitter pens",
        })
        assert response.status_code == 200
        data = response.json()
        assert data["products"] == []
        assert data["total"] == 0

    def test_query_too_short(self, test_client):
        """Query under 3 characters returns 422."""
        response = test_client.post("/api/products/ai-search", json={
            "query": "ab",
        })
        assert response.status_code == 422

    def test_query_too_long(self, test_client):
        """Query over 300 characters returns 422."""
        response = test_client.post("/api/products/ai-search", json={
            "query": "x" * 301,
        })
        assert response.status_code == 422

    def test_missing_query(self, test_client):
        """Missing query field returns 422."""
        response = test_client.post("/api/products/ai-search", json={})
        assert response.status_code == 422

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", False)
    def test_disabled_returns_503(self, test_client):
        """When API key is not configured, returns 503."""
        response = test_client.post("/api/products/ai-search", json={
            "query": "pencils",
        })
        assert response.status_code == 503
        assert "not available" in response.json()["detail"]


# ============================================
# SQL Validation Tests
# ============================================

class TestSQLValidation:
    """Test that generated SQL is validated for safety."""

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search._generate_product_sql")
    def test_blocks_drop_statement(self, mock_gen, test_client):
        """DROP TABLE in generated SQL is blocked."""
        mock_gen.return_value = _mock_generate_result(
            sql="DROP TABLE Items; SELECT * FROM Items"
        )
        response = test_client.post("/api/products/ai-search", json={
            "query": "delete all products",
        })
        assert response.status_code == 400
        detail = response.json()["detail"]
        assert "blocked" in detail.lower() or "non-SELECT" in detail

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search._generate_product_sql")
    def test_blocks_delete_statement(self, mock_gen, test_client):
        """DELETE in generated SQL is blocked."""
        mock_gen.return_value = _mock_generate_result(
            sql="DELETE FROM Items WHERE Active = 0"
        )
        response = test_client.post("/api/products/ai-search", json={
            "query": "remove inactive products",
        })
        assert response.status_code == 400

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search._generate_product_sql")
    def test_blocks_update_statement(self, mock_gen, test_client):
        """UPDATE in generated SQL is blocked."""
        mock_gen.return_value = _mock_generate_result(
            sql="UPDATE Items SET ListPrice = 0 WHERE 1=1"
        )
        response = test_client.post("/api/products/ai-search", json={
            "query": "set all prices to zero",
        })
        assert response.status_code == 400

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search._generate_product_sql")
    def test_blocks_query_without_items_table(self, mock_gen, test_client):
        """Query not referencing Items table is blocked."""
        mock_gen.return_value = _mock_generate_result(
            sql="SELECT * FROM Vendors WHERE Name LIKE '%test%'"
        )
        response = test_client.post("/api/products/ai-search", json={
            "query": "show all vendors",
        })
        assert response.status_code == 400
        assert "Items" in response.json()["detail"]

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search._generate_product_sql")
    def test_blocks_empty_sql(self, mock_gen, test_client):
        """Empty SQL from generator returns 500."""
        mock_gen.return_value = _mock_generate_result(sql="")
        response = test_client.post("/api/products/ai-search", json={
            "query": "something weird",
        })
        assert response.status_code == 500


# ============================================
# Generator Failure Tests
# ============================================

class TestGeneratorFailures:
    """Test graceful handling of query generator failures."""

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search._generate_product_sql")
    def test_generator_returns_http_error(self, mock_gen, test_client):
        """When generator raises HTTPException (tool failure), it propagates."""
        mock_gen.side_effect = HTTPException(
            status_code=500,
            detail="AI query generation failed: LLM provider not available",
        )
        response = test_client.post("/api/products/ai-search", json={
            "query": "find some pencils",
        })
        assert response.status_code == 500
        assert "generation failed" in response.json()["detail"]

    @patch("api.routes.ai_search.AI_SEARCH_ENABLED", True)
    @patch("api.routes.ai_search._generate_product_sql")
    def test_generator_exception(self, mock_gen, test_client):
        """When generator raises unexpected exception, endpoint returns 500."""
        mock_gen.side_effect = RuntimeError("connection refused")
        response = test_client.post("/api/products/ai-search", json={
            "query": "find some pencils",
        })
        assert response.status_code == 500
        assert "error" in response.json()["detail"].lower()
