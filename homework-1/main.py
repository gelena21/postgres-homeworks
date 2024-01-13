"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2
import csv

FILE_CUSTOMERS_DATA = 'north_data/customers_data.csv'
FILE_EMPLOYEES_DATA = 'north_data/employees_data.csv'
FILE_ORDERS_DATA = 'north_data/orders_data.csv'


def insert_datas_to_sql(filename, tablename):
    try:
        with open(filename, 'r', encoding='UTF-8') as file:
            data = csv.DictReader(file)
            with psycopg2.connect(host="localhost", database="north", user="postgres", password="2182") as conn:
                with conn.cursor() as curs:
                    for row in data:
                        customer_id = row['customer_id']
                        if not isinstance(customer_id, int):
                            # Handle invalid customer_id value
                            print(f"Invalid customer_id value: '{customer_id}'")
                            break

                        customer_id_int = int(customer_id)
                        row_data = []
                        values_designation = []
                        for key, value in row.items():
                            if key == "customer_id":
                                customer_id_int = int(customer_id)
                                row_data.append(customer_id_int)
                            else:
                                row_data.append(value)
                            values_designation.append('%s')
                        curs.execute(f"INSERT INTO {tablename} VALUES ({', '.join(values_designation)})",
                                     tuple(row_data))
                        row_data.clear()
                        values_designation.clear()
    except psycopg2.OperationalError as e:
        print(f"Error: {e}")
    finally:
        if conn:
            conn.close()


insert_datas_to_sql(FILE_CUSTOMERS_DATA, 'orders')
insert_datas_to_sql(FILE_EMPLOYEES_DATA, 'employees')
insert_datas_to_sql(FILE_ORDERS_DATA, 'customers')
