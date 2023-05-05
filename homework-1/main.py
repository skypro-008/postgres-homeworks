"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

path_employees_data = "./north_data/employees_data.csv"
path_customers_data = "./north_data/customers_data.csv"
path_orders_data = "./north_data/orders_data.csv"


def changing_csv(file_path: str) -> list:
    """Taking csv file and returning list"""
    list = []
    with open(file_path, newline='') as csvfile:
        spamreader = csv.DictReader(csvfile)
        for row in spamreader:
            list.append(row)
    return list


def employee_save():
    """Saving employees_data.csv to Table employees """
    i = 0
    employee = changing_csv(path_employees_data)
    conn = psycopg2.connect(host='Localhost', database='north', user='postgres',
                            password=input("Please,enter your password for Database \n-->:"))
    try:
        with conn:
            with conn.cursor() as cur:
                for emp in employee:
                    i += 1
                    cur.execute("Insert Into employees Values (%s, %s, %s, %s, %s, %s)", [i] + list(emp.values()))
    finally:
        conn.close()


def costomer_save():
    """Saving customers_data.csv to Table customers """
    customers = changing_csv(path_customers_data)
    conn = psycopg2.connect(host='Localhost', database='north', user='postgres',
                            password=input("Please,enter your password for Database \n-->:"))
    try:
        with conn:
            with conn.cursor() as cur:
                for customer in customers:
                    cur.execute("INSERT INTO customers VALUES (%s, %s, %s)", list(customer.values()))
    finally:
        conn.close()


def order_save():
    """Saving orders_data.csv to Table orders """
    orders = changing_csv(path_orders_data)
    conn = psycopg2.connect(host='Localhost', database='north', user='postgres',
                            password=input("Please,enter your password for Database \n-->:"))
    try:
        with conn:
            with conn.cursor() as cur:
                for order in orders:
                    cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", list(order.values()))
    finally:
        conn.close()


#employee_save()
#costomer_save()
#order_save()
