---
title: Iara - Prof. Alberto Ferreira de Souza
---

## TODO

### Template:

Para isso, o seguinte template será seguido:

Título

- Ano
- Categoria(s)
- Técnicas/ <br> Algoritmos

- Breve resumo

### Deep traffic light detection by overlaying synthetic context on arbitrary natural images 

- __Ano__:  Dez/2020
- __Categoria(s)__: Detecção de objetos (semáforos)
- __Técnicas/ <br> Algoritmos__:  Faster R-CNN
- __Breve resumo__:

> O trabalho propõe a utilização de imagens geradas artificialmente para o treinamento de redes neurais de forma a sanar algumas das principais dificuldades encontradas em trabalhos anteriores.

Trabalhos anteriores lidavam com datasets não balenceados (ausencia de status amarelo, por exemplo) e dificuldade de se categorizar grandes quantidades de imagens

A solução proposta se inicia pelo dataset, buscando ser o máximo balanceado possível, gerando imagens artificiais a partir de um fundo (uma imagem fora do contexto de trânsito) e um 'fronte' (uma imagem gerada artificialmente simulando um cenário de trânsito com sinais). Para validação foram usados 4 datasets: LISA (Laboratory for Intelligent & Safe Automobiles), Udacity, LaRA (La Route Automatisée), e um proprietário. 

Os modelos foram treinando usando uma implementação pública disponibilizada no Tensorflow, que utiliza __Faster R-CNN__.

