"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import pandas as pd

def customers_d():
    """Функция открывает customers_data.csv и для записи данных в базу данных postgresql
    в таблицу customers"""

    with open('north_data/customers_data.csv', encoding='utf-8') as file:
        customers = csv.reader(file, delimiter=",")
        for i in customers:
            customer_id = i[0]
            company_name = i[1]
            contact_name = i[2]

            with psycopg2.connect(host="localhost", database="north", user="admi", password="1234") as conn:
                with conn.cursor() as cur:
                    cur.execute('INSERT INTO customers VALUES(%s, %s, %s)', (customer_id, company_name, contact_name))
                    cur.execute('SELECT * FROM customers')
            conn.close()








