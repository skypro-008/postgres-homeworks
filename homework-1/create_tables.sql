-- SQL-команды для создания таблиц
create table employees(
	employee_id serial PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar (100) NOT NULL,
	title text,
	birth_date date NOT NULL,
	notes text
);
create table customers(
	customer_id char(5) PRIMARY KEY,
	company_name text,
	contact_name text
);
create table orders(
	order_id int PRIMARY KEY,
	customer_id char(5) REFERENCES customers(customer_id) NOT NULL,
	employee_id serial REFERENCES employees(employee_id) NOT NULL,
	oder_date date NOT NULL,
	ship_city text
)
