точка в кипас

vm for big data ds hse


порядок действий

```bash
sudo apt update
sudo apt apgrade
```

```bash
sudo apt install
sudo install virtualenv
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
```
pip install notebook
jupyter notebook --no-browser --ip=0.0.0.0 --port=809
```