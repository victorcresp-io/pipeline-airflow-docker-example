import os

import psycopg2
import requests
from dotenv import load_dotenv

load_dotenv()

PG_HOST = os.getenv("PG_HOST")
PG_PORT = os.getenv("PG_PORT")
PG_DB   = os.getenv("PG_DB")
PG_USER = os.getenv("PG_USER")
PG_PASS = os.getenv("PG_PASS")

api_url = "https://api.weatherstack.com/current?access_key=882ce2116a49dfa95b87cc876d840c8c&query=Brazil"

# Função para extração dos dados da API.
def fetch_data():
    print("Tentando conectar à API")
    try:
        response = requests.get(api_url)
        response.raise_for_status()

        print("Conexão com a api feita com sucesso!")
        return response.json()
    except requests.exceptions.RequestsException as e:
        print(f"Ocorreu um erro {e}")
        raise

# Função para simular os dados retornados na resposta da API.
def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'Brasilia, Brazil', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'Brasilia', 'country': 'Brazil', 'region': 'Distrito Federal', 'lat': '-15.783', 'lon': '-47.917', 'timezone_id': 'America/Sao_Paulo', 'localtime': '2026-02-25 05:37', 'localtime_epoch': 1771997820, 'utc_offset': '-3.0'}, 'current': {'observation_time': '08:37 AM', 'temperature': 20, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly cloudy'], 'astro': {'sunrise': '06:11 AM', 'sunset': '06:38 PM', 'moonrise': '01:52 PM', 'moonset': '12:07 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 55}, 'air_quality': {'co': '184.85', 'no2': '3.45', 'o3': '28', 'so2': '1.25', 'pm2_5': '2.95', 'pm10': '3.05', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 10, 'wind_degree': 301, 'wind_dir': 'WNW', 'pressure': 1014, 'precip': 0, 'humidity': 94, 'cloudcover': 75, 'feelslike': 20, 'uv_index': 0, 'visibility': 10, 'is_day': 'no'}}

#Função para conectar ao banco de dados que está sendo executado no container docker.
def connect_to_db():
    print("Conectando ao banco de dados PostgreSQL")
    try:
        conn = psycopg2.connect(
            host = PG_HOST,
            port = PG_PORT,
            dbname = PG_DB,
            user = PG_USER,
            password = PG_PASS
        )
        return conn
    except psycopg2.Error as e:
        print(f"A conexão com o banco de dados PostgreSQL falhou: {e}")
        raise

#Função responsável por criar a tabela e schema caso não existam.
def create_table(conn):
    print("Criando a tabela raw_clima")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE SCHEMA IF NOT EXISTS dev;
            CREATE TABLE IF NOT EXISTS dev.raw_clima(
                id SERIAL PRIMARY KEY,
                cidade TEXT,
                temperatura FLOAT,
                clima_descricao TEXT,
                vento_velocidade FLOAT,
                horario TIMESTAMP,
                insert_at TIMESTAMP DEFAULT NOW(),
                utc_diferenca TEXT
            )
        """)
        conn.commit()
        conn.close()
        print("Tabela criada com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro ao criar a tabela: {e}")
        raise

def insert_records(conn, data):
    try:
        weather = data['current']
        location = data['location']
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO dev.raw_clima(
                cidade,
                temperatura,
                clima_descricao,
                vento_velocidade,
                horario,
                insert_at,
                utc_diferenca
            ) VALUES (%s, %s, %s, %s, %s, NOW(), %s)
        """, (
            location['name'],
            weather['temperature'],
            weather['weather_descriptions'][0],
            weather['wind_speed'],
            location['localtime'],
            location['utc_offset']
        ))
        conn.commit()
        conn.close()
        print("Dados inseridos na tabela dev.raw_clima com sucesso!")
    except psycopg2.Error as e:
        print(f"Erro durante a inserção dos dados na tabela dev.raw_clima: {e}")
        raise

data = mock_fetch_data()
conn = connect_to_db()
insert_records(conn, data)