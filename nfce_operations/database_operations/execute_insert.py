"""Insert data into database"""

from psycopg import Error
from nfce_operations.database_operations.operations import execute_connection


def execute_insert(sql, data):
    """Insert data into database"""
    conn = execute_connection()
    try:
        with conn.cursor() as cur:
            cur.executemany(sql, data)
    except Error as error:
        print(f"ERROR: {error}")
    else:
        print("done!")
    finally:
        conn.commit()
