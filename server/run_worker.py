"""Este script inicia un worker de Celery que se conecta a un broker Redis con autenticación."""
import os

from celery import Celery


# Iniciar el worker
if __name__ == '__main__':
    password = os.getenv("REDIS_PASSWORD")

    app = Celery('tasks',
                 broker=f'redis://:{password}@localhost:6379/0',
                 backend=f'redis://:{password}@localhost:6379/0'
                 )

    app.start()
