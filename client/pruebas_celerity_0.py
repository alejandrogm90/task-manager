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
    HOST_PI = os.getenv("HOST_PI", "0.0.0.0")
    PASSWORD = os.getenv("REDIS_PASSWORD", "redisredis")
    PORT_OUT = int(os.getenv("PORT_OUT", 6380))
    TASKS_NAME = os.getenv("TASKS_NAME", 'tasks')

    # Configura la conexión a tu broker Redis
    app = Celery(TASKS_NAME, broker=f'redis://:{PASSWORD}@{HOST_PI}:{PORT_OUT}/0')

    # Lista de scripts a enviar
    scripts = [
        "/app/hello.sh param1 param2 param3 3",
    ]

    try:
        # Enviar las tareas
        for script in scripts:
            enviar_tarea(app, script)
    except Exception as e:
        print(f"Ocurrió un error: {e}")
