-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
-- Выводит company_name - название customer и объединение двух колонок - employee таблицы customers, где берет все с 1 колонки и дополняет 2 по customer_id, employee_id и shipper_id, далее где города заказчика и сотрудника - London, а компания - United Package.
SELECT customers.company_name AS customer,
CONCAT(employees.first_name, ' ', employees.last_name) AS employee
FROM orders
INNER JOIN customers USING(customer_id)
INNER JOIN employees USING(employee_id)
INNER JOIN shippers ON orders.ship_via=shippers.shipper_id
WHERE customers.city = 'London'
AND employees.city = 'London'
AND shippers.company_name = 'United Package';

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.
-- Выводит колонки product_name, units_in_stock, contact_name, phone таблиц products и suppliers, которые соединены общим shipper_id, где discontinued - не сняты с продажи, количество товара не больше 25, а products и categories связаны category_id и выводит только категории Dairy Products и Condiments, отсортированно по возрастанию.
SELECT products.product_name,
products.units_in_stock,
suppliers.contact_name.
suppliers.phone
FROM products
INNER JOIN suppliers USING(shipper_id)
WHERE products.discontinued = 0
AND products.units_in_stock < 25
AND products.category_id IN (SELECT category_id
FROM categories
WHERE categories.category_name IN ('Dairy Products', 'Condiments'))
ORDER BY units_in_stock ASC;

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
-- Выводит company_name таблицы customers, где в таблице orders нет того же customer_id, что и в customers.
SELECT company_name
FROM customers
WHERE customer_id NOT IN(
SELECT customer_id
FROM orders);

-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.
-- Выводит product_name таблицы products, где product_id = product_id таблицы order_details, где количество единиц(quantity) = 10
SELECT DISTINCT product_name
FROM products
WHERE product_id IN(
SELECT product_id FROM order_details
WHERE quantity = 10);



