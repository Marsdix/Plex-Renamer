# Plex Renamer

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-3670A0?style=flat-square&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-in_development-orange?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

A CLI tool I built because I needed it. Plex Renamer organizes your media library into the folder structure and naming conventions that Plex Media Server expects — automatically.

---

## What it does

- **Renames** series and movies to match Plex naming conventions
- **Generates** the folder structure for series, movies, and documents
- **Adds** Extras folders to existing series or movies
- **Two ways to run** — precompiled `.exe` (no Python needed) or Python script

---

## Installation

### Option 1 — `.exe` (easiest)

1. Download the latest `.exe` from [Releases](https://github.com/Marsdix/Plex-Renamer/releases/tag/v1.0.0)
2. Double-click to run — no Python required
3. On first launch it creates a **Plex Renamer** shortcut on your desktop

### Option 2 — Python script

**Requirements:** Python 3.x with "Add Python to PATH" checked during install.

```bash
# Verify Python is installed
python --version
```

1. Download the repo as ZIP → extract to a permanent folder
2. Double-click `setup.py` — creates a desktop shortcut
3. Use the shortcut to launch the app

> Keep the folder in a permanent location. Moving it later will break the shortcut — just run `setup.py` again to fix it.

---

## Usage

1. Open Plex Renamer (shortcut or `.exe`)
2. Select the folder containing your media files
3. Follow the prompts — renamed and organized files appear in the output folder

---

## Tech

- **Python** — core logic and file handling (`os`, `shutil`)
- **PyInstaller** — compiles the script into a standalone `.exe`

---

## License

MIT — use it, modify it, do what you need with it.
