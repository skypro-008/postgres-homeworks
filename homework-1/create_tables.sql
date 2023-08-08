-- SQL-команды для создания таблиц

CREATE TABLE employees (
    employee_id integer PRIMARY KEY,
    first_name varchar(50),
    last_name varchar(50),
    title varchar(255),
    birth_date date,
    notes text
);

CREATE TABLE customers (
    customer_id varchar(50) PRIMARY KEY,
    company_name varchar(50),
    contact_name varchar(50)
);

CREATE TABLE orders (
    order_id integer PRIMARY KEY,
    customer_id varchar(50) REFERENCES customers,
    employee_id integer REFERENCES employees,
    order_date date,
    ship_city varchar(50)
);
