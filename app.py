from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)


# Configurações do banco de dados
db_config = {
    'host': 'aws.connect.psdb.cloud',
    'user': 'jqckc3sb8ggvblsykkhp',
    'password': 'pscale_pw_Tef8Ao7JbElGKRJF5OHHqEvaVFocf0X1VjLmGmBIC2D',
    'database': 'vocacional-tech'
}

# Função para inserir os dados do formulário no banco de dados
def inserir_dados(nome, email, idade, escola):
    connection = mysql.connector.connect(**db_config)
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
        return "Dados do formulário recebidos com sucesso!"
    except:
        return "Os dados não foram enviados"

if __name__ == '__main__':
    app.run()
