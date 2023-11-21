-- SQL-команды для создания таблиц
CREATE TABLE customers_data
(
	customer_id char(10) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT NULL
);

CREATE TABLE employes_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(20) NOT NULL,
	last_name varchar(20) NOT NULL,
	title varchar(200) NOT NULL,
	birth_data date NOT NULL,
	notes text
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(10) REFERENCES customers_data(customer_id),
	employee_id int REFERENCES employes_data(employee_id),
	order_date date NOT NULL,
	ship_city varchar(50) NOT NULL
);

SELECT * FROM customers_data
SELECT * FROM employes_data
SELECT * FROM orders_data