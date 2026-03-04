FROM apache/airflow:slim-3.1.7-python3.13

USER root
# deps comuns pra build de wheels (evita falhas em imagem slim)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential gcc \
 && apt-get clean && rm -rf /var/lib/apt/lists/*

USER airflow

COPY requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt