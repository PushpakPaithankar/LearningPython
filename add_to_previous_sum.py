# Add to previous sum
# input
a= int(input("Enter a number: "))
b= int(input("Enter another number: "))

# define a function to add
def add(a, b):
    return (a + b)
z = add(a,b)

# print
print(f"The sum of {a} and {b} is {z}")

c = int(input("Enter a number to add to previous sum: "))
d = (z+c)
print(f"New sum is {d}")