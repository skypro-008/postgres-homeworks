"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2


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
    """Функция открывает employees_data.csv и для записи данных в базу данных postgresql
        в таблицу employees"""
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


def orders_d():
    """Функция открывает orders_data.csv и для записи данных в базу данных postgresql
            в таблицу orders"""
    with open('north_data/orders_data.csv', encoding='utf-8') as file:
        orders = csv.DictReader(file, delimiter=",")
        for i in orders:
            order_id = i['order_id']
            customer_id = i['customer_id']
            employee_id = i['employee_id']
            order_date = i['order_date']
            ship_city = i["ship_city"]

            with psycopg2.connect(host="localhost", database="north", user="admi", password="1234") as conn:
                with conn.cursor() as cur:
                    cur.execute('INSERT INTO orders VALUES(%s, %s, %s, %s, %s)',
                                (order_id, customer_id, employee_id, order_date, ship_city))
                    cur.execute('SELECT * FROM orders')
            conn.close()
customers_d()
employees_d()
orders_d()