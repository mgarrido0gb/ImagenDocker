FROM python:3.7.0-slim

ENV TZ=America/Santiago
#Instalando Python y PIP Última versión

#CREAR CARPETA LLAMADA APP
WORKDIR /app
COPY . /app


RUN  pip install --upgrade pip
#leer archivos del requeriments.txt e instalarlos
RUN pip install -r requirements.txt



#EJECUTAMOS LA APLICACIÓN"
CMD ["python","app.py"]