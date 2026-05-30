# Plex Renamer

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![PyInstaller](https://img.shields.io/badge/PyInstaller-3670A0?style=flat-square&logo=python&logoColor=white)
![Release](https://img.shields.io/github/v/release/Marsdix/Plex-Renamer?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)

A small web app that organizes your media library into the folder structure and naming conventions that Plex Media Server expects — automatically.

- Cross-platform: **Windows · macOS (Apple Silicon & Intel) · Linux**
- Bilingual UI: **Español / English** (toggle in header)
- Optional **TMDB** integration: paste your API key to see real movie/series posters
- Glassmorphism dark UI

---

## What it does

- **Creates** folder structures for movies, series, and documentaries
- **Adds** an `Extras` folder to every existing media folder
- **Renames** series episodes to `Title - SXXEXX.ext`

---

## Download

Grab the latest binary from the [Releases page](https://github.com/Marsdix/Plex-Renamer/releases/latest):

| Platform | File | How to run |
|----------|------|-----------|
| Windows (x64) | `PlexRenamer-windows-x64.exe` | Double-click |
| macOS (Apple Silicon) | `PlexRenamer-macos-arm64` | `chmod +x PlexRenamer-macos-arm64 && ./PlexRenamer-macos-arm64` |
| macOS (Intel) | `PlexRenamer-macos-x64` | `chmod +x PlexRenamer-macos-x64 && ./PlexRenamer-macos-x64` |
| Linux (x64) | `PlexRenamer-linux-x64` | `chmod +x PlexRenamer-linux-x64 && ./PlexRenamer-linux-x64` |

> On first launch a desktop shortcut is created. Flask listens on port `5001` and your default browser opens automatically.

Each release is built automatically by GitHub Actions on every `v*` tag — Windows, macOS (x64 + arm64) and Linux binaries land in the same release together.

---

## Usage

1. Launch the binary (or run from source — see below)
2. The browser opens at <http://127.0.0.1:5001>
3. Pick an action from the home grid:
   - **Crear Películas / Series / Documentales** — generate folder structures from scratch
   - **Agregar Extras** — bulk-add `Extras` folders to an existing library
   - **Renombrar Series** — rename every file inside each `Season XX` to `Title - SXXEXX.ext`
4. Use the **ES | EN** toggle in the header to switch language

To exit, click **Salir** in the header.

---

## Configuration (TMDB + language)

Settings live in `~/.plex-renamer/config.json` — outside the install location so a packaged binary can write it freely.

To enable real posters from TMDB:

1. Get a free API key at <https://www.themoviedb.org/settings/api>
2. Click **⚙ Ajustes / Settings** in the header
3. Paste the key, pick your language, save

Without a key the bundled banner images are used (graceful fallback).

---

## Run from source

Requires Python 3.10+ (3.12+ recommended).

```bash
git clone https://github.com/Marsdix/Plex-Renamer.git
cd Plex-Renamer
git lfs pull                          # poster images use Git LFS
python -m venv .venv
source .venv/bin/activate              # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

Open <http://127.0.0.1:5001>.

---

## Build a binary locally

```bash
pip install -r requirements-build.txt
pyinstaller build.spec
```

| Platform | Output |
|----------|--------|
| Windows  | `dist/PlexRenamer.exe` |
| macOS    | `dist/PlexRenamer` |
| Linux    | `dist/PlexRenamer` |

PyInstaller does **not** cross-compile — build on the target platform. For automated multi-platform builds use the included GitHub Actions workflow (`.github/workflows/release.yml`): push a `v*` tag and the three binaries are uploaded to the release.

---

## Project layout

```
app.py                       Flask routes + entry point
config.py                    Load/save ~/.plex-renamer/config.json
tmdb.py                      TMDB poster fetcher (in-memory cache + fallback)
translations.py              ES/EN UI strings
build.spec                   PyInstaller spec (cross-platform)
.github/workflows/release.yml  CI matrix build for Win / macOS / Linux
templates/                   Jinja2 templates (shared _header.html / _footer.html)
static/css/styles_global.css Single CSS with design tokens
static/images/               Bundled poster banners (Git LFS)
docs/superpowers/specs/      Design specs
```

---

## Tech stack

- **Flask** — web server + templating
- **Vanilla CSS** — single design-token-based stylesheet (no Bootstrap, no Tailwind)
- **Font Awesome** + **Fredoka One** / **Baloo 2** — typography & icons
- **PyInstaller** — single-file binaries per platform
- **GitHub Actions** — automated release builds
- **TMDB API** — optional poster source

---

## License

MIT — use it, modify it, do what you need with it.
