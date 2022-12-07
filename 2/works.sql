/*CREATE DATABASE db_person
    WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    CONNECTION LIMIT = -1
    IS_TEMPLATE = False;
    */


/* 1 Создать таблицу с основной информацией о сотрудниках: ФИО, дата рождения, дата начала работы, должность, уровень сотрудника (jun, middle, senior, lead), уровень зарплаты, идентификатор отдела, наличие/отсутствие прав(True/False). При этом в таблице обязательно должен быть уникальный номер для каждого сотрудника. */
CREATE TABLE public.person
(
    id integer NOT NULL,
    fio character,
    birthdate date,
    start_work date,
    "position" character,
    level character,
    salary bigint,
    id_department integer,
    license boolean,
    PRIMARY KEY (id)
);
ALTER TABLE public.person
    ALTER COLUMN fio TYPE character(60) COLLATE pg_catalog."default";

ALTER TABLE public.person
    ALTER COLUMN position TYPE character(60) COLLATE pg_catalog."default";

ALTER TABLE public.person
    ALTER COLUMN level TYPE character(60) COLLATE pg_catalog."default";
ALTER TABLE IF EXISTS public.person
    ADD CONSTRAINT key_dep FOREIGN KEY (id_department)
    REFERENCES public.department (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

/*2. Для будущих отчетов аналитики попросили вас создать еще одну таблицу с информацией по отделам – в таблице должен быть идентификатор для каждого отдела, название отдела (например. Бухгалтерский или IT отдел), ФИО руководителя и количество сотрудников.
*/
CREATE TABLE public.department
(
    id integer NOT NULL,
    name character(100),
    fio character(100),
    count_people integer,
    PRIMARY KEY (id)
);
ALTER TABLE IF EXISTS public.department
    ADD COLUMN id_user integer;
ALTER TABLE IF EXISTS public.department
    ADD FOREIGN KEY (id_user)
    REFERENCES public.person (id) MATCH SIMPLE
    ON UPDATE NO ACTION
    ON DELETE NO ACTION
    NOT VALID;

 /*  3. На кону конец года и необходимо выплачивать сотрудникам премию. Премия будет выплачиваться по совокупным оценкам, которые сотрудники получают в каждом квартале года. Создайте таблицу, в которой для каждого сотрудника будут его оценки за каждый квартал. Диапазон оценок от A – самая высокая, до E – самая низкая.
 */

CREATE TABLE public.grade
(
    id integer NOT NULL,
    id_user integer,
    grade character(1),
    PRIMARY KEY (id_user),
    FOREIGN KEY (id_user)
        REFERENCES public.person (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
);

/*
Уникальный номер сотрудника, его ФИО и стаж работы – для всех сотрудников компании
*/
 
 
select id, fio, date_part('year', now()) - date_part('year', start_work) year_work from person;

/*
Уникальный номер сотрудника, его ФИО и стаж работы – только первых 3-х сотрудников
*/
select id, fio, date_part('year', now()) - date_part('year', start_work) year_work from person limit 3;

/*
Уникальный номер сотрудников - водителей
*/
select id from person where license = true;


/*
Выведите номера сотрудников, которые хотя бы за 1 квартал получили оценку D или E
*/
select person.id from person left join grade on person.id=id_user where grade in ('D','E');

/*
Выведите самую высокую зарплату в компании. 
*/
select max(salary) from person ;