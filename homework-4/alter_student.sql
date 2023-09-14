-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
(
    student_id serial PRIMARY KEY,
    first_name varchar,
	last_name varchar,
	birthday date,
    phone varchar
);

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE ONLY student
ADD COLUMN middle_name varchar;

-- 3. Удалить колонку middle_name
ALTER TABLE ONLY student
DROP COLUMN middle_name;


-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE ONLY student
RENAME COLUMN birthday TO birth_date;

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE ONLY student
ALTER COLUMN phone SET DATA TYPE varchar(32);

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student (first_name, last_name, birth_date, phone)
VALUES ('Иванова', 'Алена', '2000-10-01', '+7 911-926-50-06');
INSERT INTO student (first_name, last_name, birth_date, phone)
VALUES ('Кузнецов', 'Алексей', '1987-05-11', '+7 911-439-45-67');
INSERT INTO student (first_name, last_name, birth_date, phone)
VALUES ('Острецов', 'Юрий', '1995-06-30', '+7 924-060-80-40');

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE ONLY student RESTART IDENTITY;