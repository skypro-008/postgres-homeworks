"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv
connect = psycopg2.connect(host = 'localhost',database='north', user='postgres', password='manager1')


def read_csv_to_bd(path:str, query:str)-> None:
    """функция, которая считывает данные из csv и записывает их в таблицу в БД"""
    with open(path, encoding='utf-8') as fp:
        csv_lists = csv.reader(fp)
        next(csv_lists)
        with connect.cursor() as curs:
            curs.executemany(query, csv_lists)
        connect.commit()
query_customers = """INSERT INTO customers(customer_id,company_name,contact_name)
                     VALUES (%s, %s,%s) """

query_employees = """INSERT INTO employees(employee_id,first_name,last_name,title,birth_date,notes)
                     VALUES (%s,%s,%s,%s,%s,%s) """

query_orders = """INSERT INTO orders(order_id,customer_id,employee_id,order_date,ship_city)
                     VALUES (%s,%s,%s,%s,%s) """

read_csv_to_bd('north_data/customers_data.csv', query_customers)
read_csv_to_bd('north_data/employees_data.csv', query_employees)
read_csv_to_bd('north_data/orders_data.csv', query_orders)
