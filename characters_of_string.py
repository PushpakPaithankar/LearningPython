# Enter a string
a = input ("Enter a string: ")

# Show the output back to user
print(f"Your first string is {a} and the characters are: ")

# initialize a variable
i=0

# print the characters
while (i<len(a)):
    print (a[i])
    i=i+1

print(f"Reverse order is {(a[::-1])}")