"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os
from north_data.csv_data import get_csv_data
import psycopg2


def main():
    conn = psycopg2.connect(host='localhost', database='north', user='postgres', password='4622')
    try:
        path_csv_files = ['north_data/customers_data.csv', 'north_data/employes_data.csv', 'north_data/orders_data.csv']
        for path in path_csv_files:
            path_csv = os.path.join(os.path.dirname(__file__), path)
            csv_data = get_csv_data(path_csv)
            with conn:
                with conn.cursor() as cur:
                    columns = len(csv_data[0]) * '%s, '
                    for i in csv_data[1:]:
                        cur.execute(f'INSERT INTO {path[11:-4]} VALUES ({columns.rstrip(", ")})', i)
    finally:
        conn.close()


if __name__ == '__main__':
    main()
