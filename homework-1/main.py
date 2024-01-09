"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os

from dotenv import load_dotenv
from classes import PostgreDatabase
from utils.for_open_file import open_csv_file
from config import CUSTOMERS_PATH, EMPLOYEES_PATH, ORDERS_PATH

load_dotenv()

PORT = os.getenv("PORT")

customers = open_csv_file(CUSTOMERS_PATH)
employees = open_csv_file(EMPLOYEES_PATH)
orders = open_csv_file(ORDERS_PATH)

database = PostgreDatabase("localhost", "north", "postgres", PORT)
connection = database.connect()

try:
    database.insert_into_the_table(connection, "customers", "(%s, %s, %s)", customers)
    database.insert_into_the_table(connection, "employees", "(%s, %s, %s, %s, %s, %s)", employees)
    database.insert_into_the_table(connection, "orders", "(%s, %s, %s, %s, %s)", orders)

finally:
    connection.close()
