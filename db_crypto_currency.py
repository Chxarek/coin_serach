import ssl
import requests, bs4
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://coinmarketcap.com/'
html = requests.get(url)
soup = bs4.BeautifulSoup(html.text, "html.parser")

crypto_dict = []
cur_price = soup.select('.price, .currency-name-container')
for name in cur_price:
    curr = name.get_text()
    crypto_dict.append(curr)

a, b = [], []
c, d = {}, {}
i = 0
while i < len(crypto_dict):
    if i % 2 != 0:
        a.append(float(crypto_dict[i][1:]))
    else:
        b.append(crypto_dict[i])
    i += 1

for j in range(len(a)):
     c = {j+1: {'crypto_name': b[j], 'crypto_price': a[j]}}
     d.update(c)

db_name = 'CRYPTO_COIN'
fields = ('crpt_names', 'crpt_values')


def upd_db():

    conn = sqlite3.connect('crypto.sqlite')
    cur = conn.cursor()
    cur.execute('DELETE FROM {0}'.format(db_name))
    for i in range(1, len(d) + 1):
        cur.execute('INSERT INTO {} ({}, {}) VALUES (?, ?)'.format(db_name, fields[0], fields[1]),
                    (d[i]['crypto_name'], d[i]['crypto_price']))
    conn.commit()
    cur.close()


