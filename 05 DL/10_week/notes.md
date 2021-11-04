# GAN

ганы и вариационные автоэкодеры

* nvlabs stylegan 3 <https://github.com/NVlabs/stylegan3>
* <https://thiscatdoesnotexist.com>

d dimensional noise vector $\rightarrow$  генератор $\rightarrow$ фейк изображения $\rightarrow$ в сеть дискриминатор + реальные изображения $\rightarrow$ предсказанные классы.

Важно, чтобы дискриминатор иногда ошибался - чтобы можно было учиться генератору.

<https://distill.pub/2016/deconv-checkerboard/>

## советы

1. нормализовать входы до -1 1 и добавлять на последний слой танг
2. семплировать из нормального распределения
3. использовать batchnorm - в обеих сетках
4. можно попробовать разные batchnorm для фейковых и реальных данных
5. полносвязные слои не очень хорошо, сверточные - хорошо

## сверточные ганы

1. они лучше
2. можно - учить по очереди генератор и дискриминатор учить

## condtitional gan

подавать на вход вектора классов на вход генераторов и дискриминатора

* для генератора - мы удлиняем вектор
* для дискриминатора - новые каналы кроме RGB - один нужный, заполненный 1 цами

## pixel to pixel GAN

разметка по пикселям - это mapilary  сегментация

<https://affinelayer.com/pixsrv/>

## variational autoencoders

<https://towardsdatascience.com/understanding-variational-autoencoders-vaes-f70510919f73>
