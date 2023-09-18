-- Напишите запросы, которые выводят следующую информацию:
-- 1. заказы, отправленные в города, заканчивающиеся на 'burg'. Вывести без повторений две колонки (город, страна) (см. таблица orders, колонки ship_city, ship_country)
""" выводит уникальные колонки ship_city, ship_country, где города колонки ship_city заканчиваются на 'burg', таблицы orders. """
SELECT
DISTINCT ship_city, ship_country
FROM orders
WHERE ship_city LIKE '%burg';

-- 2. из таблицы orders идентификатор заказа, идентификатор заказчика, вес и страну отгрузки. Заказ отгружен в страны, начинающиеся на 'P'. Результат отсортирован по весу (по убыванию). Вывести первые 10 записей.
""" выводит 10 колонок order_id, customer_id, freight, ship_country, где в колонке ship_country выводит только страны на 'P', а в колонке freight сортировка(по весу)(по убыванию),таблицы orders. """
SELECT order_id, customer_id, freight, ship_country
FROM orders
WHERE ship_country LIKE 'P%'
ORDER BY freight DESC
LIMIT 10;

-- 3. фамилию, имя и телефон сотрудников, у которых в данных отсутствует регион (см таблицу employees)
""" выводит колонки last_name, first_name, home_phone, где пустые строки колонки region, таблицы employees. """
SELECT last_name, first_name, home_phone
FROM employees
WHERE region IS NULL;

-- 4. количество поставщиков (suppliers) в каждой из стран. Результат отсортировать по убыванию количества поставщиков в стране
""" выводит колонку country и количество поставщиков - название number_suppliers, группируем country и отсортировываем по убыванию number_suppliers, таблицы suppliers. """
SELECT country
COUNT(*) AS number_suppliers
FROM suppliers
GROUP BY country
ORDER BY number_suppliers DESC;

-- 5. суммарный вес заказов (в которых известен регион) по странам, но вывести только те результаты, где суммарный вес на страну больше 2750. Отсортировать по убыванию суммарного веса (см таблицу orders, колонки ship_region, ship_country, freight)
""" выводит ship_country и суммарный вес - название total_freight, где ship_region - известен, сгруппировали по ship_country, дополнительная фильтрация - если суммарный вес > 2750, отсортировали по убыванию, таблицы orders. """
SELECT ship_country,
SUM(freight) AS total_freight
FROM orders
WHERE ship_region IS NOT NULL
GROUP BY ship_country
HAVING SUM(freight) > 2750
ORDER BY total_freight DESC;

-- 6. страны, в которых зарегистрированы и заказчики (customers) и поставщики (suppliers) и работники (employees).
""" выводит только те страны, в которых зарегистрированы customers, suppliers и employees. """
SELECT country FROM customers
WHERE country IN (SELECT country FROM suppliers)
INTERSECT
SELECT country FROM customers
WHERE country IN (SELECT country FROM employees);

-- 7. страны, в которых зарегистрированы и заказчики (customers) и поставщики (suppliers), но не зарегистрированы работники (employees).
""" выводит только те страны, где зарегистрированы customers и suppliers, но не employees. """
SELECT country FROM customers
WHERE country IN (SELECT country FROM suppliers)
EXCEPT
SELECT country FROM customers
WHERE country IN (SELECT country FROM employees);
