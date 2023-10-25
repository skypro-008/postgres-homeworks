import psycopg2
import csv


def open_csv_file(file):
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        return csv_reader


employees = open_csv_file('north_data/employees_data.csv')
customers = open_csv_file('north_data/customers_data.csv')
orders = open_csv_file('north_data/orders_data.csv')

"""Скрипт для заполнения данными таблиц в БД Postgres."""

db_config = {
    'dbname': 'north',
    'user': 'postgres',
    'password': '1975',
    'host': 'localhost'
}

with psycopg2.connect(**db_config) as conn:
    with conn.cursor() as cur:
        cur.executemany("INSERT INTRO employees VALUES(%S, %S, %S, %S, %S, %S)", [i for i in employees])
        cur.executemany("INSERT INTRO customers VALUES(%S, %S, %S)", [i for i in customers])
        cur.executemany("INSERT INTRO orders VALUES(%S, %S, %S, %S, %S)", [i for i in orders])
conn.close()
