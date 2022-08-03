"""Avaliable operations:
connection, insertion, retrieving.
"""

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def execute_connection():
    conn = psycopg.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DATABASE"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASS"),
    )
    return conn


def execute_query(SQL):
    conn = execute_connection()
    with conn.cursor() as cur:
        cur.execute(SQL)
        response = cur.fetchall()
    return response

