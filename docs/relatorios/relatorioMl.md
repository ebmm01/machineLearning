---
title: Relatório MultinomialNB
---

## Introdução

O curso teve por objetivo dar uma introdução sobre Machine Learning e explicar um pouco sobre seu funcionamento. São feitos 3 códigos de exemplo: primeiramente a classificação de animais em cachorros ou porcos, de forma bem simples (sem ao menos um dataset), depois um código para verificar se um usuário que visitou um site sob certos aspectos (se visitou a home, fale conosco, etc) e a partir disso compraria ou não um produto (com um dataset de 100 itens) e por fim um algoritmo muito parecido com o anterior, mas que possuia um dataset maior (cerca de 1000 itens) com variáveis categóricas (qual linguagem de programação uma pessoa x pesquisou). Em todos os programas foi utilizado o algoritmo __MultinomialNB__, e no último em específico também foi utilizado o algoritmo __AdaBoostClassifier__. 


## MultinomialNB (Naive Bayes)

Segundo a documentação: _O classificador __multinomial Naive Bayes__ é adequado para classificação com recursos discretos (por exemplo, contagem de palavras para classificação de texto). _. Ele possui algumas regras de decisão, como __maximum a posteriori__ ou um __pseudo chute__ baseado nas probabilidades de eventos.

Para o MultinomialNB, fazemos uso de __variáveis categóricas__ , ou seja, _características que não possuem valores quantitativos, mas, ao contrário, são definidas por várias categorias_. Em nosso caso temos variáveis nominais, pois são sempre dados binários. Caso tenhamos dados que não sejam 0's ou 1's, temos que retirar os __dummies__ dessas variáveis (igual fizemos no classificador 3).

## Algoritmo base (algoritmo burro) e taxa de acerto

Por fim, conseguimos estimar uma taxa de acerto para nossos classificadores. Mas há um porém: não há nenhuma outra métrica para dizer se ele está bom ou não. Podemos então chutar todos os valores como 0 ou 1, e pegar o maior valor de acerto desse chute. Isso é chamado algoritmo base, que é basicamente um chute a esmo. Caso esse algoritmo base tenha uma taxa de acerto superior aos nossos classificadores, isso quer dizer que nosso algoritmo perde para um simples chute, então não está bom. Contudo não se pode automaticamente inferir o contrário, ou seja, que se nosso classificador for superior ao algoritmo base ele é bom. Isso se dá principalemente pelo fato de que a porcentagem de acerto deve considerar diversos fatores como quantidade de dados testada (e/ou validada), o problema que estou trabalhando (prevendo se um usuário fará uma compra ou a chance de haver um terremoto?) ou mesmo questões negociais. Dessa forma o algoritmo base serve como uma estimativa inicial, e não final.