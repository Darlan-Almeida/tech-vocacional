# VOCACIONAL TECH

Site que recebe respostas relacionadas aos perfil do usuário, e atráves de Machine Learning, retorna uma área como sugestão para o usuário

# Tela de cadastro:

![tela login](Readme's/tela_login.png)

A aplicação  necessita dos cadastros dos dados básicos dos usuários, a fim de ter uma melhor análise dos resultados. A tabela usuário está arranjada da seguinte forma:

| Id       | Nome     | E-mail       | Idade  | Escola               |
|-------------|----------|--------------|----------|---------------------------|
| Serial primary Key     | Varchar(100)   | Varchar(255)    | Integer| Varchar(100) |


# Tela de perguntas:

![tela de perguntas](Readme's/tela_pergunta.png)

O site, após a inserção dos dados, permite a respostas de pergutnas chaves que serão chaves para a definição da profissão. No sistema, é guardada as respostas, a fim de analisar os resultados para aprimorar, futuramente, o teste!

| Id _usuario      | pergunta1     | pergunta2     | pergunta3  | pergunta4 | pergunta5 | profissao |
|-------------|----------|--------------|-------------|----------|---------------------------|---------------------------|
| Serial primary Key     | Varchar(10)   | Varchar(10)    | Integer| Varchar(10) | Varchar(10) | Varchar(10)|


# Processamento das respostas:

O Processamento das respostas são feitos através de um campo da IA - Machine Learning -, que usa de uma tabela com possiveis predições para possiveis respostas. Porém, nem todas as possibilidades são satisfieta nessa tabela, aí que surge o Machine Learning, para retornar um resultado que não foi previsto na tabela, porém o resultado será aquele que dá mais "match" com a das definidas na tabela. Veja a tabela





A aplicação será utilizada para contabilidade, necessitando realizar operações de pesquisa para os gerentes de forma extremamente rápida. As operações mais importantes são:
- Pesquisa pelo menor salário
- Pesquisa pelo maior salário
- Pesquisa pela mediana dos salários

O usuário do sistema necessita obter o máximo de desempenho nas operações de pesquisa, para isto, utilizei a **ordenação binária** do salários com o metódo **Quick sort**.


Ao iniciar a aplicação, os dados já cadastrados ao longo das últimas execuções são carregados a partir de um arquivo csv.
com isso, o usuário pode baixar a planilha e analisar os dados.


# Tutorial de uso da aplicação

O sistema funciona por linha de comando, pois a aplicação tem foco, apenas, no desenvolvimento back-end.


1- Crie um funcionário, o funcionário pode ser de três tipos:
- Vendedor
- Gerente
- Secretário

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://www.youtube.com/watch?v=ycesdyiZGRk)


2- Salve os dados dos funcionários cadastrados em um arquivo CSV.

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://www.youtube.com/watch?v=NAAkIfLU3Qc)


3- Remova o registro dos funcionários que desejar

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://www.youtube.com/watch?v=VOxP_RJ8zQc)

4- Atualize o registro dos funcionários que desejar

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://youtu.be/9WJlcMV-MpM)

5- Busca pelo menor salário

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://youtu.be/AwxTV0xR71Q)

6- Busca pelo maior salário

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://www.youtube.com/watch?v=AwxTV0xR71Q)

7- Busca pelo salário médio

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://youtu.be/qQ4e36506_4)


8- Ordenação da lista

[[Clique aqui para ver, no meu canal do Youtube, a execução dessa função]](https://www.youtube.com/watch?v=5q1Pzpltq9Q)


### Autor
---

![Imagem do autor](https://media.licdn.com/dms/image/D4D35AQEaArHpYygSfQ/profile-framedphoto-shrink_400_400/0/1676827319640?e=1689030000&v=beta&t=EI9NzBKbjy56r1aFldNvym7GATPY5sQhvoPA90vGMhQ)





Feito com ❤️ por Darlan Almeida👋🏽 Entre em contato!

[![Linkedin Badge](https://img.shields.io/badge/-Darlan-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/darlan-almeida/)](https://www.linkedin.com/in/darlan-almeida-92251a232/) 
[![Gmail Badge](https://img.shields.io/badge/-adarlan748@gmail.com-c14438?style=flat-square&logo=Gmail&logoColor=white&link=mailto:adarlan748@gmail.com)](mailto:adarlan748@gmail.com)

