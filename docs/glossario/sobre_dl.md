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

## Redes LSTM

As redes Long Short-Term Memory (LSTM) são uma versão modificada de redes neurais recorrentes, que facilitam a lembrança de dados anteriores ​​na memória. O problema do __gradiente de fuga (vanishing gradient) das RNN's é resolvido aqui__. O LSTM é adequado para classificar, processar e prever séries temporais, visto que os LSTMs são projetados para evitar o problema de dependência de longo prazo. Ele treina o modelo usando back-propagation (ou propagação traseira). 

Em uma rede LSTM, três 'portões' (_gates_) estão presentes:

![](https://miro.medium.com/max/1044/1*MwU5yk8f9d6IcLybvGgNxA.jpeg)

- __Portão de entrada__: descobre qual valor da entrada deve ser usado para modificar a memória. A função __sigmóide__ decide quais valores deixar passar entre 0 e 1. e a função __tanh__ atribui peso aos valores passados, decidindo seu nível de importância variando de -1 a 1.

- __Portão de esquecimento__: descobre quais detalhes devem ser descartados do bloco. É decidido pela função __sigmóide__. O portão olha o estado anterior (ht-1) e conteúdo de entrada (Xt) e gera um número entre 0 (omita isso) e 1 (mantenha isso) para cada número no estado da célula Ct-1.

- __Portão de saída__: a entrada e a memória do bloco são usadas para decidir a saída. A função __sigmóide__ decide quais valores deixar passar, entre 0 e 1,  e a função __tanh__ dá peso aos valores passados, decidindo seu nível de importância, variando de -1 a 1 e multiplicado pela saída da __sigmóide__.

![](https://pathmind.com/images/wiki/greff_lstm_diagram.png)



## Referências

[Redes Neurais Recorrentes](http://deeplearningbook.com.br/redes-neurais-recorrentes/)

[A Beginner's Guide to LSTMs and Recurrent Neural Networks](https://pathmind.com/wiki/lstm)

[MACHINE LEARNING DE SÉRIES TEMPORAIS – LSTM](https://www.monolitonimbus.com.br/machine-learning-de-series-temporais-lstm/)

[Understanding RNN and LSTM](https://towardsdatascience.com/understanding-rnn-and-lstm-f7cdf6dfc14e)