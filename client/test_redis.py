"""Este script se conecta a un broker Redis con autenticación para verificar la conexión."""
import os
import redis


if __name__ == "__main__":
    # Variables
    HOST_PI = os.getenv("HOST_PI", "0.0.0.0")
    PASSWORD = os.getenv("REDIS_PASSWORD", "redisredis")
    PORT_OUT = int(os.getenv("PORT_OUT", 6380))

    # Conectar a Redis
    client = redis.StrictRedis(
        host=HOST_PI,
        port=PORT_OUT,
        password=PASSWORD,
        decode_responses=True,
    )

    try:
        if client.ping():
            print("Conexión exitosa a Redis!")
    except redis.ConnectionError as e:
        print("No se puede conectar a Redis:", str(e))
