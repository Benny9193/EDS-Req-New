"""Hybrid retriever combining semantic search with BM25 keyword search.

Uses Reciprocal Rank Fusion (RRF) to merge results from vector similarity
and keyword matching, with optional cross-encoder reranking.
"""

import logging
import math
import re
from collections import defaultdict
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional

from agent.rag.chunker import ChunkType, DocumentChunk

logger = logging.getLogger(__name__)


@dataclass
class RetrievalResult:
    chunk: DocumentChunk
    score: float
    rank: int
    retrieval_type: str  # "semantic", "keyword", or "hybrid"
    reranked: bool = False


class BM25Index:
    """BM25Okapi keyword search index."""

    def __init__(self, k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self._documents: List[List[str]] = []
        self._chunks: List[DocumentChunk] = []
        self._doc_lengths: List[int] = []
        self._avg_dl: float = 0.0
        self._df: Dict[str, int] = defaultdict(int)  # document frequency
        self._n_docs: int = 0

    def index(self, chunks: List[DocumentChunk]) -> None:
        """Build the BM25 index from document chunks."""
        self._chunks = chunks
        self._documents = []
        self._doc_lengths = []
        self._df = defaultdict(int)

        for chunk in chunks:
            tokens = self._tokenize(chunk.content)
            self._documents.append(tokens)
            self._doc_lengths.append(len(tokens))
            seen = set()
            for token in tokens:
                if token not in seen:
                    self._df[token] += 1
                    seen.add(token)

        self._n_docs = len(chunks)
        self._avg_dl = (
            sum(self._doc_lengths) / self._n_docs if self._n_docs > 0 else 0
        )

    def search(self, query: str, n_results: int = 10) -> List[tuple]:
        """Search the index. Returns list of (chunk, score) tuples."""
        if not self._documents:
            return []

        query_tokens = self._tokenize(query)
        scores = []

        for i, doc_tokens in enumerate(self._documents):
            score = self._score_document(query_tokens, doc_tokens, i)
            if score > 0:
                scores.append((self._chunks[i], score))

        scores.sort(key=lambda x: x[1], reverse=True)
        return scores[:n_results]

    def _score_document(
        self, query_tokens: List[str], doc_tokens: List[str], doc_idx: int,
    ) -> float:
        """Compute BM25 score for a single document."""
        score = 0.0
        dl = self._doc_lengths[doc_idx]
        tf_map: Dict[str, int] = defaultdict(int)
        for token in doc_tokens:
            tf_map[token] += 1

        for qt in query_tokens:
            if qt not in tf_map:
                continue

            tf = tf_map[qt]
            df = self._df.get(qt, 0)
            idf = math.log(
                (self._n_docs - df + 0.5) / (df + 0.5) + 1.0
            )
            numerator = tf * (self.k1 + 1)
            denominator = tf + self.k1 * (
                1 - self.b + self.b * dl / self._avg_dl
            )
            score += idf * numerator / denominator

        return score

    @staticmethod
    def _tokenize(text: str) -> List[str]:
        """Simple whitespace + punctuation tokenizer."""
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        return text.split()


class HybridRetriever:
    """Combines semantic vector search with BM25 keyword search via RRF."""

    def __init__(
        self,
        vector_store,
        embedding_provider,
        semantic_weight: float = 0.7,
        keyword_weight: float = 0.3,
        rrf_k: int = 60,
        use_reranking: bool = False,
        reranker_model: str = "cross-encoder/ms-marco-MiniLM-L-6-v2",
    ):
        self._vector_store = vector_store
        self._embedding_provider = embedding_provider
        self._semantic_weight = semantic_weight
        self._keyword_weight = keyword_weight
        self._rrf_k = rrf_k
        self._use_reranking = use_reranking
        self._reranker_model = reranker_model
        self._bm25 = BM25Index()
        self._reranker = None

    def build_keyword_index(self, chunks: List[DocumentChunk]) -> None:
        """Build the BM25 keyword index from chunks."""
        self._bm25.index(chunks)
        logger.info("Built BM25 index with %d chunks", len(chunks))

    def retrieve(
        self,
        query: str,
        n_results: int = 5,
        query_type: str = "general",
    ) -> List[RetrievalResult]:
        """Retrieve relevant chunks using hybrid search.

        Args:
            query: Search query string.
            n_results: Number of results to return.
            query_type: One of "sql", "schema", "procedure", "general".
                Controls the balance between semantic and keyword search.
        """
        # Adjust weights based on query type
        sem_w, kw_w = self._get_weights_for_query_type(query_type)

        # Fetch more candidates than needed for fusion
        fetch_n = n_results * 3

        # Semantic search
        query_embedding = self._embedding_provider.embed_query(query)
        semantic_results = self._vector_store.query(
            query_embedding, n_results=fetch_n,
        )

        # Keyword search
        keyword_results = self._bm25.search(query, n_results=fetch_n)

        # Reciprocal Rank Fusion
        fused = self._rrf_fuse(
            semantic_results, keyword_results,
            sem_w, kw_w,
        )

        # Take top n
        results = fused[:n_results]

        # Optional reranking
        if self._use_reranking and results:
            results = self._rerank(query, results)

        return results

    def retrieve_for_query_type(
        self,
        query: str,
        query_type: str,
        n_results: int = 5,
    ) -> List[RetrievalResult]:
        """Convenience method that routes based on query type."""
        return self.retrieve(query, n_results=n_results, query_type=query_type)

    def _get_weights_for_query_type(self, query_type: str) -> tuple:
        """Return (semantic_weight, keyword_weight) for a query type."""
        if query_type == "sql":
            return 0.3, 0.7  # SQL benefits from exact term matching
        elif query_type == "schema":
            return 0.8, 0.2  # Schema concepts are semantic
        elif query_type == "procedure":
            return 0.5, 0.5  # Procedure names + descriptions
        else:
            return self._semantic_weight, self._keyword_weight

    def _rrf_fuse(
        self,
        semantic_results: List[Dict],
        keyword_results: List[tuple],
        semantic_weight: float,
        keyword_weight: float,
    ) -> List[RetrievalResult]:
        """Fuse results using Reciprocal Rank Fusion."""
        scores: Dict[str, float] = defaultdict(float)
        chunk_map: Dict[str, DocumentChunk] = {}

        # Score semantic results
        for rank, result in enumerate(semantic_results):
            doc_id = result["id"]
            scores[doc_id] += semantic_weight / (self._rrf_k + rank + 1)
            if doc_id not in chunk_map:
                chunk_map[doc_id] = DocumentChunk(
                    id=doc_id,
                    content=result["content"],
                    chunk_type=ChunkType(result["metadata"].get("chunk_type", "text")),
                    source_file=result["metadata"].get("source_file", ""),
                    title=result["metadata"].get("title", ""),
                    token_count=result["metadata"].get("token_count", 0),
                )

        # Score keyword results
        for rank, (chunk, _bm25_score) in enumerate(keyword_results):
            scores[chunk.id] += keyword_weight / (self._rrf_k + rank + 1)
            if chunk.id not in chunk_map:
                chunk_map[chunk.id] = chunk

        # Sort by fused score
        sorted_ids = sorted(scores.keys(), key=lambda x: scores[x], reverse=True)

        results = []
        for i, doc_id in enumerate(sorted_ids):
            chunk = chunk_map[doc_id]
            results.append(RetrievalResult(
                chunk=chunk,
                score=scores[doc_id],
                rank=i + 1,
                retrieval_type="hybrid",
            ))

        return results

    def _rerank(
        self, query: str, results: List[RetrievalResult],
    ) -> List[RetrievalResult]:
        """Rerank results using a cross-encoder model."""
        try:
            if self._reranker is None:
                from sentence_transformers import CrossEncoder
                self._reranker = CrossEncoder(self._reranker_model)

            pairs = [(query, r.chunk.content) for r in results]
            rerank_scores = self._reranker.predict(pairs)

            for result, score in zip(results, rerank_scores):
                result.score = float(score)
                result.reranked = True

            results.sort(key=lambda r: r.score, reverse=True)
            for i, r in enumerate(results):
                r.rank = i + 1

        except ImportError:
            logger.warning("Cross-encoder not available, skipping reranking")
        except Exception as e:
            logger.warning("Reranking failed: %s", e)

        return results
