import psycopg2
import csv

def open_csv_file(file):
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        return csv_reader


"""Скрипт для заполнения данными таблиц в БД Postgres."""


