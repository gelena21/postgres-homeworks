"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

FILE_CUSTOMERS_DATA = 'north_data/customers_data.csv'
FILE_EMPLOYEES_DATA = 'north_data/employees_data.csv'
FILE_ORDERS_DATA = 'north_data/orders_data.csv'


def insert_data_to_sql(filename, tablename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            data = csv.DictReader(file)
            with psycopg2.connect(host="localhost", database="north", user="postgres", password="2182") as conn:
                with conn.cursor() as curs:
                    for row in data:
                        row_data = []
                        values_designation = []
                        for key in list(row.keys()):
                            row_data.append(row[key])
                            values_designation.append('%s')
                        curs.execute(f"INSERT INTO {tablename} VALUES ({', '.join(values_designation)})",
                                     tuple(row_data))
                        row_data.clear()
                        values_designation.clear()
    finally:
        conn.close()
