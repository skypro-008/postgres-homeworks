-- SQL-команды для создания таблиц
CREATE DATABASE north;

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title text NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

CREATE TABLE customers
(
	customer_id char(5) UNIQUE PRIMARY KEY,
	company_name text NOT NULL,
	contact_name text NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
    employee_id INT REFERENCES employees(employee_id) NOT NULL,
    order_date DATE NOT NULL,
    ship_city TEXT
);