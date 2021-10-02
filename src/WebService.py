
#!/bin/python3

from flask import Flask, request
import controller

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

@app.route('/rlineal', methods=['POST'])
def preRLineal():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        vx = data['vx']
        vy = data['vy']
        x = data['x']
        return controller.getRLineal(vx, vy, x)
    else:
        return 'URL Incorrecta'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=True)

