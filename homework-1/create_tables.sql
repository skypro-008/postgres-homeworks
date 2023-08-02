-- SQL-команды для создания таблиц

"""Создание cemployees"""

CREATE TABLE employees
"""Это правильное и логичное создание таблицы"
(
	employee_id int PRIMARY KEY,
	first_name varchar(20),
	last_name varchar(20),
	title varchar(30),
	birth_date date,
	notes varchar(500)
)
"""Так я создал чтобы дланные могли передаватся в виде строк"""
"""Это не совсем правильно, но copy не берет такое большое кол-во символов в столбце notes""""
(
	employee_id varchar(20),
	first_name varchar(20),
	last_name varchar(20),
	title varchar(30),
	birth_date varchar(20),
	notes varchar(500)
)

"""Создание customers_data"

CREATE TABLE customers_data
(
	customer_id varchar(10),
	company_name varchar(40),
	contact_name varchar(30)
)

"""Создание orders_data"

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(10),
	employee_id int,
	order_date date,
	ship_city varchar(20)
)