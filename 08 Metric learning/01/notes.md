# face classification + metric learning

## face classification

определить person_id для базы людей

## face verification

* используя transfer learning
* facaial features - которые хорошо отличают людей.

верхнеуровнево - картинка $\rightarrow$ cnn $\rightarrow$ feature extractor $\rightarrow$ distance metric calculation:

* евклидово
* манхеттонское
* косинусное

## close vs open set

* могут ли новые люди появлятья?

  * face classification - closed set task
  тут мы учим separable features
  * face verification - open set task - тут мы учим large-margin features

## face classification idea

выход предследнего слоя - линейное, использовать как feature embedding.

как image retrieval - cnn-> embedding -> classification -> softmax -> probas.

## ROC AUC metric

EER - line - false positive = 1-True positive ratio

## discrimitative features?

* при классификации - хотим просто чтобы признаки делили нас на классы.
* в идеале мы хотим discriminative features
  * максимально различное между классами (max inter class distance)
  * minimum intra calss distance

для начала - нужно определеить расстояние. Часто подойдет евклидово.

## center loss

определить критерий, который минимизирует intra-class distance.

как l2 регуляризация только не на веса, а на расстояния до центров классов.

## contrastive loss

для каждой пары объектов из train - пытаемся уменьшить intra-class distance, сохраняя определеннй m margin между объектами разных классов.

когда дистанцим меньше margin - максимизируем эту дистанцию.

contrastive loss - не постоянно исползуют.

## triplet loss

мотивация kNN алгоритм для классификации

корошие результаты, когда берем умно триплеты - sample mining

имея лицо i + j, стараемся сделать эмбеддинг лица i ближе к эмбеддингу человека i чем к эмбеддингу другого j!=i

hard negative mining можно использовать подход.

## softmax - как обычно

## angular softmax loss

вспомнил бинарную классификацию с softmax. Если нормировать веса до 1, то получится. Когда веса нормализованы и bias=0, то получается что можно легко представить angular softmax loss.

### arcface

это реализация функции ошибки

можно смотерть разные подходы тут
<https://github.com/KevinMusgrave/pytorch-metric-learning>
