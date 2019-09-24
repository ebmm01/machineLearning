import csv
import pandas as pd

#Função que irá ler e carregar os csv's
def carregar_acessos():

    x = [] # => Lados da esquerda, valores que eu desconheço
    y = [] # => valores desconhecidos, o qual eu irei querer conhecer. No caso do csv eu já os conheço

    # Abro o arquivo csv
    arquivo = open('acesso.csv', 'rt')
    leitor = csv.reader(arquivo)
    
    # Pulo a primeira linha para não copiar o header
    leitor.__next__() 

    # Itero sobre as linhas e salvo nos arrays x e y
    for home, como_funciona, contato, comprou in leitor:
        x.append([
            int(home),
            int(como_funciona),
            int(contato)
        ])
        y.append(int(comprou))

    return x,y