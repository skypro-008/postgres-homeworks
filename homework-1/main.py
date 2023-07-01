"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

FILE_NAME1 = "./north_data/customers_data.csv"
FILE_NAME2 = "./north_data/employees_data.csv"
FILE_NAME3 = "./north_data/orders_data.csv"

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="123"
)


def read_file(file_name, table_name):

    """Загружает данные из файла в таблицу"""

    with open(file_name, mode="r", encoding='utf-8') as file_customers:
        file_customers.readline()

        for file_lines in file_customers.readlines():
            try:
                cleared_line = file_lines.replace("\\\n", "").replace("\'", "\'\'").replace("\"", "\'")
                cur.execute(f"INSERT INTO {table_name} VALUES ({cleared_line})")
            except Exception as e:
                print(f"Пропускаю строку {file_lines}, ошибка {e}")

if __name__ == '__main__':
    try:
        with conn.cursor() as cur:
            read_file(FILE_NAME1, "customers")
            read_file(FILE_NAME2, "employees")
            read_file(FILE_NAME3, "orders")
            conn.commit()
    finally:
        conn.close()
