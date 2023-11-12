# Importamos librería/modulos
from flask import Flask, request

# Contruimos la App
app = Flask(__name__)

# Creamos las rutas

@app.route("/welcome")
def welcome():
    return "Bienvenid@s sean"

@app.route("/")
def principal():
    return "Pagina principal"

@app.route('/method', methods=['GET','POST'])
def method():
    if request.method=='POST':
        return 'Estas usando el metodo POST'
    else:
        return 'Talvez estes usando un metodo GET'

# Correr el programa
app.run()