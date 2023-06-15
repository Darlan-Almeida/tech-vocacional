import pg8000
from models.config import DB_CONFIG


# Função para inserir os dados do formulário no banco de dados
def inserir_dados(nome, email, idade, escola):
    connection = pg8000.connect(**DB_CONFIG)
    cursor = connection.cursor()

    query = "INSERT INTO usuarios (nome, email, idade, escola) VALUES (%s, %s, %s, %s)"
    values = (nome, email, idade, escola)
    cursor.execute(query, values)

    connection.commit()
    cursor.close()
    connection.close()

    return "Cadastrado com sucesso"
