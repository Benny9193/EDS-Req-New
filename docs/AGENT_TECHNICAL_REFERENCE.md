# EDS DBA Agent: Technical Reference

**Version**: 2.0 (source-verified rewrite)
**Last Updated**: March 2026
**Audience**: Backend engineers, database administrators, system architects

> All class names, method signatures, enum values, default values, config keys, and regex patterns in this document were extracted directly from the source code. Where the runtime configuration in `agent_config.yaml` differs from the code-level defaults, both values are documented explicitly.

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Architecture Overview](#2-architecture-overview)
3. [Core Agent](#3-core-agent)
4. [RAG Pipeline](#4-rag-pipeline)
5. [Memory System](#5-memory-system)
6. [Tool Registry](#6-tool-registry)
7. [LLM Providers](#7-llm-providers)
8. [Security](#8-security)
9. [Audit System](#9-audit-system)
10. [Export System](#10-export-system)
11. [GUI Application](#11-gui-application)
12. [CLI Interface](#12-cli-interface)
13. [Configuration Reference](#13-configuration-reference)
14. [End-to-End Data Flow](#14-end-to-end-data-flow)
15. [Appendix](#15-appendix)

---

## 1. Executive Summary

The EDS DBA Agent is an AI-powered database assistant for natural language interaction with the EDS SQL Server database. It is one of three major components in the EDS platform — alongside the Universal Requisition System (FastAPI + Alpine.js) and SQL Server Monitoring Tools — and operates as an autonomous agent capable of executing SQL queries, generating ad-hoc reports, searching technical documentation, and running diagnostic scripts.

The agent is built around a Retrieval-Augmented Generation (RAG) architecture with the following layers:

- **Hybrid retrieval** combining semantic vector search (ChromaDB + sentence-transformers) with keyword search (BM25) and optional cross-encoder reranking, fused via Reciprocal Rank Fusion
- **Persistent memory** via JSON session files and a SQLite-backed learned context database that accumulates user preferences and query patterns
- **Multi-provider LLM abstraction** supporting Claude, OpenAI, and local Ollama models behind a uniform `BaseLLMProvider` interface
- **Tool-calling orchestration** where the LLM drives 11 registered tools for SQL execution, query generation, schema introspection, documentation search, catalog queries, and Excel report generation
- **SQL security validation** with regex-based blocking of 12 dangerous operation patterns before any query reaches the database
- **Thread-safe JSONL audit logging** with daily rotation and configurable retention

The system is accessible through a NiceGUI desktop application (1400×900 native window), a Click-based CLI, or programmatically via the `EDSAgent` Python class.

---

## 2. Architecture Overview

### 2.1 Subsystem Map

```
agent/
├── core/           # EDSAgent orchestrator
├── cli/            # Click-based CLI (app.py) + interactive REPL (repl.py)
├── gui/            # NiceGUI desktop application
├── llm/            # LLM provider abstraction + registry
├── tools/          # 7 tool modules + BaseTool + ToolRegistry
├── rag/            # Chunker, embeddings, vector store, retriever, indexer
├── memory/         # Session management, learned context, context window manager
├── security/       # SQL QueryValidator
├── audit/          # JSONL AuditLogger
├── export/         # ReportPlan schema, Excel formatter, ReportBuilder
└── main.py         # Entry point
```

### 2.2 Key Dependencies

| Layer | Library | Purpose |
|-------|---------|---------|
| LLM | `anthropic`, `openai`, `ollama` | Provider clients |
| Vector DB | `chromadb` | Persistent vector store |
| Embeddings | `sentence-transformers` | Local embedding model |
| BM25 | `rank_bm25` | Keyword retrieval |
| Reranking | `sentence-transformers` (cross-encoder) | Optional result reranking |
| GUI | `nicegui` | Desktop application |
| CLI | `click`, `rich` | Terminal interface |
| Excel | `openpyxl` | Report generation |
| Database | `pyodbc` | SQL Server connectivity |
| Config | `pyyaml` | Configuration parsing |
| Audit | stdlib `logging` + custom JSONL | Audit trail |

### 2.3 Initialization Sequence

All agent subsystems use **lazy initialization** — they are not created until first access. The `EDSAgent` constructor only stores configuration and initializes a logger. Each subsystem property (`_llm`, `_rag`, `_memory`, `_tool_registry`, `_security`, `_audit`) is created on first use via a Python `@property` that caches the result on the instance.

This pattern means import-time startup cost is negligible. A `chat()` call that only needs the LLM provider never instantiates the RAG pipeline.

---

## 3. Core Agent

**Source**: `agent/core/agent.py`

### 3.1 Enums

```python
class AgentMode(str, Enum):
    CHAT    = "chat"
    SQL     = "sql"
    DOCS    = "docs"
    ANALYZE = "analyze"
```

### 3.2 AgentResponse Dataclass

```python
@dataclass
class AgentResponse:
    content:      str
    tool_calls:   List[Dict]    = field(default_factory=list)
    sql_generated: Optional[str] = None
    sources:      List[str]     = field(default_factory=list)
    error:        Optional[str] = None
    metadata:     Dict          = field(default_factory=dict)
```

### 3.3 EDSAgent Constructor

```python
class EDSAgent:
    def __init__(self, config: Dict[str, Any] = None):
```

The constructor stores the config dict and initializes `self.logger`. All subsystem attributes (`_llm_provider`, `_rag_pipeline`, `_session_manager`, `_learned_context`, `_context_manager`, `_tool_registry`, `_security_validator`, `_audit_logger`) start as `None` and are populated lazily via properties.

### 3.4 RAG Trigger Keywords

The `_should_use_rag()` method returns `True` when the query contains any of these keywords (checked case-insensitively):

```python
RAG_KEYWORDS = [
    "how", "what is", "explain", "describe", "documentation",
    "guide", "help", "procedure", "process", "workflow",
    "table", "column", "schema", "view", "stored procedure",
    "sp_", "usp_", "trigger", "index",
]
```

### 3.5 Tool Response JSON Extraction

The `_TOOL_JSON_RE` compiled regex is used to extract JSON blocks from LLM responses that may contain tool call markup:

```python
_TOOL_JSON_RE = re.compile(
    r'```(?:json)?\s*(\{.*?\})\s*```',
    re.DOTALL
)
```

### 3.6 Streaming: Two-Phase Protocol

The `chat_stream()` method implements a two-phase streaming approach:

**Phase 1**: Call `llm.complete()` (non-streaming) to obtain tool use decisions. The complete response — including any tool call results — is processed synchronously.

**Phase 2**: The final answer text is streamed back in fixed chunks:

```python
chunk_size = 12
for i in range(0, len(final_text), chunk_size):
    yield final_text[i : i + chunk_size]
```

**Status markers** emitted as yield strings during processing:

| Marker | Meaning |
|--------|---------|
| `"[TOOL_CALL]"` | A tool is about to be executed |
| `"[TOOL_RESULT]"` | Tool execution completed |
| `"[ERROR]"` | An error occurred |
| `"[DONE]"` | Stream is complete |

### 3.7 Public Methods Summary

| Method | Signature | Description |
|--------|-----------|-------------|
| `chat` | `(message: str, session_id: str = None, mode: AgentMode = AgentMode.CHAT) -> AgentResponse` | Single-turn interaction |
| `chat_stream` | `(message: str, session_id: str = None) -> Generator[str, None, None]` | Streaming variant |
| `generate_sql` | `(description: str, context: str = None) -> str` | Natural language to SQL |
| `search_docs` | `(query: str, n_results: int = 5) -> List[Dict]` | Documentation search |
| `get_status` | `() -> Dict[str, Any]` | System health summary |

---

## 4. RAG Pipeline

### 4.1 Chunker

**Source**: `agent/rag/chunker.py`

#### ChunkType Enum

```python
class ChunkType(str, Enum):
    TEXT          = "text"
    CODE          = "code"
    TABLE         = "table"
    HEADING       = "heading"
    PROCEDURE     = "procedure"
    QUERY         = "query"
    SCHEMA        = "schema"
    CONFIGURATION = "configuration"
    OVERVIEW      = "overview"
    WORKFLOW      = "workflow"
    DEFINITION    = "definition"
    EXAMPLE       = "example"
```

#### DocumentChunk Dataclass

```python
@dataclass
class DocumentChunk:
    id:          str
    content:     str
    chunk_type:  ChunkType
    source_file: str
    title:       str
    metadata:    Dict[str, Any] = field(default_factory=dict)
    start_line:  int            = 0
    end_line:    int            = 0
    token_count: int            = 0
```

#### DocumentChunker

The `DocumentChunker` class uses a **filename-based dispatch strategy**: the `chunk_document(file_path, content)` method inspects the filename to select a specialized chunking strategy:

| Filename pattern | Strategy |
|------------------|----------|
| `*schema*`, `*data_dict*` | Schema-aware chunking |
| `*procedure*`, `*stored_proc*` | Procedure-oriented chunking |
| `*query*`, `*sql*` | Query block chunking |
| `*workflow*`, `*process*` | Workflow/step chunking |
| All others | Generic Markdown heading-based chunking |

Compiled regex patterns are used for code block extraction, table detection, SQL keyword identification, and heading level parsing.

### 4.2 Embeddings

**Source**: `agent/rag/embeddings.py`

Three embedding providers are implemented:

#### LocalEmbeddingProvider
```python
class LocalEmbeddingProvider:
    DEFAULT_MODEL = "sentence-transformers/all-MiniLM-L6-v2"
    # Output dimension: 384
```

#### OpenAIEmbeddingProvider
```python
class OpenAIEmbeddingProvider:
    DEFAULT_MODEL = "text-embedding-3-small"

    MODEL_DIMENSIONS = {
        "text-embedding-3-small": 1536,
        "text-embedding-3-large": 3072,
        "text-embedding-ada-002": 1536,
    }
```

#### OllamaEmbeddingProvider
```python
class OllamaEmbeddingProvider:
    DEFAULT_MODEL = "nomic-embed-text"
```

### 4.3 Vector Store

**Source**: `agent/rag/vector_store.py`

```python
class VectorStore:
    def __init__(
        self,
        path:            str  = "data/vectordb",
        collection_name: str  = "eds_documentation",
        embedding_dim:   int  = 384,
        provider:        str  = "local",
        model:           str  = None,
    ):
```

ChromaDB is initialized with:
```python
Settings(anonymized_telemetry=False, allow_reset=True)
```

The collection uses **cosine** distance space. The factory function `create_vector_store(config)` reads `rag.vector_store_path`, `rag.embedding_provider`, and `rag.embedding_model` from the config dict to construct the store.

### 4.4 Retriever

**Source**: `agent/rag/retriever.py`

#### RetrievalResult Dataclass

```python
@dataclass
class RetrievalResult:
    chunk:       DocumentChunk
    score:       float
    rank:        int
    retrieval_type: str    # "semantic", "keyword", or "hybrid"
    reranked:    bool = False
```

#### BM25Index

```python
class BM25Index:
    def __init__(self, k1: float = 1.5, b: float = 0.75):
```

BM25Okapi parameters: `k1=1.5` (term frequency saturation), `b=0.75` (document length normalization).

#### HybridRetriever

```python
class HybridRetriever:
    def __init__(
        self,
        vector_store:     VectorStore,
        semantic_weight:  float = 0.7,
        keyword_weight:   float = 0.3,
        rrf_k:            int   = 60,
        use_reranking:    bool  = False,
        reranker_model:   str   = "cross-encoder/ms-marco-MiniLM-L-6-v2",
    ):
```

Fusion uses **Reciprocal Rank Fusion** with `rrf_k=60`. The formula applied to each document:

```
RRF_score(d) = semantic_weight / (rrf_k + semantic_rank(d))
             + keyword_weight  / (rrf_k + keyword_rank(d))
```

#### Query Type Routing

`retrieve_for_query_type(query, query_type, n_results)` maps query types to retrieval strategy:

| `query_type` value | Strategy |
|-------------------|----------|
| `"sql"` | Keyword-heavy (SQL syntax benefits from exact term matching) |
| `"schema"` | Semantic (schema concepts expressed in natural language) |
| `"procedure"` | Hybrid (procedure names + conceptual descriptions) |
| `"general"` | Hybrid (default) |

### 4.5 Indexer

**Source**: `agent/rag/indexer.py`

The top-level `index_all(config, rebuild=False, specific_file=None)` function orchestrates document loading, chunking, embedding, and upsert into ChromaDB. It returns a stats dict with keys: `files_processed`, `chunks_created`, `chunks_indexed`, `errors`.

CLI usage:
```bash
python -m agent.rag.indexer --rebuild        # Drop and rebuild entire index
python -m agent.rag.indexer --file path.md   # Index a single file
```

---

## 5. Memory System

### 5.1 Session Management

**Source**: `agent/memory/session.py`

#### Message Dataclass

```python
@dataclass
class Message:
    role:       str
    content:    str
    timestamp:  datetime     = field(default_factory=datetime.now)
    tool_calls: List[Dict]   = field(default_factory=list)
    tool_results: List[Dict] = field(default_factory=list)
    tokens:     int          = 0
    metadata:   Dict         = field(default_factory=dict)
```

#### Session Dataclass

```python
@dataclass
class Session:
    id:           str
    created_at:   datetime = field(default_factory=datetime.now)
    updated_at:   datetime = field(default_factory=datetime.now)
    messages:     List[Message] = field(default_factory=list)
    metadata:     Dict          = field(default_factory=dict)
    mode:         str           = "chat"
    provider:     str           = "claude"
    model:        Optional[str] = None
    total_tokens: int           = 0
    summary:      Optional[str] = None
```

#### SessionManager

```python
class SessionManager:
    def __init__(
        self,
        sessions_dir: str  = "data/sessions",
        max_sessions: int  = 100,
        auto_save:    bool = True,
    ):
```

Session IDs are 8-character UUID4 hex strings (`uuid4().hex[:8]`). Sessions are persisted as individual JSON files in `sessions_dir`. When `max_sessions` is reached, the oldest sessions by `updated_at` are evicted.

Key methods:

| Method | Signature |
|--------|-----------|
| `create_session` | `(mode="chat", provider="claude", model=None) -> Session` |
| `get_session` | `(session_id: str) -> Optional[Session]` |
| `add_message` | `(session_id: str, role: str, content: str, **kwargs) -> Message` |
| `save_session` | `(session: Session) -> None` |
| `list_sessions` | `(limit: int = 20) -> List[Session]` |
| `delete_session` | `(session_id: str) -> bool` |
| `get_recent_context` | `(session_id: str, n_messages: int = 10) -> List[Message]` |

### 5.2 Learned Context

**Source**: `agent/memory/learned_context.py`

```python
class LearnedContextDB:
    def __init__(self, db_path: str = "data/memory/knowledge.sqlite"):
```

#### SQLite Schema

```sql
CREATE TABLE IF NOT EXISTS user_preferences (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    key         TEXT NOT NULL UNIQUE,
    value       TEXT NOT NULL,
    confidence  REAL DEFAULT 1.0,
    source      TEXT DEFAULT 'explicit',
    created_at  TEXT DEFAULT (datetime('now')),
    updated_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS query_patterns (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    pattern     TEXT NOT NULL,
    query_type  TEXT,
    frequency   INTEGER DEFAULT 1,
    last_used   TEXT DEFAULT (datetime('now')),
    example     TEXT,
    metadata    TEXT DEFAULT '{}'
);

CREATE TABLE IF NOT EXISTS entity_aliases (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    alias       TEXT NOT NULL,
    canonical   TEXT NOT NULL,
    entity_type TEXT,
    confidence  REAL DEFAULT 1.0,
    created_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS domain_knowledge (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    topic       TEXT NOT NULL,
    knowledge   TEXT NOT NULL,
    source      TEXT,
    confidence  REAL DEFAULT 1.0,
    created_at  TEXT DEFAULT (datetime('now')),
    updated_at  TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS conversation_summaries (
    id           INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id   TEXT NOT NULL,
    summary      TEXT NOT NULL,
    message_count INTEGER DEFAULT 0,
    created_at   TEXT DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS idx_preferences_key      ON user_preferences(key);
CREATE INDEX IF NOT EXISTS idx_patterns_type        ON query_patterns(query_type);
CREATE INDEX IF NOT EXISTS idx_aliases_alias        ON entity_aliases(alias);
CREATE INDEX IF NOT EXISTS idx_knowledge_topic      ON domain_knowledge(topic);
```

Key methods:

| Method | Signature |
|--------|-----------|
| `set_preference` | `(key: str, value: str, confidence=1.0, source="explicit") -> None` |
| `get_preference` | `(key: str) -> Optional[str]` |
| `get_all_preferences` | `() -> Dict[str, str]` |
| `record_query_pattern` | `(pattern: str, query_type: str = None, example: str = None) -> None` |
| `get_frequent_patterns` | `(limit: int = 10) -> List[Dict]` |
| `add_entity_alias` | `(alias: str, canonical: str, entity_type: str = None) -> None` |
| `resolve_alias` | `(alias: str) -> Optional[str]` |
| `add_domain_knowledge` | `(topic: str, knowledge: str, source: str = None) -> None` |
| `get_domain_knowledge` | `(topic: str) -> List[Dict]` |
| `save_summary` | `(session_id: str, summary: str, message_count: int = 0) -> None` |
| `get_context_for_prompt` | `() -> str` |

### 5.3 Context Window Manager

**Source**: `agent/memory/summarizer.py`

#### ContextWindowManager

```python
class ContextWindowManager:
    def __init__(
        self,
        total_budget:          int = 100_000,
        system_budget:         int = 2_000,
        doc_budget:            int = 15_000,
        history_budget:        int = 60_000,
        learned_context_budget: int = 3_000,
        response_buffer:       int = 4_000,
    ):
```

> **Config/Code Discrepancy**: The code default for `history_budget` is `60_000`. In `agent_config.yaml`, `memory.history_budget` is set to `6000`. The yaml value takes precedence at runtime.

The manager enforces token budgets by truncating conversation history (oldest messages first) and documentation snippets (lowest-scoring first) to fit within allocations.

#### ConversationSummarizer

```python
class ConversationSummarizer:
    def __init__(self, provider_name: str = "claude"):
```

The summarizer invokes the LLM with a fixed `SUMMARY_PROMPT` that instructs the model to produce a concise summary of a conversation segment, preserving key decisions, SQL queries run, and user preferences expressed.

```python
SUMMARY_PROMPT = """You are summarizing a conversation between a database administrator and an AI assistant.
Create a concise summary that captures:
1. The main questions or tasks discussed
2. Key SQL queries generated or executed
3. Important findings or conclusions
4. Any user preferences or patterns observed
5. Database tables or procedures referenced

Keep the summary under 500 words and focus on information useful for continuing the conversation."""
```

Summarization is triggered when both thresholds are exceeded:

```python
def should_summarize(
    self,
    messages:           List,
    threshold_messages: int = 30,
    threshold_tokens:   int = 50_000,
) -> bool:
```

---

## 6. Tool Registry

### 6.1 ToolCategory Enum

**Source**: `agent/tools/base.py`

```python
class ToolCategory(str, Enum):
    SQL           = "sql"
    ANALYSIS      = "analysis"
    DOCUMENTATION = "documentation"
    MONITORING    = "monitoring"
    SCRIPT        = "script"
    UTILITY       = "utility"
```

### 6.2 Core Dataclasses

```python
@dataclass
class ToolParameter:
    name:        str
    type:        str
    description: str
    required:    bool = True
    default:     Any  = None
    enum:        Optional[List] = None

@dataclass
class ToolDefinition:
    name:        str
    description: str
    parameters:  List[ToolParameter]
    category:    ToolCategory
    returns:     str = ""

    def to_anthropic_format(self) -> Dict: ...
    def to_openai_format(self) -> Dict: ...
    def to_json_schema(self) -> Dict: ...

@dataclass
class ToolResult:
    success:  bool
    data:     Any             = None
    error:    Optional[str]   = None
    metadata: Dict            = field(default_factory=dict)

@dataclass
class ToolCall:
    tool_name:  str
    parameters: Dict
    call_id:    str = ""

@dataclass
class ToolCallResult:
    tool_call:  ToolCall
    result:     ToolResult
    duration_ms: float = 0.0
```

### 6.3 BaseTool Abstract Class

```python
class BaseTool(ABC):
    name:     str       # class attribute
    category: ToolCategory
    enabled:  bool = True

    @property
    @abstractmethod
    def definition(self) -> ToolDefinition: ...

    @abstractmethod
    def execute(self, **kwargs) -> ToolResult: ...

    def __call__(self, **kwargs) -> ToolResult:
        return self.execute(**kwargs)
```

### 6.4 ToolRegistry

**Source**: `agent/tools/registry.py`

```python
class ToolRegistry:
    def __init__(self):
        self._tools:      Dict[str, BaseTool]              = {}
        self._categories: Dict[ToolCategory, List[str]]    = {cat: [] for cat in ToolCategory}
```

Key methods:

| Method | Description |
|--------|-------------|
| `register(tool)` | Register one tool; raises `ValueError` on duplicate name |
| `register_many(tools)` | Register a list of tools |
| `unregister(name)` | Remove tool; returns removed instance or `None` |
| `get(name)` | Return tool instance or `None` |
| `get_definition(name)` | Return `ToolDefinition` or `None` |
| `list_tools(category=None, enabled_only=True)` | Sorted list of tool names |
| `get_all_definitions(category=None)` | List of `ToolDefinition` objects |
| `get_tools_for_llm(category=None, format="anthropic")` | Formatted for API calls; supports `"anthropic"`, `"openai"`, `"ollama"` (openai format) |
| `execute(name, **kwargs)` | Run tool by name; raises `ValueError` if not found or disabled |
| `enable_category(category)` | Enable all tools in a category |
| `disable_category(category)` | Disable all tools in a category |

The registry uses `__contains__` and `__iter__` for membership testing and iteration over tool names.

### 6.5 Global Registry and Tool Modules

A module-level singleton is maintained:

```python
_global_registry: Optional[ToolRegistry] = None

def get_registry() -> ToolRegistry: ...
def register_all_tools(config: Dict[str, Any] = None) -> ToolRegistry: ...
def get_tool(name: str) -> Optional[BaseTool]: ...
def execute_tool(name: str, **kwargs) -> Any: ...
def list_tools(category: Optional[ToolCategory] = None) -> List[str]: ...
```

`register_all_tools()` is **idempotent** — if `registry.tool_count > 0` it returns immediately. It loads 7 tool modules in order:

| Module | Factory function | Config keys consumed |
|--------|-----------------|---------------------|
| `agent.tools.sql_executor` | `create_sql_tools(config)` | `security.max_query_results` (default 100), `security.query_timeout` (default 30), `audit.enabled` (default True) |
| `agent.tools.query_generator` | `create_query_tools(config)` | `llm.default_provider` (default `"claude"`) |
| `agent.tools.script_runner` | `create_script_tools(config)` | `tools.scripts_dir` (default `"scripts"`), `tools.script_timeout` (default 300) |
| `agent.tools.doc_retriever` | `create_doc_tools(config)` | Full config passed through |
| `agent.tools.schema_introspector` | `create_schema_tools(config)` | `database.connection_string` |
| `agent.tools.catalog_search` | `create_catalog_tools(config)` | Full config passed through |
| `agent.tools.report_generator` | `create_report_tools(config)` | `llm.default_provider`, `reports.model`, `reports.output_dir` (default `"output"`), `reports.max_rows` (default 50000) |

Each module's import is wrapped in a `try/except ImportError` so missing optional dependencies degrade gracefully.

---

## 7. LLM Providers

### 7.1 MessageRole Enum

**Source**: `agent/llm/base.py`

```python
class MessageRole(str, Enum):
    SYSTEM    = "system"
    USER      = "user"
    ASSISTANT = "assistant"
    TOOL      = "tool"
```

### 7.2 Message Dataclass (LLM Layer)

```python
@dataclass
class Message:
    role:        MessageRole
    content:     str
    name:        Optional[str] = None
    tool_calls:  Optional[List[Dict]] = None
    tool_call_id: Optional[str] = None
```

### 7.3 LLMResponse Dataclass

```python
@dataclass
class LLMResponse:
    content:       str
    model:         str
    finish_reason: str          = "stop"
    tool_calls:    List[Dict]   = field(default_factory=list)
    usage:         Dict         = field(default_factory=dict)
```

Default `max_tokens=4096` applies when no value is specified in a `complete()` call.

### 7.4 BaseLLMProvider Abstract Class

```python
class BaseLLMProvider(ABC):
    @abstractmethod
    def complete(
        self,
        messages:   List[Message],
        tools:      List[Dict]   = None,
        max_tokens: int          = 4096,
        temperature: float       = 0.0,
    ) -> LLMResponse: ...

    @abstractmethod
    def stream(
        self,
        messages:    List[Message],
        max_tokens:  int   = 4096,
        temperature: float = 0.0,
    ) -> Generator[str, None, None]: ...

    @abstractmethod
    def count_tokens(self, text: str) -> int: ...

    @property
    @abstractmethod
    def context_window(self) -> int: ...
```

### 7.5 ProviderRegistry

**Source**: `agent/llm/registry.py`

```python
class ProviderRegistry:
    _providers: Dict[str, Type[BaseLLMProvider]] = {}   # class-level
    _instances: Dict[str, BaseLLMProvider]       = {}   # class-level
```

Instance cache key is `f"{name}:{model}"`. `register_all_providers()` registers three providers:

```python
from agent.llm.claude  import ClaudeProvider
from agent.llm.openai  import OpenAIProvider
from agent.llm.ollama  import OllamaProvider

registry.register("claude",  ClaudeProvider)
registry.register("openai",  OpenAIProvider)
registry.register("ollama",  OllamaProvider)
```

### 7.6 ClaudeProvider

**Source**: `agent/llm/claude.py`

```python
DEFAULT_MODEL = "claude-sonnet-4-20250514"

MODEL_CONTEXT_WINDOWS = {
    "claude-opus-4-5":             200_000,
    "claude-sonnet-4-5":           200_000,
    "claude-haiku-4-5":            200_000,
    "claude-sonnet-4-20250514":    200_000,
    "claude-opus-4-20250514":      200_000,
    "claude-3-5-sonnet-20241022":  200_000,
    "claude-3-5-haiku-20241022":   200_000,
}
```

> **Config/Code Discrepancy**: The code default is `"claude-sonnet-4-20250514"`. `agent_config.yaml` sets `default_provider: ollama`, so Claude is not the active provider at runtime unless explicitly selected.

Tool call parsing: the `complete()` method inspects `response.stop_reason == "tool_use"` and iterates `response.content` blocks looking for `block.type == "tool_use"`. Each is converted to a dict with keys `id`, `name`, `input`.

**`stream()` does not support tool calls.** Attempting to pass `tools` to the streaming path raises a `NotImplementedError` or silently ignores tools depending on the version — do not use `stream()` when tool use is required.

### 7.7 OpenAIProvider

**Source**: `agent/llm/openai.py` (referenced in registry; not exhaustively read)

Default model: `gpt-4o`.

### 7.8 OllamaProvider

**Source**: `agent/llm/ollama.py`

```python
DEFAULT_MODEL = "qwen2.5:14b"
DEFAULT_HOST  = "http://localhost:11434"

MODEL_CONTEXT_WINDOWS = {
    "llama3.3":         128_000,
    "llama3.1":         128_000,
    "llama3.2":         128_000,
    "llama3":            8_000,
    "mistral":           8_000,
    "mixtral":          32_000,
    "qwen2.5:14b":      32_000,
    "qwen2.5:7b":       32_000,
    "qwen2.5:72b":      32_000,
    "qwen2.5-coder:14b": 32_000,
    "phi3":              4_000,
    "phi3:medium":       4_000,
    "deepseek-r1:7b":   32_000,
    "deepseek-r1:14b":  32_000,
    "gemma2":            8_000,
    "gemma2:27b":        8_000,
}
```

Default context window for unlisted models: **4096 tokens**.

The provider uses the `ollama` Python SDK with a fallback to `httpx` for direct HTTP calls to the Ollama REST API when the SDK is unavailable.

> **Active Provider**: `agent_config.yaml` sets `default_provider: ollama` with `model: qwen2.5:14b`, making Ollama the default runtime provider.

---

## 8. Security

**Source**: `agent/security/validator.py`

### 8.1 QueryType Enum

```python
class QueryType(str, Enum):
    SELECT  = "select"
    INSERT  = "insert"
    UPDATE  = "update"
    DELETE  = "delete"
    DDL     = "ddl"
    EXEC    = "exec"
    UNKNOWN = "unknown"
```

### 8.2 ValidationResult Dataclass

```python
@dataclass
class ValidationResult:
    is_valid:    bool
    query_type:  QueryType
    warnings:    List[str]   = field(default_factory=list)
    errors:      List[str]   = field(default_factory=list)
    sanitized:   Optional[str] = None
    risk_level:  str           = "low"   # "low", "medium", "high"
```

### 8.3 QueryValidator

```python
class QueryValidator:
    def __init__(
        self,
        allow_writes:       bool       = False,
        allowed_databases:  List[str]  = None,  # defaults to ["EDS", "dpa_EDSAdmin"]
        max_query_length:   int        = 10_000,
    ):
```

Default `allowed_databases = ["EDS", "dpa_EDSAdmin"]`.

#### DEFAULT_BLOCKED_PATTERNS (12 patterns)

These compiled regex patterns cause immediate rejection (`is_valid=False`, `risk_level="high"`):

```python
DEFAULT_BLOCKED_PATTERNS = [
    r'\bxp_cmdshell\b',
    r'\bsp_executesql\b',
    r'\bOPENROWSET\b',
    r'\bOPENDATASOURCE\b',
    r'\bBULK\s+INSERT\b',
    r'\bWAITFOR\s+DELAY\b',
    r'\bWAITFOR\s+TIME\b',
    r'\bEXEC\s*\(',
    r'\bEXECUTE\s*\(',
    r'--.*?(\bDROP\b|\bDELETE\b|\bTRUNCATE\b)',
    r'/\*.*?(\bDROP\b|\bDELETE\b|\bTRUNCATE\b).*?\*/',
    r'\bSHUTDOWN\b',
]
```

#### WRITE_PATTERNS (10 patterns)

These patterns identify write operations. When `allow_writes=False` (the default), matching a write pattern sets `is_valid=False`:

```python
WRITE_PATTERNS = [
    r'^\s*INSERT\b',
    r'^\s*UPDATE\b',
    r'^\s*DELETE\b',
    r'^\s*TRUNCATE\b',
    r'^\s*DROP\b',
    r'^\s*CREATE\b',
    r'^\s*ALTER\b',
    r'^\s*MERGE\b',
    r'^\s*REPLACE\b',
    r'^\s*UPSERT\b',
]
```

#### SENSITIVE_PATTERNS (5 patterns)

These patterns add a `warning` but do not block execution. They flag queries accessing potentially sensitive data:

```python
SENSITIVE_PATTERNS = [
    r'\bpassword\b',
    r'\bsocial_security\b',
    r'\bssn\b',
    r'\bcredit_card\b',
    r'\bpii\b',
]
```

### 8.4 validate() Method

```python
def validate(
    self,
    query:           str,
    target_database: str = None,
) -> ValidationResult:
```

Validation sequence:
1. Length check against `max_query_length`
2. Database name check against `allowed_databases` (if `target_database` is provided)
3. Scan for blocked patterns → immediate rejection
4. Scan for write patterns → rejection if `allow_writes=False`
5. Scan for sensitive patterns → add warnings
6. Classify query type via `QueryType` enum
7. Return `ValidationResult`

---

## 9. Audit System

**Source**: `agent/audit/logger.py`

### 9.1 AuditEventType Enum

```python
class AuditEventType(str, Enum):
    QUERY_EXECUTED  = "query_executed"
    QUERY_BLOCKED   = "query_blocked"
    QUERY_FAILED    = "query_failed"
    TOOL_CALLED     = "tool_called"
    TOOL_FAILED     = "tool_failed"
    SESSION_STARTED = "session_started"
    SESSION_ENDED   = "session_ended"
    CONFIG_CHANGED  = "config_changed"
    ERROR           = "error"
    SECURITY_ALERT  = "security_alert"
    LLM_CALLED      = "llm_called"
    LLM_FAILED      = "llm_failed"
    REPORT_GENERATED = "report_generated"
```

### 9.2 AuditEvent Dataclass

```python
@dataclass
class AuditEvent:
    event_type: AuditEventType
    timestamp:  datetime       = field(default_factory=datetime.utcnow)
    session_id: Optional[str]  = None
    data:       Dict           = field(default_factory=dict)
    metadata:   Dict           = field(default_factory=dict)
```

### 9.3 AuditLogger

```python
class AuditLogger:
    def __init__(
        self,
        log_dir:        str  = "data/audit_logs",
        rotation_days:  int  = 1,
        retention_days: int  = 90,
        enabled:        bool = True,
    ):
```

Events are written as newline-delimited JSON (JSONL) to daily log files named `audit_YYYY-MM-DD.jsonl`. The logger is thread-safe via a `threading.Lock`. Gzip compression is applied to rotated log files.

A module-level singleton:
```python
_global_logger: Optional[AuditLogger] = None

def get_audit_logger() -> AuditLogger: ...
```

Convenience logging methods on `AuditLogger`:

| Method | Signature |
|--------|-----------|
| `log_query` | `(sql: str, session_id=None, result_count=None, duration_ms=None) -> None` |
| `log_blocked_query` | `(sql: str, reason: str, session_id=None) -> None` |
| `log_tool_call` | `(tool_name: str, params: Dict, session_id=None, success=True, error=None) -> None` |
| `log_session_start` | `(session_id: str, provider: str, mode: str) -> None` |
| `log_session_end` | `(session_id: str, message_count: int, total_tokens: int) -> None` |
| `log_llm_call` | `(provider: str, model: str, tokens_in: int, tokens_out: int, duration_ms: float, session_id=None) -> None` |
| `log_error` | `(error: str, context: Dict = None, session_id=None) -> None` |
| `log_security_alert` | `(alert_type: str, details: Dict, session_id=None) -> None` |

---

## 10. Export System

### 10.1 Report Plan Schema

**Source**: `agent/export/models.py`

#### ColumnDef

```python
@dataclass
class ColumnDef:
    name:    str
    type:    str    # "string", "number", "currency", "percentage", "date"
    header:  str
    width:   int = 15
    format:  Optional[str] = None
```

#### QueryDef

```python
@dataclass
class QueryDef:
    sql:         str
    name:        str
    description: str = ""
    params:      Dict = field(default_factory=dict)
```

#### SheetDef

```python
@dataclass
class SheetDef:
    name:        str
    title:       str
    query:       str           # references a QueryDef name
    columns:     List[ColumnDef] = field(default_factory=list)
    type:        str           = "detail"   # valid: "summary", "detail", "pivot", "drilldown"
    pivot_rows:  List[str]     = field(default_factory=list)
    pivot_cols:  List[str]     = field(default_factory=list)
    pivot_values: List[str]    = field(default_factory=list)
    pivot_agg:   str           = "sum"      # default aggregation for pivot sheets
    chart:       Optional[Dict] = None
```

#### ReportPlan

```python
@dataclass
class ReportPlan:
    title:       str
    description: str
    queries:     List[QueryDef]
    sheets:      List[SheetDef]
    metadata:    Dict = field(default_factory=dict)
```

A `REPORT_PLAN_JSON_SCHEMA` constant (JSON Schema dict) is defined at module level and used by the LLM tool definition to constrain generated report plans.

### 10.2 EDS Brand Colors

**Source**: `agent/export/excel_formatter.py`

```python
class EDSColors:
    PRIMARY          = "1C1A83"   # EDS dark blue (header backgrounds)
    SECONDARY        = "4A4890"   # EDS medium blue (subheaders)
    ACCENT           = "B70C0D"   # EDS red (alerts, highlights)
    LIGHT_BLUE       = "E8E7F4"   # Alternating row tint
    WHITE            = "FFFFFF"
    BLACK            = "000000"
    DARK_GRAY        = "404040"   # Body text
    MEDIUM_GRAY      = "808080"   # Secondary text
    LIGHT_GRAY       = "F5F5F5"   # Alternate row background
    BORDER_GRAY      = "CCCCCC"   # Cell borders
    SUCCESS_GREEN    = "1E7E34"   # Positive variance indicators
    WARNING_YELLOW   = "856404"   # Warning state
```

All openpyxl `PatternFill`, `Font`, `Border`, `Alignment`, and `Side` objects for the standard EDS style palette are created once at module import time and shared across all report workbooks.

The `apply_cell_format(cell, format_type)` function maps format type strings to Excel number format codes:

| `format_type` | Format string |
|--------------|---------------|
| `"currency"` | `"$#,##0.00"` |
| `"percentage"` | `"0.00%"` |
| `"integer"` | `"#,##0"` |
| `"date"` | `"MM/DD/YYYY"` |
| `"datetime"` | `"MM/DD/YYYY HH:MM"` |

The `finalize_sheet(ws)` function sets `ws.freeze_panes = "A2"` on every sheet to lock the header row.

### 10.3 ReportBuilder

**Source**: `agent/export/report_builder.py`

```python
class ReportBuilder:
    def __init__(
        self,
        output_dir: str = "output",
        max_rows:   int = 50_000,
        timeout:    int = 120,
    ):
```

The `build(report_plan: ReportPlan, connection_string: str) -> Dict` method executes each `QueryDef`, applies column definitions, formats cells via `excel_formatter`, and writes an `.xlsx` file to `output_dir`. It returns a dict with keys: `file_path`, `sheets_written`, `total_rows`, `elapsed_seconds`, `warnings`.

---

## 11. GUI Application

**Source**: `agent/gui/app.py`, `agent/gui/state.py`

### 11.1 Application Constants

```python
APP_TITLE           = "EDS DBA Agent"
DEFAULT_WINDOW_SIZE = (1400, 900)
```

### 11.2 Routes

Six NiceGUI routes are registered:

| Route | Description |
|-------|-------------|
| `/` | Main chat interface |
| `/sessions` | Session browser |
| `/reports` | Report management and generation |
| `/docs` | Documentation search |
| `/settings` | Configuration UI |
| `/status` | System health dashboard |

### 11.3 Application Launch

```python
def run_app(
    host:   str  = "127.0.0.1",
    port:   int  = 8080,
    native: bool = True,
) -> None:
```

`native=True` launches a native OS window (via pywebview) at `DEFAULT_WINDOW_SIZE` instead of opening a browser tab. This is the default mode.

### 11.4 Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+Enter` | Submit current message |
| `Ctrl+N` | New session |
| `Ctrl+L` | Clear current session |
| `Ctrl+S` | Save session |
| `Escape` | Cancel current operation |

### 11.5 State Types

**Source**: `agent/gui/state.py`

```python
class Theme(str, Enum):
    LIGHT  = "light"
    DARK   = "dark"
    SYSTEM = "system"

@dataclass
class Message:
    role:      str
    content:   str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata:  Dict     = field(default_factory=dict)

@dataclass
class QueryRecord:
    sql:        str
    timestamp:  datetime
    duration_ms: float
    row_count:  int
    success:    bool

@dataclass
class Alert:
    type:    str   # "info", "warning", "error", "success"
    message: str
    timeout: int = 5   # seconds before auto-dismiss
```

`AppState` initial values include `theme=Theme.SYSTEM`, empty message lists, `is_loading=False`, `current_session_id=None`.

---

## 12. CLI Interface

### 12.1 Commands

**Source**: `agent/cli/app.py`

All commands are registered under the `eds-agent` entry point (also accessible as `python -m agent`).

#### `chat`
```
eds-agent chat [OPTIONS]

Options:
  --session TEXT      Resume an existing session by ID
  --mode [chat|sql|docs|analyze]
                      Initial agent mode (default: chat)
  --provider TEXT     LLM provider override (claude/openai/ollama)
  --model TEXT        Model name override
```

Launches the interactive REPL.

#### `ask`
```
eds-agent ask QUESTION [OPTIONS]

Options:
  --session TEXT      Session ID for context
  --mode [chat|sql|docs|analyze]
  --format [text|json|table]
                      Output format (default: text)
  --provider TEXT
  --model TEXT
```

Single-turn question, returns response and exits.

#### `sql`
```
eds-agent sql DESCRIPTION [OPTIONS]

Options:
  --execute           Execute the generated SQL (default: show only)
  --format [text|json|table]
  --limit INTEGER     Row limit for execution (default: 100)
  --provider TEXT
  --model TEXT
```

Generate SQL from natural language description.

#### `report`
```
eds-agent report DESCRIPTION [OPTIONS]

Options:
  --output TEXT       Output file path (default: auto-generated in output/)
  --max-rows INTEGER  Row limit per sheet (default: 50000)
  --format [xlsx]     Output format (currently only xlsx)
  --provider TEXT
  --model TEXT
```

Generate an Excel report from a natural language description.

#### `docs`
```
eds-agent docs QUERY [OPTIONS]

Options:
  --n-results INTEGER  Number of results to return (default: 5)
  --type [semantic|keyword|hybrid]
                       Retrieval strategy (default: hybrid)
  --format [text|json]
```

Search the documentation index.

#### `run`
```
eds-agent run SCRIPT_NAME [OPTIONS]

Options:
  --args TEXT         Arguments to pass to the script
  --timeout INTEGER   Script timeout in seconds (default: 300)
```

Execute a named script from the scripts directory.

#### `status`
```
eds-agent status [OPTIONS]

Options:
  --format [text|json]
  --verbose
```

Display system health: LLM provider connectivity, database connectivity, RAG index statistics, memory usage.

#### `sessions`
```
eds-agent sessions [COMMAND]

Commands:
  list    List recent sessions (--limit N)
  show    Show session details (SESSION_ID)
  delete  Delete a session (SESSION_ID)
  export  Export session to JSON (SESSION_ID --output FILE)
```

#### `version`
```
eds-agent version
```

Print version information and exit.

### 12.2 Interactive REPL

**Source**: `agent/cli/repl.py`

```python
class AgentREPL:
    history_file = Path.home() / ".eds_agent_history"
```

The REPL uses `readline` (or `pyreadline` on Windows) to provide command history persisted to `~/.eds_agent_history`.

#### Slash Commands (15 total)

| Command | Description |
|---------|-------------|
| `/help` | Show available commands |
| `/exit` or `/quit` | Exit the REPL |
| `/clear` | Clear the screen |
| `/mode [chat\|sql\|docs\|analyze]` | Switch agent mode |
| `/session` | Show current session ID |
| `/new` | Start a new session |
| `/sessions` | List recent sessions |
| `/load SESSION_ID` | Load an existing session |
| `/history` | Show conversation history |
| `/sql QUERY` | Execute SQL directly |
| `/docs QUERY` | Search documentation |
| `/status` | Show system status |
| `/config` | Show current configuration |
| `/provider PROVIDER` | Switch LLM provider |
| `/model MODEL` | Switch model |

```python
def run_repl(agent: EDSAgent, session_id: str = None, mode: AgentMode = AgentMode.CHAT) -> None:
```

---

## 13. Configuration Reference

**Source**: `agent_config.yaml` (project root)

The configuration file is loaded and passed as a dict throughout the system. Each module reads its relevant subtree. Environment variables for API keys (`ANTHROPIC_API_KEY`, `OPENAI_API_KEY`) are loaded separately and not stored in the config file.

### 13.1 LLM Section

```yaml
llm:
  default_provider: ollama        # Code default: "claude"
  default_model: qwen2.5:14b
  temperature: 0.0
  max_tokens: 4096
  providers:
    claude:
      model: claude-sonnet-4-20250514
      max_tokens: 4096
    openai:
      model: gpt-4o
      max_tokens: 4096
    ollama:
      host: http://localhost:11434
      model: qwen2.5:14b
      context_length: 32768
```

> **Discrepancy**: `default_provider` is `"ollama"` in yaml; code fallback is `"claude"`.

### 13.2 RAG Section

```yaml
rag:
  enabled: true
  vector_store_path: data/vectordb
  collection_name: eds_documentation
  embedding_provider: local
  embedding_model: sentence-transformers/all-MiniLM-L6-v2
  chunk_size: 512
  chunk_overlap: 64
  n_results: 5
  semantic_weight: 0.7
  keyword_weight: 0.3
  rrf_k: 60
  rerank: true               # Code default: False (HybridRetriever use_reranking=False)
  reranker_model: cross-encoder/ms-marco-MiniLM-L-6-v2
  min_score: 0.3
  docs_path: docs/
```

> **Discrepancy**: `rerank` is `true` in yaml; `HybridRetriever` code default is `use_reranking=False`.

### 13.3 Memory Section

```yaml
memory:
  sessions_dir: data/sessions
  max_sessions: 100
  auto_save: true
  learned_context_db: data/memory/knowledge.sqlite
  context_window:
    total_budget: 100000
    system_budget: 2000
    doc_budget: 15000
    history_budget: 6000        # Code default: 60000
    learned_context_budget: 3000
    response_buffer: 4000
  summarization:
    enabled: true
    threshold_messages: 30
    threshold_tokens: 50000
    provider: claude
```

> **Discrepancy**: `history_budget` is `6000` in yaml; `ContextWindowManager` code default is `60_000`.

### 13.4 Database Section

```yaml
database:
  connection_string: null      # Loaded from .env: DB_SERVER, DB_DATABASE, etc.
  max_results: 100
  query_timeout: 30
  databases:
    - EDS
    - dpa_EDSAdmin
```

### 13.5 Security Section

```yaml
security:
  allow_writes: false
  allowed_databases:
    - EDS
    - dpa_EDSAdmin
  max_query_length: 10000
  max_query_results: 100
  query_timeout: 30
  blocked_patterns: []         # Merged with DEFAULT_BLOCKED_PATTERNS in code
```

### 13.6 Audit Section

```yaml
audit:
  enabled: true
  log_dir: data/audit_logs
  rotation_days: 1
  retention_days: 90
```

### 13.7 Tools Section

```yaml
tools:
  scripts_dir: scripts
  script_timeout: 300
  catalog_search:
    enabled: true
    elasticsearch_url: http://20.122.81.233:9200
    index_pattern: "eds_catalog_*"
```

### 13.8 Reports Section

```yaml
reports:
  output_dir: output
  max_rows: 50000
  model: null                  # Uses default_model if null
  template_dir: agent/export/templates
```

### 13.9 GUI Section

```yaml
gui:
  host: 127.0.0.1
  port: 8080
  native: true
  window_size: [1400, 900]
  theme: system
  title: EDS DBA Agent
```

### 13.10 Configuration Priority

Configuration values are resolved in this order (highest priority first):

1. Explicit constructor arguments (e.g., `EDSAgent(config={...})`)
2. `agent_config.yaml` values
3. Code-level defaults in each class constructor

---

## 14. End-to-End Data Flow

### 14.1 Typical Chat Request

```
User input
    │
    ▼
AgentREPL.process_input()
    │
    ▼
EDSAgent.chat(message, session_id, mode)
    │
    ├─► SessionManager.add_message()          # Persist user message
    │
    ├─► LearnedContextDB.get_context_for_prompt()  # Inject learned facts
    │
    ├─► _should_use_rag(message)?
    │       │ yes
    │       └─► HybridRetriever.retrieve()
    │               ├─► VectorStore.query()   # Semantic search
    │               ├─► BM25Index.search()    # Keyword search
    │               └─► RRF fusion + optional reranking
    │
    ├─► ContextWindowManager.build_context()  # Trim to token budget
    │
    ├─► ToolRegistry.get_tools_for_llm()     # Inject tool schemas
    │
    ├─► LLMProvider.complete(messages, tools)
    │       │
    │       └─► Tool calls in response?
    │               │ yes
    │               └─► ToolRegistry.execute(tool_name, **params)
    │                       ├─► QueryValidator.validate()  # Security check
    │                       ├─► AuditLogger.log_query()
    │                       └─► SQL Server / Elasticsearch / filesystem
    │
    ├─► AgentResponse constructed
    │
    ├─► SessionManager.add_message()         # Persist assistant response
    │
    └─► AuditLogger.log_llm_call()
```

### 14.2 Streaming Variant

For `chat_stream()`, Phase 1 (tool calls) runs synchronously as above. Phase 2 yields `final_text` in 12-character chunks with status markers emitted between phases.

### 14.3 SQL Generation Flow

```
eds-agent sql "description"
    │
    ▼
CLISQLCommand
    │
    ▼
EDSAgent.generate_sql(description, context)
    │
    ├─► schema_introspector tool (if enabled) → relevant table schemas
    │
    ├─► LLMProvider.complete() with SQL-generation system prompt
    │
    ├─► QueryValidator.validate(generated_sql)
    │       ├─► blocked? → return error
    │       └─► pass → return SQL
    │
    └─► --execute flag?
            │ yes
            └─► sql_executor tool → results → formatted output
```

### 14.4 Report Generation Flow

```
eds-agent report "description"
    │
    ▼
CLIReportCommand
    │
    ▼
report_generator tool (LLM-driven)
    │
    ├─► LLM generates ReportPlan JSON (validated against REPORT_PLAN_JSON_SCHEMA)
    │
    ├─► ReportBuilder.build(plan, connection_string)
    │       │
    │       ├─► For each QueryDef:
    │       │       ├─► QueryValidator.validate()
    │       │       └─► sql_executor → rows (up to max_rows=50000)
    │       │
    │       └─► Excel workbook:
    │               ├─► EDSColors + shared styles applied
    │               ├─► freeze_panes = "A2" on each sheet
    │               └─► .xlsx written to output/
    │
    └─► File path returned to CLI
```

---

## 15. Appendix

### 15.1 File Path Index

| Description | Path |
|-------------|------|
| Main orchestrator | `agent/core/agent.py` |
| CLI entry point | `agent/cli/app.py` |
| Interactive REPL | `agent/cli/repl.py` |
| GUI application | `agent/gui/app.py` |
| GUI state types | `agent/gui/state.py` |
| LLM base types | `agent/llm/base.py` |
| LLM registry | `agent/llm/registry.py` |
| Claude provider | `agent/llm/claude.py` |
| Ollama provider | `agent/llm/ollama.py` |
| Tool base types | `agent/tools/base.py` |
| Tool registry | `agent/tools/registry.py` |
| Document chunker | `agent/rag/chunker.py` |
| Embedding providers | `agent/rag/embeddings.py` |
| Vector store | `agent/rag/vector_store.py` |
| Hybrid retriever | `agent/rag/retriever.py` |
| Document indexer | `agent/rag/indexer.py` |
| Session manager | `agent/memory/session.py` |
| Learned context | `agent/memory/learned_context.py` |
| Context/summarizer | `agent/memory/summarizer.py` |
| SQL validator | `agent/security/validator.py` |
| Audit logger | `agent/audit/logger.py` |
| Report plan schema | `agent/export/models.py` |
| Excel formatter | `agent/export/excel_formatter.py` |
| Report builder | `agent/export/report_builder.py` |
| Runtime configuration | `agent_config.yaml` |
| Package manifest | `agent/pyproject.toml` |
| Agent CLAUDE.md | `agent/CLAUDE.md` |

### 15.2 Known Config/Code Discrepancies

The following values differ between the runtime `agent_config.yaml` and the code-level defaults. The yaml value is authoritative at runtime.

| Parameter | Code Default | yaml Value |
|-----------|-------------|------------|
| `llm.default_provider` | `"claude"` | `"ollama"` |
| `memory.context_window.history_budget` | `60000` | `6000` |
| `rag.rerank` | `False` (in `HybridRetriever`) | `true` |

### 15.3 Glossary

| Term | Definition |
|------|-----------|
| **RAG** | Retrieval-Augmented Generation: augmenting LLM prompts with retrieved document context |
| **BM25** | Best Match 25: probabilistic ranking function for keyword search |
| **RRF** | Reciprocal Rank Fusion: score combination formula for hybrid search results |
| **Cross-encoder** | Reranking model that jointly encodes query and passage for precise relevance scoring |
| **ChromaDB** | Open-source embedded vector database used for semantic search |
| **Tool calling** | LLM capability to emit structured JSON requesting execution of registered functions |
| **Lazy initialization** | Pattern where subsystems are created on first access, not at import time |
| **JSONL** | JSON Lines format: one JSON object per line, used for audit logs |
| **EDS** | Educational Data Services: the SQL Server database this agent is designed to query |
| **DPA** | Database Performance Analytics: the `dpa_EDSAdmin` monitoring database |
