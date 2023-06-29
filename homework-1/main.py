"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2
import pandas as pd

def customers_d():
    """Функция открывает customers_data.csv и для записи данных в базу данных postgresql
    в таблицу customers"""

    with open('north_data/customers_data.csv', encoding='utf-8') as file:
        customers = csv.DictReader(file, delimiter=",")
        for i in customers:
            customer_id = i['customer_id']
            company_name = i['company_name']
            contact_name = i['contact_name']

            with psycopg2.connect(host="localhost", database="north", user="admi", password="1234") as conn:
                with conn.cursor() as cur:
                    cur.execute('INSERT INTO customers VALUES(%s, %s, %s)', (customer_id, company_name, contact_name))
                    cur.execute('SELECT * FROM customers')
            conn.close()

def employees_d():
    with open('north_data/employees_data.csv', encoding='utf-8') as file:
        employees = csv.DictReader(file, delimiter=",")
        for i in employees:
            employee_id = i['employee_id']
            first_name = i['first_name']
            last_name = i['last_name']
            title = i['title']
            birth_date = i["birth_date"]
            notes = i['notes']

            with psycopg2.connect(host="localhost", database="north", user="admi", password="1234") as conn:
                with conn.cursor() as cur:
                    cur.execute('INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)',
                                (employee_id, first_name, last_name, title, birth_date, notes))
                    cur.execute('SELECT * FROM employees')
            conn.close()


