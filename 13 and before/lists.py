def chop(t):
    del t[0]
    del t[len(t)-1]

def middle(t):
    return t[1:len(t)-1]

numbers = [1, 2, 3, 4]

print(middle(numbers))
print(numbers)
chop(numbers)
print(numbers)
