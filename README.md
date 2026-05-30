# Plex Renamer

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-3670A0?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

A small web app that organizes your media library into the folder structure and naming conventions that Plex Media Server expects — automatically.

- Cross-platform: **Windows · macOS · Linux**
- Bilingual UI: **Español / English**
- Optional **TMDB** integration: paste your API key to see real movie/series posters
- Glassmorphism dark UI

---

## What it does

- **Creates** folder structures for movies, series, and documentaries
- **Adds** an `Extras` folder to every existing media folder
- **Renames** series episodes to `Title - SXXEXX.ext`

---

## Download

Pre-built binaries: <https://github.com/Marsdix/Plex-Renamer/releases>

| Platform | File | Notes |
|----------|------|-------|
| macOS (Apple Silicon) | `PlexRenamer-macos-arm64` | `chmod +x` then double-click or run from terminal |
| Windows / Linux | — | Build from source (see below) |

> On first launch a desktop shortcut is created. Settings live in `~/.plex-renamer/config.json`.

---

## Run from source

Requires Python 3.10+.

```bash
git clone https://github.com/Marsdix/Plex-Renamer.git
cd Plex-Renamer
git lfs pull                          # poster images use Git LFS
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Then open <http://127.0.0.1:5001>.

---

## Build a standalone binary

A spec for PyInstaller is included. Each platform must build its own binary on that platform — there is no cross-compilation.

```bash
pip install -r requirements-build.txt
pyinstaller build.spec
```

Result:

| Platform | Output |
|----------|--------|
| Windows  | `dist/PlexRenamer.exe` |
| macOS    | `dist/PlexRenamer` (single-file executable; rename to `.command` if you want a double-click launcher) |
| Linux    | `dist/PlexRenamer` |

Double-click the binary or run it from a terminal. Flask starts on port `5001` and the default browser opens automatically.

---

## Configuration

Settings (TMDB API key, language) are saved to `~/.plex-renamer/config.json` — outside the project tree, so a packaged binary can write it regardless of install location.

To enable real posters:

1. Get a free TMDB API key at <https://www.themoviedb.org/settings/api>
2. Inside the app, click **Ajustes / Settings** in the header
3. Paste the key and save

Without a key the bundled banner images are used.

---

## Project layout

```
app.py                  Flask routes + entry point
config.py               Load/save ~/.plex-renamer/config.json
tmdb.py                 TMDB poster fetcher with in-memory cache + fallback
translations.py         ES/EN UI strings
build.spec              PyInstaller spec
templates/              Jinja2 templates (shared _header.html / _footer.html)
static/css/             Single styles_global.css with design tokens
static/images/          Bundled poster banners (Git LFS)
docs/superpowers/specs/ Design specs
```

---

## License

MIT — use it, modify it, do what you need with it.
