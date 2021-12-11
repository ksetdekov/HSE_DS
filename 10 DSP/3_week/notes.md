# распознование речи

## первым делом метрики

* WER - word error rate - количество неправильных слов - чаще будет неправильное
* CER - character error rate - он будет лучше, его проще использовать

## Listen attand and spell

послушай - примени внимание и слова

* listener - encode
  * biLstm model
* speller - decoder
  * начиная с начала - предсказываем последовательности токена из характеристического распредления по нашему словарю, какой токен должен стоять
  * специально регуляризации нет по времени аттеншн
  * attention speller выучиваем

мы учим эту модель с помощью Teacher forcing

### алгоритм Beam-searching

* интересно, применяют ли такое для

что это - для простоты зафиксируем длину словаря длины

## Languge model fusing

* к ASR model

использовать легкие языковые модели стоит

## conccecitonst tepmporal calssification

монотонный поиск alignmenta, на каждом

## jasper model

* 2018 год - CTC loss, быстрый инференс

* 2 свертки - в 4 раза меньше
* residual connections
* dillation используется - stride
* <https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#jasper>

## quarzNet

* то же самое, но есть отдельно свертки, которые смотрят на каналы (depth-wize), отдельно смотрят на на свременную сверку = они в сумме time-channel separable conv
* <https://docs.nvidia.com/deeplearning/nemo/user-guide/docs/en/main/asr/models.html#quartznet>
* GPU можно давать в эти модели

## augmentation

дешевый способ размножить датасет

* можно зашумлять разными способами
* применять к сигналу или мелСпектрограммам
* добавляем шум, меняем громкость, скорость, частоту, акустику

* маскируем частоты или время в мелСпектрограммам

## размечалка данных

* labelstudio можно использовать

## Listen attention spell - уже лучше чем человек 4 года назад

* яндекс спич кит - яндексовый уже работает хорошо
* предобученные модели для русского языка

* можно пробовать эти модели
