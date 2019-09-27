import pandas as pd
from sklearn.naive_bayes import MultinomialNB 
from sklearn.ensemble import AdaBoostClassifier
from collections import Counter

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

# Treino x% dos valores, a ser definido conforme eu achar melhor:
porcentagem_de_treino = 0.8

tamanho_de_treino = int(porcentagem_de_treino * len(y))
treino_dados = x[0:tamanho_de_treino]
treino_marcacoes = y[0:tamanho_de_treino]

# E os y% restantes serão usados para testes:
porcentagem_de_teste = 0.1


"""
Aqui uma observação: apersar de as variáveis de validação estarem ali em baixo, elas não foram
adicionadas de cara. Ao contrário, elas foram adicionadas somente ao final, para que todas as verificações sejam de fato
validadas.
"""
tamanho_de_teste = porcentagem_de_teste * len(y)
tamanho_de_validacao = len(y) - tamanho_de_treino - tamanho_de_teste
fim_de_teste = int(tamanho_de_treino +tamanho_de_teste)

teste_dados = x[tamanho_de_treino:fim_de_teste]
teste_marcacoes = y[tamanho_de_treino:fim_de_teste]

validacao_dados = x[fim_de_teste:]
validacao_marcacoes = y[fim_de_teste:]



# Crio o modelo
modelo_MultinomialNB = MultinomialNB()

def treina_e_prediz(teste_marcacoes, teste_dados,treino_dados, treino_marcacoes, modelo):

    # Treino o modelo
    modelo.fit(treino_dados, treino_marcacoes)
    
    # Predição usando a base de testes
    resultado = modelo.predict(teste_dados)

    # Agora verificamos a taxa de acerto:
    acertos = resultado == teste_marcacoes
    total_de_acertos = sum(acertos)
    total_de_elementos = len(teste_dados)
    taxa_de_acerto_local = 100.0 * (total_de_acertos/total_de_elementos)

    # treino com 90, testo com 9
    print("Total de elementos de teste:", total_de_elementos)
    print(f"Taxa de acerto: {taxa_de_acerto_local}%")
    return taxa_de_acerto_local

print("Teste com MultinomialNB: \n")
resultado_MultinomialNB = treina_e_prediz(teste_marcacoes, teste_dados,treino_dados, treino_marcacoes, modelo_MultinomialNB)


"""
Tive como resultado 82% de acerto. A princípio parece ser um bom número, mas preciso 
comparar com algo para poder dizer se de fato o é. E como fazer isso? É preciso estimar 
um 'caso base' com um algoritmo 'burro', ou chutar tudo com um único valor
"""


#Então tentaremos com outro algoritmo: AdaBoostClassifier()
print("\nTeste com AdaBoostClassifier")
modelo_AdaBoost = AdaBoostClassifier()

resultado_AdaBoost = treina_e_prediz(teste_marcacoes, teste_dados, treino_dados, treino_marcacoes, modelo_AdaBoost)

"""
Comparamos qual dos dois algoritmos teve o melhor resultado e a partir disso fazemos uma nota predição
com os % restante de validação (10% no nosso caso).
"""

if resultado_MultinomialNB > resultado_AdaBoost:
    print("\nMultinomialNB teve uma performance melhor.")
    vencedor = modelo_MultinomialNB
else:
    print("\nAdaBoost teve um resultado melhor.")
    vencedor = modelo_AdaBoost

# E defino uma função que faz a predição com a base se validação
def teste_real(modelo, validacao_dados, validacao_marcacoes):
    resultado = vencedor.predict(validacao_dados)
    acertos = (resultado == validacao_marcacoes)

    total_de_acertos = sum(acertos)
    total_de_elementos = len(validacao_marcacoes)
    taxa_de_acerto = 100.0 * total_de_acertos/total_de_elementos

    print(f"Taxa de acerto do vencedor entre os dois algoritmos no mundo real: {taxa_de_acerto}")

teste_real(vencedor, validacao_dados, validacao_marcacoes)

"""
E fazemos uma comparação com o nosso 'algoritmo burro', que apenas chuta. A partir disso podemos fazer uma comparação com o nosso
modelo utilizado, e afirmar se ele é bom ou ruim (claro, depende de outros fatores também).
Vale uma observação aqui: inicialmente calculávamos essa taxa de acerto base com as marcaçes de testes, porém optamos por fazer isso
com as marcações de validações para validar o nosso algoritmo final. Ou seja, a taxa de acerto do agoritmo vencedor e a taxa de acerto do
algoritmo burro foram feitas com base nos exatos mesmos dados. 
"""

# Com o counter eu conto os valores de 0's e 1's, sim e nãp, etc, e pego esses valores com o values()
acerto_base = max(Counter(validacao_marcacoes).values())

print(f"Taxa de acerto base (algoritmo 'burro'): {acerto_base/len(validacao_marcacoes)*100}%") 

