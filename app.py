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
    descricao = ""
    imagem = ""
    link= ""

    if (result == "back"):
        descricao = "Um profissional especializado em desenvolvimento de software e sistemas que trabalha principalmente na parte do servidor, lidando com a lógica de negócios, bancos de dados e integração de sistemas"
        imagem = "back.svg"
    elif (result == "front"):
        descricao = "Um profissional especializado em desenvolvimento de interfaces de usuário, que se concentra na criação da parte visual e interativa de um aplicativo ou site, utilizando tecnologias como HTML, CSS e JavaScript"
        imagem = "front.svg"
    elif (result == "full"):
        descricao = "Um profissional versátil que possui habilidades tanto no desenvolvimento back-end quanto front-end. Eles têm conhecimento em várias tecnologias e podem lidar com todas as camadas de um aplicativo ou site"
        imagem = "full.svg"
    elif (result == "dados"):
        descricao = "Um profissional que trabalha com análise e interpretação de grandes volumes de dados. Eles aplicam técnicas estatísticas e algoritmos para extrair informações valiosas e insights a partir dos dados, ajudando a tomar decisões informadas"
        imagem = "dados.svg"
    elif (result == "analista"):
        descricao = "Um profissional que atua na análise e resolução de problemas relacionados a sistemas de informação. Eles investigam os requisitos do sistema, identificam melhorias e propõem soluções para otimizar a eficiência e a funcionalidade dos sistemas"
        imagem = "analista.svg"
    elif (result == "engenheiro"):
        descricao = "Um profissional que projeta, desenvolve e mantém software de alta qualidade. Eles aplicam princípios de engenharia para construir soluções escaláveis, seguras e eficientes, seguindo as melhores práticas de desenvolvimento de software"
        imagem = "engenheiro.svg"

    return render_template('resultado.html', result=result , descricao=descricao , imagem=imagem)

if __name__ == '__main__':
    app.run()
