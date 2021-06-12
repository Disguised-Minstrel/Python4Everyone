fhand = None

while fhand == None:
    file_name = input("Enter name of the file: ")
    if file_name == "na na boo boo":
        print("why?")
    try:
        fhand = open(file_name, 'r')
    except:
        print("Invalid filename.")

mails = dict()

for line in fhand:
    if line.startswith("From"):
        words = line.split()
        if len(words) < 3:
            continue
        k = words[1]
        mails[k] = mails.get(k, 0) + 1

lst = list()

for k, v in list(mails.items()):
    lst.append((v, k))

lst.sort(reverse=True)
for key, val in lst[:1]:
    print(key, val)
