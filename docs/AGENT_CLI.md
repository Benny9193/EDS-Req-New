# EDS DBA Agent Guide

AI-powered database assistant for SQL Server performance analysis, natural language queries, and documentation search.

---

## Overview

The EDS DBA Agent is an intelligent assistant that helps with:

- **Natural Language to SQL** - Ask questions in plain English, get SQL queries
- **Performance Analysis** - Automated diagnostics and recommendations
- **Documentation Search** - RAG-powered search through EDS documentation
- **Script Execution** - Run analysis scripts with natural language commands
- **Proactive Monitoring** - Background monitoring with alerts (optional)

---

## Installation

### Basic Installation

```bash
cd /mnt/c/EDS

# Install with agent dependencies
pip install -e ".[agent]"

# Or install all dependencies
pip install -e ".[all]"
```

### LLM Provider Setup

#### Claude (Anthropic) - Recommended

```bash
# Set API key
export ANTHROPIC_API_KEY=your-api-key

# Or add to .env file in agent directory
echo "ANTHROPIC_API_KEY=your-api-key" >> agent/.env
```

#### OpenAI

```bash
export OPENAI_API_KEY=your-api-key
```

#### Ollama (Local)

```bash
# Install Ollama (https://ollama.ai)
# Pull a model
ollama pull qwen2.5:14b

# Start Ollama server (default: localhost:11434)
ollama serve
```

---

## Quick Start

### Interactive Chat

```bash
# Start interactive session
eds-agent chat

# Or run as module
python -m agent chat
```

### Single Questions

```bash
# Ask a question
eds-agent ask "What tables contain vendor information?"

# Generate SQL
eds-agent sql "Show top 10 vendors by order count"

# Search documentation
eds-agent docs "requisition approval process"

# Check status
eds-agent status
```

---

## CLI Commands

### `eds-agent chat`

Start an interactive chat session with the agent.

```bash
eds-agent chat [OPTIONS]

Options:
  --provider TEXT    LLM provider (claude, openai, ollama)
  --mode TEXT        Initial mode (chat, sql, docs, analyze)
  --debug           Enable debug output
```

**In-session commands:**
- `/sql` - Switch to SQL generation mode
- `/docs` - Switch to documentation search mode
- `/analyze` - Switch to analysis mode
- `/clear` - Clear conversation history
- `/exit` or `/quit` - Exit the session

### `eds-agent ask`

Ask a single question and get an answer.

```bash
eds-agent ask "What is the schema for the Vendors table?"
eds-agent ask "How do I find blocking queries?"
```

### `eds-agent sql`

Generate SQL from natural language.

```bash
eds-agent sql "List all vendors with more than 100 orders"
eds-agent sql "Find products not ordered in the last 30 days"
eds-agent sql "Show average order value by month for 2024"
```

The agent will:
1. Generate the SQL query
2. Show the query for review
3. Optionally execute it (with confirmation)

### `eds-agent docs`

Search through EDS documentation using RAG.

```bash
eds-agent docs "stored procedure dependencies"
eds-agent docs "order approval workflow"
eds-agent docs "index recommendations"
```

### `eds-agent run`

Execute analysis scripts with arguments.

```bash
# Run performance analysis
eds-agent run analyze_performance_issues --args --days 30

# Extract missing indexes
eds-agent run extract_missing_indexes

# Generate documentation
eds-agent run generate_data_dictionary
```

### `eds-agent status`

Show agent status and configuration.

```bash
eds-agent status

# Output:
# EDS DBA Agent Status
# ====================
# LLM Provider: claude (claude-sonnet-4-20250514)
# Database: EDS (connected)
# RAG Index: 1,234 documents
# Session: active (5 turns)
```

---

## Operation Modes

### Chat Mode (Default)

General conversation about the database, SQL, and EDS system.

```
User: What tables are related to purchase orders?
Agent: The main tables related to purchase orders are:
       - PurchaseOrders (header information)
       - PurchaseOrderDetails (line items)
       - Vendors (supplier information)
       ...
```

### SQL Mode

Focused on generating and executing SQL queries.

```
User: /sql
Agent: Switched to SQL mode. Describe what you want to query.

User: Show vendors with no orders in 2024
Agent: Here's the SQL:
       SELECT v.VendorID, v.VendorName
       FROM Vendors v
       WHERE NOT EXISTS (
           SELECT 1 FROM PurchaseOrders po
           WHERE po.VendorID = v.VendorID
           AND YEAR(po.OrderDate) = 2024
       )

       Execute this query? (y/n)
```

### Docs Mode

Search and retrieve information from documentation.

