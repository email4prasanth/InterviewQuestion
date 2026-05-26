# SQL Learning Roadmap Using MySQL Workbench

Start in this order:

1. Create Database
2. Create Tables
3. Insert Data
4. Select Queries
5. Filtering
6. Sorting
7. Joins
8. Aggregate Functions
9. Group By
10. Subqueries
11. Window Functions
12. Views
13. Indexes
14. Procedures
15. Interview Queries

---

# 1. Create Database

```sql
CREATE DATABASE company_db;
```

Use database:

```sql
USE company_db;
```

---

# 2. Create Tables

## Departments Table

```sql
CREATE TABLE departments (
    department_id INT PRIMARY KEY AUTO_INCREMENT,
    department_name VARCHAR(100)
);
```

## Employees Table

```sql
CREATE TABLE employees (
    employee_id INT PRIMARY KEY AUTO_INCREMENT,
    employee_name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    salary DECIMAL(10,2),
    department_id INT,
    joining_date DATE,

    FOREIGN KEY (department_id)
    REFERENCES departments(department_id)
);
```

---

# 3. Insert Data

## Departments

```sql
INSERT INTO departments(department_name)
VALUES
('HR'),
('IT'),
('Finance'),
('Sales');
```

## Employees

```sql
INSERT INTO employees
(employee_name, age, gender, salary, department_id, joining_date)
VALUES
('Prasanth', 25, 'Male', 50000, 2, '2024-01-10'),
('Ravi', 28, 'Male', 60000, 2, '2023-03-15'),
('Sneha', 30, 'Female', 70000, 1, '2022-06-20'),
('Kiran', 27, 'Male', 55000, 3, '2021-11-11'),
('Divya', 26, 'Female', 65000, 4, '2020-09-09');
```

---

# 4. SELECT Queries

## Get all records

```sql
SELECT * FROM employees;
```

## Specific columns

```sql
SELECT employee_name, salary
FROM employees;
```

---

# 5. WHERE Clause

## Salary greater than 55000

```sql
SELECT *
FROM employees
WHERE salary > 55000;
```

## Multiple conditions

```sql
SELECT *
FROM employees
WHERE age > 25
AND salary > 50000;
```

## OR condition

```sql
SELECT *
FROM employees
WHERE department_id = 1
OR department_id = 2;
```

---

# 6. ORDER BY

## Ascending

```sql
SELECT *
FROM employees
ORDER BY salary ASC;
```

## Descending

```sql
SELECT *
FROM employees
ORDER BY salary DESC;
```

---

# 7. LIMIT

```sql
SELECT *
FROM employees
LIMIT 3;
```

---

# 8. DISTINCT

```sql
SELECT DISTINCT gender
FROM employees;
```

---

# 9. Aggregate Functions

## COUNT

```sql
SELECT COUNT(*) AS total_employees
FROM employees;
```

## MAX salary

```sql
SELECT MAX(salary) AS highest_salary
FROM employees;
```

## MIN salary

```sql
SELECT MIN(salary) AS lowest_salary
FROM employees;
```

## AVG salary

```sql
SELECT AVG(salary) AS average_salary
FROM employees;
```

## SUM salary

```sql
SELECT SUM(salary) AS total_salary
FROM employees;
```

---

# 10. GROUP BY

## Department wise employee count

```sql
SELECT department_id,
       COUNT(*) AS total_employees
FROM employees
GROUP BY department_id;
```

## Department wise average salary

```sql
SELECT department_id,
       AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id;
```

---

# 11. HAVING

```sql
SELECT department_id,
       AVG(salary) AS avg_salary
FROM employees
GROUP BY department_id
HAVING AVG(salary) > 55000;
```

---

# 12. INNER JOIN

```sql
SELECT e.employee_name,
       e.salary,
       d.department_name
FROM employees e
INNER JOIN departments d
ON e.department_id = d.department_id;
```

---

# 13. LEFT JOIN

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e
LEFT JOIN departments d
ON e.department_id = d.department_id;
```

---

# 14. RIGHT JOIN

```sql
SELECT e.employee_name,
       d.department_name
FROM employees e
RIGHT JOIN departments d
ON e.department_id = d.department_id;
```

---

# 15. SELF JOIN

```sql
CREATE TABLE managers (
    emp_id INT,
    emp_name VARCHAR(100),
    manager_id INT
);
```

Insert data:

```sql
INSERT INTO managers
VALUES
(1, 'A', NULL),
(2, 'B', 1),
(3, 'C', 1),
(4, 'D', 2);
```

Query:

```sql
SELECT e.emp_name AS employee,
       m.emp_name AS manager
