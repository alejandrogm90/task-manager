"""Este script se conecta a un broker Redis con autenticación para verificar la conexión."""
import os
import redis


if __name__ == "__main__":
    password = os.getenv("REDIS_PASSWORD")
    # Conectar a Redis
    client = redis.StrictRedis(
        host='192.168.1.200', port=6379, decode_responses=True, password=password)

    try:
        if client.ping():
            print("Conexión exitosa a Redis!")
    except redis.ConnectionError as e:
        print("No se puede conectar a Redis:", str(e))
