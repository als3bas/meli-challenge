"""
This file is used to connect to the database.
"""

import os
import psycopg2

dbname = os.environ.get('DB_NAME')
user = os.environ.get('DB_USER')
password = os.environ.get('DB_PASSWORD')
host = os.environ.get('DB_HOST')
port = os.environ.get('DB_PORT')

connection = psycopg2.connect(
    dbname=dbname,
    user=user,
    password=password,
    host=host,
    port=port
)
