"""Claude (Anthropic) LLM provider."""

import logging
import os
from typing import Any, Dict, Generator, List, Optional

from agent.llm.base import BaseLLMProvider, LLMResponse, Message, MessageRole

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "claude-sonnet-4-20250514"

MODEL_CONTEXT_WINDOWS = {
    "claude-opus-4-6": 200_000,
    "claude-sonnet-4-6": 200_000,
    "claude-opus-4-5": 200_000,
    "claude-sonnet-4-5": 200_000,
    "claude-haiku-4-5": 200_000,
    "claude-sonnet-4-20250514": 200_000,
    "claude-opus-4-20250514": 200_000,
    "claude-3-5-sonnet-20241022": 200_000,
    "claude-3-5-haiku-20241022": 200_000,
}


class ClaudeProvider(BaseLLMProvider):
    """Anthropic Claude provider using the anthropic SDK."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        import anthropic

        config = config or {}
        self._model = config.get("model", DEFAULT_MODEL)
        api_key = config.get("api_key") or os.environ.get("ANTHROPIC_API_KEY")
        if not api_key:
            raise ValueError(
                "Anthropic API key required. Set ANTHROPIC_API_KEY env var "
                "or pass api_key in config."
            )
        self._client = anthropic.Anthropic(api_key=api_key)
        self._temperature = config.get("temperature", 0.0)
        self._max_tokens = config.get("max_tokens", 4096)

    def complete(
        self,
        messages: List[Message],
        tools: Optional[List[Dict]] = None,
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        system_msg = None
        api_messages = []

        for msg in messages:
            if msg.role == MessageRole.SYSTEM:
                system_msg = msg.content
            elif msg.role == MessageRole.TOOL:
                api_messages.append({
                    "role": "user",
                    "content": [
                        {
                            "type": "tool_result",
                            "tool_use_id": msg.tool_call_id or "",
                            "content": msg.content,
                        }
                    ],
                })
            else:
                api_messages.append({
                    "role": msg.role.value,
                    "content": msg.content,
                })

        kwargs: Dict[str, Any] = {
            "model": self._model,
            "messages": api_messages,
            "max_tokens": max_tokens or self._max_tokens,
            "temperature": temperature if temperature is not None else self._temperature,
        }
        if system_msg:
            kwargs["system"] = system_msg
        if tools:
            kwargs["tools"] = tools

        response = self._client.messages.create(**kwargs)

        content = ""
        tool_calls = []
        for block in response.content:
            if block.type == "text":
                content += block.text
            elif block.type == "tool_use":
                tool_calls.append({
                    "id": block.id,
                    "name": block.name,
                    "input": block.input,
                })

        return LLMResponse(
            content=content,
            model=response.model,
            finish_reason=response.stop_reason or "stop",
            tool_calls=tool_calls,
            usage={
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
            },
        )

    def stream(
        self,
        messages: List[Message],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> Generator[str, None, None]:
        system_msg = None
        api_messages = []

        for msg in messages:
            if msg.role == MessageRole.SYSTEM:
                system_msg = msg.content
            else:
                api_messages.append({
                    "role": msg.role.value,
                    "content": msg.content,
                })

        kwargs: Dict[str, Any] = {
            "model": self._model,
            "messages": api_messages,
            "max_tokens": max_tokens or self._max_tokens,
            "temperature": temperature if temperature is not None else self._temperature,
        }
        if system_msg:
            kwargs["system"] = system_msg

        with self._client.messages.stream(**kwargs) as stream:
            for text in stream.text_stream:
                yield text

    def count_tokens(self, text: str) -> int:
        return len(text) // 4

    @property
    def context_window(self) -> int:
        return MODEL_CONTEXT_WINDOWS.get(self._model, 200_000)

    @property
    def model_name(self) -> str:
        return self._model
