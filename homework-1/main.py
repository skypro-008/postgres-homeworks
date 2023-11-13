"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

if __name__ == '__main__':

    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="55555"
    )

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute()

    finally:
        conn.close()



