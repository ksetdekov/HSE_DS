# Как ускорять нейронные сети

## хитрые подходы

* декомпозиция тензоров (PCA-like)
* **quantizations**
  * symmetric
  * assymetric
* pruning
* **distillationa**

## quantization in PyTorch

* динамическая квантизация
* статическая квантизация
* обучение с учетом квантизации
* pytorch quantization

## pruning

## distillation

берем мелкую сеть, похожую по топологии, но с меньшем размером каждого слоя. используем большую сеть как учителя для малого

Получаем loss между новой сетью и учителем и student loss - от истинного

## выбирать архитектуру получше

* NiN
* SqueezeNet
* MobileNet
* ShuffleNet
* EffiNet

## Советы

Профилировать модели, писать свои кернелы, првоерить ИО, кешировать ну устройстве, DALI (<https://github.com/NVIDIA/DALI>)

## iOS

* coreml
* PyTorch mobile

## Inference

* TensorRT
  * Mixed Precision inferenct
  * Layer fusion
  * Batching
  * optimization for specific hardware
* OpenVINO

* pytorch xla tpu <https://github.com/pytorch/xla>
