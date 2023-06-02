from flask import Flask, render_template, request , jsonify
import json
from models.config import DB_CONFIG
import mysql.connector


app = Flask(__name__)


# Função para inserir os dados do formulário no banco de dados
def inserir_dados(nome, email, idade, escola):
    connection = mysql.connector.connect(**DB_CONFIG)
    cursor = connection.cursor()

    query = "INSERT INTO usuarios (nome, email, idade, escola) VALUES (%s, %s, %s, %s)"
    values = (nome, email, idade, escola)
    cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()


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
        #return "Os dados não foram enviados"


@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    values = data['values']

    # Contadores de perguntas corretas e total de perguntas
    total_questions = len(values)

    response = {
        'questionsCorrect': values,
        'totalQuestions': total_questions
    }  
    print(json.dumps(response, indent=4))

    return jsonify(response)


if __name__ == '__main__':
    app.run()
