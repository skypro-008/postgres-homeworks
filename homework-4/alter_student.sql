-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar

CREATE TABLE students
(
	student_id SERIAL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthday DATE,
	phone VARCHAR(15)
);

-- 2. Добавить в таблицу student колонку middle_name varchar

ALTER TABLE students ADD COLUMN middle_name varchar(50);

-- 3. Удалить колонку middle_name

ALTER TABLE students DROP COLUMN middle_name

-- 4. Переименовать колонку birthday в birth_date

ALTER TABLE students RENAME birthday TO birth_date

-- 5. Изменить тип данных колонки phone на varchar(32)

ALTER TABLE students ALTER COLUMN phone SET DATA TYPE varchar(32)

-- 6. Вставить три любых записи с автогенерацией идентификатора


INSERT INTO students (first_name, last_name, birthday, phone)  VALUES ('Andrey','Petrov',NULL,NULL)
INSERT INTO students (first_name, last_name, birthday, phone)  VALUES ('Arseny','Avakov',NULL, '79523337420')
INSERT INTO students (first_name, last_name, birthday, phone)  VALUES ('Arseny','Avakov',NULL, '79523337420')



-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние

TRUNCATE TABLE students
