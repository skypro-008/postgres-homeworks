"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
import os

pw_db: str = os.getenv("PW_DB")

customers_path = 'north_data/customers_data.csv'
employees_path = 'north_data/employees_data.csv'
orders_path = 'north_data/orders_data.csv'

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password=pw_db)

try:
    with conn:
        with conn.cursor() as cur:
            with open(customers_path) as customers:
                customers_read = csv.DictReader(customers)
                for row in customers_read:
                    # execute querty
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                (row['customer_id'],
                                 row['company_name'],
                                 row['contact_name']
                                ))

            with open(employees_path) as employees:
                employees_read = csv.DictReader(employees)
                for row in employees_read:
                    # execute querty
                    cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                (row['employee_id'],
                                 row['first_name'],
                                 row['last_name'],
                                 row['title'],
                                 row['birth_date'],
                                 row['notes']
                                 ))

            with open(orders_path) as orders:
                orders_read = csv.DictReader(orders)
                for row in orders_read:
                    # execute querty
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                (row['order_id'],
                                 row['customer_id'],
                                 row['employee_id'],
                                 row['order_date'],
                                 row['ship_city']
                                ))

finally:
    conn.close()