---
title: RNN & LSTM
---

## O que são redes neurais

Redes neurais são um conjunto de algoritmos que se assemelham ao cérebro humano e são projetados para reconhecer padrões. Eles interpretam os dados sensoriais através de uma percepção da máquina, rotulando ou agrupando dados brutos. Eles podem reconhecer padrões numéricos, contidos em vetores, nos quais todos os dados do mundo real (imagens, som, texto ou série temporal) devem ser traduzidos. As redes neurais artificiais são compostas por um grande número de elementos de processamento altamente interconectados (neurônio) trabalhando juntos para resolver um problema

## Recurrent Neural Networks

Redes recorrentes são um tipo de rede neural artificial projetada para reconhecer padrões em seqüências de dados, como texto, genomas, caligrafia, palavra falada ou dados numéricos de séries temporais emanados de sensores, mercados de ações e agências governamentais. Esses algoritmos levam em consideração o tempo e a sequência, e possuem uma dimensão temporal. Pesquisas mostram que eles são um dos tipos mais poderosos e úteis de redes neurais. RNNs são aplicáveis mesmo a imagens, que podem ser decompostas em uma série de "remendos" (patches) e tratadas como uma sequência.


Para o melhor entendimento sobre as RNN's, é bom antes falar sobre as redes feedfoward. Ambas as redes recebem o nome da forma como canalizam informações através de uma série de operações matemáticas realizadas nos nós da rede. As redes feedforward alimentam informações diretamente (nunca tocando em um determinado nó duas vezes), enquanto as redes recorrentes percorrem através de um loop.

![](https://i0.wp.com/deeplearningbook.com.br/wp-content/uploads/2019/07/rnn.png?w=2340)

Ou seja, uma rede feedforward não tem noção de ordem no tempo, e a única entrada que considera é o exemplo atual a que foi exposta. As redes feedforward são amnésicas em relação ao seu passado recente; elas lembram nostalgicamente apenas os momentos formativos do treinamento.

As redes recorrentes, por outro lado, tomam como entrada não apenas o exemplo de entrada atual que veem, mas também o que perceberam anteriormente no tempo.  A decisão de uma rede recorrente alcançada na etapa de tempo t-1 afeta a decisão que alcançará um momento mais tarde na etapa de tempo t. Assim, as redes recorrentes têm duas fontes de entrada, o presente e o passado recente, que se combinam para determinar como respondem a novos dados, da mesma forma que fazemos na vida. 

### Os problemas das RNN

Apesar de tudo, as redes neurais recorrentes possuem alguns problemas, dentre os quais podemos destacar: 

- Dissipação e explosão de gradiante (Gradient vanishing and exploding).
- Treinar um RNN é uma tarefa muito difícil.
- Ele não pode processar seqüências muito longas se estiver usando [__tanh__](https://theclevermachine.wordpress.com/tag/tanh-function/) ou [__relu__](https://machinelearningmastery.com/rectified-linear-activation-function-for-deep-learning-neural-networks/) como uma função de ativação.

## Referências

[Redes Neurais Recorrentes](http://deeplearningbook.com.br/redes-neurais-recorrentes/)

[A Beginner's Guide to LSTMs and Recurrent Neural Networks](https://pathmind.com/wiki/lstm)

[Understanding RNN and LSTM](https://towardsdatascience.com/understanding-rnn-and-lstm-f7cdf6dfc14e)