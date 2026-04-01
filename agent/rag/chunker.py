"""Markdown-aware document chunker for the RAG pipeline.

Splits documents into semantically meaningful chunks based on headings,
code blocks, tables, and content type. Uses filename-based dispatch to
select specialized chunking strategies.
"""

import hashlib
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class ChunkType(str, Enum):
    TEXT = "text"
    CODE = "code"
    TABLE = "table"
    HEADING = "heading"
    PROCEDURE = "procedure"
    QUERY = "query"
    SCHEMA = "schema"
    CONFIGURATION = "configuration"
    OVERVIEW = "overview"
    WORKFLOW = "workflow"
    DEFINITION = "definition"
    EXAMPLE = "example"


@dataclass
class DocumentChunk:
    id: str
    content: str
    chunk_type: ChunkType
    source_file: str
    title: str
    metadata: Dict[str, Any] = field(default_factory=dict)
    start_line: int = 0
    end_line: int = 0
    token_count: int = 0


# Patterns for content detection
_HEADING_RE = re.compile(r'^(#{1,6})\s+(.+)$', re.MULTILINE)
_CODE_BLOCK_RE = re.compile(r'```[\w]*\n(.*?)```', re.DOTALL)
_TABLE_RE = re.compile(r'^\|.+\|$', re.MULTILINE)
_SQL_KEYWORDS_RE = re.compile(
    r'\b(SELECT|INSERT|UPDATE|DELETE|CREATE|ALTER|DROP|EXEC|FROM|WHERE|JOIN)\b',
    re.IGNORECASE,
)


def _estimate_tokens(text: str) -> int:
    """Rough token estimate: ~4 chars per token."""
    return len(text) // 4


def _make_chunk_id(source_file: str, content: str, index: int) -> str:
    """Generate a deterministic chunk ID."""
    raw = f"{source_file}:{index}:{content[:100]}"
    return hashlib.md5(raw.encode()).hexdigest()[:12]


class DocumentChunker:
    """Chunks markdown documents for embedding and retrieval."""

    def __init__(
        self,
        max_chunk_size: int = 1500,
        chunk_overlap: int = 200,
        min_chunk_size: int = 100,
    ):
        self.max_chunk_size = max_chunk_size
        self.chunk_overlap = chunk_overlap
        self.min_chunk_size = min_chunk_size

    def chunk_document(
        self, file_path: str, content: str,
    ) -> List[DocumentChunk]:
        """Chunk a document using filename-based strategy dispatch."""
        name_lower = file_path.lower()

        if any(p in name_lower for p in ("schema", "data_dict")):
            return self._chunk_schema(file_path, content)
        elif any(p in name_lower for p in ("procedure", "stored_proc")):
            return self._chunk_procedures(file_path, content)
        elif any(p in name_lower for p in ("query", "sql")):
            return self._chunk_queries(file_path, content)
        elif any(p in name_lower for p in ("workflow", "process")):
            return self._chunk_workflows(file_path, content)
        else:
            return self._chunk_by_headings(file_path, content)

    def _chunk_by_headings(
        self, file_path: str, content: str,
    ) -> List[DocumentChunk]:
        """Generic heading-based chunking for markdown documents."""
        chunks = []
        sections = self._split_by_headings(content)

        for i, (title, section_content, start_line) in enumerate(sections):
            chunk_type = self._classify_content(section_content)
            sub_chunks = self._split_if_too_large(section_content)

            for j, sub in enumerate(sub_chunks):
                tokens = _estimate_tokens(sub)
                if tokens < self.min_chunk_size // 4:
                    continue

                chunk_id = _make_chunk_id(file_path, sub, i * 100 + j)
                chunks.append(DocumentChunk(
                    id=chunk_id,
                    content=sub.strip(),
                    chunk_type=chunk_type,
                    source_file=file_path,
                    title=title,
                    start_line=start_line,
                    token_count=tokens,
                    metadata={"section_index": i, "sub_index": j},
                ))

        return chunks

    def _chunk_schema(
        self, file_path: str, content: str,
    ) -> List[DocumentChunk]:
        """Schema-aware chunking: keep table definitions together."""
        return self._chunk_by_headings_with_type(
            file_path, content, ChunkType.SCHEMA,
        )

    def _chunk_procedures(
        self, file_path: str, content: str,
    ) -> List[DocumentChunk]:
        """Procedure-oriented chunking: keep procedure docs together."""
        return self._chunk_by_headings_with_type(
            file_path, content, ChunkType.PROCEDURE,
        )

    def _chunk_queries(
        self, file_path: str, content: str,
    ) -> List[DocumentChunk]:
        """Query block chunking for SQL-heavy documents."""
        return self._chunk_by_headings_with_type(
            file_path, content, ChunkType.QUERY,
        )

    def _chunk_workflows(
        self, file_path: str, content: str,
    ) -> List[DocumentChunk]:
        """Workflow/step chunking."""
        return self._chunk_by_headings_with_type(
            file_path, content, ChunkType.WORKFLOW,
        )

    def _chunk_by_headings_with_type(
        self, file_path: str, content: str, default_type: ChunkType,
    ) -> List[DocumentChunk]:
        """Chunk by headings with a default chunk type override."""
        chunks = self._chunk_by_headings(file_path, content)
        for chunk in chunks:
            chunk.chunk_type = default_type
        return chunks

    def _split_by_headings(
        self, content: str,
    ) -> List[tuple]:
        """Split content into (title, content, start_line) tuples by headings."""
        lines = content.split("\n")
        sections = []
        current_title = "Introduction"
        current_lines = []
        current_start = 0

        for i, line in enumerate(lines):
            heading_match = _HEADING_RE.match(line)
            if heading_match and current_lines:
                section_text = "\n".join(current_lines)
                if section_text.strip():
                    sections.append((current_title, section_text, current_start))
                current_title = heading_match.group(2).strip()
                current_lines = [line]
                current_start = i
            else:
                current_lines.append(line)

        # Last section
        if current_lines:
            section_text = "\n".join(current_lines)
            if section_text.strip():
                sections.append((current_title, section_text, current_start))

        return sections

    def _split_if_too_large(self, content: str) -> List[str]:
        """Split content that exceeds max_chunk_size into overlapping pieces."""
        tokens = _estimate_tokens(content)
        if tokens <= self.max_chunk_size:
            return [content]

        # Split on paragraph boundaries
        paragraphs = content.split("\n\n")
        chunks = []
        current = []
        current_tokens = 0

        for para in paragraphs:
            para_tokens = _estimate_tokens(para)

            if current_tokens + para_tokens > self.max_chunk_size and current:
                chunks.append("\n\n".join(current))
                # Keep overlap
                overlap_text = "\n\n".join(current)
                overlap_tokens = _estimate_tokens(overlap_text)
                while current and overlap_tokens > self.chunk_overlap:
                    current.pop(0)
                    overlap_text = "\n\n".join(current)
                    overlap_tokens = _estimate_tokens(overlap_text)
                current_tokens = overlap_tokens

            current.append(para)
            current_tokens += para_tokens

        if current:
            chunks.append("\n\n".join(current))

        return chunks

    def _classify_content(self, content: str) -> ChunkType:
        """Classify a chunk's content type based on its contents."""
        if _CODE_BLOCK_RE.search(content):
            if _SQL_KEYWORDS_RE.search(content):
                return ChunkType.QUERY
            return ChunkType.CODE

        table_lines = _TABLE_RE.findall(content)
        if len(table_lines) > 2:
            return ChunkType.TABLE

        if _SQL_KEYWORDS_RE.search(content):
            return ChunkType.QUERY

        return ChunkType.TEXT
