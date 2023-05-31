from sklearn import tree

# Dados de treinamento: características (cor e textura) e rótulos (classe da fruta)
perfil = [
    [1, 2, 3, 4, 5],
    [6, 7, 2, 4, 5],
    [8, 3, 7, 9, 5],
    [10, 11, 2, 12, 13],
    [1, 14, 7, 12, 13],
    [1, 11, 3, 12, 13],
    [1, 11, 2, 12, 5],
    [6, 14, 3, 4, 13],
    [8, 11, 3, 4, 5],
    [1, 3, 3, 4, 15],
    [10, 2, 2, 4, 15],
    [8, 3, 7, 16, 15],
    [1, 3, 17, 4, 18],
    [10, 2, 19, 4, 15],
    [20, 3, 19, 16, 18],
    [1, 3, 21, 22, 5],
    [23, 2, 2, 22, 18],
    [10, 7, 21, 22, 15]
]

rotulos = ["back", "back", "back", "front", "front", "front", "full", "full", "full", "dados", "dados", "dados", "analista", "analista", "analista", "engenheiro", "engenheiro", "engenheiro"]


# Criando o classificador de árvore de decisão
classificador = tree.DecisionTreeClassifier()

# Treinando o classificador
classificador = classificador.fit(perfil, rotulos)

# Dados de teste
test = [[ 1 , 2, 3 , 4 ,5]]  # Fruta com características: cor = 110 (vermelho) e textura = 0 (lisa)


resultado = classificador.predict(test)

print(resultado)


