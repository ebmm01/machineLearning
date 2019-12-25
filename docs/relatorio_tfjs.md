---
title: Relatório TensorflowJS
---

## TensorflowJS

O TensorFlow.js é uma biblioteca JavaScript acelerada por hardware de código aberto para treinamento e implantação de modelos de aprendizado de máquina.


## O projeto

O projeto consiste num site em que é possível enviar uma imagem e obter como resultado qual a possibilidade de determinados elementos estarem nelas. A ideia é que toda a rede neural seja carregada __client side__, ou seja, no próprio navegador do usuário. Isso é possível graças ao TensorflowJS e abre possibilidades interssantes, como o uso do hardware do usuário, possibilidade de se usar um celular, além de trazer [maior privacidade](https://www.quora.com/What-are-the-advantages-of-running-a-Machine-Learning-algorithm-using-a-Javascript-ML-library-like-Tensorflow-js-Isnt-better-to-train-a-model-on-the-server-side)

Os modelos utilizados, [VGG16](#vgg16) e [MobileNet](#mobilenet), foram importados do Keras e convertidos para um modelo tfjs usando um [script python](https://github.com/ebmm01/tensorflowjs/blob/master/keras_conversor/keras_conversor.pyhttps://github.com/ebmm01/tensorflowjs/blob/master/keras_conversor/keras_conversor.py). Vale salientar que é recomendado o uso do MobileNet, visto que ele já é adpatado para uso mobile (o que pode ser visto pelo seu próprio tamanho, 16mb vs 500mb do VGG16).

### Breve explicação sobre os modelos utilizados

#### VGG16

VGG16 é um rede neural convolucional para reconhecimento de objetos desenvolvido e treinando pelo grupo de Oxford, _Visual Geometry Group_ (VGG). Ele venceu a competição [ILSVR (Imagenet)](http://www.image-net.org/challenges/LSVRC/) em 2014, e é considerada uma das excelentes arquiteturas de modelos de visão até hoje.

#### MobileNet

As MobileNets são modelos pequenos, de baixa latência e baixa potência, parametrizados para atender às restrições de recursos de vários casos de uso. Eles podem ser construídos para classificação, detecção, incorporação e segmentação semelhantes à forma como outros modelos populares de larga escala, como o Inception, são usados.

As MobileNets trocam entre latência, tamanho e precisão, comparando favoravelmente com modelos populares da literatura.

### Algumas funções utilizadas

__fromPixels__ => Cria um tensor a partir de uma imagem.

__resizeNearestNeighbor__ => Redimensiona um lote de imagens 3D para uma nova forma (224x224).

__loadLayersModel__ => Carregar um modelo composto por Layers, incluindo sua topologia e pesos opcionais.

__toFloat__ => Converte o tipo para float32.

__expandDims__ => Expande a dimensão do tensor.

__reverse__ => Inverte um tensor ao longo de um eixo especificado.

__tensor1d__ => Cria um tensor unidimensional (Rank-1) com os valores, tamanho e dtype fornecidos.

__scalar__ => Cria Tensor rank-0 (escalar)

__sub__ => Subtrai dois Tensores elemento a elemento, A - B.

__div__ => Divide dois Tensores elemento a elemento, A/B.


## Referências

[TensorFlowJS](https://www.tensorflow.org/js)

[Step by step VGG16 implementation in Keras for beginners](https://towardsdatascience.com/step-by-step-vgg16-implementation-in-keras-for-beginners-a833c686ae6c)

[What is the VGG neural network?](https://www.quora.com/What-is-the-VGG-neural-network)

[MobileNet Github](https://github.com/tensorflow/tfjs-models/tree/master/mobilenet)

Olga Russakovsky*, Jia Deng*, Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma, Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein, Alexander C. Berg and Li Fei-Fei. __[ImageNet Large Scale Visual Recognition Challenge](http://www.image-net.org/challenges/LSVRC/)__. IJCV, 2015