import os
import subprocess
import webbrowser
from threading import Timer
import platform

# Configuración del entorno de Flask
os.environ["FLASK_APP"] = "app.py"  # Nombre del archivo Flask principal
os.environ["FLASK_ENV"] = "production"  # Cambiar a 'development' para ver errores detallados

def open_browser():
    """Abre automáticamente el navegador predeterminado en la URL del servidor Flask."""
    try:
        webbrowser.open("http://127.0.0.1:5000/")
    except Exception as e:
        print(f"Error al abrir el navegador: {e}")

def run_flask_app():
    """Ejecuta el servidor Flask."""
    try:
        if platform.system() == "Windows":
            # Ejecutar en Windows con consola oculta
            subprocess.Popen(
                ["flask", "run"],
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=None if os.environ["FLASK_ENV"] == "development" else subprocess.DEVNULL,
                stderr=None if os.environ["FLASK_ENV"] == "development" else subprocess.DEVNULL,
            )
        else:
            # Ejecutar en Linux/Mac
            subprocess.Popen(
                ["flask", "run"],
                stdout=None if os.environ["FLASK_ENV"] == "development" else subprocess.DEVNULL,
                stderr=None if os.environ["FLASK_ENV"] == "development" else subprocess.DEVNULL,
            )
    except FileNotFoundError:
        print("Error: Flask no está instalado o no se encuentra en el PATH.")
        exit(1)
    except Exception as e:
        print(f"Error inesperado al ejecutar Flask: {e}")
        exit(1)

if __name__ == "__main__":
    # Abrir el navegador después de 1 segundo para que Flask inicie correctamente
    Timer(1, open_browser).start()

    # Ejecutar el servidor Flask
    run_flask_app()
