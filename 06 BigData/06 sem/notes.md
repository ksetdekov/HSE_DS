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