import pandas as pd
import os

def transformar_colunas():
    os.makedirs("/opt/airflow/tmp", exist_ok=True)
    # ler arquivo
    df = pd.read_excel("/opt/airflow/file.xltx")


    # renomear colunas
    df = df.rename(columns={
        "Nome": "name",
        "Idade": "age"
    })
    # salvar resultado
    df.to_csv("/opt/airflow/tmp/df_example.csv", index=False)
    return df