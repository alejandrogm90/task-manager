"""Este módulo define las tareas que se ejecutarán en el servidor utilizando Celery."""
import os
import subprocess

from celery import Celery


# Configurar la conexión a tu broker Redis con autenticación
password = os.getenv("REDIS_PASSWORD")
app = Celery('tasks',
             broker=f'redis://:{password}@localhost:6379/0',
             backend=f'redis://:{password}@localhost:6379/0'
             )


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
