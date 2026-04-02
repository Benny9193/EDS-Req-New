"""NiceGUI-based desktop application for the EDS DBA Agent.

Provides a web-based chat interface with streaming responses, tool call
display, SQL syntax highlighting, session management, and settings.
"""

import asyncio
import logging
from datetime import datetime
from typing import Optional

logger = logging.getLogger(__name__)

APP_TITLE = "EDS DBA Agent"
DEFAULT_WINDOW_SIZE = (1400, 900)

EDS_PRIMARY = "#1c1a83"
EDS_SECONDARY = "#4a4890"
EDS_ACCENT = "#b70c0d"


def create_app():
    """Create and configure the NiceGUI application."""
    from nicegui import app, ui

    from agent.core.agent import AgentMode, EDSAgent
    from agent.gui.state import AppState, Message

    state = AppState()
    agent = EDSAgent()

    ui.add_head_html(f"""
    <style>
        .chat-message {{ padding: 12px 16px; border-radius: 8px; margin: 6px 0;
                          max-width: 85%; word-wrap: break-word; }}
        .user-msg {{ background: {EDS_PRIMARY}; color: white; margin-left: auto; }}
        .assistant-msg {{ background: #f0f0f5; color: #333; }}
        .tool-call-card {{ background: #f8f8ff; border-left: 3px solid {EDS_SECONDARY};
                           padding: 8px 12px; margin: 4px 0; font-size: 0.85em;
                           border-radius: 4px; }}
        .tool-name {{ color: {EDS_SECONDARY}; font-weight: bold; }}
        .tool-success {{ color: #1E7E34; }}
        .tool-error {{ color: {EDS_ACCENT}; }}
        .streaming-cursor {{ display: inline-block; animation: blink 1s infinite; }}
        @keyframes blink {{ 0%,50% {{ opacity: 1; }} 51%,100% {{ opacity: 0; }} }}
        pre code {{ background: #1e1e1e; color: #d4d4d4; padding: 12px; border-radius: 6px;
                    display: block; overflow-x: auto; font-size: 0.9em; }}
        .session-item {{ cursor: pointer; padding: 8px; border-radius: 4px; }}
        .session-item:hover {{ background: #e8e7f4; }}
        .session-active {{ background: #e8e7f4; border-left: 3px solid {EDS_PRIMARY}; }}
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
                value=state.current_mode, label="Mode",
            ).classes("text-white").props("dark dense")
            provider_select = ui.select(
                ["claude", "openai", "ollama"],
                value=state.current_provider, label="Provider",
            ).classes("text-white").props("dark dense")
            ui.link("Docs", "/docs").classes("text-white ml-4")
            ui.link("Settings", "/settings").classes("text-white ml-2")

        # Left drawer: sessions
        with ui.left_drawer().classes("bg-gray-50"):
            ui.label("Sessions").classes("text-lg font-bold p-2")
            ui.button("+ New Session", on_click=lambda: _new_session(
                chat_container, session_drawer,
            )).props("flat dense color=primary").classes("w-full")
            ui.separator()
            session_drawer = ui.column().classes("w-full")
            _render_session_list(session_drawer, chat_container)

        with ui.column().classes("w-full max-w-4xl mx-auto p-4 flex-grow"):
            chat_container = ui.scroll_area().classes("w-full flex-grow").style("height: 65vh")
            _render_messages(chat_container)

            # Loading indicator
            loading_row = ui.row().classes("w-full justify-center")
            loading_spinner = ui.spinner("dots", size="lg", color="primary")
            loading_spinner.visible = False

            with ui.row().classes("w-full items-end gap-2"):
                user_input = ui.textarea(
                    placeholder="Type a message... (Ctrl+Enter to send)",
                ).classes("flex-grow").props("autogrow outlined dense rows=2")
                send_btn = ui.button("Send", on_click=lambda: _send_message(
                    user_input, chat_container, mode_select, provider_select,
                    loading_spinner, send_btn,
                )).props("color=primary icon=send")

            user_input.on("keydown.ctrl.enter", lambda: _send_message(
                user_input, chat_container, mode_select, provider_select,
                loading_spinner, send_btn,
            ))

        with ui.footer().classes("bg-gray-50 text-gray-500 text-xs py-1"):
            ui.label("EDS DBA Agent v0.1.0")
            ui.space()
            ui.label("").bind_text_from(
                state, "current_session_id",
                backward=lambda s: f"Session: {s or 'none'}",
            )

    def _render_messages(container):
        container.clear()
        with container:
            for msg in state.messages:
                _render_single_message(msg)

    def _render_single_message(msg: Message):
        if msg.role == "user":
            with ui.element("div").classes("chat-message user-msg"):
                ui.label(msg.content)
        elif msg.role == "tool_calls":
            # Render tool call results
            for tc in msg.metadata.get("tool_calls", []):
                css_class = "tool-success" if tc.get("success") else "tool-error"
                with ui.element("div").classes("tool-call-card"):
                    ui.html(
                        f'<span class="tool-name">{tc.get("tool_name", "?")}</span> '
                        f'<span class="{css_class}">{"OK" if tc.get("success") else "FAILED"}</span>'
                    )
                    content = tc.get("content", "")
                    if len(content) > 300:
                        content = content[:300] + "..."
                    ui.code(content).classes("text-xs")
        else:
            with ui.element("div").classes("chat-message assistant-msg"):
                ui.markdown(msg.content)

    async def _send_message(
        user_input, chat_container, mode_select, provider_select,
        loading_spinner, send_btn,
    ):
        text = user_input.value.strip()
        if not text or state.is_loading:
            return

        state.is_loading = True
        loading_spinner.visible = True
        send_btn.disable()
        user_input.value = ""

        state.current_mode = mode_select.value
        state.current_provider = provider_select.value

        try:
            agent.mode = AgentMode(state.current_mode)
            if agent._provider_name != state.current_provider:
                agent.set_provider(state.current_provider)
        except Exception as e:
            logger.warning("Provider switch failed: %s", e)

        # Ensure session exists
        if not state.current_session_id:
            _create_session_internal()

        # Add user message
        state.messages.append(Message(role="user", content=text))
        _render_messages(chat_container)

        try:
            # Try streaming for a responsive feel
            streaming_el = None
            streamed_text = ""

            def _stream_gen():
                return agent.chat_stream(text, session_id=state.current_session_id)

            try:
                gen = await asyncio.to_thread(lambda: list(_stream_gen()))
                streamed_text = "".join(gen)

                if streamed_text:
                    state.messages.append(Message(
                        role="assistant", content=streamed_text,
                    ))
                else:
                    raise ValueError("Empty stream")

            except Exception:
                # Fall back to non-streaming (supports tool calls)
                response = await asyncio.to_thread(
                    agent.chat, text, session_id=state.current_session_id,
                )

                if response.tool_calls:
                    state.messages.append(Message(
                        role="tool_calls",
                        content=f"{len(response.tool_calls)} tool(s) called",
                        metadata={"tool_calls": response.tool_calls},
                    ))

                content = response.content or response.error or "No response"
                state.messages.append(Message(
                    role="assistant", content=content,
                    metadata=response.metadata,
                ))

        except Exception as e:
            state.messages.append(Message(role="assistant", content=f"Error: {e}"))

        state.is_loading = False
        loading_spinner.visible = False
        send_btn.enable()
        _render_messages(chat_container)

    def _create_session_internal():
        session = agent.sessions.create_session(
            mode=state.current_mode,
            provider=state.current_provider,
        )
        state.current_session_id = session.id

    def _new_session(chat_container=None, session_drawer=None):
        _create_session_internal()
        state.messages.clear()
        if chat_container:
            _render_messages(chat_container)
        if session_drawer:
            _render_session_list(session_drawer, chat_container)

    def _render_session_list(drawer, chat_container=None):
        drawer.clear()
        sessions = agent.sessions.list_sessions(limit=15)
        with drawer:
            for s in sessions:
                active = "session-active" if s.id == state.current_session_id else ""
                with ui.element("div").classes(f"session-item {active}").on(
                    "click", lambda _, sid=s.id: _load_session(sid, chat_container, drawer),
                ):
                    ui.label(f"{s.id[:8]}").classes("font-mono text-sm font-bold")
                    ui.label(
                        f"{s.mode} | {len(s.messages)} msgs"
                    ).classes("text-xs text-gray-500")

    def _load_session(session_id, chat_container=None, session_drawer=None):
        session = agent.sessions.get_session(session_id)
        if session:
            state.current_session_id = session_id
            state.messages.clear()
            for msg in session.messages:
                state.messages.append(Message(role=msg.role, content=msg.content))
            if chat_container:
                _render_messages(chat_container)
            if session_drawer:
                _render_session_list(session_drawer, chat_container)

    # ── Documentation search page ────────────────────────────────
    @ui.page("/docs")
    def docs_page():
        with ui.header().classes("bg-blue-900"):
            ui.link("< Chat", "/").classes("text-white")
            ui.label("Documentation Search").classes("text-xl font-bold text-white")

        with ui.column().classes("w-full max-w-4xl mx-auto p-4"):
            with ui.row().classes("w-full items-center gap-2"):
                search_input = ui.input("Search docs...").classes("flex-grow")
                search_btn = ui.button("Search", on_click=lambda: _do_search(
                    search_input, results_container,
                )).props("color=primary")
            results_container = ui.column().classes("w-full mt-4")

            search_input.on("keydown.enter", lambda: _do_search(
                search_input, results_container,
            ))

    async def _do_search(search_input, results_container):
        query = search_input.value.strip()
        if not query:
            return
        response = await asyncio.to_thread(
            agent.chat, query, mode=AgentMode.DOCS,
        )
        results_container.clear()
        with results_container:
            if response.tool_calls:
                for tc in response.tool_calls:
                    if tc.get("success"):
                        ui.label(
                            f"Found in: {', '.join(tc.get('metadata', {}).get('sources', []))}"
                        ).classes("text-sm text-gray-500")
            ui.markdown(response.content or response.error or "No results")

    # ── Settings page ────────────────────────────────────────────
    @ui.page("/settings")
    def settings_page():
        with ui.header().classes("bg-blue-900"):
            ui.link("< Chat", "/").classes("text-white")
            ui.label("Settings").classes("text-xl font-bold text-white")

        with ui.column().classes("w-full max-w-2xl mx-auto p-4 gap-4"):
            ui.label("LLM Provider").classes("text-lg font-bold")
            ui.select(
                ["claude", "openai", "ollama"],
                value=state.current_provider,
                on_change=lambda e: setattr(state, "current_provider", e.value),
            ).classes("w-full")

            ui.separator()
            ui.label("Agent Status").classes("text-lg font-bold")
            status = agent.get_status()
            with ui.grid(columns=2).classes("w-full gap-2"):
                for k, v in status.items():
                    if isinstance(v, dict):
                        ui.label(k).classes("font-bold")
                        ui.label(", ".join(f"{sk}={sv}" for sk, sv in v.items()))
                    elif isinstance(v, list):
                        ui.label(k).classes("font-bold")
                        ui.label(", ".join(str(x) for x in v))
                    else:
                        ui.label(k).classes("font-bold")
                        ui.label(str(v))

    # ── Status page ──────────────────────────────────────────────
    @ui.page("/status")
    def status_page():
        with ui.header().classes("bg-blue-900"):
            ui.link("< Chat", "/").classes("text-white")
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
            title=APP_TITLE, host=host, port=port,
            native=True, window_size=DEFAULT_WINDOW_SIZE, reload=False,
        )
    else:
        ui.run(title=APP_TITLE, host=host, port=port, reload=False)
