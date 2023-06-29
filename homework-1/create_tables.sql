-- SQL-команды для создания таблиц
CREATE DATABASE north;

CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name CHARACTER VARYING(30),
	last_name CHARACTER VARYING(30),
	title CHARACTER VARYING(30),
	birth_date date,
	notes text
);

CREATE TABLE customers
(
	customer_id CHARACTER VARYING(30) PRIMARY KEY,
	company_name text,
	contact_name CHARACTER VARYING(30)
);


CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id CHARACTER VARYING(30),
	employee_id int,
	order_date date NOT NULL,
	ship_city CHARACTER VARYING(30)
);
