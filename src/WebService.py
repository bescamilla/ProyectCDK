#!/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_class():
    return 'Hellow class!'

@app.route('/saludo/<persona>')
def saludodinamico(persona):
    return 'Hellow %s, bienvenido ' % persona

@app.route('/cuadrado/<int:num>')
def calculacuadrado(num):
    resp = num * num
    return 'Respuesta: %f' % resp

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)
