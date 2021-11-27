# DSP

## история

* распознование - сейчас уже решенная задача
* генерация - уже почти

## про обработку

* A/D conversion

  * quantize
  * descretizaiton
  * compression

Характерисктики

* sample rate
  * 8 kHz и выше, 22.5 или 44.1 базовый
  * sample size - квантизация - 16 bit/sample чаще всего

* number of channels - 1, 2, more

## characteristics

* SNR
* energy in decibel

## предобработка

* Mel Scale - у человека меньеш разрешение по звуку на высоких частотах

* cepstrum
  * Discrete cosine transformation
  * удобно искать пик сепструма - оно полезно для поиска главной частоты речи
  * не стабильно относительно


## griffin lim

теряется много информации о голосе