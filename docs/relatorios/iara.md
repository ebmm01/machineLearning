---
title: Iara - Prof. Alberto Ferreira de Souza
---

## Categorização de artigos

Essa seção tem por objetivo categorizar alguns dos artigos do Prof. Alberto Ferreira de Souza com ênfase em veículos autônomos. 

### Template:

Para isso, o seguinte template será seguido:

Título

- Ano
- Categoria(s)
- Técnicas/ <br> Algoritmos

- Breve resumo

...

### Deep traffic light detection by overlaying synthetic context on arbitrary natural images 

- __Ano__:  Dez/2020
- __Categoria(s)__: Detecção de objetos (semáforos)
- __Técnicas/Algoritmos__:  Faster R-CNN (também cita YOLO)
- __Breve resumo__:

> O trabalho propõe a utilização de imagens geradas artificialmente para o treinamento de redes neurais de forma a sanar algumas das principais dificuldades encontradas em trabalhos anteriores.

Trabalhos anteriores lidavam com datasets não balenceados (ausencia de status amarelo, por exemplo) e dificuldade de se categorizar grandes quantidades de imagens

A solução proposta se inicia pelo dataset, buscando ser o máximo balanceado possível, gerando imagens artificiais a partir de um fundo (uma imagem fora do contexto de trânsito) e um 'fronte' (uma imagem gerada artificialmente simulando um cenário de trânsito com sinais). Para validação foram usados 4 datasets: LISA (Laboratory for Intelligent & Safe Automobiles), Udacity, LaRA (La Route Automatisée), e um proprietário. 

Os modelos foram treinando usando uma implementação pública disponibilizada no Tensorflow, que utiliza __Faster R-CNN__.


### Keep your Eyes on the Lane: Real-time Attention-guided Lane Detection

- __Ano__:  Nov/2020
- __Categoria(s)__: Detecção de objetos (pistas)
- __Técnicas/Algoritmos__:  LaneATT (modelo proposto)
- __Breve resumo__:

> O trabalho propõe um modelo para a detecção de pistas chamado LaneATT, que utiliza backbones leves CNN ResNet

O modelo proposto, LaneATT, é um modelo de estágio único baseado em âncoras, como YOLOv3 ou SSD (Single Shot MultiBox Detector) para detecção de pistas. A detecção de âncoras é feita utilizando linhas ao invés de caixas. 

### Deep Traffic Sign Detection and Recognition Without Target Domain Real Images

- __Ano__:  Jul/2020
- __Categoria(s)__: Detecção de objetos (sinais de trânsito)
- __Técnicas/Algoritmos__:  Faster R-CNN para a validação das imagens geradas
- __Breve resumo__:

> O trabalho propõe um novo método de geração de banco de dados que requer apenas (i) imagens naturais arbitrárias, ou seja, não requer nenhuma imagem real do domínio-alvo e (ii) modelos dos sinais de trânsito.

Trabalhos anteriores já propuseram tal método, porém focados apenas na localização de sinais de trânsito, e não reconhecimento dos mesmos. Para o trabalho proposto, o dataset de treinamento é gerado em três passos: 
    
    - Primeiramente os templates de sinais de trânsito de interesse são obtidos;
    - Depois imagens de fundo (background) que não pertencem ao domínio de interesse são obtidas (ImageNet, Microsoft COCO);
    - Por fim, as amostras de treinamento são geradas, compostas por imagens com sinais de trânsito anotadas. 

Dessa forma, os principais problemas relacionados à dificuldade de obtenção de imagens (datasets) de sinais de trânsito são sanados: a dificuldade em se anotar datasets volumosos e também de se obtê-los.

### Image-Based Real-Time Path Generation Using Deep Neural Networks 

- __Ano__:  Jul/2020
- __Categoria(s)__: Planejamento de viagens/ caminho
- __Técnicas/Algoritmos__: CNN nomeado DeepPath (composto de três seções: WideResNet38, DeepLabV3 e uma seção final que realiza um up-sampling bilinear)
- __Breve resumo__:

> O trabalho propõe um planejador de viagens/caminhos em tempo real baseado em imagem para o carro autônomo IARA, denominado DeepPath, que usa CNN para inferir caminhos de imagens

Para a elaboração de caminhos pelo DeepPath, são necessárias apenas imagens do posto de vista frontal de um veículo, enquanto outros métodos requerem imagens aéreas. Em comparação com trabalhos anteriores, o DeepPath realiza apenas o planejamento do caminho, e não do movimento. Isso se dá pelo fato de ele ser desenvolvido para o veículo autônomo IARA, cujo sistema autônomo lida com planejamento de caminho e de movimento em diferente subsistemas separados.

Durante a operação de direção autônoma o DeepPath recebe um input (imagem) da câmera frontal do IARA e a localização atual do subsistema localizador, gerando uma saída (caminho). Tal tarefa é realizada a partir da utilização de uma CNN para inferir o modelo do caminho. O modelo do caminho é então transformado em um caminho real: 

    - (i) gerando o caminho no sistema de coordenadas do IARA e então 
    - (ii) transformando cada posição do caminho no sistema de coordenadas do IARA em outra posição no sistema de coordenadas mundial.


### A Large-Scale Mapping Method Based on Deep Neural Networks Applied to Self-Driving Car Localization 

- __Ano__:  Jul/2020
- __Categoria(s)__: Localização
- __Técnicas/Algoritmos__: DNN nomeado NeuralMapper 
- __Breve resumo__:

> O trabalho propõe a criação do NeuralMapper: um subsistema da arquitetura de software de autonomia da IARA que recebe dados do sensor LiDAR como entrada e gera como saída um mapa de grade de ocupação (Occupancy Grid Mapping, OGM) ao redor do carro.

A arquitetura DNN do NeuralMapper consiste em três camadas: um encoder, um context module  e um decoder. Ao final de uma predição será dito se uma grade de ocupação (0.2m X 0.2m) está livre, ocupada ou desconhecida.

A principal motivação do desenvolvimento do NeuralMapper foi a substituição do algoritmo OGM, para potencialmente reduzir a quantidade de linhas de código e a capacidade das redes neurais de lidarem com a não-linearidade dos dados. Ao final conclue-se que o NeuralMapper pode substituir o algoritmo OGM no IARA.

### PolyLaneNet: Lane Estimation via Deep Polynomial Regression 

- __Ano__:  Jul/2020
- __Categoria(s)__: Detecção de pistas
- __Técnicas/Algoritmos__: CNN nomeado PolyLaneNet (com um backbone EfficientNet-b0), mas também cita SCNN, Line-CNN, ENet-SAD e FastDraw
- __Breve resumo__:

> O trabalho propõe a criação do PolyLaneNet, uma CNN para estimativa de marcações de faixa de ponta a ponta.

No trabalho proposto, a PolyLaneNet recebe de input (entrada) imagens de uma câmera frontal montada no veículo e gera polinômios que representam cada marcação de faixa na imagem, junto com os domínios para esses polinômios e pontuações de confiança para cada faixa. Trabalhos anteriores também focavam em detecção de pistas baseadas em modelos e/ou aprendizagem  de máquina ( sem redes neurais ) porém não eram tão robustos para fatores como alteração de iluminação, condições climáticas dentre outros. Alguns modelos que utilizam redes neurais foram elaborados, porém ou não possuem o código fonte liberado para o público, ou não podem ter seus resultados reproduzidos. 

Dessa forma, a PolyLaneNet se diferencia não somente por ter uma performance similar à modelos considerados _estado-da-arte_, mas também por permitir a reprodutibilidade. 