"""Este script inicia un worker de Celery que se conecta a un broker Redis con autenticación."""
import os

from celery import Celery


def make_celery():
    """Crea una instancia de Celery"""
    # Variables
    host_pi = os.getenv("HOST_PI","0.0.0.0")
    redis_password = os.getenv("REDIS_PASSWORD", "redisredis")
    port_out = int(os.getenv("PORT_OUT", 6379))
    tasks_name = os.getenv("TASKS_NAME", 'tasks')

    # Inicializar la aplicación Celery
    broker = f'redis://:{redis_password}@{host_pi}:{port_out}/0'
    backend = f'redis://:{redis_password}@{host_pi}:{port_out}/0'

    return Celery(tasks_name, broker=broker, backend=backend)


app = make_celery()

if __name__ == '__main__':
    # Iniciar el worker
    app.start()
