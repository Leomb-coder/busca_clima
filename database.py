import os
import psycopg2
from urllib.parse import urlparse

url = urlparse(os.getenv("DATABASE_URL"))

DB_CONFIG = {
    "host":     url.hostname,
    "port":     url.port,
    "dbname":   url.path[1:],
    "user":     url.username,
    "password": url.password,
    "sslmode":  "require"
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)

def insert_clima(cidade, data, umidade, vento, precipitacao, temp_min, temp_max):
    sql = """
        INSERT INTO clima (cidade, data, umidade, vento, precipitacao, temp_min, temp_max)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    with get_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(sql, (cidade, data, umidade, vento, precipitacao, temp_min, temp_max))
        conn.commit()