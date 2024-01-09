"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    host="localhost",
    database="north",
    user="postgres",
    password="2182"
)

cur = conn.cursor()

employees_data = [
    (1, 'Nancy', 'Davolio', 'Sales Representative', '1948-12-08', 'Education includes a BA in psychology from '
                                                                  'Colorado State University in 1970. She also '
                                                                  'completed The Art of the Cold Call. Nancy is a '
                                                                  'member of Toastmasters International.'),
    (2, 'Andrew', 'Fuller', 'Vice President, Sales', '1952-02-19', 'Andrew received his BTS commercial in 1974 and a '
                                                                   'Ph.D. in international marketing from the '
                                                                   'University of Dallas in 1981. He is fluent in '
                                                                   'French and Italian and reads German. He joined '
                                                                   'the company as a sales representative, '
                                                                   'was promoted to sales manager in January 1992 and '
                                                                   'to vice president of sales in March 1993. Andrew '
                                                                   'is a member of the Sales Management Roundtable, '
                                                                   'the Seattle Chamber of Commerce, and the Pacific '
                                                                   'Rim Importers Association.'),
]

insert_query = sql.SQL(
    "INSERT INTO employees (employee_id, first_name, last_name, title, birth_date, notes) VALUES {}"
     ).format(
    sql.SQL(',').join(map(sql.Literal, employees_data))
)

cur.execute(insert_query)

customers_data = [
    ('ALFKI', 'Alfreds Futterkiste', 'Maria Anders'),
    ('ANATR', 'Ana Trujillo Emparedados y helados', 'Ana Trujillo'),
]

insert_query = sql.SQL("INSERT INTO customers (customer_id, company_name, contact_name) VALUES {}").format(
    sql.SQL(',').join(map(sql.Literal, customers_data))
)

cur.execute(insert_query)

orders_data = [
    (10248, 'VINET', 5, '1996-07-04', 'Reims'),
    (10249, 'TOMSP', 6, '1996-07-05', 'Münster'),
]

insert_query = sql.SQL(
    "INSERT INTO orders (order_id, customer_id, employee_id, order_date, ship_city) VALUES {}"
     ).format(
    sql.SQL(',').join(map(sql.Literal, orders_data))
)

cur.execute(insert_query)

conn.commit()
cur.close()
conn.close()
