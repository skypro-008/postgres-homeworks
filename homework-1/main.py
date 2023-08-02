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

with open('north_data/employees_data.csv', 'r', encoding="utf-8") as f:
    next(f)
    cursor.copy_from(f, 'employees', sep=',')

with open('north_data/employees_data.csv', mode='r') as f:
    count = 0
    csvFile = csv.reader(f)
    for row in csvFile:
        cursor.execute("INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)", (row[0], row[1], row[2], row[3], row[4], row[5]))

with open('north_data/orders_data.csv', 'r', encoding="utf-8") as f:
    next(f)
    cursor.copy_from(f, 'orders_data', sep=',')

conn.commit()