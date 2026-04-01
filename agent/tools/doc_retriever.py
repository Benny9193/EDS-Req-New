"""Documentation retriever tool — searches EDS docs via the RAG pipeline.

Uses the HybridRetriever to find relevant documentation chunks based
on a natural language query.
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


class DocRetrieverTool(BaseTool):
    """Search EDS documentation using RAG-powered hybrid retrieval."""

    name = "doc_retriever"
    category = ToolCategory.DOCUMENTATION

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self._config = config or {}
        self._retriever = None

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name=self.name,
            description=(
                "Search the EDS documentation for relevant information. "
                "Uses semantic and keyword search to find matching sections "
                "from schema docs, stored procedures, views, and guides."
            ),
            parameters=[
                ToolParameter(
                    name="query",
                    type="string",
                    description="Natural language search query.",
                ),
                ToolParameter(
                    name="query_type",
                    type="string",
                    description="Type of query for optimized search.",
                    required=False,
                    default="general",
                    enum=["general", "sql", "schema", "procedure"],
                ),
                ToolParameter(
                    name="n_results",
                    type="integer",
                    description="Number of results to return.",
                    required=False,
                    default=5,
                ),
            ],
            category=self.category,
            returns="List of relevant documentation excerpts with sources.",
        )

    def _get_retriever(self):
        """Lazy-load the retriever."""
        if self._retriever is None:
            try:
                from agent.rag.embeddings import create_embedding_provider
                from agent.rag.vector_store import VectorStore

                rag_config = self._config.get("rag", {})
                vs_config = rag_config.get("vector_store", {})

                embedding_provider = create_embedding_provider(self._config)
                vector_store = VectorStore(
                    path=vs_config.get("path", "data/vectordb"),
                    collection_name=vs_config.get("collection", "eds_documentation"),
                )

                from agent.rag.retriever import HybridRetriever
                retrieval_config = rag_config.get("retrieval", {})
                self._retriever = HybridRetriever(
                    vector_store=vector_store,
                    embedding_provider=embedding_provider,
                    semantic_weight=retrieval_config.get("semantic_weight", 0.7),
                    keyword_weight=retrieval_config.get("keyword_weight", 0.3),
                )
            except Exception as e:
                logger.error("Failed to initialize retriever: %s", e)
                raise

        return self._retriever

    def execute(self, **kwargs) -> ToolResult:
        query: str = kwargs.get("query", "")
        query_type: str = kwargs.get("query_type", "general")
        n_results: int = kwargs.get("n_results", 5)

        if not query.strip():
            return ToolResult(success=False, error="Empty query")

        try:
            retriever = self._get_retriever()
            results = retriever.retrieve(
                query, n_results=n_results, query_type=query_type,
            )

            data = []
            sources = set()
            for r in results:
                data.append({
                    "content": r.chunk.content,
                    "source": r.chunk.source_file,
                    "title": r.chunk.title,
                    "score": round(r.score, 4),
                    "chunk_type": r.chunk.chunk_type.value,
                })
                sources.add(r.chunk.source_file)

            return ToolResult(
                success=True,
                data=data,
                metadata={
                    "result_count": len(data),
                    "sources": sorted(sources),
                    "query_type": query_type,
                },
            )

        except Exception as e:
            logger.error("Doc retrieval failed: %s", e)
            return ToolResult(
                success=False,
                error=f"Retrieval error: {e}",
            )


def create_doc_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    """Factory function to create documentation retrieval tools."""
    return [DocRetrieverTool(config=config)]
