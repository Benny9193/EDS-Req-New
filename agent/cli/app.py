"""Click-based CLI for the EDS DBA Agent."""

import click
import sys

from agent.core.agent import AgentMode

_PROVIDER_CHOICE = click.Choice(["claude", "openai", "ollama"])
_MODE_CHOICE = click.Choice(["chat", "sql", "docs", "analyze"])


def _setup_logging(debug: bool = False):
    import logging
    logging.basicConfig(level=logging.DEBUG if debug else logging.WARNING)


def _create_agent(provider=None, session_id=None):
    """Create an agent with optional provider and session."""
    from agent.core.agent import EDSAgent
    agent = EDSAgent()
    if provider:
        agent.set_provider(provider)
    return agent


@click.group()
@click.version_option(version="0.1.0", prog_name="eds-agent")
def cli():
    """EDS DBA Agent - AI-powered database assistant."""
    pass


# ── chat ─────────────────────────────────────────────────────────────


@cli.command()
@click.option("--provider", type=_PROVIDER_CHOICE, default=None, help="LLM provider to use.")
@click.option("--model", type=str, default=None, help="Model name override.")
@click.option("--mode", type=_MODE_CHOICE, default="chat", help="Initial agent mode.")
@click.option("--session", "session_id", type=str, default=None, help="Resume an existing session by ID.")
@click.option("--debug", is_flag=True, help="Enable debug output.")
def chat(provider, model, mode, session_id, debug):
    """Start an interactive chat session."""
    _setup_logging(debug)
    from agent.cli.repl import start_repl
    start_repl(
        provider=provider, model=model,
        mode=AgentMode(mode), session_id=session_id, debug=debug,
    )


# ── ask ──────────────────────────────────────────────────────────────


@cli.command()
@click.argument("question")
@click.option("--provider", type=_PROVIDER_CHOICE, default=None)
@click.option("--session", "session_id", type=str, default=None, help="Session ID for context.")
@click.option("--mode", type=_MODE_CHOICE, default="chat")
def ask(question, provider, session_id, mode):
    """Ask a single question and get an answer."""
    _setup_logging()
    agent = _create_agent(provider)

    response = agent.chat(question, session_id=session_id, mode=AgentMode(mode))
    if response.error:
        click.secho(f"Error: {response.error}", fg="red", err=True)
        sys.exit(1)
    click.echo(response.content)


# ── sql ──────────────────────────────────────────────────────────────


@cli.command()
@click.argument("description")
@click.option("--provider", type=_PROVIDER_CHOICE, default=None)
@click.option("--session", "session_id", type=str, default=None)
def sql(description, provider, session_id):
    """Generate SQL from a natural language description."""
    _setup_logging()
    agent = _create_agent(provider)

    response = agent.chat(description, session_id=session_id, mode=AgentMode.SQL)
    if response.error:
        click.secho(f"Error: {response.error}", fg="red", err=True)
        sys.exit(1)
    click.echo(response.content)


# ── docs ─────────────────────────────────────────────────────────────


@cli.command()
@click.argument("query")
@click.option("--provider", type=_PROVIDER_CHOICE, default=None)
def docs(query, provider):
    """Search EDS documentation."""
    _setup_logging()
    agent = _create_agent(provider)

    response = agent.chat(query, mode=AgentMode.DOCS)
    if response.error:
        click.secho(f"Error: {response.error}", fg="red", err=True)
        sys.exit(1)
    click.echo(response.content)


# ── run ──────────────────────────────────────────────────────────────


@cli.command()
@click.argument("script_name")
@click.option("--args", "script_args", type=str, default="", help="Arguments to pass to the script.")
def run(script_name, script_args):
    """Execute an analysis script."""
    _setup_logging()
    from agent.tools.script_runner import ScriptRunnerTool
    from agent.config import load_config

    config = load_config()
    scripts_dir = config.get("tools", {}).get("scripts_dir", "scripts")
    tool = ScriptRunnerTool(scripts_dir=scripts_dir)

    result = tool.execute(script_name=script_name, args=script_args)
    if result.success:
        click.echo(result.data)
    else:
        click.secho(f"Error: {result.error}", fg="red", err=True)
        sys.exit(1)


# ── report ───────────────────────────────────────────────────────────


