-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
SELECT customers.company_name, CONCAT(first_name, ' ', last_name) AS employee
FROM orders
INNER JOIN customers USING(customer_id)
INNER JOIN employees USING(employee_id)
WHERE customers.city IN ('London') AND employees.city IN ('London') AND orders.ship_via IN (SELECT shipper_id FROM shippers where shippers.shipper_id=2)


-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.
SELECT products.product_name, products.units_in_stock, suppliers.contact_name, suppliers.phone
FROM products
INNER JOIN suppliers USING(supplier_id)
INNER JOIN categories USING(category_id)
WHERE products.discontinued <> 1 AND products.units_in_stock < 25 AND (categories.category_id=4 OR categories.category_id=2)
ORDER BY products.units_in_stock

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
-- 3 способа - В чем разница между IN и EXISTS?
SELECT company_name
FROM customers
WHERE NOT EXISTS(SELECT DISTINCT customer_id FROM orders WHERE customers.customer_id=orders.customer_id)


SELECT company_name
FROM customers
WHERE customer_id NOT IN (SELECT DISTINCT customer_id FROM orders)


Select Customers.company_name from customers
except
Select customers.company_name From orders join customers on orders.customer_id = customers.customer_id


-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.
SELECT product_name
FROM products
WHERE EXISTS (SELECT * FROM order_details WHERE products.product_id = order_details.product_id and order_details.quantity=10)