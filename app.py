
import redis
import time
from flask import Flask 
from users import users
from flask_restplus import Api
from routes.rutas import ruta_detectada
app = Flask(__name__)
api = Api(app)

api.add_namespace(ruta_detectada,path='routes/rutas')
cache = redis.Redis(host='redis', port=6379)





if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)


