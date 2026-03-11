"""Este script se conecta a un broker Redis con autenticación, obtiene el estado de una tarea 
de Celery utilizando su ID y muestra el resultado si la tarea ha finalizado."""
import os
import sys

from celery.result import AsyncResult
from celery import Celery


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python get_task_info.py <task_id>")
        sys.exit(1)

    # Variables
    HOST_PI = os.getenv("HOST_PI", "0.0.0.0")
    PASSWORD = os.getenv("REDIS_PASSWORD", "redisredis")
    PORT_OUT = int(os.getenv("PORT_OUT", 6380))
    TASKS_NAME = os.getenv("TASKS_NAME", 'tasks')

    # Configura la conexión a tu broker Redis con autenticación
    broker = f'redis://:{PASSWORD}@{HOST_PI}:{PORT_OUT}/0',
    backend = f'redis://:{PASSWORD}@{HOST_PI}:{PORT_OUT}/0'
    app = Celery(TASKS_NAME, broker=broker, backend=backend)

    # ID de la tarea
    task_id = sys.argv[1]

    # Obtener el resultado de la tarea
    result = AsyncResult(task_id, app=app)

    if result.ready():
        # La tarea ha finalizado
        if result.successful():
            # Obtener el resultado de la tarea
            output = result.result
            print(f"Resultado: {output}")
        else:
            # La tarea falló, puedes ver el motivo
            print(f"La tarea falló con el error: {result.result}")
    else:
        print("La tarea aún no ha finalizado.")
