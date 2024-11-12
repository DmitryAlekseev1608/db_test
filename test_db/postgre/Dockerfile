FROM bitnami/spark:latest
USER root

RUN apt-get update
RUN apt-get install -y \
        default-jdk -y

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /opt/bitnami/spark/app/
CMD ["./bin/spark-shell", "--master", "spark://spark-master:7077", "/opt/bitnami/spark/app/src/get_data.py"]
