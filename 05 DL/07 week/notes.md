# transfer learnign notes

## todo

как-то разобраться с reshape?

x = x.reshape(x.size(0), -1)

## если нужно 1 раз сеть обучить

мы повышаем learning rate для слоя нового и ниже для остаточных слоев

это хорошая штука для прогресс баров

```python
from tqdm.auto import tqdm
```
