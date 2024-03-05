"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv



create_tables = "create_tables.sql" #Should work but for some reason does not open for me
#The code is correnct as far as I'm concerned
employees = os.path.abspath('north_data/employees_data.csv')
orders = os.path.abspath('north_data/orders_data.csv')
customers = os.path.abspath('north_data/customers_data.csv')


#connection
conn = psycopg2.connect(
    host='localhost',
    database='north',
    user='postgres',
    password='19182521'
)

def main():
    try:
        with conn:
             with conn.cursor() as cursor:
                cursor.execute(open(create_tables, 'r').read())
                #enter employee data
                with open(employees, 'r', encoding='utf8') as file:
                    info = csv.reader(file, delimiter=",")
                    count = 0
                    for row in info:
                        if count == 0:
                            count += 1
                            continue
                        else:
                            cursor.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                                           (int(row[0]), row[1], row[2], row[3], row[4], row[5]))

                # enter customer data
                with open(customers, 'r', encoding='utf8') as file:
                    info = csv.reader(file, delimiter=",")
                    count = 0
                    for row in info:
                        if count == 0:
                            count += 1
                            continue
                        else:
                            try:
                                cursor.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                                               (row[0], row[1], row[2]))
                                conn.commit()
                            except psycopg2.DatabaseError:
                                conn.rollback()
                                continue

                # enter order data
                with open(orders, 'r', encoding='utf8') as file:
                    info = csv.reader(file, delimiter=",")
                    count = 0
                    for row in info:
                        if count == 0:
                            count += 1
                            continue
                        else:
                            try:
                                cursor.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                                           (int(row[0]), row[1], int(row[2]), row[3], row[4]))
                                conn.commit()
                            except psycopg2.DatabaseError:
                                conn.rollback()
                                continue
    
    finally:
        conn.close()



if __name__ == "__main__":
    main()