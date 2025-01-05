from flask import Flask, render_template, request
import os
import signal
import sys

app = Flask(__name__)

# Funciones para crear estructuras
def crear_estructura_peliculas(ruta_base, nombre_pelicula):
    try:
        ruta_pelicula = os.path.join(ruta_base, nombre_pelicula)
        os.makedirs(ruta_pelicula, exist_ok=True)
        os.makedirs(os.path.join(ruta_pelicula, "Extras"), exist_ok=True)
        return f"Película '{nombre_pelicula}' creada con éxito en '{ruta_base}'."
    except Exception as e:
        return f"Error al crear la película: {str(e)}"

def crear_estructura_series(ruta_base, nombre_serie, temporadas):
    try:
        ruta_serie = os.path.join(ruta_base, nombre_serie)
        os.makedirs(ruta_serie, exist_ok=True)
        for i in range(1, temporadas + 1):
            os.makedirs(os.path.join(ruta_serie, f"Season {i:02}"), exist_ok=True)
        os.makedirs(os.path.join(ruta_serie, "Extras"), exist_ok=True)
        return f"Serie '{nombre_serie}' creada con éxito en '{ruta_base}' con {temporadas} temporadas."
    except Exception as e:
        return f"Error al crear la serie: {str(e)}"

def crear_estructura_documentales(ruta_base, nombre_documental):
    try:
        ruta_documental = os.path.join(ruta_base, nombre_documental)
        os.makedirs(ruta_documental, exist_ok=True)
        os.makedirs(os.path.join(ruta_documental, "Extras"), exist_ok=True)
        return f"Documental '{nombre_documental}' creado con éxito en '{ruta_base}'."
    except Exception as e:
        return f"Error al crear el documental: {str(e)}"

# Funciones para agregar carpetas 'Extras'
def agregar_extras(ruta_base):
    try:
        carpetas = [f for f in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, f))]
        for carpeta in carpetas:
            ruta_extras = os.path.join(ruta_base, carpeta, "Extras")
            os.makedirs(ruta_extras, exist_ok=True)
        return f"Carpetas 'Extras' añadidas con éxito en todas las carpetas de '{ruta_base}'."
    except Exception as e:
        return f"Error al agregar carpetas 'Extras': {str(e)}"

# Renombrar series automáticamente
def renombrar_series_automatico(ruta_base, nombre_serie):
    try:
        carpetas = [f for f in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, f)) and f.startswith("Season")]
        if not carpetas:
            return "No se encontraron carpetas de temporadas en el formato 'Season XX'."

        carpetas.sort()
        for carpeta in carpetas:
            temporada = carpeta.split(" ")[1]
            ruta_temporada = os.path.join(ruta_base, carpeta)
            archivos = sorted(os.listdir(ruta_temporada))
            contador = 1
            for archivo in archivos:
                ruta_completa = os.path.join(ruta_temporada, archivo)
                if os.path.isdir(ruta_completa):
                    continue
                extension = os.path.splitext(archivo)[1]
                numero_episodio = f"E{contador:02}"
                nuevo_nombre = f"{nombre_serie} - S{temporada}{numero_episodio}{extension}"
                ruta_nueva = os.path.join(ruta_temporada, nuevo_nombre)
                os.rename(ruta_completa, ruta_nueva)
                contador += 1
        return f"Renombrado automático completo para la serie '{nombre_serie}'."
    except Exception as e:
        return f"Error al renombrar la serie: {str(e)}"

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
    app.run(debug=True)
