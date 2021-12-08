# attention + SOTA

## attention is all you need

2017 статья вышла

На ряде датасетов - показал себя хорошо (х4 по времени + лучше результаты)

### механизм внимание более навороченный

attention recap

### абстракции

* вектора эмбеддинга - понятно - это от слова X
* queries - мое текущее слово $W^Q$
* keys - слово с которым я себя сравниваю
* values -   $q_1 \cdot k_1 ...q_1 \cdot k_2...q_1 \cdot k_n = V$
* scores $\rightarrow$ devide by $\sqrt{dim(embedding)} = 8$
* softmax * value = sum

$$Z = softmax \left(\frac{Q\cdot K^T}{\sqrt{d_K}}\right)\cdot V$$
