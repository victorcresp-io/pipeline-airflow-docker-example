import os
from datetime import datetime

from airflow import DAG
from airflow.providers.google.cloud.operators.bigquery import BigQueryInsertJobOperator

PROJECT_ID = os.environ["GCP_PROJECT_ID"]
DATASET = os.environ["BQ_DATASET"]

with DAG(
    dag_id="bq_example_simple",
    start_date=datetime(2024, 1, 1),
    schedule=None,
    catchup=False,
) as dag:

    create_table = BigQueryInsertJobOperator(
        task_id="create_table",
        configuration={
            "query": {
                "query": f"""
                CREATE TABLE IF NOT EXISTS `{PROJECT_ID}.{DATASET}.demo_table` (
                  id INT64,
                  name STRING,
                  created_at TIMESTAMP
                )
                """,
                "useLegacySql": False,
            }
        },
        location="US",
    )

    insert_rows = BigQueryInsertJobOperator(
        task_id="insert_rows",
        configuration={
            "query": {
                "query": f"""
                INSERT INTO `{PROJECT_ID}.{DATASET}.demo_table` (id, name, created_at)
                VALUES (1, 'victor', CURRENT_TIMESTAMP()),
                       (2, 'airflow', CURRENT_TIMESTAMP())
                """,
                "useLegacySql": False,
            }
        },
        location="US",
    )

    create_table >> insert_rows