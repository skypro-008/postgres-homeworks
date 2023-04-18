import csv
import psycopg2


"""Скрипт для заполнения данными таблиц в БД Postgres."""
customers_data = './north_data/customers_data.csv'
employees_data = './north_data/employees_data.'
orders_data = './north_data/orders_data'

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
                        [(customer_id, company_name, contact_name)]
                    )

except Exception as e:
    print(e)

finally:
    if connection:
        connection.close()

