import sqlite3, re, json
from db_crypto_currency import db_name, fields, d, upd_db

upd_db()


number = int(input('Number of coins: '))


def extr_from_db():
    conn = sqlite3.connect('crypto.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT {3} FROM {0} ORDER BY {2} DESC LIMIT {1}'.format(db_name, number, fields[1], fields[0]))
    a1 = cur.fetchall()
    cur.execute('SELECT {2} FROM {0} ORDER BY {2} DESC LIMIT {1}'.format(db_name, number, fields[1], fields[0]))
    a2 = str(cur.fetchall())
    a2 = re.findall("[0-9.]+", a2)
    l = []
    for i in range(len(a1)):
        listing = {a1[i][0]: a2[i]}
        l.append(listing)
    with open('crypto(dump).json', 'w') as file_dump:
        json.dump(l, file_dump, indent=2, ensure_ascii=False)
    return json.dumps(l, separators=('\n', ':'))

print(extr_from_db())
