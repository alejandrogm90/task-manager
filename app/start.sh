#!/bin/bash

# Iniciar Redis en segundo plano
redis-server --requirepass redisredis --bind 0.0.0.0 &

# Esperar hasta que Redis esté disponible
while ! nc -z 0.0.0.0 6379; do
  sleep 1 # Esperar un segundo
done

# Establecer la variable de entorno para la URL del broker
export CELERY_BROKER_URL=redis://:redisredis@0.0.0.0:6379/0

# Iniciar Celery con la contraseña adecuada en la URL del broker
celery -A tasks worker --loglevel=info
