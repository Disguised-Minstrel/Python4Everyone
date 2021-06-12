import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

while True:
    url = input('Enter url: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    tree = ET.fromstring(data)

    lst = tree.findall("comments/comment/count")
    total = 0
    for item in lst:
        total = total + int(item.text)
    print(total)
