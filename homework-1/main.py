"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import os
import psycopg2

# Подключение к базе данных
cone = psycopg2.connect(
    dbname="north",
    user="postgres",
    password="8810533",
    host="localhost",
    port="5432"
)

north_path = os.path.dirname('north_data/')
file_name_1 = 'employees_data.csv'
file_name_2 = 'customers_data.csv'
file_name_3 = 'orders_data.csv'
file_path_1 = os.path.join(north_path, file_name_1)
file_path_2 = os.path.join(north_path, file_name_2)
file_path_3 = os.path.join(north_path, file_name_3)

with cone as conn:
    with conn.cursor() as cur:
        # Загрузка данных в таблицу employees_data
        with open(file_path_1, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # пропуск заголовков столбцов
            for row in reader:
                cur.execute("INSERT INTO employees_data (employee_id, first_name, last_name, title, birth_date, notes) "
                            "VALUES (%s, %s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4], row[5]))
        # Загрузка данных в таблицу customers_data
        with open(file_path_2, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO customers_data (customer_id, company_name, contact_name)"
                            "VALUES (%s, %s, %s)",
                            (row[0], row[1], row[2]))
        # Загрузка данных в таблицу orders_data
        with open(file_path_3, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                cur.execute("INSERT INTO orders_data (order_id, customer_id, employee_id, order_date, ship_city)"
                            "VALUES (%s, %s, %s, %s, %s)",
                            (row[0], row[1], row[2], row[3], row[4]))

# Закрытие соединения
conn.close()


