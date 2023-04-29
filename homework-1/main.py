"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv

import psycopg2


def main():
    # connect to db
    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="12345"
    )
    employees_table = "north_data/employees_data.csv"
    customers_table = "north_data/customers_data.csv"
    orders_table = "north_data/orders_data.csv"

    try:
        with conn:
            with conn.cursor() as cur:
                with open(employees_table, "r", encoding="UTf-8", newline="") as f:
                    data = csv.reader(f, delimiter=',')
                    count = 1
                    skip_header = True  # флаг, чтобы пропустить заголовки
                    for tuple_row in data:
                        if skip_header:
                            skip_header = False
                            continue  # пропускаем первую строку с заголовками
                        # execute query
                        cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                    (count, tuple_row[0], tuple_row[1], tuple_row[2], tuple_row[3], tuple_row[4]))
                        count += 1
                        cur.execute("SELECT * FROM employees")

                        rows = cur.fetchall()
                        # print(rows)  # показывает список кортежей из таблицы
                        for row in rows:
                            print(row)

                with open(customers_table, "r", encoding="UTf-8", newline="") as f:
                    data = csv.reader(f, delimiter=',')
                    skip_header = True  # флаг, чтобы пропустить заголовки
                    for tuple_row in data:
                        if skip_header:
                            skip_header = False
                            continue  # пропускаем первую строку с заголовками
                        # execute query
                        cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                    (tuple_row[0], tuple_row[1], tuple_row[2]))
                        cur.execute("SELECT * FROM customers")

                        rows = cur.fetchall()
                        # print(rows)  # показывает список кортежей из таблицы
                        for row in rows:
                            print(row)

                with open(orders_table, "r", encoding="UTf-8", newline="") as f:
                    data = csv.reader(f, delimiter=',')
                    skip_header = True  # флаг, чтобы пропустить заголовки
                    for tuple_row in data:
                        if skip_header:
                            skip_header = False
                            continue  # пропускаем первую строку с заголовками
                        # execute query
                        cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                    (tuple_row[0], tuple_row[1], tuple_row[2], tuple_row[3], tuple_row[4]))
                        cur.execute("SELECT * FROM orders")

                        rows = cur.fetchall()
                        # print(rows)  # показывает список кортежей из таблицы
                        for row in rows:
                            print(row)

    finally:
        conn.close()  # close connection


if __name__ == '__main__':
    main()
