
from re import template
from flask import Flask , jsonify , render_template , make_response , request
from users import users

app = Flask(__name__)

INFO = {
    "persona1":{
        "nombre":"matias",
        "apellido":"figueroa"
    },
    "persona2":{
        "nombre":"juan",
        "apellido":"henriquez"
    }
}


#JSON , RETORNAREMOS EL OBJETO
@app.route("/json")
def get_json():
    res =  make_response(jsonify(INFO),200)
    return res

#MÉTODO PUT
@app.route("/json/<collection>/<persona>",methods=["PUT"])
def update_collection(collection,persona):
    #INSERCION DE DATOS
    req = request.get_json()
    if collection in INFO:
        if persona :
            INFO[collection][persona] = req["new"]
            res = make_response(jsonify({"res":INFO[collection]}),200)
            return res
        res = make_response(jsonify({"error":"Persona no existe"}),400)
        return res
    res = make_response(jsonify({"mensaje":"coleccion creada"}),201)
    return res
    


#MÉTODO POST creamos una coleccion dentro en nuestro json
@app.route("/json/<collection>",methods=["POST"])
def create_collection(collection):
    #INSERCION DE DATOS
    req = request.get_json()
    if collection in INFO:
        res = make_response(jsonify({"error":"la colección existe"}))
        return res
    INFO.update({collection: req})
    
    res = make_response(jsonify({"mensaje":"coleccion creada"}),201)
    return res


#MÉTODO DELETE
@app.route("/json/<collection>",methods=["DELETE"])
def delete_collection(collection):
    if collection in INFO:
        del INFO[collection]
        res = make_response(jsonify(INFO),200)
        return res
    res = make_response(jsonify({"error":"la colección no existe"}),400)
    return res

@app.route('/temp')
def template():
    return render_template('/index.html')

@app.route('/')
def home():
    return "<h1 style='color:blue'>Home!</h1>"



@app.route('/users')
def userHandler():
    return jsonify({"users":users})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)


