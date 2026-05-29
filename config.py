"""Local config persistence (gitignored config.json)."""
import json
import os
import logging

logger = logging.getLogger(__name__)

CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

DEFAULTS = {
    "tmdb_api_key": "",
    "language": "es",
}


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
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(merged, f, indent=2, ensure_ascii=False)


def get_tmdb_key() -> str:
    return load_config().get("tmdb_api_key", "").strip()


def get_default_language() -> str:
    lang = load_config().get("language", "es")
    return lang if lang in ("es", "en") else "es"
