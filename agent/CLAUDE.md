# Agent CLAUDE.md

Development guide for the EDS DBA Agent (`/agent/`).

## Quick Start

```bash
pip install -e ".[agent]"       # Install agent dependencies
python -m agent status          # Verify setup
python -m agent chat            # Interactive session
python -m agent chat --provider claude --mode sql
```

## Architecture

```
agent/
├── core/agent.py          # EDSAgent orchestrator (tool-calling loop, session, user context)
├── cli/{app,repl}.py      # Click CLI (9 commands) + interactive REPL
├── gui/{app,state}.py     # NiceGUI desktop app with streaming + tool display
├── llm/{base,registry,claude,openai_provider,ollama}.py  # Multi-provider LLM
├── tools/                 # 7 tools: sql_executor, query_generator, doc_retriever,
│                          #   script_runner, schema_introspector, catalog_search, report_generator
├── rag/                   # Chunker → embeddings → ChromaDB → hybrid retriever (BM25+semantic+RRF)
├── memory/                # SessionManager (JSON) + LearnedContextDB (SQLite) + ContextWindowManager
├── security/              # QueryValidator (12 blocked patterns) + roles (9-tier approval levels)
├── audit/                 # Thread-safe JSONL logger with rotation
├── export/                # ReportPlan models + Excel formatter (EDS brand) + ReportBuilder
└── config.py              # Loads agent_config.yaml + env overrides
```

## Running Tests

```bash
pytest tests/agent/ -v              # All agent tests (249)
pytest tests/agent/test_roles.py    # Role/permission tests only
pytest tests/agent/ -k "integration" # End-to-end wiring tests
```

## Key Design Decisions

- **Lazy initialization**: All subsystems (LLM, tools, RAG, audit, sessions) are created on first access, not at import time. A `chat()` call that doesn't need RAG never loads ChromaDB.
- **Tool-calling loop**: `EDSAgent.chat()` runs up to 5 rounds — LLM requests tools, agent executes, feeds results back, LLM responds.
- **Role-aware**: `set_user_context(user_id, approval_level, ...)` configures what the agent tells the LLM about the user's permissions. Level 0 teachers can't execute SQL; level 9 admins get full access.
- **Audit everything**: LLM calls, tool executions, blocked queries, and security alerts are logged to JSONL with daily rotation.
- **Session persistence**: Conversations are stored as JSON files in `data/sessions/`. Learned context (preferences, patterns, aliases) accumulates in SQLite.

## Approval Levels (from EDS database)

| Level | Role | Agent Capabilities |
|-------|------|--------------------|
| 0 | Teacher/Staff | View own data, no SQL execution |
| 1 | Principal | Approve reqs, view school data |
| 2 | Business Admin | District view, budget editing |
| 3 | Accounting | Financial reports |
| 5 | Buyer/CSR | SQL execution (read-only), PO creation, bid management |
| 7-8 | Support/EDS Admin | User management, SQL writes |
| 9 | System Admin | Full access, system config |

## Adding a New Tool

1. Create `agent/tools/my_tool.py` with a class extending `BaseTool`
2. Implement `definition` property (returns `ToolDefinition`) and `execute(**kwargs)` method
3. Add a `create_my_tools(config)` factory function
4. Register in `agent/tools/registry.py` `_loaders` list
5. The tool is automatically available to the LLM via the tool-calling loop

## Adding a New LLM Provider

1. Create `agent/llm/my_provider.py` extending `BaseLLMProvider`
2. Implement `complete()`, `stream()`, `count_tokens()`, `context_window`, `model_name`
3. Register in `agent/llm/registry.py` `register_all_providers()`
4. Add config section in `agent_config.yaml` under `llm.providers`

## Environment Variables

| Variable | Purpose |
|----------|---------|
| `LLM_PROVIDER` | Override default provider (claude/openai/ollama) |
| `ANTHROPIC_API_KEY` | Claude API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `OLLAMA_HOST` | Ollama server URL (default: http://localhost:11434) |
| `DB_SERVER` | SQL Server hostname |
| `DB_DATABASE` | Default database name |
| `DB_USERNAME` / `DB_PASSWORD` | Database credentials |

## CLI Commands

```
eds-agent chat [--provider] [--model] [--mode] [--session] [--debug]
eds-agent ask QUESTION [--provider] [--session] [--mode]
eds-agent sql DESCRIPTION [--provider] [--session]
eds-agent docs QUERY [--provider]
eds-agent run SCRIPT [--args]
eds-agent report DESCRIPTION [--provider] [--preview]
eds-agent sessions [--limit] [--delete ID]
eds-agent status
eds-agent index-docs [--rebuild] [--file]
eds-agent mcp [--sse]                          # Start MCP server
```

## MCP Server

The agent can run as a Model Context Protocol server for Claude Desktop or Claude Code.

```bash
eds-agent mcp                # stdio transport (for Claude Desktop)
eds-agent mcp --sse          # SSE transport (for web clients)
eds-agent-mcp                # Direct entry point
```

**Exposed MCP tools:** `execute_sql`, `generate_sql`, `search_docs`, `introspect_schema`, `search_catalog`, `run_script`, `chat_with_agent`

**Resources:** `eds://status`, `eds://approval-levels`

**Prompts:** `sql_query`, `investigate_table`, `vendor_report`

To use with Claude Desktop, add to `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "eds-dba-agent": {
      "command": "eds-agent-mcp"
    }
  }
}
```
