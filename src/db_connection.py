"""
This file contains the connection to the database
and the query to get the transactions
"""

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

dbname = os.environ.get('DB_NAME')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')

def create_connection() -> psycopg2.extensions.connection:
    '''
    Create a connection to the database
    Returns:
        connection: Connection to the database
    '''
    connection = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )
    return connection

def get_transactions_query(month: int, status:bool = True) -> str:
    '''
    Get the query to get the transactions
    Returns:
        query: Query to get the transactions
    '''
    return f"""
        SELECT c.fiscal_id AS fiscal_id,
               c.cust_name AS name,
               t.created_at AS timestamp,
               t.id AS id_tx,
               t.pmeth_id AS payment_method,
               t.amount AS amount,
               t.cod_aut AS cod_aut,
               p.serial AS serial_pos
        FROM transactions t 
        LEFT JOIN customer c ON t.cust_id = c.id
        LEFT JOIN pos p ON t.pos_id = p.id
        WHERE EXTRACT(MONTH FROM t.created_at) = {month}
            AND t.status = {status}
    """
