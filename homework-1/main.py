"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qwerty')

try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/customers_data.csv', 'r') as f:
                csv_reader = csv.reader(f)
                next(csv_reader)
                for row in csv_reader:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", row)
                    conn.commit()
finally:
    conn.close()

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qwerty')

try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/employees_data.csv', 'r') as f:
                csv_reader = csv.reader(f)
                next(csv_reader)
                for row in csv_reader:
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", row)
                    conn.commit()
finally:
    conn.close()

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='qwerty')


try:
    with conn:
        with conn.cursor() as cursor:
            with open('north_data/orders_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute(
                        "INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                        row
                    )
                    conn.commit()
finally:
    conn.close()
