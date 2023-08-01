CREATE TABLE usuarios (
    id SERIAL PRIMARY Key,
    nome VARCHAR(100),
    email VARCHAR(255),
    idade INTEGER,
    escola VARCHAR(100)
);


-- Criação da tabela "questionarios"
CREATE TABLE questionarios (
    id_usuario INTEGER,
    pergunta1 VARCHAR(10),
    pergunta2 VARCHAR(10),
    pergunta3 VARCHAR(10),
    pergunta4 VARCHAR(10),
    pergunta5 VARCHAR(10),
    profissao VARCHAR(100)
);


CREATE TABLE opiniao(
    id_usuario INTEGER,
    opiniao VARCHAR(10)
)