/*
Попробуйте вывести не просто самую высокую зарплату во всей команде, а вывести именно фамилию сотрудника с самой высокой зарплатой.
*/
SELECT fio, salary FROM person WHERE salary=(SELECT MAX(salary) FROM person);

/*
Попробуйте вывести фамилии сотрудников в алфавитном порядке
*/
SELECT fio from person order by fio;

/*
Рассчитайте средний стаж для каждого уровня сотрудников
*/
select level,avg(date_part('year', now()) - date_part('year', start_work)) year_avg from person group by level;

/*
Выведите фамилию сотрудника и название отдела, в котором он работает
*/
SELECT person.fio, department.name from person left join department on department.id=person.id_department;

/*
Выведите название отдела и фамилию сотрудника с самой высокой зарплатой в данном отделе и саму зарплату также.
*/
select fio, max.salary from person 
left join (select id_department,max(salary) salary from person group by id_department)
max on (person.salary=max.salary)  
where max.salary is not null