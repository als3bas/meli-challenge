"""
Title: Meli challenge.
Author: Álvaro Godoy
Date: 2023-03-28
Email: alvarogodoyg@gmail.com
"""

import csv
import sys
from time import strftime
from db_connection import get_transactions_query, create_connection

try:
    month = sys.argv[1] if len(sys.argv) > 1 and 1 <= int(sys.argv[1]) <= 12 else strftime("%m")
    print(f'I\'m using Month {month or "current month"}')
except (IndexError, ValueError):
    print('Invalid month entered, should be a number between 1 and 12')
    sys.exit(1)

connection = create_connection()
cursor = connection.cursor()

def __main__():
    filename = './files/report_' + month + '.csv'
    sql = get_transactions_query(month, status=True)
    with open(filename, 'w', encoding='utf8') as file:
        writer = csv.writer(file)
        writer.writerow([
            'fiscal_id',
            'name',
            'timestamp',
            'id_tx',
            'payment_method',
            'amount',
            'cod_aut',
            'serial_pos'
        ])
        cursor.execute(sql)
        results = cursor.fetchall()

        for row in results:
            writer.writerow(row)

        print('File created with name > ' + 'report_' + month + '.csv')

    connection.close()


if __name__ == '__main__':
    __main__()
