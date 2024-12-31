from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Funciones para crear estructuras
def crear_estructura_peliculas(ruta_base, nombre_pelicula):
    ruta_pelicula = os.path.join(ruta_base, nombre_pelicula)
    os.makedirs(ruta_pelicula, exist_ok=True)
    os.makedirs(os.path.join(ruta_pelicula, "Extras"), exist_ok=True)

def crear_estructura_series(ruta_base, nombre_serie, temporadas):
    ruta_serie = os.path.join(ruta_base, nombre_serie)
    os.makedirs(ruta_serie, exist_ok=True)
    for i in range(1, temporadas + 1):
        os.makedirs(os.path.join(ruta_serie, f"Season {i:02}"), exist_ok=True)
    os.makedirs(os.path.join(ruta_serie, "Extras"), exist_ok=True)

def crear_estructura_documentales(ruta_base, nombre_documental):
    ruta_documental = os.path.join(ruta_base, nombre_documental)
    os.makedirs(ruta_documental, exist_ok=True)
    os.makedirs(os.path.join(ruta_documental, "Extras"), exist_ok=True)

# Funciones para agregar carpetas 'Extras'
def agregar_extras(ruta_base):
    carpetas = [f for f in os.listdir(ruta_base) if os.path.isdir(os.path.join(ruta_base, f))]
    for carpeta in carpetas:
        ruta_extras = os.path.join(ruta_base, carpeta, "Extras")
        os.makedirs(ruta_extras, exist_ok=True)

# Renombrar series automáticamente
def renombrar_series_automatico(ruta_base, nombre_serie):
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

@app.route("/")
def index():
    return render_template("index.html")

# Crear estructuras
@app.route("/crear_peliculas", methods=["GET", "POST"])
def crear_peliculas():
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_pelicula = request.form["nombre"]
        crear_estructura_peliculas(ruta_base, nombre_pelicula)
        return redirect(url_for("index"))
    return render_template("crear_peliculas.html")

@app.route("/crear_series", methods=["GET", "POST"])
def crear_series():
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_serie = request.form["nombre"]
        temporadas = int(request.form["temporadas"])
        crear_estructura_series(ruta_base, nombre_serie, temporadas)
        return redirect(url_for("index"))
    return render_template("crear_series.html")

@app.route("/crear_documentales", methods=["GET", "POST"])
def crear_documentales():
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_documental = request.form["nombre"]
        crear_estructura_documentales(ruta_base, nombre_documental)
        return redirect(url_for("index"))
    return render_template("crear_documentales.html")

# Añadir carpetas 'Extras'
@app.route("/agregar_extras", methods=["GET", "POST"])
def agregar_extras_view():
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        agregar_extras(ruta_base)
        return redirect(url_for("index"))
    return render_template("agregar_extras.html")

# Renombrar series automáticamente
@app.route("/renombrar_series", methods=["GET", "POST"])
def renombrar_series():
    if request.method == "POST":
        ruta_base = request.form["ruta"]
        nombre_serie = request.form["nombre"]
        mensaje = renombrar_series_automatico(ruta_base, nombre_serie)
        return render_template("mensaje.html", mensaje=mensaje)
    return render_template("renombrar_series.html")

# Información
@app.route("/info")
def info():
    info_text = """
    === Información sobre el formato de carpetas ===
    /Movies/
      /Movie Title (Year)/
        /Extras/
    /TV Shows/
      /TV Show Title/
        /Season XX/
          TV Show Title - SXXEXX - Episode Title.ext
        /Extras/
    /Documentaries/
      /Documentary Title (Year)/
        /Extras/
    """
    return render_template("info.html", info=info_text)

if __name__ == "__main__":
    app.run(debug=True)
