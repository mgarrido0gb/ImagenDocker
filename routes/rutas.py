
from json import JSONDecodeError
import json
from re import template
import redis
import time
from flask import Flask , jsonify , render_template , make_response , request
from users import users
from flask_restplus import Api , Namespace


cache = redis.Redis(host='redis', port=6379)
ruta_detectada = Namespace('routes/rutas')

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
@ruta_detectada.route("/json")
def get_json():
    return jsonify({"Usuarios":users})

#METODO GET , RETORNAMOS USUARIO SEGÚN NOMBRE
@ruta_detectada.route('/usuarios/<string:nombre>')
def getUsers(nombre):
    usersFound=[user for user in users if user['nombre'] == nombre]
    if (len(usersFound)>0):
        return jsonify({"Usuario":usersFound[0]})
    return jsonify({"msg":"Usuario no existe"})


#MÉTODO POST creamos una coleccion dentro en nuestro json
@ruta_detectada.route("/usuarios",methods=["POST"])
def create_users():
    #creamos el usuario
    new_usuario = {
        "nombre": request.json['nombre'],
        "correo": request.json['correo'],
        "telefono": request.json['telefono']
    }
    #agregar nuevo dato
    users.append(new_usuario)
    return jsonify({"msg":"Usuario agregado existosamente", "user":users})


#MÉTODO PUT
@ruta_detectada.route("/usuarios/<string:nombre>",methods=["PUT"])
def edit_user(nombre):
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
def delete_user(nombre):
    usersFound=[user for user in users if user['nombre'] == nombre]
    if len(usersFound)>0:
        users.remove(usersFound[0])
        return jsonify({
            "msg":"Usuario Eliminado",
            "users":users
        })
    return jsonify({"msg":"Usuario no ncontrado"}
                   )
@ruta_detectada.route('/temp')
def template():
    return render_template('/index.html')

@ruta_detectada.route('/')
def home():
    return "<h1 style='color:blue'>Home!</h1>"



@ruta_detectada.route('/users')
def userHandler():
    return jsonify({"users":users})


if __name__ == '__main__':
    ruta_detectada.run(host="0.0.0.0",port=4000,debug=True)
