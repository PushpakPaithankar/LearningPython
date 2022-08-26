strt_num= int(input('Enter the starting number :'))
n= int(input('Enter the number of even numbers to be printed :'))

if strt_num % 2 != 0:
    strt_num=strt_num-1

i=1
print('Even numbers are as follows')
while i<=n:
    strt_num = strt_num+2
    print(strt_num)
    i+=1

