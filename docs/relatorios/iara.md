---
title: Iara - Prof. Alberto Ferreira de Souza
---

## Categorização de artigos & sumário

Essa seção tem por objetivo categorizar alguns dos artigos do Prof. Alberto Ferreira de Souza com ênfase em veículos autônomos. 

|Índice| Ano| Categoria(s)| Técnicas/Algoritmos |
|--|--|--|--|
| <a href="#id_1">[1]</a> | Dez/2020 |Detecção de objetos (semáforos) | Faster R-CNN (também cita YOLO) |
| <a href="#id_2">[2]</a> | Nov/2020 |Detecção de objetos (pistas) | LaneATT (modelo proposto) |
| <a href="#id_3">[3]</a> | Jul/2020 |Detecção de objetos (sinais de trânsito) | Faster R-CNN para a validação das imagens geradas |
| <a href="#id_4">[4]</a> | Jul/2020 |Planejamento de viagens/ caminho | CNN nomeado DeepPath (composto de três seções: WideResNet38, DeepLabV3 e uma seção final que realiza um up-sampling bilinear) |
| <a href="#id_5">[5]</a> | Jul/2020 |Localização | DNN nomeado NeuralMapper |
| <a href="#id_6">[6]</a> | Jul/2020 |Detecção de pistas | CNN nomeado PolyLaneNet (com um backbone EfficientNet-b0), mas também cita SCNN, Line-CNN, ENet-SAD e FastDraw |
| <a href="#id_7">[7]</a> | Abr/2020 |Localização | Distribuição Gaussiana, Normalized Mutual Information (NMI) |
| <a href="#id_8">[8]</a> | Nov/2019 |Detecção de objetos (pedestres) & planejamento de caminhos | YOLO v3, R-FCNN |
| <a href="#id_9">[9]</a> | Out/2019 |Predição de volume | Generalized ICP |
| <a href="#id_10">[10]</a> | Out/2019 |Detecção de objetos (semáforos) & predição de estado | Deep Convolutional neural network (CNN) com um backbone ResNet-50 modificado  |
| <a href="#id_11">[11]</a> | Jul/2019 |Geração de grades de ocupação (sem objetos não-estáticos) | DeepLabv3+ (que usa uma variante do ResNet-101) para a Segmentação de imagem semântica e _Density-Based Spatial Clustering of Applications with Noise_ (DBSCAN) para o agrupamento de pontos  |
| <a href="#id_12">[12]</a> | Jul/2019 | Detecção de objetos (veículos à longas distâncias)| YOLOv2, mas também cita ClusterNet  |
| <a href="#id_13">[13]</a> | Jul/2019 | Detecção de objetos & geração de datasets | CycleGAN para geração do dataset, Faster R-CNN para treinamento e POC (também cita YOLO e RetinaNet para trabalhos futuros)  |
| <a href="#id_14">[14]</a> | Jul/2019 | Detecção de objetos (sinais de trânsito) & geração de datasets | Faster R-CNN |
| <a href="#id_15">[15]</a> | Jul/2019 | Detecção de objetos (semáforo) & detecção de estado dos mesmos | YOLOv3, mas também cita Faster R-CNN e DeepTLR |
| <a href="#id_16">[16]</a> | Out/2018 | Remoção de ruído de mapas de grade de ocupação (OGM) | Map decay, GraphSLAM |
| <a href="#id_17">[17]</a> | Ago/2018 | Estimação de direção de rumo (para alinhar o veículo à estrada) | CNN (inspirada na AlexNet com algumas modificações) |
| <a href="#id_18">[18]</a> | Ago/2018 | Localização a partir do reconhecimento de lugares | Rede Híbrida entre _Weightless Neural Networks_ (WNN, nomeada VibGL) & _Convolutional Neural Network_ (CNN, baseada na VGG-16) |

### Template:

Para isso, o seguinte template será seguido:

Título

- Ano
- Categoria(s)
- Técnicas/ <br> Algoritmos
- Breve resumo


<div id="id_1"></div>

### 1 - Deep traffic light detection by overlaying synthetic context on arbitrary natural images 


- __Ano__:  Dez/2020
- __Categoria(s)__: Detecção de objetos (semáforos)
- __Técnicas/Algoritmos__:  Faster R-CNN (também cita YOLO)
- __Breve resumo__:

