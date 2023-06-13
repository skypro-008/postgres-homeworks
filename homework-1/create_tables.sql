-- SQL-команды для создания таблиц

CREATE TABLE employees
(
	employee_id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text NOT NULL
);

CREATE TABLE customers
(
	customer_id varchar(100) PRIMARY KEY NOT NULL,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);
CREATE TABLE orders
(
	order_id varchar(5) PRIMARY KEY NOT NULL,
	customer_id varchar(5) REFERENCES customers(customer_id),
	employee_id int REFERENCES employees(employee_id),
	order_date date NOT NULL,
	ship_city varchar(50) NOT NULL
);
