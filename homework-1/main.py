"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os

password = os.getenv('PSQLpass')
customers = []
employees = []
orders = []

with open('north_data\customers_data.csv', 'r') as file:
    for row in file:
        rows = row.split(',')
        read_rows = []
        for item in rows:
            item = item.replace('"', '')
            item = item.replace('\n', '')
            item = item.replace("'", '')
            read_rows.append(item)
        customers.append(read_rows)
    customers = customers[1:len(customers)]

with open('north_data\employees_data.csv', 'r') as file:
    for row in file:
        rows = row.split('",')
        read_rows = []
        for item in rows:
            item = item.replace('"', '')
            item = item.replace('\n', '')
            item = item.replace("'", '')
            read_rows.append(item)
        employees.append(read_rows)
    employees = employees[1:len(employees)]

with open('north_data\orders_data.csv', 'r') as file:
    for row in file:
        rows = row.split(',')
        read_rows = []
        for item in rows:
            item = item.replace('"', '')
            item = item.replace('\n', '')
            item = item.replace("'", '')
            read_rows.append(item)
        orders.append(read_rows)
    orders = orders[1:len(orders)]

with psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password=password
) as conn:
    with conn.cursor() as cur:
        for item in customers:
            cur.execute(f"INSERT INTO customers values ('{item[0]}', '{item[1]}', '{item[2]}')")
        id = 1
        for item in employees:
            cur.execute(
                f"INSERT INTO employees values ({id}, '{item[0]}', '{item[1]}', '{item[2]}', '{item[3]}', '{item[4]}')")
            id += 1
        for item in orders:
            cur.execute(f"INSERT INTO orders values ('{item[0]}', '{item[1]}', '{item[2]}', '{item[3]}', '{item[4]}')")
