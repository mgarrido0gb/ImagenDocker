from re import template
from flask import Flask , jsonify , render_template
from users import users

app = Flask(__name__)

@app.route('/',methods=['GET'])
def ping():
    return jsonify({"response":"Hola Mundo"})

@app.route('/index')
def index():
    return render_template('/index.html')

@app.route('/users')
def userHandler():
    return jsonify({"users":users})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=4000,debug=True)


