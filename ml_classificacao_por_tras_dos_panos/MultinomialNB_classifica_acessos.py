from dados import carregar_acessos
from sklearn.naive_bayes import MultinomialNB

# Carrego o csv e savo nas variáveis x,y
x,y = carregar_acessos('acesso.csv')

"""
Preciso separar minha base de treino da minha base de testes para que meu teste
não fique contaminado, tendo resuldados que não vão ser de fato fiéis.
"""

# Base de treino
treino_dados = x[:70]
treino_marcacoes = y[:70]

# Base de testes
teste_dados = x[-29:]
teste_marcacoes = y[-29:]

# Carrego meu modelo
modelo = MultinomialNB()

# Treino meu modelo
modelo.fit(treino_dados,treino_marcacoes)

# Predição usando o base de testes
# Onde 1 => provavelmente irá comprar, e 0 não
resultado = modelo.predict(teste_dados)

# Agora verificamos a taxa de acerto:
diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * (total_de_acertos/total_de_elementos)

# treino com 90, testo com 9
print("Total de elementos:", total_de_elementos)
print("Taxa de acerto:", taxa_de_acerto)


