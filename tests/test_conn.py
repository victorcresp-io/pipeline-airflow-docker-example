"""import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
"""
import os
import time

import psycopg2
from dotenv import load_dotenv
from tasks import connect_to_db


load_dotenv()


PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB   = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")

def test_init_sql():

    with psycopg2.connect(host=PG_HOST, port=PG_PORT, dbname="postgres",
                         user=PG_USER, password=PG_PASS) as conn:
        with conn.cursor() as cur:
            cur.execute("""
                select
                 datname 
                from pg_database
                where datname in ('database', 'airflow_db');
            """)
            rows = cur.fetchall()
            dbs = {row[0] for row in rows}

            assert "database" in dbs
            assert "airflow_db" in dbs

def test_create_table_and_schema():
    conn = connect_to_db()
    cursor = conn.cursor()

    cursor.execute("SELECT 1")

    result = cursor.fetchone()
    assert result[0] == 1