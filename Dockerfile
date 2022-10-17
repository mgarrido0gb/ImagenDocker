FROM alpine:3.10

#Instalando Python y PIP Última versión
RUN apk add --no-cache python3-dev \
    && pip3 install --upgrade pip

#CREAR CARPETA LLAMADA APP
WORKDIR /app
COPY . /app

#CONFIGURAR VARIABLES NECESARIAS FLASK PARA FUNCIONAR
ENV FLASK_APP app.py

ENV FLASK_RUN_HOST 0.0.0.0

#INSTALAR MODULOS NECESARIOS PARA LA EJECUCIÓN DEL PROYECTO
RUN apk add --no-cache gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

#leer archivos del requeriments.txt e instalarlos
RUN pip install -r requirements.txt

#COPIAR TODO EL DIRECTORIO DEL TRABAJO AL CONTENEDOR
COPY . .

#EJECUTAMOS LA APLICACIÓN
CMD [ "python3","src/app.py" ]