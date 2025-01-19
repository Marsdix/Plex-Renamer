from flask import Flask, render_template, request
import os
import signal
import sys
import logging  # Para manejo de logs
from threading import Timer  # Para abrir el navegador automáticamente
import webbrowser  # Para manejar el navegador automáticamente
from win32com.client import Dispatch  # Para crear accesos directos en Windows

# Configuración de registros
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

# Ajustar rutas dinámicas si se ejecuta empaquetado
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS  # Ruta temporal creada por PyInstaller
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

template_folder = os.path.join(base_path, "templates")
static_folder = os.path.join(base_path, "static")

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder)

# Función para abrir automáticamente el navegador
def open_browser():
    """
    Abre automáticamente el navegador en la dirección del servidor Flask.
    """
    webbrowser.open_new("http://127.0.0.1:5000/")

# Función para crear acceso directo en el escritorio
def create_desktop_shortcut():
    """
    Crea un acceso directo en el escritorio si no existe.
    """
    try:
        desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")  # Ruta al escritorio
        shortcut_path = os.path.join(desktop, "Renombrador Plex.lnk")
        target_path = os.path.abspath(sys.argv[0])  # Ruta del script actual o ejecutable
        icon_path = os.path.join(static_folder, "icons", "palomitera.ico")

        # Comprobar si ya existe el acceso directo
        if os.path.exists(shortcut_path):
            logger.info("El acceso directo ya existe.")
            return

        # Crear el acceso directo
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = sys.executable  # Ruta del ejecutable de Python o .exe
        shortcut.Arguments = f'"{target_path}"'  # Pasa el archivo como argumento
        shortcut.WorkingDirectory = os.path.dirname(target_path)
        shortcut.IconLocation = icon_path if os.path.exists(icon_path) else ""
        shortcut.save()

        logger.info(f"Acceso directo creado: {shortcut_path}")
    except Exception as e:
        logger.error(f"Error al crear el acceso directo: {e}")

# Función genérica para manejar errores
def manejar_error(mensaje, error):
    logger.error(f"{mensaje}: {error}")
    return f"{mensaje}: {error}"

# Funciones para crear estructuras
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

# Funciones para agregar carpetas 'Extras'
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

# Renombrar series automáticamente
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

@app.route("/")
def index():
    return render_template("index.html")

# Crear películas
@app.route("/crear_peliculas", methods=["GET", "POST"])
def crear_peliculas():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_pelicula = request.form["nombre"]
        mensaje = crear_estructura_peliculas(ruta_base, nombre_pelicula)
    return render_template("crear_peliculas.html", mensaje=mensaje)

# Crear series
@app.route("/crear_series", methods=["GET", "POST"])
def crear_series():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_serie = request.form["nombre"]
        temporadas = int(request.form["temporadas"])
        mensaje = crear_estructura_series(ruta_base, nombre_serie, temporadas)
    return render_template("crear_series.html", mensaje=mensaje)

# Crear documentales
@app.route("/crear_documentales", methods=["GET", "POST"])
def crear_documentales():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_documental = request.form["nombre"]
        mensaje = crear_estructura_documentales(ruta_base, nombre_documental)
    return render_template("crear_documentales.html", mensaje=mensaje)

# Añadir carpetas 'Extras'
@app.route("/agregar_extras", methods=["GET", "POST"])
def agregar_extras_view():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        mensaje = agregar_extras(ruta_base)
    return render_template("agregar_extras.html", mensaje=mensaje)

# Renombrar series automáticamente
@app.route("/renombrar_series", methods=["GET", "POST"])
def renombrar_series():
    mensaje = None
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_serie = request.form["nombre"]
        mensaje = renombrar_series_automatico(ruta_base, nombre_serie)
    return render_template("renombrar_series.html", mensaje=mensaje)

# Información
@app.route("/info")
def info():
    return render_template("info.html")

# Cerrar Flask con os.kill
@app.route("/shutdown", methods=["GET"])
def shutdown():
    os.kill(os.getpid(), signal.SIGINT)
    return "Servidor apagado correctamente."

if __name__ == "__main__":
    # Crear acceso directo si no existe
    create_desktop_shortcut()

    # Abrir navegador automáticamente después de iniciar el servidor Flask
    Timer(1, open_browser).start()

    # Ejecutar la aplicación Flask
    app.run(debug=False)
