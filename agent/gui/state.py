"""GUI application state management."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List, Optional


class Theme(str, Enum):
    LIGHT = "light"
    DARK = "dark"
    SYSTEM = "system"


@dataclass
class Message:
    role: str
    content: str
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict = field(default_factory=dict)


@dataclass
class QueryRecord:
    sql: str
    timestamp: datetime
    duration_ms: float
    row_count: int
    success: bool


@dataclass
class Alert:
    type: str  # "info", "warning", "error", "success"
    message: str
    timeout: int = 5


@dataclass
class AppState:
    """Global GUI application state."""

    theme: Theme = Theme.SYSTEM
    messages: List[Message] = field(default_factory=list)
    query_history: List[QueryRecord] = field(default_factory=list)
    alerts: List[Alert] = field(default_factory=list)
    is_loading: bool = False
    current_session_id: Optional[str] = None
    current_mode: str = "chat"
    current_provider: str = "ollama"
