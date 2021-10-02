точка в кипас

vm for big data ds hse


порядок действий

```bash
sudo apt update
sudo apt apgrade
```

```bash
sudo apt install virtualenv
```

```
virtualenv venv --python=python3.6
source venv/bin/activate
```

зачем нужны окружения - нужно чтобы пакеты не конфликтовали
прописываем переменные окружения

```bash
nano spark_environ.sh
```

```
sudo apt install default-jdk scala git -y && \
wget https://downloads.apache.org/spark/spark-3.1.2/spark-3.1.2-bin-hadoop2.7.tgz &&\
tar xvf spark-* && \
sudo mv spark-3.1.2-bin-hadoop2.7 /opt/spark && \
export SPARK_HOME=/opt/spark && \
export PATH=$PATH:$SPARK_HOME/bin:$SPARK_HOME/sbin && \
export PYSPARK_PYTHON=/usr/bin/python3 && \
start-all.sh
```

```bash
chmod +x ./spark_environ.sh && ./spark_environ.sh
```

добавить файлы, который мы сгенерировал в авторизированные ключи
```
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keyz
```

```
pip install notebook

jupyter notebook --no-browser --ip=0.0.0.0 --port=8098
python -m ipykernel install --user --name=venv
jupyter kernelspec list
```

последняя команда - показывает, какие есть кернелы

брать ноутбука ссылку и заменить имя на IP4 адрес, который 


```python
import findspark
findspark.init()

import pyspark

spark = pyspark.sql.SparkSession.builder.getOrCreate()
```

спарк сессия определяется Спарк Контекстом.
Есть сессия и она или создается заново изи подключается.

попробуем запустить на нашем спарке 3 ноутбук
можно через winscp подключатьс0



# настроить tmux
```bash
sudo apt install tmux
python -m ipykernel install --user --name=venv
tmux
source venv/bin/activate
jupyter notebook --no-browser --ip=0.0.0.0 --port=8098
```

# Партиционирование

```python
df.write.parquet('./test_df.parquet')
```

```bash
!du -h -d 2 ./test_df.parquet/*
```

## как работает?
* как групбай
* каждое значение - отдельный файл

хорошая идея по уникальным датам это разбить.
+ ускоряет работу

Это про сохранение данных.

Еще есть вариант партиционирования на уровне задачи самой

Возможно помните мы когда говорили про "кирпичики" по которым по сути spark делит все наши данные
по сути по ним происходят вычисления 
Нарпимер - есть набор данных он разделяется на partitions 

Есть два разных вида partition - первый по которому спарк непосредственно делит, над которыми и производятся вычисления - все наши мап-редюсы выполняются именно над ними, то есть по сути спрак внутри себя разделят данные и соотвественно вычиления на группы или partitions

в зависимости от partitions  генерируется разное количество tasks


и второе понятие partiotions  - это именно физическая запись на жесткий диск
Если вы посмотрите внутрь какого-либо файла parquet, который вы сохраните с помощью spark_df.write().save()  - заметите внутри какое-то количество файлов, по сути коллекцию файлов, которая образует наш один большой файл


Можно принудительно менять количесвто partitions  при записи и при обработке
например командами coalesce()
или repartiion

df - абстракция над rdd

и партиция - которая делится на таски