> O trabalho propõe a utilização de imagens geradas artificialmente para o treinamento de redes neurais de forma a sanar algumas das principais dificuldades encontradas em trabalhos anteriores.

Trabalhos anteriores lidavam com datasets não balenceados (ausencia de status amarelo, por exemplo) e dificuldade de se categorizar grandes quantidades de imagens

A solução proposta se inicia pelo dataset, buscando ser o máximo balanceado possível, gerando imagens artificiais a partir de um fundo (uma imagem fora do contexto de trânsito) e um 'fronte' (uma imagem gerada artificialmente simulando um cenário de trânsito com sinais). Para validação foram usados 4 datasets: LISA (Laboratory for Intelligent & Safe Automobiles), Udacity, LaRA (La Route Automatisée), e um proprietário. 

Os modelos foram treinando usando uma implementação pública disponibilizada no Tensorflow, que utiliza __Faster R-CNN__.

<div id="id_2"></div>

### 2 - Keep your Eyes on the Lane: Real-time Attention-guided Lane Detection

- __Ano__:  Nov/2020
- __Categoria(s)__: Detecção de objetos (pistas)
- __Técnicas/Algoritmos__:  LaneATT (modelo proposto)
- __Breve resumo__:

> O trabalho propõe um modelo para a detecção de pistas chamado LaneATT, que utiliza backbones leves CNN ResNet

O modelo proposto, LaneATT, é um modelo de estágio único baseado em âncoras, como YOLOv3 ou SSD (Single Shot MultiBox Detector) para detecção de pistas. A detecção de âncoras é feita utilizando linhas ao invés de caixas. 

<div id="id_3"></div>

### 3 - Deep Traffic Sign Detection and Recognition Without Target Domain Real Images

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

<div id="id_4"></div>

### 4 - Image-Based Real-Time Path Generation Using Deep Neural Networks 

- __Ano__:  Jul/2020
- __Categoria(s)__: Planejamento de viagens/ caminho
- __Técnicas/Algoritmos__: CNN nomeado DeepPath (composto de três seções: WideResNet38, DeepLabV3 e uma seção final que realiza um up-sampling bilinear)
- __Breve resumo__:

> O trabalho propõe um planejador de viagens/caminhos em tempo real baseado em imagem para o carro autônomo IARA, denominado DeepPath, que usa CNN para inferir caminhos de imagens

Para a elaboração de caminhos pelo DeepPath, são necessárias apenas imagens do posto de vista frontal de um veículo, enquanto outros métodos requerem imagens aéreas. Em comparação com trabalhos anteriores, o DeepPath realiza apenas o planejamento do caminho, e não do movimento. Isso se dá pelo fato de ele ser desenvolvido para o veículo autônomo IARA, cujo sistema autônomo lida com planejamento de caminho e de movimento em diferente subsistemas separados.

Durante a operação de direção autônoma o DeepPath recebe um input (imagem) da câmera frontal do IARA e a localização atual do subsistema localizador, gerando uma saída (caminho). Tal tarefa é realizada a partir da utilização de uma CNN para inferir o modelo do caminho. O modelo do caminho é então transformado em um caminho real: 

    - (i) gerando o caminho no sistema de coordenadas do IARA e então 
    - (ii) transformando cada posição do caminho no sistema de coordenadas do IARA em outra posição no sistema de coordenadas mundial.


<div id="id_5"></div>

### 5 - A Large-Scale Mapping Method Based on Deep Neural Networks Applied to Self-Driving Car Localization 

- __Ano__:  Jul/2020
- __Categoria(s)__: Localização
- __Técnicas/Algoritmos__: DNN nomeado NeuralMapper 
- __Breve resumo__:

> O trabalho propõe a criação do NeuralMapper: um subsistema da arquitetura de software de autonomia da IARA que recebe dados do sensor LiDAR como entrada e gera como saída um mapa de grade de ocupação (Occupancy Grid Mapping, OGM) ao redor do carro.

A arquitetura DNN do NeuralMapper consiste em três camadas: um encoder, um context module  e um decoder. Ao final de uma predição será dito se uma grade de ocupação (0.2m X 0.2m) está livre, ocupada ou desconhecida.

A principal motivação do desenvolvimento do NeuralMapper foi a substituição do algoritmo OGM, para potencialmente reduzir a quantidade de linhas de código e a capacidade das redes neurais de lidarem com a não-linearidade dos dados. Ao final conclue-se que o NeuralMapper pode substituir o algoritmo OGM no IARA.

