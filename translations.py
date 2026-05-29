"""UI translations for Spanish (es) and English (en)."""

STRINGS = {
    "es": {
        # Brand / global
        "brand": "Gestor de Medios",
        "brand_subtitle": "Plex Renamer · Organiza tu biblioteca",
        "exit": "Salir",
        "home": "Inicio",
        "settings": "Ajustes",
        "back_home": "Volver al inicio",
        "footer_text": "Plex Renamer",

        # Index
        "index_title": "¿Qué quieres organizar hoy?",
        "index_subtitle": "Crea estructuras, añade Extras o renombra archivos para que Plex los detecte correctamente.",
        "index_nav_label": "Acciones principales",

        # Nav tiles
        "nav_movies_h": "Crear Películas",
        "nav_movies_p": "Genera carpetas con estructura Plex para películas.",
        "nav_series_h": "Crear Series",
        "nav_series_p": "Crea carpetas con temporadas y carpeta Extras incluida.",
        "nav_docs_h": "Crear Documentales",
        "nav_docs_p": "Estructura específica para documentales con Extras.",
        "nav_extras_h": "Agregar Extras",
        "nav_extras_p": "Añade la carpeta Extras a todas las carpetas existentes.",
        "nav_rename_h": "Renombrar Series",
        "nav_rename_p": "Renombrado automático tipo S01E01 por temporada.",
        "nav_info_h": "Información",
        "nav_info_p": "Convenciones de Plex y guía de uso de la aplicación.",

        # Form pages — common
        "field_base_path": "Ruta base",
        "field_required": "*",
        "field_name": "Nombre",
        "hint_base_path_movies": "Carpeta donde se creará la película.",
        "hint_base_path_series": "Carpeta donde se creará la serie.",
        "hint_base_path_docs": "Carpeta donde se creará el documental.",
        "hint_base_path_extras": "Carpeta padre con tus medios (películas, series, etc.).",
        "hint_base_path_rename": "Carpeta que contiene Season 01, Season 02, …",
        "hint_name_movies": "Formato recomendado: Título (Año).",
        "hint_name_docs": "Formato recomendado: Título (Año).",
        "hint_name_rename": "Se usa como prefijo en cada archivo renombrado.",
        "hint_seasons": "Una carpeta por temporada en formato Season XX.",

        # Crear películas
        "movies_page_subtitle": "Carpeta + carpeta Extras lista para Plex",
        "movies_card_title": "Nueva película",
        "movies_card_desc": "Crea una carpeta con el nombre exacto que Plex espera y una carpeta Extras dentro.",
        "movies_field_name": "Nombre de la película",
        "movies_submit": "Crear película",
        "movies_poster_label": "Películas",
        "movies_poster_caption": "Carpeta lista para Plex",

        # Crear series
        "series_page_subtitle": "Temporadas y carpeta Extras incluidas",
        "series_card_title": "Nueva serie",
        "series_card_desc": "Se crearán carpetas Season 01, Season 02, … y una Extras.",
        "series_field_name": "Nombre de la serie",
        "series_field_seasons": "Número de temporadas",
        "series_submit": "Crear serie",
        "series_poster_label": "Series",
        "series_poster_caption": "Temporadas y Extras",

        # Crear documentales
        "docs_page_subtitle": "Estructura con carpeta Extras",
        "docs_card_title": "Nuevo documental",
        "docs_card_desc": "Crea carpeta con nombre exacto y una Extras dentro.",
        "docs_field_name": "Nombre del documental",
        "docs_submit": "Crear documental",
        "docs_poster_label": "Documentales",
        "docs_poster_caption": "Carpeta con Extras",

        # Agregar extras
        "extras_page_subtitle": "Carpetas Extras en lote",
        "extras_card_title": "Añadir carpeta Extras",
        "extras_card_desc": "Recorre todas las carpetas de la ruta indicada y crea una Extras dentro de cada una si no existe.",
        "extras_submit": "Agregar Extras a todo",
        "extras_poster_label": "Extras",
        "extras_poster_caption": "Una carpeta por cada medio",

        # Renombrar series
        "rename_page_subtitle": "Formato S01E01 automático",
        "rename_card_title": "Renombrado automático",
        "rename_card_desc": "Recorre cada Season XX y renombra archivos a Nombre - S01E01.ext.",
        "rename_field_path": "Ruta base de la serie",
        "rename_field_name": "Nombre de la serie",
        "rename_submit": "Renombrar",
        "rename_poster_label": "Renombrar",
        "rename_poster_caption": "S01E01, S01E02, …",

        # Info
        "info_page_subtitle": "Convenciones de Plex y guía rápida",
        "info_heading_structure": "Estructura de carpetas",
        "info_intro": "Plex detecta el contenido cuando los nombres siguen estas convenciones. Esta app crea las carpetas automáticamente — esto es lo que genera:",
        "info_heading_conventions": "Convenciones",
        "info_conv_movies_docs": "Películas y documentales: Título (Año).",
        "info_conv_series": "Series: temporadas en formato Season XX.",
        "info_conv_episodes": "Episodios: Nombre - S01E01.ext.",
        "info_conv_extras": "Carpeta Extras dentro de cada medio.",
        "info_heading_usage": "Cómo usar la app",
        "info_usage_create": "Crear Películas / Series / Documentales — genera la estructura desde cero.",
        "info_usage_extras": "Agregar Extras — añade la carpeta Extras en lote sobre una biblioteca existente.",
        "info_usage_rename": "Renombrar Series — renombra todos los archivos de cada Season XX al formato SXXEXX.",

        # Success
        "success_page_subtitle": "Operación completada",
        "success_card_title": "¡Operación completada!",

        # Settings
        "settings_page_subtitle": "API de TMDB e idioma",
        "settings_heading": "Ajustes",
        "settings_intro": "Configura tu API key de TMDB para obtener carteles reales de películas y series. Sin key se usan carteles incluidos en la app.",
        "settings_tmdb_label": "TMDB API key",
        "settings_tmdb_hint": "Tu key se guarda en config.json local — nunca se sube a Git.",
        "settings_tmdb_get": "Obtén tu API key gratis en themoviedb.org",
        "settings_lang_label": "Idioma de la interfaz",
        "settings_lang_es": "Español",
        "settings_lang_en": "English",
        "settings_save": "Guardar ajustes",
        "settings_show": "Mostrar",
        "settings_hide": "Ocultar",
        "settings_saved": "Ajustes guardados correctamente.",
        "settings_status": "Estado de TMDB",
        "settings_status_active": "Activa — carteles reales en uso.",
        "settings_status_inactive": "No configurada — usando carteles locales.",
    },
    "en": {
        # Brand / global
        "brand": "Media Manager",
        "brand_subtitle": "Plex Renamer · Organize your library",
        "exit": "Exit",
        "home": "Home",
        "settings": "Settings",
        "back_home": "Back to home",
        "footer_text": "Plex Renamer",

        # Index
        "index_title": "What do you want to organize today?",
        "index_subtitle": "Create folder structures, add Extras, or rename files so Plex detects them correctly.",
        "index_nav_label": "Main actions",

        # Nav tiles
        "nav_movies_h": "Create Movies",
        "nav_movies_p": "Generate folders with Plex structure for movies.",
        "nav_series_h": "Create Series",
        "nav_series_p": "Create folders with seasons and an Extras folder.",
        "nav_docs_h": "Create Documentaries",
        "nav_docs_p": "Specific structure for documentaries with Extras.",
        "nav_extras_h": "Add Extras",
        "nav_extras_p": "Add an Extras folder to every existing folder.",
        "nav_rename_h": "Rename Series",
        "nav_rename_p": "Automatic S01E01 renaming by season.",
        "nav_info_h": "Info",
        "nav_info_p": "Plex conventions and how to use the app.",

        # Form pages — common
        "field_base_path": "Base path",
        "field_required": "*",
        "field_name": "Name",
        "hint_base_path_movies": "Folder where the movie will be created.",
        "hint_base_path_series": "Folder where the series will be created.",
        "hint_base_path_docs": "Folder where the documentary will be created.",
        "hint_base_path_extras": "Parent folder with your media (movies, series, etc.).",
        "hint_base_path_rename": "Folder containing Season 01, Season 02, …",
        "hint_name_movies": "Recommended format: Title (Year).",
        "hint_name_docs": "Recommended format: Title (Year).",
        "hint_name_rename": "Used as a prefix on every renamed file.",
        "hint_seasons": "One folder per season in Season XX format.",

        # Crear películas
        "movies_page_subtitle": "Folder + Extras folder, Plex-ready",
        "movies_card_title": "New movie",
        "movies_card_desc": "Create a folder with the exact name Plex expects and an Extras folder inside.",
        "movies_field_name": "Movie name",
        "movies_submit": "Create movie",
        "movies_poster_label": "Movies",
        "movies_poster_caption": "Folder ready for Plex",

        # Crear series
        "series_page_subtitle": "Seasons and Extras folder included",
        "series_card_title": "New series",
        "series_card_desc": "Season 01, Season 02, … and an Extras folder will be created.",
        "series_field_name": "Series name",
        "series_field_seasons": "Number of seasons",
        "series_submit": "Create series",
        "series_poster_label": "Series",
        "series_poster_caption": "Seasons and Extras",

        # Crear documentales
        "docs_page_subtitle": "Structure with Extras folder",
        "docs_card_title": "New documentary",
        "docs_card_desc": "Create a folder with the exact name and an Extras folder inside.",
        "docs_field_name": "Documentary name",
        "docs_submit": "Create documentary",
        "docs_poster_label": "Documentaries",
        "docs_poster_caption": "Folder with Extras",

        # Agregar extras
        "extras_page_subtitle": "Extras folders in bulk",
        "extras_card_title": "Add Extras folder",
        "extras_card_desc": "Walks every folder under the given path and creates an Extras folder inside each one if missing.",
        "extras_submit": "Add Extras everywhere",
        "extras_poster_label": "Extras",
        "extras_poster_caption": "One folder per media item",

        # Renombrar series
        "rename_page_subtitle": "Automatic S01E01 format",
        "rename_card_title": "Automatic rename",
        "rename_card_desc": "Walks every Season XX and renames files to Name - S01E01.ext.",
        "rename_field_path": "Series base path",
        "rename_field_name": "Series name",
        "rename_submit": "Rename",
        "rename_poster_label": "Rename",
        "rename_poster_caption": "S01E01, S01E02, …",

        # Info
        "info_page_subtitle": "Plex conventions and quick guide",
        "info_heading_structure": "Folder structure",
        "info_intro": "Plex detects content when names follow these conventions. This app creates the folders automatically — here's what it produces:",
        "info_heading_conventions": "Conventions",
        "info_conv_movies_docs": "Movies and documentaries: Title (Year).",
        "info_conv_series": "Series: seasons in Season XX format.",
        "info_conv_episodes": "Episodes: Name - S01E01.ext.",
        "info_conv_extras": "Extras folder inside each media item.",
        "info_heading_usage": "How to use the app",
        "info_usage_create": "Create Movies / Series / Documentaries — generates the structure from scratch.",
        "info_usage_extras": "Add Extras — adds an Extras folder in bulk over an existing library.",
        "info_usage_rename": "Rename Series — renames every file inside each Season XX to SXXEXX format.",

        # Success
        "success_page_subtitle": "Operation completed",
        "success_card_title": "Operation completed!",

        # Settings
        "settings_page_subtitle": "TMDB API and language",
        "settings_heading": "Settings",
        "settings_intro": "Configure your TMDB API key to fetch real posters for movies and series. Without a key, the bundled posters are used.",
        "settings_tmdb_label": "TMDB API key",
        "settings_tmdb_hint": "Your key is stored in a local config.json — never pushed to Git.",
        "settings_tmdb_get": "Get your free API key at themoviedb.org",
        "settings_lang_label": "Interface language",
        "settings_lang_es": "Español",
        "settings_lang_en": "English",
        "settings_save": "Save settings",
        "settings_show": "Show",
        "settings_hide": "Hide",
        "settings_saved": "Settings saved successfully.",
        "settings_status": "TMDB status",
        "settings_status_active": "Active — real posters in use.",
        "settings_status_inactive": "Not configured — using local posters.",
    },
}


def t(key: str, lang: str = "es") -> str:
    """Lookup a translation key for the given language, fallback to key itself."""
    return STRINGS.get(lang, STRINGS["es"]).get(key, STRINGS["es"].get(key, key))
