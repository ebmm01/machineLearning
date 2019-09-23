# É gordo? Tem pernas curtas? Late? 
# Onde 1 = true, 0 = false

porco1 = [1,1,0]
porco2 = [1,1,0]
porco3 = [1,1,0]
cachorro1 = [1,1,1]
cachorro2 = [0,1,1]
cachorro3 = [0,1,1]

dados = [porco1, porco2, porco3, cachorro1, cachorro2, cachorro3]

# Onde 1 = porco, -1 = cachorro
marcacoes = [1,1,1,-1,-1,-1]

# Agora inserimos um elemento 'misterioso': não sabemos o que ele é,
# e deixaremos o sistema dizer qual é
misterioso = [[1,1,1]]


from sklearn.naive_bayes import MultinomialNB

# Crio o modelo com base no MultinomialNB
modelo = MultinomialNB()

# E treinamos nosso modelo:
modelo.fit(dados, marcacoes)

# Iremos então tentar ver qual bicho é o elemento misterioso:
print(modelo.predict(misterioso)) # => [-1], ou seja, cachorro.

# podemos também testar vários elementos ao mesmo tempo:
misterioso2 = [1,0,0]
misterioso3 = [0,0,1]
testes = [misterioso[0], misterioso2, misterioso3]

print(modelo.predict(testes))

# Porém eu sei qual animal é cada um 'misterioso':
# -1 = porco, 1 = cachorro
marcacoes_teste = [-1, 1, -1]

resultado = modelo.predict(testes)
print(resultado) # => [-1 1 -1], ou seja, ele 'acertou'

"""
 Como sabíamos o que cada animal era, podemos fazer uma comparação do resultado real
 Com o resultado do estimador. onde for 0 quer dizer que o estimador acertou, e qualquer coisa 
 diferente disso quer dizer que ele errou
"""
diferencas = resultado - marcacoes_teste # => [0 0 0], ou seja, ele acertou todos
print("Diferenças:" ,diferencas)

# Podemos também adicionar o total de acertos numa array:
acertos = [d for d in diferencas if d==0]

# E o total de acertos é o tamanho desse array:
total_de_acertos = len(acertos)
print("Total de acertos:",acertos)

# E verificamos o total de elementos:
total_de_elementos = len(testes)
print("Total de elementos de teste:", total_de_elementos)

# Definimos então nossa taxa de acerto:

taxa_de_acerto = 100.0 * (total_de_acertos / total_de_elementos)

print("Taxa de acerto:", taxa_de_acerto, "%")