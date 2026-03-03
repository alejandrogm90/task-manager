"""Este módulo define las tareas que se ejecutarán en el servidor a través de Celery."""
import os
import subprocess

from celery import Celery


# Variables
PASSWORD = os.getenv("REDIS_PASSWORD")

# Inicializar la aplicación Celery
app = Celery('tasks', broker=f'redis://:{PASSWORD}@localhost:6379/0',
             backend=f'redis://:{PASSWORD}@localhost:6379/0')


@app.task
def ejecutar_script(script):
    """Ejecuta un script de shell y devuelve su salida."""
    result = subprocess.run(
        ['bash', script], capture_output=True, text=True, check=False)
    return result.stdout


@app.task
def ejecutar_script_python(script):
    """Ejecuta un script de Python y devuelve su salida."""
    result = subprocess.run(
        ['python3', script], capture_output=True, text=True, check=False)
    return result.stdout
