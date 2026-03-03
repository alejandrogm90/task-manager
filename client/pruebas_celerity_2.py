"""Este script se conecta a un broker Redis con autenticación y envía tareas a Celery 
para ejecutar scripts específicos en el servidor. Asegúrate de que la variable de entorno 
REDIS_PASSWORD esté configurada correctamente antes de ejecutar este script."""

from tasks import ejecutar_script


if __name__ == "__main__":
    # Lista de scripts a enviar
    scripts = [
        "/home/xel/bin/cpu-info-2.sh",
        "/home/xel/bin/cpu-info-2.sh",
        # "/ruta/a/tus/scripts/script2.sh",
        # "/ruta/a/tus/scripts/script3.sh",
    ]

    try:
        # Enviar las tareas
        for script in scripts:
            result = ejecutar_script(script)
            print(f"Resultado de ejecutar {script}:\n{result}")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
