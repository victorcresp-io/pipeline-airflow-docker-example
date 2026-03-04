import os
from datetime import datetime, timedelta

from dotenv import load_dotenv
from airflow import DAG
from airflow.providers.google.cloud.transfers.gcs_to_local import GCSToLocalFilesystemOperator

load_dotenv()

BUCKET_GCS = os.getenv("BUCKET_GCS")
CAMINHO_FILE = os.getenv("CAMINHO_FILE")

default_args = {
    'description': 'Uma dag exemplo para orquestrar os dados',
    'start_date': datetime(2026, 2, 27),
    'catchup': False
}

dag = DAG(
    dag_id ='teste-victor',
    default_args = default_args,
    schedule = timedelta(minutes= 5)
)




with dag:
    task1 = GCSToLocalFilesystemOperator(
        task_id="ingerir_dados_cloud_storage",
        bucket='pipeline-airflow-docker-example',
        object_name='raw/raw_exemplo_pipeline_airflow_docker.xltx',
        filename="/opt/airflow/file.csv",
        gcp_conn_id="victor_conexao"
    )
