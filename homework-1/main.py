"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv


def file_reader(path):
    """
    Функция для открытия файла csv и возвращения списка данных
    """
    with open(path, "r") as file:
        csv_reader = csv.reader(file)
        count = 0
        result = []
        for row in csv_reader:
            if count == 0:
                count += 1
            else:
                result.append(row)
                count += 1
    return result


customers_data = file_reader("north_data/customers_data.csv")
employees_data = file_reader("north_data/employees_data.csv")
orders_data = file_reader("north_data/orders_data.csv")

with psycopg2.connect(host="localhost", database="north", user="postgres", password="brnlol479") as conn:
    with conn.cursor() as cur:
        for customer in customers_data:
            cur.execute("INSERT INTO customers VALUES(%s, %s, %s)",
                        (customer[0], customer[1], customer[2]))
        for employee in employees_data:
            cur.execute("INSERT INTO employees VALUES(%s, %s, %s, %s, %s, %s)",
                        (employee[0], employee[1], employee[2], employee[3], employee[4], employee[5]))
        for order in orders_data:
            cur.execute("INSERT INTO orders VALUES(%s, %s, %s, %s, %s)",
                        (order[0], order[1], order[2], order[3], order[4]))
conn.close()
