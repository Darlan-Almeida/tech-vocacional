from flask import Flask, render_template, request, jsonify , session

from flask_session import Session
from control.test import realizar_teste
from control.crud import inserir_dados, inserir_resposta, inserir_opiniao

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/termos/')
def termos():
    return render_template('termos.html')    

@app.route('/formulario', methods=['POST'])
def formulario():
    nome = request.form['nome']
    email = request.form['email']
    idade = request.form['idade']
    escola = request.form['escola']

    try:
        usuario_id = inserir_dados(nome, email, idade, escola)
        session["usuario_id"] = usuario_id
        return render_template('questionario.html', usuario_id=session["usuario_id"])
    except:
        return "Error"


@app.route('/submit/', methods=['POST'])
def submit():


    data = request.get_json()
    values = data['values']
    
    #checando valores
    print(values)
    print(session["usuario_id"])

    result = realizar_teste(values)

    inserir_resposta(int(session["usuario_id"]) , values[0], values[1], values[2], values[3], values[4], result)
    return jsonify(result=result)


@app.route('/resultado/<result>' , methods=['GET'])
def resultado(result):
    descricao = ""
    imagem = ""
    link = ""

    if result == "Desenvolvedor Back-end":
        descricao = "Um profissional especializado em desenvolvimento de software e sistemas que trabalha principalmente na parte do servidor, lidando com a lógica de negócios, bancos de dados e integração de sistemas"
        imagem = "back.svg"
        link = "https://blog.orientu.com.br/profissoes/desenvolvedor-back-end/"

    elif result == "Desenvolvedor Front-end":
        descricao = "Um profissional especializado em desenvolvimento de interfaces de usuário, que se concentra na criação da parte visual e interativa de um aplicativo ou site, utilizando tecnologias como HTML, CSS e JavaScript"
        imagem = "front.svg"
        link = "https://blog.orientu.com.br/profissoes/desenvolvedor-front-end/"
        
    elif result == "Desenvolvedor Fullstack":
        descricao = "Um profissional versátil que possui habilidades tanto no desenvolvimento back-end quanto front-end. Eles têm conhecimento em várias tecnologias e podem lidar com todas as camadas de um aplicativo ou site"
        imagem = "full.svg"
        link = "https://kenzie.com.br/blog/full-stack-o-que-e/"
        
    elif result == "Profissional de Dados":
        descricao = "Um profissional que trabalha com análise e interpretação de grandes volumes de dados. Eles aplicam técnicas estatísticas e algoritmos para extrair informações valiosas e insights a partir dos dados, ajudando a tomar decisões informadas"
        imagem = "dados.svg"
        link = "https://blog.revelo.com.br/carreiras-em-dados/"
        
    elif result == "Analista de Sistemas":
        descricao = "Um profissional que atua na análise e resolução de problemas relacionados a sistemas de informação. Eles investigam os requisitos do sistema, identificam melhorias e propõem soluções para otimizar a eficiência e a funcionalidade dos sistemas"
        imagem = "analista.svg"
        link = "https://blog.orientu.com.br/profissoes/analista-de-sistemas/"
        
    elif result == "Engenheiro de Software":
        descricao = "Um profissional que projeta, desenvolve e mantém software de alta qualidade. Eles aplicam princípios de engenharia para construir soluções escaláveis, seguras e eficientes, seguindo as melhores práticas de desenvolvimento de software"
        imagem = "engenheiro.svg"
        link = "https://blog.somostera.com/data-science/carreiras-em-dados-em-destaque-no-mercado"
        

    return render_template('resultado.html', result=result, descricao=descricao, imagem=imagem, link=link, usuario_id=session["usuario_id"])


@app.route('/receber_opiniao/',methods=['POST', 'GET'])
def receber_opiniao():
    if request.method == 'POST':
        data = request.get_json()
        opiniao = data.get('opiniao')

        #checando valores
        print(opiniao)
        print(session["usuario_id"])
        
        inserir_opiniao(session["usuario_id"], opiniao)
        return jsonify({'message': 'Opinião recebida com sucesso'})



if __name__ == '__main__':
    app.run()
