fhand = None

while fhand == None:
    file_name = input("Enter name of the file: ")
    if file_name == "na na boo boo":
        print("why?")
    try:
        fhand = open(file_name, 'r')
    except:
        print("Invalid filename.")

total = 0
count = 0

for line in fhand:
    if line.startswith("X-DSPAM-Confidence"):
        sub = line[line.find(':')+1:]
        total = total + float(sub.strip())
        count += 1

average = total / count
print("Average spam confidence: %g" % average)
