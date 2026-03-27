# -*- mode: python ; coding: utf-8 -*-
"""
PyInstaller spec file for EDS DBA Agent

Build with:
    pyinstaller eds_agent.spec

Or create fresh spec:
    pyinstaller --onefile --windowed --name "EDS DBA Agent" agent/gui/app.py
"""

import sys
from pathlib import Path

# Project root
PROJECT_ROOT = Path(SPECPATH)

block_cipher = None

# Collect all agent modules
agent_modules = []
for py_file in (PROJECT_ROOT / 'agent').rglob('*.py'):
    rel_path = py_file.relative_to(PROJECT_ROOT)
    module_path = str(rel_path.with_suffix('')).replace('\\', '.').replace('/', '.')
    agent_modules.append(module_path)

a = Analysis(
    ['agent/gui/app.py'],
    pathex=[str(PROJECT_ROOT)],
    binaries=[],
    datas=[
        # Include configuration files
        ('agent_config.yaml', '.'),
        # Include documentation for RAG
        ('docs', 'docs'),
        # Include any data files
        ('data', 'data') if (PROJECT_ROOT / 'data').exists() else (None, None),
    ],
    hiddenimports=[
        # NiceGUI and web dependencies
        'nicegui',
        'nicegui.native',
        'fastapi',
        'uvicorn',
        'starlette',
        'websockets',
        'httptools',
        'watchfiles',

        # LLM providers
        'anthropic',
        'openai',
        'ollama',
        'httpx',

        # Database and utilities
        'pyodbc',
        'pandas',
        'numpy',

        # RAG dependencies
        'chromadb',
        'sentence_transformers',

        # Agent modules
        'agent',
        'agent.llm',
        'agent.llm.base',
        'agent.llm.registry',
        'agent.llm.claude',
        'agent.llm.ollama',
        'agent.gui',
        'agent.gui.app',
        'agent.core',
        'agent.tools',
        'agent.rag',
        'agent.memory',
        'agent.audit',
        'agent.security',
        'agent.cli',
        'agent.cli.app',

        # Standard library
        'asyncio',
        'json',
        'yaml',
        'sqlite3',
        'logging',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        # Exclude unnecessary packages to reduce size
        'tkinter',
        'matplotlib',
        'scipy',
        'PIL',
        'cv2',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

# Filter out None entries from datas
a.datas = [(src, dst) for src, dst in a.datas if src is not None]

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='EDS DBA Agent',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,  # No console window
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico' if (PROJECT_ROOT / 'assets' / 'icon.ico').exists() else None,
)
