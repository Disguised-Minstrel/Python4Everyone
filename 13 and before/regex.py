import re

while True:
    filename = input("Enter the filename: ")
    try:
        handle = open(filename)
        break
    except:
        print("Invalid input.")

entire_document = handle.read()
lst = re.findall('[0-9]+', entire_document)
for x in range(len(lst)):
    lst[x] = int(lst[x])
print(sum(lst))