```
User: /docs
Agent: Switched to documentation mode. What would you like to search?

User: How do triggers work in the order system?
Agent: Based on the documentation:
       [EDS_TRIGGERS.md] The order system uses several triggers...
```

### Analyze Mode

Run diagnostic analyses on the database.

```
User: /analyze
Agent: Switched to analysis mode. What would you like to analyze?

User: Check for blocking issues in the last hour
Agent: Running blocking analysis...
       [Results from investigate_blocking_event.py]
```

---

## Configuration

### Main Configuration File

**Location:** `agent_config.yaml` (project root) or `agent/agent_config.yaml`

```yaml
# LLM Provider Configuration
llm:
  default_provider: claude
  providers:
    claude:
      model: claude-sonnet-4-20250514
      temperature: 0.0
      max_tokens: 4096
    openai:
      model: gpt-4o
      temperature: 0.0
    ollama:
      model: qwen2.5:14b
      host: http://localhost:11434

# RAG Configuration
rag:
  embeddings:
    provider: local
    model: sentence-transformers/all-MiniLM-L6-v2
  retrieval:
    default_results: 5
    max_results: 20

# Security Settings
security:
  read_only_mode: false
  require_confirmation_for_writes: true
  allowed_databases:
    - EDS
    - dpa_EDSAdmin

# Tool Settings
tools:
  scripts_dir: scripts
  script_timeout: 300
```

### Environment Variables

| Variable | Purpose | Example |
|----------|---------|---------|
| `ANTHROPIC_API_KEY` | Claude API key | `sk-ant-...` |
| `OPENAI_API_KEY` | OpenAI API key | `sk-...` |
| `DB_SERVER` | SQL Server host | `localhost` |
| `DB_DATABASE` | Default database | `EDS` |

### Security Configuration

```yaml
security:
  # Block all write operations
  read_only_mode: true

  # Require confirmation for writes (when read_only_mode: false)
  require_confirmation_for_writes: true

  # Only allow queries to these databases
  allowed_databases:
    - EDS
    - dpa_EDSAdmin

  # Always blocked operations
  blocked_operations:
    - DROP DATABASE
    - xp_cmdshell
    - sp_configure
```

---

## Architecture

### Component Overview

```
┌────────────────────────────────────────────────────────────┐
│                      CLI / GUI                              │
│  (cli/app.py)           (gui/app.py)                       │
└────────────────────────────────────────────────────────────┘
                            │
                            ▼
┌────────────────────────────────────────────────────────────┐
│                    Core Agent                               │
│                   (core/agent.py)                          │
│                                                            │
│   ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐    │
│   │   LLM    │ │  Tools   │ │  Memory  │ │   RAG    │    │
│   │ Provider │ │ Registry │ │ Manager  │ │ Pipeline │    │
│   └──────────┘ └──────────┘ └──────────┘ └──────────┘    │
└────────────────────────────────────────────────────────────┘
         │              │            │            │
         ▼              ▼            ▼            ▼
┌──────────────┐ ┌──────────────┐ ┌─────────┐ ┌──────────────┐
│ Claude/OpenAI│ │ SQL Executor │ │Sessions │ │ Vector Store │
│   /Ollama    │ │Script Runner │ │ Memory  │ │  (ChromaDB)  │
└──────────────┘ └──────────────┘ └─────────┘ └──────────────┘
```

### Directory Structure

```
agent/
├── core/           # Main agent orchestrator
│   └── agent.py    # EDSAgent class
├── cli/            # Command-line interface
│   └── app.py      # Click-based CLI
├── gui/            # Web GUI (NiceGUI)
│   └── app.py      # GUI application
├── llm/            # LLM providers
│   ├── base.py     # BaseLLMProvider
│   ├── claude.py   # Claude implementation
│   ├── openai.py   # OpenAI implementation
│   └── ollama.py   # Ollama implementation
├── tools/          # Agent tools
│   ├── sql_executor.py
│   ├── query_generator.py
│   ├── script_runner.py
│   └── doc_retriever.py
├── rag/            # RAG pipeline
│   ├── chunker.py
│   ├── embeddings.py
│   ├── vectorstore.py
│   └── retriever.py
├── memory/         # Session and context
│   ├── session.py
│   └── learned_context.py
├── security/       # SQL validation
│   └── validator.py
└── audit/          # Audit logging
    └── logger.py
```

---

## Available Tools

### SQL Executor

Execute SQL queries against the EDS database.

```python
# Tool: sql_executor
# Input: SQL query string
# Output: Query results as formatted table
```

### Query Generator

Generate SQL from natural language descriptions.

