import psycopg2
from psycopg2.extras import RealDictCursor

# Connection config
DB_CONFIG = {
    "host":     "localhost",
    "port":     5432,
    "dbname":   "historico_clima",
    "user":     "postgres",
    "password": 1234
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