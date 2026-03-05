import pandas as pd


def transformar_colunas():
    # ler arquivo
    df = pd.read_excel("/opt/airflow/file.xltx")


    # renomear colunas
    df = df.rename(columns={
        "nome": "name",
        "idade": "age"
    })
    # salvar resultado
    return df