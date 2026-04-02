"""Embedding providers for the RAG pipeline.

Supports local sentence-transformers, OpenAI, and Ollama embedding models.
Each provider implements embed_texts() and embed_query() methods.
"""

import logging
import os
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class BaseEmbeddingProvider(ABC):
    """Abstract base class for embedding providers."""

    @abstractmethod
    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        """Embed a batch of texts. Returns list of embedding vectors."""
        ...

    @abstractmethod
    def embed_query(self, query: str) -> List[float]:
        """Embed a single query. May use a different model/prefix."""
        ...

    @property
    @abstractmethod
    def dimension(self) -> int:
        """Return the embedding dimension."""
        ...

    @property
    @abstractmethod
    def model_name(self) -> str:
        ...


class LocalEmbeddingProvider(BaseEmbeddingProvider):
    """Local embeddings via sentence-transformers."""

    DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

    def __init__(
        self,
        model: Optional[str] = None,
        device: str = "cpu",
        batch_size: int = 32,
    ):
        from sentence_transformers import SentenceTransformer

        self._model_name = model or self.DEFAULT_MODEL
        self._device = device
        self._batch_size = batch_size
        self._model = SentenceTransformer(self._model_name, device=device)
        self._dim = self._model.get_sentence_embedding_dimension()

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        embeddings = self._model.encode(
            texts, batch_size=self._batch_size, show_progress_bar=False,
        )
        return embeddings.tolist()

    def embed_query(self, query: str) -> List[float]:
        return self.embed_texts([query])[0]

    @property
    def dimension(self) -> int:
        return self._dim

    @property
    def model_name(self) -> str:
        return self._model_name


class OpenAIEmbeddingProvider(BaseEmbeddingProvider):
    """OpenAI embeddings via the openai SDK."""

    DEFAULT_MODEL = "text-embedding-3-small"

    MODEL_DIMENSIONS = {
        "text-embedding-3-small": 1536,
        "text-embedding-3-large": 3072,
        "text-embedding-ada-002": 1536,
    }

    def __init__(self, model: Optional[str] = None):
        import openai

        self._model_name = model or self.DEFAULT_MODEL
        api_key = os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY env var required for OpenAI embeddings")
        self._client = openai.OpenAI(api_key=api_key)

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        response = self._client.embeddings.create(
            model=self._model_name, input=texts,
        )
        return [item.embedding for item in response.data]

    def embed_query(self, query: str) -> List[float]:
        return self.embed_texts([query])[0]

    @property
    def dimension(self) -> int:
        return self.MODEL_DIMENSIONS.get(self._model_name, 1536)

    @property
    def model_name(self) -> str:
        return self._model_name


class OllamaEmbeddingProvider(BaseEmbeddingProvider):
    """Ollama embeddings for local models like nomic-embed-text."""

    DEFAULT_MODEL = "nomic-embed-text"

    def __init__(
        self,
        model: Optional[str] = None,
        host: Optional[str] = None,
    ):
        self._model_name = model or self.DEFAULT_MODEL
        self._host = host or os.environ.get("OLLAMA_HOST", "http://localhost:11434")
        self._dim: Optional[int] = None

        try:
            import ollama
            self._client = ollama.Client(host=self._host)
            self._use_sdk = True
        except ImportError:
            self._client = None
            self._use_sdk = False

    def embed_texts(self, texts: List[str]) -> List[List[float]]:
        results = []
        for text in texts:
            emb = self._embed_single(text)
            results.append(emb)
        return results

    def embed_query(self, query: str) -> List[float]:
        return self._embed_single(query)

    def _embed_single(self, text: str) -> List[float]:
        if self._use_sdk and self._client:
            response = self._client.embeddings(
                model=self._model_name, prompt=text,
            )
            embedding = response.get("embedding", [])
        else:
            import httpx
            resp = httpx.post(
                f"{self._host}/api/embeddings",
                json={"model": self._model_name, "prompt": text},
                timeout=30.0,
            )
            resp.raise_for_status()
            embedding = resp.json().get("embedding", [])

        if self._dim is None and embedding:
            self._dim = len(embedding)
        return embedding

    @property
    def dimension(self) -> int:
        return self._dim or 768  # nomic-embed-text default

    @property
    def model_name(self) -> str:
        return self._model_name


def create_embedding_provider(config: Optional[Dict[str, Any]] = None) -> BaseEmbeddingProvider:
    """Factory to create an embedding provider from config."""
    config = config or {}
    rag_config = config.get("rag", {}).get("embeddings", {})
    provider = rag_config.get("provider", "local")

    if provider == "local":
        return LocalEmbeddingProvider(
            model=rag_config.get("model"),
            device=rag_config.get("device", "cpu"),
            batch_size=rag_config.get("batch_size", 32),
        )
    elif provider == "openai":
        return OpenAIEmbeddingProvider(model=rag_config.get("model"))
    elif provider == "ollama":
        return OllamaEmbeddingProvider(
            model=rag_config.get("model"),
            host=rag_config.get("host"),
        )
    else:
        raise ValueError(f"Unknown embedding provider: {provider}")
