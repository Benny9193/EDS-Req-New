"""Core EDSAgent orchestrator.

Coordinates LLM calls, tool execution, and conversation management.
The agent supports a tool-calling loop: the LLM can request tool executions,
whose results are fed back for a follow-up response.
"""

import json
import logging
import re
import time
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Generator, List, Optional

from agent.config import get_default_provider, get_llm_config, load_config
from agent.llm.base import LLMResponse, Message, MessageRole
from agent.llm.registry import get_provider

logger = logging.getLogger(__name__)

MAX_TOOL_ROUNDS = 5  # Safety limit on consecutive tool-call rounds


class AgentMode(str, Enum):
    CHAT = "chat"
    SQL = "sql"
    DOCS = "docs"
    ANALYZE = "analyze"


@dataclass
class AgentResponse:
    content: str
    tool_calls: List[Dict] = field(default_factory=list)
    sql_generated: Optional[str] = None
    sources: List[str] = field(default_factory=list)
    error: Optional[str] = None
    metadata: Dict = field(default_factory=dict)


SYSTEM_PROMPT = """You are the EDS DBA Agent, an AI-powered database assistant for the EDS (Educational Data Services) SQL Server system.

You help with:
- Answering questions about the EDS database schema, tables, and stored procedures
- Generating SQL queries from natural language descriptions
- Explaining database concepts, performance issues, and best practices
- Searching through EDS documentation

The EDS system is a K-12 e-procurement platform with databases containing information about:
- Vendors, products, and pricing
- Purchase orders, requisitions, and bids
- Schools, districts, and users
- Budget tracking and approvals

Key databases: EDS (production catalog, ~1.4 TB, 439 tables) and dpa_EDSAdmin (monitoring).

When generating SQL:
- Always use explicit column names (no SELECT *)
- Include table aliases for readability
- Use BidHeaderId (not BidHeaderKey) for bid references
- Default date range is the most recent completed budget year (Dec 1 – Nov 30)

You have access to tools. Use them when the user asks you to execute queries, generate SQL, or perform other actions that require tools. When you use a tool, you will receive the result and can then respond to the user.

Be concise, accurate, and helpful. If you're unsure about a schema detail, say so."""

MODE_PROMPTS = {
    AgentMode.SQL: (
        "\n\nYou are in SQL generation mode. Focus on generating correct, "
        "efficient SQL Server queries. Use the query_generator tool to produce SQL, "
        "and the sql_executor tool to run it if the user requests execution."
    ),
    AgentMode.DOCS: (
        "\n\nYou are in documentation search mode. Help the user find "
        "information in the EDS documentation. Reference specific docs when possible."
    ),
    AgentMode.ANALYZE: (
        "\n\nYou are in analysis mode. Help diagnose database performance issues, "
        "blocking, missing indexes, and other operational concerns."
    ),
}

_TOOL_JSON_RE = re.compile(
    r'```(?:json)?\s*(\{.*?\})\s*```',
    re.DOTALL,
)


