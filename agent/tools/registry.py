"""Tool registry for managing and executing agent tools."""

import logging
import time
from typing import Any, Dict, List, Optional

from agent.tools.base import (
    BaseTool,
    ToolCall,
    ToolCallResult,
    ToolCategory,
    ToolDefinition,
    ToolResult,
)

logger = logging.getLogger(__name__)


class ToolRegistry:
    """Registry for agent tools with category management and LLM format conversion."""

    def __init__(self):
        self._tools: Dict[str, BaseTool] = {}
        self._categories: Dict[ToolCategory, List[str]] = {
            cat: [] for cat in ToolCategory
        }

    @property
    def tool_count(self) -> int:
        return len(self._tools)

    def register(self, tool: BaseTool) -> None:
        """Register a tool. Raises ValueError on duplicate name."""
        if tool.name in self._tools:
            raise ValueError(f"Tool '{tool.name}' is already registered")
        self._tools[tool.name] = tool
        self._categories[tool.category].append(tool.name)
        logger.debug("Registered tool: %s (%s)", tool.name, tool.category.value)

    def register_many(self, tools: List[BaseTool]) -> None:
        for tool in tools:
            self.register(tool)

    def unregister(self, name: str) -> Optional[BaseTool]:
        tool = self._tools.pop(name, None)
        if tool:
            self._categories[tool.category].remove(name)
        return tool

    def get(self, name: str) -> Optional[BaseTool]:
        return self._tools.get(name)

    def get_definition(self, name: str) -> Optional[ToolDefinition]:
        tool = self._tools.get(name)
        return tool.definition if tool else None

    def list_tools(
        self,
        category: Optional[ToolCategory] = None,
        enabled_only: bool = True,
    ) -> List[str]:
        if category:
            names = self._categories.get(category, [])
        else:
            names = list(self._tools.keys())

        if enabled_only:
            names = [n for n in names if self._tools[n].enabled]

        return sorted(names)

    def get_all_definitions(
        self,
        category: Optional[ToolCategory] = None,
    ) -> List[ToolDefinition]:
        names = self.list_tools(category=category, enabled_only=True)
        return [self._tools[n].definition for n in names]

    def get_tools_for_llm(
        self,
        category: Optional[ToolCategory] = None,
        format: str = "anthropic",
    ) -> List[Dict]:
        """Get tool definitions formatted for a specific LLM provider.

        Args:
            category: Optional category filter.
            format: One of "anthropic", "openai", "ollama" (uses openai format).
        """
        definitions = self.get_all_definitions(category=category)
        if format == "anthropic":
            return [d.to_anthropic_format() for d in definitions]
        else:
            # OpenAI and Ollama both use OpenAI format
            return [d.to_openai_format() for d in definitions]

    def execute(self, name: str, **kwargs) -> ToolResult:
        """Execute a tool by name. Raises ValueError if not found or disabled."""
        tool = self._tools.get(name)
        if tool is None:
            raise ValueError(f"Tool '{name}' not found")
        if not tool.enabled:
            raise ValueError(f"Tool '{name}' is disabled")
        return tool.execute(**kwargs)

    def execute_call(self, tool_call: ToolCall) -> ToolCallResult:
        """Execute a ToolCall and return a timed ToolCallResult."""
        start = time.perf_counter()
        try:
            result = self.execute(tool_call.tool_name, **tool_call.parameters)
        except Exception as e:
            result = ToolResult(success=False, error=str(e))
        elapsed = (time.perf_counter() - start) * 1000
        return ToolCallResult(
            tool_call=tool_call,
            result=result,
            duration_ms=round(elapsed, 2),
        )

    def enable_category(self, category: ToolCategory) -> None:
        for name in self._categories.get(category, []):
            self._tools[name].enabled = True

    def disable_category(self, category: ToolCategory) -> None:
        for name in self._categories.get(category, []):
            self._tools[name].enabled = False

    def __contains__(self, name: str) -> bool:
        return name in self._tools

    def __iter__(self):
        return iter(sorted(self._tools.keys()))


# Module-level singleton
_global_registry: Optional[ToolRegistry] = None


def get_registry() -> ToolRegistry:
    """Get or create the global tool registry."""
    global _global_registry
    if _global_registry is None:
        _global_registry = ToolRegistry()
    return _global_registry


def register_all_tools(config: Optional[Dict[str, Any]] = None) -> ToolRegistry:
    """Register all built-in tools. Idempotent — returns immediately if already loaded."""
    registry = get_registry()
    if registry.tool_count > 0:
        return registry

    config = config or {}

    # Each module import is wrapped to degrade gracefully if dependencies are missing
    _loaders = [
        ("agent.tools.sql_executor", "create_sql_tools"),
        ("agent.tools.query_generator", "create_query_tools"),
        ("agent.tools.doc_retriever", "create_doc_tools"),
    ]

    for module_name, factory_name in _loaders:
        try:
            import importlib
            mod = importlib.import_module(module_name)
            factory = getattr(mod, factory_name)
            tools = factory(config)
            registry.register_many(tools)
            logger.info("Loaded tools from %s", module_name)
        except ImportError as e:
            logger.debug("Skipping %s: %s", module_name, e)
        except Exception as e:
            logger.warning("Failed to load %s: %s", module_name, e)

    return registry


def get_tool(name: str) -> Optional[BaseTool]:
    return get_registry().get(name)


def execute_tool(name: str, **kwargs) -> ToolResult:
    return get_registry().execute(name, **kwargs)


def list_tools(category: Optional[ToolCategory] = None) -> List[str]:
    return get_registry().list_tools(category=category)


def reset_registry() -> None:
    """Reset the global registry (for testing)."""
    global _global_registry
    _global_registry = None
