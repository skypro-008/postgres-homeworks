"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from parsing_csv_files import ParsingCSVFiles
data = ParsingCSVFiles()
customers_data = data.parsing_customers_file()
employees_data = data.parsing_employees_file()
orders_data = data.parsing_orders_file()
# connect to database
# conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
def add_customers_data():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
    try:
        with conn:
            # create cursor
            with conn.cursor() as cur:

                # execute query
                cur.executemany('INSERT INTO customers_data VALUES (%s, %s, %s)', customers_data[1:])
                cur.execute('SELECT * FROM customers_data')

                rows = cur.fetchall()
                for row in rows:
                    print(row)
    finally:
        # close connection
        conn.close()


def add_employees_data():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
    try:
        with conn:
            # create cursor
            with conn.cursor() as cur:
                # execute query
                cur.executemany('INSERT INTO employees_data VALUES (%s, %s, %s, %s, %s, %s)', employees_data[1:])
                cur.execute('SELECT * FROM employees_data')

                rows = cur.fetchall()
                for row in rows:
                    print(row)
    finally:
        # close connection
        conn.close()

def add_orders_data():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='12345')
    try:
        with conn:
            # create cursor
            with conn.cursor() as cur:
                # execute query
                cur.executemany('INSERT INTO orders_data VALUES (%s, %s, %s, %s, %s)', orders_data[1:])
                cur.execute('SELECT * FROM orders_data')

                rows = cur.fetchall()
                for row in rows:
                    print(row)
    finally:
        # close connection
        conn.close()

add_customers_data()
add_employees_data()
add_orders_data()