"""
This file is used to connect to the database.
"""

import os
import psycopg2

Db = {
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT'),
    'database': os.environ.get('DB_NAME'),
    'user': os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
}

connection = psycopg2.connect(
    dbname=Db['database'],
    user=Db['user'],
    password=Db['password'],
    host=Db['host'],
    port=Db['port']
)
