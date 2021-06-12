import socket
import re

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

body = False
while True:
    data = mysock.recv(512)
    content = data.decode()
    of_interest = re.findall('\r\n\r\n([\s\S]*)', content)
#    print(content)
#    print(of_interest)
    if len(data) < 1: break
    if of_interest != []:
        body = True
        print(of_interest[0], end='')
        of_interest = []
    elif body:
        print(content, end='')

mysock.close()
