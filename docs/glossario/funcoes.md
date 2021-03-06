---
title: Conceitos diversos
---

## Notações diversas

- __Função de custo - J(Θ)__: Medida de desempenho. Dá uma ideia da quantidade de erros gerado pelo sistema em suas previsões.

- __Hipótese - hΘ(x)__: Função de previsão do sistema.

- __Taxa de aprendizagem - η__: Define o tamanho do passo a ser dado no [gradiente de descida](#gradiente-de-descida-ou-metodo-do-gradiente)

## Conceitos diversos

- __Lógica difusa__: forma de lógica multivalorada, na qual os valores de verdade das variáveis podem ser qualquer número real entre 0/falso e 1/verdadeiro, diferentemente do que se verifica na lógica booleana, segundo a qual os valores lógicos podem ser apenas 0 ou 1

- __Classes desequilibradas__ (_skewed constants_): Quando uma das classes é muito inferior às demais. Por exemplo, se num dataset de pacientes que possuem ou não cancer, somente 0,5% possuir câncer.

- __Clustering__: Um agrupamento de itens com base em características em comum. Muito utilizado em apdenziado não-supervisionado.

## Aprendizado de máquina (Machine learning)

__Arthur Samuel (1965)__: Campo de estudo que propicia a computadores a habilidade de aprender sem ser explicitamente programado.

__Tom Mitchell (1998)__: Problema de aprendizagem bem colocado: um programa de computador é orientado para aprender da experiência __E__, com respeito a alguma tarefa __T__ e alguma medida de performance __P__, se sua performance em __I__, como medida por P, melhora com a experiência __E__.

### Aprendizado supervisionado

Quando são apresentadas ao computador exemplos de entradas e saídas desejadas. O objetivo é aprender uma regra geral que mapeia as entradas para as saídas (ou uma [hipótese](#notacoes-diversas)). Ele pode ser categorizado em dois tipos:

- __Problemas de regressão__: Predizer a saída de valores contínuos (ou predizer um valor de saída real);

- __Problemas de classificação__: Predizer resultados em entradas discretas.

### Aprendizado não-supervisionado

No aprendizado não-supervisionado, os dados não são rotulados. O sistema tenta aprender sem um 'professor'.

## Regressão


### Linear

Regressão linear é uma equação para se estimar a condicional (valor esperado) de uma variável y, dados os valores de algumas outras variáveis x.

![](https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/LinearRegression.svg/300px-LinearRegression.svg.png)

### Logística

Regressão Logística é uma técnica de modelagem utilizada para lidar com variáveis binárias (0 ou 1). Ela permite estimar a probabilidade associada à ocorrência de determinado evento em face de um conjunto de variáveis explanatórias.

![](https://estatsite.files.wordpress.com/2018/08/linear_vs_logistic_regression.jpg?w=940)
Fonte da Imagem: https://www.machinelearningplus.com

## Support Vector Machine (SVM)

Uma máquina de vetores de suporte (SVM, do inglês: support vector machine) é um conceito na ciência da computação para um conjunto de métodos de aprendizado supervisionado que analisam os dados e reconhecem padrões, usado para classificação e análise de regressão. O SVM padrão toma como entrada um conjunto de dados e prediz, para cada entrada dada, qual de duas possíveis classes a entrada faz parte, o que faz do SVM um classificador linear binário não probabilístico. Dados um conjunto de exemplos de treinamento, cada um marcado como pertencente a uma de duas categorias, um algoritmo de treinamento do SVM constrói um modelo que atribui novos exemplos a uma categoria ou outra. Um modelo SVM é uma representação de exemplos como pontos no espaço, mapeados de maneira que os exemplos de cada categoria sejam divididos por um espaço claro que seja tão amplo quanto possível. Os novos exemplos são então mapeados no mesmo espaço e preditos como pertencentes a uma categoria baseados em qual o lado do espaço eles são colocados.

Em outras palavras, o que uma SVM faz é encontrar uma linha de separação, mais comumente chamada de hiperplano entre dados de duas classes. Essa linha busca maximizar a distância entre os pontos mais próximos em relação a cada uma das classes:

![](https://upload.wikimedia.org/wikipedia/commons/3/31/%D7%9E%D7%9B%D7%95%D7%A0%D7%AA_%D7%95%D7%95%D7%A7%D7%98%D7%A8%D7%99%D7%9D_%D7%AA%D7%95%D7%9E%D7%9B%D7%99%D7%9D_%D7%93%D7%95%D7%92%D7%9E%D7%90.jpg)
Fonte da Imagem: https://pt.wikipedia.org/wiki

## Função sigmóide

A função sigmóide é uma função matemática de amplo uso em campos como a economia e a computação. O nome "sigmóide" vem da forma em S do seu gráfico. Ela assume valores apenas entre 0 e 1.

Ela é definida como:

![](https://wikimedia.org/api/rest_v1/media/math/render/svg/faaa0c014ae28ac67db5c49b3f3e8b08415a3f2b)

E possui o seguinte gráfico: 

![](https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/Logistic-curve.png/220px-Logistic-curve.png)

## Gradiente de descida (ou método do gradiente)

O método do gradiente (ou método do máximo declive) é um método numérico usado em otimização. Para encontrar um mínimo (local) de uma função usa-se um esquema iterativo, onde em cada passo se toma a direção (negativa) do gradiente, que corresponde à direção de declive máximo. Pode ser encarado como o método seguido por um curso da água, na sua descida pela força da gravidade.

No âmbito do machine learning, é utilizada para otimizar a função de custo, buscando reduzir seu valor.

## Referências 

- [Método do gradiente](https://pt.wikipedia.org/wiki/M%C3%A9todo_do_gradiente)

- [Aprendizado de máquina](https://pt.wikipedia.org/wiki/Aprendizado_de_m%C3%A1quina#Tipos_de_problemas_e_tarefas)

- [Regressão Linear](https://pt.wikipedia.org/wiki/Regress%C3%A3o_linear)

- [Mãos à Obra: Aprendizado de Máquina com Scikit-Learn & TensorFlow](https://www.amazon.com.br/M%C3%A3os-Obra-Aprendizado-Scikit-Learn-TensorFlow/dp/8550803812)

- [Máquina de vetores de suporte](https://pt.wikipedia.org/wiki/M%C3%A1quina_de_vetores_de_suporte)