-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
CREATE TABLE student
(
	student_id SERIAL NOT NULL,
	first_name VARCHAR(50) NOT NULL,
	last_name VARCHAR(50) NOT NULL,
	birthday DATE NOT NULL,
	phone VARCHAR(50)
);

-- 2. Добавить в таблицу student колонку middle_name varchar
ALTER TABLE student ADD COLUMN middle_name VARCHAR(50)

-- 3. Удалить колонку middle_name
ALTER TABLE student DROP COLUMN middle_name

-- 4. Переименовать колонку birthday в birth_date
ALTER TABLE student RENAME COLUMN birthday TO birth_date

-- 5. Изменить тип данных колонки phone на varchar(32)
ALTER TABLE student ALTER COLUMN phone SET DATA TYPE VARCHAR(32)

-- 6. Вставить три любых записи с автогенерацией идентификатора
INSERT INTO student
(
	first_name, last_name, birth_date, phone
)
VALUES('Alex', 'Kean', '2000-01-01', '+7778')

INSERT INTO student
(
	first_name, last_name, birth_date, phone
)
VALUES('Helen', 'Trix', '2000-05-06', '+7774')

INSERT INTO student
(
	first_name, last_name, birth_date, phone
)
VALUES('Joe', 'Bex', '2000-04-02', '+7773')

-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
TRUNCATE TABLE student