-- SQL-команды для создания таблиц

-- Создание таблицы CUSTOMERS
CREATE TABLE customers
(
    customer_id VARCHAR PRIMARY KEY,
    company_name VARCHAR(50) NOT NULL,
    contact_name VARCHAR(50) NOT NULL
);


-- Создание таблицы EMPLOYEES
CREATE TABLE employees
(
    employee_id INTEGER PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    title VARCHAR(50) NOT NULL,
    birth_date DATE,
    notes TEXT
);


-- Создание таблицы ORDERS
CREATE TABLE orders
(
    order_id INTEGER PRIMARY KEY,
    customer_id VARCHAR REFERENCES customers(customer_id),
    employee_id INTEGER REFERENCES employees(employee_id),
    order_date DATE,
    ship_city VARCHAR(30)
);


