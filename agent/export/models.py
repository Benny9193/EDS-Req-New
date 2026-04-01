"""Report plan data models for the export system."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class ColumnDef:
    name: str
    type: str  # "string", "number", "currency", "percentage", "date"
    header: str
    width: int = 15
    format: Optional[str] = None


@dataclass
class QueryDef:
    sql: str
    name: str
    description: str = ""
    params: Dict = field(default_factory=dict)


@dataclass
class SheetDef:
    name: str
    title: str
    query: str  # references a QueryDef name
    columns: List[ColumnDef] = field(default_factory=list)
    type: str = "detail"  # "summary", "detail", "pivot", "drilldown"
    chart: Optional[Dict] = None


@dataclass
class ReportPlan:
    title: str
    description: str
    queries: List[QueryDef]
    sheets: List[SheetDef]
    metadata: Dict = field(default_factory=dict)
