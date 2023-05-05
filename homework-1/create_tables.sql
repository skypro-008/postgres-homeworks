-- SQL-command for creating Database
CREATE DATABASE north;


-- SQL-commands for creating Tables
CREATE TABLE employees
(
    employee_id serial PRIMARY KEY,
    first_name varchar(20) NOT NULL,
    last_name varchar(20) NOT NULL,
    title varchar(50) NOT NULL,
    birth_date timestamp NOT NULL,
    notes text NOT NULL
);

CREATE TABLE customers
(
    customer_id varchar(10) PRIMARY KEY,
    company_name varchar(50) NOT NULL,
    contact_name varchar(50) NOT NULL
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(5) REFERENCES customers(customer_id) NOT NULL,
    employee_id int REFERENCES employees(employee_id) NOT NULL,
    order_date timestamp NOT NULL,
    ship_city varchar(20) NOT NULL
);