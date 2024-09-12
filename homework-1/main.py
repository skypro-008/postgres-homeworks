"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

if __name__ == '__main__':

    employees_csv = "../homework-1/north_data/employees_data.csv"
    customers_csv = "../homework-1/north_data/customers_data.csv"
    orders_csv = "../homework-1/north_data/orders_data.csv"

    # Подкючение к базе данных north
    conn = psycopg2.connect(host='localhost', database="north", user='postgres', password='sql2023', port='5432')

    conn.autocommit = True
    cursor = conn.cursor()

    # Копирование данных из файла employees_data.csv
    sql = '''COPY employees(employee_id,first_name,\
    last_name,title,birth_date,notes)
    FROM employees_csv
    DELIMITER ','
    CSV HEADER;'''

    cursor.execute(sql)

    sql_1 = '''select * from employees;'''
    cursor.execute(sql_1)
    for i in cursor.fetchall():
        print(i)

    # Копирование данных из файла customers_data.csv
    sql_2 = '''COPY customers(customer_id,company_name,\
    contact_name)
    FROM employees_csv
    DELIMITER ','
    CSV HEADER;'''

    cursor.execute(sql_2)

    sql_3 = '''select * from customers;'''
    cursor.execute(sql_3)
    for i in cursor.fetchall():
        print(i)

    # Копирование данных из файла orders_data.csv
    sql_4 = '''COPY orders(order_id,customer_id,\
    employee_id,order_date,ship_city)
    FROM orders_csv
    DELIMITER ','
    CSV HEADER;'''

    cursor.execute(sql_4)

    sql_5 = '''select * from orders;'''
    cursor.execute(sql_5)
    for i in cursor.fetchall():
        print(i)

    conn.commit()
    conn.close()
