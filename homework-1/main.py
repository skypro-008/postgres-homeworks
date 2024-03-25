"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2
from config import EMPLOYEES_DATA_PATH, CUSTOMERS_DATA_PATH, ORDERS_DATA_PATH


def fill_tables():
    # connect to db
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='Iwilldietomorrow92815'
    )
    try:
        with conn:
            with conn.cursor() as cur:
                with open('north_data/customers_data.csv', 'r', encoding='UTF-8') as f:
                    data = csv.DictReader(f)
                    for row in data:
                        cur.execute(
                            'INSERT INTO customers VALUES(%s, %s, %s)',
                            (row['customer_id'], row['company_name'], row['contact_name'])
                        )

                with open('north_data/employees_data.csv', 'r', encoding='UTF-8') as f:
                    data = csv.DictReader(f)
                    for row in data:
                        cur.execute(
                            'INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)',
                            (row['employee_id'], row['first_name'], row['last_name'],
                             row['title'], row['birth_date'], row['notes'])
                        )

                with open('north_data/orders_data.csv', 'r', encoding='UTF-8') as f:
                    data = csv.DictReader(f)
                    for row in data:
                        cur.execute(
                            'INSERT INTO orders VALUES(%s, %s, %s, %s, %s)',
                            (row['order_id'], row['customer_id'], row['employee_id'],
                             row['order_date'], row['ship_city'])
                        )

    finally:
        conn.close()


if __name__ == '__main__':
    fill_tables()
