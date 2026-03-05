# ETL Project – Airflow + PostgreSQL (Docker Compose)

Este é um projeto de **ETL para Engenharia de Dados** que está em desenvolvimento. Na ETL de exemplo, os dados brutos são extraídos do Google Cloud Storage, transformados com pandas e carregados para a Google Cloud Storage na camada Raw.

A ideia é disponibilizar um ambiente já configurado com Airflow, Docker e PostgreSQL, facilitando a criação e execução de pipelines de dados.

Atualmente o projeto contém:

- Configuração do Apache Airflow
- Configuração do PostgreSQL
- Orquestração com Docker Compose
- Pipeline de CI configurado com verificações:
  - Se o banco de dados do Airflow foi criado
  - Se o banco de dados destinado à ingestão de dados foi criado
- Dag Airflow com uma ETL de exemplo.

---

## Requisitos

- Python 3.13
- Docker
- Docker Compose

---

## Como executar o projeto

###  Criar ambiente virtual

No diretório raiz do projeto:

```bash
python -m venv terminalvirtual
```

###  Ativar ambiente virtual

```bash
source terminalvirtual/bin/activate
```

###  Executar containers

```bash
docker compose build
```

```bash
docker compose up
```