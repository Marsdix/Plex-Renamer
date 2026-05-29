"""TMDB poster fetcher with in-memory cache + graceful fallback."""
import json
import logging
import random
import time
import urllib.error
import urllib.request

from config import get_tmdb_key

logger = logging.getLogger(__name__)

CACHE_TTL = 300  # seconds
_cache: dict[tuple[str, str], tuple[float, str]] = {}
IMAGE_BASE = "https://image.tmdb.org/t/p/w500"
API_BASE = "https://api.themoviedb.org/3"


def _api_lang(lang: str) -> str:
    return "es-ES" if lang == "es" else "en-US"


def get_random_poster(media_type: str, lang: str = "es") -> str | None:
    """Return a random poster URL from TMDB popular endpoint, or None on any failure.

    media_type: "movie" or "tv"
    lang: "es" or "en"
    """
    if media_type not in ("movie", "tv"):
        return None

    key = get_tmdb_key()
    if not key:
        return None

    cache_key = (media_type, lang)
    now = time.time()
    cached = _cache.get(cache_key)
    if cached and now - cached[0] < CACHE_TTL:
        results = cached[1]
        if results:
            return f"{IMAGE_BASE}{random.choice(results)}"

    url = f"{API_BASE}/{media_type}/popular?language={_api_lang(lang)}&page=1&api_key={key}"
    req = urllib.request.Request(url, headers={"Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=3) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        logger.warning(f"TMDB HTTP {e.code} for {media_type}: {e.reason}")
        return None
    except (urllib.error.URLError, TimeoutError, OSError) as e:
        logger.warning(f"TMDB request failed for {media_type}: {e}")
        return None
    except (json.JSONDecodeError, ValueError) as e:
        logger.warning(f"TMDB invalid JSON for {media_type}: {e}")
        return None

    posters = [r["poster_path"] for r in data.get("results", []) if r.get("poster_path")]
    if not posters:
        return None

    _cache[cache_key] = (now, posters)
    return f"{IMAGE_BASE}{random.choice(posters)}"


def is_configured() -> bool:
    return bool(get_tmdb_key())