<div id="id_6"></div>

### 6 - PolyLaneNet: Lane Estimation via Deep Polynomial Regression 

- __Ano__:  Jul/2020
- __Categoria(s)__: Detecção de pistas
- __Técnicas/Algoritmos__: CNN nomeado PolyLaneNet (com um backbone EfficientNet-b0), mas também cita SCNN, Line-CNN, ENet-SAD e FastDraw
- __Breve resumo__:

> O trabalho propõe a criação do PolyLaneNet, uma CNN para estimativa de marcações de faixa de ponta a ponta.

No trabalho proposto, a PolyLaneNet recebe de input (entrada) imagens de uma câmera frontal montada no veículo e gera polinômios que representam cada marcação de faixa na imagem, junto com os domínios para esses polinômios e pontuações de confiança para cada faixa. Trabalhos anteriores também focavam em detecção de pistas baseadas em modelos e/ou aprendizagem  de máquina ( sem redes neurais ) porém não eram tão robustos para fatores como alteração de iluminação, condições climáticas dentre outros. Alguns modelos que utilizam redes neurais foram elaborados, porém ou não possuem o código fonte liberado para o público, ou não podem ter seus resultados reproduzidos. 

Dessa forma, a PolyLaneNet se diferencia não somente por ter uma performance similar à modelos considerados _estado-da-arte_, mas também por permitir a reprodutibilidade. 

Ao final verifica-se uma precisão consideravelmente alta para linhas mais próximas à camera, e menor conforme a distância até o horizonte aumenta (por um provável desbalanceamento nos dados) e um viés da rede para linhas em detrimento de curvas acentuadas.

<div id="id_7"></div>

### 7 - Evaluating the Limits of a LiDAR for an Autonomous Driving Localization

- __Ano__:  Abr/2020
- __Categoria(s)__: Localização
- __Técnicas/Algoritmos__: Distribuição Gaussiana, Normalized Mutual Information (NMI)
- __Breve resumo__:

> O trabalho apresenta uma análise para mostrar o quão simples pode ser um sensor LiDAR sem reduzir a precisão da localização que usa mapas rodoviários e de satélite juntos para posicionar globalmente o carro, e propõe uma nova técnica para localização global de um veículo.

No trabalho proposto, os resultados mostram que mesmo com simplificações significativas no sensor LiDAR, ainda é possível realizar a localização do veículo com precisão suficiente para algumas aplicações (com testes realizados no IARA). As simplificações se dão pela redução dos scans horizontais, linhas verticais, _framerate_ e barulho (_noise_). Verifica-se que uma redução dos scans horizontais de 100% para 12% aumenta o Erro médio absoluto (_MAE_) de 0.8m para apenas 0.84m. 

Outros cenários foram testados, mostrando que uma redução nos custos e tipo de sensores LiDAR podem ser feitas sem impactar significativamente a performance dos sistemas de localização.

<div id="id_9"></div>

### 9 - Simple and Effective Load Volume Estimation in Moving Trucks using LiDAR

- __Ano__:  Out/2019
- __Categoria(s)__: Predição de volume
- __Técnicas/Algoritmos__: Generalized ICP 
- __Breve resumo__:

> O trabalho propõe uma nova técnica para estimar o volume de cargas de caminhões em movimento usando dois sensores LiDARs.

<div id="id_10"></div>

### 10 - Relevant Traffic Light Localization via Deep Regression

- __Ano__:  Out/2019
- __Categoria(s)__: Detecção de objetos (semáforos) & predição de estado
- __Técnicas/Algoritmos__: Deep Convolutional neural network (CNN) com um backbone ResNet-50 modificado 
- __Breve resumo__:

> O trabalho propõe uma nova técnica para estimar o volume de cargas de caminhões em movimento usando dois sensores LiDARs.

Um dos problemas enfrentados por veículos autônomos é a detecção de estado de um semáforo (vermelho, amarelo ou verde). Tal problema ja foi abordado por alguns autores, porém envolve a utilização de uma série de sensores consideravelmente caros (LiDAR, câmeras, detectores de luz, dentre outros) e funciona em cenários bem restritos.

