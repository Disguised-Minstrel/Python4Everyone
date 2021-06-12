import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_name_rec(url, index):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    print("Retriving:", tags[index].get('href', None))
    return tags[index].get('href', None)

url = input('Enter - ')
count = int(input("Enter count: "))
index = int(input("Enter index: "))
for name in range(count):
    url = get_name_rec(url, index)
