## Introdução

O curso tem como objetivo gerar recomendações de filmes do site Movie Lens e implementar uma variação do algorítimo k-NN (k-nearest neighbors). nesse relatório iremos abordar sobre o algorítimo elaborado, além de explicar de forma breve alguns dos conceitos utilizados

## Sistemas de recomendação e heurísticas iniciais

Sistemas recomendadores (ou de recomendação) são softwares e 
Sistemas de recomendação ( do ingles _Recommender Systems - RSs_) são ferramentas e técnicas de software que fornecem sugestões de itens para serem úteis ao usuário. As sugestões estão relacionadas a vários processos de tomada de decisão, como quais itens comprar, que música escutar ou que notícias on-line ler [1].

As recomendações podem ser feitas a partir de diversas abordagens, e dependem de fatores como __conhecimento prévio ou não dos gostos do usuário, datasets__ dentre outros. 

No nosso caso, o dataset consistia em uma série de notas de filmes por diversos usuários, todos com um ID numérico. Dessa forma, nossa primeira abordagem foi a __heurística de total de votos__: faz sentido pensar que se um filme possui um alto número de avaliações é porque ele pode ser uma recomendação interessante.

De cara vimos alguns problemas nessa abordagem. Um alto número de avaliações não necessáriamente quer dizer que o filme foi bem recomendado. Ao contrário, posso ter um filme com grande número de avaliações, mas a maioria delas negativa. Assim, chegamos a segunda abordagem: __ordenar pela média__ dos filmes. 

Com essa segunda heurística eu passo a recomendar filmes que foram mais bem avaliados, tornando as recomendações mais válidas. Contudo com um novo problema: recomendar filmes com base única e exclusivamente na avaliação pode trazer filmes com avaliações enviesadas ou de nicho, com poucas ou somente uma avaliação, não sendo uma boa opção de recomendação.

Uma forma de resolver esse problema é determinar um número mínimo de avaliações para que um filme seja recomendado, e nesse caso nós descartamos filmes com menos de 50 avaliações, o que melhora o nosso recomendador.

Ainda assim, todas os métodos acima não assumem nenhum conhecimento prévio sobre o usuário, e o nosso dataset nós dá esses dados. Podemos então fazer um outro tipo de abordagem: escolher um usuário qualquer e procurar outros usuários com gostos similares ao inicialmente escolhido.

### Distância euclidiana entre os usuários & Collaborative filtering

Até o momento fizemos apenas uma filtragem baseada apenas nas notas e número de avaliações dos filmes, ou seja, uma filtragem baseada em conteúdo (_content based filtering_). Mas, e se considerarmos as avaliações dos usuários? Como o dataset nos fornece esses dados, é possível fazer uma filtragem colaborativa (_colaborative filtering_), ou seja, recomendar filmes a partir das avaliações dos próprios usuários.

Para isso temos de calcular as distâncias entre as avaliações de um usuário qualquer e os outros usuários. Esse cálculo é a __distância euclidiana__ entre as notas dos filmes, e quanto menor for o resultado, mais próximos são os gostos entre os usuários. A partir disso podemos montar uma lista com os n usuários mais próximos, pegando os filmes mais bem avaliados por eles.

### Collaborative filtering & Content based filtering: o melhor de dois mundos

O método anterior, apesar de ser muito eficiente, também possui algumas falhas: filmes visto somente por 1 ou poucos usuários da lista ou de nicho voltam a ser recomendados. Isso leva a necessidade de alguns ajustes: devemos considerar não somente a filtragem colaborativa, mas também o conteúdo. 

Em suma, devemos considerar um número mínimo de usuários que viram o mesmo filme para que o título seja recomendado (consideramos 50% nesse caso) e devemos também descartar filmes abaixo do limiar de avaliações determinado anteriormente (no mínimo 50 avaliações) e filmes que já foram vistos pelo usuaŕio inicial.

A partir disso nosso recomendador irá calcular possíveis filmes, recomendando novos filmes com base nos filmes que o usuaŕio inicial assistiu e avaliou. Esse algorítmo passa a ser uma implementação muito próxima do ___k nearest neighbors (knn)_ ou 'k mais próximos vizinhos'__.


## Referencias

[1] Francesco Ricci and Lior Rokach and Bracha Shapira, Introduction to Recommender Systems Handbook, Recommender Systems Handbook, Springer, 2011

F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. <https://doi.org/10.1145/2827872>