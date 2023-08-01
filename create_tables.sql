"""Создание emlployees"

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(30) NOT NULL,
	birth_date date NOT NULL,
	notes text
)

"""Создание customers_data"

CREATE TABLE customers_data
(
	customer_id varchar(5) NOT NULL,
	company_name varchar(40) NOT NULL,
	contact_name varchar(30) NOT NULL
)

"""Создание orders_data"

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(5) NOT NULL,
	employee_id int NOT NULL,
	order_date date NOT NULL,
	ship_city varchar(20) NOT NULL
)