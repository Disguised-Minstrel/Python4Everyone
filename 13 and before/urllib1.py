import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://py4e-data.dr-chuck.net/regex_sum_1272533.txt")

size = 0
while True:
    info = fhand.read(2000)
    if len(info) < 1: break
    if 3000 - size > 2000:
        print(info.decode())
    elif 3000 > size:
        print(info.decode()[:3000-size])
    size = size + len(info)

print(size, "characters in a file.")
