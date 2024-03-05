"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import os
import csv

create_tables = 'create_tables.sql'
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
    conn.close()