# обучение с подкреплением

## RL

есть:

* environment (states $S_t$)
* agent does actions $a_t$
* environment sends reward $r_{t+1}$ and next state $S_{t+1}$

## подбора параметров

hyper tune, optuna - схожая идея. Сначал исследует, потом оптимизирует.

## идея

мы пытаемся выразить дествия агента с помощью функций, для каждой пусть будет нейросеть и это будет задача deep reinforcement learning. в зависимости от функции, получим разные алгоритмы.

## MDP формализм

* не важно как пришли в состоянии оказались - действия будут зависеть от того где мы находимся

## Глобавльная задача - максимизировать суммарный выигрыш

$$R = \sum_t{r_t}$$

Политика агента  $\pi(a|s) = P(\text{take action } a|\text{in state } s)$

Нужно найти политику с максимомум выигрыша

$$\pi(a|s) : E_{\pi} [R] \rightarrow \max$$

## cross entropy methond

1. initialize policy
2. repeat

    1. sapmple $n$ sesions
    2. pick $n/4$ best (elite)
    3. change policy so that it prioritize actions from them

## tabular crossentropy method

* elite - M
* all - N games

Политика = матрица S состояний по строкам и A  действий возможных
в элитных у нас K/N = p(a|s) для элитных

обновим это повторение - ad nauseam

$$\pi(a|s) = \frac{\text{took a at s}}{\text{was at s}}$$

## перейдем к приближенному crossentropy
