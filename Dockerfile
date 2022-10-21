FROM python:3.7.0-slim

ENV TZ=America/Santiago
#Instalando Python y PIP Última versión

#CREAR CARPETA LLAMADA APP
WORKDIR /app
COPY . /app



#leer archivos del requeriments.txt e instalarlos
RUN pip install -r requirements.txt



#EJECUTAMOS LA APLICACIÓN
CMD ["gunicorn", "app:app",  "-w 8", "-t 3600", "-b", "0.0.0.0:4000"]