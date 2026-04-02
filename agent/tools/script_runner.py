"""Script runner tool — executes Python analysis scripts from the scripts directory.

Runs monitoring and analysis scripts (e.g. analyze_performance_issues,
extract_missing_indexes) with optional arguments and timeout control.
"""

import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

from agent.tools.base import (
    BaseTool,
    ToolCategory,
    ToolDefinition,
    ToolParameter,
    ToolResult,
)

logger = logging.getLogger(__name__)


class ScriptRunnerTool(BaseTool):
    """Execute Python analysis scripts from the scripts directory."""

    name = "script_runner"
    category = ToolCategory.SCRIPT

    def __init__(
        self,
        scripts_dir: str = "scripts",
        timeout: int = 300,
    ):
        self._scripts_dir = Path(scripts_dir)
        self._timeout = timeout

    @property
    def definition(self) -> ToolDefinition:
        return ToolDefinition(
            name=self.name,
            description=(
                "Execute a Python analysis script from the scripts directory. "
                "Available scripts include performance analysis, index extraction, "
                "blocking investigation, and documentation generation."
            ),
            parameters=[
                ToolParameter(
                    name="script_name",
                    type="string",
                    description="Name of the script to run (without .py extension).",
                ),
                ToolParameter(
                    name="args",
                    type="string",
                    description="Command-line arguments to pass to the script.",
                    required=False,
                    default="",
                ),
            ],
            category=self.category,
            returns="Script stdout output.",
        )

    def execute(self, **kwargs) -> ToolResult:
        script_name: str = kwargs.get("script_name", "")
        args: str = kwargs.get("args", "")

        if not script_name.strip():
            return ToolResult(success=False, error="Empty script name")

        # Resolve script path
        script_path = self._scripts_dir / f"{script_name}.py"
        if not script_path.exists():
            # Try without .py in case it was included
            script_path = self._scripts_dir / script_name
            if not script_path.exists():
                available = self._list_scripts()
                return ToolResult(
                    success=False,
                    error=f"Script '{script_name}' not found. Available: {', '.join(available[:10])}",
                )

        # Security: ensure script is within the scripts directory
        try:
            script_path = script_path.resolve()
            scripts_root = self._scripts_dir.resolve()
            if not str(script_path).startswith(str(scripts_root)):
                return ToolResult(
                    success=False,
                    error="Script path traversal detected",
                    metadata={"risk_level": "high"},
                )
        except Exception:
            return ToolResult(success=False, error="Invalid script path")

        # Build command
        cmd = [sys.executable, str(script_path)]
        if args:
            cmd.extend(args.split())

        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=self._timeout,
                cwd=str(self._scripts_dir.parent),
            )

            output = result.stdout
            if result.stderr:
                output += f"\n[stderr]: {result.stderr}"

            return ToolResult(
                success=result.returncode == 0,
                data=output,
                error=f"Exit code {result.returncode}" if result.returncode != 0 else None,
                metadata={
                    "script": script_name,
                    "exit_code": result.returncode,
                    "output_length": len(output),
                },
            )

        except subprocess.TimeoutExpired:
            return ToolResult(
                success=False,
                error=f"Script timed out after {self._timeout}s",
                metadata={"script": script_name},
            )
        except Exception as e:
            return ToolResult(success=False, error=f"Execution error: {e}")

    def _list_scripts(self) -> List[str]:
        """List available script names."""
        if not self._scripts_dir.exists():
            return []
        return sorted(
            p.stem for p in self._scripts_dir.glob("*.py")
            if not p.name.startswith("_")
        )


def create_script_tools(config: Optional[Dict[str, Any]] = None) -> List[BaseTool]:
    config = config or {}
    tools_config = config.get("tools", {})
    return [
        ScriptRunnerTool(
            scripts_dir=tools_config.get("scripts_dir", "scripts"),
            timeout=tools_config.get("script_timeout", 300),
        ),
    ]
