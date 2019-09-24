import csv
import pandas as pd

#Função que irá ler e carregar os csv's
def carregar_acessos(file):

    x = [] # => Lados da esquerda, valores que eu desconheço
    y = [] # => valores desconhecidos, o qual eu irei querer conhecer. No caso do csv eu já os conheço

    # Abro o arquivo csv
    arquivo = open(file, 'rt')
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

def carregar_buscas(file):

    x = [] # => Lados da esquerda, valores que eu desconheço
    y = [] # => valores desconhecidos, o qual eu irei querer conhecer. No caso do csv eu já os conheço

    # Abro o arquivo csv
    arquivo = open(file, 'rt')
    leitor = csv.reader(arquivo)
    
    # Pulo a primeira linha para não copiar o header
    leitor.__next__() 

    # Itero sobre as linhas e salvo nos arrays x e y
    for home, busca, logado, comprou in leitor:
        x.append([
            int(home),
            busca,
            int(logado)
        ])
        y.append(int(comprou))

    return x,y