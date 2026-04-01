"""ChromaDB-based vector store for document embeddings.

Provides persistent storage and cosine similarity search over
document chunks embedded by the RAG pipeline.
"""

import logging
from typing import Any, Dict, List, Optional

from agent.rag.chunker import DocumentChunk

logger = logging.getLogger(__name__)


class VectorStore:
    """Persistent vector store backed by ChromaDB."""

    def __init__(
        self,
        path: str = "data/vectordb",
        collection_name: str = "eds_documentation",
        embedding_function: Optional[Any] = None,
    ):
        import chromadb
        from chromadb.config import Settings

        self._path = path
        self._collection_name = collection_name

        self._client = chromadb.PersistentClient(
            path=path,
            settings=Settings(
                anonymized_telemetry=False,
                allow_reset=True,
            ),
        )

        # Get or create the collection with cosine distance
        kwargs: Dict[str, Any] = {
            "name": collection_name,
            "metadata": {"hnsw:space": "cosine"},
        }
        if embedding_function:
            kwargs["embedding_function"] = embedding_function

        self._collection = self._client.get_or_create_collection(**kwargs)

    @property
    def count(self) -> int:
        return self._collection.count()

    def upsert_chunks(
        self,
        chunks: List[DocumentChunk],
        embeddings: List[List[float]],
    ) -> int:
        """Upsert document chunks with their embeddings. Returns count upserted."""
        if not chunks:
            return 0

        ids = [c.id for c in chunks]
        documents = [c.content for c in chunks]
        metadatas = [
            {
                "source_file": c.source_file,
                "title": c.title,
                "chunk_type": c.chunk_type.value,
                "start_line": c.start_line,
                "end_line": c.end_line,
                "token_count": c.token_count,
            }
            for c in chunks
        ]

        self._collection.upsert(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )
        return len(chunks)

    def query(
        self,
        query_embedding: List[float],
        n_results: int = 5,
        where: Optional[Dict] = None,
    ) -> List[Dict[str, Any]]:
        """Query the vector store for similar chunks.

        Returns list of dicts with keys: id, content, metadata, distance.
        """
        kwargs: Dict[str, Any] = {
            "query_embeddings": [query_embedding],
            "n_results": n_results,
        }
        if where:
            kwargs["where"] = where

        results = self._collection.query(**kwargs)

        items = []
        if results and results["ids"]:
            for i, doc_id in enumerate(results["ids"][0]):
                items.append({
                    "id": doc_id,
                    "content": results["documents"][0][i] if results["documents"] else "",
                    "metadata": results["metadatas"][0][i] if results["metadatas"] else {},
                    "distance": results["distances"][0][i] if results["distances"] else 0.0,
                })
        return items

    def delete_by_source(self, source_file: str) -> None:
        """Delete all chunks from a specific source file."""
        self._collection.delete(
            where={"source_file": source_file},
        )

    def reset(self) -> None:
        """Delete and recreate the collection."""
        self._client.delete_collection(self._collection_name)
        self._collection = self._client.get_or_create_collection(
            name=self._collection_name,
            metadata={"hnsw:space": "cosine"},
        )

    def get_sources(self) -> List[str]:
        """Get all unique source files in the store."""
        results = self._collection.get(include=["metadatas"])
        sources = set()
        if results and results["metadatas"]:
            for meta in results["metadatas"]:
                if meta and "source_file" in meta:
                    sources.add(meta["source_file"])
        return sorted(sources)
