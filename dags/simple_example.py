import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator
from utils.tasks import transformar_colunas

load_dotenv()

BUCKET_GCS = os.getenv("BUCKET_GCS")
CAMINHO_FILE = os.getenv("CAMINHO_FILE")

default_args = {
    'description': 'Uma dag exemplo para orquestrar os dados',
    'start_date': datetime(2026, 2, 27),
    'catchup': False
}

dag = DAG(
    dag_id ='dag_example',
    default_args = default_args,
#    schedule = timedelta(minutes= 5) Intervalo de execução do dag. Neste caso, a pipeline é acionado de 5 em 5 minutos.
)



# Uma dag de exemplo que extrai dados do google cloud storage.
with dag:
    task1 = GCSToLocalFilesystemOperator(
        task_id="ingerir_dados_cloud_storage",
        bucket='pipeline-airflow-docker-example',
        object_name='raw/raw_exemplo_pipeline_airflow_docker.xltx',
        filename="/opt/airflow/file.xltx",
        gcp_conn_id="victor_conexao"
    )

    task2 = PythonOperator(
        task_id="transformar_dados",
        python_callable=transformar_colunas
    )

    task1 >> task2



