import psycopg2
import csv

# имена файлов
customers_data = "customers_data.csv"
employees_data = "employees_data.csv"
orders_data = "orders_data.csv"


def get_list_from_file(path):
    with open(f"north_data/{path}", "r", encoding="utf-8") as f:
        file_list = csv.reader(f)
        total = []
        for el in file_list:
            total.append(el)

    return total


customers_data_list = get_list_from_file(customers_data)
employees_data_list = get_list_from_file(employees_data)
orders_data_list = get_list_from_file(orders_data)

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="12345"
)
cur = conn.cursor()


def fill_table(data_list, name_table):
    data_list = data_list[1:]

    for el in data_list:
        string_config = "%s, " * len(data_list[0])
        cur.execute(f"INSERT INTO {name_table} VALUES ({string_config[:-2]})", tuple(el))


fill_table(customers_data_list, "customers")
fill_table(employees_data_list, "employees")
fill_table(orders_data_list, "orders")

conn.commit()

cur.close()
conn.close()
