"""
Title: Meli challenge.
Author: Álvaro Godoy
Date: 2023-03-28
Email: alvarogodoyg@gmail.com
"""

import csv
import sys
from time import strftime
from db_connection import connection as DbConnection

try:
    MONTH = sys.argv[1] if len(sys.argv) > 1 and 1 <= int(sys.argv[1]) <= 12 else strftime("%m")
    print(f'I\'m using Month {MONTH or "current month"}')
except (IndexError, ValueError):
    print('Invalid month entered, should be a number between 1 and 12')
    sys.exit(1)

connection = DbConnection
cursor = connection.cursor()

def __main__():
    sql = f"""
        select
            c.fiscal_id as fiscal_id,
            c.cust_name as name,
            t.created_at as timestamp,
            t.id as id_tx,
            t.pmeth_id as payment_method,
            t.amount as amount,
            t.cod_aut as cod_aut,
            p.serial as serial_pos
        from
            transactions t
        left join customer c on
            t.cust_id = c.id
        left join pos p on
            t.pos_id = p.id
        where
            extract(month from t.created_at) = {MONTH}
            and t.status = true
    """

    with open('./files/report_' + MONTH + '.csv', 'w', encoding='utf8') as f:
        writer = csv.writer(f)

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

        print('File created with name > ' + 'report_' + MONTH + '.csv')

    connection.close()


if __name__ == '__main__':
    __main__()
