"""Agent configuration loader.

Reads agent_config.yaml from the project root, with environment variable overrides.
"""

import logging
import os
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)

_config: Optional[Dict[str, Any]] = None


def _find_config_file() -> Optional[Path]:
    """Locate agent_config.yaml by walking up from this file's directory."""
    current = Path(__file__).resolve().parent
    for _ in range(5):
        candidate = current / "agent_config.yaml"
        if candidate.exists():
            return candidate
        current = current.parent
    return None


def _apply_env_overrides(config: Dict[str, Any]) -> Dict[str, Any]:
    """Override config values with environment variables where set."""
    env_map = {
        "LLM_PROVIDER": ("llm", "default_provider"),
        "ANTHROPIC_API_KEY": ("llm", "providers", "claude", "api_key"),
        "OPENAI_API_KEY": ("llm", "providers", "openai", "api_key"),
        "OLLAMA_HOST": ("llm", "providers", "ollama", "host"),
        "DB_SERVER": ("database", "server"),
        "DB_DATABASE": ("database", "database"),
        "DB_USERNAME": ("database", "username"),
        "DB_PASSWORD": ("database", "password"),
    }

    for env_var, key_path in env_map.items():
        value = os.environ.get(env_var)
        if value is not None:
            d = config
            for key in key_path[:-1]:
                d = d.setdefault(key, {})
            d[key_path[-1]] = value

    return config


def load_config(config_path: Optional[str] = None) -> Dict[str, Any]:
    """Load and cache the agent configuration."""
    global _config
    if _config is not None:
        return _config

    config: Dict[str, Any] = {}

    path = Path(config_path) if config_path else _find_config_file()
    if path and path.exists():
        try:
            import yaml
            with open(path) as f:
                config = yaml.safe_load(f) or {}
            logger.info("Loaded config from %s", path)
        except Exception as e:
            logger.warning("Failed to load config from %s: %s", path, e)
    else:
        logger.info("No agent_config.yaml found, using defaults")

    config = _apply_env_overrides(config)
    _config = config
    return config


def get_llm_config(provider_name: Optional[str] = None) -> Dict[str, Any]:
    """Get config dict for a specific LLM provider."""
    config = load_config()
    llm_config = config.get("llm", {})

    if provider_name is None:
        provider_name = llm_config.get("default_provider", "ollama")

    providers = llm_config.get("providers", {})
    return providers.get(provider_name, {})


def get_default_provider() -> str:
    """Get the default LLM provider name."""
    config = load_config()
    return config.get("llm", {}).get("default_provider", "ollama")


def reset_config() -> None:
    """Clear cached config (useful for testing)."""
    global _config
    _config = None
