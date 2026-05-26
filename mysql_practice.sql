-- Create batabase
CREATE database company_db;
USE company_db;

-- Create Tables
create table departments (
	department_id INT primary key auto_increment,
    department_name varchar(100)
);
-- Insert Data in department
INSERT INTO departments (department_name)
VALUES
('HR'),
('IT'),
('Finance'),
('Sales');

SELECT * FROM departments;
-- Create employees table
create table employees (
	employee_id Int primary key	auto_increment,
    emlpoyee_name varchar(100),
    employee_age int,
    gender varchar(10),
    salary int,
    department_id int,
    joining_date date,
    
    foreign key (department_id )
    references departments(department_id)
);	
-- Insert data in table
Insert into employees (emlpoyee_name, employee_age, gender, salary, department_id, joining_date)
values
('Prasanth', 34, 'Male', 50000, 2, '2024-01-10'),
('Ravi', 28, 'Male', 60000, 2, '2023-03-15'),
('Sneha', 30, 'Female', 70000, 1, '2022-06-20'),
('Kiran', 27, 'Male', 55000, 3, '2021-11-11'),
('Divya', 26, 'Female', 65000, 4, '2020-09-09');

select * from employees;
select employee_age, salary from employees;
-- where clause
select * from employees where salary >60000;
-- Multiple conditions
select * from employees where employee_age>28 and salary >60000;
-- OR condition
select * from employees where department_id=1 or department_id=2;
-- asceding order
select * from employees order by salary ASC;
-- descendin order
select * from employees order by employee_age desc;
-- LIMIT
select * from employees limit 3;
-- distint
select distinct gender from employees;
-- aggreate function
select count(*) as total_employees from employees; 
-- MAX salary
select max(salary) as highest_salary from employees;
-- min salary
select min(salary) as lowest_salary from employees;
-- group by dept wise
select department_id, count(*) as total_employees from employees group by department_id; 
-- Department wise average salary
select department_id, avg(salary) as avg_salary from employees group by	department_id;