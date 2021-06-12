fhand = None

while fhand == None:
    file_name = input("Enter name of the file: ")
    try:
        fhand = open(file_name, 'r')
    except:
        print("Invalid filename.")

for line in fhand:
    print(line.strip().upper())
