"""Este script inicia un worker de Celery que se conecta a un broker Redis con autenticación."""
import os

from celery import Celery


def make_celery():
    """Crea una instancia de Celery"""
    redis_password = os.getenv("REDIS_PASSWORD")
    return Celery('tasks', broker=f'redis://:{redis_password}@localhost:6379/0',
                  backend=f'redis://:{redis_password}@localhost:6379/0')


app = make_celery()

if __name__ == '__main__':
    # Iniciar el worker
    app.start()
