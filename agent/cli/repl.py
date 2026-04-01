"""Interactive REPL for the EDS DBA Agent."""

import sys
from typing import Optional

from agent.core.agent import AgentMode, EDSAgent


WELCOME = """
╔══════════════════════════════════════════════════╗
║            EDS DBA Agent v0.1.0                  ║
║    AI-powered database assistant                 ║
╚══════════════════════════════════════════════════╝

Commands:
  /sql        Switch to SQL generation mode
  /docs       Switch to documentation search mode
  /analyze    Switch to analysis mode
  /chat       Switch to general chat mode
  /clear      Clear conversation history
  /new        Start a new session
  /sessions   List recent sessions
  /load ID    Resume a session by ID
  /history N  Show last N messages (default 10)
  /provider X Switch provider (claude|openai|ollama)
  /status     Show agent status
  /help       Show this help
  /exit       Exit the session

Type your question or command below.
"""

MODE_LABELS = {
    AgentMode.CHAT: "chat",
    AgentMode.SQL: "sql",
    AgentMode.DOCS: "docs",
    AgentMode.ANALYZE: "analyze",
}


def _get_prompt(mode: AgentMode, session_id: Optional[str] = None) -> str:
    sid = session_id[:6] if session_id else "no-session"
    return f"[{MODE_LABELS[mode]}:{sid}] > "


def _print_colored(text: str, color: str) -> None:
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
    try:
        from rich.console import Console
        from rich.markdown import Markdown
        console = Console()
        console.print(Markdown(text))
    except ImportError:
        print(text)


