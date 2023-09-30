-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    title varchar(255),
	birth_date date,
    notes text
);
CREATE TABLE customers_data
(
    customer_id varchar(255) PRIMARY KEY,
    company_name varchar(255) NOT NULL,
    contact_name varchar(255) NOT NULL
);

CREATE TABLE orders_data
(
    order_id int PRIMARY KEY,
    customer_id varchar(255) NOT NULL,
    employee_id int NOT NULL,
    order_date date NOT NULL,
    ship_city varchar(255) NOT NULL
);

SELECT * FROM orders_data