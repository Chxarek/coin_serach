import sqlite3, re, json
from db_crypto_currency import db_name, fields, d, upd_db

qupd_db()            #getting the results from db_crypto_currency.py


number = int(input('Number of coins: '))


def extr_from_db():
    conn = sqlite3.connect('crypto.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT {3} FROM {0} ORDER BY {2} DESC LIMIT {1}'.format(db_name, number, fields[1], fields[0])) #currencies names selection, ordered by value regression
    a1 = cur.fetchall()
    cur.execute('SELECT {2} FROM {0} ORDER BY {2} DESC LIMIT {1}'.format(db_name, number, fields[1], fields[0])) #currencies price values selection, ordered by value regression
    a2 = str(cur.fetchall())        #tupple to string
    a2 = re.findall("[0-9.]+", a2)  #only digits remain, emulating float
    l = []
    for i in range(len(a1)):
        listing = {a1[i][0]: a2[i]}                             # getting data like this: {'Bitcoin': '8734.43'}, {'ThoreCoin': '1328.15'}, {'Maker': '727.12'}
        l.append(listing)                                       # a1[i][0] - getting rid from ',' (tupple type trash)
    with open('crypto(dump).json', 'w') as file_dump:           # writing copy of data to the file
        json.dump(l, file_dump, indent=2, ensure_ascii=False)
    return json.dumps(l, separators=('\n', ':'))                #formatting to json with column type printing

print(extr_from_db())
