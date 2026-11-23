-- 1. Создать таблицу student с полями student_id serial, first_name varchar, last_name varchar, birthday date, phone varchar
create table student (
    student_id serial primary key,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    birthday DATE,
    phone VARCHAR(20)
);
-- 2. Добавить в таблицу student колонку middle_name varchar
alter table student
add column middle_name varchar(50);
-- 3. Удалить колонку middle_name
alter table student
drop column middle_name;
-- 4. Переименовать колонку birthday в birth_date
alter table student
rename column birthday to birth_date;
-- 5. Изменить тип данных колонки phone на varchar(32)
alter table student
alter column phone type varchar(32);
-- 6. Вставить три любых записи с автогенерацией идентификатора
insert into student (first_name, last_name, birth_date, phone)
values 
    ('Ivan', 'Ivanov', '2000-01-01', '+79001112233'),
    ('Petr', 'Petrov', '2001-02-02', '+79004445566'),
    ('Anna', 'Sidorova', '1999-03-03', '+79007778899');
-- 7. Удалить все данные из таблицы со сбросом идентификатор в исходное состояние
truncate table student restart identity;
