"""Скрипт для заполнения данными таблиц в БД Postgres."""
import csv
import psycopg2

connect = psycopg2.connect(host="localhost", database="north", user="postgres", password="12345")
cursor = connect.cursor()

# absolute paths
file_path_employees = r"C:\Users\janle\PycharmProjects\postgres-homeworks\homework-1\north_data\employees_data.csv"
file_path_customers = r"C:\Users\janle\PycharmProjects\postgres-homeworks\homework-1\north_data\customers_data.csv"
file_path_orders = r"C:\Users\janle\PycharmProjects\postgres-homeworks\homework-1\north_data\orders_data.csv"

with open(file_path_employees, "r") as file:
    employees = csv.reader(file)
    next(employees)  # skip 1st row
    for row in employees:
        cursor.execute("""
            INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (int(row[0]), row[1], row[2], row[3], row[4], row[5]))

with open(file_path_customers, "r") as file:
    customers = csv.reader(file)
    next(customers)
    for row in customers:
        cursor.execute("""
            INSERT INTO customers (customer_id, company_name, contact_name)
            VALUES (%s, %s, %s)
        """, (row[0], row[1], row[2]))

with open(file_path_orders, "r") as file:
    orders = csv.reader(file)
    next(orders)
    for row in orders:
        cursor.execute("""
            INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)
            VALUES (%s, %s, %s, %s, %s)
        """, (row[0], row[1], int(row[2]), row[3], row[4]))

connect.commit()
connect.close()
