"""LLM provider registry for managing and instantiating providers."""

import logging
from typing import Any, Dict, Optional, Type

from agent.llm.base import BaseLLMProvider

logger = logging.getLogger(__name__)


class ProviderRegistry:
    """Registry for LLM provider classes and cached instances."""

    _providers: Dict[str, Type[BaseLLMProvider]] = {}
    _instances: Dict[str, BaseLLMProvider] = {}

    @classmethod
    def register(cls, name: str, provider_class: Type[BaseLLMProvider]) -> None:
        cls._providers[name] = provider_class
        logger.debug("Registered LLM provider: %s", name)

    @classmethod
    def get_provider(
        cls,
        name: str,
        config: Optional[Dict[str, Any]] = None,
    ) -> BaseLLMProvider:
        """Get or create a provider instance.

        Instances are cached by provider name + model to avoid recreating clients.
        """
        if name not in cls._providers:
            raise ValueError(
                f"Unknown provider '{name}'. "
                f"Available: {list(cls._providers.keys())}"
            )

        config = config or {}
        model = config.get("model", "")
        cache_key = f"{name}:{model}" if model else name

        if cache_key not in cls._instances:
            provider_class = cls._providers[name]
            cls._instances[cache_key] = provider_class(config)
            logger.info("Created %s provider instance (model=%s)", name, model or "default")

        return cls._instances[cache_key]

    @classmethod
    def list_providers(cls) -> list:
        return sorted(cls._providers.keys())

    @classmethod
    def is_registered(cls, name: str) -> bool:
        return name in cls._providers

    @classmethod
    def clear_instances(cls) -> None:
        cls._instances.clear()

    @classmethod
    def reset(cls) -> None:
        cls._providers.clear()
        cls._instances.clear()


def register_all_providers() -> None:
    """Register all built-in LLM providers. Import errors are logged, not raised."""
    try:
        from agent.llm.claude import ClaudeProvider
        ProviderRegistry.register("claude", ClaudeProvider)
    except ImportError:
        logger.debug("Claude provider unavailable (anthropic not installed)")

    try:
        from agent.llm.openai_provider import OpenAIProvider
        ProviderRegistry.register("openai", OpenAIProvider)
    except ImportError:
        logger.debug("OpenAI provider unavailable (openai not installed)")

    try:
        from agent.llm.ollama import OllamaProvider
        ProviderRegistry.register("ollama", OllamaProvider)
    except ImportError:
        logger.debug("Ollama provider unavailable (ollama not installed)")


def get_provider(
    name: str,
    config: Optional[Dict[str, Any]] = None,
) -> BaseLLMProvider:
    """Convenience function to get a provider, registering all if needed."""
    if not ProviderRegistry.list_providers():
        register_all_providers()
    return ProviderRegistry.get_provider(name, config)
