from flask import Flask, render_template, request

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

    # Faça o que quiser com os dados do formulário
    # Neste exemplo, estamos apenas imprimindo-os
    print(f"Nome: {nome}")
    print(f"E-mail: {email}")
    print(f"Idade: {idade}")
    print(f"Escola: {escola}")

    return "Dados do formulário recebidos com sucesso!"

if __name__ == '__main__':
    app.run()
