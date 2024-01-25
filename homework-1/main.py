import csv
import psycopg2
"""Скрипт для заполнения данными таблиц в БД Postgres."""

try:
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='1'
    )
    with conn.cursor() as cur:
        with open('north_data/customers_data.csv', 'r') as customers_file:
            data = csv.DictReader(customers_file)
            for record in data:
                cur.execute('INSERT INTO customers VALUES (%s,%s,%s)',(
                    record['customer_id'],
                    record['company_name'],
                    record['contact_name']
                ))
        with open('north_data/employees_data.csv', 'r') as employees_file:
            data = csv.DictReader(employees_file)
            for record in data:
                cur.execute('INSERT INTO employees VALUES (%s,%s,%s,%s,%s,%s)',(
                    record['employee_id'],
                    record['first_name'],
                    record['last_name'],
                    record['title'],
                    record['birth_date'],
                    record['notes']
                ))
        with open('north_data/orders_data.csv', 'r') as orders_file:
            data = csv.DictReader(orders_file)
            for record in data:
                cur.execute('INSERT INTO orders VALUES (%s,%s,%s,%s,%s)',(
                    record['order_id'],
                    record['customer_id'],
                    record['employee_id'],
                    record['order_date'],
                    record['ship_city']
                ))
        cur.execute('SELECT * FROM employees')
        cur.execute('SELECT * FROM customers')
        cur.execute('SELECT * FROM orders')
finally:
    conn.commit()
    conn.close()
