"""OpenAI LLM provider."""

import logging
import os
from typing import Any, Dict, Generator, List, Optional

from agent.llm.base import BaseLLMProvider, LLMResponse, Message, MessageRole

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "gpt-4o"

MODEL_CONTEXT_WINDOWS = {
    "gpt-4o": 128_000,
    "gpt-4o-mini": 128_000,
    "gpt-4-turbo": 128_000,
    "gpt-4": 8_192,
    "gpt-3.5-turbo": 16_385,
}


class OpenAIProvider(BaseLLMProvider):
    """OpenAI provider using the openai SDK."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        import openai

        config = config or {}
        self._model = config.get("model", DEFAULT_MODEL)
        api_key = config.get("api_key") or os.environ.get("OPENAI_API_KEY")
        if not api_key:
            raise ValueError(
                "OpenAI API key required. Set OPENAI_API_KEY env var "
                "or pass api_key in config."
            )
        self._client = openai.OpenAI(api_key=api_key)
        self._temperature = config.get("temperature", 0.0)
        self._max_tokens = config.get("max_tokens", 4096)

    def complete(
        self,
        messages: List[Message],
        tools: Optional[List[Dict]] = None,
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        api_messages = []
        for msg in messages:
            if msg.role == MessageRole.TOOL:
                api_messages.append({
                    "role": "tool",
                    "content": msg.content,
                    "tool_call_id": msg.tool_call_id or "",
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
        if tools:
            kwargs["tools"] = tools

        response = self._client.chat.completions.create(**kwargs)
        choice = response.choices[0]

        tool_calls = []
        if choice.message.tool_calls:
            import json
            for tc in choice.message.tool_calls:
                tool_calls.append({
                    "id": tc.id,
                    "name": tc.function.name,
                    "input": json.loads(tc.function.arguments),
                })

        return LLMResponse(
            content=choice.message.content or "",
            model=response.model,
            finish_reason=choice.finish_reason or "stop",
            tool_calls=tool_calls,
            usage={
                "input_tokens": response.usage.prompt_tokens if response.usage else 0,
                "output_tokens": response.usage.completion_tokens if response.usage else 0,
            },
        )

    def stream(
        self,
        messages: List[Message],
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> Generator[str, None, None]:
        api_messages = [
            {"role": msg.role.value, "content": msg.content}
            for msg in messages
        ]

        kwargs: Dict[str, Any] = {
            "model": self._model,
            "messages": api_messages,
            "max_tokens": max_tokens or self._max_tokens,
            "temperature": temperature if temperature is not None else self._temperature,
            "stream": True,
        }

        stream = self._client.chat.completions.create(**kwargs)
        for chunk in stream:
            if chunk.choices and chunk.choices[0].delta.content:
                yield chunk.choices[0].delta.content

    def count_tokens(self, text: str) -> int:
        return len(text) // 4

    @property
    def context_window(self) -> int:
        return MODEL_CONTEXT_WINDOWS.get(self._model, 128_000)

    @property
    def model_name(self) -> str:
        return self._model
