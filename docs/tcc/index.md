---
title: TCC
---

## HOG SVM & XGBOOST

Obs.: A coluna __Ori.__ representa a origem do dataset. "__tcc__" significa que os valores foram obtidos durante a execução para obtenção dos dados, "__art__" representa os dados obtidos no artigo referenciado ao final da página e "__norm__" representa a execução num dataset normalizado.

Obs.: A execução normalizada foi feita "alinhando por baixo". Isso quer dizer que, para que o mesmo número de amostras (positivas e negativas) fosse executado nos algoritmos, foi escolhido o menor número. Nos datasets atuais, é o número de amostras negativas do PSU (500). Como a divisão treino-teste é 80/20, São usadas 400 amostras de teste e 100 para treino (negativas e positivas, totalizando 1000 amostras).

### INRIA

```
Treino: 1218 positive, 614 negative
Teste: 435 positive, 288 negative
```

|Ori.|Algoritmo|Acurácia|Precision|Recall|F1 Score|TN-FP-FN-TP|
|----|--|--|--|--|--|--|
|tcc |Linear SVM| 86,36%|86,66%|76,73%|81,39%|57% - 5% - 9% - 29%|
|norm |Linear SVM| 79,5%|78,64%|81%|79,80%|39% - 11% - 10% - 40%|
|__art__ |__Linear SVM__| __86%__|__92%__|__87%__|__89%__| __??__ |
|tcc |XGBoost|87,85%|94,19%|73,26%|82,42%|59% - 2% - 11% - 28%|
|norm |XGBoost|82%|80,76%|84%|82,35%|40% - 10% - 8% - 42%|
|__art__ |__XGBoost__|__82%__|__94%__|__80%__|__86%__| __??__ |

### PSU

- Resolução 960x720:

```
Treino: 815 positive, 400 negative
Teste: 204 positive, 100 negative
```

|Ori.|Algoritmo|Acurácia|Precision|Recall|F1 Score|TN-FP-FN-TP|
|----|--|--|--|--|--|--|
|tcc |Linear SVM| 84,21%|84,82%| 93,13%|88,78%|22% - 11% - 5% - 62%|
|norm |Linear SVM| 77,5%|79,56%| 74%|76%|41% - 9% - 13% - 37%|
|__art__ |__Linear SVM__| __82%__|__64%__| __74%__|__78%__| __??__ |
|tcc |XGBoost|80,59%|79,11%|96,50%|86,97%|15% - 18% - 2% - 64%|
|norm |XGBoost|77,5%|76,69%|79%|77,83%|38% - 12% - 11% - 39%|
|__art__ |__XGBoost__|__76%__|__53%__|__68%__|__69%__| __??__ |

- Resolução 256x256:

```
Treino: 840 positive, 400 negative
Teste: 211 positive, 100 negative
```

|Ori.|Algoritmo|Acurácia|Precision|Recall|F1 Score|TN-FP-FN-TP|
|----|--|--|--|--|--|--|
|tcc |Linear SVM| 83,55%|84,07%| 93,13%|88,37%|21% - 12% - 5% - 62%|
|norm |Linear SVM| 75,5%|79,31%| 69%|73,79%|41% - 9% - 15% - 35%|
|__art__ |__Linear SVM__| __82%__|__64%__| __74%__|__78%__| __??__ |
|tcc |XGBoost|79,60%|77,95%|97,05%|86,46%|15% - 18% - 2% - 65%|
|norm |XGBoost|76%|79,54%|70%|74,46%|41% - 9% - 15% - 35%|
|__art__ |__XGBoost__|__76%__|__53%__|__68%__|__69%__| __??__ |

Obs.: O artigo original não especifica qual a resolução foi utilizada, logo os dados foram espelhados em ambas as tabelas. 

Para o psu, foi realizado um split (a partir de um script para automatizar a tarefa) em 80-20 (treino-teste) randômico. Os dados estão desbalanceados, pendendo mais para amostras positivas (com pedestres)

## Yolov3

|Ori.|Dataset|aP|
|--|--|--|
| Yolo default (coco dataset) | INRIA | 96,18% |
| Yolo custom (INRIA) | INRIA | 91,41% |
| Yolo default (coco dataset) | PSU | 76,02% |
| Yolo custom (PSU) | PSU | 67,62% |
| Yolo default (coco dataset) | INRIA & PSU | 79,29% |
| Yolo custom (INRIA & PSU) | INRIA & PSU | 66,73% |


## Referências:

- R. M. Castelino, G. P. M. Pinheiro, B. J. G. Praciano, G. A. Santos, L. Weichenberger and R. T. D. S. Júnior, "Improving the Accuracy of Pedestrian Detection in Partially Occluded or Obstructed Scenarios," 2020 10th International Conference on Advanced Computer Information Technologies (ACIT), 2020, pp. 834-838, doi: 10.1109/ACIT49673.2020.9208877.

- M. Thu, N. Suvonvorn, and M. Karnjanadecha, “A new dataset
benchmark for pedestrian detection,” in Proceedings of the 3rd
International Conference on Biomedical Signal and Image Processing,
2018, pp. 17–22

- N. Dalal, “INRIA Person Dataset,” 2005. [Online]. Available:
http://pascal.inrialpes.fr/data/human/.