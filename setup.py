import os
import sys
import subprocess
import webbrowser
from threading import Timer
import platform
from win32com.client import Dispatch  # Para crear accesos directos en Windows

# Configuración del entorno de Flask
os.environ.setdefault("FLASK_APP", "app.py")  # Nombre del archivo Flask principal
os.environ.setdefault("FLASK_ENV", "production")  # Cambiar a 'development' para ver errores detallados

# Ajustar rutas dinámicas si se ejecuta empaquetado
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(os.path.abspath(__file__))

def open_browser():
    """
    Abre automáticamente el navegador predeterminado en la URL del servidor Flask.
    """
    try:
        url = "http://127.0.0.1:5000/"
        webbrowser.open(url)
        print(f"Navegador abierto en {url}")
    except Exception as e:
        print(f"Error al abrir el navegador: {e}")

def create_desktop_shortcut():
    """
    Crea un acceso directo en el escritorio para ejecutar la aplicación.
    """
    try:
        desktop = os.path.join(os.path.join(os.environ["USERPROFILE"]), "Desktop")  # Ruta al escritorio
        shortcut_path = os.path.join(desktop, "Renombrador Plex.lnk")

        # Si se empaquetó con PyInstaller, usar el ejecutable directamente
        if getattr(sys, 'frozen', False):
            target_path = sys.executable  # Ejecutable generado por PyInstaller
        else:
            target_path = os.path.abspath(sys.argv[0])  # Ruta del script actual

        icon_path = os.path.join(base_path, "static", "icons", "palomitera.ico")

        if os.path.exists(shortcut_path):
            print("El acceso directo ya existe en el escritorio.")
            return

        # Crear el acceso directo
        shell = Dispatch("WScript.Shell")
        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = target_path
        shortcut.WorkingDirectory = os.path.dirname(target_path)
        shortcut.Arguments = ""  # Sin argumentos adicionales
        shortcut.IconLocation = icon_path if os.path.exists(icon_path) else ""
        shortcut.WindowStyle = 7  # Ejecutar minimizado (ocultar ventana)
        shortcut.save()

        print(f"Acceso directo creado en el escritorio: {shortcut_path}")
    except Exception as e:
        print(f"Error al crear el acceso directo: {e}")

def run_flask_app():
    """
    Ejecuta el servidor Flask de manera multiplataforma.
    """
    try:
        flask_command = ["flask", "run", "--host=127.0.0.1", "--port=5000"]

        if platform.system() == "Windows":
            # Ejecutar en Windows con consola oculta
            subprocess.Popen(
                flask_command,
                creationflags=subprocess.CREATE_NO_WINDOW,
                stdout=subprocess.DEVNULL if os.environ["FLASK_ENV"] == "production" else None,
                stderr=subprocess.DEVNULL if os.environ["FLASK_ENV"] == "production" else None,
            )
        else:
            # Ejecutar en Linux/Mac
            subprocess.Popen(
                flask_command,
                stdout=subprocess.DEVNULL if os.environ["FLASK_ENV"] == "production" else None,
                stderr=subprocess.DEVNULL if os.environ["FLASK_ENV"] == "production" else None,
            )
        print("Servidor Flask iniciado correctamente.")
    except FileNotFoundError:
        print("Error: Flask no está instalado o no se encuentra en el PATH.")
        exit(1)
    except Exception as e:
        print(f"Error inesperado al ejecutar Flask: {e}")
        exit(1)

if __name__ == "__main__":
    # Crear el acceso directo en el escritorio
    create_desktop_shortcut()

    # Abrir el navegador después de 1 segundo para que Flask inicie correctamente
    Timer(1, open_browser).start()

    # Ejecutar el servidor Flask
    run_flask_app()