```python
# Tool: query_generator
# Input: Natural language question
# Output: Generated SQL query
```

### Script Runner

Execute existing Python analysis scripts.

```python
# Tool: script_runner
# Input: Script name and arguments
# Output: Script output
```

### Documentation Retriever

Search documentation using RAG.

```python
# Tool: doc_retriever
# Input: Search query
# Output: Relevant documentation excerpts
```

---

## GUI Application

The agent includes a web-based GUI built with NiceGUI.

### Starting the GUI

```bash
# Run the GUI
eds-agent-gui

# Or
python -m agent.gui.app
```

### GUI Features

- Chat interface with syntax highlighting
- SQL query builder and executor
- Documentation browser
- Session history
- Settings panel

---

## Examples

### Example: Finding Slow Queries

```bash
$ eds-agent ask "What are the slowest queries in the last week?"

Agent: I'll analyze the slow queries from the past week.

Based on the DPA data, here are the top 5 slowest queries:

1. usp_GetIndexData (avg 45.2s)
   - Called 1,234 times
   - Total time: 15.5 hours
   - Recommendation: Add missing index on OrderDate

2. sp_SyncVendorData (avg 23.1s)
   ...

Would you like me to investigate any of these further?
```

### Example: Generating Complex SQL

```bash
$ eds-agent sql "Show monthly order totals by vendor for 2024, with running totals"

Agent: Here's the SQL query:

SELECT
    v.VendorName,
    FORMAT(o.OrderDate, 'yyyy-MM') as Month,
    SUM(od.ExtendedPrice) as MonthlyTotal,
    SUM(SUM(od.ExtendedPrice)) OVER (
        PARTITION BY v.VendorID
        ORDER BY FORMAT(o.OrderDate, 'yyyy-MM')
    ) as RunningTotal
FROM Vendors v
JOIN PurchaseOrders o ON v.VendorID = o.VendorID
JOIN PurchaseOrderDetails od ON o.OrderID = od.OrderID
WHERE YEAR(o.OrderDate) = 2024
GROUP BY v.VendorID, v.VendorName, FORMAT(o.OrderDate, 'yyyy-MM')
ORDER BY v.VendorName, Month

Execute this query? (y/n)
```

### Example: Documentation Search

```bash
$ eds-agent docs "trigger cascade effects"

Agent: Based on the documentation, here's information about trigger cascades:

From EDS_TRIGGERS.md:
---
The following triggers can cause cascade effects:

1. trig_DetailUpdate (on OrderDetails)
   - Updates OrderHeader totals
   - Can trigger trig_OrderTotal

2. trig_InventoryAdjust (on Inventory)
   - Updates stock levels
   - May trigger reorder notifications
---

Related documents:
- EDS_PROCEDURE_DEPENDENCIES.md
- EDS_BUSINESS_WORKFLOWS.md
```

---

## Troubleshooting

### "API key not found"

```bash
# Set the API key
export ANTHROPIC_API_KEY=your-key

# Or create .env file
echo "ANTHROPIC_API_KEY=your-key" > agent/.env
```

### "Database connection failed"

```bash
# Verify database settings in parent .env
cat .env | grep DB_

# Test connection
python test_db.py
```

### "RAG index not found"

```bash
# Build the RAG index
eds-agent index-docs

# This indexes documents from docs/ directory
```

### "Ollama connection refused"

```bash
# Ensure Ollama is running
ollama serve

# Check if model is available
ollama list
```

---

## Development

### Adding a New LLM Provider

1. Create provider file in `llm/`:
   ```python
   # llm/newprovider.py
   from agent.llm.base import BaseLLMProvider

   class NewProvider(BaseLLMProvider):
       def generate(self, messages, tools=None):
           # Implementation
           pass
   ```

2. Register in `llm/registry.py`

### Adding a New Tool

1. Create tool file in `tools/`:
   ```python
   # tools/newtool.py
   from agent.tools.base import BaseTool

   class NewTool(BaseTool):
       name = "new_tool"
       description = "Tool description for LLM"

       def execute(self, input_data):
           # Implementation
           return result
   ```

2. Register in `tools/registry.py`

### Running Tests

```bash
cd agent

# Run all tests
pytest

# Run with coverage
pytest --cov=agent

# Run specific test
pytest tests/test_security.py -v
```

---

## See Also

- [Configuration Reference](CONFIGURATION.md) - Configuration details
- [Scripts README](../scripts/README.md) - Available analysis scripts
- [API Reference](API_REFERENCE.md) - API documentation
- [Database Architecture](wiki/architecture/database-architecture.md) - Database details
