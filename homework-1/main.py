import csv
import psycopg2


"""Скрипт для заполнения данными таблиц в БД Postgres."""
customers_data = './north_data/customers_data.csv'
employees_data = './north_data/employees_data.csv'
orders_data = './north_data/orders_data.csv'

connection = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='661104'
)

try:
    with connection:
        with connection.cursor() as cursor:

            with open(customers_data) as file:
                file_reader = csv.DictReader(file, delimiter=',')

                for i in file_reader:
                    customer_id = i.get('customer_id')
                    company_name = i.get('company_name')
                    contact_name = i.get('contact_name')

                    cursor.executemany(
                        'INSERT INTO customers VALUES (%s, %s, %s)',
                        [(customer_id, company_name, contact_name)])

            with open(employees_data) as file:
                file_reader = csv.DictReader(file, delimiter=',')

                for i in file_reader:
                    first_name = i.get('first_name')
                    last_name = i.get('last_name')
                    title = i.get('title')
                    birth_date = i.get('birth_date')
                    notes = i.get('notes')

                    cursor.executemany(
                        'INSERT INTO employees VALUES (default, %s, %s, %s, %s, %s)',
                        [(first_name, last_name, title, birth_date, notes)])

            with open(orders_data) as file:
                file_reader = csv.DictReader(file, delimiter=',')

                for i in file_reader:
                    order_id = i.get('order_id')
                    customer_id = i.get('customer_id')
                    employee_id = i.get('employee_id')
                    order_date = i.get('order_date')
                    ship_city = i.get('ship_city')

                    cursor.executemany(
                        'INSERT INTO orders VALUES (%s, %s, %s, %s, %s)',
                        [(order_id, customer_id, employee_id, order_date, ship_city)])

except Exception as e:
    print(e)

finally:
    if connection:
        connection.close()
