"""Este script se conecta a un broker Redis con autenticación y envía tareas a Celery 
para ejecutar scripts específicos en el servidor. Asegúrate de que la variable de entorno 
REDIS_PASSWORD esté configurada correctamente antes de ejecutar este script."""
import os

from celery import Celery


def enviar_tarea(celery_app: Celery, script_path: str):
    """
    Envía una tarea a Celery para ejecutar un script específico.
    Args:
        celery_app (Celery): La instancia de Celery para enviar la tarea.
        script_path (str): La ruta del script que se desea ejecutar.
    """
    result = celery_app.send_task('tasks.ejecutar_script', args=[script_path])
    print(f"Tarea enviada para: {script_path}, ID de tarea: {result.id}")


if __name__ == "__main__":
    # Variables
    HOST_PI = os.getenv("HOST_PI")
    PASSWORD = os.getenv("REDIS_PASSWORD")

    # Configura la conexión a tu broker Redis
    app = Celery(
        'run_worker', broker=f'redis://:{PASSWORD}@{HOST_PI}:6379/0')

    # Lista de scripts a enviar
    scripts = [
        "/home/xel/bin/cpu-info-2.sh",
        "/home/xel/bin/cpu-info-2.sh",
        # "/ruta/a/tus/scripts/script2.sh",
        # "/ruta/a/tus/scripts/script3.sh",
    ]

    try:
        # Enviar las tareas
        for script in scripts:
            enviar_tarea(app, script)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
