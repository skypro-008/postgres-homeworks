-- SQL-команды для создания таблиц
CREATE DATABASE north;

CREATE TABLE customers (customer_id varchar(30) PRIMARY KEY,
						company_name varchar(100) NOT NULL,
						contact_name varchar(100) NOT NULL
					   )

CREATE TABLE employees(employees_id int PRIMARY KEY,
					   first_name varchar(50) NOT NULL,
					   last_name varchar(50) NOT NULL,
					   title varchar(100) NOT NULL,
					   birth_date varchar(50),
					   notes text NOT NULL
					  );

CREATE TABLE orders (
	order_id int PRIMARY KEY,
	customer_id varchar(30),
	employees_id int NOT NULL,
	order_date varchar(50) NOT NULL,
	ship_city varchar(100)
)