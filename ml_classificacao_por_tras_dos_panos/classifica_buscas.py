import pandas as pd
from sklearn.naive_bayes import MultinomialNB 

# Leio com o pandas e retono um dataframe
df = pd.read_csv('buscas.csv')

# Pego as colunas de atributos
x_df = df[['home', 'busca', 'logado']]

# pego as colunas de resultado
y_df = df['comprou']

# E extraio os dummies do  do x
xdummies_df = pd.get_dummies(x_df)

# Pego novamente uma array de valores de x e y
x = xdummies_df.values
y = y_df.values

# Treino 90% dos valores:
tamanho_de_treino = int(0.9 * len(y))
treino_dados = x[:tamanho_de_treino]
treino_marcacoes = y[:tamanho_de_treino]

# E os 10% restantes serão usados para testes:
tamanho_de_teste = int(len(y) - tamanho_de_treino)
teste_dados = x[-tamanho_de_teste:]
teste_marcacoes = y[-tamanho_de_teste:]

# Crio o modelo
modelo = MultinomialNB()

# Treino o modelo
modelo.fit(treino_dados, treino_marcacoes)

# Predição usando a base de testes
resultado = modelo.predict(teste_dados)

# Agora verificamos a taxa de acerto:
diferencas = resultado - teste_marcacoes

acertos = [d for d in diferencas if d == 0]
total_de_acertos = len(acertos)
total_de_elementos = len(teste_dados)
taxa_de_acerto = 100.0 * (total_de_acertos/total_de_elementos)

# treino com 90, testo com 9
print("Total de elementos de teste:", total_de_elementos)
print("Taxa de acerto:", taxa_de_acerto)