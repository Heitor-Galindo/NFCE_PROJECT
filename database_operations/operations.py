"""Database operations:
fetchall, executemany
"""

import os
import psycopg
from dotenv import load_dotenv

load_dotenv()


def execute_connection():
    """Connect to database"""
    conn = psycopg.connect(
        host=os.getenv("POSTGRES_HOST"),
        port=os.getenv("POSTGRES_PORT"),
        dbname=os.getenv("POSTGRES_DATABASE"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASS"),
    )
    return conn


def execute_query(sql):
    """Execute a query without params and return all results as a list"""
    conn = execute_connection()
    with conn.cursor() as cur:
        cur.execute(sql)
        response = cur.fetchall()
    return response


def execute_insert(sql, data):
    """Insert data into database"""
    conn = execute_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(sql, data)
    except Exception as error:
        print(f"ERROR: {error}")
    else:
        print("done!")
    finally:
        conn.commit()
