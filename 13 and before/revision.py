import re

handle = open('m-box.txt')
total = 0
count = 0

for line in handle:
    line = line.rstrip()
    x = re.findall('^New Revision: ([0-9.]+)', line)
    if x == []:
        continue
    total = total + int(x[0])
    count += 1

print(total // count)
