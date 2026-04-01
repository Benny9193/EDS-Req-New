"""Document indexer — loads, chunks, embeds, and upserts docs into the vector store.

Orchestrates the full indexing pipeline: read markdown files from /docs/,
chunk them, compute embeddings, and store in ChromaDB.
"""

import logging
from pathlib import Path
from typing import Any, Dict, List, Optional

from agent.rag.chunker import DocumentChunker

logger = logging.getLogger(__name__)


def index_all(
    config: Optional[Dict[str, Any]] = None,
    rebuild: bool = False,
    specific_file: Optional[str] = None,
) -> Dict[str, Any]:
    """Index documentation files into the vector store.

    Args:
        config: Agent configuration dict.
        rebuild: If True, drop and rebuild the entire index.
        specific_file: If set, only index this single file.

    Returns:
        Stats dict with keys: files_processed, chunks_created, chunks_indexed, errors.
    """
    from agent.rag.embeddings import create_embedding_provider
    from agent.rag.vector_store import VectorStore

    config = config or {}
    rag_config = config.get("rag", {})
    doc_config = config.get("documentation", {})

    docs_dir = doc_config.get("docs_dir", "docs")
    vs_config = rag_config.get("vector_store", {})
    vs_path = vs_config.get("path", "data/vectordb")
    collection = vs_config.get("collection", "eds_documentation")
    chunk_config = rag_config.get("chunking", {})

    stats = {
        "files_processed": 0,
        "chunks_created": 0,
        "chunks_indexed": 0,
        "errors": [],
    }

    # Initialize components
    try:
        embedding_provider = create_embedding_provider(config)
    except Exception as e:
        logger.error("Failed to create embedding provider: %s", e)
        stats["errors"].append(f"Embedding provider: {e}")
        return stats

    try:
        store = VectorStore(path=vs_path, collection_name=collection)
    except Exception as e:
        logger.error("Failed to create vector store: %s", e)
        stats["errors"].append(f"Vector store: {e}")
        return stats

    if rebuild:
        logger.info("Rebuilding index from scratch")
        store.reset()

    chunker = DocumentChunker(
        max_chunk_size=chunk_config.get("max_chunk_size", 1500),
        chunk_overlap=chunk_config.get("chunk_overlap", 200),
        min_chunk_size=chunk_config.get("min_chunk_size", 100),
    )

    # Collect files to index
    if specific_file:
        files = [Path(specific_file)]
    else:
        docs_path = Path(docs_dir)
        if not docs_path.exists():
            stats["errors"].append(f"Docs directory not found: {docs_dir}")
            return stats

        # Index specific files from config, or all .md files
        file_list = doc_config.get("files", [])
        if file_list:
            files = [docs_path / f for f in file_list]
        else:
            files = sorted(docs_path.rglob("*.md"))

    # Process each file
    for file_path in files:
        if not file_path.exists():
            logger.warning("File not found: %s", file_path)
            stats["errors"].append(f"File not found: {file_path}")
            continue

        try:
            content = file_path.read_text(encoding="utf-8")
            if not content.strip():
                continue

            # Chunk
            chunks = chunker.chunk_document(str(file_path), content)
            stats["chunks_created"] += len(chunks)

            if not chunks:
                continue

            # Embed in batches
            batch_size = 32
            for i in range(0, len(chunks), batch_size):
                batch = chunks[i : i + batch_size]
                texts = [c.content for c in batch]
                embeddings = embedding_provider.embed_texts(texts)
                store.upsert_chunks(batch, embeddings)
                stats["chunks_indexed"] += len(batch)

            stats["files_processed"] += 1
            logger.info(
                "Indexed %s: %d chunks", file_path.name, len(chunks),
            )

        except Exception as e:
            logger.error("Failed to index %s: %s", file_path, e)
            stats["errors"].append(f"{file_path}: {e}")

    logger.info(
        "Indexing complete: %d files, %d chunks indexed",
        stats["files_processed"],
        stats["chunks_indexed"],
    )
    return stats


def main():
    """CLI entry point for indexing."""
    import argparse
    import sys

    logging.basicConfig(level=logging.INFO)

    parser = argparse.ArgumentParser(description="Index EDS documentation for RAG")
    parser.add_argument("--rebuild", action="store_true", help="Drop and rebuild index")
    parser.add_argument("--file", type=str, help="Index a specific file")
    args = parser.parse_args()

    from agent.config import load_config
    config = load_config()

    stats = index_all(config, rebuild=args.rebuild, specific_file=args.file)
    print(f"Files processed: {stats['files_processed']}")
    print(f"Chunks created:  {stats['chunks_created']}")
    print(f"Chunks indexed:  {stats['chunks_indexed']}")
    if stats["errors"]:
        print(f"Errors: {len(stats['errors'])}")
        for err in stats["errors"]:
            print(f"  - {err}")
        sys.exit(1)


if __name__ == "__main__":
    main()
