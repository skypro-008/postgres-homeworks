import csv
import pathlib

import psycopg2

way_customers = pathlib.Path(__file__).parent.joinpath(
    'homework-1').joinpath('north_data').joinpath('customers_data.csv')

way_employees = pathlib.Path(__file__).parent.joinpath(
    'homework-1').joinpath('north_data').joinpath('employees_data.csv')

way_orders = pathlib.Path(__file__).parent.joinpath(
    'homework-1').joinpath('north_data').joinpath('orders_data.csv')


def write_in_customer(conn):
    with open(way_customers, 'r', encoding='utf8') as file:
        result = csv.reader(file)
        next(result)

    for row in result:
        with conn:
            with conn.cursor() as cur:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', row)


def write_in_employees(conn):
    with open(way_employees, 'r', encoding='utf8') as file:
        result = csv.reader(file)
        next(result)

        for row in result:
            with conn:
                with conn.cursor() as cur:
                    cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', row)


def write_in_orders(conn):
    with open(way_orders, 'r', encoding='utf8') as file:
        result = csv.reader(file)
        next(result)

        for row in result:
            with conn:
                with conn.cursor() as cur:
                    cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', row)


def read_psql(conn, table):

    with conn:
        with conn.cursor() as cur:
            cur.execute(f'SELECT * FROM {table}')
            row = cur.fetchall()

            for i in row:
                print(i)
