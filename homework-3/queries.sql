-- Напишите запросы, которые выводят следующую информацию:
-- 1. Название компании заказчика (company_name из табл. customers) и ФИО сотрудника, работающего над заказом этой компании (см таблицу employees),
-- когда и заказчик и сотрудник зарегистрированы в городе London, а доставку заказа ведет компания United Package (company_name в табл shippers)
SELECT customers.company_name AS customer_company_name,
       CONCAT(employees.first_name, ' ', employees.last_name) AS employee_full_name
FROM customers
JOIN orders ON customers.customer_id = orders.customer_id
JOIN employees ON orders.employee_id = employees.employee_id
WHERE customers.city = 'London' AND employees.city = 'London' AND orders.ship_via = (
    SELECT shipper_id
    FROM shippers
    WHERE company_name = 'United Package'
);

-- 2. Наименование продукта, количество товара (product_name и units_in_stock в табл products),
-- имя поставщика и его телефон (contact_name и phone в табл suppliers) для таких продуктов,
-- которые не сняты с продажи (поле discontinued) и которых меньше 25 и которые в категориях Dairy Products и Condiments.
-- Отсортировать результат по возрастанию количества оставшегося товара.
SELECT p.product_name, p.units_in_stock, s.contact_name, s.phone
FROM products p
JOIN categories c ON p.category_id = c.category_id
JOIN suppliers s ON p.supplier_id = s.supplier_id
WHERE p.discontinued = 0
  AND p.units_in_stock < 25
  AND c.category_name IN ('Dairy Products', 'Condiments')
ORDER BY p.units_in_stock ASC;

-- 3. Список компаний заказчиков (company_name из табл customers), не сделавших ни одного заказа
SELECT company_name
FROM customers
LEFT JOIN orders ON customers.customer_id = orders.customer_id
WHERE order_id IS NULL;


-- 4. уникальные названия продуктов, которых заказано ровно 10 единиц (количество заказанных единиц см в колонке quantity табл order_details)
-- Этот запрос написать именно с использованием подзапроса.
SELECT product_name
FROM products
WHERE product_id = ANY(
   SELECT product_id
   FROM order_details
    WHERE quantity = 10
);
