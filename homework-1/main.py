"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='qm4p00ed'
)
cursor = conn.cursor()

with open('north_data/customers_data.csv', mode='r') as f:
    csvFile = csv.reader(f)
    for row in csvFile:
        cursor.execute("INSERT INTO customers_data VALUES(%s, %s, %s)", (row[0], row[1], row[2]))


with open('north_data/employees_data.csv', mode='r') as f:
    csvFile = csv.reader(f)
    for row in csvFile:
        cursor.execute("INSERT INTO employees_data VALUES(%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))


with open('north_data/orders_data.csv', mode='r') as f:
    csvFile = csv.reader(f)
    for row in csvFile:
        print(type(row[0]))
        cursor.execute("INSERT INTO orders_data VALUES(%s, %s, %s, %s, %s)", (int(row[0]), row[1], row[2], row[3], row[4]))

conn.commit()