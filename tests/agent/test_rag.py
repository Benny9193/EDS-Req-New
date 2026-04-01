"""Tests for the RAG pipeline: chunker, BM25, retriever, and indexer."""

import pytest
from unittest.mock import MagicMock, patch

from agent.rag.chunker import (
    ChunkType,
    DocumentChunk,
    DocumentChunker,
)
from agent.rag.retriever import BM25Index, HybridRetriever, RetrievalResult


# ── Sample documents ─────────────────────────────────────────────────

SAMPLE_MD = """# Vendors Overview

The EDS system tracks vendors who supply products to schools.

## Vendor Table

| Column | Type | Description |
|--------|------|-------------|
| VendorId | INT | Primary key |
| VendorName | VARCHAR | Vendor name |

## Key Queries

```sql
SELECT VendorId, VendorName
FROM Vendors
WHERE VendorName LIKE '%School%'
```

## Vendor Workflows

When a new vendor is onboarded, the following steps occur:
1. Application submission
2. Background check
3. Contract negotiation
4. Catalog upload
"""

SCHEMA_MD = """# EDS Schema

## Vendors Table

VendorId INT PK
VendorName VARCHAR(200)
VendorCode VARCHAR(10)

## Items Table

ItemId INT PK
VendorId INT FK
Description VARCHAR(500)
"""

PROCEDURE_MD = """# Stored Procedures

## sp_GetVendors

Returns active vendors with optional filtering.

Parameters:
- @VendorId INT (optional)
- @ActiveOnly BIT (default 1)

## sp_UpdateVendor

Updates vendor information.
"""


# ── DocumentChunker ──────────────────────────────────────────────────


