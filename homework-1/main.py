"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import psycopg2.errors
from utils import get_data_from_csv


employees = get_data_from_csv('employees', 'north_data/employees_data.csv')
customers = get_data_from_csv('customers', 'north_data/customers_data.csv')
orders = get_data_from_csv('orders', 'north_data/orders_data.csv')


def main():
    conn = psycopg2.connect(host="localhost",
                            database="north",
                            user="postgres",
                            password="1379")
    try:
        with conn:
            with conn.cursor() as cur:

                cur.executemany('INSERT INTO employees VALUES(%s, %s, %s, %s)', employees)
                cur.executemany('INSERT INTO customers VALUES(%s, %s)', customers)
                cur.executemany('INSERT INTO orders VALUES(%s, %s, %s, %s, %s)', orders)

    except psycopg2.errors.UniqueViolation:
        print("Уже есть в таблице")

    finally:
        conn.close()


if __name__ == '__main__':
    main()
