"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

"""Коннект к постгрес"""
connect = psycopg2.connect(
    host='localhost',
    database='north',
    user='eugene',
    password='postgres'
)

"""Заполнение таблицы customers"""
try:
    with connect:
        with connect.cursor() as cursor:
            with open('north_data/customers_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute("INSERT INTO customers (customer_id, company_name, contact_name) "
                                   "VALUES (%s, %s, %s)", row)
finally:
    connect.close()


connect = psycopg2.connect(
    host='localhost',
    database='north',
    user='eugene',
    password='postgres'
)

"""Заполнение таблицы employees"""
try:
    with connect:
        with connect.cursor() as cursor:
            with open('north_data/employees_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute("INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) "
                                   "VALUES (%s, %s, %s, %s, %s, %s)", row)
finally:
    connect.close()


connect = psycopg2.connect(
    host='localhost',
    database='north',
    user='eugene',
    password='postgres'
)

"""Заполнение таблицы orders"""
try:
    with connect:
        with connect.cursor() as cursor:
            with open('north_data/orders_data.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    cursor.execute("INSERT INTO orders (order_id, customer_id, employee_id, order_data, ship_city) "
                                   "VALUES (%s, %s, %s, %s, %s)", row)
finally:
    connect.close()