"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn_params = {
    "host": "localhost",
    "database": "north",
    "user": "postgres",
    "password": "89054313192"
}

with open("north_data/customers_data.csv", newline='', encoding='UTF-8') as csv_f:
    dict_data = csv.reader(csv_f)
    customers_data = [row for row in dict_data]
    customers_data.pop(0)
with open("north_data/employees_data.csv", newline='', encoding='UTF-8') as csv_f:
    dict_data = csv.reader(csv_f)
    employees_data = [row for row in dict_data]
    employees_data.pop(0)
with open("north_data/orders_data.csv", newline='', encoding='UTF-8') as csv_f:
    dict_data = csv.reader(csv_f)
    orders_data = [row for row in dict_data]
    orders_data.pop(0)
with psycopg2.connect(**conn_params) as conn:
    with conn.cursor() as cur:
        insert = "INSERT INTO customers VALUES (%s, %s, %s);"
        [cur.execute(insert, (customer[0], customer[1], customer[2])) for customer in customers_data]
        insert = "INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s);"
        [cur.execute(insert, (empl[0], empl[1], empl[2], empl[3], empl[4], empl[5])) for empl in employees_data]
        insert = "INSERT INTO orders VALUES (%s, %s, %s, %s, %s);"
        [cur.execute(insert, (order[0], order[1], order[2], order[3], order[4])) for order in orders_data]
