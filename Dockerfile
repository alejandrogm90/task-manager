# Usar una imagen base de Ubuntu
FROM ubuntu:20.04

# Instalar dependencias necesarias
RUN apt-get update

# Configurar tzdata sin interacción
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y tzdata && \
    ln -fs /usr/share/zoneinfo/Etc/UTC /etc/localtime && \
    dpkg-reconfigure -f noninteractive tzdata

# Instalar python3 básicos
RUN apt-get install -y \
    python3 \
    python3-pip \
    python3-setuptools \
    redis-server \
    netcat \
    && apt-get clean

# Crear un directorio de trabajo
WORKDIR /app

# Copiar archivos de la aplicación
COPY app/ ./
#COPY server/ ./

# Instalar dependencias
RUN pip3 install --no-cache-dir -r requirements.txt

# Copiar el script de entrada
RUN chmod +x /app/start.sh

# Especificar el script por defecto
CMD ["/app/start.sh"]
