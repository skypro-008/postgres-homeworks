-- Напишите запросы, которые выводят следующую информацию:
-- 1. заказы, доставленные в страны France, Germany, Spain (таблица orders, колонка ship_country)
""" выводит все колонки таблицы orders только с указанными городами колонки ship_country. """
SELECT *
FROM orders
WHERE ship_country IN ('France', 'Germany', 'Spain');

-- 2. уникальные страны и города, куда отправлялись заказы, отсортировать по странам и городам (таблица orders, колонки ship_country, ship_city)
""" выводит уникальные строки колонок ship_country, ship_city с сортировкой по алфавиту колонок ship_country, ship_city таблицы orders. """
SELECT
DISTINCT ship_country, ship_city
FROM orders
ORDER BY ship_country, ship_city;

-- 3. сколько дней в среднем уходит на доставку товара в Германию (таблица orders, колонки order_date, shipped_date, ship_country)
""" выводит среднее значение разницы колонок (shipped_date - order_date) в колонке с названием delivery_goods, где ship_country выводит только определенную страну, таблицы orders. """
SELECT
AVG(shipped_date - order_date) AS delivery_goods
FROM orders
WHERE ship_country = 'Germany';


-- 4. минимальную и максимальную цену среди продуктов, не снятых с продажи (таблица products, колонки unit_price, discontinued не равно 1)
""" выводит максимальное значение - название max_price, минимальное значение - название min_price, где discontinued != 1(не снят с продажи), таблицы products."""
SELECT
MAX(unit_price) AS max_price,
MIN(unit_price) AS min_price
FROM products
WHERE discontinued <> 1;

-- 5. минимальную и максимальную цену среди продуктов, не снятых с продажи и которых имеется не меньше 20 (таблица products, колонки unit_price, units_in_stock, discontinued не равно 1)
""" выводит максимальное значение - название max_price, минимальное значение - название min_price, где discontinued != 1(не снят с продажи) и units_in_stock >= 20(количество не меньше 20), таблицы products."""
SELECT
MAX(unit_price) AS max_price,
MIN(unit_price) AS min_price
FROM products
WHERE discontinued <> 1 AND units_in_stock >= 20;
