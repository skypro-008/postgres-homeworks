"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2
from config import EMPLOYEES_DATA_PATH, CUSTOMERS_DATA_PATH, ORDERS_DATA_PATH


def func_fill(cur, file, table, values):
    with open(file, 'r', encoding='UTF-8') as f:
        data = csv.DictReader(f)
        for row in data:
            cur.execute(
                f'INSERT INTO {table} VALUES({values})',
                (row.values())
            )


def fill_tables():
    # connect to db
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password=os.environ['POSTGRESKEY']

    )
    try:
        with conn:
            with conn.cursor() as cur:
                func_fill(cur, 'north_data/customers_data.csv', 'customers', '%s, %s, %s')
                func_fill(cur, 'north_data/employees_data.csv', 'employees', '%s, %s, %s, %s, %s, %s')
                func_fill(cur, 'north_data/orders_data.csv', 'orders', '%s, %s, %s, %s, %s')

    finally:
        conn.close()


if __name__ == '__main__':
    fill_tables()
