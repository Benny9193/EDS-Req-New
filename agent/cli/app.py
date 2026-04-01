"""Click-based CLI for the EDS DBA Agent."""

import click
import sys

from agent.core.agent import AgentMode


@click.group()
@click.version_option(version="0.1.0", prog_name="eds-agent")
def cli():
    """EDS DBA Agent - AI-powered database assistant."""
    pass


@cli.command()
@click.option("--provider", type=click.Choice(["claude", "openai", "ollama"]), default=None,
              help="LLM provider to use.")
@click.option("--mode", type=click.Choice(["chat", "sql", "docs", "analyze"]), default="chat",
              help="Initial agent mode.")
@click.option("--debug", is_flag=True, help="Enable debug output.")
def chat(provider, mode, debug):
    """Start an interactive chat session."""
    import logging
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.WARNING)

    from agent.cli.repl import start_repl
    start_repl(provider=provider, mode=AgentMode(mode), debug=debug)


@cli.command()
@click.argument("question")
@click.option("--provider", type=click.Choice(["claude", "openai", "ollama"]), default=None)
def ask(question, provider):
    """Ask a single question and get an answer."""
    import logging
    logging.basicConfig(level=logging.WARNING)

    from agent.core.agent import EDSAgent
    agent = EDSAgent()
    if provider:
        agent.set_provider(provider)

    response = agent.chat(question)
    if response.error:
        click.secho(f"Error: {response.error}", fg="red", err=True)
        sys.exit(1)
    click.echo(response.content)


@cli.command()
@click.argument("description")
@click.option("--provider", type=click.Choice(["claude", "openai", "ollama"]), default=None)
def sql(description, provider):
    """Generate SQL from a natural language description."""
    import logging
    logging.basicConfig(level=logging.WARNING)

    from agent.core.agent import EDSAgent
    agent = EDSAgent()
    if provider:
        agent.set_provider(provider)

    response = agent.chat(description, mode=AgentMode.SQL)
    if response.error:
        click.secho(f"Error: {response.error}", fg="red", err=True)
        sys.exit(1)
    click.echo(response.content)


@cli.command()
@click.argument("query")
@click.option("--provider", type=click.Choice(["claude", "openai", "ollama"]), default=None)
def docs(query, provider):
    """Search EDS documentation."""
    import logging
    logging.basicConfig(level=logging.WARNING)

    from agent.core.agent import EDSAgent
    agent = EDSAgent()
    if provider:
        agent.set_provider(provider)

    response = agent.chat(query, mode=AgentMode.DOCS)
    if response.error:
        click.secho(f"Error: {response.error}", fg="red", err=True)
        sys.exit(1)
    click.echo(response.content)


@cli.command()
def status():
    """Show agent status and configuration."""
    import logging
    logging.basicConfig(level=logging.WARNING)

    from agent.config import get_default_provider, get_llm_config

    provider_name = get_default_provider()
    provider_config = get_llm_config(provider_name)

    click.secho("EDS DBA Agent Status", fg="cyan", bold=True)
    click.secho("=" * 40, fg="cyan")
    click.echo(f"  Default provider: {provider_name}")
    click.echo(f"  Model: {provider_config.get('model', 'default')}")
    click.echo(f"  Version: 0.1.0")
    click.echo()

    # Check provider availability
    click.secho("Provider Availability:", fg="cyan", bold=True)
    for name, pkg in [("claude", "anthropic"), ("openai", "openai"), ("ollama", "ollama")]:
        try:
            __import__(pkg)
            marker = click.style("✓", fg="green")
        except ImportError:
            marker = click.style("✗", fg="red")
        active = " (active)" if name == provider_name else ""
        click.echo(f"  {marker} {name}{active}")


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
