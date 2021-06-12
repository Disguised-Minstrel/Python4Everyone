from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('tr')
total = 0
for tag in tags:
    print(tag)
    text = str(tag)
    numbers = re.findall('[0-9]+', text)
    print(numbers)
    for number in numbers:
        total = total + int(number)
print(total)
