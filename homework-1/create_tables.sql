-- SQL-команды для создания таблиц
CREATE TABLE IF NOT EXISTS customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name text NOT NULL,
	contact_name text NOT NULL
);

CREATE TABLE IF NOT EXISTS employees
(
	employee_id smallserial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date NOT NULL DEFAULT CURRENT_DATE,
	notes text
);

CREATE TABLE IF NOT EXISTS orders
(
	order_id serial PRIMARY KEY,
	customer_id varchar REFERENCES customers(customer_id),
	employee_id smallserial REFERENCES employees(employee_id),
	order_date date NOT NULL DEFAULT CURRENT_DATE,
	ship_city varchar(50) NOT NULL
);
