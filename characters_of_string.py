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

print(f"Your reverse string of {a} is: ")
i=0

# Reverse of previous string
b=a[::-1]
while (i<len(b)):
    print (b[i])
    i=i+1
