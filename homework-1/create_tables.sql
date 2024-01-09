-- SQL-команды для создания таблиц
CREATE TABLE employees
(
	employee_id int PRIMARY KEY,
	first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NUll,
	birth_date date,
	notes text
);

SELECT * FROM employees

CREATE TABLE customers
(
	customer_id varchar(50) PRIMARY KEY,
	company_name varchar(50) NOT NULL,
	contact_name varchar(50) NOT null
);

CREATE TABLE orders
(
	order_id int PRIMARY KEY,
	customer_id varchar(50) NOT NULL,
	employee_id int,
	order_date date,
	ship_city varchar(20)
)