Para resolver esse problema, o trabalho propõe um modelo que utiliza um modelo de regressão profunda (_deep regression model_) para prever as coordenadas bidimensionais de um semáforo numa imagem, obtendo uma acurácia indo de 80.22 até 88.59%, a depender do cenário de avaliação.

<div id="id_11"></div>

### 11 - Removing Movable Objects from Grid Maps of Self-Driving Cars Using Deep Neural Networks

- __Ano__:  Jul/2019
- __Categoria(s)__: Geração de grades de ocupação (sem objetos não-estáticos)
- __Técnicas/Algoritmos__:  DeepLabv3+ (que usa uma variante do ResNet-101) para a Segmentação de imagem semântica e _Density-Based Spatial Clustering of Applications with Noise_ (DBSCAN) para o agrupamento de pontos
- __Breve resumo__:

> O trabalho propõe uma técnica para remover vestígios de objetos móveis de mapas de grade de ocupação (OGM) com base em redes neurais profundas.

Até uma data anterior ao momento de publicação do paper, um dos problemas que a IARA enfrentava era não possuir uma forma de gerar mapas de grade de ocupação (OGM) de forma automática, o que forçava a necessidade de um trabalho manual para a geração dos mesmos.

Dessa forma, o trabalho propõe uma técnica chamada _Enhanced OGM generation_ (E-OGM-G), baseada na técnica _Large-Scale Environment Mapping System_ (LEMS), para gerar OGM "limpos". A técnica recebe como entrada imagens e nuvens de pontos, sendo processada com uma Segmentação de imagem semântica, remoção de piso, agrupamento de pontos e remoção de objetos móveis para, por fim, gerar um OGM limpo.

<div id="id_12"></div>

### 12 - Bio-Inspired Foveated Technique for Augmented-Range Vehicle Detection Using Deep Neural Networks

- __Ano__:  Jul/2019
- __Categoria(s)__: Detecção de objetos (veículos à longas distâncias)
- __Técnicas/Algoritmos__: YOLOv2, mas também cita ClusterNet
- __Breve resumo__:

> O trabalho propõe uma técnica de renderização otimizada (_foveat_) bio-inspirada para detectar carros em uma câmera de visão de longo alcance usando uma rede neural convolucional profunda

A técnica proposta no trabalho parte da ideia de que os humanos conseguem detectar facilmente outros veículos a longas distâncias observando determinados pontos no horizonte; a partir disso propõe-se a elaboração de um modelo que utiliza como entrada imagens de câmera (ao contrário de dados de sensores RADAR ou LiDAR, que são consideravelmente mais caros).

O _augmented-range vehicle detection system_(ARVDS, modelo proposto) funciona da seguinte forma: uma imagem de entrada é recebida pelo sistema a partir da câmera. A partir do sistema de projeção de _waypoints_ do IARA são realizados cortes na imagem. A partir da imagem original e dos cortes gerados é aplicada a rede YOLOv2 para a detecção de veículos. 

Ao final , o ARVDS foi capaz de aumentar a precisão de detecção de veículos distantes de 29.51% para 63.15%.

<div id="id_13"></div>

### 13 - Cross-Domain Car Detection Using Unsupervised Image-to-Image Translation: From Day to Night

- __Ano__:  Jul/2019
- __Categoria(s)__: Detecção de objetos & geração de datasets   
- __Técnicas/Algoritmos__: CycleGAN para geração do dataset, Faster R-CNN para treinamento e POC (também cita YOLO e RetinaNet para trabalhos futuros)
- __Breve resumo__:

> O trabalho propõe um método para treinar um sistema de detecção de um veículo autônomo com dados anotados de um domínio de origem (imagens diurnas) sem exigir as anotações de imagem do domínio alvo (imagens noturnas)

O trabalho cita a dificuldade de treinar e testar modelos de alta-performance em determinado domínio, mas o modelo é treinado em  um domínio distinto, porém análogo (por exemplo, ter a intenção de se detectar semáforos em cenas noturnas mas só possuir um dataset com imagens de semáforos durante o dia).  

Para isso, o modelo proposto recebe como input imagens diurnas anotadas (com bounding boxes) e imagens noturnas sem nenhum tipo de anotação, e gera imagens falsas utilizando a rede CycleGAN. As anotações são então copiadas para as imagens falsas, que agora possuem o contexto noturno sem alterar fatos importantes (como posições de veículos, sinais de trânsito e semáforos). Na sequência, é escolhido um framework Faster R-CNN para a detecção de objetos.

