"""Base classes and dataclasses for the LLM provider abstraction layer."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, Generator, List, Optional


class MessageRole(str, Enum):
    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"
    TOOL = "tool"


@dataclass
class Message:
    role: MessageRole
    content: str
    name: Optional[str] = None
    tool_calls: Optional[List[Dict]] = None
    tool_call_id: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = {"role": self.role.value, "content": self.content}
        if self.name:
            d["name"] = self.name
        if self.tool_calls:
            d["tool_calls"] = self.tool_calls
        if self.tool_call_id:
            d["tool_call_id"] = self.tool_call_id
        return d


@dataclass
class LLMResponse:
    content: str
    model: str
    finish_reason: str = "stop"
    tool_calls: List[Dict] = field(default_factory=list)
    usage: Dict = field(default_factory=dict)


class BaseLLMProvider(ABC):
    """Abstract base class for LLM providers."""

    @abstractmethod
    def complete(
        self,
        messages: List[Message],
        tools: Optional[List[Dict]] = None,
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        """Send messages to the LLM and get a complete response."""
        ...

    @abstractmethod
    def stream(
        self,
        messages: List[Message],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> Generator[str, None, None]:
        """Stream a response from the LLM. Does not support tool calls."""
        ...

    @abstractmethod
    def count_tokens(self, text: str) -> int:
        """Estimate token count for given text."""
        ...

    @property
    @abstractmethod
    def context_window(self) -> int:
        """Return the context window size for the current model."""
        ...

    @property
    @abstractmethod
    def model_name(self) -> str:
        """Return the model name/identifier."""
        ...
