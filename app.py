
import redis
import time
from flask import Flask 
from users import users
from flask_restplus import Api
from routes.rutas import ruta_detectada

app = Flask(__name__)
api = Api(app)

api.add_namespace(ruta_detectada,path='/rutas')






if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)


