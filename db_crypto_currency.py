import ssl
import requests, bs4
import sqlite3

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://coinmarketcap.com/'                          #connecting and preparing the source data for further transforms
html = requests.get(url)
soup = bs4.BeautifulSoup(html.text, "html.parser")

crypto_dict = []                                              #make some sorting and
cur_price = soup.select('.price, .currency-name-container')   #create unformatted list of currencies with names and price values
for name in cur_price:
    curr = name.get_text()
    crypto_dict.append(curr)

a, b = [], []
c, d = {}, {}
i = 0
while i < len(crypto_dict):                    #adding some format to the list's data:
    if i % 2 != 0:
        a.append(float(crypto_dict[i][1:]))     #making list of prices with stripping $-sign from price value
    else:
        b.append(crypto_dict[i])                #making list of names
    i += 1

for j in range(len(a)):                                            #creating dictionary out from the previous,
     c = {j+1: {'crypto_name': b[j], 'crypto_price': a[j]}}        #containing data like: {1: {'crypto_name': 'Bitcoin', 'crypto_price': 8743.36},...}
     d.update(c)

db_name = 'CRYPTO_COIN'
fields = ('crpt_names', 'crpt_values')


def upd_db():

    conn = sqlite3.connect('crypto.sqlite')
    cur = conn.cursor()
    cur.execute('DELETE FROM {0}'.format(db_name))      #deleting all the previous data every time we make an update
    for i in range(1, len(d) + 1):
        cur.execute('INSERT INTO {} ({}, {}) VALUES (?, ?)'.format(db_name, fields[0], fields[1]),      #filling the db with the updated stuff
                    (d[i]['crypto_name'], d[i]['crypto_price']))
    conn.commit()
    cur.close()


