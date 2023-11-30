"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import json
import os
import pathlib

import psycopg2
from utils import write_in_customer, write_in_employees, write_in_orders, read_psql

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="55555"
)

if __name__ == '__main__':

    print('1 сохранить customers\n2 сохранить employees\n3 сохранить orders\n4 показать записи таблиц')
    option = int(input(': '))

    if option == 1:
        write_in_customer(conn)

    elif option == 2:

        write_in_employees(conn)

    elif option == 3:

        write_in_orders(conn)

    elif option == 4:

        print('1 customer\n2 employees\n3 orders')
        opt = int(input(': '))

        if opt == 1:
            read_psql(conn, 'customers')

        elif opt == 2:
            read_psql(conn, 'employees')

        elif opt == 3:
            read_psql(conn, 'orders')

        else:
            print('не корректный ввод')

    else:
        print('не корректный ввод')

    conn.close()
