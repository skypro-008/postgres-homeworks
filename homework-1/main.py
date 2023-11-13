"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

if __name__ == '__main__':

    conn = psycopg2.connect(
        host="localhost",
        database="north",
        user="postgres",
        password="55555"
    )

    try:
        with conn:
            with conn.cursor() as cur:
                cur.execute('CREATE TABLE customers (customer_id varchar(30) PRIMARY KEY, company_name \
                varchar(100) NOT NULL, contact_name varchar(100));')

                cur.execute('CREATE TABLE employees(employees_id int PRIMARY KEY, first_name varchar(50) NOT NULL, \
                last_name varchar(50) NOT NULL, title varchar(100) NOT NULL, birth_date varchar(50), \
                notes text NOT NULL)')

    finally:
        conn.close()



