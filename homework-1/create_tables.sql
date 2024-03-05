-- SQL-команды для создания таблиц
Create TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(50) NOT NULL,
	last_name varchar(50) NOT NULL,
	title varchar(50) NOT NULL,
	birth_date date,
	notes text
);

Create TABLE customers
(
	customer_id varchar(5) PRIMARY KEY,
	company_name varchar(100),
	contact_name varchar(100)
);
Create TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar REFERENCES customers(customer_id) NOT NULL,
	employee_id int REFERENCES employees(employee_id) NOT NULL,
	order_date date,
	ship_city varchar(50),
	UNIQUE(customer_id)
)
