import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# URL's

sample = 'http://py4e-data.dr-chuck.net/comments_42.xml'
actual = 'http://py4e-data.dr-chuck.net/comments_1879243.xml'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Main

address = actual
print('Retrieving', address)
uh = urllib.request.urlopen(address, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
print(data.decode())
tree = ET.fromstring(data)
counts = tree.findall('.//count')
counts = list(map(lambda x : int(x.text), counts))
print(sum(counts))
