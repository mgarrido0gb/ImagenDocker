from json import JSONDecodeError
import json
from re import template
import string
import redis
import time
from flask import jsonify , request
from users import users
from flask_restplus import Namespace , Resource


cache = redis.Redis(host='redis', port=6379)
ruta_detectada = Namespace('ruta_detectada',description='Rutas detectadas')

def get_hit_count():
    retries =5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -=1
            time.sleep(0.5)


#JSON , RETORNAREMOS EL OBJETO
#MÉTODO GET , RETORNAMOS LISTADO
@ruta_detectada.route("/usuarios",methods=['GET'])
class usuarios(Resource):
    def get(self):
        return jsonify({"Usuarios":users})


#METODO GET , RETORNAMOS USUARIO SEGÚN NOMBRE
@ruta_detectada.route('/usuariosNombre/<string:nombre>',methods=['GET'])
class usuariosNombre(Resource):
    def get(self,nombre):
     usersFound=[user for user in users if user['nombre'] == nombre]
     if (len(usersFound)>0):
         return jsonify({"Usuario":usersFound[0]})
     return jsonify({"msg":"Usuario no existe"})
 
#MÉTODO POST creamos una coleccion dentro en nuestro json
@ruta_detectada.route("/usuariosPost",methods=["POST"])
class usuariosPost(Resource):
    def post(self):
         #creamos el usuario
        new_usuario = {
            "nombre": request.form['nombre'],
            "correo": request.form['correo'],
            "telefono": request.form['telefono']
        }
    #agregar nuevo dato
        users.append(new_usuario)
        return jsonify({"msg":"Usuario agregado existosamente", "user":users})


#MÉTODO PUT
@ruta_detectada.route("/usuariosPut/<string:nombre>",methods=["PUT"])
class usuariosPut(Resource):
    def put(self,nombre):
        usersFound=[user for user in users if user['nombre'] == nombre]
        #si el usuario es encontrado
        if (len(usersFound)>0):
            usersFound[0]['nombre']= request.json['nombre']
            usersFound[0]['correo']= request.json['correo']
            usersFound[0]['telefono']= request.json['telefono']
            return jsonify({
                "msg":"Usuario actualizado",
                "user": usersFound[0]
            })
        return jsonify({"msg":"Usuario no encontrado"})



#MÉTODO DELETE
@ruta_detectada.route("/usuarios/<string:nombre>",methods=["DELETE"])
class usuariosDelete(Resource):
    def delete(self,nombre):
        usersFound=[user for user in users if user['nombre'] == nombre]
        if len(usersFound)>0:
            users.remove(usersFound[0])
            return jsonify({
                "msg":"Usuario Eliminado",
                "users":users
                })
        return jsonify({"msg":"Usuario no ncontrado"})
    
 
