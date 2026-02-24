import os
import time
import psycopg


def test_init_sql_ran():

    with psycopg.connect(host=PG_HOST, port=PG_PORT, dbname="postgres",
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