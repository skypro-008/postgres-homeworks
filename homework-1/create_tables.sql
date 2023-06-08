CREATE TABLE employees
(
    employee_id serial PRIMARY KEY,
	first_name text NOT NULL,
	last_name text NOT NULL,
	title text NOT NULL,
	birth_date date NOT NULL,
	notes text NOT NULL
);

SELECT * FROM employees;

CREATE TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name text NOT NULL,
	contact_name text NOT NULL
);

SELECT * FROM customers;

CREATE TABLE orders
(
	order_id text,
	customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id),
	order_date text NOT NULL,
	ship_city text NOT NULL
);

SELECT * FROM orders;