class TestDocumentChunker:
    def test_chunk_generic_markdown(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("docs/overview.md", SAMPLE_MD)
        assert len(chunks) > 0
        assert all(isinstance(c, DocumentChunk) for c in chunks)

    def test_chunks_have_ids(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("test.md", SAMPLE_MD)
        ids = [c.id for c in chunks]
        assert len(ids) == len(set(ids))  # all unique

    def test_chunks_have_source_file(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("docs/test.md", SAMPLE_MD)
        for c in chunks:
            assert c.source_file == "docs/test.md"

    def test_chunks_have_titles(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("test.md", SAMPLE_MD)
        titles = [c.title for c in chunks]
        assert any("Vendor" in t for t in titles)

    def test_chunk_types_classified(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("test.md", SAMPLE_MD)
        types = {c.chunk_type for c in chunks}
        # Should detect at least text and either query or code
        assert ChunkType.TEXT in types or ChunkType.QUERY in types or ChunkType.TABLE in types

    def test_schema_dispatch(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("docs/EDS_SCHEMA.md", SCHEMA_MD)
        for c in chunks:
            assert c.chunk_type == ChunkType.SCHEMA

    def test_procedure_dispatch(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("docs/EDS_STORED_PROCEDURES.md", PROCEDURE_MD)
        for c in chunks:
            assert c.chunk_type == ChunkType.PROCEDURE

    def test_min_chunk_size_filter(self):
        chunker = DocumentChunker(min_chunk_size=100)
        chunks = chunker.chunk_document("test.md", "# Title\n\nShort.")
        # "Short." is under min size, may be filtered
        for c in chunks:
            assert len(c.content) >= 10  # at least has some content

    def test_large_document_split(self):
        chunker = DocumentChunker(max_chunk_size=100)
        large_content = "# Title\n\n" + "\n\n".join(
            [f"Paragraph {i} with enough text to fill up the chunk." for i in range(50)]
        )
        chunks = chunker.chunk_document("test.md", large_content)
        assert len(chunks) > 1

    def test_token_count_populated(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("test.md", SAMPLE_MD)
        for c in chunks:
            assert c.token_count > 0

    def test_empty_content(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("test.md", "")
        assert chunks == []

    def test_query_dispatch(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("docs/QUERY_examples.md", "# Queries\n\nSELECT 1")
        for c in chunks:
            assert c.chunk_type == ChunkType.QUERY

    def test_workflow_dispatch(self):
        chunker = DocumentChunker()
        chunks = chunker.chunk_document("docs/business_workflow.md", "# Steps\n\n1. Do thing\n2. Done")
        for c in chunks:
            assert c.chunk_type == ChunkType.WORKFLOW


# ── BM25Index ────────────────────────────────────────────────────────


class TestBM25Index:
    @pytest.fixture
    def indexed_bm25(self):
        chunks = [
            DocumentChunk(id="1", content="SELECT VendorName FROM Vendors WHERE VendorId = 9",
                          chunk_type=ChunkType.QUERY, source_file="a.md", title="Vendor Query"),
            DocumentChunk(id="2", content="The items table stores product catalog information",
                          chunk_type=ChunkType.TEXT, source_file="b.md", title="Items"),
            DocumentChunk(id="3", content="Purchase orders track vendor transactions and spending",
                          chunk_type=ChunkType.TEXT, source_file="c.md", title="POs"),
            DocumentChunk(id="4", content="School Specialty is the largest vendor by spend",
                          chunk_type=ChunkType.TEXT, source_file="d.md", title="Vendor Info"),
        ]
        bm25 = BM25Index()
        bm25.index(chunks)
        return bm25

    def test_search_returns_results(self, indexed_bm25):
        results = indexed_bm25.search("vendor", n_results=5)
        assert len(results) > 0

    def test_search_relevance(self, indexed_bm25):
        results = indexed_bm25.search("vendor")
        # "vendor" appears in chunks 1, 3, 4 — should score them higher
        top_ids = [r[0].id for r in results[:3]]
        assert "1" in top_ids or "3" in top_ids or "4" in top_ids

    def test_search_no_match(self, indexed_bm25):
        results = indexed_bm25.search("xylophone")
        assert len(results) == 0

    def test_search_empty_index(self):
        bm25 = BM25Index()
        bm25.index([])
        assert bm25.search("anything") == []

    def test_search_limit(self, indexed_bm25):
        results = indexed_bm25.search("vendor", n_results=2)
        assert len(results) <= 2

    def test_sql_keyword_matching(self, indexed_bm25):
        results = indexed_bm25.search("SELECT VendorName")
        assert len(results) > 0
        assert results[0][0].id == "1"  # SQL chunk should rank first


# ── HybridRetriever (mocked vector store) ────────────────────────────


class TestHybridRetriever:
    @pytest.fixture
    def mock_vector_store(self):
        store = MagicMock()
        store.query.return_value = [
            {
                "id": "v1",
                "content": "Vendors table contains supplier information",
                "metadata": {"source_file": "schema.md", "title": "Vendors", "chunk_type": "schema", "token_count": 50},
                "distance": 0.15,
            },
            {
                "id": "v2",
                "content": "Purchase orders link to vendors via VendorId",
                "metadata": {"source_file": "orders.md", "title": "POs", "chunk_type": "text", "token_count": 40},
                "distance": 0.25,
            },
        ]
        return store

    @pytest.fixture
    def mock_embedder(self):
        embedder = MagicMock()
        embedder.embed_query.return_value = [0.1] * 384
        embedder.embed_texts.return_value = [[0.1] * 384]
        embedder.dimension = 384
        return embedder

    @pytest.fixture
    def retriever(self, mock_vector_store, mock_embedder):
        r = HybridRetriever(
            vector_store=mock_vector_store,
            embedding_provider=mock_embedder,
        )
        # Build BM25 with some chunks
        chunks = [
            DocumentChunk(id="v1", content="Vendors table contains supplier information",
                          chunk_type=ChunkType.SCHEMA, source_file="schema.md", title="Vendors"),
            DocumentChunk(id="k1", content="Vendor spend analysis by budget year",
                          chunk_type=ChunkType.TEXT, source_file="analysis.md", title="Spend"),
        ]
        r.build_keyword_index(chunks)
        return r

    def test_retrieve_returns_results(self, retriever):
        results = retriever.retrieve("vendor information", n_results=3)
        assert len(results) > 0
        assert all(isinstance(r, RetrievalResult) for r in results)

    def test_retrieve_has_scores(self, retriever):
        results = retriever.retrieve("vendor", n_results=3)
        for r in results:
            assert r.score > 0
            assert r.rank > 0
            assert r.retrieval_type == "hybrid"

    def test_query_type_sql_weights(self, retriever):
        sem_w, kw_w = retriever._get_weights_for_query_type("sql")
        assert kw_w > sem_w  # SQL should be keyword-heavy

    def test_query_type_schema_weights(self, retriever):
        sem_w, kw_w = retriever._get_weights_for_query_type("schema")
        assert sem_w > kw_w  # Schema should be semantic-heavy

    def test_query_type_general_default(self, retriever):
        sem_w, kw_w = retriever._get_weights_for_query_type("general")
        assert sem_w == 0.7
        assert kw_w == 0.3

    def test_retrieve_for_query_type(self, retriever):
        results = retriever.retrieve_for_query_type("SELECT vendor", "sql", n_results=2)
        assert len(results) > 0

    def test_rrf_fusion_combines_sources(self, retriever):
        # Both semantic and keyword should contribute to results
        results = retriever.retrieve("vendor", n_results=5)
        ids = {r.chunk.id for r in results}
        # Should contain results from both semantic (v1, v2) and keyword (v1, k1)
        assert len(ids) >= 2


# ── RetrievalResult ──────────────────────────────────────────────────


class TestRetrievalResult:
    def test_defaults(self):
        chunk = DocumentChunk(
            id="t1", content="test", chunk_type=ChunkType.TEXT,
            source_file="f.md", title="Test",
        )
        r = RetrievalResult(chunk=chunk, score=0.95, rank=1, retrieval_type="semantic")
        assert r.reranked is False
        assert r.score == 0.95


# ── Indexer (mocked) ─────────────────────────────────────────────────


class TestIndexer:
    def test_index_all_with_missing_docs_dir(self):
        from agent.rag.indexer import index_all
        with patch("agent.rag.embeddings.create_embedding_provider") as mock_emb, \
             patch("agent.rag.vector_store.VectorStore"):
            mock_emb.return_value = MagicMock()
            stats = index_all({"documentation": {"docs_dir": "/nonexistent"}})
            assert "not found" in stats["errors"][0].lower()

    def test_index_specific_file(self, tmp_path):
        from agent.rag import indexer

        # Create a test file
        test_file = tmp_path / "test.md"
        test_file.write_text("# Test\n\nSome content about vendors and products that is long enough to pass the minimum chunk size filter for the chunker.")

        mock_emb = MagicMock()
        mock_emb.embed_texts.return_value = [[0.1] * 384]

        mock_store = MagicMock()
        mock_store.upsert_chunks.return_value = 1

        # Patch the imports at the module where they're used
        original_index_all = indexer.index_all

        def patched_index_all(**kwargs):
            with patch("agent.rag.embeddings.create_embedding_provider", return_value=mock_emb), \
                 patch("agent.rag.vector_store.VectorStore", return_value=mock_store):
                return original_index_all(**kwargs)

        stats = patched_index_all(config={}, specific_file=str(test_file))
        assert stats["files_processed"] == 1
        assert stats["chunks_created"] > 0
        assert len(stats["errors"]) == 0
