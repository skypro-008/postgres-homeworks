"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os

import psycopg2

PASS = os.environ.get('PG_PASS')
DATA_PATH = os.path.abspath("../homework-1/north_data")


# Создаём список кортежей из файла csv для передачи в метод executemany
# is_id_data флаг для добавления id в таблицу employees
def get_data(file_name=""):
    result = []
    if os.path.exists(os.path.join(DATA_PATH, file_name)):
        with open(os.path.join(DATA_PATH, file_name), mode="r", encoding='utf-8') as r_file:
            file_reader = csv.reader(r_file, delimiter=",")
            is_not_title = False
            for row in file_reader:
                if is_not_title:
                    temp_list = []
                    for item in row:
                        temp_list.append(item)
                    result.append(tuple(temp_list))
                else:
                    is_not_title = True
    return result


# Подключаемся к базе и заполняем таблицы из csv файлов.
conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='silence11')
try:
    with conn:
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO customers VALUES (%s, %s, %s)", get_data('customers_data.csv'))
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                            get_data('employees_data.csv'))
        with conn.cursor() as cur:
            cur.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", get_data('orders_data.csv'))
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM customers")

finally:
    conn.close()