FROM managers e
LEFT JOIN managers m
ON e.manager_id = m.emp_id;
```

---

# 16. Subquery

## Employees earning more than average salary

```sql
SELECT employee_name, salary
FROM employees
WHERE salary >
(
    SELECT AVG(salary)
    FROM employees
);
```

---

# 17. EXISTS

```sql
SELECT department_name
FROM departments d
WHERE EXISTS
(
    SELECT *
    FROM employees e
    WHERE e.department_id = d.department_id
);
```

---

# 18. IN Operator

```sql
SELECT *
FROM employees
WHERE department_id IN (1,2);
```

---

# 19. BETWEEN

```sql
SELECT *
FROM employees
WHERE salary BETWEEN 50000 AND 65000;
```

---

# 20. LIKE

## Starts with P

```sql
SELECT *
FROM employees
WHERE employee_name LIKE 'P%';
```

## Ends with a

```sql
SELECT *
FROM employees
WHERE employee_name LIKE '%a';
```

---

# 21. UPDATE

```sql
UPDATE employees
SET salary = 80000
WHERE employee_id = 1;
```

---

# 22. DELETE

```sql
DELETE FROM employees
WHERE employee_id = 5;
```

---

# 23. ALTER TABLE

## Add column

```sql
ALTER TABLE employees
ADD email VARCHAR(100);
```

## Modify column

```sql
ALTER TABLE employees
MODIFY salary DECIMAL(12,2);
```

---

# 24. DROP TABLE

```sql
DROP TABLE managers;
```

---

# 25. TRUNCATE TABLE

```sql
TRUNCATE TABLE employees;
```

---

# 26. Create View

```sql
CREATE VIEW employee_view AS
SELECT employee_name, salary
FROM employees;
```

Use view:

```sql
SELECT * FROM employee_view;
```

---

# 27. Index

```sql
CREATE INDEX idx_employee_name
ON employees(employee_name);
```

---

# 28. Stored Procedure

```sql
DELIMITER //

CREATE PROCEDURE GetEmployees()
BEGIN
    SELECT * FROM employees;
END //

DELIMITER ;
```

Call procedure:

```sql
CALL GetEmployees();
```

---

# 29. Window Functions

## Rank employees by salary

```sql
SELECT employee_name,
       salary,
       RANK() OVER (ORDER BY salary DESC) AS salary_rank
FROM employees;
```

## Row Number

```sql
SELECT employee_name,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num
FROM employees;
```

---

# 30. Interview Queries

## Find 2nd Highest Salary

```sql
SELECT MAX(salary) AS second_highest
FROM employees
WHERE salary <
(
    SELECT MAX(salary)
    FROM employees
);
```

---

## Find Duplicate Records

```sql
CREATE TABLE users (
    id INT,
    email VARCHAR(100)
);
```

Insert:

```sql
INSERT INTO users
VALUES
(1,'a@gmail.com'),
(2,'b@gmail.com'),
(3,'a@gmail.com');
```

Find duplicates:

```sql
SELECT email,
       COUNT(*) AS total
FROM users
GROUP BY email
HAVING COUNT(*) > 1;
```

---

## Delete Duplicate Records

```sql
DELETE u1
FROM users u1
JOIN users u2
ON u1.email = u2.email
AND u1.id > u2.id;
```

---

## Find Employees Joined in Last 30 Days

```sql
SELECT *
FROM employees
WHERE joining_date >= CURDATE() - INTERVAL 30 DAY;
```

---

## Highest Salary in Each Department

```sql
SELECT department_id,
       MAX(salary) AS highest_salary
FROM employees
GROUP BY department_id;
```

---

# Important Interview Concepts

## Primary Key
Uniquely identifies each row.

## Foreign Key
Creates relationship between tables.

## Normalization
Reduces data redundancy.

## Index
Improves query performance.

## ACID Properties

- Atomicity
- Consistency
- Isolation
- Durability

---

# Best Practice for Learning

Practice daily:
1. Create table
2. Insert data
3. Write queries
4. Modify queries
5. Solve interview questions

Focus heavily on:
- JOINS
- GROUP BY
- SUBQUERIES
- WINDOW FUNCTIONS

These are most asked in interviews.