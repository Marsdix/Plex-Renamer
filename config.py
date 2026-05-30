"""Local config persistence in ~/.plex-renamer/config.json.

Stored in the user home directory so a frozen PyInstaller binary can
write it regardless of install location permissions (Program Files,
/Applications, etc.).
"""
import json
import logging
import os

logger = logging.getLogger(__name__)

CONFIG_DIR = os.path.join(os.path.expanduser("~"), ".plex-renamer")
CONFIG_PATH = os.path.join(CONFIG_DIR, "config.json")

DEFAULTS = {
    "tmdb_api_key": "",
    "language": "es",
}


def _ensure_dir() -> None:
    try:
        os.makedirs(CONFIG_DIR, exist_ok=True)
    except OSError as e:
        logger.warning(f"Could not create config dir {CONFIG_DIR}: {e}")


def load_config() -> dict:
    if not os.path.exists(CONFIG_PATH):
        return dict(DEFAULTS)
    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
        return {**DEFAULTS, **data}
    except (json.JSONDecodeError, OSError) as e:
        logger.warning(f"config.json corrupt or unreadable ({e}); using defaults")
        return dict(DEFAULTS)


def save_config(data: dict) -> None:
    merged = {**load_config(), **data}
    _ensure_dir()
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)


def get_tmdb_key() -> str:
    return load_config().get("tmdb_api_key", "").strip()


def get_default_language() -> str:
    lang = load_config().get("language", "es")
    return lang if lang in ("es", "en") else "es"
