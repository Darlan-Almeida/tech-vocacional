from sklearn import tree
from control.dict import dict


def realizar_teste(test_data):

    perfil = [
        [dict["razoavelmente"], dict["ruim"], dict["mediana"], dict["pesquisa"], dict["enigma"]],
        [dict["gosto"], dict["pessima"], dict["ruim"], dict["pesquisa"], dict["enigma"]],
        [dict["adoro"], dict["mediana"], dict["pessima"], dict["apresentar"], dict["enigma"]],
        [dict["upouco"], dict["otima"], dict["ruim"], dict["estilizar"], dict["pintar"]],
        [dict["razoavelmente"], dict["boa"], dict["pessima"], dict["estilizar"], dict["pintar"]],
        [dict["razoavelmente"], dict["otima"], dict["mediana"], dict["estilizar"], dict["pintar"]],
        [dict["razoavelmente"], dict["otima"], dict["ruim"], dict["estilizar"], dict["enigma"]],
        [dict["gosto"], dict["boa"], dict["mediana"], dict["pesquisa"], dict["pintar"]],
        [dict["adoro"], dict["otima"], dict["mediana"], dict["pesquisa"], dict["enigma"]],
        [dict["razoavelmente"], dict["mediana"], dict["mediana"], dict["pesquisa"], dict["grafico"]],
        [dict["upouco"], dict["ruim"], dict["ruim"], dict["pesquisa"], dict["grafico"]],
        [dict["adoro"], dict["mediana"], dict["pessima"], dict["apresentar"], dict["grafico"]],
        [dict["razoavelmente"], dict["mediana"], dict["boa"], dict["pesquisa"], dict["resumo"]],
        [dict["upouco"], dict["ruim"], dict["otima"], dict["pesquisa"], dict["grafico"]],
        [dict["npouco"], dict["mediana"], dict["otima"], dict["apresentar"], dict["resumo"]],
        [dict["razoavelmente"], dict["mediana"], dict["razoavelmente"], dict["liderar"], dict["enigma"]],
        [dict["boa"], dict["ruim"], dict["ruim"], dict["liderar"], dict["resumo"]],
        [dict["upouco"], dict["pessima"], dict["boa"], dict["liderar"], dict["grafico"]]
    ]

    rotulos = ["Desenvolvedor Back-end", "Desenvolvedor Back-end", "Desenvolvedor Back-end", "Desenvolvedor Front-end", "Desenvolvedor Front-end", "Desenvolvedor Front-end", "Desenvolvedor Fullstack", "Desenvolvedor Fullstack", "Desenvolvedor Fullstack", "Profissional de Dados", "Profissional de Dados", "Profissional de Dados",
               "Analista de Sistemas", "Analista de Sistemas", "Analista de Sistemas", "Engenheiro de Software", "Engenheiro de Software", "Engenheiro de Software"]

    # Criando o classificador de árvore de decisão
    classificador = tree.DecisionTreeClassifier()

    # Treinando o classificador
    classificador = classificador.fit(perfil, rotulos)

    test_data_numeric = [dict[feature] for feature in test_data]
    resultado = classificador.predict([test_data_numeric])

    return resultado[0]

