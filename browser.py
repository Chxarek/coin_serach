#import socket
#
#mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#mysock.connect(('data.pr4e.org', 80))
#cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
#mysock.send(cmd)
#
#while True:
#    data = mysock.recv(512)
#    if len(data) < 1:
#        break
#    print(data.decode(),end='')
#
#mysock.close()


#import urllib.request, urllib.parse, urllib.error
#
#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#for line in fhand:
#    print(line.decode().strip())


#import urllib.request, urllib.parse, urllib.error
#
#fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#
#counts = dict()
#for line in fhand:
#    words = line.decode().split()
#    for word in words:
#        counts[word] = counts.get(word, 0) + 1
#print(counts)


#import urllib.request, urllib.parse, urllib.error                         #!!!Попробовать что то тут спарсить, поиграться обязательно!!!
#
#fhand = urllib.request.urlopen('https://www.wowprogress.com/')
#for line in fhand:
#    print(line.decode().strip())


#from urllib.request import urlopen
#from bs4 import BeautifulSoup
import ssl
import requests, bs4
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter: ')
url = 'https://coinmarketcap.com/'
html = requests.get(url)
soup = bs4.BeautifulSoup(html.text, "html.parser")

crypto_dict = []
cur_price = soup.select('.price, .currency-name-container')
#print(cur_price)
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

#for i in range(1,5):
#    print(d[i].keys())
#

#print(d[1].keys(), d[1].values())

#for k in range(1,len(d)):
#    print(d[k]['crypto_name'])
#

def testing():
    with open('file(dump).json', 'w') as file_dump:
        json.dump(d, file_dump, indent=2, ensure_ascii=False)
        json_str = json.dumps(d, indent=2)
        return json_str


#e = testing()
#print(e)
#hand = open('file(dump).json')
#r = requests.get('file(dump).json').json()
#print(r)
#for line in hand:
#    print(line).json()
#



