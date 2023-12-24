-- SQL-команды для создания таблиц
CREATE TABLE customers
(
	customer_id char(5) NOT NULL,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL,
	UNIQUE (customer_id)
);

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL,
	notes text
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id char(5) UNIQUE REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_data date NOT NULL,
	ship_city varchar(50) NOT NULL
);