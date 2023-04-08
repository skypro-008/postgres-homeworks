import pprint

import psycopg2
import csv

"""Скрипт для заполнения данными таблиц в БД Postgres."""

#connect to db
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='Xthtpnthybb1!'
)

file1 = './north_data/customers_data.csv'
file2 = './north_data/employees_data.csv'
file3 = './north_data/orders_data.csv'

# def get_read_csv(file):
#     data = []
#     with open(file, 'r', encoding='UTF=8') as f:
#         data_file = csv.DictReader(f)
#         for i in data_file:
#             data.append(i)
#         return data


def get_read_csv(file):
    data = []
    with open(file, 'r', encoding='UTF-8') as f:
        data_reader = csv.reader(f)
        next(data_reader, None)
        for d in data_reader:
            data.append(d)
        return data


# try:
#     with conn:
#         with conn.cursor() as cur:
#             data_customer = get_read_csv(file2)
#             for i in data_customer:
#                 # exeсute query
#                 cur.execute('INSERT INTO customers VALUES (%s, %s, %s)', i)
#                 cur.execute('SELECT * FROM customers')
#                 rows = cur.fetchall()
#                 for row in rows:
#                     print(row)
# finally:
#     # close connection
#     conn.close()


# try:
#     with conn:
#         with conn.cursor() as cur:
#             data_employee = get_read_csv(file2)
#             for i in data_employee:
                    # exeсute query
#                 cur.execute('INSERT INTO employees (first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s)', i)
#                 # cur.execute('SELECT * FROM employees')
#                 # rows = cur.fetchall()
#                 # for row in rows:
#                 #     print(row)
# finally:
#     # close connection
#     conn.close()


# try:
#     with conn:
#         with conn.cursor() as cur:
#             data_orders = get_read_csv(file3)
#             for i in data_orders:
#                 # exeсute query
#                 cur.execute('INSERT INTO orders VALUES (%s, %s, %s, %s, %s)', i)
#                 # cur.execute('SELECT * FROM employees')
#                 # rows = cur.fetchall()
#                 # for row in rows:
#                 #     print(row)
# finally:
#     # close connection
#     conn.close()
