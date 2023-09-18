-- Напишите запросы, которые выводят следующую информацию:
-- 1. "имя контакта" и "город" (contact_name, city) из таблицы customers (только эти две колонки)
""" Ввыводит колонки contact_name, city таблицы customers. """
SELECT contact_name, city
FROM customers;

-- 2. идентификатор заказа и разницу между датами формирования (order_date) заказа и его отгрузкой (shipped_date) из таблицы orders
""" выводит колонки order_id, date_difference (считаем разницу (order_date - shipped_date) и даем название колонке) таблицы orders. """
SELECT order_id, order_date - shipped_date AS date_difference
FROM orders;


-- 3. все города без повторов, в которых зарегистрированы заказчики (customers)
""" выводит уникальные(без повторений) значения колонки city таблицы customers. """
SELECT DISTINCT city
FROM customers;


-- 4. количество заказов (таблица orders)
""" выводит общее количество строк колонни number_orders таблицы orders. """
SELECT COUNT(*) AS number_orders
FROM orders;


-- 5. количество стран, в которые отгружался товар (таблица orders, колонка ship_country)
""" выводит количество уникальных строк колокни ship_country - даем название number_countries таблицы orders. """
SELECT COUNT(DISTINCT ship_country) AS number_countries
FROM orders;