# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller spec — cross-platform single-file build for Plex Renamer.

Build:
  pyinstaller build.spec

Output:
  dist/PlexRenamer       (macOS / Linux)
  dist/PlexRenamer.exe   (Windows)
"""

import os
import sys
from PyInstaller.utils.hooks import collect_data_files

block_cipher = None

datas = [
    ("templates", "templates"),
    ("static", "static"),
]

hiddenimports = [
    "config",
    "tmdb",
    "translations",
]

# Windows-only: pywin32 for desktop shortcut creation
if sys.platform == "win32":
    hiddenimports += ["win32com", "win32com.client"]

icon_path = None
if sys.platform == "win32":
    candidate = os.path.join("static", "icons", "Palomitera.ico")
    if os.path.exists(candidate):
        icon_path = candidate
elif sys.platform == "darwin":
    candidate = os.path.join("static", "icons", "Palomitera.ico")
    if os.path.exists(candidate):
        icon_path = candidate

a = Analysis(
    ["app.py"],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["tkinter", "pytest", "playwright"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="PlexRenamer",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,        # GUI app: no terminal window on Windows
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=icon_path,
)
