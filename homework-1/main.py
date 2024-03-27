"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2

ROOT_DIR = os.path.dirname(__file__)
DATA_PATH = os.path.join(ROOT_DIR, 'north_data')
EMPLOYEES_DATA_PATH = os.path.join(ROOT_DIR, 'north_data', 'employees_data.csv')
CUSTOMERS_DATA_PATH = os.path.join(ROOT_DIR, 'north_data', 'customers_data.csv')
ORDERS_DATA_PATH = os.path.join(ROOT_DIR, 'north_data', 'orders_data.csv')


def func_fill(cur, file, table, value):
    with open(file, 'r', encoding='UTF-8') as f:
        data = csv.DictReader(f)
        for row in data:
            cur.execute(
                f'INSERT INTO {table} VALUES({value})',
                (list(row.values()))
            )


def fill_tables():
    # connect to db
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password=os.environ["220913"]

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