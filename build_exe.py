"""
Build script for EDS DBA Agent executable.

This script builds a standalone .exe file that can be distributed
without requiring Python to be installed.

Usage:
    python build_exe.py

Requirements:
    pip install pyinstaller nicegui anthropic
"""

import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent


def check_dependencies():
    """Check that required build dependencies are installed."""
    missing = []

    try:
        import PyInstaller
    except ImportError:
        missing.append('pyinstaller')

    try:
        import nicegui
    except ImportError:
        missing.append('nicegui')

    if missing:
        print(f"Missing dependencies: {', '.join(missing)}")
        print(f"Install with: pip install {' '.join(missing)}")
        return False

    return True


def build():
    """Build the executable."""
    if not check_dependencies():
        sys.exit(1)

    print("=" * 60)
    print("Building EDS DBA Agent Executable")
    print("=" * 60)

    # Ensure data directories exist
    (PROJECT_ROOT / 'data' / 'vectordb').mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / 'data' / 'sessions').mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / 'data' / 'memory').mkdir(parents=True, exist_ok=True)
    (PROJECT_ROOT / 'data' / 'audit').mkdir(parents=True, exist_ok=True)

    # Run PyInstaller
    cmd = [
        sys.executable, '-m', 'PyInstaller',
        '--clean',
        '--noconfirm',
        str(PROJECT_ROOT / 'eds_agent.spec')
    ]

    print(f"Running: {' '.join(cmd)}")
    print()

    result = subprocess.run(cmd, cwd=PROJECT_ROOT)

    if result.returncode == 0:
        exe_path = PROJECT_ROOT / 'dist' / 'EDS DBA Agent.exe'
        print()
        print("=" * 60)
        print("BUILD SUCCESSFUL!")
        print("=" * 60)
        print(f"Executable: {exe_path}")
        print()
        print("To run the application:")
        print(f'  "{exe_path}"')
    else:
        print()
        print("BUILD FAILED!")
        print("Check the error messages above.")
        sys.exit(1)


if __name__ == '__main__':
    build()
