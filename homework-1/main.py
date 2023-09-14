"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2



""" connect to db and open cursor """

conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='silence11')

# Создание курсора
cur = conn.cursor()

# Открытие файлов с данными

cur = conn.cursor()

with open('north_data/employees_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # пропуск хедера
    for row in reader:
        cur.execute(
            "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
            row
        )

with open('north_data/customers_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # пропуск хедера
    for row in reader:
        cur.execute(
            "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s)",
            row
        )

with open('north_data/orders_data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)  # пропуск хедера
    for row in reader:
        cur.execute(
            "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s)",
            row
        )

conn.commit()
cur.close()
conn.close()