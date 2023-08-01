import pg8000
from models.config import DB_CONFIG


# Função para inserir os dados do formulário no banco de dados
def inserir_dados(nome, email, idade, escola):
    connection = pg8000.connect(**DB_CONFIG)
    cursor = connection.cursor()

    query = "INSERT INTO usuarios (nome, email, idade, escola) VALUES (%s, %s, %s, %s) RETURNING id"
    values = (nome, email, idade, escola)
    cursor.execute(query, values)



    connection.commit()

    # Recupera o ID do usuário inserido
    usuario_id = cursor.fetchone()[0]

    cursor.close()
    connection.close()

    return usuario_id



def inserir_resposta( usuario_id, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, profissao):
    connection = pg8000.connect(**DB_CONFIG)
    cursor = connection.cursor()

    query = "INSERT INTO questionarios ( id_usuario,pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, profissao) VALUES (%s, %s, %s, %s, %s , %s, %s)"
    values = (usuario_id, pergunta1, pergunta2, pergunta3, pergunta4, pergunta5, profissao)
    cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()

    return "Cadastrado com sucesso"


def inserir_opiniao( usuario_id, opiniao):
    connection = pg8000.connect(**DB_CONFIG)
    cursor = connection.cursor()

    query = "INSERT INTO opiniao ( id_usuario, opiniao) VALUES (%s, %s)"
    values = (usuario_id, opiniao)
    cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()

    return "Cadastrado com sucesso"