"""Base classes and dataclasses for the agent tool system."""

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional


class ToolCategory(str, Enum):
    SQL = "sql"
    ANALYSIS = "analysis"
    DOCUMENTATION = "documentation"
    MONITORING = "monitoring"
    SCRIPT = "script"
    UTILITY = "utility"


@dataclass
class ToolParameter:
    name: str
    type: str
    description: str
    required: bool = True
    default: Any = None
    enum: Optional[List] = None

    def to_json_schema(self) -> Dict[str, Any]:
        schema: Dict[str, Any] = {
            "type": self.type,
            "description": self.description,
        }
        if self.enum:
            schema["enum"] = self.enum
        if self.default is not None:
            schema["default"] = self.default
        return schema


@dataclass
class ToolDefinition:
    name: str
    description: str
    parameters: List[ToolParameter]
    category: ToolCategory
    returns: str = ""

    def to_json_schema(self) -> Dict[str, Any]:
        """Convert to JSON Schema for tool parameters."""
        properties = {}
        required = []
        for param in self.parameters:
            properties[param.name] = param.to_json_schema()
            if param.required:
                required.append(param.name)

        return {
            "type": "object",
            "properties": properties,
            "required": required,
        }

    def to_anthropic_format(self) -> Dict[str, Any]:
        """Format for Anthropic's tool calling API."""
        return {
            "name": self.name,
            "description": self.description,
            "input_schema": self.to_json_schema(),
        }

    def to_openai_format(self) -> Dict[str, Any]:
        """Format for OpenAI's tool calling API."""
        return {
            "type": "function",
            "function": {
                "name": self.name,
                "description": self.description,
                "parameters": self.to_json_schema(),
            },
        }


@dataclass
class ToolResult:
    success: bool
    data: Any = None
    error: Optional[str] = None
    metadata: Dict = field(default_factory=dict)


@dataclass
class ToolCall:
    tool_name: str
    parameters: Dict
    call_id: str = ""


@dataclass
class ToolCallResult:
    tool_call: ToolCall
    result: ToolResult
    duration_ms: float = 0.0


class BaseTool(ABC):
    """Abstract base class for agent tools."""

    name: str
    category: ToolCategory
    enabled: bool = True

    @property
    @abstractmethod
    def definition(self) -> ToolDefinition:
        """Return the tool's definition for LLM registration."""
        ...

    @abstractmethod
    def execute(self, **kwargs) -> ToolResult:
        """Execute the tool with the given parameters."""
        ...

    def __call__(self, **kwargs) -> ToolResult:
        return self.execute(**kwargs)
