"""
Title: Meli challenge.
Author: Álvaro Godoy
Date: 2023-03-28
Email: alvarogodoyg@gmail.com
"""

import csv
import time
import db_connection

MONTH = "1"

connection = db_connection.connection
cursor = connection.cursor()


def dummy_loop():
    while True:
        print('Hola')
        time.sleep(5)


def __main__():
    sql = """
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
    """

    with open('./files/reporte_' + MONTH + '.csv', 'w', encoding='utf8') as f:
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

        # results = cursor.execute(sql).fetrchall()

        # for row in results:
        #     writer.writerow(row)

        print('File created ' + 'reporte_' + MONTH + '.csv')

    connection.close()


dummy_loop()
