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
teste = [misterioso[0], misterioso2]

print(modelo.predict(teste))