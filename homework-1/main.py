"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

def get_data_from_csv(key: str, path:str):
    with open(path, encoding='utf-8') as file:
        reader = csv.DictReader(file)
        data = []
        if key == 'employees':
            for row in reader:
                first_name = row['first_name']
                last_name = row['last_name']
                profession = row['title']
                description = row['notes']
                data.append((first_name, last_name, profession, description))

        elif key == 'customers':
            for row in reader:
                customer_id = row['customer_id']
                company_name = row['company_name']
                contact = row['contact_name']
                data.append((customer_id, company_name, contact))

        elif key == 'orders':
            for row in reader:
                order_id = row['order_id']
                customer_id = row['customer_id']
                employee_id = row['employee_id']
                order_date = row['order_date']
                ship_city = row['ship_city']
                data.append((order_id, customer_id, employee_id, order_date, ship_city))
        return data

employees = get_data_from_csv('employees', 'north_data/employees_data.csv')
customers = get_data_from_csv('customers', 'north_data/customers_data.csv')
orders = get_data_from_csv('orders', 'north_data/orders_data.csv')

def main():
    conn = psycopg2.connect(host='localhost', database='north2', user='postgres', password='12345')

    try:
        with conn:
            with conn.cursor() as cur:
                cur.executemany('INSERT INTO employees (first_name, last_name, title, notes)' 
                                'VALUES (%s, %s, %s, %s)', employees)
                cur.executemany('INSERT INTO customers (customer_id, company_name, contact_name)'
                                'VALUES (%s, %s, %s)', customers)
                cur.executemany('INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city)'
                                'VALUES (%s, %s, %s, %s, %s)', orders)

    finally:
        conn.close()

if __name__ == '__main__':
    main()
