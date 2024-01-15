-- SQL-команды для создания таблиц
CREATE TABLE employees
(
    employee_id int PRIMARY KEY,
    first_name varchar(100) NOT NULL,
	last_name varchar(100) NOT NULL,
	title varchar(100) NOT NULL,
	birth_date varchar(100) NOT NULL,
	notes varchar(500) NOT NULL
);

CREATE TABLE customers
(
    customer_id varchar(10) PRIMARY KEY,
    company_name varchar(100) NOT NULL,
	contact_name varchar(100) NOT NULL
);

CREATE TABLE orders
(
    order_id int PRIMARY KEY,
    customer_id varchar(10) NOT NULL REFERENCES customers(customer_id),
	employee_id int NOT NULL REFERENCES employees(employee_id),
	order_date varchar(100) NOT NULL,
	ship_city varchar(100) NOT NULL
)

ALTER TABLE employees
ALTER COLUMN employee_id TYPE INT,
ALTER COLUMN birth_date TYPE VARCHAR(100),
ALTER COLUMN notes TYPE VARCHAR(500);

ALTER TABLE customers
ALTER COLUMN customer_id TYPE VARCHAR(10);

ALTER TABLE orders
ALTER COLUMN order_id TYPE INT,
ALTER COLUMN customer_id TYPE VARCHAR(10),
ALTER COLUMN employee_id TYPE INT,
ALTER COLUMN order_date TYPE VARCHAR(100),
ALTER COLUMN ship_city TYPE VARCHAR(100)
