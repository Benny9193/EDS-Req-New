"""Interactive REPL for the EDS DBA Agent."""

import sys
from typing import Optional

from agent.core.agent import AgentMode, EDSAgent


WELCOME = """
╔══════════════════════════════════════════════╗
║          EDS DBA Agent v0.1.0                ║
║  AI-powered database assistant               ║
╚══════════════════════════════════════════════╝

Commands:
  /sql      - Switch to SQL generation mode
  /docs     - Switch to documentation search mode
  /analyze  - Switch to analysis mode
  /chat     - Switch to general chat mode
  /clear    - Clear conversation history
  /status   - Show agent status
  /help     - Show this help
  /exit     - Exit the session

Type your question or command below.
"""

MODE_LABELS = {
    AgentMode.CHAT: "chat",
    AgentMode.SQL: "sql",
    AgentMode.DOCS: "docs",
    AgentMode.ANALYZE: "analyze",
}


def _get_prompt(mode: AgentMode) -> str:
    return f"[{MODE_LABELS[mode]}] > "


def _print_colored(text: str, color: str) -> None:
    """Print with ANSI color codes."""
    colors = {
        "cyan": "\033[96m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "red": "\033[91m",
        "reset": "\033[0m",
        "bold": "\033[1m",
        "dim": "\033[2m",
    }
    code = colors.get(color, "")
    reset = colors.get("reset", "")
    print(f"{code}{text}{reset}")


def _try_rich_print(text: str) -> None:
    """Try to use rich for markdown rendering, fall back to plain print."""
    try:
        from rich.console import Console
        from rich.markdown import Markdown
        console = Console()
        console.print(Markdown(text))
    except ImportError:
        print(text)


def start_repl(
    provider: Optional[str] = None,
    mode: AgentMode = AgentMode.CHAT,
    debug: bool = False,
) -> None:
    """Start the interactive REPL session."""
    agent = EDSAgent()
    agent.mode = mode

    if provider:
        try:
            agent.set_provider(provider)
        except Exception as e:
            _print_colored(f"Failed to set provider '{provider}': {e}", "red")
            _print_colored(f"Falling back to default provider.", "yellow")

    print(WELCOME)

    status = agent.get_status()
    _print_colored(
        f"Provider: {status['provider']} | Model: {status['model']} | Mode: {status['mode']}",
        "dim",
    )
    print()

    # Try to use prompt_toolkit for better input handling
    try:
        from prompt_toolkit import PromptSession
        from prompt_toolkit.history import FileHistory
        import os

        history_path = os.path.expanduser("~/.eds_agent_history")
        session = PromptSession(history=FileHistory(history_path))

        def get_input(prompt_str):
            return session.prompt(prompt_str)
    except ImportError:
        def get_input(prompt_str):
            return input(prompt_str)

    while True:
        try:
            prompt_str = _get_prompt(agent.mode)
            user_input = get_input(prompt_str).strip()

            if not user_input:
                continue

            # Handle commands
            if user_input.startswith("/"):
                cmd = user_input.lower().split()[0]

                if cmd in ("/exit", "/quit", "/q"):
                    _print_colored("Goodbye!", "cyan")
                    break

                elif cmd == "/help":
                    print(WELCOME)
                    continue

                elif cmd == "/clear":
                    agent.clear_history()
                    _print_colored("Conversation history cleared.", "green")
                    continue

                elif cmd == "/status":
                    s = agent.get_status()
                    _print_colored("Agent Status:", "cyan")
                    for k, v in s.items():
                        print(f"  {k}: {v}")
                    continue

                elif cmd == "/sql":
                    agent.mode = AgentMode.SQL
                    _print_colored("Switched to SQL generation mode.", "green")
                    continue

                elif cmd == "/docs":
                    agent.mode = AgentMode.DOCS
                    _print_colored("Switched to documentation search mode.", "green")
                    continue

                elif cmd == "/analyze":
                    agent.mode = AgentMode.ANALYZE
                    _print_colored("Switched to analysis mode.", "green")
                    continue

                elif cmd == "/chat":
                    agent.mode = AgentMode.CHAT
                    _print_colored("Switched to general chat mode.", "green")
                    continue

                elif cmd == "/provider":
                    parts = user_input.split()
                    if len(parts) < 2:
                        _print_colored("Usage: /provider <claude|openai|ollama>", "yellow")
                        continue
                    try:
                        agent.set_provider(parts[1])
                        _print_colored(f"Switched to {parts[1]} provider.", "green")
                    except Exception as e:
                        _print_colored(f"Failed to switch provider: {e}", "red")
                    continue

                else:
                    _print_colored(f"Unknown command: {cmd}. Type /help for commands.", "yellow")
                    continue

            # Send to agent
            _print_colored("Thinking...", "dim")

            try:
                # Try streaming first
                full_response = ""
                first_chunk = True
                for chunk in agent.chat_stream(user_input):
                    if first_chunk:
                        # Clear the "Thinking..." line
                        sys.stdout.write("\033[A\033[K")
                        first_chunk = False
                    sys.stdout.write(chunk)
                    sys.stdout.flush()
                    full_response += chunk

                if first_chunk:
                    # No chunks received, clear "Thinking..."
                    sys.stdout.write("\033[A\033[K")

                print()  # newline after response
                print()  # blank line for readability

            except (NotImplementedError, Exception) as e:
                # Fall back to non-streaming
                sys.stdout.write("\033[A\033[K")  # Clear "Thinking..."
                response = agent.chat(user_input)
                if response.error:
                    _print_colored(f"Error: {response.error}", "red")
                else:
                    _try_rich_print(response.content)
                print()

        except KeyboardInterrupt:
            print()
            _print_colored("(Use /exit to quit)", "dim")
            continue

        except EOFError:
            _print_colored("\nGoodbye!", "cyan")
            break
