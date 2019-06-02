import sqlite3
from browser import d

db_name = 'CRYPTO_COIN'
fields = ('crpt_names', 'crpt_values')

def upd_db():
    conn = sqlite3.connect('crypto.sqlite')
    cur = conn.cursor()
    cur.execute('DELETE FROM {0}'.format(db_name))
    for i in range(1, len(d)+1):
        cur.execute('INSERT INTO {} ({}, {}) VALUES (?, ?)'.format(db_name, fields[0], fields[1]), (d[i]['crypto_name'], d[i]['crypto_price']))
    conn.commit()  
    cur.close()

upd_db()




