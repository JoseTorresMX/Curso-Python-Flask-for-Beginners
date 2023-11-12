#Importamos librería/modulos
from flask import Flask

#Contruimos la App
app=Flask(__name__)

#Creamos las rutas
@app.route("/welcome")
def welcome():
    return "Bienvenid@s sean"

@app.route("/")
def principal():
    return "Pagina principal"

#Correr el programa
app.run()