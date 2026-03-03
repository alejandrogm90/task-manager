"""Este script se conecta a un broker Redis con autenticación para verificar la conexión."""
import os
import redis


if __name__ == "__main__":
    # Variables
    HOST_PI = os.getenv("HOST_PI")
    PASSWORD = os.getenv("REDIS_PASSWORD")

    # Conectar a Redis
    client = redis.StrictRedis(
        host=HOST_PI, port=6379, decode_responses=True, password=PASSWORD)

    try:
        if client.ping():
            print("Conexión exitosa a Redis!")
    except redis.ConnectionError as e:
        print("No se puede conectar a Redis:", str(e))
