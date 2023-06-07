from flask import Flask, render_template, request , jsonify
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
        return "dados não recebidos"



@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    values = data['values']
    print(values)

    result = realizar_teste(values)


    print(result)

    return values
    
    """if(values == "analista"):
        return render_template('profissoes/analista.html')

    if(values == "back"):
        return render_template('profissoes/back.html')

    if(values == "dados"):
        return render_template('profissoes/dados.html')

    if(values == "engenheiro"):
        return render_template('profissoes/engenheiro.html')

    if(values == "front"):
        return render_template('profissoes/front.html')

    if(values == "back"):
        return render_template('profissoes/back.html')"""
    



if __name__ == '__main__':
    app.run()
