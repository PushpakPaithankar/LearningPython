# Take user input
a = int(input("Enter a number: "))
print(f"you entered: {a}")

# Enter how many numbers you want to print
b = int(input("How many even numbers you wish to print? "))

# Conditions: while,if, else
i = 0
while (i<b):
    if (a % 2)==0:
        a = a+2
        print(a)
    else:
        print(a+1)
        a = a+1
    i =i+1
