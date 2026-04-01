"""NiceGUI-based desktop application for the EDS DBA Agent.

Provides a web-based chat interface with SQL syntax highlighting,
documentation browser, session management, and settings panel.
"""

import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

APP_TITLE = "EDS DBA Agent"
DEFAULT_WINDOW_SIZE = (1400, 900)

# EDS brand colors
EDS_PRIMARY = "#1c1a83"
EDS_SECONDARY = "#4a4890"
EDS_ACCENT = "#b70c0d"


def create_app():
    """Create and configure the NiceGUI application."""
    from nicegui import app, ui

    from agent.core.agent import AgentMode, EDSAgent
    from agent.gui.state import Alert, AppState, Message

    state = AppState()
    agent = EDSAgent()

    # ── Shared CSS ───────────────────────────────────────────────
    ui.add_head_html(f"""
    <style>
        .chat-message {{ padding: 12px 16px; border-radius: 8px; margin: 4px 0; max-width: 85%; }}
        .user-msg {{ background: {EDS_PRIMARY}; color: white; margin-left: auto; }}
        .assistant-msg {{ background: #f0f0f0; color: #333; }}
        .mode-badge {{ padding: 2px 8px; border-radius: 4px; font-size: 0.8em; }}
        pre code {{ background: #1e1e1e; color: #d4d4d4; padding: 12px; border-radius: 6px;
                    display: block; overflow-x: auto; font-size: 0.9em; }}
    </style>
    """)

    # ── Main chat page ───────────────────────────────────────────
    @ui.page("/")
    def main_page():
        with ui.header().classes("bg-blue-900"):
            ui.label(APP_TITLE).classes("text-xl font-bold text-white")
            ui.space()
            mode_select = ui.select(
                ["chat", "sql", "docs", "analyze"],
                value=state.current_mode,
                label="Mode",
            ).classes("text-white").props("dark dense")
            provider_select = ui.select(
                ["claude", "openai", "ollama"],
                value=state.current_provider,
                label="Provider",
            ).classes("text-white").props("dark dense")

        with ui.left_drawer().classes("bg-gray-100") as drawer:
            ui.label("Sessions").classes("text-lg font-bold p-2")
            ui.button("New Session", on_click=lambda: _new_session()).props("flat dense")
            ui.separator()
            session_list = ui.column().classes("w-full")

        with ui.column().classes("w-full max-w-4xl mx-auto p-4 flex-grow"):
            chat_container = ui.column().classes("w-full flex-grow overflow-auto")
            _render_messages(chat_container)

            with ui.row().classes("w-full items-end"):
                user_input = ui.textarea(
                    placeholder="Type a message... (Ctrl+Enter to send)",
                ).classes("flex-grow").props("autogrow outlined dense rows=2")
                send_btn = ui.button("Send", on_click=lambda: _send_message(
                    user_input, chat_container, mode_select, provider_select,
                )).props(f"color=primary")

            # Keyboard shortcut: Ctrl+Enter to send
            user_input.on("keydown.ctrl.enter", lambda: _send_message(
                user_input, chat_container, mode_select, provider_select,
            ))

        with ui.footer().classes("bg-gray-50 text-gray-500 text-sm"):
            ui.label(f"EDS DBA Agent v0.1.0")
            ui.space()
            ui.label("").bind_text_from(state, "current_session_id",
                                         backward=lambda s: f"Session: {s or 'none'}")

    def _render_messages(container):
        container.clear()
        with container:
            for msg in state.messages:
                css = "user-msg" if msg.role == "user" else "assistant-msg"
                with ui.element("div").classes(f"chat-message {css}"):
                    if msg.role == "assistant":
                        ui.markdown(msg.content)
                    else:
                        ui.label(msg.content)

    async def _send_message(user_input, chat_container, mode_select, provider_select):
        text = user_input.value.strip()
        if not text or state.is_loading:
            return

        state.is_loading = True
        user_input.value = ""

        # Update mode/provider if changed
        state.current_mode = mode_select.value
        state.current_provider = provider_select.value

        try:
            agent.mode = AgentMode(state.current_mode)
            if agent._provider_name != state.current_provider:
                agent.set_provider(state.current_provider)
        except Exception as e:
            logger.warning("Provider switch failed: %s", e)

        state.messages.append(Message(role="user", content=text))
        _render_messages(chat_container)

        try:
            response = agent.chat(text, session_id=state.current_session_id)
            state.messages.append(Message(
                role="assistant",
                content=response.content or response.error or "No response",
                metadata=response.metadata,
            ))
        except Exception as e:
            state.messages.append(Message(
                role="assistant",
                content=f"Error: {e}",
            ))

        state.is_loading = False
        _render_messages(chat_container)

    def _new_session():
        session = agent.sessions.create_session(
            mode=state.current_mode,
            provider=state.current_provider,
        )
        state.current_session_id = session.id
        state.messages.clear()

    # ── Documentation search page ────────────────────────────────
    @ui.page("/docs")
    def docs_page():
        with ui.header().classes("bg-blue-900"):
            ui.link("← Back", "/").classes("text-white")
            ui.label("Documentation Search").classes("text-xl font-bold text-white")

        with ui.column().classes("w-full max-w-4xl mx-auto p-4"):
            search_input = ui.input("Search docs...").classes("w-full")
            results_container = ui.column().classes("w-full")

            async def _search():
                query = search_input.value.strip()
                if not query:
                    return
                response = agent.chat(query, mode=AgentMode.DOCS)
                results_container.clear()
                with results_container:
                    ui.markdown(response.content)

            search_input.on("keydown.enter", _search)

    # ── Settings page ────────────────────────────────────────────
    @ui.page("/settings")
    def settings_page():
        with ui.header().classes("bg-blue-900"):
            ui.link("← Back", "/").classes("text-white")
            ui.label("Settings").classes("text-xl font-bold text-white")

        with ui.column().classes("w-full max-w-2xl mx-auto p-4"):
            ui.label("LLM Provider").classes("text-lg font-bold")
            ui.select(
                ["claude", "openai", "ollama"],
                value=state.current_provider,
                on_change=lambda e: setattr(state, "current_provider", e.value),
            ).classes("w-full")

            ui.separator()
            ui.label("Agent Status").classes("text-lg font-bold")
            status = agent.get_status()
            for k, v in status.items():
                ui.label(f"{k}: {v}")

    # ── Status page ──────────────────────────────────────────────
    @ui.page("/status")
    def status_page():
        with ui.header().classes("bg-blue-900"):
            ui.link("← Back", "/").classes("text-white")
            ui.label("System Status").classes("text-xl font-bold text-white")

        with ui.column().classes("w-full max-w-2xl mx-auto p-4"):
            status = agent.get_status()
            for k, v in status.items():
                with ui.row().classes("w-full"):
                    ui.label(f"{k}:").classes("font-bold w-48")
                    ui.label(str(v))


def run_app(
    host: str = "127.0.0.1",
    port: int = 8080,
    native: bool = True,
) -> None:
    """Launch the GUI application."""
    from nicegui import ui

    create_app()

    if native:
        ui.run(
            title=APP_TITLE,
            host=host,
            port=port,
            native=True,
            window_size=DEFAULT_WINDOW_SIZE,
            reload=False,
        )
    else:
        ui.run(
            title=APP_TITLE,
            host=host,
            port=port,
            reload=False,
        )
