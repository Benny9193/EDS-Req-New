"""Ollama (local) LLM provider."""

import logging
import os
from typing import Any, Dict, Generator, List, Optional

from agent.llm.base import BaseLLMProvider, LLMResponse, Message, MessageRole

logger = logging.getLogger(__name__)

DEFAULT_MODEL = "qwen2.5:14b"
DEFAULT_HOST = "http://localhost:11434"

MODEL_CONTEXT_WINDOWS = {
    "llama3.3": 128_000,
    "llama3.1": 128_000,
    "llama3.2": 128_000,
    "llama3": 8_000,
    "mistral": 8_000,
    "mixtral": 32_000,
    "qwen2.5:14b": 32_000,
    "qwen2.5:7b": 32_000,
    "qwen2.5:72b": 32_000,
    "qwen2.5-coder:14b": 32_000,
    "phi3": 4_000,
    "phi3:medium": 4_000,
    "deepseek-r1:7b": 32_000,
    "deepseek-r1:14b": 32_000,
    "gemma2": 8_000,
    "gemma2:27b": 8_000,
}


class OllamaProvider(BaseLLMProvider):
    """Ollama provider for local LLM inference."""

    def __init__(self, config: Optional[Dict[str, Any]] = None):
        config = config or {}
        self._model = config.get("model", DEFAULT_MODEL)
        self._host = config.get("host") or os.environ.get("OLLAMA_HOST", DEFAULT_HOST)
        self._temperature = config.get("temperature", 0.0)
        self._max_tokens = config.get("max_tokens", 4096)
        self._client = None
        self._use_sdk = True

        try:
            import ollama
            self._client = ollama.Client(host=self._host)
        except ImportError:
            self._use_sdk = False
            logger.info("ollama SDK not available, falling back to httpx")

    def _httpx_chat(
        self,
        messages: List[Dict],
        stream: bool = False,
        tools: Optional[List[Dict]] = None,
    ) -> Any:
        """Fallback using httpx when ollama SDK is unavailable."""
        import httpx

        payload: Dict[str, Any] = {
            "model": self._model,
            "messages": messages,
            "stream": stream,
            "options": {
                "temperature": self._temperature,
                "num_predict": self._max_tokens,
            },
        }
        if tools:
            payload["tools"] = tools

        if stream:
            return httpx.stream(
                "POST",
                f"{self._host}/api/chat",
                json=payload,
                timeout=120.0,
            )
        else:
            resp = httpx.post(
                f"{self._host}/api/chat",
                json=payload,
                timeout=120.0,
            )
            resp.raise_for_status()
            return resp.json()

    def complete(
        self,
        messages: List[Message],
        tools: Optional[List[Dict]] = None,
        max_tokens: int = 4096,
        temperature: float = 0.0,
    ) -> LLMResponse:
        api_messages = []
        for msg in messages:
            api_messages.append({
                "role": msg.role.value,
                "content": msg.content,
            })

        if self._use_sdk and self._client:
            kwargs: Dict[str, Any] = {
                "model": self._model,
                "messages": api_messages,
                "options": {
                    "temperature": temperature if temperature is not None else self._temperature,
                    "num_predict": max_tokens or self._max_tokens,
                },
            }
            if tools:
                kwargs["tools"] = tools

            response = self._client.chat(**kwargs)

            content = response.get("message", {}).get("content", "")
            tool_calls = []
            for tc in response.get("message", {}).get("tool_calls", []):
                func = tc.get("function", {})
                tool_calls.append({
                    "id": f"ollama_{func.get('name', 'unknown')}",
                    "name": func.get("name", ""),
                    "input": func.get("arguments", {}),
                })

            return LLMResponse(
                content=content,
                model=self._model,
                finish_reason="tool_use" if tool_calls else "stop",
                tool_calls=tool_calls,
                usage={
                    "input_tokens": response.get("prompt_eval_count", 0),
                    "output_tokens": response.get("eval_count", 0),
                },
            )
        else:
            response = self._httpx_chat(api_messages, stream=False, tools=tools)
            content = response.get("message", {}).get("content", "")
            return LLMResponse(
                content=content,
                model=self._model,
                finish_reason="stop",
                usage={
                    "input_tokens": response.get("prompt_eval_count", 0),
                    "output_tokens": response.get("eval_count", 0),
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

        if self._use_sdk and self._client:
            response_stream = self._client.chat(
                model=self._model,
                messages=api_messages,
                stream=True,
                options={
                    "temperature": temperature if temperature is not None else self._temperature,
                    "num_predict": max_tokens or self._max_tokens,
                },
            )
            for chunk in response_stream:
                content = chunk.get("message", {}).get("content", "")
                if content:
                    yield content
        else:
            import json
            with self._httpx_chat(api_messages, stream=True) as resp:
                for line in resp.iter_lines():
                    if line:
                        data = json.loads(line)
                        content = data.get("message", {}).get("content", "")
                        if content:
                            yield content

    def count_tokens(self, text: str) -> int:
        return len(text) // 4

    @property
    def context_window(self) -> int:
        return MODEL_CONTEXT_WINDOWS.get(self._model, 4096)

    @property
    def model_name(self) -> str:
        return self._model