Ao final, verifica-se que a adição das imagens geradas artificialmente é capaz de melhorar a performance do modelo de detecção de objetos em 10.7%. Também é sugerido como trabalhos futuros utilizar outros detectores de objetos "estado-da-arte" como YOLO e RetinaNet

<div id="id_14"></div>

### 14 - Effortless Deep Training for Traffic Sign Detection Using Templates and Arbitrary Natural Images

- __Ano__:  Jul/2019
- __Categoria(s)__: Detecção de objetos (sinais de trânsito) & geração de datasets
- __Técnicas/Algoritmos__: Faster R-CNN
- __Breve resumo__:

> O trabalho propõe um método de geração de datasets que requer apenas: (i) imagens naturais arbitrárias, ou seja, não requer nenhuma imagem real do domínio de interesse, e (ii) modelos dos sinais de trânsito, ou seja, modelos criados sinteticamente para ilustrar a aparência da categoria de um sinal de trânsito

Trabalhos anteriores já propuseram tal método, porém focados apenas na localização de sinais de trânsito, e não reconhecimento dos mesmos. Para o trabalho proposto, o dataset de treinamento é gerado em três passos: 
    
- Primeiramente os templates de sinais de trânsito de interesse são obtidos;
- Depois imagens de fundo (background) que não pertencem ao domínio de interesse são obtidas (ImageNet, Microsoft COCO);
- Por fim, as amostras de treinamento são geradas, compostas por imagens com sinais de trânsito anotadas. 

Dessa forma, os principais problemas relacionados à dificuldade de obtenção de imagens (datasets) de sinais de trânsito são sanados: a dificuldade em se anotar datasets volumosos e também de se obtê-los.

Obs.: O trabalho é muito parecido ao realizado em <a href="#id_3">[3]</a>. O principal ponto de diferença entre eles é:
    
-  Enquanto <a href="#id_3">[3]</a> foca em descobrir cada classe dos sinais de trânsito (ex.: diferenciar placas de velocidade com valores diferentes), <a href="#id_14">[14]</a> foca apenas na detecção do mesmo, sem classificá-los;

<div id="id_15"></div>

### 15 - Traffic Light Recognition Using Deep Learning and Prior Maps for Autonomous Cars

- __Ano__:  Jul/2019
- __Categoria(s)__: Detecção de objetos (semáforo) & detecção de estado dos mesmos
- __Técnicas/Algoritmos__: YOLOv3, mas também cita Faster R-CNN e DeepTLR
- __Breve resumo__:

> O trabalho propõe integrar o poder de detecção baseada em aprendizagem profunda com os mapas anteriores usados pela _IARA_ para reconhecer os semáforos relevantes de rotas predefinidas.

Trabalhos anteriores já abordaram a questão de reconhecimento de semáforos, porém nenhum se propôs a utilizar redes neurais em conjunto com dados prévios de mapas para "avisar" onde potencialmente haverá um sinal. 

Dessa forma, o trabalho propõe utilizar os dados de mapas gerados pela IARA através dos sensores LiDAR e câmeras, em conjunto com a rede YOLOv3, para detectar semáforos e classificar o estado dos mesmos.

O treinamento e validação do modelo foi realizado utilizando os datasets _DriveU Traffic Light Dataset_ (DTLD) e _LISA Traffic Light Dataset_ (LISATLD), ambos disponíveis de forma pública. Ao final a precisão variou de 60.86 à 88.59%, a depender do cenário e variáveis avaliadas.


<div id="id_16"></div>


### 16 - Memory-like Map Decay for Autonomous Vehicles based on Grid Maps

- __Ano__:  Out/2018
- __Categoria(s)__: Remoção de ruído de mapas de grade de ocupação (OGM)
- __Técnicas/Algoritmos__: Map decay, GraphSLAM
- __Breve resumo__:

> O trabalho propõe uma estratégia para corrigir imperfeições em mapas de grade de ocupação (OGM) denominada decaimento de mapa (Map Decay), 

O algoritmo proposto no trabalho, _Map decay_, usa como inspiração as habilidades do cérebro de liberar informações que não são mais necessárias da memória de curto prazo e de dar sentido a dados sensoriais incompletos, preenchendo-os com conhecimento de longo prazo. Dessa forma, ele torna-se uma solução simples e eficiente para lidar com imperfeições causadas por objetos em movimento.

