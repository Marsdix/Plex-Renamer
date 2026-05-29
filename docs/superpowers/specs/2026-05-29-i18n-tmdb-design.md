# i18n (ES/EN) + TMDB integration

## Resumen
Añadir dos features:
1. **i18n**: soporte español + inglés con toggle en header
2. **TMDB**: integración opcional para mostrar posters reales desde TMDB cuando el usuario añade su API key. Sin key → posters locales (banners existentes).

Todo configurable desde nueva página `/settings`. Configuración persistida en `config.json` local (gitignored).

## Arquitectura

### Persistencia local
- `config.json` en raíz del proyecto, esquema:
  ```json
  { "tmdb_api_key": "", "language": "es" }
  ```
- Helper `config.py` con `load_config()` y `save_config(data)`. Idempotente.
- `.gitignore` incluye `config.json`.

### Módulo i18n
- `translations.py` exporta dict `STRINGS = {"es": {...}, "en": {...}}` con ~50 keys (strings de UI).
- Helper en `app.py`:
  - `get_lang()` lee cookie `lang`, fallback `config.json`, fallback `es`.
  - `app.jinja_env.globals['t'] = lambda key: STRINGS[get_lang()].get(key, key)`
- Ruta `/set_language/<lang>` setea cookie + redirect referer.
- Templates reemplazan strings hardcoded por `{{ t('key') }}`.

### Módulo TMDB
- `tmdb.py` con función `get_random_poster(media_type: str) -> str | None`:
  - `media_type` ∈ `{"movie", "tv"}`
  - Lee API key de `config.json`. Si vacía → return None.
  - GET `https://api.themoviedb.org/3/{media_type}/popular?language={lang}&page=1`
  - Random pick de `results`, devuelve `https://image.tmdb.org/t/p/w500{poster_path}`
  - Caché en memoria: dict `{(media_type, lang): (timestamp, url)}` con TTL 5 min
  - Errores (401, timeout, conexión) → return None + log warning

### Settings page (`/settings`)
- GET: muestra form con TMDB key (password input + toggle visibility), lang radio buttons
- POST: valida (lang ∈ {"es","en"}), guarda en config.json, redirect /settings con mensaje
- Glass card centrada (estilo `content-card`)
- Link "Get free API key" → themoviedb.org/settings/api

## Routes Flask
| Route | Method | Acción |
|-------|--------|--------|
| `/settings` | GET | Render settings page |
| `/settings` | POST | Guarda config.json, redirect |
| `/set_language/<lang>` | GET | Set cookie, redirect referer |
| Routes existentes | (sin cambios de path) | Inyectan `poster_url` en context |

## Templates afectados
- `index.html`: i18n strings + link a `/settings`
- `crear_peliculas.html`: i18n + poster TMDB (movie) o local
- `crear_series.html`: i18n + poster TMDB (tv) o local
- `crear_documentales.html`: i18n + siempre local (TMDB sin endpoint específico)
- `agregar_extras.html`: i18n + siempre local
- `renombrar_series.html`: i18n + poster TMDB (tv) o local
- `info.html`: i18n
- `success.html`: i18n
- `settings.html` (NUEVO): form de configuración

## Header (cambio compartido)
- Añadir toggle `ES | EN` glass pill al lado del logo
- Añadir botón ⚙ Settings en header right (junto a Salir)

## Strings i18n (preliminar)
Categorías:
- Navegación: home, settings, exit, back
- Headings de página: create_movies, create_series, create_docs, add_extras, rename_series, info, success
- Form labels: base_path, name, season_count, required
- Buttons: create, add, rename, save
- Alerts: success, error
- Descripciones de cada nav-tile
- Settings page: tmdb_api_key, language, save_settings, get_api_key
- Info page: convenciones, cómo usar
- Footer

## Errores
- Sin TMDB key → posters locales, sin warning visible
- TMDB 401/403/timeout → posters locales + log
- config.json corrupto → recrear con defaults + log
- lang inválido en POST → reject, mantener actual

## Testing manual
- Toggle ES/EN cambia todos los textos
- Settings sin key: posters locales en /crear_peliculas
- Settings con key válida: posters TMDB en /crear_peliculas
- Settings con key inválida: fallback a locales
- config.json gitignored y no aparece en `git status`

## Fuera de scope
- Más idiomas (solo ES + EN)
- TMDB para documentales (no hay endpoint popular)
- Búsqueda TMDB por nombre escrito (puede ser fase 3)
- Cache persistente (solo memoria)
