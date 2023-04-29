-- SQL-команды для создания таблиц
CREATE TABLE employees
(
employee_id serial PRIMARY KEY,
first_name text NOT NULL,
last_name text NOT NULL,
title text,
birth_date date,
notes text
);

CREATE TABLE customers
(
customer_id varchar(5) PRIMARY KEY,
company_name text NOT NULL,
contact_name text NOT NULL
);

CREATE TABLE orders
(
order_id int PRIMARY KEY,
customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,
employee_id int REFERENCES employees(employee_id) NOT NULL,
order_date date NOT NULL,
ship_city text
);
