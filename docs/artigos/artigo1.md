---
title: 'Predição à evasão escolar: Estudo de caso aplicado no IFSULDEMINAS'
---

## Resumo

O artigo ___Predição à evasão escolar: Estudo de caso aplicado no IFSULDEMINAS___ fala sobre a aplicação de técnicas de Machine Learning para automação na prediçao de evasão escolar no Instituto Federal de Educação, Ciência e Tecnologia do Sul de Minas (IFSULDEMINAS). Tal predição é (era) feita manualmente, o que levava tempo, impossibilitando uma atuação mais prática para evitar a evasão de alunos que pudessem estar em tal condição.

O universo de interesse da pesquisa foram estudantes matriculados em 2013 nos seguintes cursos técnicos: __Informática, Comunicação Visual, Produção em moda e
Enfermagem__. Os atributos selecionados para a predição foram  __sexo, idade, etnia, estado civil, renda familiar, procedência escolar e as notas das disciplinas do
primeiro semestre dos cursos__, sendo analisados dados de 54 alunos que concluíram os cursos e mais 45 alunos que não concluíram. 

Os classificadores escolhidos foram ___SimpleCart, J48, RandomForest___ (todos àrvores de decisão) e ___Naive Bayes___, com os seguintes resultados: 

|Classificador| Acurácia por curso||||
|--|--|--|--|--|
| |Informática| Com. Visual |Produção em moda| Enfermagem|
|SimpleCart |64,28% |54,16%| 89,47% |92,86%|
|J48 |64,28%| 66,66% |94,75% |82,14%|
|RandomForest| 75% |79,16% |89,47% |85,71%|
|Naive Bayes| 67,86%| 79,16%| 89,47%| 85,71%|

Não são dados detalhes sobre a arquitetura utilizada, nem sobre o modelo utilizado.

## Referências

Carla Fernandes da SILVA; Clayton Silva MENDES -  [PREDIÇÃO À EVASÃO ESCOLAR: Estudo de caso aplicado no IFSULDEMINAS – Campus Passos](https://pdfs.semanticscholar.org/f997/c81a9083665f6de427d7698a788733dfebfa.pdf)
. 