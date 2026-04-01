"""Interactive REPL for the EDS DBA Agent."""

import sys
from dataclasses import dataclass, field
from typing import List, Optional

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


@dataclass
class CommandResult:
    """Result of processing a REPL slash command."""

    action: str  # "continue", "exit", "error", "info"
    message: str = ""
    new_session_id: Optional[str] = None
    output_lines: List[str] = field(default_factory=list)


def handle_command(
    user_input: str,
    agent: EDSAgent,
    session_id: str,
) -> CommandResult:
    """Process a slash command and return a result.

    This is extracted from the REPL loop so it can be tested independently.
    """
    cmd = user_input.lower().split()[0]
    parts = user_input.split()

    if cmd in ("/exit", "/quit", "/q"):
        return CommandResult(action="exit", message="Goodbye!")

    elif cmd == "/help":
        return CommandResult(action="info", message=WELCOME)

    elif cmd == "/clear":
        agent.clear_history()
        session = agent.sessions.create_session(
            mode=agent.mode.value,
            provider=agent._provider_name or "ollama",
        )
        return CommandResult(
            action="continue",
            message=f"History cleared. New session: {session.id}",
            new_session_id=session.id,
        )

    elif cmd == "/new":
        session = agent.sessions.create_session(
            mode=agent.mode.value,
            provider=agent._provider_name or "ollama",
        )
        agent.clear_history()
        return CommandResult(
            action="continue",
            message=f"New session: {session.id}",
            new_session_id=session.id,
        )

    elif cmd == "/sessions":
        sessions_list = agent.sessions.list_sessions(limit=10)
        if not sessions_list:
            return CommandResult(action="info", message="No sessions found.")
        lines = []
        for s in sessions_list:
            marker = " *" if s.id == session_id else ""
            lines.append(
                f"  {s.id}  {s.mode:<8} {len(s.messages):>3} msgs  "
                f"{s.updated_at[:19]}{marker}"
            )
        return CommandResult(action="info", message="Recent sessions:", output_lines=lines)

    elif cmd == "/load":
        if len(parts) < 2:
            return CommandResult(action="error", message="Usage: /load <session-id>")
        target_id = parts[1]
        existing = agent.sessions.get_session(target_id)
        if existing:
            agent.clear_history()
            return CommandResult(
                action="continue",
                message=f"Loaded session {target_id} ({len(existing.messages)} messages)",
                new_session_id=target_id,
            )
        else:
            return CommandResult(action="error", message=f"Session {target_id} not found.")

    elif cmd == "/history":
        n = 10
        if len(parts) > 1 and parts[1].isdigit():
            n = int(parts[1])
        recent = agent.sessions.get_recent_context(session_id, n_messages=n)
        if not recent:
            return CommandResult(action="info", message="No messages in this session.")
        lines = []
        for msg in recent:
            role = msg.role.upper()
            content = msg.content[:120]
            if len(msg.content) > 120:
                content += "..."
            lines.append(f"  [{role}] {content}")
        return CommandResult(
            action="info",
            message=f"Last {len(recent)} messages:",
            output_lines=lines,
        )

    elif cmd == "/status":
        s = agent.get_status()
        lines = []
        for k, v in s.items():
            if isinstance(v, dict):
                lines.append(f"  {k}:")
                for sk, sv in v.items():
                    lines.append(f"    {sk}: {sv}")
            elif isinstance(v, list):
                lines.append(f"  {k}: {', '.join(str(x) for x in v)}")
            else:
                lines.append(f"  {k}: {v}")
        lines.append(f"  session: {session_id}")
        return CommandResult(action="info", message="Agent Status:", output_lines=lines)

    elif cmd == "/sql":
        agent.mode = AgentMode.SQL
        return CommandResult(action="continue", message="Switched to SQL generation mode.")

    elif cmd == "/docs":
        agent.mode = AgentMode.DOCS
        return CommandResult(action="continue", message="Switched to documentation search mode.")

    elif cmd == "/analyze":
        agent.mode = AgentMode.ANALYZE
        return CommandResult(action="continue", message="Switched to analysis mode.")

    elif cmd == "/chat":
        agent.mode = AgentMode.CHAT
        return CommandResult(action="continue", message="Switched to general chat mode.")

    elif cmd == "/provider":
        if len(parts) < 2:
            return CommandResult(action="error", message="Usage: /provider <claude|openai|ollama>")
        try:
            agent.set_provider(parts[1])
            return CommandResult(action="continue", message=f"Switched to {parts[1]} provider.")
        except Exception as e:
            return CommandResult(action="error", message=f"Failed to switch provider: {e}")

    else:
        return CommandResult(action="error", message=f"Unknown command: {cmd}. Type /help for commands.")


def _get_prompt(mode: AgentMode, session_id: Optional[str] = None) -> str:
    sid = session_id[:6] if session_id else "no-session"
    return f"[{MODE_LABELS[mode]}:{sid}] > "


def _print_colored(text: str, color: str) -> None:
    colors = {
        "cyan": "\033[96m", "green": "\033[92m", "yellow": "\033[93m",
        "red": "\033[91m", "reset": "\033[0m", "bold": "\033[1m", "dim": "\033[2m",
    }
    code = colors.get(color, "")
    reset = colors.get("reset", "")
    print(f"{code}{text}{reset}")


def _try_rich_print(text: str) -> None:
    try:
        from rich.console import Console
        from rich.markdown import Markdown
        Console().print(Markdown(text))
    except ImportError:
        print(text)


def _print_command_result(result: CommandResult) -> None:
    """Print a CommandResult with appropriate coloring."""
    color_map = {"continue": "green", "info": "cyan", "error": "red", "exit": "cyan"}
    color = color_map.get(result.action, "dim")

    if result.message:
        _print_colored(result.message, color)
    for line in result.output_lines:
        print(line)


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
        session = agent.sessions.create_session(mode=mode.value, provider=provider_name)
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
        get_input = lambda prompt_str: pt_session.prompt(prompt_str)
    except ImportError:
        get_input = input

    while True:
        try:
            prompt_str = _get_prompt(agent.mode, session_id)
            user_input = get_input(prompt_str).strip()

            if not user_input:
                continue

            # Handle slash commands
            if user_input.startswith("/"):
                result = handle_command(user_input, agent, session_id)
                _print_command_result(result)

                if result.new_session_id:
                    session_id = result.new_session_id

                if result.action == "exit":
                    break
                continue

            # Send to agent
            _print_colored("Thinking...", "dim")

            try:
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
                sys.stdout.write("\033[A\033[K")
                response = agent.chat(user_input, session_id=session_id)
                if response.error:
                    _print_colored(f"Error: {response.error}", "red")
                else:
                    _try_rich_print(response.content)
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
