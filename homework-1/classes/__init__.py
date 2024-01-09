from datetime import datetime
from typing import Any

import psycopg2


class Customer:
    """
    Класс необходим для создания сущности покупателя
    """

    def __init__(self, customer_id: str, company_name: str, contact_name: str):
        self.customer_id = customer_id
        self.company_name = company_name
        self.contact_name = contact_name


class Employee:
    """
    Класс необходим для создания сущности работника
    """

    def __init__(self, employee_id: int, first_name: str, last_name: str, title: str, birth_date: datetime, notes: str):
        self.employee_id = employee_id
        self.first_name = first_name
        self.last_name = last_name
        self.title = title
        self.birth_date = birth_date
        self.notes = notes


class Order:
    """
    Класс необходим для создания сущности заказа
    """

    def __init__(self, order_id: int, customer_id: str, employee_id: int, order_date: datetime, ship_city: str):
        self.order_id = order_id
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.order_date = order_date
        self.ship_city = ship_city


class PostgreDatabase:
    """
    Класс для работы с базой данных в PostgreSQL
    """

    def __init__(self, host: str, database: str, user: str, password: Any):
        self._host = host
        self._database = database
        self._user = user
        self._password = password

    def connect(self):
        """
        Метод для подключения к базе данных
        """
        return psycopg2.connect(host=self._host, database=self._database, user=self._user, password=self._password)

    @staticmethod
    def insert_into_the_table(connection, table_name, formatter, data):
        """
        Метод для вставки данных в таблицу
        """
        with connection:
            with connection.cursor() as cur:
                if len(data) > 1:
                    cur.executemany(f"INSERT INTO {table_name} VALUES {formatter}", data)
                else:
                    cur.execute(f"INSERT INTO {table_name} VALUES {formatter}", data)
