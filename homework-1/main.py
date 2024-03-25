"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from config import EMPLOYEES_DATA_PATH, CUSTOMERS_DATA_PATH, ORDERS_DATA_PATH


def connecting():
    # connect to db
    conn = psycopg2.connect(
        host='localhost',
        database='north',
        user='postgres',
        password='Iwilldietomorrow92815'
    )
    try:
        adding_data_in_table(conn, taking_information(CUSTOMERS_DATA_PATH), 'customers', '%s, %s, %s')
        adding_data_in_table(conn, taking_information(EMPLOYEES_DATA_PATH), 'employees', '%s, %s, %s, %s, %s, %s')
        adding_data_in_table(conn, taking_information(ORDERS_DATA_PATH), 'orders', '%s, %s, %s, %s, %s')

    finally:
        conn.close()


def taking_information(file):
    # open some files and return data from them
    with open(file, 'r', encoding='utf8') as f:
        data = f.readlines()

    return data


def adding_data_in_table(conn, data, table_name, count):
    with conn:
        with conn.cursor() as cur:
            for i in range(1, len(data)):
                print(data[i])
                data_list = data[i].replace('\n', '').replace('"', '').split(',')
                if data == EMPLOYEES_DATA_PATH:
                    data_list[5] = (', '.join([data_list[j] for j in range(5, len(data_list))]))

                cur.execute(f'INSERT INTO {table_name} VALUES ({count})', data_list)


if __name__ == '__main__':
    connecting()
