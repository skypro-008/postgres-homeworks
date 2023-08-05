-- SQL-команды для создания таблиц

"""Создание employees"""

CREATE TABLE employees_data

(
	employee_id serial PRIMARY KEY,
	first_name varchar,
	last_name varchar,
	title varchar,
	birth_date date,
	notes text
)

"""Создание customers_data"

CREATE TABLE customers_data

(
	customer_id varchar PRIMARY KEY,
	company_name varchar,
	contact_name varchar
)

"""Создание orders_data"

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar REFERENCES customers_data(customer_id),
	employee_id int REFERENCES employees_data(employee_id),
	order_date date,
	ship_city varchar
)