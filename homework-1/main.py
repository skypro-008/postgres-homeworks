"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='1'
)
try:
    with conn.cursor() as curs:
        with open('north_data\\employees_data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # print(row)
                curs.execute(
                    'INSERT INTO employees(employee_id, first_name, last_name, title, birth_date, notes) VALUES(%s, %s, %s, %s, %s, %s)',
                    (row['employee_id'], row['first_name'], row['last_name'], row['title'], row['birth_date'], row['notes']))
            conn.commit()

        with open('north_data\\customers_data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # print(row)
                curs.execute(
                    'INSERT INTO customers_data(customer_id, company_name, contact_name) VALUES(%s, %s, %s)',
                    (row['customer_id'], row['company_name'], row['contact_name']))
            conn.commit()

        with open('north_data\\orders_data.csv') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # print(row)
                curs.execute(
                    'INSERT INTO orders_data(order_id, customer_id, employee_id, order_date, ship_city) VALUES(%s, %s, %s, %s, %s)',
                    (row['order_id'], row['customer_id'], row['employee_id'], row['order_date'], row['ship_city']))
            conn.commit()

finally:
    conn.close()

