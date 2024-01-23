"""Скрипт для заполнения данными таблиц в БД Postgres."""
import pandas as pd
import psycopg2

# Параметры подключения к базе данных
db_params = {
    'host': 'localhost',
    'database': 'north',
    'user': 'postgres',
    'password': '050305'
}


# Функция для выполнения SQL-запросов
def execute_query():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    try:
        # Чтение данных из CSV файла в DataFrame
        employees_data = pd.read_csv('north_data/employees_data.csv')
        customers_data = pd.read_csv('north_data/customers_data.csv')
        orders_data = pd.read_csv('north_data/orders_data.csv')

        # Вставка данных в таблицу employees
        cursor.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)", employees_data.values)

        # Вставка данных в таблицу customers
        cursor.executemany("INSERT INTO customers VALUES (%s, %s, %s)", customers_data.values)

        # Вставка данных в таблицу orders
        cursor.executemany("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)", orders_data.values)

        # Применение изменений
        conn.commit()
        print("Data successfully inserted.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Не забудьте закрыть соединение
        cursor.close()
        conn.close()


# Вызов функции
execute_query()
