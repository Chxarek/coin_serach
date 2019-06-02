import ssl
import requests, bs4
import json

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


def testing():
    with open('file(dump).json', 'w') as file_dump:
        json.dump(d, file_dump, indent=2, ensure_ascii=False)
        json_str = json.dumps(d, indent=2)
        return json_str
