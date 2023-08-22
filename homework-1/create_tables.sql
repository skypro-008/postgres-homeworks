CREATE TABLE customers_data
(
	customer_id varchar(255) PRIMARY KEY,
	company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE employees_data
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date date,
	notes text
);

CREATE TABLE orders_data
(
	order_id int PRIMARY KEY,
	customer_id varchar(255) REFERENCES customers_data(customer_id),
	employee_id int REFERENCES employees_data(employee_id),
	order_date date,
	ship_city varchar(100) NOT NULL
);

SELECT * FROM employees_data
SELECT * FROM customers_data
SELECT * FROM orders_data
