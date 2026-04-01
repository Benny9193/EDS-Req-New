"""Core EDSAgent orchestrator.

This is the main agent class that coordinates LLM calls, tool execution,
and conversation management. In this initial vertical slice, it handles
direct chat via the LLM provider. Tool calling, RAG, memory, and security
layers will be added incrementally.
"""

import logging
import re
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Generator, List, Optional

from agent.config import get_default_provider, get_llm_config, load_config
from agent.llm.base import LLMResponse, Message, MessageRole
from agent.llm.registry import get_provider

logger = logging.getLogger(__name__)


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

Be concise, accurate, and helpful. If you're unsure about a schema detail, say so."""

MODE_PROMPTS = {
    AgentMode.SQL: (
        "\n\nYou are in SQL generation mode. Focus on generating correct, "
        "efficient SQL Server queries. Show the query, explain it briefly, "
        "and ask if the user wants to execute it."
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

    Coordinates LLM calls, manages conversation history within a session,
    and will eventually orchestrate tool calls, RAG retrieval, and memory.
    """

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self._config = config or load_config()
        self.logger = logging.getLogger(f"{__name__}.EDSAgent")

        # Lazy-init subsystem slots
        self._llm_provider = None
        self._provider_name: Optional[str] = None

        # In-memory conversation history (will be replaced by SessionManager)
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

    def set_provider(self, provider_name: str) -> None:
        """Switch to a different LLM provider."""
        provider_config = get_llm_config(provider_name)
        self._llm_provider = get_provider(provider_name, provider_config)
        self._provider_name = provider_name
        self.logger.info("Switched to %s provider", provider_name)

    def _build_messages(self, user_message: str) -> List[Message]:
        """Build the message list for the LLM call."""
        system = SYSTEM_PROMPT
        mode_extra = MODE_PROMPTS.get(self._mode, "")
        if mode_extra:
            system += mode_extra

        messages = [Message(role=MessageRole.SYSTEM, content=system)]
        messages.extend(self._history)
        messages.append(Message(role=MessageRole.USER, content=user_message))
        return messages

    def chat(
        self,
        message: str,
        session_id: Optional[str] = None,
        mode: Optional[AgentMode] = None,
    ) -> AgentResponse:
        """Send a message and get a response.

        Args:
            message: The user's message.
            session_id: Optional session ID (for future session management).
            mode: Optional mode override for this call.
        """
        if mode is not None:
            self._mode = mode

        messages = self._build_messages(message)

        try:
            response: LLMResponse = self.llm.complete(messages)
        except Exception as e:
            self.logger.error("LLM call failed: %s", e)
            return AgentResponse(
                content="",
                error=f"LLM error: {e}",
            )

        # Store conversation in history
        self._history.append(Message(role=MessageRole.USER, content=message))
        self._history.append(
            Message(role=MessageRole.ASSISTANT, content=response.content)
        )

        # Trim history to avoid unbounded growth (keep last 40 messages)
        if len(self._history) > 40:
            self._history = self._history[-40:]

        return AgentResponse(
            content=response.content,
            tool_calls=response.tool_calls,
            metadata={
                "model": response.model,
                "finish_reason": response.finish_reason,
                "usage": response.usage,
                "provider": self._provider_name,
            },
        )

    def chat_stream(
        self,
        message: str,
        session_id: Optional[str] = None,
    ) -> Generator[str, None, None]:
        """Stream a response from the agent.

        Yields text chunks as they arrive. Does not support tool calls.
        """
        messages = self._build_messages(message)

        try:
            full_response = ""
            for chunk in self.llm.stream(messages):
                full_response += chunk
                yield chunk

            # Store in history after streaming completes
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

        return {
            "provider": provider_name,
            "model": model,
            "mode": self._mode.value,
            "history_length": len(self._history),
            "available_providers": ["claude", "openai", "ollama"],
        }