<div id="id_17"></div>

### 17 - Heading Direction Estimation Using Deep Learning with Automatic Large-scale Data Acquisition

- __Ano__:  Ago/2018
- __Categoria(s)__: Estimação de direção de rumo (para alinhar o veículo à estrada)
- __Técnicas/Algoritmos__: CNN (inspirada na AlexNet com algumas modificações)
- __Breve resumo__:

> O trabalho propõe uma abordagem para o problema de estimar a direção de rumo que mantém o veículo alinhado com a direção da estrada para Sistemas avançados de assistência ao motorista (do inglês _ADAS_)

O sistema proposto utiliza plataformas públicas disponíveis (como _Open Street Maps_ e _Google street view_) para a obtenção dos dados e anotação dos mesmos, obtendo uma base de dados consideravelmente grande. Na sequência, a base de dados obtida é utilizada para treinar uma rede CNN que irá atacar o problema proposto, recebendo como entrada uma única imagem, prevendo a diferença na orientação atual do carro e a orientação "ideal" do carro 4 metros à frente na estrada. 

Trabalhos anteriores já buscaram abordar esse problema, porém caiam em questões de complexidade algorítmica, dificuldade de generalização ou utilização de sensores caros, como LiDAR.  

<div id="id_18"></div>

### 18 - Visual Global Localization with a Hybrid WNN-CNN Approach

- __Ano__:  Ago/2018
- __Categoria(s)__: Localização a partir do reconhecimento de lugares
- __Técnicas/Algoritmos__: Rede Híbrida entre _Weightless Neural Networks_ (WNN, nomeada VibGL) & _Convolutional Neural Network_ (CNN, baseada na VGG-16)
- __Breve resumo__:

> O trabalho propõe uma abordagem híbrida utilizando redes WNN e CNN para resolver o problema de localização global usando as informações topológicas e métricas para aproximar a posição atual do veículo, sendo bastante útil em ambientes onde não é possível utilizar GPS ()

O paper ja abordou o problema de reconhecimento de lugar (_place recognition_) em trabalhos anteriores, gerando um sistema de reconhecimendo conhecido como _VibGL_ (WNN). 

Para o trabalho proposto, a abordagem é dupla: (i) um WNN para resolver o reconhecimento de lugar como um problema de classificação e (ii) uma CNN para resolver a localização visual (_visual localization_) como um problema de regressão métrica.

O sistema funciona da seguinte forma: dada uma imagem de câmera ao vivo, o primeiro sistema (i) recupera a imagem mais semelhante e sua pose associada, enquanto o último (ii) compara a imagem coletada com a imagem de câmera ao vivo para gerar uma pose relativa 6D. O resultado final é uma estimativa da pose atual do robô/veículo autônomo (IARA)

Ao final, o sistema é capaz de localizar o veículo 90% do tempo com um erro médio de 1.2m, contra 1.12m do sistema _SLAM_ e 0.37m do GPS, ambos com 89% de localização.

<div id="id_19"></div>

### 19 - Mapping road lanes using laser remission and deep neural networks

- __Ano__:  Ago/2018
- __Categoria(s)__: 
- __Técnicas/Algoritmos__: Efficient Neural Network (ENet) DNN
- __Breve resumo__:

> O trabalho propõe a utilização de redes neurais profundas (DNN) para resolver o problema de inferir a posição e propriedades relevantes de vias urbanas com sinalização horizontal (faixas/marcações na pista) pobre ou ausente, de forma a permitir a operação de carros autônomos em tais situações.

O trabalho cita o fato de que, anteriormente ao projeto desenvolvido, o IARA (veículo autônomo), não possuia um mecanismo automático para inferir as faixas das estradas, utilizando _Road Definition Data Files_ (RDDF).

Para o desenvolvimento da rede, um dataset foi elaborado a partir da construção de mapas de estradas utilizando dados do sensor LiDAR (Laser Remission) na região da UFES. O dataset foi anotado manualmente, e utilizado para o treinamento e validação da rede DNN. 

Ao final do experimento, obteve-se uma acurácia média de 83.7%. Tal valor, de acordo com o paper, poderia ser superior, visto que a anotação manual possui imperfeições por ser bastante trabalhosa, impactando no treinamento da rede.
