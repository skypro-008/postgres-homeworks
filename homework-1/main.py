import psycopg2
import os
import csv

"""Скрипт для заполнения данными таблиц в БД Postgres."""
# connect to db

DB_PSW = os.getenv('DB_PSW')
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=DB_PSW
)
try:
    with conn:
        with conn.cursor() as cur:
            with open('north_data/customers_data.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader) # пропустить первую строку
                rows = [row for row in reader]
                cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", rows)
            with open('north_data/employees_data.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)
                rows = [row for row in reader]
                cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", rows)
            with open('north_data/orders_data.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                next(reader)
                rows = [row for row in reader]
                cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", rows)
finally:
    conn.close()
