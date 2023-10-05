"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

FILE_CUSTOMERS_DATA = 'north_data/customers_data.csv'
FILE_EMPLOYEES_DATA = 'north_data/employees_data.csv'
FILE_ORDERS_DATA = 'north_data/orders_data.csv'


def insert_data_to_sql(filename, name_table):
    with open(filename, 'r', encoding='UTF-8') as file:
        data = csv.DictReader(file)
        with psycopg2.connect(host="localhost", database="north", user="denis", password="123456") as conn:
            with conn.cursor() as curs:
                for row in data:
                    row_data = []
                    values_designation = []
                    for key in list(row.keys()):
                        row_data.append(row[key])
                        values_designation.append('%s')
                    curs.execute(f"INSERT INTO {name_table} VALUES ({', '.join(values_designation)})", tuple(row_data))
                    row_data.clear()
                    values_designation.clear()
        conn.close()


insert_data_to_sql(FILE_CUSTOMERS_DATA, 'customers')
insert_data_to_sql(FILE_EMPLOYEES_DATA, 'employees')
insert_data_to_sql(FILE_ORDERS_DATA, 'orders')
