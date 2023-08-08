-- Имя контакта и город (contact_name, country) из таблицы customers
SELECT contact_name, country
FROM customers

-- Идентификатор заказа и разница между датами формирования (order_date) заказа и его отгрузкой (shipped_date) из таблицы orders
SELECT order_id, shipped_date - order_date
FROM orders

-- Все города без повторений, в которых зарегистрированы заказчики (customers)
SELECT DISTINCT city
FROM customers

-- Количество заказов (таблица orders)
SELECT count(*)
FROM orders

-- Количество стран, в которые отгружался товар (таблица orders, колонка ship_country)
SELECT count(distinct ship_country)
FROM orders
