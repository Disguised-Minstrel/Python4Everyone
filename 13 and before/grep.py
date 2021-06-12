import re

term = input("Enter a regular expression: ")

while True:
    filename = input("Enter name of the file: ")
    try:
        handle = open(filename)
        break
    except:
        print("Invalid filename.")

count = 0

for line in handle:
    line = line.rstrip()
    if re.search(term, line):
        count += 1

print("%s had %d lines that matched %s." % (filename, count, term))
