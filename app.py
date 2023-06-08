from flask import Flask, render_template, request , jsonify , redirect, url_for
import json
from control.test import realizar_teste
from control.crud import inserir_dados


app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario', methods=['POST'])
def formulario():
    nome = request.form['nome']
    email = request.form['email']
    idade = request.form['idade']
    escola = request.form['escola']

    try:
        inserir_dados(nome , email , idade , escola)
        return render_template('questionario.html')
    except:
        return render_template('questionario.html')



@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    values = data['values']

    result = realizar_teste(values)


    print(values , result)

    return jsonify(result=result)



@app.route('/resultado/<result>')
def resultado(result):
    return render_template('resultado.html', result=result)

if __name__ == '__main__':
    app.run()
