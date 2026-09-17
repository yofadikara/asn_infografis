import psycopg2
from dotenv import load_dotenv
import os
from pathlib import Path
from dataconfig.mapping import logger


#Load ENV
def load_env():
    env_path = Path(__file__).resolve().parents[1] / '.env'  # naik 1 level
    load_dotenv()
    return {
        "host": os.getenv("DB_HOST"),
        "port": os.getenv("DB_PORT"),
        "dbname": os.getenv("DB_NAME"),
        "user": os.getenv("DB_USER"),
        "password": os.getenv("DB_PASS")
    }

#Connect DB
def connect_db(params):
    try:
        conn = psycopg2.connect(**params)
        logger.info("Koneksi ke database berhasil.")
        return conn
    except Exception as e:
        logger.warning("Koneksi ke database gagal:", e)
        return None