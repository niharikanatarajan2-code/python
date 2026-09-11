CREATE TABLE locations (
    location_id INT PRIMARY KEY,
    city VARCHAR(50),
    country VARCHAR(50)
);

CREATE TABLE job_roles (
    role_id INT PRIMARY KEY,
    role_title VARCHAR(50)
);

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(100),
    location_id INT
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    role_id INT,
    manager_id INT
);

CREATE TABLE department_assignments (
    employee_id INT,
    department_id INT
);

CREATE TABLE projects (
    project_id INT PRIMARY KEY,
    project_name VARCHAR(100),
    budget DECIMAL(12,2),
    status VARCHAR(20)
);

CREATE TABLE project_assignments (
    employee_id INT,
    project_id INT,
    allocation_percentage DECIMAL(5,2)
);

CREATE TABLE salaries (
    employee_id INT PRIMARY KEY,
    base_salary DECIMAL(10,2),
    bonus DECIMAL(10,2)
);

CREATE TABLE performance_reviews (
    employee_id INT,
    review_rating DECIMAL(3,1),
    review_date DATE
);

INSERT INTO locations VALUES (1, 'New York', 'US'), (2, 'London', 'UK'), (3, 'Toronto', 'CA'), (4, 'Berlin', 'DE');
INSERT INTO job_roles VALUES (1, 'Engineer'), (2, 'Manager'), (3, 'Analyst');
INSERT INTO departments VALUES (10, 'Global Tech Support', 1), (20, 'FinTech Dev', 2), (30, 'HR', 3);
INSERT INTO employees VALUES (101, 'Alice', 'Smith', 1, 103), (102, 'Bob', 'Jones', 3, 103), (103, 'Charlie', 'Brown', 2, NULL);
INSERT INTO department_assignments VALUES (101, 10), (102, 20), (103, 10);
INSERT INTO projects VALUES (500, 'Global Infrastructure Sync', 500000.00, 'Active'), (501, 'Local Launch', 50000.00, 'Active');
INSERT INTO project_assignments VALUES (101, 500, 60.00), (102, 501, 40.00), (103, 500, 50.00);
INSERT INTO salaries VALUES (101, 85000.00, 5000.00), (102, 60000.00, 2000.00), (103, 120000.00, 15000.00);
INSERT INTO performance_reviews VALUES (101, 4.5, '2026-01-15'), (102, 3.8, '2026-02-10'), (103, 4.8, '2026-01-20');

SELECT DISTINCT 
    emp.employee_id,
    emp.first_name,
    emp.last_name,
    dept.department_name,
    proj.project_name,
    proj.budget,
    loc.city,
    loc.country,
    mgr.last_name AS manager_name,
    role.role_title,
    sal.base_salary,
    sal.bonus,
    (sal.base_salary + sal.bonus) AS total_compensation,
    rev.review_rating,
    rev.review_date
FROM employees emp
INNER JOIN department_assignments da 
    ON emp.employee_id = da.employee_id
INNER JOIN departments dept 
    ON da.department_id = dept.department_id
INNER JOIN project_assignments pa 
    ON emp.employee_id = pa.employee_id
INNER JOIN projects proj 
    ON pa.project_id = proj.project_id
INNER JOIN locations loc 
    ON dept.location_id = loc.location_id
INNER JOIN job_roles role 
    ON emp.role_id = role.role_id
INNER JOIN salaries sal 
    ON emp.employee_id = sal.employee_id
LEFT JOIN employees mgr 
    ON emp.manager_id = mgr.employee_id
LEFT JOIN performance_reviews rev 
    ON emp.employee_id = rev.employee_id
WHERE (proj.project_name LIKE '%Global%' OR dept.department_name LIKE '%Tech%')
  AND proj.status = 'Active'
  AND loc.country IN ('US', 'UK', 'CA', 'DE')
  AND sal.base_salary >= 75000.00
  AND rev.review_rating >= 4.0
  AND pa.allocation_percentage >= 50.00
ORDER BY 
    loc.country ASC, 
    dept.department_name ASC, 
    total_compensation DESC, 
    emp.last_name ASC;