class EDSAgent:
    """Main agent orchestrator.

    Coordinates LLM calls with tool-calling loop. When the LLM requests
    tool execution, the agent runs the tool and feeds the result back
    for up to MAX_TOOL_ROUNDS iterations.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self._config = config or load_config()
        self.logger = logging.getLogger(f"{__name__}.EDSAgent")

        # Lazy-init subsystem slots
        self._llm_provider = None
        self._provider_name: Optional[str] = None
        self._tool_registry = None
        self._audit_logger = None
        self._session_manager = None
        self._learned_context = None
        self._context_manager = None
        self._summarizer = None
        self._conversation_summary: Optional[str] = None

        # User context (set via set_user_context)
        self._user_context = None

        # In-memory conversation history (fallback when no session_id)
        self._history: List[Message] = []
        self._mode: AgentMode = AgentMode.CHAT

    @property
    def mode(self) -> AgentMode:
        return self._mode

    @mode.setter
    def mode(self, value: AgentMode) -> None:
        self._mode = value
        self.logger.info("Mode changed to %s", value.value)

    @property
    def llm(self):
        """Lazy-load the LLM provider."""
        if self._llm_provider is None:
            provider_name = self._provider_name or get_default_provider()
            provider_config = get_llm_config(provider_name)
            self._llm_provider = get_provider(provider_name, provider_config)
            self._provider_name = provider_name
            self.logger.info(
                "Initialized %s provider (model=%s)",
                provider_name,
                self._llm_provider.model_name,
            )
        return self._llm_provider

    @property
    def tools(self):
        """Lazy-load the tool registry."""
        if self._tool_registry is None:
            from agent.tools.registry import register_all_tools
            self._tool_registry = register_all_tools(self._config)
            self.logger.info(
                "Loaded %d tools", self._tool_registry.tool_count
            )
        return self._tool_registry

    @property
    def audit(self):
        """Lazy-load the audit logger."""
        if self._audit_logger is None:
            from agent.audit.logger import get_audit_logger
            self._audit_logger = get_audit_logger(self._config)
        return self._audit_logger

    @property
    def sessions(self):
        """Lazy-load the session manager."""
        if self._session_manager is None:
            from agent.memory.session import SessionManager
            memory_config = self._config.get("memory", {})
            self._session_manager = SessionManager(
                sessions_dir=memory_config.get("sessions_dir", "data/sessions"),
                max_sessions=memory_config.get("max_sessions", 100),
            )
        return self._session_manager

    @property
    def learned_context(self):
        """Lazy-load the learned context database."""
        if self._learned_context is None:
            from agent.memory.learned_context import LearnedContextDB
            memory_config = self._config.get("memory", {})
            self._learned_context = LearnedContextDB(
                db_path=memory_config.get(
                    "learned_context_db", "data/memory/knowledge.sqlite"
                ),
            )
        return self._learned_context

    @property
    def context_manager(self):
        """Lazy-load the context window manager."""
        if self._context_manager is None:
            from agent.memory.summarizer import ContextWindowManager
            memory_config = self._config.get("memory", {})
            self._context_manager = ContextWindowManager(
                total_budget=memory_config.get("context_budget", 100_000),
                doc_budget=memory_config.get("doc_budget", 15_000),
                history_budget=memory_config.get("history_budget", 60_000),
            )
        return self._context_manager

    def set_provider(self, provider_name: str) -> None:
        """Switch to a different LLM provider."""
        provider_config = get_llm_config(provider_name)
        self._llm_provider = get_provider(provider_name, provider_config)
        self._provider_name = provider_name
        self.logger.info("Switched to %s provider", provider_name)

    def set_user_context(
        self,
        user_id: int,
        approval_level: int,
        district_id: int = None,
        school_id: int = None,
        user_name: str = "",
        district_name: str = "",
        school_name: str = "",
    ) -> None:
        """Set the current user's context for role-aware behavior.

        This controls what the agent tells the user they can do,
        and restricts SQL execution and write operations based on level.
        """
        from agent.security.roles import UserContext, Permission

        self._user_context = UserContext(
            user_id=user_id,
            approval_level=approval_level,
            district_id=district_id,
            school_id=school_id,
            user_name=user_name,
            district_name=district_name,
            school_name=school_name,
        )

        # Adjust SQL validator based on user level
        if self._tool_registry:
            sql_tool = self._tool_registry.get("sql_executor")
            if sql_tool and hasattr(sql_tool, "_validator"):
                sql_tool._validator.allow_writes = self._user_context.can_write_sql()

        self.logger.info(
            "User context set: %s (level %d)",
            self._user_context.level_label,
            approval_level,
        )

    @property
    def user_context(self):
        return self._user_context

    def _get_llm_tools(self) -> Optional[List[Dict]]:
        """Get tool definitions formatted for the current LLM provider."""
        if self.tools.tool_count == 0:
            return None

        provider_name = self._provider_name or get_default_provider()
        fmt = "anthropic" if provider_name == "claude" else "openai"
        tool_defs = self.tools.get_tools_for_llm(format=fmt)
        return tool_defs if tool_defs else None

    def _build_messages(
        self, user_message: str, session_id: Optional[str] = None,
    ) -> List[Message]:
        """Build the message list for the LLM call."""
        system = SYSTEM_PROMPT
        mode_extra = MODE_PROMPTS.get(self._mode, "")
        if mode_extra:
            system += mode_extra

        # Inject user context if set
        if self._user_context:
            system += f"\n\nCurrent user context:\n{self._user_context.to_prompt_context()}"

        # Inject learned context if available (trimmed to budget)
        try:
            context = self.learned_context.get_context_for_prompt()
            if context:
                context = self.context_manager.trim_learned_context(context)
                system += f"\n\nLearned context:\n{context}"
        except Exception:
            pass  # Don't fail the chat if learned context is unavailable

        messages = [Message(role=MessageRole.SYSTEM, content=system)]

        # Load history from session if provided, otherwise use in-memory
        history_msgs: List[Dict] = []
        if session_id:
            session_msgs = self.sessions.get_recent_context(session_id, n_messages=40)
            history_msgs = [{"role": sm.role, "content": sm.content} for sm in session_msgs]
        else:
            history_msgs = [{"role": m.role.value, "content": m.content} for m in self._history]

        # Check if summarization is needed
        if history_msgs:
            from agent.memory.summarizer import ConversationSummarizer
            summarizer = ConversationSummarizer(
                provider_name=self._provider_name or "ollama"
            )
            if summarizer.should_summarize(history_msgs):
                try:
                    # Summarize older messages, keep recent ones
                    split = len(history_msgs) // 2
                    old_msgs = history_msgs[:split]
                    recent_msgs = history_msgs[split:]
                    self._conversation_summary = summarizer.summarize(old_msgs)
                    history_msgs = recent_msgs
                    self.logger.info(
                        "Summarized %d messages, keeping %d recent",
                        split, len(recent_msgs),
                    )
                except Exception as e:
                    self.logger.warning("Summarization failed: %s", e)

            # Trim history to budget
            history_msgs = self.context_manager.trim_history(
                history_msgs, summary=self._conversation_summary,
            )

        for hm in history_msgs:
            role_str = hm.get("role", "user")
            try:
                role = MessageRole(role_str)
            except ValueError:
                role = MessageRole.USER
            messages.append(Message(role=role, content=hm.get("content", "")))

        messages.append(Message(role=MessageRole.USER, content=user_message))
        return messages

    def _execute_tool_calls(
        self,
        tool_calls: List[Dict],
        session_id: Optional[str] = None,
    ) -> List[Dict]:
        """Execute tool calls and return results as dicts."""
        results = []
        for tc in tool_calls:
            tool_name = tc.get("name", "")
            tool_input = tc.get("input", {})
            call_id = tc.get("id", "")

            self.logger.info("Executing tool: %s(%s)", tool_name, tool_input)
            start = time.perf_counter()

            try:
                result = self.tools.execute(tool_name, **tool_input)
                # Serialize result data for the LLM
                if result.success:
                    content = json.dumps(result.data, default=str)
                else:
                    content = f"Error: {result.error}"
            except Exception as e:
                self.logger.error("Tool execution failed: %s", e)
                content = f"Error: {e}"
                result = None

            elapsed_ms = (time.perf_counter() - start) * 1000
            success = result.success if result else False

            # Audit log the tool call
            self.audit.log_tool_call(
                tool_name=tool_name,
                params=tool_input,
                session_id=session_id,
                success=success,
                error=None if success else content,
                duration_ms=round(elapsed_ms, 2),
            )

            results.append({
                "call_id": call_id,
                "tool_name": tool_name,
                "content": content,
                "success": success,
                "metadata": result.metadata if result else {},
            })

        return results

    def chat(
        self,
        message: str,
        session_id: Optional[str] = None,
        mode: Optional[AgentMode] = None,
    ) -> AgentResponse:
        """Send a message and get a response, with tool-calling loop.

        If the LLM requests tool execution, the agent runs the tools and
        feeds results back for up to MAX_TOOL_ROUNDS iterations.
        """
        if mode is not None:
            self._mode = mode

        messages = self._build_messages(message, session_id=session_id)
        llm_tools = self._get_llm_tools()

        all_tool_calls = []
        sql_generated = None

        for _round in range(MAX_TOOL_ROUNDS):
            try:
                llm_start = time.perf_counter()
                response: LLMResponse = self.llm.complete(
                    messages, tools=llm_tools
                )
                llm_elapsed = (time.perf_counter() - llm_start) * 1000

                # Audit log the LLM call
                usage = response.usage or {}
                self.audit.log_llm_call(
                    provider=self._provider_name or "unknown",
                    model=response.model,
                    tokens_in=usage.get("input_tokens", 0),
                    tokens_out=usage.get("output_tokens", 0),
                    duration_ms=round(llm_elapsed, 2),
                    session_id=session_id,
                )
            except Exception as e:
                self.logger.error("LLM call failed: %s", e)
                self.audit.log_error(str(e), session_id=session_id)
                return AgentResponse(content="", error=f"LLM error: {e}")

            # If no tool calls, we have the final response
            if not response.tool_calls:
                break

            # Execute requested tools
            tool_results = self._execute_tool_calls(
                response.tool_calls, session_id=session_id
            )
            all_tool_calls.extend(tool_results)

            # Track generated SQL from query_generator results
            for tr in tool_results:
                if tr["tool_name"] == "query_generator" and tr["success"]:
                    sql_generated = tr["content"]

            # Append assistant message with tool calls to conversation
            messages.append(
                Message(
                    role=MessageRole.ASSISTANT,
                    content=response.content or "",
                    tool_calls=response.tool_calls,
                )
            )

            # Append tool results for each call
            for tc, tr in zip(response.tool_calls, tool_results):
                messages.append(
                    Message(
                        role=MessageRole.TOOL,
                        content=tr["content"],
                        tool_call_id=tc.get("id", ""),
                    )
                )
        else:
            # Exhausted tool rounds
            self.logger.warning("Hit MAX_TOOL_ROUNDS (%d)", MAX_TOOL_ROUNDS)

        # Persist to session if session_id provided, otherwise use in-memory history
        if session_id:
            self.sessions.add_message(session_id, "user", message)
            self.sessions.add_message(
                session_id, "assistant", response.content,
                tool_calls=all_tool_calls,
            )
        else:
            self._history.append(Message(role=MessageRole.USER, content=message))
            self._history.append(
                Message(role=MessageRole.ASSISTANT, content=response.content)
            )
            if len(self._history) > 40:
                self._history = self._history[-40:]

        return AgentResponse(
            content=response.content,
            tool_calls=all_tool_calls,
            sql_generated=sql_generated,
            metadata={
                "model": response.model,
                "finish_reason": response.finish_reason,
                "usage": response.usage,
                "provider": self._provider_name,
                "tool_rounds": _round + 1 if response.tool_calls else 0,
            },
        )

    def chat_stream(
        self,
        message: str,
        session_id: Optional[str] = None,
    ) -> Generator[str, None, None]:
        """Stream a response from the agent.

        Yields text chunks as they arrive. Does not support tool calls —
        use chat() for tool-calling interactions.
        """
        messages = self._build_messages(message, session_id=session_id)

        try:
            full_response = ""
            for chunk in self.llm.stream(messages):
                full_response += chunk
                yield chunk

            # Persist to session or in-memory history
            if session_id:
                self.sessions.add_message(session_id, "user", message)
                self.sessions.add_message(session_id, "assistant", full_response)
            else:
                self._history.append(Message(role=MessageRole.USER, content=message))
                self._history.append(
                    Message(role=MessageRole.ASSISTANT, content=full_response)
                )
                if len(self._history) > 40:
                    self._history = self._history[-40:]

        except Exception as e:
            self.logger.error("Stream failed: %s", e)
            yield f"\n[Error: {e}]"

    def clear_history(self) -> None:
        """Clear the conversation history."""
        self._history.clear()

    def get_status(self) -> Dict[str, Any]:
        """Return agent status information."""
        provider_name = self._provider_name or get_default_provider()
        model = self._llm_provider.model_name if self._llm_provider else "not initialized"

        tool_count = self._tool_registry.tool_count if self._tool_registry else 0
        tool_names = list(self._tool_registry) if self._tool_registry else []

        status = {
            "provider": provider_name,
            "model": model,
            "mode": self._mode.value,
            "history_length": len(self._history),
            "tools_loaded": tool_count,
            "tools": tool_names,
            "available_providers": ["claude", "openai", "ollama"],
        }

        if self._user_context:
            status["user"] = {
                "name": self._user_context.user_name,
                "level": self._user_context.approval_level,
                "role": self._user_context.level_label,
                "district_id": self._user_context.district_id,
                "school_id": self._user_context.school_id,
            }

        return status
