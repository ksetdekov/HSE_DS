# Синтез речи

## dilated convolution

* это на чем работает TCN
* convolution, который все дальше назад смотрит

## causal convlution

* чтобы на будущее на смотрели

## gated mechanism - gated attention

## WaveNet

* работает хорошо, но большой минус - синтез очень долго будет идти - он по одному сэмплу генерирует

## Есть решения

* GAN - учится отличать людей от синтезированной речи
  * MelGAN
  * Parallel WaveGAN

* Flow-based models
  * Autoregressive normalizing flows (inverse autoregressive flow)
  * 
