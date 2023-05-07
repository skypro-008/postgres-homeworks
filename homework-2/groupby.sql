-- Напишите запросы, которые выводят следующую информацию:
-- 1. заказы, отправленные в города, заканчивающиеся на 'burg'. Вывести без повторений две колонки (город, страна) (см. таблица orders, колонки ship_city, ship_country)
SELECT Distinct ship_city, ship_country
FROM orders
Where ship_city like ('%burg')


-- 2. из таблицы orders идентификатор заказа, идентификатор заказчика, вес и страну отгрузки. Заказ отгружен в страны, начинающиеся на 'P'. Результат отсортирован по весу (по убыванию). Вывести первые 10 записей.
Select order_id, customer_id, freight, ship_country
FROM orders
Where ship_country like ('P%')
Order by (freight) Desc
limit 10

-- 3. фамилию и телефон сотрудников, у которых в данных отсутствует регион (см таблицу employees)
Select last_name, home_phone
FROM employees
Where region is Null

-- 4. количество поставщиков (suppliers) в каждой из стран. Результат отсортировать по убыванию количества поставщиков в стране
Select country, Count(*)
FROM suppliers
Group by country
order by Count(country) DESC

-- 5. суммарный вес заказов (в которых известен регион) по странам, но вывести только те результаты, где суммарный вес на страну больше 2750. Отсортировать по убыванию суммарного веса (см таблицу orders, колонки ship_region, ship_country, freight)
Select  ship_country, Sum(freight)
FROM orders
Where ship_region IS Not Null
Group by ship_country
Having Sum(freight) > 2750
Order by Sum(freight) DESC

-- 6. страны, в которых зарегистрированы и заказчики (customers) и поставщики (suppliers) и работники (employees).

Select  country From customers
Intersect
Select country From suppliers
Intersect
Select country From employees
-- 7. страны, в которых зарегистрированы и заказчики (customers) и поставщики (suppliers), но не зарегистрированы работники (employees).
Select  country From customers
Intersect
Select country From suppliers
EXCEPT
Select country From employees