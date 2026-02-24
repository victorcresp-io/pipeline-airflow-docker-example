# ETL Project – Airflow + PostgreSQL (Docker Compose)

Este é um projeto de **ETL para Engenharia de Dados** que está em desenvolvimento.

Atualmente o projeto contém:

- Configuração do Apache Airflow
- Configuração do PostgreSQL
- Orquestração com Docker Compose
- Pipeline de CI configurado com verificações:
  - Se o banco de dados do Airflow foi criado
  - Se o banco de dados destinado à ingestão de dados foi criado

O projeto ainda está em evolução.

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

###  Instalar as dependências

```bash
pip install -r requirements.txt
```

###  Executar containers

```bash
docker compose up
```