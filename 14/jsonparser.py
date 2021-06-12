import urllib.request, urllib.parse, urllib.error
import json

while True:
    url = input('Enter url: ')
    if len(url) < 1: break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    print(data.decode())
    info = json.loads(data)
    print(info)
    
    total = 0
    for item in info["comments"]:
        total = total + int(item["count"])
    print(total)
