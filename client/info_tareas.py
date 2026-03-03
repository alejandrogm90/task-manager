"""Este script se conecta a un broker Redis con autenticación, obtiene el estado de una tarea 
de Celery utilizando su ID y muestra el resultado si la tarea ha finalizado."""
import os
import sys

from celery.result import AsyncResult
from celery import Celery


if __name__ == "__main__":
    if not os.getenv("REDIS_PASSWORD"):
        print("Error: La variable de entorno REDIS_PASSWORD no está configurada.")
        sys.exit(1)
    if len(sys.argv) != 2:
        print("Uso: python get_task_info.py <task_id>")
        sys.exit(2)

    # Configura la conexión a tu broker Redis con autenticación
    password = os.getenv("REDIS_PASSWORD")
    app = Celery('tasks',
                 broker=f'redis://:{password}@localhost:6379/0',
                 backend=f'redis://:{password}@localhost:6379/0')

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