def start_repl(
    provider: Optional[str] = None,
    model: Optional[str] = None,
    mode: AgentMode = AgentMode.CHAT,
    session_id: Optional[str] = None,
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
            _print_colored("Falling back to default provider.", "yellow")

    # Resume or create a session
    if session_id:
        existing = agent.sessions.get_session(session_id)
        if existing:
            _print_colored(f"Resumed session {session_id} ({len(existing.messages)} messages)", "green")
        else:
            _print_colored(f"Session {session_id} not found, creating new.", "yellow")
            session_id = None

    if not session_id:
        provider_name = agent._provider_name or "ollama"
        session = agent.sessions.create_session(
            mode=mode.value, provider=provider_name,
        )
        session_id = session.id

    print(WELCOME)

    status = agent.get_status()
    _print_colored(
        f"Provider: {status['provider']} | Model: {status['model']} "
        f"| Mode: {status['mode']} | Session: {session_id}",
        "dim",
    )
    print()

    # Try to use prompt_toolkit for better input handling
    try:
        from prompt_toolkit import PromptSession
        from prompt_toolkit.history import FileHistory
        import os

        history_path = os.path.expanduser("~/.eds_agent_history")
        pt_session = PromptSession(history=FileHistory(history_path))

        def get_input(prompt_str):
            return pt_session.prompt(prompt_str)
    except ImportError:
        def get_input(prompt_str):
            return input(prompt_str)

    while True:
        try:
            prompt_str = _get_prompt(agent.mode, session_id)
            user_input = get_input(prompt_str).strip()

            if not user_input:
                continue

            # Handle commands
            if user_input.startswith("/"):
                cmd = user_input.lower().split()[0]
                parts = user_input.split()

                if cmd in ("/exit", "/quit", "/q"):
                    _print_colored("Goodbye!", "cyan")
                    break

                elif cmd == "/help":
                    print(WELCOME)

                elif cmd == "/clear":
                    agent.clear_history()
                    # Create a fresh session
                    session = agent.sessions.create_session(
                        mode=agent.mode.value,
                        provider=agent._provider_name or "ollama",
                    )
                    session_id = session.id
                    _print_colored(f"History cleared. New session: {session_id}", "green")

                elif cmd == "/new":
                    session = agent.sessions.create_session(
                        mode=agent.mode.value,
                        provider=agent._provider_name or "ollama",
                    )
                    session_id = session.id
                    agent.clear_history()
                    _print_colored(f"New session: {session_id}", "green")

                elif cmd == "/sessions":
                    sessions_list = agent.sessions.list_sessions(limit=10)
                    if not sessions_list:
                        _print_colored("No sessions found.", "dim")
                    else:
                        _print_colored("Recent sessions:", "cyan")
                        for s in sessions_list:
                            marker = " *" if s.id == session_id else ""
                            print(f"  {s.id}  {s.mode:<8} {len(s.messages):>3} msgs  "
                                  f"{s.updated_at[:19]}{marker}")

                elif cmd == "/load":
                    if len(parts) < 2:
                        _print_colored("Usage: /load <session-id>", "yellow")
                    else:
                        target_id = parts[1]
                        existing = agent.sessions.get_session(target_id)
                        if existing:
                            session_id = target_id
                            agent.clear_history()
                            _print_colored(
                                f"Loaded session {target_id} ({len(existing.messages)} messages)",
                                "green",
                            )
                        else:
                            _print_colored(f"Session {target_id} not found.", "red")

                elif cmd == "/history":
                    n = 10
                    if len(parts) > 1 and parts[1].isdigit():
                        n = int(parts[1])
                    recent = agent.sessions.get_recent_context(session_id, n_messages=n)
                    if not recent:
                        _print_colored("No messages in this session.", "dim")
                    else:
                        _print_colored(f"Last {len(recent)} messages:", "cyan")
                        for msg in recent:
                            role = msg.role.upper()
                            content = msg.content[:120]
                            if len(msg.content) > 120:
                                content += "..."
                            _print_colored(f"  [{role}] {content}", "dim")

                elif cmd == "/status":
                    s = agent.get_status()
                    _print_colored("Agent Status:", "cyan")
                    for k, v in s.items():
                        if isinstance(v, dict):
                            print(f"  {k}:")
                            for sk, sv in v.items():
                                print(f"    {sk}: {sv}")
                        elif isinstance(v, list):
                            print(f"  {k}: {', '.join(str(x) for x in v)}")
                        else:
                            print(f"  {k}: {v}")
                    print(f"  session: {session_id}")

                elif cmd == "/sql":
                    agent.mode = AgentMode.SQL
                    _print_colored("Switched to SQL generation mode.", "green")

                elif cmd == "/docs":
                    agent.mode = AgentMode.DOCS
                    _print_colored("Switched to documentation search mode.", "green")

                elif cmd == "/analyze":
                    agent.mode = AgentMode.ANALYZE
                    _print_colored("Switched to analysis mode.", "green")

                elif cmd == "/chat":
                    agent.mode = AgentMode.CHAT
                    _print_colored("Switched to general chat mode.", "green")

                elif cmd == "/provider":
                    if len(parts) < 2:
                        _print_colored("Usage: /provider <claude|openai|ollama>", "yellow")
                    else:
                        try:
                            agent.set_provider(parts[1])
                            _print_colored(f"Switched to {parts[1]} provider.", "green")
                        except Exception as e:
                            _print_colored(f"Failed to switch provider: {e}", "red")

                else:
                    _print_colored(f"Unknown command: {cmd}. Type /help for commands.", "yellow")

                continue

            # Send to agent
            _print_colored("Thinking...", "dim")

            try:
                # Try streaming first
                full_response = ""
                first_chunk = True
                for chunk in agent.chat_stream(user_input, session_id=session_id):
                    if first_chunk:
                        sys.stdout.write("\033[A\033[K")
                        first_chunk = False
                    sys.stdout.write(chunk)
                    sys.stdout.flush()
                    full_response += chunk

                if first_chunk:
                    sys.stdout.write("\033[A\033[K")

                print()
                print()

            except (NotImplementedError, Exception):
                # Fall back to non-streaming
                sys.stdout.write("\033[A\033[K")
                response = agent.chat(user_input, session_id=session_id)
                if response.error:
                    _print_colored(f"Error: {response.error}", "red")
                else:
                    _try_rich_print(response.content)

                    # Show tool calls if any
                    if response.tool_calls:
                        _print_colored(
                            f"  [{len(response.tool_calls)} tool call(s)]", "dim",
                        )
                print()

        except KeyboardInterrupt:
            print()
            _print_colored("(Use /exit to quit)", "dim")
            continue

        except EOFError:
            _print_colored("\nGoodbye!", "cyan")
            break
