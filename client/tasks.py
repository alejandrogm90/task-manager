"""Este módulo define las tareas que se ejecutarán en el servidor a través de Celery."""
import os
import subprocess

from celery import Celery


# Variables
HOST_PI = os.getenv("HOST_PI", "0.0.0.0")
PASSWORD = os.getenv("REDIS_PASSWORD", "redisredis")
PORT_OUT = int(os.getenv("PORT_OUT", 6380))
TASKS_NAME = os.getenv("TASKS_NAME", 'tasks')

# Inicializar la aplicación Celery
broker=f'redis://:{PASSWORD}@{HOST_PI}:{PORT_OUT}/0'
backend=f'redis://:{PASSWORD}@{HOST_PI}:{PORT_OUT}/0'
app = Celery(TASKS_NAME, broker=broker, backend=backend)


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
