# Usa la imagen oficial de Python
FROM python:3.9-slim

# Copia el archivo Python al contenedor
COPY index.py /app/index.py

# Establece el directorio de trabajo
WORKDIR /app

# Expone el puerto 8000 para acceso externo
EXPOSE 8000

# Ejecuta el servidor al iniciar el contenedor
CMD ["python", "index.py"]