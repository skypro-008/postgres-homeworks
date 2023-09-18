"""Скрипт для заполнения данными таблиц в БД Postgres."""

import psycopg2
import csv


def executing_sql(query):

    """ Функция для установления соединения и выполнения запросов. """

    conn = psycopg2.connect(host="localhost", port="5432", database="north", user="postgres")
    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute(query)
    finally: conn.close()


def filling_in_tables(name, csv_file):

    """ Функция для заполнения таблиц. """

    with open(csv_file, "r", newline="", encoding="utf-8") as file:
        rows = csv.reader(file)
        for row in rows:
            values = "', '".join(row)
            query = f"INSERT INTO {name} VALUES ('{values}');"
            executing_sql(query)


# Заполнение таблицы employees данными
employees_csv = "north_data/employees_data.csv"
filling_in_tables("employees", employees_csv)

# Заполнение таблицы customers данными
customers_csv = "north_data/customers_data.csv"
filling_in_tables("customers", customers_csv)

# Заполнение таблицы orders данными
orders_csv = "north_data/orders_data.csv"
filling_in_tables("orders", orders_csv)
