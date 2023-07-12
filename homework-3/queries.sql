-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
SELECT customers.company_name, CONCAT(employees.first_name, ' ', employees.first_name) FROM orders
Left JOIN
customers
USING(customer_id)
Left JOIN
employees
USING(employee_id)
Left JOIN
shippers
ON ship_via = shipper_id
WHERE customers.city = 'London' AND employees.city = 'London' AND shippers.company_name = 'United Package'


-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.
SELECT product_name, contact_name, phone
FROM products
LEFT JOIN
suppliers
USING(supplier_id)
LEFT JOIN
public.categories
USING(category_id)
WHERE discontinued = 0 AND units_in_stock < 25 AND (category_name = 'Dairy Products' or category_name = 'Condiments')
ORDER BY units_in_stock

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
SELECT company_name FROM customers
WHERE NOT EXISTS (SELECT order_id FROM orders WHERE customers.customer_id = orders.customer_id)

-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.
SELECT DISTINCT(sub.product_name) from
(SELECT product_name FROM order_details JOIN products USING(product_id) WHERE quantity=10 ) AS sub