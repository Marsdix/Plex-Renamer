from flask import Flask, render_template, request, redirect, make_response, url_for
import os
import signal
import sys
import logging
from threading import Timer
import webbrowser
import platform

from config import load_config, save_config, get_default_language
from translations import STRINGS
from tmdb import get_random_poster, is_configured as tmdb_configured

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(base_path, "templates")
static_folder = os.path.join(base_path, "static")

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)


# --- i18n -------------------------------------------------------------------

SUPPORTED_LANGS = ("es", "en")


def current_lang() -> str:
    cookie = request.cookies.get("lang")
    if cookie in SUPPORTED_LANGS:
        return cookie
    return get_default_language()


def t(key: str) -> str:
    lang = current_lang()
    return STRINGS.get(lang, STRINGS["es"]).get(key, STRINGS["es"].get(key, key))


@app.context_processor
def inject_globals():
    return {
        "t": t,
        "lang": current_lang(),
        "tmdb_active": tmdb_configured(),
    }


# --- Open browser + desktop shortcut ---------------------------------------

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5001/")


def create_desktop_shortcut():
    system = platform.system()
    try:
        if system == "Windows":
            from win32com.client import Dispatch
            desktop = os.path.join(os.environ["USERPROFILE"], "Desktop")
            shortcut_path = os.path.join(desktop, "Renombrador Plex.lnk")
            target_path = os.path.abspath(sys.argv[0])
            icon_path = os.path.join(static_folder, "icons", "Palomitera.ico")
            if os.path.exists(shortcut_path):
                logger.info("El acceso directo ya existe.")
                return
            shell = Dispatch("WScript.Shell")
            shortcut = shell.CreateShortcut(shortcut_path)
            shortcut.TargetPath = sys.executable
            shortcut.Arguments = f'"{target_path}"'
            shortcut.WorkingDirectory = os.path.dirname(target_path)
            shortcut.IconLocation = icon_path if os.path.exists(icon_path) else ""
            shortcut.save()
            logger.info(f"Acceso directo creado: {shortcut_path}")
        elif system == "Darwin":
            desktop = os.path.join(os.path.expanduser("~"), "Desktop")
            script_path = os.path.abspath(sys.argv[0])
            shortcut_path = os.path.join(desktop, "Renombrador Plex.command")
            if os.path.exists(shortcut_path):
                logger.info("El acceso directo ya existe.")
                return
            os.makedirs(desktop, exist_ok=True)
            with open(shortcut_path, "w") as f:
                f.write(f'#!/bin/bash\ncd "{os.path.dirname(script_path)}"\n"{sys.executable}" "{script_path}"\n')
            os.chmod(shortcut_path, 0o755)
            logger.info(f"Acceso directo creado: {shortcut_path}")
        else:
            logger.info(f"Creación de acceso directo no soportada en {system}.")
    except Exception as e:
        logger.error(f"Error al crear el acceso directo: {e}")


# --- Domain helpers --------------------------------------------------------

def manejar_error(mensaje, error):
    logger.error(f"{mensaje}: {error}")
    return f"{mensaje}: {error}"


def crear_estructura_peliculas(ruta_base, nombre_pelicula):
    try:
        if not os.path.exists(ruta_base):
            return f"Ruta base '{ruta_base}' no existe."
        ruta_pelicula = os.path.join(ruta_base, nombre_pelicula)
        os.makedirs(ruta_pelicula, exist_ok=True)
        os.makedirs(os.path.join(ruta_pelicula, "Extras"), exist_ok=True)
        return f"Película '{nombre_pelicula}' creada con éxito en '{ruta_base}'."
    except Exception as e:
        return manejar_error("Error al crear la película", e)


def crear_estructura_series(ruta_base, nombre_serie, temporadas):
    try:
        if not os.path.exists(ruta_base):
            return f"Ruta base '{ruta_base}' no existe."
        ruta_serie = os.path.join(ruta_base, nombre_serie)
        os.makedirs(ruta_serie, exist_ok=True)
        for i in range(1, temporadas + 1):
            os.makedirs(os.path.join(ruta_serie, f"Season {i:02}"), exist_ok=True)
        os.makedirs(os.path.join(ruta_serie, "Extras"), exist_ok=True)
        return f"Serie '{nombre_serie}' creada con éxito en '{ruta_base}' con {temporadas} temporadas."
    except Exception as e:
        return manejar_error("Error al crear la serie", e)


def crear_estructura_documentales(ruta_base, nombre_documental):
    try:
        if not os.path.exists(ruta_base):
            return f"Ruta base '{ruta_base}' no existe."
        ruta_documental = os.path.join(ruta_base, nombre_documental)
        os.makedirs(ruta_documental, exist_ok=True)
        os.makedirs(os.path.join(ruta_documental, "Extras"), exist_ok=True)
        return f"Documental '{nombre_documental}' creado con éxito en '{ruta_base}'."
    except Exception as e:
        return manejar_error("Error al crear el documental", e)


