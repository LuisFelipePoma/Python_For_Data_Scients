# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl

# URL's

sample = 'http://py4e-data.dr-chuck.net/known_by_Fikret.html'
actual = 'http://py4e-data.dr-chuck.net/known_by_Corin.html'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = actual


# Retrieve all of the anchor tags

count = 7
pos = 18 - 1


def retrieve(link, count):
    
    html = urllib.request.urlopen(link, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    data = []
    for tag in tags:
        link = tag.get('href', None)
        nombre = str(tag.contents[0])
        data.append((link, nombre))
    print("Retrieving: ", data[pos][0])
    nombre = data[pos][1]
    if count <= 1:
        return nombre
    return retrieve(data[pos][0], count-1)

name = retrieve(url, count)
print(name)