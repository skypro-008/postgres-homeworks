"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import json
import os
import pathlib

import psycopg2
from utils import write_in_customer, write_in_employees, write_in_orders

way_customers = pathlib.Path(__file__).parent.joinpath('north_data').joinpath('customers_data.csv')
way_employees = pathlib.Path(__file__).parent.joinpath('north_data').joinpath('employees_data.csv')
way_orders = pathlib.Path(__file__).parent.joinpath('north_data').joinpath('orders_data.csv')

if __name__ == '__main__':

    print('1 сохранить customers\n2 сохранить employees\n3 сохранить orders\n4 показать записи таблиц')
    option = int(input(': '))

    if option == 1:

        with open(way_customers, 'r', encoding='utf8') as file:
            result = csv.reader(file)

            for i in result:

                if i[0] != 'customer_id':
                    write_in_customer(i)

    elif option == 2:

        with open(way_employees, 'r', encoding='utf8') as file:
            result = csv.reader(file)

            for i in result:

                if i[0] != 'employee_id':
                    write_in_employees(i)

    elif option == 3:

        with open(way_orders, 'r', encoding='utf8') as file:
            result = csv.reader(file)

            for i in result:

                if i[0] != 'order_id':
                    write_in_orders(i)

    elif option == 4:

        print('1 customer\n2 employees\n3 orders')
        opt = int(input(': '))

        if opt == 1:

            conn = psycopg2.connect(
                host="localhost",
                database="north",
                user="postgres",
                password="55555"
            )

            try:

                with conn:

                    with conn.cursor() as cur:

                        cur.execute('SELECT * FROM customers')
                        row = cur.fetchall()

                        for i in row:
                            print(i)

            finally:

                conn.close()

        elif opt == 2:

            conn = psycopg2.connect(
                host="localhost",
                database="north",
                user="postgres",
                password="55555"
            )

            try:

                with conn:

                    with conn.cursor() as cur:

                        cur.execute('SELECT * FROM employees')
                        row = cur.fetchall()

                        for i in row:
                            print(i)

            finally:

                conn.close()

        elif opt == 3:

            conn = psycopg2.connect(
                host="localhost",
                database="north",
                user="postgres",
                password="55555"
            )

            try:
                with conn:

                    with conn.cursor() as cur:
                        cur.execute('SELECT * FROM orders')
                        row = cur.fetchall()

                        for i in row:
                            print(i)

            finally:
                conn.close()

        else:
            print('не корректный ввод')

    else:
        print('не корректный ввод')