def agregar_extras(ruta_base):
    try:
        if not os.path.exists(ruta_base):
            return f"Ruta base '{ruta_base}' no existe."
        carpetas = [f for f in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, f))]
        for carpeta in carpetas:
            ruta_extras = os.path.join(ruta_base, carpeta, "Extras")
            os.makedirs(ruta_extras, exist_ok=True)
        return f"Carpetas 'Extras' añadidas con éxito en todas las carpetas de '{ruta_base}'."
    except Exception as e:
        return manejar_error("Error al agregar carpetas 'Extras'", e)


def renombrar_series_automatico(ruta_base, nombre_serie):
    try:
        if not os.path.exists(ruta_base):
            return f"Ruta base '{ruta_base}' no existe."
        carpetas = [f for f in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, f)) and f.startswith("Season")]
        if not carpetas:
            return "No se encontraron carpetas de temporadas en el formato 'Season XX'."

        carpetas.sort()
        for carpeta in carpetas:
            temporada = carpeta.split(" ")[1]
            ruta_temporada = os.path.join(ruta_base, carpeta)
            archivos = sorted(os.listdir(ruta_temporada))
            for contador, archivo in enumerate(archivos, start=1):
                ruta_completa = os.path.join(ruta_temporada, archivo)
                if os.path.isdir(ruta_completa):
                    continue
                extension = os.path.splitext(archivo)[1]
                numero_episodio = f"E{contador:02}"
                nuevo_nombre = f"{nombre_serie} - S{temporada}{numero_episodio}{extension}"
                ruta_nueva = os.path.join(ruta_temporada, nuevo_nombre)
                os.rename(ruta_completa, ruta_nueva)
        return f"Renombrado automático completo para la serie '{nombre_serie}'."
    except Exception as e:
        return manejar_error("Error al renombrar la serie", e)


# --- Routes ----------------------------------------------------------------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/crear_peliculas", methods=["GET", "POST"])
def crear_peliculas():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_pelicula = request.form["nombre"]
        mensaje = crear_estructura_peliculas(ruta_base, nombre_pelicula)
    poster_url = get_random_poster("movie", current_lang())
    return render_template("crear_peliculas.html", mensaje=mensaje, poster_url=poster_url)


@app.route("/crear_series", methods=["GET", "POST"])
def crear_series():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_serie = request.form["nombre"]
        temporadas = int(request.form["temporadas"])
        mensaje = crear_estructura_series(ruta_base, nombre_serie, temporadas)
    poster_url = get_random_poster("tv", current_lang())
    return render_template("crear_series.html", mensaje=mensaje, poster_url=poster_url)


@app.route("/crear_documentales", methods=["GET", "POST"])
def crear_documentales():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_documental = request.form["nombre"]
        mensaje = crear_estructura_documentales(ruta_base, nombre_documental)
    return render_template("crear_documentales.html", mensaje=mensaje)


@app.route("/agregar_extras", methods=["GET", "POST"])
def agregar_extras_view():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        mensaje = agregar_extras(ruta_base)
    return render_template("agregar_extras.html", mensaje=mensaje)


@app.route("/renombrar_series", methods=["GET", "POST"])
def renombrar_series():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_serie = request.form["nombre"]
        mensaje = renombrar_series_automatico(ruta_base, nombre_serie)
    poster_url = get_random_poster("tv", current_lang())
    return render_template("renombrar_series.html", mensaje=mensaje, poster_url=poster_url)


@app.route("/info")
def info():
    return render_template("info.html")


@app.route("/settings", methods=["GET", "POST"])
def settings():
    saved = False
    if request.method == "POST":
        api_key = request.form.get("tmdb_api_key", "").strip()
        lang = request.form.get("language", "es")
        if lang not in SUPPORTED_LANGS:
            lang = "es"
        save_config({"tmdb_api_key": api_key, "language": lang})
        response = make_response(redirect(url_for("settings", saved=1)))
        response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365)
        return response

    saved = request.args.get("saved") == "1"
    config = load_config()
    return render_template(
        "settings.html",
        saved=saved,
        tmdb_key=config.get("tmdb_api_key", ""),
        current_language=current_lang(),
    )


@app.route("/set_language/<lang>")
def set_language(lang):
    if lang not in SUPPORTED_LANGS:
        lang = "es"
    referer = request.referrer or url_for("index")
    response = make_response(redirect(referer))
    response.set_cookie("lang", lang, max_age=60 * 60 * 24 * 365)
    return response


@app.route("/shutdown", methods=["GET"])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return "Servidor apagado correctamente."


if __name__ == "__main__":
    create_desktop_shortcut()
    Timer(1, open_browser).start()
    app.run(host="127.0.0.1", port=5001, debug=False)
