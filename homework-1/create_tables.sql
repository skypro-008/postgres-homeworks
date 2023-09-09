-- SQL-команды для создания таблиц
CREATE TABLE employees (
    employee_id int PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    title VARCHAR(100) NOT NULL,
	birth_date DATE NOT NULL,
	notes text NOT NULL
);

CREATE TABLE customers (
    customer_id VARCHAR PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id VARCHAR REFERENCES customers(customer_id),
    employee_id INT REFERENCES employees(employee_id),
    order_date DATE NOT NULL,
    ship_city VARCHAR(50) NOT NULL
);