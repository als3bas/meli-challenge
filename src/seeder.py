"""
Seeder for meli challenge
"""
from faker import Faker
import chile_rut
import db_connection
fake = Faker('es_ES')

CUSTOMER_QTY=40


def customer_seeder(cursor):
    customer_query = """
      INSERT INTO customer (cust_name, fiscal_id, email, address) VALUES (%s, %s, %s, %s)
      """
    customer_data = []
    for _ in range(CUSTOMER_QTY - 1):
        customer_data.append((
            fake.name(),
            chile_rut.random_rut(),
            fake.email(),
            fake.address()
        ))
    cursor.executemany(customer_query, customer_data)


def pos_seeder(cursor):
    pos_query = """
    INSERT INTO pos (serial, model, app_ver, cust_id, active) VALUES (%s, %s, %s, %s, %s)
    """
    pos_data = []
    for _ in range(30):
        pos_data.append((
            fake.unique.ean(length=13),
            fake.unique.sbn9(separator='-'),
            fake.random_int(min=1, max=5),
            fake.random_int(min=1, max=CUSTOMER_QTY - 1),
            fake.boolean(chance_of_getting_true=80)
        ))
    cursor.executemany(pos_query, pos_data)


def transaction_seeder(cursor):
    transaction_query = """
    INSERT INTO transactions (cust_id, pmeth_id, cod_aut, created_at, amount, status, pos_id) VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    transaction_data = []
    for _ in range(400):
        transaction_data.append((
            fake.random_int(min=1, max=CUSTOMER_QTY - 1),
            fake.random_element(elements=(30,31,13)),
            fake.unique.ean(length=8),
            fake.date_time_between(start_date='-1y', end_date='now'),
            fake.random_int(min=1000, max=100000),
            fake.boolean(chance_of_getting_true=80),
            fake.random_int(min=1, max=30)
        ))
    cursor.executemany(transaction_query, transaction_data)


def main():
    connection = db_connection.connection
    cur = connection.cursor()

    # Seeders
    try:
        customer_seeder(cur)
        connection.commit()
        pos_seeder(cur)
        connection.commit()
        transaction_seeder(cur)
        connection.commit()
    except Exception as error:
        print(error)
        connection.rollback()
    finally:
        connection.close()


main()