@cli.command()
@click.argument("description")
@click.option("--provider", type=_PROVIDER_CHOICE, default=None)
@click.option("--preview", is_flag=True, help="Preview the report plan without executing.")
def report(description, provider, preview):
    """Generate an Excel report from a natural language description."""
    _setup_logging()
    import json
    from agent.tools.report_generator import ReportGeneratorTool
    from agent.config import load_config, get_default_provider

    config = load_config()
    provider_name = provider or get_default_provider()

    tool = ReportGeneratorTool(provider_name=provider_name)
    result = tool.execute(description=description, preview_only=preview)

    if result.success:
        if preview:
            click.secho("Report Plan Preview:", fg="cyan", bold=True)
            click.echo(json.dumps(result.data, indent=2))
        else:
            data = result.data
            click.secho("Report Generated:", fg="green", bold=True)
            click.echo(f"  File: {data.get('file_path')}")
            click.echo(f"  Sheets: {data.get('sheets_written')}")
            click.echo(f"  Rows: {data.get('total_rows')}")
            click.echo(f"  Time: {data.get('elapsed_seconds')}s")
    else:
        click.secho(f"Error: {result.error}", fg="red", err=True)
        sys.exit(1)


# ── sessions ─────────────────────────────────────────────────────────


@cli.command()
@click.option("--limit", type=int, default=20, help="Maximum sessions to list.")
@click.option("--delete", "delete_id", type=str, default=None, help="Delete a session by ID.")
def sessions(limit, delete_id):
    """List or manage chat sessions."""
    _setup_logging()
    from agent.memory.session import SessionManager

    mgr = SessionManager()

    if delete_id:
        if mgr.delete_session(delete_id):
            click.secho(f"Deleted session {delete_id}", fg="green")
        else:
            click.secho(f"Session {delete_id} not found", fg="red")
        return

    session_list = mgr.list_sessions(limit=limit)
    if not session_list:
        click.echo("No sessions found.")
        return

    click.secho(f"Sessions ({len(session_list)}):", fg="cyan", bold=True)
    for s in session_list:
        msg_count = len(s.messages)
        click.echo(
            f"  {s.id}  {s.mode:<8} {s.provider:<8} "
            f"{msg_count:>3} msgs  {s.updated_at[:19]}"
        )


# ── status ───────────────────────────────────────────────────────────


@cli.command()
def status():
    """Show agent status and configuration."""
    _setup_logging()
    from agent.config import get_default_provider, get_llm_config
    from agent.tools.registry import register_all_tools

    provider_name = get_default_provider()
    provider_config = get_llm_config(provider_name)

    click.secho("EDS DBA Agent Status", fg="cyan", bold=True)
    click.secho("=" * 40, fg="cyan")
    click.echo(f"  Default provider: {provider_name}")
    click.echo(f"  Model: {provider_config.get('model', 'default')}")
    click.echo(f"  Version: 0.1.0")
    click.echo()

    # Provider availability
    click.secho("Provider Availability:", fg="cyan", bold=True)
    for name, pkg in [("claude", "anthropic"), ("openai", "openai"), ("ollama", "ollama")]:
        try:
            __import__(pkg)
            marker = click.style("✓", fg="green")
        except ImportError:
            marker = click.style("✗", fg="red")
        active = " (active)" if name == provider_name else ""
        click.echo(f"  {marker} {name}{active}")

    # Tools
    click.echo()
    click.secho("Registered Tools:", fg="cyan", bold=True)
    try:
        registry = register_all_tools()
        for name in registry:
            click.echo(f"  - {name}")
        click.echo(f"  Total: {registry.tool_count}")
    except Exception:
        click.echo("  (tools not loaded)")


# ── index-docs ───────────────────────────────────────────────────────


@cli.command("index-docs")
@click.option("--rebuild", is_flag=True, help="Drop and rebuild the entire index.")
@click.option("--file", "specific_file", type=str, default=None, help="Index a specific file.")
def index_docs(rebuild, specific_file):
    """Build or rebuild the RAG documentation index."""
    import logging
    logging.basicConfig(level=logging.INFO)

    from agent.config import load_config
    from agent.rag.indexer import index_all

    config = load_config()
    stats = index_all(config, rebuild=rebuild, specific_file=specific_file)

    click.secho("Indexing Complete", fg="cyan", bold=True)
    click.echo(f"  Files processed: {stats['files_processed']}")
    click.echo(f"  Chunks created:  {stats['chunks_created']}")
    click.echo(f"  Chunks indexed:  {stats['chunks_indexed']}")
    if stats["errors"]:
        click.secho(f"  Errors: {len(stats['errors'])}", fg="red")
        for err in stats["errors"]:
            click.echo(f"    - {err}")
