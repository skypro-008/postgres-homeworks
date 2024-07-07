import csv
import psycopg2
import os


def read_csv_file(filepath):
    with open(filepath, newline='', encoding='utf-8') as csvfile:
        filereader = csv.reader(csvfile)
        next(filereader)
        return [tuple(row) for row in filereader]


def insert_customers(conn, data):
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s) ON CONFLICT (customer_id) DO NOTHING;",
        data
    )
    print(f"Customers: Успешно вставлено {cur.rowcount} записей.")


def insert_employees(conn, data):
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s, %s) ON CONFLICT (employee_id) DO NOTHING;",
        data
    )
    print(f"Employees: Успешно вставлено {cur.rowcount} записей.")


def insert_orders(conn, data):
    cur = conn.cursor()
    cur.executemany(
        "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (order_id) DO NOTHING;",
        data
    )
    print(f"Orders: Успешно вставлено {cur.rowcount} записей.")


def main():
    global conn
    db_params = {
        'host': 'localhost',
        'database': 'north',
        'user': 'postgres',
        'password': os.getenv('DB_PASSWORD', '1014'),
        'port': '5433'
    }

    try:
        conn = psycopg2.connect(**db_params)
        conn.autocommit = True

        customers_data = read_csv_file(
            '/Users/anastasiya/PycharmProjects/python/postgres/postgres-homeworks/homework-1/north_data/customers_data.csv')
        insert_customers(conn, customers_data)

        employees_data = read_csv_file(
            '/Users/anastasiya/PycharmProjects/python/postgres/postgres-homeworks/homework-1/north_data/employees_data.csv')
        insert_employees(conn, employees_data)

        orders_data = read_csv_file(
            '/Users/anastasiya/PycharmProjects/python/postgres/postgres-homeworks/homework-1/north_data/orders_data.csv')
        insert_orders(conn, orders_data)

    except psycopg2.DatabaseError as e:
        print(f"Ошибка базы данных: {e}")
    finally:
        if conn:
            conn.close()


if __name__ == '__main__':
    main()
