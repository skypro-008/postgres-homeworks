import psycopg2
import csv
import os

user = os.environ.get('USER')
password = os.environ.get('PASSWORD')

with psycopg2.connect(host='localhost', database='north', user=user, password=password) as conn:

    with conn.cursor() as cur:

        with open(os.path.join('..', 'homework-1', 'north_data', 'customers_data.csv'), 'r', encoding='utf-8')\
                as file_customers:
            # запись данных в переменную
            csv_text = csv.reader(file_customers)
            # пропуск первой строчки
            next(csv_text)
            # запись данных в таблицу
            for i in csv_text:
                cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', tuple(i))

        with open(os.path.join('..', 'homework-1', 'north_data', 'employees_data.csv'), 'r', encoding='utf-8')\
                as file_employees:
            # запись данных в переменную
            csv_text = csv.reader(file_employees)
            # пропуск первой строчки
            next(csv_text)
            # запись данных в таблицу
            for i in csv_text:
                cur.execute('INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)', tuple(i))

        with open(os.path.join('..', 'homework-1', 'north_data', 'orders_data.csv'), 'r', encoding='utf-8')\
                as file_order:
            # запись данных в переменную
            csv_text = csv.reader(file_order)
            # пропуск первой строчки
            next(csv_text)
            # запись данных в таблицу
            for i in csv_text:
                cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', tuple(i))

conn.close()
