-- Напишите запросы, которые выводят следующую информацию:
-- 1. заказы, отправленные в города, заканчивающиеся на 'burg'. Вывести без повторений две колонки (город, страна) (см. таблица orders, колонки ship_city, ship_country)
SELECT DISTINCT ship_city, ship_country
FROM public.orders
WHERE ship_city LIKE '%burg'

-- 2. из таблицы orders идентификатор заказа, идентификатор заказчика, вес и страну отгрузки. Заказ отгружен в страны, начинающиеся на 'P'. Результат отсортирован по весу (по убыванию). Вывести первые 10 записей.
SELECT order_id, customer_id, freight, ship_country
FROM public.orders
WHERE ship_country LIKE 'P%'
ORDER BY freight DESC
LIMIT 10

-- 3. фамилию, имя и телефон сотрудников, у которых в данных отсутствует регион (см таблицу employees)
SELECT last_name, first_name, home_phone
FROM public.employees
WHERE region IS null

-- 4. количество поставщиков (suppliers) в каждой из стран. Результат отсортировать по убыванию количества поставщиков в стране
SELECT suppliers.country, count(suppliers.supplier_id)
FROM public.suppliers
GROUP BY suppliers.country
ORDER BY count(suppliers.supplier_id) DESC

-- 5. суммарный вес заказов (в которых известен регион) по странам, но вывести только те результаты, где суммарный вес на страну больше 2750. Отсортировать по убыванию суммарного веса (см таблицу orders, колонки ship_region, ship_country, freight)
SELECT SUM(orders.freight)
FROM public.orders
WHERE (orders.ship_region is NULL) = false
GROUP BY orders.ship_country
HAVING SUM(orders.freight) > 2750

-- 6. страны, в которых зарегистрированы и заказчики (customers) и поставщики (suppliers) и работники (employees).
SELECT suppliers.country
FROM public.suppliers as suppliers JOIN public.customers as customers ON suppliers.country=customers.country
EXCEPT
SELECT employees.country
FROM public.employees

-- 7. страны, в которых зарегистрированы и заказчики (customers) и поставщики (suppliers), но не зарегистрированы работники (employees).
SELECT suppliers.country
FROM public.suppliers as suppliers JOIN public.customers as customers ON suppliers.country=customers.country
INTERSECT
SELECT employees.country
FROM public.employees