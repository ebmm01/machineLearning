---
title: 'Mining Educational Data to Predict Academic Dropouts: a Case Study in Blended Learning Course' 
---

## Resumo

_Mineração de dados educacionais para prever desistências acadêmicas: um estudo de caso no curso num curso semipresencial_ (tradução livre)

O _paper_ propõe um sistema de predição simples utilizando àrvores de decisão com o objetivo de prever a possibilidade de evasão de um aluno no meio do semestre com base em dados de anos anteriores. O foco do trabalho são cursos semipresenciais.

### Trabalho proposto 

Os dados obtidos consistem num conjunto de informações (logs) de uma disciplina obrigatória do segundo semestre de um curso de engenharia da Universidade de Kumamoto.  Os dados foram obtidos a partir da atividade de 717 alunos.

Como a disciplina é semipresencial, o foco maior na extração de features (carcterísticas/variáveis de entrada) foi na parte à distância. A atividade principal no __LMS__ (_Learning Management System_, ou Sistema de Gestão de Aprendizagem) consiste na aplicação de questionários relacionados ao(s) conteúdo(s) aplicado durante a semana. Foram cnosideradas 4 variáveis relacionadas ao quiz no _paper_:

|Variável|Medida     |Descrição |
|--|---|--|
|Frequência de tentativas de um questionário| Número médio de dias entre tentativas| Indicador de persistência dos alunos na resolução de questionários e esforço para concluir os questionários antes do prazo final|
|Duração da tentativa de um questionário|Tempo médio gasto para envios de tentativas (em minutos)| O curso é uma matéria fundamental de engenharia, portanto os testes consistem em problemas que levam tempo para serem resolvidos. Portanto, esse recurso pode ser o indicador para tentativas de adivinhação e estudantes com dificuldade em resolver o problema.|
|Número de atividades do questionário|--|Número total de eventos de atividades relacionadas ao questionário no LMS|
|Número de tentativas de questionários|--|Contagem de tentativas de questionário|

Foi utilizada uma árvore de decisão como modelo preditivo para classificar a evasão de alunos a partir das variáveis extraídas. Duas regras de decisão foram usadas para os alunos serem considerados desistentes: 

 - 1) Se todos os critérios do classificador forem atendidos;
 - 2) Se três dos quatro critérios do classificador forem atendidos.

Onde os critérios variavam de ano ano. Para o ano de 2012, por exemplo, foram obtidos os seguintes critérios:

|Variáveis |Critério|
|--|--|
|Frequência de tentativas de um questionário| > 11.16|
|Duração da tentativa de um questionário |< 9.2 __ou__  >20|
|Número de atividades do questionário| < 104|
|Número de tentativas de questionários| < 16|

Ou seja, se três ou mais das variáveis acima forem observadas num aluno, é muito provável que ele irá evadir.

## Refêrencias

Otgontsetseg Sukhbaatar, Kohichi Ogata, Tsuyoshi Usagawa - [Mining Educational Data to Predict Academic Dropouts: a Case Study in Blended Learning Course](https://ieeexplore-ieee-org.ez54.periodicos.capes.gov.br/stamp/stamp.jsp?tp=&arnumber=8650138) - Graduate School of Science and Technology, Kumamoto University, Kumamoto, Japan