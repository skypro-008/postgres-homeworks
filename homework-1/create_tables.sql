-- SQL-команды для создания таблиц

"""Создание cemployees"""

CREATE TABLE employees_data
"""Это правильное и логичное создание таблицы"
(
	employee_id int PRIMARY KEY,
	first_name varchar(20),
	last_name varchar(20),
	title varchar(30),
	birth_date date,
	notes text
)
"""Так я создал чтобы дланные могли передаватся в виде строк"""
"""Это не совсем правильно, но copy не берет такое большое кол-во символов в столбце notes""""
(
	employee_id varchar(20) PRIMARY KEY,
	first_name varchar(20),
	last_name varchar(20),
	title varchar(30),
	birth_date varchar(20),
	notes text
)

"""Создание customers_data"

CREATE TABLE customers_data
(
	customer_id varchar(20) PRIMARY KEY,
	company_name varchar(40),
	contact_name varchar(30)
)

"""Создание orders_data"

CREATE TABLE orders_data
(
	order_id varchar(20),
	customer_id varchar(20) UNIQUE REFERENCES customers_data(customer_id) NOT NULL,
	employee_id varchar(20) UNIQUE REFERENCES employees_data(employee_id) NOT NULL,
	order_date varchar(20),
	ship_city varchar(20)
)