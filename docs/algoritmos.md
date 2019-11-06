## Multinominal Naive bayes

O classificador __multinomial Naive Bayes__ é adequado para classificação com recursos discretos (por exemplo, contagem de palavras para classificação de texto). Ele utiliza o __maximum a posteriori__ como regra de decisão. Ele estima a probabilidade condicional de uma palavra específica dada uma classe como a frequência relativa do termo t em documentos pertencentes à classe (c). A variação leva em consideração o número de ocorrências do termo t nos documentos de treinamento da classe (c), incluindo várias ocorrências. 

![](https://miro.medium.com/max/300/1*DdFz2o7Jt7uFzAGP8Pwdrg.png)

### Parâmetros do MultinomialNB

__alpha__ : float, optional (default=1.0):
Parâmetro de suavização aditivo (Laplace se == 1/ Lidstone se < 1 ou 0 para sem suavização). 
A idéia básica é aumentar as probabilidades de todos os bigramas (sequências de duas palavras) na equação de probabilidades não máxima  em __n__ para tornar tudo diferente de zero. -- Hiperparâmetro

__fit_prior__ : boolean, optional (default=True)
Se deve aprender as probabilidades anteriores da classe ou não. Se falso, um uniforme anterior será usado.

__class_prior__ : array-like, size (n_classes,), optional (default=None)
Probabilidades anteriores das classes. Se especificado, os anteriores não são ajustados de acordo com os dados.

## AdaBoostClassifier

Segundo a documentação, _Um classificador AdaBoost é um meta-estimador que começa ajustando um classificador no conjunto de dados original e depois ajusta cópias adicionais do classificador no mesmo conjunto de dados, mas onde os pesos das instâncias classificadas incorretamente são ajustados para que os classificadores subsequentes se concentrem mais em casos difíceis_. 

Na prática, ele combina diversos algoritmos de classificação fracos e transforma todos num unico forte. Um algoritmo de classificação fraco é um algoritmo simples que tem um desempenho ruim, mas que funciona melhor do que ficar adivinhando respostas aleatórias.

Ele pode ser aplicado em qualquer algoritmo de classificação de dados, pois a sua tecnica é baseada em muitos classificadores diferentes e não num unico só, talvez ele possa te retornar um melhor resultado.

### Parâmetros AdaBoostClassifier

__base_estimator__ : object, optional (default=None)
O estimador base a partir do qual o conjunto impulsionado (Boost) é construído. É necessário suporte para ponderação de amostra, além de atributos classes_ e n_classes_ adequados. Se __None__, o estimador base é __DecisionTreeClassifier__ (max_depth = 1)

__n_estimators__ : integer, optional (default=50)
O número máximo de estimadores nos quais o Boost é finalizado. Em caso de __perfect fit__, o procedimento de aprendizado é finalizado antes.

__learning_rate__ : float, optional (default=1.)
A taxa de aprendizado reduz a contribuição de cada classificador por learning_rate. Há um trade-off entre __learning_rate__ e __n_estimators__.
Learning rate shrinks the contribution of each classifier by learning_rate. There is a trade-off between learning_rate and n_estimators.

__algorithm__ : {‘SAMME’, ‘SAMME.R’}, optional (default=’SAMME.R’)
Se "SAMME.R", então usa o algoritmo de _boosting_ real __SAMME.R__. __base_estimator__ deve suportar o cálculo de probabilidades de classe. Se "SAMME", use o algoritmo de _boosting_ discreto __SAMME__. O algoritmo SAMME.R normalmente converge mais rápido que o SAMME, obtendo um erro de teste mais baixo com menos _boosting's_ de aumento.

__random_state__ : int, RandomState instance or None, optional (default=None)
Se um inteiro, __random_state__ é a _seed_ usada pelo gerador de números aleatórios; Se uma instância _RandomState_, __random_state__ se torna o gerador de números aleatórios; Se __None__, o gerador de números aleatórios é a instância __RandomState__ usada pelo __np.random__.

## Curiosidades

_At a high level, AdaBoost is similar to Random Forest in that they both tally up the predictions made by each decision trees within the forest to decide on the final classification_ (https://towardsdatascience.com/machine-learning-part-17-boosting-algorithms-adaboost-in-python-d00faac6c464)

## Referencias

### MultinomialNB

- https://www.quora.com/How-does-multinomial-Naive-Bayes-work

- https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html

- https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes

- https://datascience.stackexchange.com/questions/30473/how-does-the-mutlinomial-bayess-alpha-parameter-affects-the-text-classificati

### AdaBoostClassifier

- https://scikit-learn.org/stable/modules/generated/sklearn.ensemble.AdaBoostClassifier.html

- https://blog.dfrnks.com/2018/07/15/machine-learning-algoritmo-AdaBoostClassifier.html