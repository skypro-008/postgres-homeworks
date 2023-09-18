-- SQL-команды для создания таблиц

""" Создание таблицы customers. """
CREATE TABLE customers
(
    customer_id VARCHAR(100) NOT NULL,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR((100) NOT NULL
);

SELECT * FROM customers;

""" Создание таблицы employees. """
CREATE TABLE employees
(
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR((100) NOT NULL,
    title VARCHAR((100) NOT NULL,
    birth_date DATE NOT NULL,
    notes TEXT
);

SELECT * FROM employees;

""" Создание таблицы orders. """
CREATE TABLE orders
(
    order_id INT PRIMARY KEY,
    customer_id VARCHAR(100) NOT NULL,
    employee_id INT UNIQUE REFERENCES employees(employee_id) NOT NULL,
    order_date DATE NOT NULL,
    ship_city VARCHAR(100) NOT NULL
);

SELECT * FROM orders;